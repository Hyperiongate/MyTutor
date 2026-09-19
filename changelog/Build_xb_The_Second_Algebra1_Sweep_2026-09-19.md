# Build xb — The Second Algebra I Sweep (2026-09-19)

REPORT HEADER (copied first): Course sweep -- algebra1 -- 2026-09-18 23:42 UTC (build xa).
Read by openai · gpt-5.5. By kind: words-board 23, unclear 14, false 11, untaught-term 1,
tone 1. 36 of 36 lessons read · 50 findings (6 on generators, 44 authored) · 10 lessons
clean · 0 unplaced · 0 unread · 46 minutes. The first sweep (wi, fixed in wk) was 72
findings, 8 clean.

The sixth course of the second round: **72 → 50 findings, 8 → 10 clean.** The first
reading after `xa` closed the near-repeat praise class, and the sweep did not raise it
once — six generator findings in all, three of them a reviewer habit this project has
already ruled on (reason choices are tap-only by design). The authored pile's class was
Algebra I's own: **the equation as given is missing from the board** — the undo pictures
start one step in, a substituted line has no "x = 4" beside it, the words point at
brackets the board does not show.

Stamp: **`2026-09-19xb-the-second-algebra1-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — two ops

- **`exmul`** (4): the praise said "3 times 4 equals 12 x's" over a caption that wrote
  `4 × 3`. One order everywhere now — *b* copies of *a* x's is "b times a" — in the ask's
  step line, the praise, the walk-back and its caption.
- **`sumd`** (1): the walk-back's thirty-word first sentence is three short ones.
- **Declined** (`roots`, 1): "the answer choices are not read aloud" — every tap question
  is tap-only by design (the `wx` ruling), and the same decline covers the three authored
  reason questions the sweep raised for the same reason.

## The authored pile (lessons/algebra1.py) — 42 edits

**The equation as given (words-board, 23).** Two-steps-back's worked line and reason board
open with the balance as given (`5x + 2 = 27`; `2x + 3 = 11`) before the undo pictures, and
the worked line writes `5x = 27 − 2 = 25`. The closing `3x + 2 = 3 × 4 + 2 = 14` carries
`x = 4` first (HIGH). `x + 4 < 11` before its undo. The swap picture draws the `x | y` bar
before the swapped one. Start-and-climb's closing board carries `y = 3x + 2` and the words
read it "at x equals 4". The lowest-point teach and recap boards carry `y = (x − 3)² + 2`,
the rule their words point at. The eraser lesson's board writes trip two (`5 + eraser = 9,
so eraser = 4`), which is what the words explain. `f(3) = feed f the number 3` → `f(3)
means: feed f the number 3`. The closing boards are read: "x is 3, two y's are 8, and
together they make 11"; "x plus 3 is less than 10, so x is less than 7"; "x squared is
25, so x is 5"; "the middle term 5 x". The common factor's bracket is spoken as "2 times
the whole of 5 x plus 2" (both worked lines). Half of 25 is "12 and a half", said and drawn
as `12.5`. "In one picture" → "in one line" where the board is a line. "Four children have
5 pencils each".

**Laws with their condition (false, 11).** The rectangle is "x take away 3 wide — x is
bigger than 3 here". A function: "for every number it is allowed to eat, exactly one
number comes out" (HIGH, why and recap). "For the rising lines in this lesson, every time
x steps one to the right, y climbs". "In these problems the buys differ by one pencil, so
one pencil is left alone" (HIGH); "this shopping system has two prices". "Multiplying
powers of the same base ADDS the counts" (HIGH, the advance line); "for whole-number powers
like these". "A rule like y equals x squared plus a number bends into a bowl".

**Unclear, untaught, tone (16).** "The input is the number that goes in" before the word
is used. "Feed them both a 4: the first machine puts out 9, the second puts out 10." "The
6 from machine one is the number timesed by 3"; "the 4 multiplies the 3 too". "A common
mix-up", not "the careless move". "Multiply the climb by x". "6 is the bigger answer".
Seven long sentences split (two-steps-with-a-letter, the-biggest-x ×2, undoing-a-plus,
two-machines, where-two-rules-agree, two-answers).

## Counts

Course lines **40,005** (no beat added); closure 40,259; speechmap **2,184** of 40,311;
forSpeech drift **1,878** — unchanged. `L.validate` over all 360: 0 failures (one caught
mid-build: a 37-word teach sentence). The referee sweep over all ten courses: still the one
intro card. Every new board line rendered headlessly with no `boardWarn`. PART **3mw** (8
checks). Two `wk` pins moved to the split sentences ("A product only ever lands on zero",
"The brackets on the board mean") — the first battery run caught them.

## After the push

Prewarm: exmul's lines, sumd's walk-backs, and roughly forty Algebra I rewrites. Then
**Geometry** against `wk`'s 63 findings, 7 clean (fixed in `wl`); then Prob/Stat and
Calculus's second reading.

## Battery

Frozen copy, 2026-09-19: **12,732 passed · 0 failed · 3 skipped** (12,724 at `xa`). The first run failed the two `wk` pins named above (12,730 · 2 · 3); the second run was clean.

I did no harm and this file is not truncated.
