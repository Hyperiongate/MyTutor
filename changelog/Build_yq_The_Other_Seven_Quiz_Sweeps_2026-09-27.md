# Build yq — The Other Seven Quiz Sweeps, 2026-09-27

Jim ran the remaining seven quiz sweeps back to back on `yo` and pasted them together:
**Algebra I 20 (25 clean), Geometry 6 (34), Algebra II 2 (34), Pre-Calc 9 (33), Calculus 7
(30), Diffeq 1 (35), Prob/Stat 5 (32)** — fifty findings, all on generators, none on
authored beats. With `ym` through `yp`, every one of the ten courses' quizzes has now been
read once.

Stamp: **`2026-09-27yq-the-other-seven-quiz-sweeps`**. PART **3ok**.

## Most of the fifty were `yp`'s classes, seen before `yp` shipped

The reports were read on `yo`. Twenty-three of the fifty are a fact the QUIZ SPACE printed
by accident and the reader enforced — *"the ones carry"* on complementary angles (five,
Geometry), *"add past ten"* on a line's start-plus-climb and on two machines in a row
(nine, Algebra I and Pre-Calc), the money-doubles interval — all scoped to their ops in
`yp` and no longer printed. Nine more were the reader taking the wrong number for a: *"x
equals 6 is outside 2..4"* on the derivative-at-a-point quiz, where x is c and c runs to 9;
the same on two-steps-with-a-letter, f-of-x, the power rule, the forbidden x. Every one is
inside its shape; `yp`'s `[a=.. b=.. c=..]` on each ask settles it, and no data changes.
Two twins (degrees 6 and 2, then 2 and 6) were already replaced by `yp`.

## New, one — "b never divides a" (11)

*"x plus 6 equals 12 is outside the quiz space because 12 divides by 6 exactly, breaking the
stated bank fact that b never divides a."* Nine lessons' banks — undoing a plus, the biggest
x, the range, the middle half's box, the jump, the trapezium's speeds — happened never to
have b dividing a, and the page said *never*. It is an accident of twelve problems, not a
rule of the lesson. Like `b_divides_c` in `yp`, **`b_divides_a` is a rule only when it
always holds** (sharing fairly, dividing two-digit: still *always*); a bank that never has
it records nothing, prints nothing, and the reader has nothing to enforce.

## New, two — a demonstration read two more ways (8, then 57)

The reader found worked examples my number rule had missed. The scatter-plot quiz drew
`[[scatter points="(2,10),(4,20),(6,25),(8,35),…"]]` and asked the dot at 8 — the very plot
of the teach beat; the arc quiz asked a 60-degree arc on a rim of 18 after the worked line
*"Central angle: 60 degrees — that is 6 equal parts, so the arc is 18 divided by 6"* — 60
and 18 with a 6 between them; the fair-prize quiz's *6 tokens, 25 percent* after *"6 tokens
a play, winning a quarter of the time: 600 over 25 wins"*. `demonstrated` now also (a)
matches a quiz ask's **board tag** against the teaching boards — same tag, same numeric
attributes, the picture *is* the example, whatever the numbers — and (b) allows **one
stranger** between the problem's numbers. Measured across the canon: 226 pinned questions
read as demonstrated; **57 replaced** where the op had a fresh problem; **169 stay, marked**
(the scatter lesson has one plot and no fresh point on it — its questions are the lesson's
own by design, and the page says so).

## New, three — the knife-edge asks in the lesson's own words (1)

Diffeq's one finding: the lesson teaches *"the middle squared must equal 4 times the last"*,
and the quiz asked *"With 24 on the y prime term, what must the plain y term be"* — two terms
it never taught. `cdmp`'s ask says *"With 24 in the middle, what must the last term be to
land exactly there?"* now. Its twelve bank asks and five quiz asks are new lines.

## Proved

PART 3ok: `b_divides_a` always-only (undoing-a-plus silent, sharing-fairly still *always*,
the nine banks record nothing); one stranger counts and two do not; a drawn board tag is a
demonstration; the fair-prize, median and arc repeats gone, the scatter one marked with no
fresh point; `cdmp`'s words and the lesson validating; the misread-number findings inside
their shapes with the numbers on the page; the dated notes. One pin moved (3oi's
demonstrated-stay ceiling, 130 → 180; its fixture's 7 + 5 became 7 + 4, one stranger apart
now). The blanket counts re-anchored (course lines 40,542; closure 40,796; speechmap scan
40,848).

## What Jim does

Push; `/health` says the yq stamp. **Prewarm: 74 new lines** (57 quiz asks + the
knife-edge's 17) — Price it, then render. The quiz instrument has now read every course
once; the second readings are the check. Run them in whatever order, back to back, and
paste together as before.

## Files

`drillpool.py` (`_ALWAYS_ONLY` gains `b_divides_a`; `_tag_sig`, `_DEMO_STRANGERS`, the two
new tests in `demonstrated`), `lessonscripts.py` (`cdmp` spoken), `tools/genquiz.py` (note),
`quizsets.py` (57 replaced), `speechmap.py` (regenerated), `main.py` (stamp; prewarm 74),
`ruletests.py` (PART 3ok; one pin moved; counts re-anchored), this doc, the refreshed
`START_HERE_Handoff_2026-09-27.md`.

Battery on the frozen copy, 2026-09-27: **13,279 passed · 0 failed · 3 skipped**, first run clean (13,271 at `yp`).

I did no harm and this file is not truncated.
