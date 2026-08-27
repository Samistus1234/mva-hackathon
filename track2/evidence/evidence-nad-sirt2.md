# Evidence Verification: NAD+/SIRT2 → BUBR1 Stabilization as a Repurposing Strategy in MVA1

**Verifier note.** Every PMID below was resolved through NCBI E-utilities (esearch/efetch) or ClinVar esummary against the live database, and the quantitative claims were pulled from PMC full text, not from abstracts or secondary summaries. Where I could not verify an identifier I say so explicitly. Nothing here is reconstructed from memory.

**Patient context.** Compound heterozygous *BUB1B*: p.Leu737Ter (nonsense) + p.Asn1002Lys (C-terminal missense, within the kinase domain). Phenotype: rhabdomyosarcoma, nephrocalcinosis from birth, short stature, FTT, muscle atrophy, prematurity 32wk, IUGR ~1kg, parental recurrent miscarriage.

---

## 1. Summary evidence table

| # | Claim | Verdict | Primary source | What the source actually says |
|---|---|---|---|---|
| 1a | SIRT2 deacetylates BubR1 and increases BubR1 protein levels/stability | **CONFIRMED** | North BJ et al., *EMBO J* 2014;33(13):1438–53. **PMID 24825348**, PMCID PMC4194088 | SIRT2 maintains **lysine-668 (K668)** of BubR1 deacetylated; CBP acetylates it. K668Q (acetyl-mimic) **enhanced** BubR1 ubiquitylation; K668R (non-acetylatable) **reduced** it. Acetylation at K668 drives BubR1 to proteasomal degradation. **The specific E3 ligase is not identified in the paper.** |
| 1b | The acetylation site is K668 | **CONFIRMED** | Same | Verbatim: "the ability of SIRT2 to maintain lysine-668 of BubR1 in a deacetylated state". |
| 1c | An NAD+ precursor raised BubR1 in vivo | **CONFIRMED, with correction** | Same | The precursor was **NMN (nicotinamide mononucleotide), NOT nicotinamide riboside.** NR does not appear in this paper. Dose: **500 mg/kg/day intraperitoneal × 7 days**, in **wild-type C57BL/6 mice** (3-month and 30-month, NIA Aged Rodent Colony). BubR1 rose clearly **in testes**; in heart it was "difficult to determine" in aged animals. In aged mice, testis BubR1 was **restored to 3-month-old levels**. |
| 1d | The NMN effect is SIRT2-dependent | **CONFIRMED (with a caveat the authors themselves raise)** | Same | 1 mM NMM × 24h induced BubR1 in WT MEFs; induction was "almost completely absent" in *Sirt2*−/− MEFs. But the authors note "we did see a **slight increase** of BubR1 following NMN treatment in *Sirt2*−/− MEFs, suggesting that another sirtuin, or other pathways regulated by NMN, may also be able to influence BubR1 abundance." |
| 1e | NAD+ precursor supplementation **extended lifespan** in BubR1 H/H mice | **REFUTED as stated** | Same | **NMN was never tested for lifespan in BubR1^H/H mice.** Lifespan extension came from **SIRT2 transgenic overexpression** (a genetic, not pharmacological, intervention), in a separate cohort. Conflating the two is the single most common misreading of this paper. |
| 1f | Magnitude of the lifespan effect | **CONFIRMED (numbers exact)** | Same | SIRT2tg;BubR1^H/H vs BubR1^H/H: **+58% median lifespan, +21% maximal lifespan** (n = 31 vs 33, **P = 0.0384**, log-rank). Sex-split: **males +123% median**; **females no change**. Mice "remained small" — dwarfism was not rescued. |
| 2 | NAD+ repletion stabilizes a **missense** BUBR1 protein specifically | **REFUTED / no direct evidence exists** | — | The word "missense" **does not appear anywhere in North et al. 2014.** Only engineered lysine substitutions (K668Q/K668R) modelling acetylation states were tested — not disease variants. No paper found tests NAD+, NMN, NR or SIRT2 on any patient-derived BUBR1 missense protein. **This is an inferential leap and must be labelled as one.** |
| 3a | BubR1 hypomorphic mouse phenotype | **CONFIRMED** | Baker DJ et al., *Nat Genet* 2004;36(7):744–9. **PMID 15208629** | BubR1^H/H express **~10%** of normal BUBR1. Progressive aneuploidy plus progeroid features: **short lifespan, cachectic dwarfism, lordokyphosis, cataracts, loss of subcutaneous fat, impaired wound healing**, meiotic segregation defects and infertility. BUBR1 declines in multiple tissues with natural ageing. |
| 3b | The mouse maps closely to human MVA | **PARTIALLY CONFIRMED — important divergences** | Sieben CJ et al., *J Clin Invest* 2020;130(1):171–88. **PMID 31738183**, PMCID PMC6934189 (erratum *JCI* 2020;130(11):6188) | Allelic series: BubR1^−/− dies by E3.5; BubR1^−/H by P1; BubR1^H/H (~10%) viable. **Crucially: "BubR1^H/H mice are sensitive to carcinogen-induced tumors, but do not live long enough to assess predisposition to spontaneous tumors."** So the mouse does **not** model the spontaneous childhood-cancer risk (RMS/Wilms) that dominates the human phenotype — the exact feature most relevant to this patient. |
| 3c | Genotype-matched mouse (truncating + kinase-domain missense) | **REFUTED as a usable model** | Same | The mouse modelling the human BUBR1^X753/L1012P patient — **BubR1^X753/L1002P — was embryonic lethal**: 0 pups among 388 newborns, 0 at E13.5, viable only at E3.5. The human patient with that same genotype **lived 3.6 months.** Mouse is more severe than human for this allelic architecture. |
| 4a | Human NR safety/PK, dose range | **CONFIRMED** | Conze D, Brenner C, Kruger CL. *Sci Rep* 2019;9(1):9772. **PMID 31278280** | 8-week RCT, overweight healthy adults. NR **100 / 300 / 1000 mg/day** dose-dependently raised whole-blood NAD+ by **22% / 51% / 142%** within 2 weeks, sustained. No flushing; no significant AE difference vs placebo; no LDL elevation; no 1-carbon dysregulation. Industry-funded (ChromaDex). |
| 4b | Human NR in acute illness | **CONFIRMED** | Simic P et al., *BMC Nephrol* 2020;21(1):342. **PMID 32791973** | NR+pterostilbene up to **1000/200 mg twice daily × 2 days** in 24 AKI inpatients: safe, +37% NAD+ overall; **3/20 minor GI side effects**. Note: NRPT, not NR alone; Elysium-affiliated authors. |
| 4c | Human NMN safety/dose | **CONFIRMED** | Yi L et al., *GeroScience* 2023;45(1):29–43. **PMID 36482258** | RCT, 80 healthy middle-aged adults, 60 days, **300 / 600 / 900 mg/day oral NMN**. Dose-dependent NAD+ rise; "no safety issues"; well tolerated to 900 mg/day. Industry-affiliated (Abinopharm). |
| 4d | **PEDIATRIC** NAD+ precursor data | **CONFIRMED — this exists and is the strongest practical finding for this project** | Veenhuis SJG et al., *Mov Disord* 2021;36(12):2951–57. **PMID 34515380**, PMCID PMC9291897 | Open-label NR in **24 ataxia-telangiectasia patients, 17 of them children (<18y)**; classic-phenotype subgroup mean age **10.3y**. Dose **25 mg/kg body weight/day × 4 months**. Ataxia scores improved, IgG rose; **"Adverse effects did not occur."** Open-label, no control arm — authors concede placebo effects cannot be excluded. |
| 4e | NR in a **young child** | **CONFIRMED** | Steinbrücker K et al., *Neuropediatrics* 2023;54(1):78–81. **PMID 36223879** | Single A-T child, NR started at **age 3 years 6 months**, 11 months follow-up. SARA 27→9; GMFM 61→78%; antibiotic use and infection hospitalisations down >90%. **"No adverse effects occurred."** n = 1 case report; authors note development may partly explain motor gains. |
| 4f | NAD+ repletion may fuel tumour growth | **CONFIRMED as a real, documented concern** | Heske CM. *Front Oncol* 2020;9:1514. **PMID 32010616**, PMCID PMC6978772 (NCI Pediatric Oncology Branch) | "Tumor cells have increased requirements for NAD+. Thus, many cancers exhibit an increased reliance on NAD+ production pathways." The entire therapeutic logic of NAMPT inhibitors is to **deplete** NAD+ in tumours — i.e. the oncology field is pushing the dial in the *opposite* direction from this hypothesis. |
| 4g | NR specifically promotes brain metastasis | **CONFIRMED — the paper exists and says this** | Maric T et al., *Biosens Bioelectron* 2023;220:114826. **PMID 36371959** (Epub 2022 Oct 29) | Verbatim: "NR supplementation results in a **significant increase in cancer prevalence and metastases of TNBC to the brain**." Concludes with "the need to personalize their use in certain patient populations." **Caveats a reviewer will raise:** this is primarily a *probe-development* (bioluminescent BiNR) methods paper; the cancer result is a downstream application, one murine TNBC model, not a rhabdomyosarcoma or paediatric model. It is nonetheless the specific paper the field cites for NR-and-metastasis, and it should not be waved away. |
| 4h | Contrary oncology evidence exists | **NOTED** | — | NR has been reported to *suppress* hepatocellular carcinoma progression in mice. Direction of effect appears **tumour-type dependent**. I did not verify a PMID for the HCC paper to primary-source standard — **PMID unverified**; treat as "conflicting reports exist," not as a citable counterweight. |
| 5a | Any clinical trial in MVA patients | **REFUTED — none exists** | ClinicalTrials.gov API v2, queried live | `query.term=mosaic variegated aneuploidy` → **totalCount 0**. `query.term=BUB1B` → **totalCount 0**. There is no registered interventional trial for MVA or targeting BUB1B, anywhere. |
| 5b | Any published attempt to pharmacologically raise BUBR1 in humans | **REFUTED — none found** | — | No human study of any BUBR1-raising agent was identified. All BUBR1-elevation evidence is mouse-genetic (transgenic overexpression) or cell-culture (ectopic cDNA). |

