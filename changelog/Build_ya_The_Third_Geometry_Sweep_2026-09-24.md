# Build ya — The Third Geometry Sweep, 2026-09-24

Sweep header, 2026-09-24 20:46 UTC, read by gpt-5.5 on build
`2026-09-24xy-the-two-flags-nobody-could-screenshot`: **36 of 36 lessons read · 11 findings
(0 on generators, 11 on authored beats) · 27 lessons clean · 0 unplaced · 0 unread ·
2141.2s.** By kind: false 8, words-board 3. The floors: `xb`'s reading **36 findings, 16
clean**; `wk`'s **63, 7**.

Stamp: **`2026-09-24ya-the-third-geometry-sweep`**. PART **3nv**. A sweep build (Jim pasted the
report as he went offline; built after `xz`, before the over-tall-beat gate build).

## The pile

Eleven findings, twenty-seven clean, no generator finding — the second course in a row with
none (Basic was the first, in `xz`). Geometry went 63 → 36 → 11. **All eleven fixed, nothing
declined**, and nothing in it was a new class: eight are the condition class the third round
keeps finding, three are words-and-board — and one of those three earned a new figure attribute.

## The condition class (8)

- **The inscribed angle (HIGH).** *"An angle with its corner on the rim is an inscribed angle,
  and it measures half the arc across from it"* — a corner on the rim is not enough; the arms
  must reach the rim too, and the arc is the one the angle *opens onto*. Now: *"An angle with
  its corner on the rim and both arms reaching the rim is an inscribed angle. It measures half
  the arc it opens onto."* (The why beat already said "with both arms reaching the circle"; the
  recap had dropped it.)
- **The flip, why and recap.** *"Every point jumps to the other side"* — a point on the mirror
  stays put. Both beats say so now: *"Every point off the mirror jumps to the other side, the
  same distance away; a point on the mirror stays put."*
- *"Everything else about the circle follows from"* the radius → *"every other measurement of
  the circle"*.
- *"A line segment — a line with two ends"* → *"a piece of a line with two ends"*.
- *"Never an add; adding bends the shape"* — not for a square → *"adding the same number to
  sides of different lengths bends the shape"*.
- *"Every arc is measured in degrees"* → *"In this lesson an arc is measured in degrees"*.
- *"The out-of number is always the whole bag"* → *"When the chance is a count from the bag,
  the out-of number is the whole bag."*

## Words and board (3)

**`[[graph segments="(1,3)-(1,8)"]]` is new.** The straight-up lesson said *"a segment
standing straight up on the grid, from (1, 3) to (1, 8)"* over `lines="x=1"` — the whole line.
`math-figures.js` draws the piece of line between two points now (thick, clipped to the
window, negatives allowed; rendered headless on both a vertical and a horizontal segment),
and all six of that lesson's boards — the picture, the teach, the recap, the reason question
and the two worked pairs — draw their segment instead of a line or bare dots. The board
contract picks the attribute up from the renderer, as with `xs`'s `field=`.

The reason question in the exterior-angle lesson names the 80 its board labels (*"angles of
40, 60 and 80, and the exterior angle beside the 80 is 100"*). The half-the-arc picture said
*"slide the corner … and the angle stays 40"* over one static drawing — it is a would-be now
(*"Put the corner anywhere else on the far side of the rim and the angle would still be 40"*),
which claims the fact without promising a picture.

Three rewritten sentences ran to 27–30 words and were split before the battery (3na caught
two in the smoke run). Grading under the 09-22 ruling: **class** (the condition, 8),
**one-off** (3).

## Counts

Course lines **40,495 — unchanged**. Speechmap 941. Every Geometry lesson validates. Two pins
moved with the text (3mc's `lines="x=1"` board; 3mh's line-segment sentence).
`tools/pinscan.py` clean.

## After the push

`/health` = `2026-09-24ya-the-third-geometry-sweep`. **Prewarm ~12 lines.** Open Geometry unit 7
lesson 1 (straight up): the segment from (1, 3) to (1, 8) is a thick bar between the two
dots now, not a line across the grid. Then the gate build the `xy` instrument named — the
over-tall beat — and the sweeps left: Calculus 46 (its third), Entry 19, Pre-Calc's fourth.

## Files

`lessons/geometry.py` (12 spoken edits, 6 boards), `static/math-figures.js` (`segments=`),
`ruletests.py` (PART 3nv; two pins moved), `speechmap.py` (regenerated, 941), `main.py`
(stamp), this doc, the refreshed `START_HERE_Handoff_2026-09-24.md`.

Battery on the frozen copy, 2026-09-24: two runs on ya's own tree reached 13,083 with one stale pin of mine each time (3mh's "along the far side of the rim", then a 3nt list pin that yb's S10 moved); the clean run is the one shared with `yb`, built in the same offline session: **13,097 passed · 0 failed · 3 skipped** (13,073 at `xz`).

I did no harm and this file is not truncated.
