#!/usr/bin/env python3
"""Resolve GRCh38 coordinates for the MVA candidate-gene panel via Ensembl REST.

Writes analysis/mva_gene_panel.tsv (one row per gene) and flushes each row as
it resolves, so a partial run still leaves a usable file. Ensembl names
chromosomes without the 'chr' prefix (e.g. "15"); the VCF may differ -- the
pipeline normalises when extracting.
"""
import json
import os
import subprocess
import sys
import time

GENES = ["BUB1B", "CEP57", "BUB1", "TRIP13", "BUB3", "MAD2L1", "MAD2L2",
         "ZW10", "ZWINT", "CASC5", "ANAPC1", "PLK1", "CDC20", "CDC27"]

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mva_gene_panel.tsv")


def fetch(gene: str):
    url = (f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene}"
           "?content-type=application/json")
    for attempt in range(4):
        try:
            r = subprocess.run(
                ["curl", "-s", "--max-time", "20", "-H", "User-Agent: mva-hackathon-analysis", url],
                capture_output=True, text=True, timeout=25)
            if r.returncode == 0 and r.stdout.strip():
                d = json.loads(r.stdout)
                return (d["display_name"], d["seq_region_name"], d["start"],
                        d["end"], d["strand"], d.get("assembly_name")), None
            time.sleep(1.5 * (attempt + 1))
        except Exception as e:  # noqa: BLE001
            time.sleep(1.5 * (attempt + 1))
            last_err = repr(e)
    return None, last_err if "last_err" in dir() else "empty-response"


def main() -> int:
    rows = []
    with open(OUT, "w") as f:
        f.write("gene\tchrom\tstart\tend\tstrand\tassembly\n")
        for g in GENES:
            rec, err = fetch(g)
            if err:
                line = f"{g}\tERROR\t{err}"
                rows.append(None)
            else:
                line = "\t".join(str(x) for x in rec)
                rows.append(rec)
            print(line, flush=True)
            f.write(line + "\n")
            f.flush()
    ok = sum(1 for r in rows if r)
    print(f"\n{ok}/{len(rows)} genes resolved -> {OUT}", flush=True)
    return 0 if ok == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