---

## 2. The N1002 / kinase-domain missense question — the load-bearing section

This is where the hypothesis lives or dies, and the evidence is **genuinely supportive but with one serious complication that must not be buried.**

### 2.1 The patient's exact variants in ClinVar (queried live)

| Variant | ClinVar | Classification | Review status | Condition |
|---|---|---|---|---|
| `NM_001211.6(BUB1B):c.2210T>G (p.Leu737Ter)` | UID 533901 | **Pathogenic / Likely pathogenic** | criteria provided, **multiple submitters, no conflicts** | Mosaic variegated aneuploidy syndrome 1 |
| `NM_001211.6(BUB1B):c.3006T>A (p.Asn1002Lys)` | UID 4600147 | **Uncertain significance (VUS)** | criteria provided, **single submitter** | "Inborn genetic diseases" (last evaluated 2025-09-19) |

**Be honest about this in the write-up:** the truncating allele is solidly pathogenic; **p.Asn1002Lys is currently a VUS with a single submitter and is not annotated to MVA in ClinVar.** No published functional study of N1002K was found — PubMed returns **zero** results for `BUB1B AND N1002K` and for `BUB1B AND Asn1002`. Any statement that N1002K is a hypomorphic MVA allele is an inference from its position and from the behaviour of neighbouring kinase-domain variants, not an established fact.

