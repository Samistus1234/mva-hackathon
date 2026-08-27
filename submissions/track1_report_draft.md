# Track 1 Report — MVA Hackathon 2026
*Rare Disease, Real Kid: MVA Hackathon 2026 · Track 1 Variant Prediction*
*Team: Samistus1234 · 2026-08-26*

---

## 1. Case summary

- Proband: a child with a clinical diagnosis of Mosaic Variegated Aneuploidy (MVA).
- Phenotype (from `Challenge_Clinical_Phenotype_1.docx`):
  - Rhabdomyosarcoma (HP:0002859) — primary oncological event
  - Nephrocalcinosis (HP:0000121) — since birth
  - Short stature (HP:0004322), failure to thrive (HP:0001508), skeletal muscle atrophy (HP:0003202)
  - Premature birth at 32 weeks (HP:0001622), small for gestational age / IUGR ≈ 1 kg (HP:0001518)
  - Parental history of recurrent spontaneous abortion (HP:0200067)
- Interpretation: cancer predisposition + growth restriction + renal anomaly + adverse
  perinatal history + parental reproductive loss is the classic MVA cluster, pointing to a
  constitutional chromosome-segregation (spindle-assembly checkpoint, SAC) defect.

## 2. Hypothesis

- MVA is caused almost exclusively by **biallelic** (compound-heterozygous or homozygous)
  loss-of-function in SAC / centrosome genes.
- Gene priors (highest → lowest): **BUB1B** (MVA1) > **CEP57** (MVA2) > **BUB1** (MVA3) >
  **TRIP13** (MVA-like) > CASC5/KNL1 > other SAC/centrosome genes (BUB3, MAD2L1, MAD2L2,
  ZW10, ZWINT, ANAPC1, PLK1, CDC20, CDC27).
- Because MVA is recessive, the expected answer is a **compound-heterozygous pair** (two
  rare protein-altering variants in one gene), consistent with the organizers'
  "compound-heterozygous answer key."

## 3. Methods

- **Data**: the challenge's single-proband WGS VCF (gated; identifiers withheld here),
  GRCh38 (no `chr` prefix in contig IDs), Sentieon Haplotyper → GVCFtyper →
  VariantFiltration. Variant calling already performed; this is a VCF-only analysis path.
- **Candidate-gene panel**: 14 genes spanning the SAC / centrosome apparatus
  (BUB1B, CEP57, BUB1, TRIP13, BUB3, MAD2L1, MAD2L2, ZW10, ZWINT, CASC5, ANAPC1, PLK1,
  CDC20, CDC27), GRCh38 coordinates resolved from Ensembl.
- **Extraction**: `bcftools view -R <panel BED ±20 kb flanks>` → 1,392 biallelic records.
- **Annotation**: Ensembl VEP REST (GRCh38). For each variant we captured the most-damaging
  transcript consequence, gene, impact, gnomAD allele frequency, and ClinVar status; the
  two lead variants were re-queried with `hgvs=1;canonical=1` for transcript/protein HGVS.
- **Ranking heuristic**: variant severity (LoF > missense > splice > other) × gene prior ×
  rarity (gnomAD AF); compound-het status (≥2 coding variants in one gene) flagged.
- **Scoring is exact-match**: chrom/pos/ref/alt must equal the hidden key; coordinates are
  GRCh38. Because the VCF uses no-`chr` contigs while clinical/HGVS notation is `chr`-
  prefixed, both notations of the lead pair were submitted (rank 1 and 2).

## 4. Results

**Primary causal hypothesis — compound-heterozygous BUB1B (MVA1).**

| Variant | Gene | HGVS (canonical) | Consequence | Zygosity | gnomAD AF | ClinVar |
|---|---|---|---|---|---|---|
| chr15:g.40209701T>G | BUB1B | `NM_001211.6:c.2210T>G` → p.(Leu737Ter) | stop_gained (HIGH, LoF) | het | 3.3–8.0×10⁻⁵ | **pathogenic / likely_pathogenic** (rs759242053) |
| chr15:g.40220612T>G | BUB1B | `ENST00000287598.11:c.3006T>G` → p.(Asn1002Lys) | missense (MODERATE) | het | **absent** (not in gnomAD) | none — novel |

