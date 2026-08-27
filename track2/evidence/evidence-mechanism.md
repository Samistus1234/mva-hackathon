# Evidence — BUBR1 domain architecture & the pseudokinase correction

Verified by coordinator, 2026-08-27. Primary sources only.

## Domain architecture (UniProt O60566, BUBR1/BUB1B)

- Protein length: **1050 aa**
- BUB1 N-terminal domain: **62–226**
- "Protein kinase" domain: **766–1050**
- Region necessary for KNL1 interaction: 152–185

Mapping the proband's two alleles:

| Allele | Position | Location | Predicted consequence |
|---|---|---|---|
| p.Leu737Ter | 737 / 1050 | **before** the C-terminal domain (766–1050) | truncation removes the entire C-terminal domain; transcript a strong NMD candidate → functionally null |
| p.Asn1002Lys | 1002 / 1050 | **inside** the C-terminal domain | full-length protein carrying a substitution in the folded C-terminal domain |

## CRITICAL CORRECTION — it is a pseudokinase, not a kinase

Do **not** write that p.Asn1002Lys "impairs kinase activity." Human BUBR1 catalysis is
dispensable. Framing this as lost catalysis would be a factual error a judge would catch.

**Suijkerbuijk SJ, van Dam TJ, Karagöz GE, et al. "The vertebrate mitotic checkpoint
protein BUBR1 is an unusual pseudokinase." Dev Cell. 2012 Jun 12;22(6):1321-9.
PMID 22698286. doi:10.1016/j.devcel.2012.03.009**

Verbatim from the abstract:
- "putative catalysis by human BUBR1 is dispensable for error-free chromosome segregation"
- "**residues that interact with ATP in conventional kinases are essential for
  conformational stability in BUBR1**"
- Human BUBR1 retained the catalytic triad but is an "unusual, triad-containing
  pseudokinase"; catalytic motifs underwent nonconserved degeneration.

**Why this matters for us:** the C-terminal domain's job is *conformational stability*.
A missense there is therefore best modelled as **destabilising the protein / lowering
BUBR1 protein level**, not as abolishing an enzymatic activity. That makes
"raise/stabilise residual BUBR1 protein" the mechanistically correct therapeutic lever
for this specific allele — the allele-aware core of our proposal.

## The pseudokinase domain has a required checkpoint function

**Gama Braga L, Cisneros AF, Mathieu MM, et al. "BUBR1 Pseudokinase Domain Promotes
Kinetochore PP2A-B56 Recruitment, Spindle Checkpoint Silencing, and Chromosome
Alignment." Cell Rep. 2020 Nov 17;33(7):108397. PMID 33207204.
doi:10.1016/j.celrep.2020.108397** (senior author Sabine Elowe)

Verbatim from the abstract:
- "the C-terminal pseudokinase domain of human BUBR1 is required to promote KARD
  phosphorylation"
- "**Mutation or removal of the pseudokinase domain results in decreased PP2A-B56
  recruitment to the outer kinetochore attenuated checkpoint silencing and errors in
  chromosome alignment as a result of imbalance in Aurora B activity**"

**Why this matters:** this is direct, published support that a *mutation* (not only a
deletion) in the domain containing p.Asn1002Lys produces chromosome-alignment errors —
i.e. the missegregation that generates mosaic aneuploidy. It links the proband's second
allele to the phenotype through PP2A-B56/Aurora B balance, independent of any catalysis
claim.

## Resulting mechanism chain (safe to assert)

null allele (L737Ter, NMD) + destabilised/alignment-defective allele (N1002K in the
pseudokinase domain) → reduced functional BUBR1 dose → impaired KARD→PP2A-B56 recruitment
and Aurora B imbalance → chromosome missegregation → **mosaic variegated aneuploidy** →
aneuploidy-induced senescence + tumour predisposition → the child's rhabdomyosarcoma,
growth failure, and the parents' recurrent aneuploid pregnancy loss.

## Caveats to state in the report

- p.Asn1002Lys is absent from gnomAD and has no published functional assay. Its
  destabilising effect is **predicted** from domain function, not measured. The report
  must say so, and should propose the assay that would settle it (BUBR1 immunoblot /
  turnover in patient fibroblasts or lymphoblastoid cells).
- Phase (in *trans*) is inferred from allele balance and disease biology; parental
  genotypes were not available.
