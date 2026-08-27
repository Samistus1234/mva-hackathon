# Evidence Verification — Senolytics as a Therapeutic Axis in MVA1 (BUB1B)

**Verifier role:** independent evidence audit, not advocacy. Verdicts below include refutations of claims in the brief.
**Date of verification:** 2026-08-27. All PMIDs machine-verified against the Europe PMC REST API by exact title match; full texts read via PMC where open access.
**Patient context:** child, compound-het BUB1B (p.Leu737Ter null + p.Asn1002Lys missense), rhabdomyosarcoma (active/prior), nephrocalcinosis, short stature, failure to thrive, muscle atrophy, prematurity 32wk, IUGR.

---

## 1. Summary verdict table

| # | Claim as stated in brief | Verdict | Anchor reference |
|---|---|---|---|
| 1 | Baker DJ et al., **Nature Cell Biology 2011**, INK-ATTAC clearance in BubR1 progeroid mice | **PARTIALLY CONFIRMED — journal and year wrong as cited** | Baker DJ, *Nature* 2011;479:232–236. PMID **22048312** |
| 1b | Clearance extended **lifespan** in BubR1 progeroid mice | **REFUTED** — healthspan only; survival "not substantially extended" | same, PMID 22048312 |
| 2 | Baker DJ et al., *Nature* 2016, naturally occurring p16+ cells shorten healthy lifespan | **CONFIRMED** | *Nature* 2016;530:184–189. PMID **26840489** |
| 3 | Aneuploidy / chromosome missegregation induces senescence in human cells | **CONFIRMED**, with a BUB1-specific human primary-cell paper | PMIDs **27731420**, **28633018**, **30108207** |
| 4a | Zhu Y et al., *Aging Cell* 2015 = founding senolytic paper (D+Q) | **CONFIRMED** | *Aging Cell* 2015;14:644–658. PMID **25754370** |
| 4b | Justice JN 2019 IPF human trial | **CONFIRMED as an n=14 open-label single-arm pilot** — not efficacy evidence | *eBioMedicine* 2019;40:554–563. PMID **30616998** |
| 4c | Hickson LJ 2019 DKD human trial | **CONFIRMED as an n=9 open-label pilot**; note a published **corrigendum** | *eBioMedicine* 2019;47:446–456. PMID **31542391**; corrigendum PMID **31982828** |
| 5 | Fisetin senolytic (Yousefzadeh 2018) | **CONFIRMED** in mice; **no completed published human efficacy trial** | *EBioMedicine* 2018;36:18–28. PMID **30279143** |
| 6a | Dasatinib is FDA-approved in children | **CONFIRMED** — Ph+ CML-CP and Ph+ ALL, **≥1 year of age** | FDA/DailyMed label; approval 2017-11-09 |
| 6b | TKIs impair longitudinal growth in children | **CONFIRMED — strongly, and this is the single biggest problem for this patient** | PMIDs **38497150**, **34309636**; dasatinib US label §5 |
| 7a | Senolytics may help in the setting of prior malignancy | **PARTIALLY CONFIRMED** — preclinical + one adult-survivor phase 2 (no results posted) | PMIDs **27979832**, **33494434**; NCT04733534 |
| 7b | Senescent-cell clearance could be tumour-promoting | **CONFIRMED as a legitimate mechanistic risk**, not confirmed as an observed harm | PMIDs **11544531**, **34389744**, **18516091** |
| 8 | A senolytic has been trialled in a progeroid or CIN syndrome patient / in MVA | **REFUTED — none found. Zero.** | ClinicalTrials.gov search; no pediatric senolytic trial of any kind |

---

## 2. Claim-by-claim detail

### Claim 1 — Baker 2011, INK-ATTAC in BubR1 progeroid mice
**Verdict: PARTIALLY CONFIRMED. The citation in the brief is wrong on journal.**

- Correct citation: **Baker DJ, Wijshake T, Tchkonia T, LeBrasseur NK, Childs BG, van de Sluis B, Kirkland JL, van Deursen JM. "Clearance of p16Ink4a-positive senescent cells delays ageing-associated disorders." *Nature*. 2011;479(7372):232–236. PMID 22048312, PMCID PMC3468323.**
- It is ***Nature***, not *Nature Cell Biology*. The confusion is understandable and worth naming explicitly, because there **is** a separate BubR1 paper in *Nature Cell Biology*: **Baker DJ et al., *Nat Cell Biol* 2008;10(7):825–836, PMID 18516091** — "Opposing roles for p16Ink4a and p19Arf in senescence and ageing caused by BubR1 insufficiency." That 2008 paper used **germline p16 deletion**, not inducible clearance. If the report cites "Nat Cell Biol 2011" a reviewer will read it as a fabricated or conflated citation. Fix it.

**Model:** BubR1 hypomorphic (BubR1^H/H) mice carrying the INK-ATTAC transgene (p16^Ink4a promoter → drug-inducible FKBP–caspase-8). Clearance triggered by AP20187, **0.2 µg/g body weight i.p. every 3 days**.

**Tissues/phenotypes improved:** adipose tissue (fat loss prevented), skeletal muscle (sarcopenia delayed, fibre diameter maintained, exercise capacity improved), eye (cataract onset delayed), and lordokyphosis. Both lifelong clearance (delayed onset) and late-life clearance (attenuated progression of established phenotypes) worked.

