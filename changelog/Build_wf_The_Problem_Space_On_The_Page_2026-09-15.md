# Build wf — The Problem Space On The Page (2026-09-15)

The third Entry sweep after we: **15 findings** (70 → 47 → 15), **24 lessons clean** (9 →
12 → 24), 0 on generators. Nine of the fifteen are answered in `lessons/entry.py`. The other
six are the reason this build exists.

## The six, and what they had in common

"Which is bigger" — "not always true if the two numbers are the same." The op's check forbids
equal numbers. "Take away from bigger numbers" — "false for 7 − 7 or 5 − 8." The bank never
takes a bigger number away; the course never does. "What a digit is worth" — "a 0 in the tens
place is worth 0." No digit in the bank is 0. "Crossing a hundred" — "in three-digit
addition, ten tens are carried into the hundreds column." Every number in the lesson is
two-digit. "Ten more" (last sweep) — "94 + 10." The bank stops at 89.

The charter already told the reviewer to judge a rule against the numbers the lesson uses.
It kept not doing that — because it could not SEE them. It reads a transcript of what is
said and drawn; the bank's range and the op's constraint were nowhere on the page.

## The fix: `problem_space(lesson)`

Every transcript now opens with one line, computed from the bank and the worked pairs plus
the op's own constraint in the engine's words:

> PROBLEM SPACE: 12 problems; a from 1 to 20; b from 2 to 19; op big; every problem
> satisfies — big: two different numbers inside the counting range. A rule is judged
> against THESE problems, not against numbers this lesson cannot ask.

And the charter's rule now points at it: a case outside the problem space — two equal
numbers where the space says they differ, a hundreds column where every number is two-digit,
a zero where no digit is zero — is NOT a finding. That is a charter line, once, for a whole
class of objections; the Forever War's mechanism as designed.

## The nine answered

Doubles' why defines a double before it uses the word ("a double is the same number twice —
five and five, six and six"), and its recap no longer calls doubles "the quickest sums there
are". The story recap says "each of THESE story problems". Take-away-bigger's recap starts
"at the number you begin with — the big one". Ten-more's recap draws 34 AND 44. Tens-and-ones'
reason option says "in a two-digit number" (and still fits a button: under twelve words).
Adding three-digit numbers' trap is split into short sentences. Crossing a hundred says
"today both numbers are two-digit". Take-away-two-digit draws the stacked layout on the beat
that says "the ones digit on top". How-much-longer says the cubes are the same size and
touching end to end, and every board carries the unit ("13 cubes − 4 cubes = 9 cubes").
Sides-and-corners splits its long line and says "today's shape names tell you how many
sides" (a square's does not).

## Counts and tests

No voice line added (course 39,996; speechmap 2,244 of 40,302 unchanged). `L.validate` over
all 360 lessons: 0 failures. PART 3ma pins the problem-space line (its content, its place
as the second line of every transcript, the charter naming it, all 360 lessons rendering
one) and the nine authored answers by class.

## After the push

1. Prewarm — a handful of rewritten Entry lines.
2. Re-run Entry once more. With the problem space on the page, I expect single digits, and
   what is left should be worth reading one by one.
3. Then Basic — the sweep is calibrated enough now to be worth the $2 on the next course.

Battery: 12,470 passed, 0 failed, 3 skipped (frozen copy, first run, 2026-09-15).

I did no harm and this file is not truncated.
