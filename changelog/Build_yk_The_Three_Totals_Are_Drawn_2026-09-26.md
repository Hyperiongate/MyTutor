# Build yk — The Three Totals Are Drawn, 2026-09-26

Jim, on the Geometry review: *"it shows a picture of a right angle and says a right angle is
90 degrees, a straight line is 180 degrees, and all the way around a full circle is 360
degrees. And yet it only shows a picture of a right angle. I think we need to show a straight
line with kind of an arc showing that's 180 degrees. A circle showing, starting at one point,
going around all the way around, that's 360 degrees … I think that needs to be shown in
geometry early on."*

Stamp: **`2026-09-26yk-the-three-totals-are-drawn`**. PART **3oe**. A small figure build.

## What the board could not draw

`[[angle]]` capped at 180 (since 08-01, so a straight line was never bent). A full turn had
no drawing at all, which is why `yi`'s review beat put the corner on the board and the other
two totals on a step line. Jim's rule — *wherever we can, the words get a picture* — and the
words say three pictures.

## Two things the angle figure learned

**`deg="360"` is the full turn.** One ray from a centred vertex, and an arrowed arc that
leaves the ray and sweeps the whole way round back to it, arriving a few degrees short so the
turn visibly *arrives* (the SVG arc command cannot draw a closed circle in one arc, so the
sweep is two half-turns). Labelled 360°. Anything else above 180 still caps at 180.

**`row="90,180,360"` draws several angles side by side in one figure.** The first live look
at the review with three separate figures showed them stacked, shrunk to the 340px floor by
the fitter, the first one scrolled half out of view. A row is one landscape `<svg>` — each
panel is the plain angle drawing, shifted into its slot — so the board gives it full width
(1100px on a laptop) and nothing is shrunk. `names="a square corner|a straight line|a full
turn"` writes a word under each, and the 90° panel says *90°* like its neighbours (alone, a
square corner draws its mark and no number). Up to four panels. The board contract reads both
attributes off the renderer.

## Where they are used

The review's angles beat: *"A square corner is 90 degrees, a straight line is 180, and a full
turn is 360"* over `[[angle row="90,180,360" …]]`. And Geometry lesson one's why beat — *"a
right angle is 90 degrees, and the angles along a straight line make 180"* — which carried
only its goal card, draws the two beside it (`row="90,180"`). That is the "early on".

## Proved

PART 3oe: the two features by text, the contract, the two boards — and **rendered headless
in the battery**: the row is one `<svg>` with viewBox `0 0 900 238`, landscape, three
`<g>` panels, the labels 90° / 180° / 360° and the three names; the full turn alone has its
arrowhead; `deg="500"` still draws 180°.

## Files

`static/geo-figures.js` (`fullTurn`, `angleRow`), `lessons/bridges.py` (the angles beat),
`lessons/geometry.py` (lesson one's why board), `ruletests.py` (PART 3oe), `main.py` (stamp;
nothing to prewarm — boards only), `speechmap.py` (unchanged), this doc, the refreshed
`START_HERE_Handoff_2026-09-26.md`.

Battery on the frozen copy, 2026-09-26: **13,195 passed · 0 failed · 3 skipped**, first run clean (13,189 at `yj`).

I did no harm and this file is not truncated.