For calibration, the closest characterised residue, **L1012P**, is *also* only "Uncertain significance" in ClinVar (UID 6765) despite a decade of functional data and a mouse model — so VUS status here reflects the thinness of MVA curation, not evidence against pathogenicity.

### 2.2 Missense vs truncating: do missense alleles retain partial function? — **YES, and this is the strongest support the hypothesis has**

**Suijkerbuijk SJ, van Osch MH, Bos FL, Hanks S, Rahman N, Kops GJ. "Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy." *Cancer Res* 2010;70(12):4891–900. PMID 20516114, PMCID PMC2887387.**

This paper studied the exact allelic architecture our patient has. Verbatim from the abstract: **"In patients with biallelic mutations, a missense mutation pairs with a truncating mutation."**

Findings, from full text:

1. **Truncating alleles are effectively null.** "None of the truncated proteins, 386X, 731X and 753X, could be detected in lysates of MVA patient cell lines or in parental controls." Low abundance is "the direct result of the **absence of transcripts** from truncating mutants" — consistent with NMD, which is what we predict for p.Leu737Ter.

2. **Kinase-domain missense alleles make normal mRNA but unstable protein.** Northern blot showed mRNA of I909T, R727C and Y155C was **unaffected**. Cycloheximide chase showed protein turnover of I909T and R727C was **increased ~2-fold** vs wild-type. Full-length missense BUBR1 in patient lines was **decreased 2–6 fold**, and "BUBR1 protein abundance was most severely decreased when mutations occurred **in or near the kinase domain**, but less by a mutation in the N-terminal TPR domain."

