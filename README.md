# MVA Hackathon 2026 — Samistus1234

*Rare Disease, Real Kid: The MVA Hackathon 2026* ·
[challenge Space](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026)

One child with **Mosaic Variegated Aneuploidy**. Track 1 asks which variant causes it;
Track 2 asks whether anything can be done about it. This repository holds both.

**Patient data handling.** The WGS VCF and the phenotype document are gated on Hugging
Face and stay local — neither is in this repository, and no read-level data (allelic
depths, quality scores) or patient-derived variant table is published here. What the
repository does contain is the variant *predictions* that constitute the Track 1
submission itself, including the secondary candidates that were submitted and scored, and
the gated dataset's own filename where reproduction commands require it. All challenge
data is deleted within 30 days of challenge close per the data-use terms
(WCG IRB #20252010).

---

## Track 1 — Variant prediction · **submitted, 100 rank points / F-max 1.000**

**Compound-heterozygous *BUB1B* (MVA1)** — a full match against the clinically confirmed
answer key.

| Allele | Position (GRCh38) | Protein | Evidence |
|---|---|---|---|
| 1 | chr15:40209701 T>G | **p.(Leu737Ter)** stop_gained | ClinVar pathogenic (rs759242053); gnomAD ≈ 5×10⁻⁵ |
| 2 | chr15:40220612 T>G | **p.(Asn1002Lys)** missense | absent from gnomAD; PolyPhen probably damaging, SIFT deleterious |

Method: a 14-gene spindle-assembly-checkpoint / centrosome panel, `bcftools` extraction
over GRCh38 panel BEDs, Ensembl VEP REST annotation, then ranking by severity × gene prior
× rarity with compound-het flagging.

```bash
python3 -u analysis/track1_analyze.py --vcf WGS_EX2312012_HGWCNDSX7.vcf.gz
python3 analysis/validate_submission.py submissions/track1_primary.csv
```

`validate_submission.py` checks the CSV against the challenge's own scorer before upload.
Full write-up: [`submissions/track1_report_draft.md`](submissions/track1_report_draft.md).

*Scoring note:* Track 1 matches chrom/pos/ref/alt exactly. The VCF uses no-`chr` contigs
(`15`) while clinical notation is `chr15`, so both notations of the lead pair were
submitted as a formatting hedge.

---

## Track 2 — Drug repurposing

Full analysis in [`track2/`](track2/). Three things there:

**A mechanism-hop tool for undruggable genes.** Ask any drug database what targets BUB1B
and the answer is zero compounds — where most rare-disease repurposing stops.
[`track2/repurpose.py`](track2/repurpose.py) hops through the gene's interaction
neighbourhood instead, and ranks the druggable partners. It takes any gene symbol, so it
runs unchanged on CEP57, TRIP13, or any other undiagnosed case.

**An allele-aware mechanism analysis.** The two alleles are not equivalent: one makes no
protein, the other makes a full-length protein that is destroyed early because the
C-terminal *pseudokinase* fold that holds BUBR1 stable is disrupted. In MVA patients with
this architecture, restoring such protein to wild-type levels fully restores checkpoint
function — the defect is quantity, not quality. That is the therapeutic opening.

**An honest verdict.** All three candidate axes (NAD⁺/SIRT2, senolytics, proteostasis)
were assessed and none is deployable in this child; the report says why, and includes a
section listing the claims we withdrew against primary sources. What we recommend instead
is a measurement-first programme: two cheap patient-cell experiments, each designed to
refute one of our own hypotheses, before any drug is considered.

Report: [`track2/report/samistus1234_track2_report.md`](track2/report/samistus1234_track2_report.md)
· Evidence dossiers: [`track2/evidence/`](track2/evidence/)

---

## Reproducing

Python 3.11+, standard library only for `track2/repurpose.py` (public Open Targets and
DGIdb GraphQL APIs, no key required). Track 1 additionally needs `bcftools` and gated
dataset access.

## Licence

Code MIT. Submission artifacts CC BY 4.0 per challenge rules.
