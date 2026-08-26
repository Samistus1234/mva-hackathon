#!/usr/bin/env python3
"""
Validate a Track 1 submission CSV before uploading it to the hackathon Space.

Uses the SAME parser the organizers' scorer uses (source/evaluation.py
load_submission + score_proband), so if this passes, the Space will accept it
and return a score rather than a scoring error.

Usage:
    python3 analysis/validate_submission.py submissions/track1_draft.csv
    # optional: score against a known ground truth (normally hidden):
    python3 analysis/validate_submission.py submissions/track1_draft.csv --gt gold_standard_track1.json
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "source"))

from evaluation import load_submission, score_proband  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--gt", type=Path, help="ground-truth JSON (rarely available)")
    args = ap.parse_args()

    if not args.csv.exists():
        sys.exit(f"not found: {args.csv}")

    print(f"== Validating {args.csv} with the official parser ==")
    try:
        by_proband = load_submission(str(args.csv))
    except Exception as e:  # noqa: BLE001
        sys.exit(f"❌ INVALID submission: {e}")

    for pid, rows in by_proband.items():
        print(f"\nProband {pid}: {len(rows)} rows (max 10)")
        for r in rows:
            vs = " + ".join(
                f"{v[0]}:{v[1]} {v[2]}>{v[3]}" for v in sorted(r.variants)
            )
            print(f"  rank {r.rank:>2}  epcr={r.epcr:<5}  {r.finding_type:<9}  {vs}")

    if args.gt:
        import json
        gt = json.loads(args.gt.read_text())
        if isinstance(gt, dict) and "PROBAND01" in gt:
            entry = gt["PROBAND01"]
            tv = frozenset(tuple(v) for v in entry) if isinstance(entry, list) else \
                frozenset((v["chrom"], v["pos"], v["ref"], v["alt"])
                          for v in entry.get("primary_variants", []))
        else:
            tv = frozenset(tuple(v) for v in gt)
        for pid, rows in by_proband.items():
            res = score_proband(pid, rows, tv)
            print(f"\nScore vs provided GT: rank_points={res.rank_points}, "
                  f"f_max={res.f_max:.3f}, full@rank={res.full_match_rank}, "
                  f"partial@rank={res.partial_match_rank}")

    print("\n✅ Format is valid and submit-able.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
