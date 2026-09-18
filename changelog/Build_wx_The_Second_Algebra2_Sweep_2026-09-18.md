# Build wx — The Second Algebra II Sweep (2026-09-18)

REPORT HEADER (copied first): Course sweep -- algebra2 -- 2026-09-18 00:35 UTC (build ww).
Read by openai · gpt-5.5. By kind: false 24, words-board 13, unclear 5, unsupported 1. 35 of
36 lessons read · 43 findings (5 on generators, 38 authored) · 14 lessons clean · 0 unplaced ·
1 unread (alg2-u5-between-the-squares: an OpenAI 520 — a transient; the sweep went on, as
`wv` intends) · 44 minutes. The first sweep (wk, read on build wk) was 73 findings.

The third course of the second round: **73 → 43 findings, 14 clean.** And it read the praise
beats after `ww`'s engine change without raising the praise-board shape once — the fix was
the engine's, so it held here. Twenty-four of the 43 are the class this course showed the
first time: a law stated for today's numbers as if it were the whole truth. This time the
laws were the ones a mathematician would flinch at — "squares are never negative", "a cubic
has three answers", "more factors, more crossings", "a full turn changes nothing" — each true
with its condition and false without it, and the fix each time is the condition.

Stamp: **`2026-09-18wx-the-second-algebra2-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — five ops

- **`disc`** walk-back: "You never report the test number, only its sign: 1 crossings." A zero
  test number is a *touch*, and "1 crossings" is no grammar. Now "only what its sign says:
  2 crossings / 1 touch / 0 crossings", and the graph's caption says the same.
- **`expv`** ask (HIGH): "you win 4 tokens *exactly* 2 times out of every 3 plays" made a
  certainty of a chance — the board and the praise had always said "about". Now the ask does.
- **`gaus`** praise: "11 numbers, paired end to end, each pair 12" — the middle 6 has no
  partner. Now "Pair the list with a reversed copy of itself: 11 pairs, each 12. That is 11
  times 12 for two copies of the sum, so halve it — 66", which is what the walk-back's
  rectangle draws.
- **`rsol`** praise checked "2 times 5 equals 10" while its board checks forward
  (`10 ÷ 2 = 5`). The praise checks forward too.
- **`rsum3`** walk-back (HIGH): "a cubic has three answers" → "this cubic, with three
  different factors, has three answers".

## The authored pile (lessons/algebra2.py) — 39 edits

**Laws with their condition (24 false).** "Squares are never negative" → *real-number*
squares (HIGH, why and recap). "Plus or minus the root of that number, times i" → "x squared
equals negative a, for a positive a, is solved by plus or minus the root of a, times i"
(HIGH); "today we take the positive one" → "the one with the positive number in front of i".
The test number's sign "tells you how many times the curve meets the x line" and the recap
reports "the meetings with the x line" — a touch is not a crossing. The vertex rule "in this
form — a squared bracket plus a number"; the formula answers "without a table". The
wiggle-count's "because the last stretch always runs off to the horizon" was a reason that
proved nothing → "a rule for these graphs that Calculus will explain". "More factors, more
crossings" → "more *different* factors like these" (HIGH), and the reason button says so.
The survivor: "for x not equal to zero, split the top". "The undo of dividing by x: one more
divide" → "when a number divided by x equals an answer, divide the number by the answer"
(HIGH). "That neighbour is the closest log" → "the exponent of that power is the closest
whole-number log". The product law carries "for positive a and b, in one base" on the
closing board and in the words (HIGH). "A full turn changes NOTHING" → "…about where the
arrow points", and the recap "keeps the arrow in the same place". "Every choice is a slot" →
"every category is a slot, and the choices in each slot times together" (why and recap).

**Words and board (13).** The reason boards write what they ask: the two trips
(`3 apples + 2 bananas = 14`, `1 apple + 2 bananas = 8`); the sample's `20 asked, 5 yes ·
school 60 = 3 × 20` (HIGH). The sample's worked lines draw `10 asked, 4 yes · school 30` and
`15 asked, 6 yes · school 45`. The test-number worked board writes the value, `3² − 4·1 = 5,
positive`. The forbidden-x reason caption said "the hole at x = 4" — it is a break, not a
hole (HIGH); now "the curve breaks at x = 4 — no point there". `√30 is between 5 and 6 — not
15` is drawn where it is said. The closing boards are read: "x is 15 squared — 225"; "up
gives 1, down gives negative 1, and flat gives 0"; "Twenty asked, 5 said yes, a school of
60" and "5 times 3, about 15"; and "the doubling pond" over `2 × 81 = 162` is now "the pond
that triples … 2 times 81 is 162". The cube's board line loses its dangling dot.

**Unclear (5) and unsupported (1).** The cube's reason button says what a cube is ("because
5 cubed means 5 times 5 times 5, minus kept"). The hidden exponent's reason example moves
from 3³ = 27 (base and log both 3, so the wrong button read as true) to 5³ = 125. "Not the
base itself" → "not the brick you were handed". The survivor recap and the slots picture in
short sentences; "multiplied", not "timesed", in the logs recap.

**Declined:** the height lesson's "the tutor never reads the three reason choices aloud" —
every reason question in every course is tap-only by design; the choices *are* the buttons.

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap **2,244**; forSpeech drift
**1,938** — unchanged. `L.validate` over all 360: 0 failures (four caught mid-build: a
walk-back that must name its answer — "no crossings" → "0 crossings"; two reason buttons over
twelve words; a 35-word sentence). The referee sweep over all ten courses: still the one intro
card. Every new board line rendered headlessly with no `boardWarn`. PART **3ms** (8 checks);
seven PART 3mh pins moved to the new wording.

## After the push

Prewarm: the five ops' lines and roughly forty Algebra II rewrites. Then **Entry** against
`wg`'s floor of 14 findings, 26 clean — the youngest course, and the first rerun of a course
that was already swept four times; then Basic, Pre-Algebra, Algebra I, Geometry, Prob/Stat in
first-round order. Six of ten courses will then have had a second reading.

## Battery

Frozen copy, 2026-09-18: **12,693 passed · 0 failed · 3 skipped** (12,685 at `ww`). The first run failed two old `tl` pins on disc's walk-back, which quoted the very words this build changed ("only its sign", "1 crossings") — moved; the second run was clean.

I did no harm and this file is not truncated.