**Lifespan — the critical caveat, verbatim from the paper:**
> "Cardiac failure is presumably the main cause of death in BubR1^H/H mice (data not shown), which could explain why the overall survival of AP20187-treated BubR1^H/H;INK-ATTAC mice was **not substantially extended**."

**So: healthspan, not lifespan.** In the exact BubR1 model that is our disease analogue, clearing senescent cells improved the tissues that carry p16 burden and did **not** meaningfully extend survival, because the fatal organ (heart) was not one of the p16-driven compartments. This is directly relevant: it predicts that a senolytic in MVA1 would, at best, address muscle/adipose/growth-adjacent phenotypes — and would **not** be expected to address the thing most likely to kill the patient (cancer).

**Reviewer caveats:** (i) genetic ablation of p16+ cells is not pharmacology — INK-ATTAC is a clean, complete, cell-autonomous kill switch with no off-target kinase inhibition, so it is a *proof of mechanism*, not a *proof of drug*; (ii) BubR1^H/H is a hypomorph (reduced protein), our patient is compound-het null/missense — allelic series matters (see §4); (iii) n and effect sizes are modest and the phenotypes are mouse-specific (lordokyphosis has no human read-out).

### Claim 2 — Baker 2016, Nature
**Verdict: CONFIRMED.**

**Baker DJ, Childs BG, Durik M, Wijers ME, Sieben CJ, Zhong J, et al. "Naturally occurring p16Ink4a-positive cells shorten healthy lifespan." *Nature*. 2016;530(7589):184–189. PMID 26840489, PMCID PMC4845101.**

- Background: **normal/wild-type mice** (two cohorts: mixed 129Sv/C57BL/6/FVB and congenic C57BL/6) carrying INK-ATTAC — i.e. *not* progeroid.
- **Median lifespan increased 27% (mixed) and 24% (C57BL/6)**; sex-specific increases 17–35%.
- Organs improved: kidney (reduced glomerulosclerosis, attenuated BUN rise), heart (preserved cardiomyocyte number, maintained stress tolerance via Sur2a), adipose (fat mass and adipocyte size preserved).
- **Tumours:** no change in macroscopic tumour incidence or spectrum at autopsy; **increased tumour latency**. Median lifespan extension in mice dying *without* tumours was 24–42%, so the longevity gain was **not** attributable to cancer protection.
- Authors' own caveats: clearance was **partial and tissue-selective** (ineffective in liver and colon); repeated vehicle injection may have confounded C57BL/6 male longevity; maximum-lifespan extension inconsistent across backgrounds.

**Why this matters for us, honestly:** the 24–27% lifespan number everyone quotes comes from **normal-ageing mice, not the BubR1 model.** The BubR1 model — the one that is actually our disease — is the one where lifespan did *not* move. Presenting the 2016 number next to a BUB1B patient without that distinction would be an overclaim, and a sharp reviewer will catch it.

### Claim 3 — Aneuploidy → senescence in human cells
**Verdict: CONFIRMED. Direct human-cell evidence exists, and one paper uses BUB1 knockdown specifically.**

1. **Andriani GA, Almeida VP, Faggioli F, Mauro M, Tsai WL, Santambrogio L, Maslov A, Gadina M, Campisi J, Vijg J, Montagna C. "Whole Chromosome Instability induces senescence and promotes SASP." *Sci Rep*. 2016;6:35218. PMID 27731420, PMCID PMC5059742.**
   The most on-point paper for this project. **Human primary fibroblasts** with siRNA knockdown of the **SAC component BUB1** (and separately the cohesin SMC1A). Result: significant correlation between the fraction of non-diploid cells and senescence-associated features; W-CIN induced DNA double-strand breaks, oxidative stress, and a **SASP**. This is the closest published mechanistic mirror of MVA1 biology in human cells — weakened SAC → aneuploidy → senescence + SASP.

2. **Santaguida S, Richardson A, Iyer DR, M'Saad O, Zasadil L, Knouse KA, Wong YL, Rhind N, Desai A, Amon A. "Chromosome mis-segregation generates cell-cycle-arrested cells with complex karyotypes that are eliminated by the immune system." *Dev Cell*. 2017;41(6):638–651.e5. PMID 28633018, PMCID PMC5536848.**
   Missegregation → further genomic instability → cell-cycle arrest; arrested cells show **senescence features and a pro-inflammatory secretome** that drives their **immune clearance** (NK-cell mediated). Important nuance for us: the physiological fate of these cells is *immune surveillance*, not indefinite persistence.

3. **He Q, Au B, Kulkarni M, Shen Y, Lim KJ, et al. (Crasta KC). "Chromosomal instability-induced senescence potentiates cell non-autonomous tumourigenic effects." *Oncogenesis*. 2018;7(8):62. PMID 30108207, PMCID PMC6092349.**
   CIN-induced senescent cells exert **non-cell-autonomous pro-tumourigenic effects** on neighbours via the SASP. This is the strongest published rationale *for* clearing them in a CIN syndrome — and simultaneously a reminder that the SASP is the pathogenic entity, which senomorphics could also target.

