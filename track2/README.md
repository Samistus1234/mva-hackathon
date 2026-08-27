# Track 2 — Drug repurposing for MVA

Repositioning hypotheses for the Track 1 proband: a child with Mosaic Variegated
Aneuploidy caused by compound-heterozygous **BUB1B** (`p.Leu737Ter` null +
`p.Asn1002Lys` missense).

> These are research hypotheses for laboratory follow-up. Nothing here is medical
> advice, and no drug named here is established therapy for MVA.

## The obstacle, stated plainly

```
$ python3 repurpose.py --gene BUB1B
=== stage 0: are the seed genes themselves druggable? ===
  BUB1B: DGIdb knows 0 drugs. A direct-lookup pipeline stops here — this is why we hop.
```

Zero. That single line is the reason rare-disease repurposing stalls: the causal
protein is a checkpoint scaffold nobody has drugged, so gene→drug lookup ends before
it starts. `repurpose.py` hops outward instead — through the gene's physical
interaction neighbourhood — and asks which *neighbours* carry mature pharmacology.

## What the hop finds

Running the two mechanism axes of this disease:

| Axis | Seeds | Command | Output |
|---|---|---|---|
| Restore BUBR1 dose | `BUB1B` | `--gene BUB1B` | `outputs/axis1_bub1b_stabilisation.tsv` |
| Clear the downstream consequence | `CDKN2A TP53` | `--gene CDKN2A TP53` | `outputs/axis2_senescence.tsv` |

Axis 1 is the informative one. BUB1B has 37 interactors above the confidence floor, of
which 14 carry any drug evidence — and **nine of those 14 are acetylation machinery**
(KAT2A, KAT2B, SIRT2, EP300, and five HDACs). The pipeline is blind to the literature, yet
it nominates the axis where the in-vivo evidence sits: SIRT2 deacetylates BubR1 and
controls its stability.

Read that result carefully, though. The six top-priority rows all sit at exactly 0.40 —
the interaction floor — so their order is a tie, and SIRT2 itself ranks eighth. CREBBP,
the acetyltransferase that opposes SIRT2 in this mechanism, is absent from BUB1B's IntAct
neighbourhood entirely. The honest claim is that the tool nominates the acetylation
*class*, not that it picks out SIRT2.

Controls, because "hub genes return chromatin modifiers" is the obvious objection: *HBB*
returns HSPA8, MDM4, PSMC5 and the other globins; *SMN1* returns **SMN2** first — the
target of nusinersen, the approved therapy for spinal muscular atrophy. The acetylation
enrichment is specific to BUB1B, and the tool recovers a known rare-disease target when
one exists.

Axis 2 yields 318 interactors above the floor, headed by CDK4/CDK6 (palbociclib,
abemaciclib, ribociclib), SIRT1, CREBBP and PARP1 — the p16–RB senescence axis, with
PARP1, an NAD⁺-consuming enzyme, tying the two axes back together.

Full reasoning, evidence grading, and the pediatric safety analysis:
[`report/samistus1234_track2_report.md`](report/samistus1234_track2_report.md).

## Running it

```bash
python3 repurpose.py --gene BUB1B                       # single seed
python3 repurpose.py --gene CDKN2A TP53 --out x.tsv     # mechanism axis, several seeds
python3 repurpose.py --gene CEP57                       # any other MVA gene
python3 repurpose.py --gene SMN1                        # positive control: returns SMN2
```

No install, no API key, no patient data — standard library only, over the public
Open Targets and DGIdb GraphQL endpoints. Because it takes any gene symbol, the same
command works for the other MVA genes (`CEP57`, `TRIP13`) and for any undiagnosed
case whose causal gene turns out to be undruggable.

**Scoring.** Each neighbour scores `interaction_score × maturity`, where maturity
weights approved drugs (75%) over sheer count of known binders (25%). This ranks
*tractability*, not therapeutic merit — it is a hypothesis generator whose output is
meant to be filtered by mechanism and safety, which is what the report does. Ties at
the 0.40 interaction floor are real ties, not precision. The full interaction
neighbourhood is paged in — an earlier version read only the first page and silently
dropped most of a well-studied gene's partners.
