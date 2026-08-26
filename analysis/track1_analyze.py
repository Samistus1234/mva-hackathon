#!/usr/bin/env python3
"""
Track 1 (Variant Prediction) analysis pipeline for the MVA Hackathon 2026.

Workflow (run from ~/mva-hackathon):
    python3 analysis/track1_analyze.py --vcf data/WGS_EX2312012_HGWCNDSX7.vcf.gz

Phases:
  A. Inspect  - read the VCF header (reference build, chromosome naming, FILTER/INFO).
  B. Extract  - pull every variant overlapping the MVA candidate-gene panel
                (analysis/mva_gene_panel.{chr,nochr}.bed -- auto-picks the
                naming convention the VCF actually uses).
  C. Annotate - send the panel variants to Ensembl VEP REST (GRCh38) in chunks
                of 200; capture gene, impact, consequence, gnomAD AF, ClinVar.
  D. Rank     - score each candidate for causal plausibility in MVA and emit a
                ranked candidate table + a draft submission CSV.

The scoring rules the submission is judged by live in source/evaluation.py:
rank points (100/50/25/10 by rank) + F-max; only exact chrom/pos/ref/alt
matches count, and the answer is a compound-heterozygous pair (MVA is
recessive). This script's output is the raw material; the CSV you actually
submit is curated from candidates.tsv by hand before each of the 6 submissions.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ANALYSIS = ROOT / "analysis"
SUBMISSIONS = ROOT / "submissions"

PANEL_TSV = ANALYSIS / "mva_gene_panel.tsv"
BED_CHR = ANALYSIS / "mva_gene_panel.chr.bed"
BED_NOCHR = ANALYSIS / "mva_gene_panel.nochr.bed"

# Gene prior = how likely biallelic loss in this gene causes classic MVA
# (BUB1B = MVA1 dominant cause; CEP57 = MVA2; BUB1 = MVA3; TRIP13 related).
GENE_PRIOR = {
    "BUB1B": 1.0, "CEP57": 0.9, "BUB1": 0.7, "TRIP13": 0.6, "CASC5": 0.5,
    "BUB3": 0.3, "MAD2L1": 0.3, "MAD2L2": 0.3, "ZW10": 0.3, "ZWINT": 0.3,
    "ANAPC1": 0.25, "PLK1": 0.2, "CDC20": 0.2, "CDC27": 0.2,
}

LOF_TERMS = {"stop_gained", "frameshift_variant", "splice_acceptor_variant",
             "splice_donor_variant", "start_lost", "stop_lost",
             "transcript_ablation"}
SPLICE_TERMS = {"splice_region_variant", "splice_polypyrimidine_tract_variant"}
MISSENSE_TERMS = {"missense_variant", "missense_variant&splice_region_variant",
                  "inframe_deletion", "inframe_insertion"}

# Severity order for choosing the most damaging annotation of a variant.
SEVERITY = ["transcript_ablation", "splice_acceptor_variant",
            "splice_donor_variant", "stop_gained", "frameshift_variant",
            "stop_lost", "start_lost", "missense_variant",
            "inframe_deletion", "inframe_insertion", "protein_altering_variant",
            "splice_region_variant", "splice_polypyrimidine_tract_variant",
            "synonymous_variant"]


def worst_severity(terms: list[str]) -> int:
    best = len(SEVERITY) + 1
    for t in terms:
        for known in SEVERITY:
            if t == known:
                best = min(best, SEVERITY.index(known))
    return best if best <= len(SEVERITY) else 99  # unknown/other => low priority

VEP_URL = "https://rest.ensembl.org/vep/human/region"


def sh(*cmd: str, **kw) -> subprocess.CompletedProcess:
    return subprocess.run(list(cmd), capture_output=True, text=True,
                          timeout=kw.get("timeout", 300), check=True)


# ── Phase A: inspect header ──────────────────────────────────────────────────
def inspect_header(vcf: Path) -> dict:
    out = sh("bcftools", "view", "-h", str(vcf)).stdout
    contigs, info_fields = [], {}
    build = None
    for line in out.splitlines():
        if line.startswith("##contig"):
            contigs.append(line.split("ID=", 1)[1].split(",")[0])
        elif line.startswith("##INFO=<ID="):
            f = line.split("##INFO=<ID=", 1)[1].split(",", 1)[0]
            info_fields[f] = line
        elif line.startswith("##reference"):
            build = line
    chrom_style = "chr" if any(c.startswith("chr") for c in contigs) else "nochr"
    print(f"[A] contigs: {len(contigs)} (sample: {contigs[:4]}...) -> chrom style '{chrom_style}'")
    if build:
        print(f"[A] reference line: {build.strip()}")
    print(f"[A] INFO fields present: {sorted(info_fields)[:25]}")
    return {"contigs": contigs, "chrom_style": chrom_style, "info_fields": info_fields,
            "reference": build}


# ── Phase B: extract panel variants ─────────────────────────────────────────
def extract_panel(vcf: Path, chrom_style: str) -> list[dict]:
    bed = BED_CHR if chrom_style == "chr" else BED_NOCHR
    out = sh("bcftools", "view", "-R", str(bed), str(vcf), "-Ov").stdout
    records = []
    for line in out.splitlines():
        if line.startswith("#"):
            continue
        f = line.split("\t")
        rec = {
            "chrom": f[0], "pos": int(f[1]), "id": f[2], "ref": f[3], "alt": f[4],
            "qual": f[5], "filter": f[6], "info": f[7], "raw": line,
        }
        # keep only simple bi-allelic substitutions/indels we can annotate
        alts = rec["alt"].split(",")
        if len(alts) == 1 and "/" not in rec["alt"] and "*" not in rec["alt"]:
            records.append(rec)
    print(f"[B] {len(records)} panel-gene variant record(s) extracted ({bed.name})")
    return records


# ── Phase C: annotate via VEP REST ───────────────────────────────────────────
def vep_chunk(chunk: list[dict]) -> dict:
    variants = [f"{r['chrom']} {r['pos']} {r['id']} {r['ref']} {r['alt']} . . ."
                for r in chunk]
    body = json.dumps({"variants": variants}).encode()
    req = urllib.request.Request(
        VEP_URL, data=body,
        headers={"Content-Type": "application/json", "Accept": "application/json",
                 "User-Agent": "mva-hackathon-analysis"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))
    return {}


def annotate(records: list[dict]) -> list[dict]:
    """Annotate all records with VEP, chunks in parallel (Ensembl tolerates it;
    serial is ~57s/200 variants, 4 workers ~4x faster)."""
    if not records:
        return []
    from concurrent.futures import ThreadPoolExecutor, as_completed
    chunks = [records[i:i + 200] for i in range(0, len(records), 200)]
    done = [False] * len(chunks)

    def work(i: int):
        try:
            return i, vep_chunk(chunks[i])
        except Exception as e:  # noqa: BLE001
            return i, {"error": str(e)}

    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(work, i) for i in range(len(chunks))]
        for fut in as_completed(futs):
            i, results = fut.result()
            if isinstance(results, dict) and results.get("error"):
                print(f"[C] chunk {i} failed: {results['error']}")
                for r in chunks[i]:
                    r["vep"] = {"gene": None, "impact": None, "terms": [], "loF": False,
                                "gnomad_af": None, "clinvar": None}
                done[i] = True
                continue
            by_input = {}
            for res in results:
                by_input.setdefault(res["input"], []).append(res)
            for r in chunks[i]:
                key = f"{r['chrom']} {r['pos']} {r['id']} {r['ref']} {r['alt']} . . ."
                hits = by_input.get(key) or []
                r["vep"] = summarize_vep(hits[0]) if hits else {"gene": None,
                                                               "impact": None,
                                                               "terms": [], "loF": False,
                                                               "gnomad_af": None,
                                                               "clinvar": None}
            done[i] = True
            print(f"[C] chunk {i}/{len(chunks)} annotated ({sum(done)}/{len(chunks)})", flush=True)
    return records


def summarize_vep(res: dict) -> dict:
    """Pick the most damaging consequence across all transcripts; pull gnomAD
    AF and ClinVar from the colocated-variants block."""
    tc = res.get("transcript_consequences") or []
    if not tc:
        return {"gene": None, "impact": None, "terms": [], "loF": False,
                "gnomad_af": None, "clinvar": None}
    best_tc = min(tc, key=lambda c: worst_severity(c.get("consequence_terms", [])))
    gene = best_tc.get("gene_symbol") or best_tc.get("gene_id")
    terms = best_tc.get("consequence_terms", [])
    impact = best_tc.get("impact")
    loF = bool(set(terms) & LOF_TERMS) or impact == "HIGH"
    gnomad_af = None
    clinvar = None
    for cv in res.get("colocated_variants") or []:
        if gnomad_af is None and cv.get("freq_gnomAD"):
            gnomad_af = cv["freq_gnomAD"]
        if clinvar is None and cv.get("clin_sig"):
            clinvar = cv["clin_sig"]
    return {"gene": gene, "impact": impact, "terms": terms, "loF": loF,
            "gnomad_af": gnomad_af, "clinvar": clinvar}


# ── Phase D: rank ────────────────────────────────────────────────────────────
def score_candidate(r: dict) -> float:
    ann = r.get("vep") or {}
    gene = ann.get("gene") or ""
    prior = GENE_PRIOR.get(gene, 0.05)
    if ann.get("loF"):
        func = 1.0
    elif set(ann.get("terms", [])) & MISSENSE_TERMS:
        func = 0.7
    elif set(ann.get("terms", [])) & SPLICE_TERMS:
        func = 0.6
    else:
        func = 0.3  # intronic/synonymous: low, keep only for completeness
    af = ann.get("gnomad_af")
    if af is None:
        rarity = 0.8   # unknown frequency: investigate, don't discard
    elif af < 0.001:
        rarity = 1.0
    elif af < 0.01:
        rarity = 0.6
    else:
        rarity = 0.1
    return prior * func * rarity


def compound_het_boost(records: list[dict]) -> list[dict]:
    # Two rare coding variants in the SAME gene in trans is the MVA signature.
    genes = {}
    for r in records:
        genes.setdefault((r.get("vep") or {}).get("gene"), []).append(r)
    for gene, rs in genes.items():
        if len(rs) >= 2:
            coding = [r for r in rs if (r.get("vep") or {}).get("impact") not in ("MODIFIER", None)]
            if len(coding) >= 2:
                print(f"[D] compound-het candidate: {gene} has {len(coding)} coding variants")
    return records


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vcf", type=Path, default=DATA / "WGS_EX2312012_HGWCNDSX7.vcf.gz")
    args = ap.parse_args()
    vcf = args.vcf
    if not vcf.exists():
        sys.exit(f"VCF not found: {vcf}\nDownload it first (see analysis/README.md).")

    meta = inspect_header(vcf)
    records = extract_panel(vcf, meta["chrom_style"])
    if not records:
        print("[!] No variants in the panel genes. Widen the panel or check build.")
        return
    records = annotate(records)
    compound_het_boost(records)

    ranked = sorted(records, key=score_candidate, reverse=True)
    out_tsv = ANALYSIS / "candidates.tsv"
    with open(out_tsv, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["rank", "score", "chrom", "pos", "ref", "alt", "qual", "filter",
                    "gene", "impact", "consequence", "loF", "gnomad_af", "clinvar", "raw"])
        for i, r in enumerate(ranked, 1):
            a = r.get("vep") or {}
            w.writerow([i, f"{score_candidate(r):.3f}", r["chrom"], r["pos"], r["ref"],
                        r["alt"], r["qual"], r["filter"], a.get("gene"), a.get("impact"),
                        "/".join(a.get("terms", [])), a.get("loF"), a.get("gnomad_af"),
                        a.get("clinvar"), r["raw"]])
    print(f"\n[D] {len(ranked)} candidates ranked -> {out_tsv}")
    print("    Review analysis/candidates.tsv, curate the top rows into a submission")
    print("    CSV (see analysis/README.md), then validate with analysis/validate_submission.py")


if __name__ == "__main__":
    main()
