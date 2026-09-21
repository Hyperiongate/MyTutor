# Build xc — The Second Geometry Sweep (2026-09-19)

REPORT HEADER (copied first): Course sweep -- geometry -- 2026-09-19 01:52 UTC (build xb).
Read by openai · gpt-5.5. By kind: words-board 18, unclear 9, false 7, untaught-term 2. 36
of 36 lessons read · 36 findings (8 on generators, 28 authored) · 16 lessons clean · 0
unplaced · 0 unread · 38 minutes. The first sweep (wk, fixed in wl) was 63 findings, 7
clean.

The seventh course of the second round: **63 → 36 findings, 7 → 16 clean** — the best
second-round drop yet, and the most clean lessons after Entry. Eight generator findings on
three ops, one of them the reading's only real HIGH on the engine: the inscribed-angle
walk-back gave a *false reason for a true rule* ("the rim is farther away, and from
farther away it looks exactly half"). The lesson's own beats were fixed in `wl`; the
walk-back had kept the old reason. The authored class was Geometry's own: **the picture
the words describe is not on the board** — an exterior angle spoken over a plain
triangle, a segment spoken over two dots, a table's traps spoken over three step lines.

Stamp: **`2026-09-19xc-the-second-geometry-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — three ops

- **`insc`** walk-back (HIGH): "from the rim the arc looks half … the rim is farther away,
  and from farther away it looks exactly half" → "an angle on the rim opening onto an arc
  is half that arc. 36 divided by 2 equals 18 degrees. From the middle the same arc would
  be 36: the middle angle equals its arc, and the rim angle is half of it." The `tk` pin
  that guarded the old reason moved with it.
- **`outc`** walk-back (6): "adding gives 8 things, not outfits" over a board that drew only
  `6 × 2 = 12`; the wrong path is drawn (`6 + 2 = 8 ✗ things, not outfits`).
- **`alen`** walk-back (1): the first sentence split in two.

## The authored pile (lessons/geometry.py) — 29 edits

**The picture the words describe (words-board, 18).** The exterior-angle picture (HIGH)
now draws the straight line the words stand the 80 and the 100 on (`[[angle deg="180"
split="80,100"]]` after the triangle). The straight-up segment is drawn along its line
(`lines="x=1"` through both ends). The two-way table sits under the traps beat, with its
caption naming the next-door boxes. The hypotenuse worked line draws `9² + 12² = 81 + 144
= 225` and `15 × 15 = 225`. "The base angles waiting" → "filled in: 70 and 70. Here is
where they came from." The closing boards are read: "180 take away 50 is 130 next door,
and the twins across match"; "180 take away the pair's 104 leaves 76"; "12 divided by 4 is
3"; "opposite equals 5 times 4, which is 20"; "3 squared plus 4 squared is 5 squared"; "6
times 4 is 24"; "girls row, soccer column, 2".

**Laws with their condition (false, 7).** "The line is 8 long" → "the segment" (teach and
the reason choice). "Stand at an angle in a right triangle" → "one of the sharp angles".
"The straight path is ALWAYS shorter" (HIGH, teach and recap) → "for a slant like this —
an across AND an up"; "whenever there is both an across and an up". "Choices do not add up;
they times up" → "when every shirt can go with every hat". The enlarging-copy ✗ line said
the 5 was "the short side" — it is the long one, and adding grew it *too little*.

**Untaught and unclear (11).** "A radius is a line from the middle of a circle to its rim"
before "radiuses" is used. "The tangent — written tan on the board — is 8 divided by 4"
before the caption writes `tan`. Eight long sentences split (the factor's why and teach,
the missing leg ×2, the tangent recap, the rim teach, the fourth corner ×2).

## Counts

Course lines **40,005** (no beat added); closure 40,259; speechmap **2,184** of 40,311;
forSpeech drift **1,878** — unchanged. `L.validate` over all 360: 0 failures. The referee
sweep over all ten courses: still the one intro card. Every new board line rendered
headlessly with no `boardWarn`. PART **3mx** (7 checks). Three pins moved — `tk`'s insc reason,
and two `wl` pins the first battery run caught (the fourth-corner sentence now starts "In these
puzzles"; "stand at" became "stand at one of the sharp angles") — each marked "(xc)".

## After the push

Prewarm: the three ops' lines and roughly thirty Geometry rewrites. Then **Prob/Stat**
against `wo`'s 92 findings, 1 clean (fixed in `wq`) — the last first-round course with a
single reading — and then Calculus's second reading (`wq`'s 88, 4 clean, fixed in `wr`).

## Battery

Frozen copy, 2026-09-19: **12,739 passed · 0 failed · 3 skipped** (12,732 at `xb`). The first run failed the two `wl` pins named above (12,737 · 2 · 3); the second run was clean.

I did no harm and this file is not truncated.