**Reviewer caveats:** all three are *in vitro* / cell-line systems using acute experimental missegregation (siRNA, Mps1 inhibitors, nocodazole washout). None studies constitutional, lifelong, germline-driven mosaic aneuploidy in a human patient. The inferential leap from "acute BUB1 knockdown in cultured fibroblasts senesces" to "this child's tissues carry a clinically meaningful, druggable senescent-cell burden" is **unmeasured**. No published study has quantified p16/p21/SA-β-gal burden in MVA patient tissue. That is a real gap and should be stated as one — ideally as the first proposed experiment rather than an assumed premise.

### Claim 4 — Dasatinib + quercetin (D+Q)

**4a. Founding paper — CONFIRMED.**
**Zhu Y, Tchkonia T, Pirtskhalava T, Gower AC, Ding H, Giorgadze N, et al. "The Achilles' heel of senescent cells: from transcriptome to senolytic drugs." *Aging Cell*. 2015;14(4):644–658. PMID 25754370, PMCID PMC4531078.**
Established the senolytic concept: senescent cells upregulate pro-survival ("SCAP") networks; silencing key nodes (ephrins, PI3Kδ, p21, BCL-xL, PAI-2) kills senescent but not proliferating/quiescent cells. **Dasatinib** preferentially killed senescent human **preadipocytes**; **quercetin** preferentially killed senescent human **endothelial cells** and mouse BM-MSCs — hence the combination. In vivo, D+Q reduced senescent-cell burden in chronologically aged, radiation-exposed, and progeroid mice.
*Caveat: cell-type-selective senolysis is a documented feature, not a bug — no senolytic clears all senescent cells, and neither drug has been shown to clear senescent myoblasts, renal tubular cells, or growth-plate chondrocytes, which are the compartments that matter for this patient.*

**4b. IPF — CONFIRMED, and it is precisely as weak as feared.**
**Justice JN, Nambiar AM, Tchkonia T, LeBrasseur NK, Pascual R, Hashmi SK, et al. "Senolytics in idiopathic pulmonary fibrosis: results from a first-in-human, open-label, pilot study." *eBioMedicine*. 2019;40:554–563. PMID 30616998, PMCID PMC6412088.**
- Design: **open-label, single-arm, no placebo, two centres. n = 14**, mean age 70.8y, stable IPF.
- Dosing: dasatinib 100 mg/day + quercetin 1250 mg/day, **3 consecutive days/week × 3 weeks = 9 dosing days**. Follow-up 5–7 days post-treatment.
- Primary endpoints were **retention and assessment-completion rates** — i.e. feasibility, *not* efficacy. 100% retention; assessments completed in 13/14.
- Secondary: 6MWD **+21.5 m (p=0.012)**; 4-m gait speed **+0.12 m/s (p=0.024)**; chair-stand time **−2.2 s (p=0.013)**. **Pulmonary function (FEV₁, FVC) unchanged (p>0.05).**
- Safety: **67 non-serious AEs**, 1 SAE (possible pneumonia with hospitalisation, post-intervention).
- Authors' stated limitations, verbatim: "single-arm open-label design is absence of a standard of care or placebo control arm"; senescent-cell clearance could not be measured in lung; circulating SASP results "were inconclusive"; "follow-up period is too short and the sample size too modest."

**The follow-up RCT is essentially null and must be cited alongside it.**
**Nambiar A, Kellogg D, Justice J, Goros M, Gelfond J, et al. "Senolytics dasatinib and quercetin in idiopathic pulmonary fibrosis: results of a phase I, single-blind, single-center, randomized, placebo-controlled pilot trial on feasibility and tolerability." *eBioMedicine*. 2023;90:104481. PMID 36857968, PMCID PMC10006434.**
- **n = 12 (6 D+Q, 6 placebo)**, same dosing.
- Result: "change in FVC, FEV1, 6MWD, SPPB, fatigability **do not appear to differ meaningfully between the treatment groups**."
- **65 non-serious AEs in the D+Q arm vs 22 on placebo**; sleep disturbance and anxiety disproportionately in D+Q (**4/6 vs 0/6**).
- Conclusion is tolerability/feasibility only.
**Implication: when the 2019 open-label functional gains were tested against placebo, they did not replicate.** Any report that cites Justice 2019's +21.5 m walk distance without Nambiar 2023 is cherry-picking, and a rigour-judged reviewer will treat that as a serious flaw.

**4c. Diabetic kidney disease — CONFIRMED as a mechanistic pilot.**
**Hickson LJ, Langhi Prata LGP, Bobart SA, Evans TK, Giorgadze N, et al. "Senolytics decrease senescent cells in humans: preliminary report from a clinical trial of dasatinib plus quercetin in individuals with diabetic kidney disease." *eBioMedicine*. 2019;47:446–456. PMID 31542391, PMCID PMC6796530. Corrigendum: *eBioMedicine* 2020;52:102595, PMID 31982828.**
- Design: **open-label phase 1, single-arm. n = 9** (+2 for progenitor assays only). Age **68.7 ± 3.1 y (range 55–79)**. eGFR 27.0 ± 2.1.
- Dosing: dasatinib 100 mg/day + quercetin 1000 mg/day (500 mg b.i.d.) × **3 consecutive days**; biopsies at day 14.
- Results (adipose): p16^INK4A+ cells **−35% (p=0.001)**; p21^CIP1+ **−17% (p=0.009)**; SA-β-gal+ **−62% (p=0.005)**; CD68+ macrophages **−28% (p=0.0001)**; crown-like structures **−86% (p=0.001)**. Skin epidermis: p16+ **−20% (p=0.026)**, p21+ **−31% (p=0.016)**.
- Circulating SASP significantly decreased: IL-1α, IL-2, IL-6, IL-9, MMP-2, MMP-9, MMP-12 (all p<0.05).
- Safety: no SAEs, no discontinuations.
- Authors' own words: "The field of senolytics is new… **Fewer than 150 subjects have been treated with these drugs in the context of clinical trials**," and they advise against use "outside the context of clinical trials until more is known about their effects and side effects."

