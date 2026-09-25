# Build yd — Every Label Goes Through the Fit, 2026-09-25

What the ten-course screen survey asked for, and two of its own checks corrected.

Stamp: **`2026-09-25yd-every-label-goes-through-the-fit`**. PART **3nx**. A gate build.

## The survey, in one table

All 360 lessons at 1280×900, no errors: **0 lines below the fold, 0 unexplained figure-size
disagreements** in every course — the two flags `xy` set out to measure are closed
everywhere. 253 lessons have a beat the fitter shrinks (`pu`, by design). And **508 labels
under 9px**, in Algebra I and up: 473 of them the grapher's, the rest bars, histogram and
scatter.

## The grapher never had a fit

`graph()` opens its own `<svg>` — its viewBox grows leftward to make room for wide y labels
(`ua`) — so it never went through `svgOpen` and never set `vk`'s fit ratio; and its grid
numbers, point labels, legend, hole marker and axis letters were written with raw font
sizes besides. A graph drawn narrow, on a phone or by `pu`'s shrink, kept 7.7px numbers,
whatever `yb` re-fitted. Now `graph()` measures its room first (`_fit = figFit(S)`), every
label it writes reads `fitSize()`, the y-label margin grows with the fit, and `AXIS_LBL`
became `axisLbl()` so the x/y letters of bars, histogram and scatter fit too. A wide board
is byte-for-byte what it was (fit 1). `alg1-u4-reading-the-line`, the lesson with the most
small labels: every label 9.8–10px now, shrunk graphs included; no S10.

**One thing to look at, not changed:** even at full width a graph's grid numbers are 10
units on a 440-unit viewBox — 9.8px on a laptop. The fit only enlarges them when the graph
is drawn *narrower* than its viewBox. If they read small on your screen, the base size is a
one-number change (10 → 12) — your eye's call, since it changes every graph on every board.

## Two old checks, taught by the survey

**S5** ("the caption answers the question") fired 14 times where the caption merely
*repeats* the question — "two bars side by side — how much longer is the pencil?". A
caption that is itself a question answers nothing; S5 skips it. **S1** ("one formula, two
typographies") fired once, on Algebra II's *A new number*: `i² = −1` with a plain `i`
beside a styled `x`. That is the `gn2` case-sensitive table doing its job — `i` is a number,
drawn plain so it never reads as a variable — so S1 leaves `i` alone on a board that
carries `i²` or the word *imaginary*, and still fires on a plain `i` in an ordinary formula.
Three fixtures.

## Files

`static/math-figures.js` (the grapher's fit; `axisLbl()`; no raw label size left),
`screencheck.py` (S5, S1, three fixtures), `ruletests.py` (PART 3nx), `main.py` (stamp), this
doc, the refreshed `START_HERE_Handoff_2026-09-24.md`.

Battery on the frozen copy, 2026-09-25: **13,110 passed · 0 failed · 3 skipped** (13,098 at `yc`); the first run fell on one stale pin of mine (`ua`'s y-label margin, which now grows with the fit), the second clean.

I did no harm and this file is not truncated.
