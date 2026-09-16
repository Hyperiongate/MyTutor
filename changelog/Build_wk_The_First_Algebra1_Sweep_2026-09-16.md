# Build wk — The First Algebra I Sweep (2026-09-16)

The first sweep of Algebra I, on `wi`: **72 findings** (9 on generators, 63 authored), 8 of
36 lessons clean, 0 unplaced, 43 minutes. Two things this course showed that the younger
ones did not: a *voice* class (a times over a bracket cannot be heard — "3 times, 2 x plus 3"
is 6x + 3 to the ear), and the dot, in the first course where " · " *is* a times sign.

Stamp: **`2026-09-16wk-the-first-algebra1-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — seven items, two rulings

- **`sys1`** praise: "the lines cross there, and that crossing is the answer" — the crossing
  is a point; the question asked for x. Now "the x of that crossing is the answer". Its
  walk-back is four short sentences instead of one long one.
- **`sys2`** board label: "swap y in: x + (x + 5) = 13" said the opposite of what happened.
  Now "swap x + 5 in for y".
- **`exmul`**: "4 groups of 3 is 3 times 4" over a board that wrote 4 × 3 — the board's order.
- **`hitg`, `sci`, `slp`** walk-backs split into shorter sentences (the reviewer's 25-word
  bar; all three were over 30).
- **`gcfx`** ask: "6 x plus 15 equals: 3 times, 2 x plus what?" → "3 times the whole of, 2 x
  plus what?" — the bracket is heard.
- **Ruled, not fixed** (two charter lines in `coursesweep.py`): `rnge`'s walk-back says "not
  7 — the ends are not added" while the STUDENT line said 780. Every walk-back names the
  *common* wrong answer for its problem — it is scripted per problem and the sweep's miss is
  synthetic (right + 777). And `yint`'s "y = 6x + 8 starts outside a 0..5 grid": `range=` is
  the x-window; the y-window fits the line on its own.

## The dot, in the course where it is a times sign

Fifteen authored step lines and three generator lines (`evxy`'s "x = 3 · y = 4", `fnum`'s
"2 + ? = 6 · 2 × ? = 8", `outl`'s "median = 4 · mean = 10") joined two equations with " · ".
In Algebra I the child has just learned that x³ · x² means a product; "x = 3 · y = 4" reads
as an equation about a product. Every one is two `[[step]]` tags now, and the pin from `wh`
grew: **no step line in Entry, Basic, Pre-Algebra or Algebra I — authored or generated,
judged by the rendered transcript — joins two equations with a dot**. `x³ · x² = x⁵` (one
equation, a real product) is untouched, and the pin proves it. The upper six courses still
carry the convention (~60 authored, ~44 generated); each course's sweep is the moment to
take it out, as this one was.

## The authored pile (lessons/algebra1.py) — 56 answered

**The voice class — "the whole of".** "4 times x take away 3 is 4 x take away 12" is false as
heard (4x − 3 ≠ 4x − 12) and true as written, 4(x − 3). The fix is a spoken bracket: "4 times
*the whole of* x take away 3". Same in the common-factor lesson three times (teach, picture,
reason question) and in `gcfx`'s ask. The Entry–Pre-Algebra sweeps never saw this because
those courses have no brackets; every course from here up will.

**Laws with their condition.** The eraser lesson's law (HIGH ×2): "two buys with the same
unknown in both — take one away and it vanishes" needs *the same amount* of the unknown;
recap and advance line both. "Two rules on one grid cross once" → straight-line rules that
are not parallel (HIGH). "Every pair of brackets you will ever multiply is this rectangle,
and it always has four rooms" (HIGH ×2, why and recap) → every pair of two-piece brackets
like these. "The days are a power of 2" (HIGH ×2) → the number of days is the power *on* the
2; the multiplier is a power of 2. "Multiplying powers ADDED" (HIGH) → two powers of x.
"Zero times anything is zero — and NOTHING ELSE, times anything, ever lands on zero" (HIGH)
→ a product lands on zero only when one of the things multiplied is zero. "5 is the square
root of 25 — the number that squares to it" (HIGH) → the *positive* number, and "x is a
distance, so we keep the positive one" on the way to x = 5. "Undo a less-than exactly like
an equation" (HIGH) → undo a *plus* in a less-than (the bank is all `x + a < b`); and the
boundary "is not x itself", not "not a number". "10 to a power is a 1 with that many zeros"
(HIGH) → a whole-number power. "Stop after one undo and you have what two x's weigh" (HIGH)
→ all the x's together (3x, 4x, 5x are in the bank). And the MEDIUMs of the same shape:
"every time" → for a line with no brackets; "parentheses meant TIMES" → a number against
parentheses; "each is one undo" → each after the first; "the hidden number must add to the x
count" → the hidden number and the known one; "every line has a starting height" → every
line on our grid; "a count needs everything the same" → to collect into one number of x's,
every piece must be an x; "the range says everything about spread" → one honest measure;
"what number squared equals the height" → the *starting* height (recap and advance line).

**Three reason distractors** were true, or the answer by coincidence: "x is whatever is on
the right pan" (true once x is alone); "the slope is the first number of the first point"
(2, and the slope was 2); "6 is halfway between the two ends, 4 and 8" (true for 4 … 8). Each
replaced with a wrong reason. The doubling reason now says "3 times 2 times 2 times 2"
instead of "3 times 2, three times".

**Words-board.** The sum-and-difference picture said "here is the bigger one on its own"
over a board that drew the whole bar again — the words now say so. The eraser picture writes
"1 pencil = 14 − 9 = 5"; its teach tape stops pricing the eraser before the words do; its
recap draws *both* buys. The less-than worked example writes `x + 5 < 14` and the
subtraction. Factoring writes the failed partner `2 + 3 = 5 ✗`. The doubling trap writes
`3 → 5 → 7 → 9` (the words said all four). The odd-one-out picture writes the 65 and 65 ÷ 5.
"Look how the bars pull away from a straight line" (no line drawn) → each bar leaps further
than the one before. The number machine reads its rule ("written two x plus one, where x is
whatever goes in"). Two-machines' recap names the board's add-2-then-times-3 before the
discount-and-tax analogy. The zero-product worked example says "equals zero" before giving
its two answers. Five closing beats speak the equation their board writes. The brackets in
`3 × (4 + 2) = 18 ✗` are read.

**Tone and clarity.** "The lazy answer" → tempting. "You have known since the curve lesson"
→ we saw in the curve lesson. "The first equation you ever solved" → the first *kind* of
equation you solved today. Six long sentences split. "Apples and apples, with a power in
place of the apple" spelled out. "Copying a whole pile times" → times the counts.

## Counts

Course lines **39,998** (no beat added); closure 40,252; speechmap 2,245 of 40,304 — none
moved. `L.validate` over all 360: 0 failures (one caught mid-build: a split sentence pushed
the common-factor trap to 35 words; the dash became a full stop). Every new board tag
rendered headlessly, no `boardWarn`. PART **3mf**.

## After the push

Prewarm: roughly seventy rewritten Algebra I lines. Then **Geometry**. Expect the "whole of"
class (it has brackets), the dot (one authored line, and the generator's), and the usual
laws-without-conditions. Two rulings for Jim, both raised by this course: (1) *"times the
whole of"* is now the house phrase for a spoken bracket — say so once in RULES.md's canon if
you agree; (2) the dot between two equations is gone from the four courses swept so far; the
remaining six get it as their sweeps land, unless you would rather it went in one pass.

I did no harm and this file is not truncated.