**This is the strongest human evidence that exists, and what it proves is target engagement in adipose and skin — not clinical benefit in any organ.**

**One more honest data point the report should not omit:**
**Farr JN, Atkinson EJ, Achenbach SJ, Volkman TL, et al. "Effects of intermittent senolytic therapy on bone metabolism in postmenopausal women: a phase 2 randomized controlled trial." *Nat Med*. 2024;30(9):2605–2612. PMID 38956196, PMCID PMC11705617.**
The best-powered senolytic RCT to date (n=60, 20 weeks). **Primary endpoint negative**: change in CTx did not differ (D+Q −4.1% vs control −7.7%, **p=0.611**). P1NP rose transiently at 2 wk (+16%, p=0.020) and 4 wk (+16%, p=0.024) but not at 20 weeks. **This is directly relevant to us because it is a bone/skeletal endpoint** — the tissue axis closest to this patient's growth failure — and D+Q did not move it.

### Claim 5 — Fisetin
**Verdict: CONFIRMED in mice; human efficacy UNPROVEN.**

**Yousefzadeh MJ, Zhu Y, McGowan SJ, Angelini L, Fuhrmann-Stroissnigg H, et al. "Fisetin is a senotherapeutic that extends health and lifespan." *EBioMedicine*. 2018;36:18–28. PMID 30279143, PMCID PMC6197652.**
- Of 10 flavonoids screened, fisetin was the most potent senolytic.
- Acute/intermittent dosing in progeroid and old mice reduced senescence markers in multiple tissues ("hit-and-run" kinetics).
- Chronic late-life administration to wild-type mice improved tissue homeostasis, suppressed age-related pathology, and **extended median and maximum lifespan**.

**Human status:** no completed, published, peer-reviewed efficacy trial. Ongoing/registered work includes AFFIRM (NCT03430037, frailty in older women, fisetin 20 mg/kg/day × 2 days), STOP-Sepsis (NCT05758246, protocol published in *Trials* 2024), COVID-FIS (NCT04537299), and a pilot in multimorbidity (NCT06431932). **As of this verification no fisetin trial has reported a positive clinical efficacy endpoint in humans.**

**Fisetin's relevance for a paediatric candidate:** it is the *only* senolytic in the mainstream set that is a dietary flavonoid rather than a kinase inhibitor, so it carries none of the TKI growth-plate liability described in §6. That makes it the more defensible candidate for this patient on safety grounds — while being the weaker candidate on evidence grounds. This tension should be stated openly rather than resolved by assertion.

### Claim 6 — PAEDIATRIC SAFETY OF DASATINIB. **This is the section that undermines the lead candidate, and it should be reported at full strength.**

**Approval status — CONFIRMED.** FDA granted regular approval **9 November 2017** for paediatric Ph+ CML in chronic phase (priority review + orphan designation), based on 97 paediatric patients across a phase 1 dose-ranging and a phase 2 trial. Current US label indications cover **paediatric patients ≥1 year of age** with Ph+ CML-CP and, in combination with chemotherapy, newly diagnosed Ph+ ALL.

**Paediatric dosing (current US label, weight-banded, once daily):**

| Body weight | Dose |
|---|---|
| 10 to <20 kg | 40 mg |
| 20 to <30 kg | 60 mg |
| 30 to <45 kg | 70 mg |
| ≥45 kg | 100 mg |

(The 2017 approval press material quotes 30–45 kg = 75 mg; the current label says **70 mg**. Use the label. Trial dosing was ~60 mg/m²/day.) Label: **"Do not crush, cut or chew tablets. Swallow tablets whole."** No suspension formulation. Dispersed-in-juice administration was studied and showed **36% lower bioavailability** — a genuine practical problem for a small child with failure to thrive.

**GROWTH TOXICITY — the disqualifying signal.**

Dasatinib US label, Warnings & Precautions, *Effects on Growth and Development in Pediatric Patients*, verbatim:
> "In pediatric trials of dasatinib in chronic phase CML after at least 2 years of treatment, adverse reactions associated with bone growth and development were reported in **5 (5.2%) patients, one of which was severe in intensity (Growth Retardation Grade 3)**. These 5 cases included cases of **epiphyses delayed fusion, osteopenia, growth retardation, and gynecomastia**. Of these 5 cases, 1 case of osteopenia and 1 case of gynecomastia resolved during treatment."

The label instructs that **bone growth and development should be monitored in paediatric patients**.

Class-level evidence is considerably stronger than the dasatinib label alone suggests:

- **Stiehler S, Sembill S, Schleicher O, Marx M, et al. "Imatinib treatment and longitudinal growth in pediatric patients with chronic myeloid leukemia: influence of demographic, pharmacological, and genetic factors in the German CML-PAED cohort." *Haematologica*. 2024;109(8):2555–2563. PMID 38497150, PMCID PMC11290534.**
  n = 94 paediatric CML patients. **Median height SDS change −0.35 at 12 months and −0.76 at 24 months.** Decline more pronounced prepubertally at 12 months (median Δ height SDS **−0.61 prepubertal vs −0.30 pubertal**), converging by 24 months (−0.55 vs −0.50). Height-velocity SDS improved from −1.86 at month 6 to −0.82 at month 24 — still subnormal. **Only 18% of patients showed adequate individual growth (Δ height SDS ≥0) between months 12–18.**

- **Hijiya N, Maschan A, Rizzari C, Shimada H, Dufour C, et al. "A phase 2 study of nilotinib in pediatric patients with CML: long-term update on growth retardation and safety." *Blood Adv*. 2021;5(14):2925–2934. PMID 34309636, PMCID PMC8341357.** Confirms growth retardation as a recognised, monitored, class-level TKI toxicity in children requiring long-term follow-up.

- Mechanism is off-target and directly relevant: TKIs non-selectively inhibit **c-KIT, PDGFR-α/β, and c-FMS**, which are expressed by osteoblasts and osteoclasts and are required for normal growth-plate and bone remodelling. Dasatinib is a **broader** multi-kinase inhibitor than imatinib (adds SRC-family kinases), so there is no pharmacological reason to expect it to be gentler on the growth plate.

**Honest conclusion on claim 6, stated plainly:** the dominant, best-evidenced senolytic in the literature is a drug whose signature paediatric toxicity is **impaired longitudinal growth and delayed epiphyseal fusion**, in a patient whose two most prominent non-oncological problems are **short stature and failure to thrive**. The toxicity and the phenotype are the same axis. Prepubertal children are the most affected subgroup, and this patient is prepubertal. This is not a manageable side effect in this context — it is a direct aggravation of the presenting complaint. Any proposal advancing D+Q for this child must either (a) present a growth-protective plan and a hard stopping rule, or (b) drop dasatinib in favour of a non-TKI senolytic. Concealing or minimising this would be the most serious rigour failure available in this report.

### Claim 7 — Oncology: help or harm?

**7a. Evidence that senolytics may HELP after cancer therapy — PARTIALLY CONFIRMED (preclinical + one unreported adult trial).**

- **Demaria M, O'Leary MN, Chang J, Shao L, Liu S, et al. "Cellular senescence promotes adverse effects of chemotherapy and cancer relapse." *Cancer Discov*. 2017;7(2):165–176. PMID 27979832, PMCID PMC5296251.** Chemotherapy induces therapy-induced senescence (TIS) in normal murine and human cells; in a transgenic tracking/ablation model, persistent TIS cells drove local and systemic inflammation, and **eliminating TIS cells reduced bone marrow suppression, cardiac dysfunction, cancer recurrence, and loss of physical activity/strength.** This is the strongest conceptual case for senolytics *after* cytotoxic therapy — relevant since this patient has received RMS treatment.
- **Sarcoma-specific: Lafontaine J, Cardin GB, Malaquin N, Boisvert JS, Rodier F, et al. "Senolytic targeting of Bcl-2 anti-apoptotic family increases cell death in irradiated sarcoma cells." *Cancers (Basel)*. 2021;13(3):386. PMID 33494434, PMCID PMC7866159.** Irradiated soft-tissue sarcoma cultures undergo TIS; adding **venetoclax (ABT-199) or navitoclax (ABT-263)** after irradiation induced rapid apoptosis in the senescent fraction. **Note carefully: this works with BCL-2/BCL-xL inhibitors, not with D+Q, and it is cell-culture data.**
- **Closest human trial: NCT04733534, "SEN-SURVIVORS."** Sponsor **St. Jude Children's Research Hospital**; **Phase 2**; status **active, not recruiting**; actual enrolment **110**; **eligibility ≥18 years, adults only**; two arms — D+Q (dasatinib 100 mg/day + quercetin 500 mg b.i.d. on days 1–3 and 30–32) and fisetin (20 mg/kg/day on days 1, 2, 30, 31); primary outcomes change in walking speed and blood CD3+ p16^INK4A abundance; **no results posted.**
  **This is the single most instructive fact for our risk framing: the world's leading paediatric oncology centre is testing senolytics in survivors of childhood cancer — and set the minimum age at 18. They deliberately did not enrol children.**

**7b. Evidence that clearing senescent cells could be TUMOUR-PROMOTING — CONFIRMED as a mechanistic risk.**

- Senescence is a *bona fide* tumour-suppressive barrier: oncogene-induced senescence (OIS) is an intrinsic anti-cancer mechanism, and loss of p16^INK4A is one of the most frequent lesions in human cancer.
- **Sharpless NE, Bardeesy N, Lee KH, Carrasco D, Castrillon DH, Aguirre AJ, et al. "Loss of p16Ink4a with retention of p19Arf predisposes mice to tumorigenesis." *Nature*. 2001;413(6851):86–91. PMID 11544531.**
  *(Verification note: this is PMID **11544531**, not 11544530. 11544530 is the adjacent Krimpenfort melanoma paper in the same issue. Do not transpose these.)*
  p16^Ink4a-specific knockout mice (p19^Arf intact) are **tumour-prone**. Removing p16 function is oncogenic in mice.