3. **The degradation route is proteasomal and chaperone-gated.** HSP90 inhibition (geldanamycin) severely depleted I909T and L1012P but barely touched wild-type; CHX+GA together "removed virtually all mutant BUBR1 protein"; **MG132 prevented the enhanced turnover.** Conclusion: "HSP90 activity is needed for folding of BUBR1 substitution mutants and for preventing their clearance via proteasomal degradation." The mutants are **misfolded, not functionally dead**.

4. **THE KEY RESULT — raising the mutant protein restores function.** Verbatim: **"forced overexpression of the poorly expressed substitution mutants I909T and L1012P to levels comparable to wild-type BUBR1 fully restored the response to nocodazole… This showed that these mutations do not impose significant constraints on BUBR1 function other than affecting overall BUBR1 protein abundance."**

   This is a direct in-cell proof of concept for the entire strategy: for kinase-domain missense alleles, **the defect is quantity, not quality.** Restore the level and you restore mitotic checkpoint function.

5. **But not every missense allele is in that class.** The paper defines **two** classes. Y155C (TPR domain) is a *separation-of-function* allele — it restored chromosome alignment but **failed** to reconstitute checkpoint activity, so more of it would not help. L844F was poorly expressed *and* unable to restore any defect. R550Q and Q921H were functionally indistinguishable from wild-type. **Which class N1002K falls into is unknown and untested.** Position (kinase domain) predicts the tractable "low abundance" class, but this is a prediction.

6. Ectopic wild-type BUBR1 in patient cells induced a 2-fold increase in nocodazole response and "mitotic checkpoint activity was almost fully restored to parental levels" — confirming BUBR1 dysfunction is causal and dose-sensitive.

### 2.3 The complication that cuts against the hypothesis — do not omit this

**Sieben CJ et al., *J Clin Invest* 2020 (PMID 31738183)** modelled L1012P in mouse (L1002P) and found something the 2010 cell work could not see:

> "The only notable difference between the 2 genotypes was the dramatic difference in **PCS** [premature chromatid separation], indicating that **the presence of BUBR1^L1002P protein interferes with the cell's ability to sustain strong bonds between duplicated chromosomes** before anaphase onset."

And:

> "BubR1^H/H and BubR1^H/L1002P mice have quite obvious phenotypic differences **despite an inability to detect differences in overall BUBR1 protein levels** in a broad spectrum of tissues… **BUBR1 allelic effects beyond protein level and aneuploidy contribute to disease heterogeneity.**"

**Read plainly: a kinase-domain missense BUBR1 protein is not simply a dilute wild-type protein. It has its own interfering activity on sister-chromatid cohesion, and the phenotype is not a pure function of total BUBR1 abundance.** A therapy that selectively increases the missense protein pool could in principle increase PCS even while increasing total BUBR1. This is the most serious mechanistic objection to the hypothesis and a reviewer will find it. It is *not* fatal — the same paper found several progeroid phenotypes (growth retardation, lifespan, muscle wasting, cardiac stress sensitivity) were **milder** in H/L1002P than H/H — but it converts "more BUBR1 is straightforwardly good" into "the effect of more mutant BUBR1 is allele-specific and unmeasured for N1002K."

