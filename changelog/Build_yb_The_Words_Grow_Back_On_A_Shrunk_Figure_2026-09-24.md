# Build yb — The Words Grow Back on a Shrunk Figure, 2026-09-24

The gate build `xy`'s instrument named: **the over-tall beat.** Built after `ya` in the same
session, while Jim was offline.

Stamp: **`2026-09-24yb-the-words-grow-back-on-a-shrunk-figure`**. PART **3nw**. A gate build.

## What the instrument said

`xy`'s survey of 45 lessons at 1280×900 left 29 LOW S9s: a beat whose bubble, figure and
step lines run past the board, so `pu`'s fitter shrinks the figure — proportionally since
`xy` fixed the NaN, to the 340px floor at worst. That is Jim's `pu` ruling working ("visible
without the student moving anything"). What was wrong with it was visible in the very
screenshot that proved the NaN fix: the array at 351px with its labels at 6px. The figure
was drawn for the full board, `vk` fitted its labels for that width, and the shrink scaled
the words down with the picture — the phone defect `vk` closed, reopened one build over by
the fitter.

## What changed

**The figure can be drawn for a known width.** `MathFigures.svg(kind, attrs, {room: px})`
tells `figFit` the width the figure will actually get; with no room given it measures the
board as before, so nothing else draws differently.

**The fitter draws again what it shrank.** `showFig` keeps the attributes on the wrapper;
after `fitTurnToBoard`'s passes settle, every figure it shrank is drawn again for the width
it now has (`figRedraw`: the `<svg>` alone is replaced — the wrapper, its caption, its kind,
its `maxWidth` and the `pu` bookkeeping stay; `data-pu-room` marks it). A restore draws the
figure for the full board first, so a window that grows back gets the full-board labels
back too. Geo figures are untouched — their viewBoxes are already narrower than a board.

**The instrument measures it.** `FIGURES_JS` reports every figure's smallest label in screen
pixels (font-size × drawn width ÷ viewBox width) and whether it was redrawn; **S10 — the
figure's words are readable** — fails a label under 9px. Fixtures both ways.

**And one figure fixed on the way.** The array's "N rows" label sat in the left margin with
the per-row counts and read "5 rows2" — by a few units at full size, by a lot once the labels
grow. It sits to the right of the dots now, in 110 units of room.

## Measured

`basic-u3-story-problems`, the lesson from the `xy` screenshot: every shrunk array is
redrawn, the smallest label 12–15px where it was 6px; the 340px floor case reads. PART 3nw
drives it every battery. What is *not* claimed: the S9 LOW count. The fitter still shrinks
the same beats by the same amounts — that is by design, and the honest next step, if Jim
wants the figures bigger on a laptop, is the beat itself (fewer step lines under a figure,
or a shorter bubble), which the instrument now counts per lesson.

## Files

`static/math-figures.js` (`svg(kind, a, {room})`; the array's row label), `static/board.js`
(`__figAttrs`, `figRedraw`, the redraw in `fitTurnToBoard` and on restore), `screencheck.py`
(`label_px`/`refit` in `FIGURES_JS`, S10, fixtures), `ruletests.py` (PART 3nw; one 3nt pin
widened for S10's place in the list), `main.py` (stamp), this doc, the refreshed
`START_HERE_Handoff_2026-09-24.md`.

Battery on the frozen copy, 2026-09-24 (ya + yb together): **13,097 passed · 0 failed · 3 skipped** (13,073 at `xz`).

I did no harm and this file is not truncated.