- **Rhabdomyosarcoma-specific and directly on point: Li JJ, Kovach AR, DeMonia M, Slemmons KK, et al. "Expression of oncogenic HRAS in human Rh28 and RMS-YM rhabdomyosarcoma cells leads to oncogene-induced senescence." *Sci Rep*. 2021;11(1):16505. PMID 34389744, PMCID PMC8363632.** In human RMS cells, growth inhibition is mediated by **oncogene-induced senescence**, associated with increased RB-pathway activity and **p16 and p21 expression**. In other words: **in this patient's own tumour type, p16/p21-marked senescence is a demonstrated tumour-restraining program.** A senolytic is, by construction, a drug that kills p16/p21-high cells.
- The BubR1 literature compounds this. **Baker DJ et al., *Nat Cell Biol* 2008, PMID 18516091** established that in BubR1-insufficient mice **p16 is the effector of senescence/ageing while p19^Arf is an attenuator** — the Cdkn2a locus is doing opposing jobs in the very genotype we are targeting. And BubR1 hypomorphic mice are **predisposed to carcinogen-induced cancers**; MVA patients are cancer-prone by definition (Wilms tumour surveillance with renal ultrasound every 3–4 months to age 5 is standard of care in BUB1B-confirmed MVA).

**Balancing evidence (do not overstate the harm either):** Baker 2016 (PMID 26840489) found that lifelong INK-ATTAC clearance in normal mice **did not increase tumour incidence** and in fact **increased tumour latency**. So the theoretical harm has not been observed in the cleanest long-term in vivo clearance experiment. The honest statement is: **mechanistically plausible, not empirically demonstrated, and never tested in a cancer-predisposed host.** Nobody has run a senolytic in an animal or human with a germline chromosome-instability cancer-predisposition syndrome.

### Claim 8 — Has a senolytic ever been trialled in a progeroid or CIN syndrome, or in MVA?
**Verdict: REFUTED. No. Report this plainly.**

- **No senolytic trial in MVA.** None registered, none published.
- **No senolytic trial in any progeroid syndrome.** Human HGPS therapeutics are farnesylation-directed (lonafarnib ± pravastatin + zoledronic acid, NCT00879034); progeroid mice (HGPS, XFE) are used as *preclinical models* to test senolytics, which is the opposite direction of evidence flow.
- **No senolytic trial in any chromosome-instability syndrome** (ataxia-telangiectasia, Bloom, Fanconi, Rothmund-Thomson, etc.).
- **No senolytic trial in any paediatric population, for any indication.** Every registered D+Q / fisetin trial identified sets a minimum age of 18 or higher (SEN-SURVIVORS ≥18; AFFIRM older women; DKD 55–79; IPF ~70; osteoporosis postmenopausal). The paediatric senolytic evidence base is **empty**.
- Existing MVA-relevant animal work is descriptive, not therapeutic: **Wijshake T, Malureanu LA, Baker DJ, Jeganathan KB, van de Sluis B, van Deursen JM. "Reduced life- and healthspan in mice carrying a mono-allelic BubR1 MVA mutation." *PLoS Genet*. 2012;8(12):e1003138. PMID 23300461, PMCID PMC3531486**; and **Sieben CJ, Jeganathan KB, Nelson GG, Sturmlechner I, et al. "BubR1 allelic effects drive phenotypic heterogeneity in mosaic-variegated aneuploidy progeria syndrome." *J Clin Invest*. 2020;130(1):171–188. PMID 31738183, PMCID PMC6934189** — the latter is important because it establishes that **specific BUB1B allele combinations produce materially different phenotypes**, which cuts against extrapolating from the BubR1^H/H hypomorph to a null/missense compound heterozygote.

---

## 3. What we CAN claim

1. **The mechanistic chain is real and citable end-to-end.** Weakened SAC → chromosome missegregation → aneuploidy → senescence with SASP is documented in **human primary cells with BUB1 knockdown specifically** (PMID 27731420), corroborated by two independent groups (PMIDs 28633018, 30108207).
2. **Senescent cells are causally, not merely correlatively, involved in degenerative phenotypes.** Genetic clearance improves adipose, skeletal muscle and lens phenotypes **in a BubR1 hypomorphic mouse — the closest available animal model of our patient's gene** (PMID 22048312), and extends median lifespan 24–27% in normal mice (PMID 26840489).
3. **p16 is a validated effector in BubR1 insufficiency specifically** (PMID 18516091) — the target is not borrowed from generic ageing biology; it was nominated in BubR1 biology.
4. **Senolytic drugs engage the target in humans.** D+Q measurably reduces p16+, p21+ and SA-β-gal+ cells in human adipose and skin and lowers circulating SASP (PMID 31542391).
5. **A senolytic-as-post-cancer-therapy rationale exists** and is being tested by a paediatric-oncology sponsor in survivors of childhood cancer (PMID 27979832; NCT04733534).
6. **Fisetin is a genuine senolytic** with mouse lifespan data and no TKI growth-plate liability (PMID 30279143).