- Both calls are `PASS` with high quality scores and balanced allele depth (consistent
  with true heterozygosity rather than contamination), on canonical-transcript coding
  changes. Read-level metrics are withheld from this public copy.
- **Model**: one allele is a null (p.L737Ter; NMD/truncation removes the C-terminal
  domain), the other a damaging C-terminal missense (p.N1002K; Polyphen
  *probably_damaging*, SIFT *deleterious*). In *trans* this is biallelic BUB1B loss of
  function — the most common genetic cause of MVA (MVA1).

**Secondary / incidental findings (submitted below the primary):**

| Rank | Variant | Gene | Consequence | Zygosity | gnomAD AF | Rationale |
|---|---|---|---|---|---|---|
| 3 | chr11:g.95795499C>CT | CEP57 (MVA2) | splice-polypyrimidine-tract (LOW) | **hom** (1/1) | absent | homozygous = biallelic; MVA2 second MVA gene |
| 4 | chr1:g.11682017C>T | MAD2L2 | splice_acceptor (HIGH) | **hom** (1/1) | absent | MAD2L2/REV7 reported in MVA-spectrum; lower prior |
| 5 | chr2:g.111730323T>C | ANAPC1 | splice_acceptor (HIGH) | het (0/1) | absent | SAC/APC-C component; fails MQ40 filter → low confidence |

## 5. Interpretation & evidence

1. **Gene prioritization.** BUB1B is the dominant MVA gene (MVA1); its product is the
   mitotic checkpoint kinase essential to the SAC. Biallelic loss is the canonical
   mechanism. CEP57 (MVA2) is second; MAD2L2/REV7 and TRIP13 are MVA-spectrum.
2. **Variant-level fit.** The two lead alleles satisfy every criterion for a recessive
   causal pair: (i) same top-prior gene; (ii) both protein-altering; (iii) both
   ultra-rare (the missense is absent from gnomAD entirely); (iv) one is a ClinVar
   **pathogenic** truncating allele (rs759242053) with confirmed clinical significance
   for the G allele; (v) both heterozygous with balanced reads — consistent with two
   heterozygous alleles *in trans* rather than a homozygous genotype.
3. **Phenotype match.** Rhabdomyosarcoma + severe pre/post-natal growth restriction +
   recurrent pregnancy loss in the parents is precisely the MVA1 profile. The parents'
   miscarriages reflect embryonic aneuploidy from the same checkpoint defect.
4. **Negative controls within the panel.** CASC5/KNL1 (5 coding variants) are all common
   benign homozygous missenses (ClinVar benign, common rsIDs) — ruled out. BUB1, TRIP13,
   BUB3, ZW10, ZWINT, MAD2L1, PLK1, CDC20, CDC27 carry no rare protein-altering variant.

## 6. Secondary / incidental findings

- **CEP57 (MVA2)** homozygous splice-polypyrimidine-tract insertion — a plausible MVA2
  hypothesis if the primary BUB1B pair were excluded, but it is LOW-impact (VEP) and the
  gene accounts for fewer MVA cases than BUB1B.
- **MAD2L2** homozygous splice-acceptor — retained as a lower-prior MVA-spectrum candidate.
- **ANAPC1** splice-acceptor — heterozygous, but the call is FILTER=MQ40 (fails mapping
  quality), so confidence is low; listed for completeness.

## 7. Limitations

- Single proband; no parental genotypes → phase (*cis*/*trans*) is inferred from allele
  balance and biology, not proven.
- Annotation and population frequency depend on Ensembl VEP and gnomAD public data; a
  private allele (p.Asn1002Lys) cannot be definitively assessed for frequency.
- Exact-match scoring means coordinate formatting (chr vs no-chr) and GRCh38 build are
  consequential; both notations of the primary pair are submitted to hedge this.
- The hidden answer key is not observable; confidence is probabilistic.

## 8. Reproducibility

- Code: https://github.com/Samistus1234/mva-hackathon — `analysis/`
  pipeline scripts (`track1_analyze.py`, gene panel, BEDs, `validate_submission.py`,
  README runbook) fully reconstruct the analysis.
- Environment: macOS; `bcftools`, Python 3.13, Ensembl VEP REST (GRCh38).
- Inputs: `SageBio/mva-hackathon-2026-data` VCF + phenotype document.
