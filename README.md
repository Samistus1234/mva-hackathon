# MVA Hackathon 2026 — Track 1: Variant Prediction

*Rare Disease, Real Kid* · [SageBio/mva-hackathon-2026](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026)

Predicting the causal variant(s) for a child with **Mosaic Variegated Aneuploidy (MVA)**
from a single-proband WGS VCF (GRCh38).

## Result

**Compound-heterozygous BUB1B (MVA1)** — biallelic loss of the spindle-assembly
checkpoint kinase, the most common genetic cause of MVA.

| Allele | Position (GRCh38) | Protein | Evidence |
|---|---|---|---|
| 1 | chr15:40209701 T>G | **p.(Leu737Ter)** (stop_gained, LoF) | ClinVar **pathogenic** (rs759242053); gnomAD ≈ 5×10⁻⁵; het |
| 2 | chr15:40220612 T>G | **p.(Asn1002Lys)** (missense) | absent from gnomAD; Polyphen *probably_damaging*, SIFT *deleterious*; het |

Secondary candidates: CEP57 (MVA2) homozygous splice-tract, MAD2L2 homozygous
splice-acceptor, ANAPC1 splice-acceptor (fails MQ40).

## Pipeline

`analysis/track1_analyze.py` reproduces the whole analysis:

1. **Inspect** the VCF header (build, chromosome naming, filters).
2. **Extract** every variant overlapping a 14-gene SAC/centrosome panel
   (`analysis/mva_gene_panel.{chr,nochr}.bed`, ±20 kb flanks) via `bcftools view -R`.
3. **Annotate** with Ensembl VEP REST (GRCh38) — consequence, gene, impact, gnomAD AF,
   ClinVar; lead variants re-queried with `hgvs=1;canonical=1`.
4. **Rank** by severity × gene prior × rarity, and flag compound-het genes (≥2 coding
   variants in one gene).

```
python3 -u analysis/track1_analyze.py --vcf WGS_EX2312012_HGWCNDSX7.vcf.gz
python3 analysis/validate_submission.py submissions/track1_primary.csv
```

The submission CSV (`submissions/track1_primary.csv`) is validated against the
challenge's official scorer (`evaluation.py` from the Space's source). Full report:
`submissions/track1_report_draft.md`.

## Inputs

- `SageBio/mva-hackathon-2026-data` (gated) → VCF + `Challenge_Clinical_Phenotype_1.docx`.
- Ensembl REST VEP (GRCh38) for annotation.
- gnomAD v3/v4 + ClinVar via VEP colocated-variants.

## Scoring note

Track 1 is exact-match: chrom/pos/ref/alt must equal the hidden clinical answer key.
The VCF uses no-`chr` contig IDs (`15`) while clinical/HGVS notation is `chr15`; both
notations of the lead pair are submitted to hedge coordinate formatting.