## 4. What we CANNOT claim

1. **We cannot claim senolytics extend lifespan in a BubR1 model.** They demonstrably did not (PMID 22048312, verbatim: "not substantially extended"). The 24–27% figure is from **normal** mice. Conflating the two is the most likely single point of reviewer attack.
2. **We cannot claim clinical efficacy of any senolytic in any human disease.** Every human study is a small open-label pilot or a null RCT. The two placebo-controlled results available are **null on efficacy** (IPF, PMID 36857968) and **negative on the primary endpoint** (bone, PMID 38956196).
3. **We cannot claim a measured senescent-cell burden in MVA patients.** No one has quantified p16/p21/SA-β-gal in MVA patient tissue. The therapeutic premise is inferred, not measured.
4. **We cannot claim paediatric safety of any senolytic.** No senolytic has ever been given to a child in a trial, for any indication.
5. **We cannot claim BubR1^H/H mouse results transfer to this genotype.** PMID 31738183 shows BubR1 allelic combinations drive materially divergent phenotypes; a hypomorph is not a null/missense compound heterozygote.
6. **We cannot claim senolytics are oncologically neutral in a cancer-predisposition syndrome.** No senolytic has been tested in a germline CIN cancer-predisposition host, animal or human.
7. **We cannot present D+Q as a paediatric-ready regimen.** No suspension formulation; tablets must not be crushed; dispersion in juice reduces bioavailability 36%.

## 5. Risk register — SPECIFIC TO THIS PATIENT