### 2.4 Supporting premise: more BUBR1 is beneficial (in mice, genetically)

Baker DJ et al., *Nat Cell Biol* 2013;15(1):96–102. **PMID 23242215.** Transgenic sustained high-level BubR1 expression preserved genomic integrity, reduced tumorigenesis even against oncogenic Ras, corrected checkpoint and microtubule–kinetochore attachment defects, and extended lifespan. This is the cleanest evidence that raising BUBR1 is *desirable* — but it raises **wild-type** BUBR1 by transgene, which is not what any drug does and not what our patient has available in quantity.

---

## 3. Mechanistic gap analysis — the honest chain

| Link | Status |
|---|---|
| NAD+ declines → BubR1 declines, via SIRT2/K668 | Established in mouse and cells (PMID 24825348) |
| NMN raises NAD+ and raises BubR1 in vivo | Established, **wild-type mice, testes, 7 days, IP** (PMID 24825348) |
| K668 is present in the N1002K protein | Structurally true (full-length protein, K668 ≪ 1002) — **but never tested** |
| Kinase-domain missense BUBR1 is degraded by the proteasome | Established (PMID 20516114) |
| …but via **HSP90-gated misfolding QC**, not via K668 acetylation | Established (PMID 20516114). **These are two different degradation routes.** Whether SIRT2/K668 deacetylation can rescue a *misfolded* mutant is untested and is the central unproven step. |
| Raising a kinase-domain missense BUBR1 to WT levels restores checkpoint function | Established in cells for I909T and L1012P (PMID 20516114) — **not for N1002K** |
| NAD+ repletion achieves that in a patient | **No evidence at any level.** No human, no MVA model, no missense allele. |

The chain has **two unbridged links**, and honesty about both is what will distinguish this submission.

---

## 4. What we can and cannot claim

### We CAN claim (fully sourced)

- SIRT2 deacetylates BubR1 at **K668**, blocking its ubiquitylation and proteasomal degradation; NAD+ decline with age drives BubR1 loss through this axis. (PMID 24825348)
- **NMN** at 500 mg/kg/day IP × 7 days raised NAD+ and **restored testis BubR1 in 30-month-old mice to 3-month-old levels**. (PMID 24825348)
- Genetic SIRT2 overexpression extended median lifespan of BubR1^H/H mice by **58%** (males 123%, females 0%; P = 0.0384). (PMID 24825348)
- In MVA patients with a missense/truncating pair, the truncating allele yields **no detectable transcript or protein**, while the kinase-domain missense allele yields **normal mRNA but ~2-fold accelerated protein turnover** and 2–6× reduced protein. (PMID 20516114)
- **Restoring kinase-domain missense BUBR1 (I909T, L1012P) to wild-type levels fully restored mitotic checkpoint function** — the defect for this class is abundance, not intrinsic function. (PMID 20516114)
- The missense protein's instability is **proteasome-dependent and HSP90-gated** — pharmacologically tractable in principle. (PMID 20516114)
- Human NAD+ precursors are well tolerated: NR to 1000 mg/day × 8 weeks (PMID 31278280); NMN to 900 mg/day × 60 days (PMID 36482258).
- **Paediatric NR exposure data exist**: 25 mg/kg/day × 4 months in 24 A-T patients, 17 of them children, no adverse effects (PMID 34515380); and a single child dosed from **age 3y6m** for 11 months with no adverse effects (PMID 36223879).
- **No clinical trial has ever been registered for MVA or BUB1B** (ClinicalTrials.gov, totalCount 0 for both queries) — the unmet-need argument is airtight.

### We CANNOT claim (and should pre-empt)

