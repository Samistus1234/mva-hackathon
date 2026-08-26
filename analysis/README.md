# MVA Hackathon 2026 — Track 1 (Variant Prediction) runbook

Everything here is derived from the **official Space source** cloned into `../source/`
(`evaluation.py`, `groundtruth.py`, `tabs/submit_track1.py`, `config.py`, `rules.py`),
not from hearsay.

## The task

One real child with Mosaic Variegated Aneuploidy (MVA). Predict the causal variant(s)
from WGS (VCF + FASTQs) + phenotype. Submit a ranked CSV of up to 10 rows; the answer
key (private `SageBio/mva-hackathon-2026-gt/gold_standard_track1.json`) is
**compound-heterozygous** (MVA is recessive) and "NHS-validated".

## Submission format (exact columns)

```
proband_id,chrom_1,pos_1,ref_1,alt_1,chrom_2,pos_2,ref_2,alt_2,epcr,finding_type,notes
```

- One row per variant **or** compound-het pair. `chrom_2…alt_2` blank for single rows.
- `epcr` in (0,1]; `finding_type` = `primary`/`secondary` (secondary doesn't affect score).
- **Coordinates must be GRCh38.** Matching is exact: `chrom/pos/ref/alt` strings must
  equal the key's, so mirror the VCF's chromosome convention (`chr15` vs `15`).
- Up to 10 rows. Template: `../source/static/templates/track1_submission_template.csv`.

## Scoring (from `source/evaluation.py`)

| Rank | Points |
|---|---|
| 1 | 100 |
| 2–3 | 50 |
| 4–5 | 25 |
| 6–10 | 10 |

- **Full match** (row == whole answer set) → points by rank. **Partial** (1 of 2 het
  alleles) → half points.
- **F-max** = best precision/recall across EPCR thresholds, at variant level.
- Leaderboard: rank_points desc, then F-max. Best of 6 submissions counts.
- Extra rows below the true row never hurt (F-max sweeps thresholds) — use the 10-row
  budget for hedges.

## Strategy

1. **Literature-first:** MVA is caused almost exclusively by biallelic loss in
   `BUB1B` (MVA1, chr15) ≫ `CEP57` (MVA2, chr11) > `BUB1` (MVA3, chr2) / `TRIP13`.
   Panel in `mva_gene_panel.tsv` (GRCh38 coords from Ensembl, 2026-08-26) + BED files.
2. Extract panel variants from the VCF (`track1_analyze.py`), annotate (VEP REST),
   rank by LoF > missense, rarity (gnomAD AF), gene prior.
3. The winning move is the correct compound-het **pair in one row at EPCR 1.0**.
   If only one allele is findable, submit it alone at rank 1 (still 50 pts + F-max 0.667).
4. Iterate across the 6 submission slots; each submission is scored instantly on upload.

## Pipeline

```bash
# 0. once (user):
#    - request access: https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data
#    - create read token, run:  ! hf auth login
# 1. download the VCF-only slice (~317 MB, NOT the 85 GB FASTQs):
bash analysis/download_data.sh
# 2. inspect header + extract + annotate + rank:
python3 analysis/track1_analyze.py --vcf data/WGS_EX2312012_HGWCNDSX7.vcf.gz
# 3. curate candidates.tsv into a submission CSV (10 rows max), then validate
#    with the OFFICIAL parser before uploading:
python3 analysis/validate_submission.py submissions/track1_draft.csv
```

## Rules you must honour (from `tabs/rules.py`)

- 18+, individual HF registration; teams optional.
- No recontacting the family / MVA Society.
- **Delete all data within 30 days of close (24 Oct 2026)** and email
  `RarediseaserealkidMVAhackathon2026@synapse.org` to confirm.
- Submissions are CC BY 4.0. Report (PDF/MD) + public GitHub URL required per submission.
- WCG IRB protocol #20252010.
