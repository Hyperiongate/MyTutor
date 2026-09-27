# Build yp — The Facts Belong To Their Op, 2026-09-27

The first Basic quiz sweep, read on `yo`: **12 findings, 31 lessons clean.** Three classes,
none the reader's. And the first Pre-Algebra sweep (**6 findings, 30 clean**) landed while
the battery ran, so its three classes are folded in below — one push, not two.

Stamp: **`2026-09-27yp-the-facts-belong-to-their-op`**. PART **3oj**.

## Class one — a fact the bank kept by accident, printed, and enforced (4)

*"35 times 3 is outside the quiz space because the ones multiplication carries."* The QUIZ
SPACE had said *never — the ones carry*, because `_facts` measured the carry by **addition**
(5 + 3 < 10) on a multiplication bank, and every bank problem happened to agree. The reader
did what the page told it. Same on factor pairs: *"the two numbers add past ten"* — true of
12 and 6 as a and b, meaningless for the op, and the reader applied it to the factors 6 and
2.

`_facts(p, op)` now scopes them: the sum passes ten and the ones carry are `+`'s; the ones
borrow is `−`'s; and a new one for `/` — **the tens and the ones each divide by b**, the
taught tens-and-ones split, which is exactly what *56 ÷ 4* broke (50 ÷ 4 does not go) — the
sweep's two division findings, real. The rest (a bigger, a equals b, b divides a, the zeros,
the story) are every op's. A fact no longer measured is no longer printed, so it is no
longer enforced.

## Class two — a landmark value is a landmark (5, all on percent-of)

Percent-of's bank is 10, 25 and 50 — a tenth, a quarter, a half, each its own method, each
with its own array board. The quiz asked *20 percent of 5*, *36 percent of 25*, *45 percent
of 20*: inside the floor-to-ceiling range 10..50, outside the three values, and the board
for 45% said *"45% is one of 2 equal parts"* over a half-of-20 model that points at 10 while
the key is 9. Two HIGHs, words-board, real.

`shape_of` keeps a field's exact **value set** when the values are few and far apart — at
most four distinct values across a span at least ten times as many (10/25/50 over 41;
25/50/100; 90/180/270/360; the price-up lesson's 10/20/30/50) — and a digit field's 1, 2, 8, 9
over nine is not that. `keeps_shape` says *"a=45 not one of 10, 25, 50"*; the quiz page
prints *"a is one of 10, 25, 50 and nothing else"*. Percent-of's five and the price-up
lesson's two are replaced; every percent-of board now says what its words say.

## Class three — "2 and 5." was not a number (1, and 14 more)

The LCM quiz asked *2 and 5*, the worked line's own example, unmarked. `_INT_RE` refused a
digit followed by a period — meant to skip decimals, it skipped every number that ended a
sentence — so *"One more together. 2 and 5."* was never read as a demonstration. Fixed (a
trailing period is not a decimal point); fourteen more demonstrated questions came into
view and are replaced where their op had a fresh one.

## Folded in — the first Pre-Algebra quiz sweep (6)

**The same question twice (2).** *"How many different numbers divide 9 exactly?"* was turn 2
and turn 5 — two pinned problems, `a=9 b=8` and `a=9 b=2`, told apart by a b the child never
hears. And *76° on a line, how big is the other* then *104° on a line, how big is the other*
— the same pair both ways round. A question's identity in a quiz is **what the child
meets**: `drillpool.asked_as` (its spoken line and its board), and `twin_key` (the op, the
numbers and the answer as a multiset — 4 groups of 2 and 2 groups of 4 are one question).
`distinct_set` drops both kinds when a set is drawn; the generator replaces a later repeat
when the op has a fresh problem, and never with another repeat; `fresh_spares` is the one
owner of "could replace" (the generator and the battery both read it). Eighteen quizzes
had a twin; thirteen are replaced, one word-for-word repeat too; seven thin sets keep one.

**A proportion scales by a whole number (1).** *6 over 9 equals what over 21* — every bank
problem's c is a whole multiple of its b; 21 is not a multiple of 9. A new general fact for
three-number problems, `b_divides_c`, kept as a rule only when it *always* holds (a bank
where it never holds is an accident, not a rule — the first pass recorded five of those).

**The reader read the wrong number (1).** *"36 bottles in 9 hours"* was called above the
ceiling because the reader took 9 for a; a is 4 (the hours asked), b is 9, and the shape
allows it. Every quiz-ask line on the sweep page now ends with the question's own numbers —
`[a=4 b=9 c=36]` — and the charter says to judge the QUIZ SPACE against those.

The other two: the decimal-sharing repeat was already caught by the number-regex fix; the
40%-down one is gone with the landmark set.

**38 questions replaced** (7 outside a landmark set, 2 that do not split, 1 that does not
scale, 14 demonstrated, 13 twins, 1 asked the same way); 123 demonstrated ones stay, marked. **Prewarm: 38 new asks.**

## Proved

PART 3oj: `_facts` by op on fixtures (the sum and carry only for +, the borrow only for −,
the split for /, none of them for ×, the general ones everywhere); percent-of's landmark set
kept and 45% refused, the digit field's not; multiply's shape silent on the carry, divide's
saying the split, factor pairs' silent on the sum; the regex on *"2 and 5."* and *"5.2"*,
and the LCM line a demonstration; the three percents gone; every division splits; every
percent-of board matches its words; **every pinned question inside the yp shape**; the page's
wording; `asked_as`, `twin_key`, `distinct_set` on fixtures; **no quiz asks the same question
twice where its op had a fresh problem** (seven thin sets keep one); the factors quiz asks 9
once and the angles quiz has no pair both ways round; b divides c as an always-only rule; one
owner of "could replace"; every ask's numbers on the page and the charter's words; the dated
notes. One pin moved (3oi: a fresh question carries its numbers). The blanket counts re-anchored (course lines 40,543; closure
40,797; speechmap scan 40,849).

## Files

`drillpool.py` (`_facts(p, op)` with `b_divides_c`, landmark sets in `shape_of` /
`keeps_shape`, `_INT_RE`, `asked_as`, `twin_key`, `distinct_set`, `fresh_spares`, the
fallback lane), `coursesweep.py` (the landmark set, the split and every ask's numbers on
the quiz page; the charter), `tools/genquiz.py` (repeats and twins replaced; one owner of
"could replace"), `quizsets.py` (38 replaced), `speechmap.py` (regenerated), `main.py`
(stamp; prewarm 38), `ruletests.py` (PART 3oj; one pin moved; counts re-anchored), this
doc, the refreshed `START_HERE_Handoff_2026-09-27.md`.

Battery on the frozen copy, 2026-09-27: **13,271 passed · 0 failed · 3 skipped**, first run clean with the Pre-Algebra fold (the Basic-only run before it: 13,263 · 0 · 3) (13,251 at `yo`).

I did no harm and this file is not truncated.