- ❌ **"NR/NMN extended lifespan in BubR1 mice."** It did not. **SIRT2 transgenic overexpression** did. NMN was never tested for survival. This is the error most likely to be caught.
- ❌ **"Nicotinamide riboside raised BubR1."** The paper used **NMN**. NR appears nowhere in North et al.
- ❌ **"NAD+ repletion stabilizes mutant/missense BUBR1."** Zero evidence. The word "missense" is absent from the source paper; only K668Q/K668R acetyl-mimetics were tested. **This is the hypothesis, not a finding.**
- ❌ **"The BubR1 hypomorphic mouse models our patient."** It models the *progeroid* half. It does **not** model spontaneous childhood cancer — BubR1^H/H mice "do not live long enough to assess predisposition to spontaneous tumors" (PMID 31738183). Our patient's defining event is a rhabdomyosarcoma.
- ❌ **"A mouse exists with our patient's genotype."** The genotype-matched mouse (**BubR1^X753/L1002P**, truncating + kinase-domain missense) is **embryonic lethal before E13.5** while the equivalent human lived 3.6 months. There is no viable animal model of this allelic architecture.
- ❌ **"N1002K is a known hypomorphic MVA allele."** It is a **ClinVar VUS, single submitter**, not annotated to MVA, with **no functional study in the literature**. Its assignment to the "low abundance, rescuable" class is a **positional inference** from I909T/L1012P.
- ❌ **"Raising total BUBR1 will help."** PMID 31738183 shows allelic effects **beyond protein level**: the L1002P protein actively **interferes with sister-chromatid cohesion** (dramatic PCS increase) at matched total BUBR1. Selectively boosting a missense pool is not mechanistically neutral.
- ⚠️ **Oncology risk must be stated, not minimised.** Tumours are NAD+-avid and the field builds **NAMPT inhibitors to deplete NAD+** in cancer (PMID 32010616, NCI). NR supplementation **increased cancer prevalence and brain metastasis** in a murine TNBC model (PMID 36371959). In a child **who has already had a rhabdomyosarcoma and carries a constitutional chromosomal-instability cancer-predisposition syndrome**, this is the central safety objection to the entire proposal. Counter-evidence in other tumour types exists but I could not verify it to primary-source standard — **PMID unverified**; do not cite it as a rebuttal.

### Framing that survives scrutiny

Present this as a **mechanistically-motivated hypothesis with a defined preclinical path**, never as a ready intervention:

1. The rescuable-class argument (PMID 20516114) is the strongest card — lead with it, because it is a *direct functional demonstration* that raising kinase-domain missense BUBR1 restores checkpoint function.
2. State the NAD+/SIRT2 axis as a **plausible route to that end**, explicitly flagged as never tested on a missense allele.
3. Name the first experiment: patient-derived fibroblasts/LCLs, N1002K protein level and cycloheximide half-life ± NMN/NR ± SIRT2 modulation, with PCS and aneuploidy readouts — the PCS readout specifically addresses the PMID 31738183 objection.
4. Carry the oncology risk in the open, as a stated contraindication requiring surveillance, not a footnote.
5. Note the honest alternative: since the degradation is **HSP90-gated and proteasomal** (PMID 20516114), chaperone/proteostasis modulation is arguably a *more mechanistically direct* target than NAD+ — and does not carry the tumour-NAD+ liability. This strengthens rather than weakens the submission's rigor.

---

## 5. Full citation list (all verified via NCBI E-utilities)

