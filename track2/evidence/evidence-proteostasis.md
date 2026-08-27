# Proteostasis Modulation as a Route to Raising Residual BUBR1 in MVA — Evidence Audit

**Scope:** rigorous verification of the hypothesis that, because the patient's BUBR1 p.Asn1002Lys
allele produces a misfolded, chaperone-dependent, proteasome-cleared protein, *proteostasis
modulation* is a more direct pharmacological route to raising residual BUBR1 than NAD+ repletion.

**Method:** NCBI E-utilities (esearch/esummary/efetch) against PubMed; every PMID below was
retrieved and its metadata read. Where an abstract could not be obtained, this is stated. No
identifier in this document is inferred or reconstructed.

**Date of audit:** 2026-08-27.

**Headline verdict: the hypothesis is mechanistically well-founded and empirically unsupported.**
The disease logic is correct and the "more BUBR1 is better" premise is one of the better-evidenced
claims in this whole space. What does not exist is a drug that does it. Every specific
pharmacological instantiation we tested either (a) has no agent, (b) has an agent that failed its
own randomised trials, (c) is unsafe in a child, or (d) is predicted by the aneuploidy literature to
act in the *wrong direction* on the patient's pre-malignant compartment.

---

## 0. Foundation — what the established facts actually license

| Claim | Source | Verdict |
|---|---|---|
| MVA missense BUBR1 alleles cluster in/near the kinase domain, have normal mRNA, accelerated turnover, 2–6× reduced protein; ectopic re-expression to WT levels fully restores checkpoint | Suijkerbuijk 2010, Cancer Res, **PMID 20516114** (abstract retrieved and read in full) | **CONFIRMED.** Abstract explicitly states MVA mutations fall into two classes, that low abundance results from "absence of transcripts from truncating mutants combined with high protein turnover of missense mutants," that "in this group of missense mutants, the amino acid change consistently occurs in or near the BUBR1 kinase domain," and that "ectopic expression of BUBR1 restored mitotic checkpoint activity." |
| The patient's p.Asn1002Lys belongs to that low-abundance class | — | **INFERRED, NOT DEMONSTRATED.** N1002K sits inside the pseudokinase domain (aa 766–1050) and 10 residues from L1012P, one of the two alleles Suijkerbuijk rescued (the other being I909T). The inference is strong but it is an inference. **No published work characterises N1002K.** This is the single most important missing experiment (§5). |
| Raising BUBR1 protein is beneficial *in vivo* | Baker DJ 2013, Nat Cell Biol, **PMID 23242215** — "Increased expression of BubR1 protects against aneuploidy and cancer and extends healthy lifespan" | **CONFIRMED and strongly supportive.** Transgenic sustained high-level BubR1 preserved genomic integrity, reduced tumorigenesis "even in the presence of… oncogenic Ras," extended lifespan and delayed age-related aneuploidy. This is the best available proof that the *therapeutic objective* is sound. |
| BUBR1 dose effects are graded, so a partial increase could matter | Sieben CJ 2020, J Clin Invest, **PMID 31738183** (erratum **PMID 33136097**) | **CONFIRMED.** Mouse *BubR1^L1002P* (mimicking human L1012P — the patient's near-neighbour allele) combined with hypomorphic and truncating alleles produced graded viability and graded progeroid severity: `X753/L1002P` and `H/X753` died prematurely; `H/L1002P` was viable with attenuated progeroid pathology. Also: "BUBR1 allelic effects beyond protein level and aneuploidy contribute to disease heterogeneity." |

**What this licenses:** that total BUBR1 abundance is a real, graded, disease-modifying variable, and
that in this patient 100% of residual BUBR1 comes from the N1002K allele (the L737Ter allele is
NMD'd, no protein). Any fractional stabilisation of N1002K is therefore a fractional increase in
*total* BUBR1. That is a genuinely attractive therapeutic setup.

**What it does not license:** any claim that a drug can achieve it. See below.

---

## 1. The HSP90 direction problem — is HSP90 *activation* available?

The user's framing is correct and the problem is worse than stated.

| Agent / claim | Source | Verdict |
|---|---|---|
| Direct small-molecule HSP90 **activators** exist as a drug class | PubMed `HSP90 activator[tiab]` → **5 total hits**, all reviewed | **REFUTED. The class does not exist.** The five hits are: parthenolide (**PMID 40815947**) — an *inhibitor* of Hsp90α ATPase; matrine (**PMID 29867458**) — activates *extracellular* Hsp90 for axonal growth, not the intracellular client-maturation cycle; goniothalamin (**PMID 25294885**) — enhances Hsp90 ATPase activity but *inhibits* its chaperone activity, i.e. explicitly uncouples the two; a Chinese-language commentary (**PMID 29858888**); and Aha1 (below). There is no clinical or preclinical HSP90-activating drug. |
| Aha1 — the one true HSP90 activator — is a viable strategy | Shelton LB 2017, PNAS, **PMID 28827321**, "Hsp90 activator Aha1 drives production of pathological tau aggregates" | **REFUTED, and instructively so.** Aha1 (activator of Hsp90 ATPase homolog 1) is a co-chaperone that genuinely activates HSP90 — and doing so "dramatically increased the production of aggregated tau"; Aha1 overexpression in rTg4510 mice caused insoluble/oligomeric tau accumulation and cognitive deficits; the *inhibitor* KU-177 reduced insoluble tau. The authors hold a patent on **inhibiting** Aha1. Accelerating the HSP90 ATPase cycle is not the same as increasing folding capacity, and where it has been tested in vivo it was pathogenic. |
| Indirect route: HSF1 activation raises HSP90AA1/HSP70/co-chaperone transcription | Dayalan Naidu & Dinkova-Kostova 2017, FEBS J, **PMID 28052564** (regulation of mammalian HSF1); Wen C 2025, J Med Chem, **PMID 40901799** (small molecules targeting the HSF1 pathway); Kurop 2021, Eur J Med Chem, **PMID 34563965** | **CONFIRMED as the only available route.** HSF1 activation is the only pharmacologically reachable way to raise chaperone capacity, and it raises HSP70 and HSP90 together with co-chaperones. |
| Available HSF1/HSR-inducing agents | arimoclomol & bimoclomol (§2); BGP-15 (**PMID 22322357**, **PMID 22174906**, **PMID 24386957**); geranylgeranylacetone/teprenone (**PMID 40719441** phase-2 HFpEF RCT; **PMID 40227474** GENIALITY post-op AF; **PMID 37883347** RCT in COVID-19); celastrol (**PMID 41594602**, **PMID 40116098**); HDAC inhibitors as arimoclomol potentiators (**PMID 31900865**) | **PARTIALLY CONFIRMED.** Agents exist. Teprenone is an approved anti-ulcer drug in Japan with human RCT exposure, making it nominally repurposable. **But none has ever been shown to raise the level of a specific destabilised missense client protein in a patient.** Celastrol is a natural product with a dirty polypharmacology profile (it is also proteasome-inhibiting and HSP90-disrupting) and is not a credible pediatric agent. |

### The mechanistic trap nobody in the hypothesis has accounted for

HSF1 activation raises **HSP70** at least as much as HSP90. HSP70, with the E3 ligase **CHIP**, is
the *triage* arm of the chaperone system — the machinery that decides a client is unsalvageable and
ubiquitinates it. Raising HSP70 can therefore accelerate, not retard, degradation of a misfolded
client.

This is not speculative. Garcia AM 2025, Mol Pharmacol, **PMID 40023517** reports a high-throughput
screen that found "a novel small-molecule modulator of Hsp70 that **selectively enhances
ubiquitination and degradation of misfolded** neuronal NO synthase." Hsp70 modulation demonstrably
runs in both directions depending on the compound and the client. See also Zeng 2025, Cell Signal,
**PMID 39978610** — Hsp70 *incompletely* disaggregates a misfolded menin truncation, with
tumourigenic consequence.

**Net verdict on §1: the HSP90 direction problem is real, and it is not solvable with existing
pharmacology.** There is no HSP90 activator. The indirect HSF1 route is available but its net effect
on a specific HSP90 client whose degradation is HSP70/CHIP-mediated is *sign-indeterminate* and has
to be measured, not assumed.

---

## 2. Arimoclomol and the HSR co-inducer class

| Question | Source | Verdict |
|---|---|---|
| Regulatory status | Keam SJ 2025, Drugs, **PMID 39715913** "Arimoclomol: First Approval"; Beninger 2024, Clin Ther, **PMID 39572292**; AHFS monograph **PMID 39561251** | **CONFIRMED APPROVED.** MIPLYFFA™, approved **September 2024 in the USA**, in combination with miglustat, for neurological manifestations of Niemann-Pick disease type C, in adults and **pediatric patients ≥2 years**. Developed by Zevra Therapeutics. Note the mechanism as stated on approval: "thought to **upregulate CLEAR (Coordinated Lysosomal Expression and Regulation) network genes and improve lysosomal function**" — i.e. the *label* mechanism is TFEB/lysosomal, not HSP-client stabilisation. |
| Pivotal efficacy | Mengel E 2025, Mol Genet Metab, **PMID 40663813** (NPC-002 48-month OLE); Mengel 2025, Mol Genet Metab Rep, **PMID 40520915** (12-month DB RCT, rescored 4-domain NPCCSS) | **CONFIRMED, with a caveat.** In the OLE, placebo→arimoclomol switchers went from mean annual 5DNPCCSS change of 2.0 on placebo to 0.1 in year 1 on arimoclomol. Sustained ≥5 years, no new safety concerns. **Caveat:** the primary endpoint scale was **rescored post hoc** into a 4-domain instrument (R4DNPCCSS) — a real methodological soft spot the paper itself flags in its title. |
| **Pediatric safety** | Mengel E 2026, Mol Genet Metab Rep, **PMID 42376638** — phase 2/3 open-label **infant** substudy | **CONFIRMED, small.** n=5, aged 14–23 months at screening, exposure 72–1109 days, all on concomitant miglustat. 108 AEs, mostly mild/moderate; 15 SAEs across two patients; **two AEs (elevated ALT/AST) considered probably related**, resolved in 51 days, patient withdrawn. PK in infants comparable to the 2–19y population. "No new safety signals." |
| Real-world safety | Berry-Kravis E 2026, Mol Genet Metab, **PMID 42551329** — US Early Access Program, 4 years | **CONFIRMED.** n=109 (48.6% adults), mean exposure 820 days. 248 AEs, of which **17 events in 13 participants (12.8%) treatment-related**. Disease severity scores broadly stable. |
| **ALS** | Benatar M 2024, Lancet Neurol, **PMID 38782015** — ORARIALS-01, phase 3, n=245 randomised, 239 mITT | **NEGATIVE — a decisive refutation of the general HSR-co-induction thesis.** CAFS over 76 weeks: 0.51 (arimoclomol) vs 0.49 (placebo), **p=0.62**; Cliff's delta 0.039 (95% CI −0.116 to 0.194). Treatment-related AEs 65% vs 52%; discontinuation for AEs 16% vs 5%. The authors' own interpretation: "**safety data suggest that a higher dose of arimoclomol would not have been tolerated**" — i.e. the dose cannot be pushed to chase a bigger chaperone effect. |
| **Inclusion body myositis** | Machado PM 2023, Lancet Neurol, **PMID 37739573**, n=150 efficacy population | **NEGATIVE.** IBMFRS change at month 20: −3.26 (arimoclomol) vs −2.26 (placebo); mean difference −0.99 (95% CI −2.23 to 0.24), **p=0.12** — numerically favouring placebo. Discontinuation for AEs 18% vs 5%. **Transaminases ≥3× ULN in 7% vs 1%. One case of tubulointerstitial nephritis in the arimoclomol arm.** Preceded by a negative proof-of-concept trial, Ahmed M 2016, Sci Transl Med, **PMID 27009270**. |
| Does HSP amplification actually do anything in a mammal? | Gray J 2022, EBioMedicine, **PMID 36455410** | **CONFIRMED preclinically.** Bimoclomol or recombinant human HSP70 given IP to *Npc1^-/-* mice P7–P34 improved myelination, increased mature oligodendrocytes and active/inactive phospho-Fyn ratio, and preserved cerebellar weight (abolished by the Fyn inhibitor saracatinib). Real target engagement — **but on a lipid-storage/myelination axis, not on stabilising a destabilised missense client.** |

### Honest reading of the arimoclomol dossier

The drug is approved, orally dosed, BBB-penetrant, has genuine pediatric PK and safety data down to
14 months, and is the single most repurposable proteostasis agent in existence. That is the good news
and it is not trivial.

The bad news is threefold and each part is load-bearing:

1. **It has failed the two diseases where the HSR-co-induction thesis was directly on trial.** ALS
   and IBM are both protein-mishandling diseases; both were adequately powered; both were flatly
   negative. The one indication it won is the one where its mechanism is described as
   *lysosomal/CLEAR*, not chaperone-client.
2. **Its NPC mechanism may not be the mechanism we want.** Shammas 2025, Mol Genet Metab,
   **PMID 40215728** is titled "Mechanistic insights into arimoclomol mediated effects on
   **lysosomal function**." If arimoclomol's clinical benefit runs through TFEB/lysosome rather than
   through raised HSP90 folding capacity, its approval tells us nothing about whether it can
   stabilise BUBR1.
3. **Two safety signals map onto this patient's existing organ burden.** Hepatic transaminase
   elevation recurs across the infant substudy, the IBM trial (7% vs 1%) and the EAP. And the IBM
   trial recorded a case of **tubulointerstitial nephritis** — in a child who already has
   **nephrocalcinosis**, that is a specific, non-hypothetical monitoring concern, not boilerplate.

---

## 3. Pharmacological chaperone precedent in other genetic disease

This is the strongest part of the hypothesis and it must be stated precisely, because it is very easy
to overclaim.

| Precedent | Source | What it establishes |
|---|---|---|
| **Migalastat**, Fabry disease | Germain DP 2016, N Engl J Med, **PMID 27509102** "Treatment of Fabry's Disease with the Pharmacologic Chaperone Migalastat"; Hughes DA 2017, J Med Genet, **PMID 27834756** (ATTRACT, 18-month phase 3 vs ERT); Feldt-Rasmussen 2020, Mol Genet Metab, **PMID 33012654** (30-month OLE); Bichet 2021, Mol Genet Metab Rep, **PMID 34401344** (long-term renal function); Kallish 2025, J Med Genet, **PMID 40897525** (long-term efficacy in females) | **The closest true precedent.** An orally administered small molecule that binds a *destabilised missense* enzyme, increases its cellular level and trafficking, and produced clinical benefit in randomised trials. Critically: **amenability is variant-specific** — Benjamin ER 2017, Genet Med, **PMID 27657681**, "The validation of pharmacogenetics for the identification of Fabry patients to be treated with migalastat," exists precisely because only a subset of *GLA* missense variants respond. |
| **Elexacaftor/tezacaftor/ivacaftor**, CFTR F508del | Middleton PG 2019, N Engl J Med, **PMID 31697873** (single F508del allele); Heijerman HGM 2019, Lancet, **PMID 31679946** (F508del homozygous); pediatric extension to ≥2 years, Goralski 2026, J Cyst Fibros, **PMID 42315414** | **The most transformative precedent.** F508del is a misfolded, ER-retained, proteasome-degraded protein — the closest structural analogy to the BUBR1 situation — and it was corrected pharmacologically with disease-changing effect, now down to age 2. |
| **Tafamidis**, ATTR | verified as a large, mature literature (PubMed `tafamidis AND transthyretin` — 385 hits; e.g. systematic review **PMID 42589936**; real-world outcomes **PMID 42463463**). *Note: the original ATTR-ACT NEJM citation was not individually retrieved in this audit; I am not asserting a PMID for it.* | Stabilisation of a native-but-labile protein by a small molecule, approved and clinically effective. |
| **Deucravacitinib** — a **pseudokinase**-domain-binding approved drug | Roskoski R 2023, Pharmacol Res, **PMID 36754102** "Deucravacitinib is an allosteric TYK2 protein kinase inhibitor FDA-approved for the treatment of psoriasis"; selectivity analyses **PMID 40200906**, **PMID 39353258**; triple-action mechanism **PMID 40378946** | **The most under-appreciated precedent for *this specific target*.** It is proof that the degenerate ATP pocket of a **pseudokinase domain** is druggable with a selective small molecule that locks a domain conformation. Given Suijkerbuijk 2012 (**PMID 22698286**) established that BUBR1's ATP-interacting residues serve *conformational stability* rather than catalysis, the TYK2-JH2 precedent is the direct structural argument that a BUBR1 pseudokinase-pocket stabiliser is *chemically conceivable*. |
| Generic chemical chaperones (4-PBA) | Alport syndrome **PMID 40484355**, **PMID 40975521**; vascular EDS COL3A1 **PMID 40280907**; SLC6A1 DEE **PMID 42650175**; osteogenesis imperfecta **PMID 39706289**; but also **PMID 36012668** — 4-PBA derivatives prevented SOD1 aggregation in vitro with **no effect on disease progression in SOD1-ALS mice**; and **PMID 36373957** "4-phenylbutyric acid — Identity crisis; can it act as a translation inhibitor?" | **WEAK.** Broad preclinical activity across many misfolding diseases, essentially no controlled clinical validation for protein-level rescue, and an unresolved question about its actual mechanism. |

### What the precedents establish vs. what they do NOT

**They establish** — beyond reasonable dispute — that *raising the cellular level of a destabilised
missense protein with an orally-administered small molecule produces real clinical benefit in human
genetic disease*. The therapeutic logic of this hypothesis is proven in principle. That is a genuine
and defensible claim for the report.

**They do not establish** — and this is the sentence that has to appear in the writeup — that this is
achievable by *generic proteostasis modulation*. Every one of these successes is a **target-specific
molecule found by dedicated high-throughput screening against that one protein**: migalastat is an
iminosugar that occupies the α-Gal A active site; VX-445/661/770 came from ~15 years of CFTR-directed
screening; tafamidis binds the TTR thyroxine site; deucravacitinib binds TYK2-JH2. **Not one of them
is a chaperone-capacity booster.** Arimoclomol is the only genuinely generic proteostasis agent that
reached approval, and it failed the two trials where a generic mechanism was actually tested.

Migalastat's amenability requirement is the sharpest warning: even within a single well-characterised
gene, with a purpose-built drug, most variants do not respond, and a companion pharmacogenetic assay
had to be built to tell which ones do. Extrapolating a generic chaperone effect to an
uncharacterised BUBR1 allele is several steps beyond what any of this supports.

---

## 4. Proteasome inhibition — is it viable?

**Verdict: NOT VIABLE. Drop it.** The user's expectation is correct, and there is a reason for
dropping it that is much stronger than the obvious toxicity argument.

| Consideration | Source | Finding |
|---|---|---|
| Pediatric tolerability of bortezomib | LeBlanc ZC 2025, Front Pharmacol, **PMID 40843380** — systematic review of pediatric BTZ use | Better than expected, and I will not overstate the toxicity case: pediatric patients showed **lower** peripheral neuropathy and GI toxicity than adults; marrow suppression and infection were comparable or higher; conclusion "acceptable safety profile for use in pediatric patients," with a recommendation for antibacterial/antifungal prophylaxis. **However** every source study is short-course oncology (relapsed ALL/AML — e.g. **PMID 41692013**, **PMID 42376206**, **PMID 41445872**), i.e. weeks of cyclical IV therapy under transplant-grade supportive care. There is **no** chronic, years-long pediatric proteasome-inhibition safety dataset, and none will exist. |
| Selectivity | — | MG132 preventing BUBR1 turnover in vitro is a *mechanistic probe result*, not a therapeutic lead. Proteasome inhibition stabilises the entire misfolded proteome indiscriminately — including the SAC substrates whose *timely destruction* is what mitosis depends on. Inhibiting the proteasome in a cell whose problem is a mitotic checkpoint is mechanistically incoherent at the whole-cell level. |
| **The decisive argument** | Ippolito MR 2024, Cancer Discov, **PMID 39247952** — "Increased RNA and Protein Degradation Is Required for Counteracting Transcriptional Burden and Proteotoxic Stress in Human Aneuploid Cells" | **Aneuploid cells mitigate proteotoxic stress by reducing translation and *increasing protein degradation*, "rendering them more sensitive to proteasome inhibition."** Recapitulated across hundreds of cancer cell lines and primary tumours, and aneuploidy level was significantly associated with **myeloma patients' clinical response to proteasome inhibitors**. In MVA the aneuploid cells *are the patient's tissue* — mosaic, constitutional, throughout the body. Chronic proteasome inhibition is therefore predicted to be **selectively cytotoxic to the patient's own somatic cells**, in a child who already has failure to thrive. |

Proteasome inhibition is not merely unsafe here; it is *directionally* the wrong drug in a
constitutionally aneuploid host. **DROP.**

---

## 5. Has anyone attempted to pharmacologically stabilise BUBR1?

**Verdict: NO. Nothing. This is a genuine white space.**

Searches run:
- `BUB1B[tiab] AND (chaperone[tiab] OR HSP90[tiab] OR proteostasis[tiab] OR stabiliz*[tiab] OR stabilis*[tiab])` → **14 hits, all reviewed, none relevant.** The closest is Cui A 2025, J Cell Mol Med, **PMID 40857057**, "KIFC1 Overexpression Promotes Pancreatic Carcinoma Progression via **Stabilising BUB1B**" — an oncogenic mechanism running the opposite way (stabilised BUB1B as a *cancer driver*, motivating BUB1B *inhibitors*, cf. El Hafi 2025, Eur J Med Chem, **PMID 39818011**, "Synthesis and biological assessment of **BUB1B inhibitors**"). The remainder are prognostic-biomarker papers.
- `BUBR1[tiab] AND (chaperone OR HSP90 OR proteasome OR degradation)` → 89 hits; the BUBR1 degradation literature is entirely about *physiological* mitotic turnover — FBXW7 (**PMID 38008853**), Pellino-1 (**PMID 28410192**), UBR5 (**PMID 35217622**), HDAC2/3 deacetylation (**PMID 28985013**) — i.e. mapping the machinery that destroys BUBR1 normally, with **zero** work on pharmacologically protecting a mutant from it.
- `mosaic variegated aneuploidy AND treatment` → 23 hits; **no pharmacological intervention of any kind.** The entire MVA "treatment" literature is oncological and supportive: reduced-intensity chemo for RMS (**PMID 31184400**), bilateral nephrectomy + PD for Wilms (**PMID 31081598**), HSCT (**PMID 31053147**), cancer surveillance guidance (Nakano 2024, Clin Cancer Res, **PMID 39264246**).

**Implication for the report — and this is a positive, not a negative:** the *only* demonstrated
rescue of an MVA missense BUBR1 allele remains **genetic** (ectopic re-expression, Suijkerbuijk 2010,
PMID 20516114; transgenic overexpression, Baker 2013, PMID 23242215). The therapeutic objective is
validated and the pharmacology has never been attempted. That is exactly what a drug-repurposing
hackathon entry should be able to say out loud — provided it says it honestly, as a gap, and does not
dress an untested idea as an established one.

---

## 6. Aneuploidy-selective vulnerability — and the tension, addressed head-on

The literature here is mature, and it is largely **hostile** to the proteostasis-boosting proposal.

| Finding | Source | Direction |
|---|---|---|
| The three canonical aneuploidy-selective antiproliferative agents are the energy-stress inducer **AICAR**, the protein-folding inhibitor **17-AAG (an HSP90 inhibitor)**, and the autophagy inhibitor **chloroquine** | Tang YC, Williams BR, Siegel JJ, **Amon A**. Cell 2011, **PMID 21315436** | **AGAINST.** AICAR induced p53-mediated apoptosis in trisomy-1/13/16/19 MEFs; AICAR + 17-AAG synergised against aneuploid human cancer lines. Every one of the three is the *inverse* of the proposed intervention. The proposal is, quite literally, to give the antidote to the Amon-lab aneuploidy-selective triad. |
| Aneuploid cells are more dependent on protein *degradation* and more sensitive to proteasome inhibition | Ippolito 2024, Cancer Discov, **PMID 39247952** | **AGAINST** (for PIs; see §4) |
| Aneuploidy imposes proteostasis disruption, mitochondrial dysfunction, aggregation | Amponsah PS 2025, Nat Commun, **PMID 40527892**; review **PMID 40221883** "The proteostasis burden of aneuploidy"; Cheng 2025, Annu Rev Genomics Hum Genet, **PMID 40333415** | Context |
| **Boosting** protein quality control *dampens* aneuploidy's deleterious effects | Joy J 2021, Dev Cell, **PMID 34216545** | **FOR.** In a *Drosophila* epithelial model, aneuploidy saturates autophagy → compromised mitophagy → dysfunctional mitochondria → ROS → JNK → senescence; and "activation of the major protein quality control mechanisms and mitophagy **dampens the deleterious effects of aneuploidy**." This is the single best mechanistic support for the hypothesis anywhere in the literature — and it is in flies, in an epithelium, genetic not pharmacological. |
| Aneuploid-cell fitness can be improved by a *non*-chaperone route | Hwang S / Torres EM 2019, Cell Rep, **PMID 31747614** | **FOR, alternative axis.** Raising long-chain bases suppressed nuclear-morphology abnormalities and **improved fitness** of cells from Down, Patau and Edwards syndrome patients. Related: sphingolipid homeostasis as an aneuploid liability, Tang 2017, Cancer Res, **PMID 28775166**; Hwang 2017, Cell Rep, **PMID 29281829**. |
| Aneuploidy can be an oncogenic dependency in its own right | Girish V / Sheltzer JM 2023, Science, **PMID 37410869** | Context — "aneuploidy addiction"; trisomy 1q required for malignant growth via MDM4/p53 suppression. |

### The tension, stated plainly

**If aneuploid cells survive on the edge of proteostatic collapse, then raising chaperone capacity
prolongs the survival of every aneuploid cell in the body — including the ones that are one hit away
from becoming the next rhabdomyosarcoma.** This child has already had one rhabdomyosarcoma. MVA
carries a documented predisposition to RMS and Wilms tumour (**PMID 42595739**, **PMID 31184400**,
**PMID 31081598**, **PMID 33209717**) severe enough to warrant dedicated surveillance guidelines
(**PMID 39264246**). Proteotoxic-stress-induced death and senescence of aneuploid cells is plausibly
a *tumour-suppressive* mechanism that the proposal would blunt.

I want to be even-handed about how strong this objection is, because it can be overstated too:

- Tang 2011 is a **cancer-therapeutic** paper. It shows aneuploid cells can be *selectively killed*;
  it does not show that aneuploid-cell death is what protects an MVA patient from cancer.
- Joy 2021 points the other way and is the more physiologically apt model (a developing epithelium,
  not a tumour): there, proteostasis support *reduced* aneuploidy-driven damage.
- The two are reconcilable — proteostasis capacity is probably protective for tissue function and
  permissive for aneuploid-clone persistence at the same time. Which effect dominates in a
  10-year-old with a cancer-predisposition syndrome is **unknown and not currently knowable from the
  literature.**

That is the honest position, and it is a *disqualifying* uncertainty for a lead candidate in a
cancer-predisposed child, while being an entirely acceptable one for a secondary candidate with a
defined preclinical decision point.

### The alternative that the same literature actually supports

The one intervention with demonstrated *in vivo* benefit in a BubR1-hypomorphic **mammal** is not a
chaperone drug at all — it is **senescent-cell clearance**. Baker DJ 2011, Nature, **PMID 22048312**:
in the *BubR1 progeroid mouse background*, INK-ATTAC-mediated removal of p16^Ink4a-positive cells
delayed onset of adipose, skeletal-muscle and eye pathology, and late-life clearance attenuated
already-established disorders. Supporting: **PMID 18516091** (p16/p19Arf in BubR1 insufficiency),
**PMID 23602569** (p21 in BubR1 progeroid mice), **PMID 34216545** (aneuploidy→senescence is the
terminal step). This maps directly onto the patient's short stature, failure to thrive and
progeroid features. Caveats that must be stated: the mouse tool was **genetic**, not pharmacological;
pediatric senolytic dosing is unestablished; and senescence is itself tumour-suppressive, so clearing
senescent cells in a cancer-predisposed child carries its own inverted risk. But if the report wants
a *second* mechanistic axis with real in-genotype in vivo evidence, this is the one the literature
actually offers.

---

## 7. AMPK / metformin — does the pipeline hit survive contact with evidence?

**Verdict: DOES NOT SURVIVE. Drop metformin. The evidence that exists points the opposite way.**

| Claim | Source | Verdict |
|---|---|---|
| AMPK activation affects aneuploid-cell behaviour | Tang 2011, Cell, **PMID 21315436** | **CONFIRMED — and it is a hazard signal, not a benefit signal.** AICAR is an AMPK activator, and it is one of the three aneuploidy-*selective killers*. "AICAR induces p53-mediated apoptosis in primary MEFs trisomic for chromosome 1, 13, 16, or 19." If this generalises, AMPK activation in a constitutionally mosaic-aneuploid child would preferentially kill the patient's own aneuploid tissue. |
| Metformin benefits trisomic human cells | Buczyńska A 2025, Front Mol Biosci, **PMID 40552127** | **WEAK / INSUFFICIENT.** In vitro only; two T21 fibroblast lines (Detroit 532/539) plus one control; 48 h; 10–50 μM metformin reduced total oxidative capacity and oxidative DNA/RNA damage, raised total antioxidant capacity, raised PRKAA1/AMPK activity. **No karyotypic, mitotic-checkpoint, proliferative or protein-level endpoint. No in vivo work. No BUBR1 measurement.** |
| Metformin/AMPK affects aneuploidy tolerance in vivo | `(AICAR OR metformin OR AMPK) AND (aneuploidy OR chromosomal instability)` → 39 hits, reviewed | **NO EVIDENCE.** The AMPK–genome-stability literature that exists concerns replication-fork protection (**PMID 31053472**, **PMID 40749324**), centrosome amplification on AMPKα1 *loss* (**PMID 32316320**), LKB1 inactivation → centromere defects (**PMID 32668413**), and kinetochore AMPK during mitosis (**PMID 36336348**). None supports metformin as an aneuploidy-tolerance or BUBR1-raising agent. Note also **PMID 35568294**: high-dose metformin induces genotoxic stress. |

**Assessment of the pipeline signal itself:** PRKAA2/metformin surfacing as a *network neighbour* of
TRIP13 is a graph-topology artifact. TRIP13 is a bona fide MVA gene (biallelic *TRIP13* → Wilms tumour
and chromosome missegregation, Yost S 2017, Nat Genet, **PMID 28553959**), so the neighbourhood is
real — but proximity in an interaction/co-expression graph is not a mechanism, and here the one piece
of direct experimental evidence about AMPK activation in aneuploid cells says the intervention is
*cytotoxic to aneuploid cells*. Reporting metformin as a candidate would be exactly the failure mode
of sizing a hypothesis from network structure rather than from the assay.

---

## What we CAN claim

1. The patient's residual BUBR1 comes entirely from one missense allele, and total BUBR1 abundance is
   a graded, disease-modifying variable in this exact genotype (**PMID 20516114**, **PMID 31738183**).
2. Raising BUBR1 protein is beneficial in vivo in mice: it reduces aneuploidy, suppresses
   tumorigenesis even against oncogenic Ras, and extends healthy lifespan (**PMID 23242215**).
3. For the MVA missense allele class, the defect is protein **quantity**, and restoring quantity
   restores checkpoint function completely (**PMID 20516114**).
4. Pharmacologically raising the level of a destabilised missense protein is a **proven therapeutic
   modality in human genetic disease** — migalastat (**PMID 27509102**, **PMID 27834756**) and
   elexacaftor/tezacaftor/ivacaftor (**PMID 31697873**, **PMID 31679946**).
5. Pseudokinase domains are **druggable** by selective small molecules that act on domain
   conformation — deucravacitinib/TYK2-JH2 is FDA-approved proof (**PMID 36754102**).
6. **Nobody has ever attempted to pharmacologically stabilise BUBR1.** The white space is real
   and verifiable (three independent searches, §5).
7. An HSR co-inducer with an approved pediatric indication down to age 2 exists and its PK/safety
   have been characterised in infants (**PMID 39715913**, **PMID 42376638**, **PMID 42551329**).

## What we CANNOT claim

1. **That the patient's N1002K allele is a low-abundance allele.** It has never been characterised.
   This is an inference from position and from two neighbouring alleles.
2. **That any drug raises BUBR1 levels.** No agent, in any system, has been shown to do this. Zero.
3. **That HSP90 can be pharmacologically activated.** The class does not exist; the only genuine
   HSP90 activator (Aha1) is pathogenic in vivo (**PMID 28827321**).
4. **That HSF1/HSR induction would raise BUBR1 rather than lower it.** It co-induces HSP70, the
   triage arm; Hsp70 modulators demonstrably enhance degradation of misfolded clients
   (**PMID 40023517**). The sign of the effect is unknown.
5. **That arimoclomol's NPC approval validates a chaperone-client-stabilisation mechanism.** Its
   label mechanism is CLEAR/lysosomal (**PMID 39715913**, **PMID 40215728**), and the generic HSR
   thesis failed both trials that tested it (**PMID 38782015**, **PMID 37739573**).
6. **That the CFTR/Fabry precedents transfer.** They are target-specific molecules from dedicated
   screening campaigns, not generic proteostasis boosters; and even within Fabry, most variants are
   not amenable (**PMID 27657681**).
7. **That boosting proteostasis is oncologically safe in this child.** The direction of effect on
   the pre-malignant aneuploid compartment is genuinely unresolved (§6).
8. **That metformin/AMPK has any role.** The one relevant experiment says AMPK activation kills
   aneuploid cells (**PMID 21315436**).

---

## Ranked recommendation

### 1. Proteostasis modulation → **SECONDARY candidate**, with a mandatory gating experiment. Not a lead.

Keep it, but reframe it and be explicit about what it is. It earns its place because the
disease-mechanism fit is the best of any hypothesis on the table — the established defect *is*
accelerated turnover of a chaperone-dependent protein, and no other proposed mechanism is that
proximate — and because arimoclomol is a real, approved, pediatric-dosed, orally available agent.

It cannot be the lead because:
- the specific chaperone implicated (HSP90) cannot be pharmacologically raised;
- the only available lever (HSF1) co-induces the degradation-triage arm, so the sign of the effect on
  BUBR1 is unknown;
- the agent failed both randomised trials of its generic mechanism;
- and the aneuploidy literature raises a credible, unresolved concern that it protects the
  pre-malignant compartment in a child who has already had one sarcoma.

**Gating experiment, and it is cheap and decisive:** patient (or MVA-genotype) fibroblasts +
arimoclomol / bimoclomol / geranylgeranylacetone → BUBR1 immunoblot (steady-state level), cycloheximide-chase
(turnover rate), and mitotic-checkpoint assay (nocodazole/taxol arrest index) — exactly the assay
panel Suijkerbuijk 2010 already established for this allele class. One in-vitro readout converts this
from speculation to a lead or kills it. **Recommend the report present it at this altitude: a
mechanism-matched, testable secondary hypothesis with a named first experiment, not a treatment
proposal.**

### 2. BUBR1 pseudokinase-pocket pharmacological chaperone → **highest scientific value, longest horizon**

This is the intellectually correct answer and the report should say so even though it yields no
repurposed drug. Suijkerbuijk 2012 (**PMID 22698286**) established that the ATP-interacting residues
serve conformational stability; deucravacitinib (**PMID 36754102**) proves a degenerate pseudokinase
pocket can be drugged conformationally; migalastat and ETI prove the modality delivers clinical
benefit. A ligand that occupies the BUBR1 pseudokinase pocket and stabilises N1002K is the
mechanistically precise intervention. It is a discovery program, not a repurposing hit — and framing
it honestly as such is stronger than pretending an existing drug does this.

### 3. Senescent-cell clearance → **worth naming as a second axis**

The only pharmacologically-adjacent intervention with in vivo benefit in a BubR1-hypomorphic mammal
(**PMID 22048312**), targeting the progeroid/FTT phenotype rather than the cancer risk. Genetic tool,
not a drug; pediatric senolytics unestablished; carries its own inverted tumour-suppression risk.
Mention, do not lead with.

### 4. Proteasome inhibition → **DROP**

Non-selective; mechanistically incoherent for a mitotic-checkpoint disease; no chronic pediatric
safety data; and decisively, aneuploid cells are *more* sensitive to proteasome inhibition
(**PMID 39247952**), so chronic PI is predicted to be selectively toxic to this patient's own tissue.

### 5. HSP90 activation as a named strategy → **DROP**

No such drug class exists (5 PubMed hits, none an activator of the client-maturation cycle), and the
one real HSP90 activator drives pathology in vivo (**PMID 28827321**). Do not put "HSP90 activator"
in the report as a candidate; put the *problem* in the report as a finding — it is a better
contribution than a fake candidate.

### 6. Metformin / AMPK → **DROP**

Network-proximity artifact. The single direct experiment (**PMID 21315436**) says AMPK activation
selectively kills aneuploid cells. Reporting it as a candidate would invert the evidence.

---

## On the framing question (proteostasis vs NAD+)

The NAD+ arm was not audited here and this document does not adjudicate it. One honest caution for
the writeup: proteostasis modulation has the *more proximate mechanistic rationale* — it addresses
the actual measured defect (accelerated proteasomal turnover of a chaperone-gated protein) rather
than a downstream metabolic correlate. But proximity of rationale is not superiority of evidence.
By the standard of "has anyone shown this raises BUBR1," **both arms score zero**, and the report
should not let a better story stand in for a better dataset.

---

### Search record

Queries executed against PubMed via E-utilities: `BUB1B[tiab] AND (chaperone|HSP90|proteostasis|stabiliz*)`
(14); `BUBR1[tiab] AND (chaperone|HSP90|proteasome|degradation)` (89); `mosaic variegated aneuploidy AND treatment`
(23); `mosaic variegated aneuploidy AND (cancer risk|rhabdomyosarcoma|Wilms)` (28); `arimoclomol` (85);
`arimoclomol AND (Niemann-Pick|NPC)` (25); `arimoclomol AND inclusion body myositis AND randomised` (6);
`HSF1 activator[tiab] OR heat shock response inducer[tiab] OR HSP co-inducer[tiab]` (30); `HSP90 activator[tiab]` (5);
`HSF1 AND small molecule activator AND (proteostasis|neurodegeneration)` (23); `(geranylgeranylacetone|teprenone) AND heat shock protein` (209);
`celastrol AND HSF1` (44); `BGP-15 AND (clinical trial|human|insulin)` (54); `(4-phenylbutyrate|sodium phenylbutyrate) AND chemical chaperone AND misfold*` (73);
`pharmacological chaperone AND (migalastat|Fabry)` (194); `elexacaftor tezacaftor ivacaftor AND F508del` (263);
`tafamidis AND transthyretin AND (stabilizer|randomized)` (385); `deucravacitinib AND TYK2 pseudokinase` (28);
`pseudokinase AND (ligand|ATP) AND (stabilization|conformational stability)` (46);
`bortezomib AND (pediatric|children) AND (neuropathy|toxicity)` (104); `aneuploidy AND proteotoxic stress` (46);
`aneuploidy AND (selective vulnerability|targeted therapy) AND (HSP90|autophagy|energy stress)` (16);
`aneuploidy AND HSP90 inhibitor AND sensitivity` (4); `(Torres EM|Williams BR|Sheltzer JM)[au] AND aneuploidy` (40);
`aneuploidy-selective antiproliferation compounds` (1); `Tang YC[au] AND aneuploid` (6);
`(AICAR|metformin|AMPK) AND (aneuploidy|chromosomal instability)` (39); `(metformin|AMPK) AND (Down syndrome|trisomy 21)` (168);
`BubR1 AND (p16Ink4a|senescent cells|senolytic)` (57); `Baker DJ[au] AND BubR1` (22);
`BubR1 overexpression AND (lifespan|aging|healthy)` (6); `CHIP[tiab] AND Hsp70 AND (triage|degradation) AND misfolded` (64);
`Hsp90 AND kinase client AND (stabilization|maturation) AND Cdc37` (88).

Full abstracts retrieved and read for: 20516114, 21315436, 22048312, 23242215, 27009270, 28827321,
31738183, 31747614, 34216545, 36455410, 37410869, 37739573, 38782015, 39247952, 39715913, 40552127,
40663813, 40843380, 42376638, 42551329.

**PMID unverified:** the original ATTR-ACT tafamidis NEJM trial — the tafamidis literature was
confirmed to exist at scale (385 hits, individual records listed above) but the pivotal trial's own
PMID was not individually retrieved, so no identifier is asserted for it.
