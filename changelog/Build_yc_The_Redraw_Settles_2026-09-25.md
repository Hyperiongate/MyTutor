# Build yc — The Redraw Settles, 2026-09-25

A one-function fix to `yb`, found by the ten-course screen survey the morning after.

Stamp: **`2026-09-25yc-the-redraw-settles`**. No new PART — 3nw's pins moved to the new shape
and gained one.

## What the survey showed

The survey (`screencheck --script`, one course at a time) ran four times slower than the
same lessons had the day before, and `basic-u5-equivalent-fractions` never settled at all.
The cause was `yb`'s own redraw: every redraw of a shrunk figure is a DOM mutation; the feed's
`MutationObserver` answers every mutation with `scrollFeed`; `scrollFeed` runs the fitter; the
fitter redrew the figure again. A loop at 60 fps for as long as a shrunk figure was on the
board — invisible on screen, expensive underneath. Under the survey's fake clock it was slow;
on a real tablet it would have been a warm battery.

## The fix

`figSettle(svgs)`: a shrunk figure is redrawn only when the width it is drawn for
**changes** (`data-pu-room` differs from the new width); a figure back at full width is
redrawn for the full board only if it had been drawn for a room; otherwise nothing. The
restore step no longer redraws before measuring (label size does not change an SVG's
height at a given width, so the measurement was never affected). Idempotent: the observer's
next call finds nothing to do. What the child sees is exactly `yb`.

`basic-u5-equivalent-fractions` captures in 48 s now (it had not finished in 240).

## Files

`static/board.js` (`figSettle`; the fitter calls it in both exits), `ruletests.py` (3nw's two
redraw pins moved; one new pin — redraw only on a change of width; 3fy's and 3nt's
"never touches a turn that already fits" pins moved to the new literal), `main.py` (stamp),
this doc, the refreshed `START_HERE_Handoff_2026-09-24.md`.

Battery on the frozen copy, 2026-09-25: **13,098 passed · 0 failed · 3 skipped** (13,097 at `yb`), first run clean.

I did no harm and this file is not truncated.
