# Track 2 pitch video — 3 minutes

**Team Samistus1234 · MVA Hackathon 2026**
Target 2:55–3:00. Narrated film, no on-camera presenter. ~447 words at ~150 wpm.

**Compliance:** no patient identifiers, no images of the child or family, no clinical
detail beyond the released HPO phenotype. Framed throughout as research hypotheses.

---

## Shot list & narration

### 1 · The problem (0:00–0:25)
**Visual:** black; the phrase "fewer than 50 people worldwide" fades in, then the HPO
feature list assembling as text.

> A child somewhere is living with Mosaic Variegated Aneuploidy. Fewer than fifty people
> worldwide are known to have it. There is no established treatment. Their family opened
> that child's genome to strangers, hoping someone would find something.
>
> In Track One, we found it.

### 2 · The variant (0:25–0:50)
**Visual:** the leaderboard row — 100 rank points, F-max 1.000 — then the two variants
appearing on the BUB1B protein bar (Panel A of the mechanism figure).

> Compound-heterozygous BUB1B. A perfect match against the clinically confirmed answer.
>
> But a diagnosis is not a treatment. Track Two asks the harder question: knowing this,
> can anything be done?

### 3 · The wall (0:50–1:15)
**Visual:** terminal, live typing of `python3 repurpose.py --gene BUB1B`, output landing
on the line **"DGIdb knows 0 drugs."** Hold on the zero.

> Here is where rare-disease drug discovery usually ends. Ask any drug database what
> targets BUB1B and the answer is nothing. Zero compounds. The protein is a checkpoint
> scaffold nobody has ever built a drug against.
>
> So we stopped asking about the gene, and started asking about its neighbourhood.

### 4 · The insight (1:15–1:55)
**Visual:** Panel A→B of the mechanism figure — the truncation greying out the C-terminal
domain; then the second allele highlighted inside it.

> The two variants are not equivalent, and that turns out to be everything.
>
> One is a stop codon. That copy is destroyed before a protein is ever made — nothing to
> work with.
>
> The other is a single letter change inside the domain that holds BUBR1 folded. That copy
> makes a complete protein. The cell just throws it away too quickly.
>
> And when researchers took the equivalent mutants from patients with this combination and
> restored them to normal levels in human cells, the checkpoint came back completely. The
> defect is quantity, not quality. That is a target.

### 5 · The honest part (1:55–2:35)
**Visual:** three candidate cards sliding in, each stamped with its disqualifier in red.

> So which drug? We tested every axis the biology offers, and reported what we found
> rather than what we hoped.
>
> Boosting NAD-plus raises this protein in mice. But tumours run on NAD-plus — oncology
> builds drugs to deplete it. The evidence genuinely cuts both ways, and it has never been
> tested on a variant like this one. In a child who has already had a sarcoma, that is not
> a bet you make on untested mechanism.
>
> Senolytics clear the damaged cells aneuploidy leaves behind. But the standard senolytic
> is dasatinib, whose labelled harm in children is stunted growth — this child's own
> presenting complaint. And no senolytic regimen has ever been trialled in a child for that
> purpose. St Jude's study, in survivors of childhood cancer, set the minimum age at
> eighteen.
>
> And boosting the cell's protein-folding machinery — the most direct lever of the three —
> is precisely the antidote to the vulnerabilities that make aneuploid cells killable. In a
> child predisposed to cancer, that cuts both ways.

### 6 · The contribution (2:35–3:00)
**Visual:** the two experiments as a clean decision tree, then the repo URL.

> Which leaves the finding we would defend hardest. Nobody has ever measured what this
> variant does to protein levels. Nobody has ever measured the senescent burden in an MVA
> patient. There has never been a single registered trial for this disease.
>
> So we propose two cheap experiments on patient cells, designed to *refute* our own
> hypotheses before anyone reaches for a prescription.
>
> For a child with a cancer-predisposition syndrome, getting the order of the questions
> right matters more than another list of drugs.
>
> Code and full report — all of it open.

---

## Production notes

- **Narrator:** ElevenLabs, measured documentary register; no urgency, no sentimentality.
  The material carries itself.
- **Music:** sparse piano, low bed, ducking under narration; silence for the "zero" hold.
- **Type:** the mechanism figure's palette (`#0d1117` ground) so figure and titles match.
- **Pacing:** hold the terminal "0 drugs" for a full beat — it is the film's turn.
- **End card:** github.com/Samistus1234/mva-hackathon + "Hypotheses for laboratory
  follow-up. Not medical advice."

---

## Rendered output

- **Final video:** `mva_track2_pitch.mp4` — 2:45, 1920×1080, 25 fps, loudness-normalised
  to −16 LUFS. Not committed (13 MB); produced from the frames in this directory plus
  ElevenLabs narration, assembled with ffmpeg.
- **Frames:** `f1_problem.png` … `f6_end.png`, plus `terminal.png` (the stage-0 "0 drugs"
  moment). Rendered from HTML at 1920×1080 via headless Chrome, so every frame is
  reproducible and editable as text.