| Risk | Severity | Evidence | Mitigation / stopping rule |
|---|---|---|---|
| **Dasatinib worsens the presenting phenotype (short stature, FTT).** Growth retardation, epiphyses delayed fusion, osteopenia are labelled paediatric toxicities (5.2%, incl. Grade 3); imatinib cohort data show −0.76 median height SDS at 24 months, worst prepubertally; only 18% grew adequately at 12–18 months. | **CRITICAL — likely disqualifying** | Dasatinib US label §5; PMID 38497150; PMID 34309636 | **Do not propose dasatinib as the lead in this patient.** If retained at all: pre/post growth-plate imaging, height SDS and height-velocity SDS q3mo, bone age, IGF-1, hard stop at Δ height SDS ≤ −0.3. Prefer a non-TKI senolytic. |
| **Removing p16/p21-high cells removes a tumour-suppressive barrier in a cancer-predisposed child with prior RMS.** OIS in human RMS is p16/p21-mediated; p16 loss is tumourigenic in mice; MVA carries standing Wilms surveillance. | **CRITICAL** | PMID 34389744; PMID 11544531; PMID 18516091 | Counterweight: PMID 26840489 showed no increased tumour incidence and increased latency. But this is untested in a CIN host. Any protocol needs intensified tumour surveillance, oncology co-management, and an explicit oncological stopping rule. Cannot be waved away. |
| **Nephrocalcinosis + senolytic renal exposure.** Quercetin and dasatinib have renal handling considerations; the DKD pilot enrolled eGFR ~27 but in adults only, n=9, 3 days. | **HIGH — unquantified in children** | PMID 31542391 (adults only) | Baseline and serial renal function/imaging; renal dosing unknown in paediatrics; treat as an open question, not a solved one. |
| **Skeletal muscle atrophy may not respond.** The BubR1 mouse muscle benefit came from *genetic* ablation. D+Q has never been shown to clear senescent myoblasts, and the only skeletal-endpoint RCT was negative. | **MODERATE — efficacy risk, not safety** | PMID 22048312 vs PMID 38956196 | Pre-specify muscle endpoints; do not assume the mouse result transfers pharmacologically. |
| **No paediatric dosing basis exists for any senolytic.** D+Q paediatric PK unstudied for this indication; fisetin 20 mg/kg is an adult trial dose. Dasatinib tablets cannot be crushed; juice dispersion −36% bioavailability. | **HIGH — practical** | Dasatinib label; NCT03430037, NCT04733534 | Formulation and PK work is a prerequisite, not a detail. |
| **Immune clearance of aneuploid cells is a physiological process that may be disrupted.** Missegregation-derived arrested cells are normally NK-cleared; pharmacological senolysis is not the same as immune surveillance. | **MODERATE — mechanistic uncertainty** | PMID 28633018 | Flag as an unknown; consider whether senomorphic (SASP-suppressing) approaches carry a better risk profile than senolytic killing in this host. |
| **Evidence base is thinner than the enthusiasm suggests.** Fewer than 150 humans total had received senolytics in trials as of 2019 per the investigators themselves; the two controlled trials since are null/negative. | **HIGH — framing risk** | PMID 31542391 (authors' own statement); PMIDs 36857968, 38956196 | State it in the report. A reviewer who finds it themselves will discount everything else. |

**Bottom line for this patient:** the *mechanism* is well-supported and the target nomination in BubR1 biology is legitimate and citable. The *drug* is the problem. Dasatinib's signature paediatric toxicity is the patient's presenting complaint, and senescence in his tumour type is tumour-suppressive. The defensible framing is a **mechanism-first hypothesis with fisetin (or a non-TKI senolytic) as the candidate**, an explicit acknowledgement that no child has ever received a senolytic, and a first proposed experiment that **measures senescent-cell burden in MVA patient cells** rather than assuming it.

---

## 6. Verified reference list (all PMIDs machine-checked)

| PMID | Citation |
|---|---|
| 22048312 | Baker DJ, et al. Clearance of p16Ink4a-positive senescent cells delays ageing-associated disorders. *Nature*. 2011;479:232–236. PMC3468323 |
| 26840489 | Baker DJ, et al. Naturally occurring p16Ink4a-positive cells shorten healthy lifespan. *Nature*. 2016;530:184–189. PMC4845101 |
| 18516091 | Baker DJ, et al. Opposing roles for p16Ink4a and p19Arf in senescence and ageing caused by BubR1 insufficiency. *Nat Cell Biol*. 2008;10:825–836. PMC2594014 |
| 23300461 | Wijshake T, et al. Reduced life- and healthspan in mice carrying a mono-allelic BubR1 MVA mutation. *PLoS Genet*. 2012;8:e1003138. PMC3531486 |
| 31738183 | Sieben CJ, et al. BubR1 allelic effects drive phenotypic heterogeneity in mosaic-variegated aneuploidy progeria syndrome. *J Clin Invest*. 2020;130:171–188. PMC6934189 |
| 27731420 | Andriani GA, et al. Whole Chromosome Instability induces senescence and promotes SASP. *Sci Rep*. 2016;6:35218. PMC5059742 |
| 28633018 | Santaguida S, et al. Chromosome mis-segregation generates cell-cycle-arrested cells with complex karyotypes that are eliminated by the immune system. *Dev Cell*. 2017;41:638–651.e5. PMC5536848 |
| 30108207 | He Q, et al. Chromosomal instability-induced senescence potentiates cell non-autonomous tumourigenic effects. *Oncogenesis*. 2018;7:62. PMC6092349 |
| 25754370 | Zhu Y, et al. The Achilles' heel of senescent cells: from transcriptome to senolytic drugs. *Aging Cell*. 2015;14:644–658. PMC4531078 |
| 30616998 | Justice JN, et al. Senolytics in idiopathic pulmonary fibrosis: first-in-human, open-label, pilot study. *eBioMedicine*. 2019;40:554–563. PMC6412088 |
| 36857968 | Nambiar A, et al. Senolytics D+Q in IPF: phase I randomized placebo-controlled pilot. *eBioMedicine*. 2023;90:104481. PMC10006434 |
| 31542391 | Hickson LJ, et al. Senolytics decrease senescent cells in humans (diabetic kidney disease). *eBioMedicine*. 2019;47:446–456. PMC6796530 |
| 31982828 | Corrigendum to Hickson LJ et al. *eBioMedicine*. 2020;52:102595 |
| 38956196 | Farr JN, et al. Effects of intermittent senolytic therapy on bone metabolism in postmenopausal women: phase 2 RCT. *Nat Med*. 2024;30:2605–2612. PMC11705617 |
| 30279143 | Yousefzadeh MJ, et al. Fisetin is a senotherapeutic that extends health and lifespan. *EBioMedicine*. 2018;36:18–28. PMC6197652 |
| 38497150 | Stiehler S, et al. Imatinib treatment and longitudinal growth in pediatric CML (German CML-PAED). *Haematologica*. 2024;109:2555–2563. PMC11290534 |
| 34309636 | Hijiya N, et al. Phase 2 nilotinib in pediatric CML: long-term update on growth retardation and safety. *Blood Adv*. 2021;5:2925–2934. PMC8341357 |
| 27979832 | Demaria M, et al. Cellular senescence promotes adverse effects of chemotherapy and cancer relapse. *Cancer Discov*. 2017;7:165–176. PMC5296251 |
| 33494434 | Lafontaine J, et al. Senolytic targeting of Bcl-2 anti-apoptotic family increases cell death in irradiated sarcoma cells. *Cancers*. 2021;13:386. PMC7866159 |
| 34389744 | Li JJ, et al. Expression of oncogenic HRAS in human Rh28 and RMS-YM rhabdomyosarcoma cells leads to oncogene-induced senescence. *Sci Rep*. 2021;11:16505. PMC8363632 |
| 11544531 | Sharpless NE, et al. Loss of p16Ink4a with retention of p19Arf predisposes mice to tumorigenesis. *Nature*. 2001;413:86–91. (NOT 11544530) |
| 18548531 | García-Castillo H, et al. Clinical and genetic heterogeneity in patients with mosaic variegated aneuploidy: delineation of clinical subtypes. *Am J Med Genet A*. 2008;146A:1687–1695 |

**Non-PMID sources:** FDA/DailyMed dasatinib (Sprycel) prescribing information (paediatric indications, weight-banded dosing, §5 Effects on Growth and Development); FDA approval announcement 2017-11-09; ClinicalTrials.gov **NCT04733534** (SEN-SURVIVORS, St. Jude, Phase 2, n=110, ≥18y, active-not-recruiting, no results posted), **NCT03430037** (AFFIRM), **NCT05758246** (STOP-Sepsis), **NCT04537299** (COVID-FIS), **NCT06431932**, **NCT00879034** (HGPS lonafarnib).

**Nothing in this document is an unverified PMID.** Where a numeric detail could not be confirmed from a primary source it is marked as such in the text.
