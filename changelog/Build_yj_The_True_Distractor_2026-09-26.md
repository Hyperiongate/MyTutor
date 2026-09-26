# Build yj — The True Distractor, 2026-09-26

The pre-sweep `yh` asked for. Jim: "Begin the true distractor pre-sweep."

Stamp: **`2026-09-26yj-the-true-distractor`**. PART **3od**. A pre-sweep build (the structural
kind — `xe`, `xf`, `xh`, `xj` — measure a class across the canon by machine, fix what it
finds, ratchet it).

## The class

`yh` found one in Pre-Calc: *"A puzzle with roots 2 and 6 ends in the number 12"* offered
*"because the end number is the bigger root, doubled"* — and 6 doubled **is** 12. A child
who taps it is right by the numbers and wrong by the reason, and the lesson grades it
wrong. That is a distractor that teaches the opposite of what it was written to catch.

## The instrument

`tools/distractorscan.py`. For each of the **292** reason questions (`lesson["explain"]`):
read the numbers out of the spoken question; take the one it presents as the result (the
number before *", not"* — *"is 6, not 12"* — else the last); for each wrong choice, read the
arithmetic its words name (added, times, take away, divided, doubled, halved, squared, root,
bigger, smaller, average, one more…) and compute it. Two tiers:

- **A verdict** — the choice names its own numbers and states a conclusion that is the
  result, and the arithmetic really reaches it: *"because 18 take away 12 is 6"* under *"the
  GCF of 12 and 18 is 6"*. Right by its own numbers. Three of these.
- **A candidate** — the choice is in words and its operation lands on the result over the
  question's numbers: *"the bigger root, doubled"*; *"the other angle is always twice the
  first"* (30 → 60). Read by hand: **34 at the first pass, 20 left after the fix**, and the
  twenty are the operation the question itself uses said as a false law (*"plus always moves
  you to the right"* under 3 plus negative 5), or a comparison (*"4 is bigger than 2"*) — a
  true remark, not a derivation of the answer.

`python tools/distractorscan.py` prints the hits; `--all` prints every judged choice.

## Eleven were right by the numbers

Three verdicts and eight candidates the reading confirmed. Each is false now, and each still
names a real misconception:

| lesson | was — and why it was true | now |
|---|---|---|
| Basic, GCF of 12 and 18 = 6 | *6 is half of 12* (12 ÷ 2 = 6); *18 take away 12 is 6* | *the greatest common factor is always the smaller number* (12); *12 and 18 share no factor bigger than 3* |
| Basic, factor pairs 18 & 2 → 9 | *18 take away 9 leaves 9* (circular, true) | *18 take away 2 leaves 16* (the named wrong answer) |
| Basic, perimeter 5 × 3 = 16 | *16 is twice 8* (true, and nearly the reason) | *5 plus 3 is the whole walk around* (8) |
| Pre-Algebra, ratio 2:3, 6 flour → 9 milk | *you add 3 to both sides* (6 + 3 = 9) — **`xa`'s own replacement** for an earlier true distractor (*"add 3 cups of milk"*) | *6 divided by 2 is 3, so the milk is 3* |
| Geometry, 30 and 60 make a corner | *the other angle is always twice the first* (2 × 30 = 60) | *the two angles always add to 180* (150) |
| Geometry, (3, 5) slides 4 right → x = 7 | *a slide right adds 4 to both numbers* (x becomes 7) | *a slide right adds 4 to y, never to x* (3) |
| Geometry, 3 → 6 so 5 → 10 | *the big side is always double, whatever the factor* (the factor is 2) | *the big side is always 6, whatever the small side* |
| Algebra II, \|3 − 8\| = 5 | *the take away was done the wrong way round* (8 − 3 = 5) | *the bars keep only the first number, 3* |
| Prob/Stat, 5 tokens, win 1 in 5, fair prize 25 | *a prize is always five times the stake* (5 × 5 = 25) | *a fair prize is always double the stake* (10) |
| Calculus, (5x + 3)⁶, front number 30 | *the power is always multiplied by five* (the inside is 5) | *the power is always multiplied by three* (18) |
| Calculus, 8t = 40 at t = 5 | *40 is divided by the distance's number* (40 ÷ 8 = 5) | *40 take away 8 is the time* (32) |

The ratio one is worth a line in the handoff: a sweep replaced a true distractor with
another true distractor, and nothing measured it until now. The instrument is what closes
that, not the reading.

## Proved

PART 3od: the scanner on known text (the result before *", not"*, the opener's own *"One
… not"* never counted, *"negative 4"* as −4; the three verdicts as they were; a stated
conclusion that is not the result is no verdict; Vieta's distractor is a candidate); **zero
verdicts across the canon**; the candidates ratcheted at 20 with the twenty named, so a new
one is read before the count moves; all 292 questions judged; the eleven by text; every
choice still a button (12 words) and every lesson validates. One pin moved (3md's ratio
distractor — which had pinned the true one).

## Files

`tools/distractorscan.py` (new), `lessons/basic.py`, `lessons/prealgebra.py`,
`lessons/geometry.py`, `lessons/algebra2.py`, `lessons/probstat.py`, `lessons/calculus.py`
(eleven choices), `ruletests.py` (PART 3od; one pin moved), `main.py` (stamp; nothing to
prewarm — choices are buttons, never spoken), `speechmap.py` (regenerated, unchanged), this
doc, the refreshed `START_HERE_Handoff_2026-09-26.md`.

Battery on the frozen copy, 2026-09-26: **13,189 passed · 0 failed · 3 skipped**, first run clean (13,174 at `yi`).

I did no harm and this file is not truncated.
