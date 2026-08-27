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

Axis 1 is the informative one. Of BUB1B's 37 confident interactors, the druggable
ones are almost entirely its **acetylation-control machinery** — KAT2B and KAT2A
(acetyltransferases), SIRT2, and the class-I/II HDACs. The pipeline is blind to the
literature, yet it lands on precisely the axis where the in-vivo evidence sits: SIRT2
deacetylates BubR1 and controls its stability, and raising NAD⁺ raises BubR1 in
BubR1-hypomorphic mice. Convergence of an unbiased network hop with published mouse
pharmacology is what promoted this axis to candidate #1 in the report.

Axis 2 surfaces CDK4/CDK6 (palbociclib, abemaciclib, ribociclib), SIRT1, and PARP1 —
the p16–RB senescence axis, and, in PARP1, an NAD⁺-consuming enzyme that ties the two
axes back together.

Full reasoning, evidence grading, and the pediatric safety analysis:
[`report/samistus1234_track2_report.md`](report/samistus1234_track2_report.md).

## Running it

```bash
python3 repurpose.py --gene BUB1B                       # single seed
python3 repurpose.py --gene CDKN2A TP53 --out x.tsv     # mechanism axis, several seeds
python3 repurpose.py --gene CEP57                       # any other MVA gene
```

No install, no API key, no patient data — standard library only, over the public
Open Targets and DGIdb GraphQL endpoints. Because it takes any gene symbol, the same
command works for the other MVA genes (`CEP57`, `TRIP13`) and for any undiagnosed
case whose causal gene turns out to be undruggable.

**Scoring.** Each neighbour scores `interaction_score × maturity`, where maturity
weights approved drugs (75%) over sheer count of known binders (25%). This ranks
*tractability*, not therapeutic merit — it is a hypothesis generator whose output is
meant to be filtered by mechanism and safety, which is what the report does. Ties at
the 0.40 interaction floor are real ties, not precision.
