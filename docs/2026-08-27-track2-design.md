# Track 2 Design — Drug Repurposing for MVA (BUB1B compound-het proband)

*MVA Hackathon 2026 · Track 2 · Team Samistus1234 · designed 2026-08-27*

## Goal

One-shot Track 2 submission (deadline 2026-10-24): a written report proposing repositioned
drug candidates grounded in the proband's confirmed genotype, a public reproducible
pipeline, and a 3-minute pitch video. Judged 35% scientific rigor / 25% potential impact /
25% innovation / 15% scalability.

## Scientific spine — allele-aware mechanism

The proband (Track 1, scored 100/1.000) carries compound-heterozygous BUB1B:

- **p.Leu737Ter** (chr15:40209701 T>G) — premature stop; transcript expected to undergo
  nonsense-mediated decay → effectively a null allele.
- **p.Asn1002Lys** (chr15:40220612 T>G) — C-terminal (kinase-domain) missense; produces a
  full-length, presumably hypomorphic protein.

Consequence: **BUBR1 insufficiency**, not absence — weakened spindle-assembly checkpoint
and kinetochore error correction → chromosome missegregation → mosaic aneuploidy →
p16/p21 senescence induction, growth failure, and tumor predisposition (matches the
child's rhabdomyosarcoma, IUGR/short stature, nephrocalcinosis; parental recurrent
miscarriage matches embryonic aneuploidy).

The therapeutic logic exploits the asymmetry: the missense allele's full-length protein is
a substrate for **stabilization** (raise residual BUBR1 dose), and the downstream
senescent-cell burden is a substrate for **clearance**.

## Ranked candidates (to be PMID-verified before drafting)

1. **NAD⁺ repletion — nicotinamide riboside / NMN.** SIRT2 deacetylates BubR1 and
   prevents its degradation; NAD⁺ precursor supplementation raised BubR1 levels and
   extended lifespan in Bub1b hypomorphic mice (North et al., EMBO J 2014). Allele-aware
   fit: stabilize p.Asn1002Lys protein.
2. **Senolytics — dasatinib + quercetin; fisetin.** The Bub1b^H/H mouse is the model in
   which clearance of p16^Ink4a-positive senescent cells was first shown to delay
   ageing-associated degeneration (Baker et al., Nature 2011). Dasatinib has established
   pediatric dosing (CML). Positioned strictly as a research hypothesis with oncology
   caveats.
3. **Adjunct tier (conditional on evidence surviving verification)** — e.g., rapamycin /
   mTOR inhibition for senescence attenuation. Included only with primary-source support.

All claims verified against primary papers (PMIDs), per the verify-before-fixing
discipline; explicit "hypotheses for investigation, not medical advice" framing and
pediatric-oncology safety section.

## Reproducible pipeline (innovation + scalability)

`track2/repurpose.py` — CLI: gene(s) + mechanism class → ranked candidate table, querying
Open Targets / DGIdb public APIs; committed outputs for BUB1B (and the other MVA genes
CEP57/TRIP13 as generalization demos). Monitoring/biomarker section (micronucleus assay,
aneuploidy fraction, p16 expression) shows how candidates would be evaluated in any MVA
patient.

## Repo layout

Rename canonical repo `mva-hackathon-track1` → **`mva-hackathon`** (GitHub redirects the
submitted Track 1 URL). Add:

```
track2/
  report/samistus1234_track2_report.md   # the submission report
  repurpose.py                           # pipeline CLI
  outputs/                               # committed candidate tables
  video/script.md                        # pitch narration + shot list
docs/2026-08-27-track2-design.md         # this design
```

No patient data anywhere in the repo (unchanged rule).

## Video (3 min, narrated film)

Local pipeline (ffmpeg + ElevenLabs narrator + licensed music): child's story → variant
find (leaderboard capture) → mechanism animation (diagram frames) → two-pronged
therapeutic logic → scalability close. ~420-word script. Risks: ElevenLabs billing (402
seen previously — verify credits first; fallback: alternate TTS or user-recorded VO).
Upload target YouTube/Vimeo staged for the user to approve/publish.

## Quality gates & submission

1. Research verification sweep (primary sources) → 2. report draft → 3. pipeline built +
outputs committed → 4. independent fresh-context adversarial review (refute-first, two
passes, different agents) → 5. video render → 6. user reviews everything → 7. user gives
explicit go → submit via Space form (report file + GitHub URL + video URL). 0/1 slot —
nothing is uploaded without the user's sign-off.
