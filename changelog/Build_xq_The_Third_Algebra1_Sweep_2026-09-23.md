# Build xq — The Third Algebra I Sweep, 2026-09-23

Stamp: **`2026-09-23xq-the-third-algebra1-sweep`**. PART **3nl**. The third round's Algebra I
reading — the first sweep run on `xp`, after two were lost to deploys on 09-22.

## The report (header, kept because the paste does not survive a compaction)

```
# Course sweep -- algebra1 -- 2026-09-23 02:22 UTC  (build 2026-09-23xp-the-sweep-survives-a-restart)
_By kind: false 8, repeats 6, words-board 5, unclear 3, untaught-term 1_
36 of 36 lessons read · 23 findings (9 on generators, 14 on authored beats) · 23 lessons clean · 0 unplaced · 0 unread · 2770.0s
```

**72 → 50 → 23 findings; 8 → 10 → 23 clean.** The xa praise class (near-repeats across 25 ops)
did not come up; the xb class (the equation as given missing from the board) did not come up.
The cycle converges.

## Grading, per the 09-22 ruling

**Class — fixed once in the generator.** `exadd` drew five "repeats" findings on one lesson,
and `yint` one: in both, the praise was the walk-back in other words ("3 x's joined by 7 more
x's — 10 x's multiplied, which is x to the power 10. The powers ADD." followed by "3 x's
joined by 7 more x's — count them … the counts ADD: x to the power 10"). Both sat under the
3nf word measure because the walk-back added a phrase or two. The rule stands: a praise is a
credit line. `exadd` now says "x to the power 10 — 3 plus 7: the powers ADD." and its
walk-back counts the piles one at a time — "count the first pile — 3 x's. Count the second
pile — 7 more. Two piles joined, so the counts ADD: 3 plus 7 equals 10, and 10 x's multiplied
is x to the power 10." — with `[[step eq="3 + 7 = 10"]]` added under the tape, the "new visual
step" the reviewer asked for. `yint`'s praise is "y is 3 — 4 times zero is nothing, so only the
plus 3 is left."; its walk-back keeps the steps. The walk-back playing after a right answer
over the same board is by design (ww) and stays.

**One-offs — fixed where quoted.** `outl`: the ask board showed `mean = 10` and the words never
said it; the ask now says "The mean is now 10 — but I am asking for the MEDIAN." `slp`: "When x
goes up by 1" for a step to the right — "When x steps 1 to the right, how much does y go up?"
`un3`: the walk-back spoke a check it did not draw — `[[step eq="2 × 5 + 4 = 14 ✓"]]` is the
last step line now (the referee passes it; the un3 shape pin moved with it).

**Authored — thirteen lines in `lessons/algebra1.py`.** Most are the law without its
condition, the class the 09-22 finding said has to be READ: the curve lesson said doubling and
squaring agree at 2 and "everywhere else it breaks" — they agree at zero too, and the line says
so now; "a single unusual number DRAGS the mean and leaves the median standing" → "In a group
like this one, …" (the HIGH); "every line on our grid has a starting height" → "on our grids, a
line has a starting height"; "half of the maths you will ever meet" → "a lot of the maths you
will meet"; "Every point is an input standing under its output" → "Every point on this line …"
(the other HIGH). Then the point-versus-coordinate pair in the crossing lesson: "the crossing
HAS the one x", teach and recap (the generator's own "the x of that crossing is the answer" was
already right). And the singles: "same letter, like x" for the untaught "base"; the pond's
recap tells the multiplier (a power of 2) from the number in all (the start times it — the
validator's canon word, not "total"); the four-rooms recap says "one pair … and every pair
like it opens the same way" over its one-pair board; "the slope is 5 take away 3, which is 2";
"Each right answer, 3 and 5, answers its own bracket"; the reading-the-line recap answers
every input "by one rule", since its board is the rule, not the picture.

**Refused — one.** "timesed" in a reason choice called nonstandard. "times / timesed /
timesing" is the course's verb for multiplying, in every course (Hundreds of lines). One
charter line in `coursesweep.py` says so; the choice keeps its word.

## Proven

PART 3nl: the five generator fixes (text, boards, the referee refusing none), the thirteen
authored lines by quote, the charter line, validate, counts unchanged (**40,495** course lines;
speechmap **941 of 40,801**), dated notes. Pins moved: two in 3mw (the four-rooms recap, the
counting-the-copies advance line), one in 3mf (the four-rooms count), one in the Algebra I
shape PART (un3's board). `pinscan` 0 misses; the five measures zero.

Battery on the frozen copy: **12,920 passed · 0 failed · 3 skipped** (12,907 at xp).

## After the push

`/health` = `2026-09-23xq-the-third-algebra1-sweep`. **Prewarm — about 50 lines** (exadd's
and yint's praises under three prefixes and their walk-backs, outl's and slp's asks, un3's
walk-back, the thirteen authored lines).

## Files

`lessonscripts.py`, `lessons/algebra1.py`, `coursesweep.py`, `ruletests.py` (PART 3nl),
`speechmap.py` (regenerated, unchanged in count), `main.py` (stamp), this doc, the refreshed
`START_HERE_Handoff_2026-09-23.md`.

I did no harm and this file is not truncated.
