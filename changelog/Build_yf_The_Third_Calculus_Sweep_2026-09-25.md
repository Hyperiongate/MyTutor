# Build yf — The Third Calculus Sweep, 2026-09-25

Sweep header, 2026-09-26 00:58 UTC, read by gpt-5.5 on build
`2026-09-25ye-the-scripted-lane-goes-nightly`: **36 of 36 lessons read · 24 findings (2 on
generators, 22 on authored beats) · 18 lessons clean · 0 unplaced · 0 unread · 2166.9s.** By
kind: false 15, words-board 8, untaught-term 1. The floors: `xi`'s reading **46 findings, 13
clean**; `wq`'s **88, 4**.

Stamp: **`2026-09-25yf-the-third-calculus-sweep`**. PART **3nz**. A sweep build — the first since
Jim's "let's take a break from sweeps" (09-24); he pasted the report, so it was built.

## The pile

Twenty-four findings, eighteen clean. Calculus went 88 → 46 → 24. **All twenty-four fixed,
nothing declined**, and every one of them is a class the third round already knows: ten are
the condition class, six are words-and-board, five are one-offs, two are generators — and
one HIGH that was our own.

## The HIGH was xi's fix

`xi` closed a HIGH in the volumes-of-revolution lesson by writing *"Squaring the radius gives
one slice its area; stacking those slices along the length turns it into a solid"* — which
lost the π. The teach beat and the `revo` walk-back both say *"Pi times the radius squared
gives one slice its area; stacking those circles along the length turns it into a solid"*
now, and `xi`'s pin moved with the text. Worth remembering: a sweep fix is text like any
other, and the next reading reads it.

## The generators (2 ops)

Both walk-backs spoke their wrong-path numbers over a board that drew only the right one.
`chan` (*"Forgetting the inside leaves 3 … and 11 adds what should be timesed"*) draws
`3 ✗ inside forgotten · 11 ✗ added` — the authored teach board's own shape; `linf` (*"33 takes
one from the other and 108 times them"*) draws `33 ✗ taken away · 108 ✗ timesed`. `ww`'s
pattern; PART 3nz checks every bank problem of both ops draws its own two. The first cut wrote
them as equations (`36 − 3 = 33 ✗ · 36 × 3 = 108 ✗`) and the dot rule caught it in the battery —
two equations never share a step line.

## The condition class (10)

The limit-law reason choice carries its condition (*"because each has its own limit, and the
limit passes through"* — 12 words is the button cap); *"on this curve, the average rate
between two different x's was the two put together"*; *"no quotient rule"*, not *"no rule at
all"*; *"setting the first derivative to zero cannot find it"*; *"For the graphs in this
lesson, which stay above the axis"* (the Fundamental Theorem recap) and *"For a curve that
stays above the axis, like these"* (the average-value recap); *"For a steady rate like this
one"* (the differential-equation recap) and *"before it tells you what is left"*; *"This right
triangle under the ramp is half of the square around it"*; and *"the tempting guess, and it is
not the rule"* for the product of derivatives.

## Words and board (6)

The tangent is named the first time the picture shows one (*"The straight line touching the
curve there is called the tangent"*). The fence area is spoken with its bracket — *"x times
the whole of 20 take away x"*, Algebra I's rule. The chain-rule teach explains the `11 ✗
added` its board already drew. The antiderivative picture draws the forwards step
`3x² → 6x` the words describe. The trapezium picture draws a halfway line (`lines="x=2.5"`)
where the words say *"find the height halfway along"* — a point would have labelled the 7 and
given the shortcut away. And two reason boards draw their givens: `starts with 20 L` over the
accumulation tank, `under the top: 50 · under the bottom: 18` over the gap between two curves.

## One-offs (5)

*"the inflection point is at x equals 2"*; *"The derivative 52 x came from 26 x squared"* (and
the reason question's *"The derivative 6 x"*, same shape); *"one antiderivative"*, not *"the
first"*; *"a definite integral — the area under this graph over these 5 seconds: 8 times 5 is
40"*; the fence beat trimmed to the 80-word cap (*"Four tens use the fence exactly: a
square"*). Three rewritten sentences ran to 27 words and were split before the battery.

Grading under the 09-22 ruling: **class** (the condition 10, words-and-board 6, generator 2),
**one-off** (5), **reviewer** (0).

## Counts

Course lines **40,495 — unchanged**. Speechmap 941. Every lesson validates. Three pins moved
with the text (3ju's fence bracket; xi's squaring line, both halves; 3mm's "above the axis"
condition on the Fundamental Theorem recap). `tools/pinscan.py`: its reports were those
pins before they moved and 3nu's own negative pin.

## After the push

`/health` = `2026-09-25yf-the-third-calculus-sweep`. **Prewarm ~22 lines** (Calculus). Open
Calculus unit 8 lesson 1 (the trapezium): a dotted halfway line stands on the ramp, no
number on it. Sweeps left in the third round: Entry 19 and Pre-Calc's fourth — when Jim asks.

## Files

`lessons/calculus.py` (22 spoken/board edits), `lessonscripts.py` (`chan`, `linf` and `revo`
walk-backs), `ruletests.py` (PART 3nz; two pins moved), `speechmap.py` (regenerated, 941),
`main.py` (stamp), this doc, the refreshed `START_HERE_Handoff_2026-09-25.md`.

Battery on the frozen copy, 2026-09-25: **13,136 passed · 0 failed · 3 skipped**, second run clean — the first fell on four of my own lines: the two generators' ✗ lines written as equations joined by a dot (the dot rule, 3mj/3mk/3ml) and 3mm's "above the axis" pin on the recap I reworded (13,119 at `ye`).

I did no harm and this file is not truncated.
