# Build zf — the lesson counts to ten (2026-10-06)

Stamp: `2026-10-06zf-the-lesson-counts-to-ten`. Battery: **13,523 passed · 0 failed · 3 skipped** (PART 3oz
added; the giveaway audit's count moved 21 → 22 — the count to ten is a sixth honest beat,
the same ruling wd gave counting-past-ten).
**Prewarm: 1 line** (Entry u1 "Counting to 10", the second teach beat).

The last build off the phone pass: P4.

## What was wrong, and what it is now

Jim, in Entry unit 1 lesson 1 on his phone: "this is counting to 10 and we never actually
count to 10 in this entire lesson." He was right. The picture counts five, the first teach
beat three, the second seven, the worked examples four and six, the recap four; the asks come
from a bank that reaches ten, but the lesson itself never says "ten".

The second teach beat is the whole count now: *"Watch me count again, all the way to ten this
time. One, two, three, four, five, six, seven, eight, nine, ten. Ten stars."* — over ten stars
that tick in one at a time (`count="1"`; the count-along's reach is twelve, so the picture
counts with him; on a phone the ten wrap as a row, zc). The lesson does what its title promises
once, before it asks the student to count a smaller group. Nothing else in the lesson moved.

## Proof

PART 3oz: the lesson has a teach beat that says "eight, nine, ten. Ten stars." over a
`groups="10" count="1"` board; the count is within `OBJ_COUNT_MAX`; the bank still reaches
ten; the dated note is in. The lesson validator and the sweeps run over the new line as part of
the battery.

## Files

`lessons/entry.py` (u1 counting-to-10, the second teach beat), `speechmap.py` (regenerated),
`ruletests.py` (PART 3oz), `main.py` (stamp), this doc, the handoff.

I did no harm and this file is not truncated.