- North BJ, Rosenberg MA, Jeganathan KB, Hafner AV, Michan S, Dai J, Baker DJ, Cen Y, Wu LE, Sauve AA, van Deursen JM, Rosenzweig A, Sinclair DA. SIRT2 induces the checkpoint kinase BubR1 to increase lifespan. *EMBO J*. 2014;33(13):1438–53. **PMID 24825348**. PMCID PMC4194088.
- Suijkerbuijk SJ, van Osch MH, Bos FL, Hanks S, Rahman N, Kops GJ. Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy. *Cancer Res*. 2010;70(12):4891–900. **PMID 20516114**. PMCID PMC2887387.
- Sieben CJ, Jeganathan KB, Nelson GG, Sturmlechner I, Zhang C, van Deursen WH, Bakker B, Foijer F, Li H, Baker DJ, van Deursen JM. BubR1 allelic effects drive phenotypic heterogeneity in mosaic-variegated aneuploidy progeria syndrome. *J Clin Invest*. 2020;130(1):171–88. **PMID 31738183**. PMCID PMC6934189. (Erratum: *J Clin Invest*. 2020;130(11):6188.)
- Baker DJ, Jeganathan KB, Cameron JD, Thompson M, Juneja S, Kopecka A, Kumar R, Jenkins RB, de Groen PC, Roche P, van Deursen JM. BubR1 insufficiency causes early onset of aging-associated phenotypes and infertility in mice. *Nat Genet*. 2004;36(7):744–9. **PMID 15208629**.
- Baker DJ, Dawlaty MM, Wijshake T, Jeganathan KB, Malureanu L, van Ree JH, et al. Increased expression of BubR1 protects against aneuploidy and cancer and extends healthy lifespan. *Nat Cell Biol*. 2013;15(1):96–102. **PMID 23242215**.
- Hanks S, Coleman K, Reid S, Plaja A, Firth H, Fitzpatrick D, et al. Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. *Nat Genet*. 2004;36(11):1159–61. **PMID 15475955**.
- Hanks S, Coleman K, Summersgill B, Messahel B, Williamson D, Pritchard-Jones K, et al. Comparative genomic hybridization and BUB1B mutation analyses in childhood cancers associated with mosaic variegated aneuploidy syndrome. *Cancer Lett*. 2006;239(2):234–8. **PMID 16182441**. (Documents embryonal rhabdomyosarcoma in a biallelic-BUB1B MVA case — directly relevant to this patient.)
- Conze D, Brenner C, Kruger CL. Safety and metabolism of long-term administration of NIAGEN (nicotinamide riboside chloride)… *Sci Rep*. 2019;9(1):9772. **PMID 31278280**. PMCID PMC6611812.
- Simic P, Vela Parada XF, Parikh SM, Dellinger R, Guarente LP, Rhee EP. Nicotinamide riboside with pterostilbene (NRPT) increases NAD+ in patients with acute kidney injury (AKI)… *BMC Nephrol*. 2020;21(1):342. **PMID 32791973**. PMCID PMC7427083.
- Yi L, Maier AB, Tao R, Lin Z, Vaidya A, Pendse S, et al. The efficacy and safety of β-nicotinamide mononucleotide (NMN) supplementation in healthy middle-aged adults… *GeroScience*. 2023;45(1):29–43. **PMID 36482258**. PMCID PMC9735188.
- Veenhuis SJG, van Os NJH, Janssen AJWM, van Gerven MHJC, Coene KLM, Engelke UFH, et al. Nicotinamide riboside improves ataxia scores and immunoglobulin levels in ataxia telangiectasia. *Mov Disord*. 2021;36(12):2951–57. **PMID 34515380**. PMCID PMC9291897.
- Steinbrücker K, Tiefenthaler E, Schernthaner EM, Jungwirth J, Wortmann SB. Nicotinamide riboside for ataxia telangiectasia: a report of an early treated individual. *Neuropediatrics*. 2023;54(1):78–81. **PMID 36223879**.
- Heske CM. Beyond energy metabolism: exploiting the additional roles of NAMPT for cancer therapy. *Front Oncol*. 2020;9:1514. **PMID 32010616**. PMCID PMC6978772.
- Maric T, Bazhin A, Khodakivskyi P, Mikhaylov G, Solodnikova E, Yevtodiyenko A, et al. A bioluminescent-based probe for in vivo non-invasive monitoring of nicotinamide riboside uptake reveals a link between metastasis and NAD+ metabolism. *Biosens Bioelectron*. 2023;220:114826. **PMID 36371959**.
- ClinVar (queried live): BUB1B c.2210T>G p.Leu737Ter, UID 533901, Pathogenic/Likely pathogenic, multiple submitters, MVA1. BUB1B c.3006T>A p.Asn1002Lys, UID 4600147, Uncertain significance, single submitter. BUB1B c.3035T>C p.Leu1012Pro, UID 6765, Uncertain significance.
- ClinicalTrials.gov API v2 (queried live): `mosaic variegated aneuploidy` → 0 studies; `BUB1B` → 0 studies.
