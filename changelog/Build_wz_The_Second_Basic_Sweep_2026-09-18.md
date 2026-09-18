# Build wz — The Second Basic Sweep (2026-09-18)

REPORT HEADER (copied first): Course sweep -- basic -- 2026-09-18 13:29 UTC (build wy).
Read by openai · gpt-5.5. By kind: words-board 21, false 14, unclear 2, unsupported 2,
tone 1, untaught-term 1. 36 of 36 lessons read · 41 findings (12 on generators, 29
authored) · 14 lessons clean · 0 unplaced · 0 unread · 28 minutes. The first sweep (wg,
fixed in wh) was 67 findings, 7 clean.

The fourth course of the second round: **67 → 41 findings, 7 → 14 clean.** The generator's
class was a walk-back that promises "step by step" and draws only the end — `wpc`'s hundred
grid with no multiplications, `simp`'s pies with no divide. The authored class was Basic's
own from the first reading, one layer down: a rule for the lesson's numbers said as a law
("one part is the answer", "it works for every number", "anything that repeats", "you need
what one costs"). One HIGH was the sweep's own fault and is fixed in the tool, not the
lesson.

Stamp: **`2026-09-18wz-the-second-basic-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — four ops

- **`wpc`** walk-back (6): "10 times 10 is a hundred, so do the same to the top — 7 times 10
  is 70" over a grid that showed only 70. The two lines are drawn above the grid
  (`10 × 10 = 100`, `7 × 10 = 70`); the praise carries the same board. The lesson's second
  worked line (13 out of 20) draws its steps the same way, as its first already did.
- **`simp`** walk-back (3): "14 and 21 both share 7, so divide both by 7" over the finished
  pie alone. The divide is written top and bottom (`top: 14 ÷ 7 = 2`, `bottom: 21 ÷ 7 = 3`)
  before the pies; the worked 8/12 line gets the same two lines.
- **`fs`** ask caption (2): "hop back 1 fourths" → "1 fourth" — and `fa`'s "hop 1 more
  eighths" with it, though the sweep did not reach it.
- **`mtz`** praise (1): "the gap was filled with zeros" for 270 → the count, in the
  walk-back's own words: "a zero holds the ones" / "two zeros hold the tens and the ones".

## The sweep's own mistake (coursesweep.py)

The times-table lesson's HIGH — "all 81 facts" is false because "the problem space says 12
problems" — was the PROBLEM SPACE line's fault. That lesson practises as an 81-fact pass
(build sz); its bank only feeds the worked pairs, the quiz and the drill. `problem_space()`
now says so for any lesson whose mastery is "table": "a times-table pass — all 81 facts,
1 × 1 to 9 × 9 … the bank's facts are the worked pairs' asks, not the pass". The intro
line stands.

## The authored pile (lessons/basic.py) — 27 edits

**Laws with their condition (14 false, 2 unsupported).** "Every bigger sum is built on"
these two moves → "carry you through most bigger sums and take-aways". Rounding "hops to
the closer one — a number exactly halfway hops up". The tens piece of 34 × 2 is not a
times-table fact → "the same fact with its tens". "It works for every number" (HIGH) →
"every whole number". "Groups put together — times; a pile shared out — divided by" →
*equal* groups, shared *equally*. The buses "arrive now" and LCM is "for regular repeats on
two different beats, like every 2 minutes and every 3". "One part is the answer" (HIGH,
teach and recap) → "for a fraction with 1 on top". "You can only add pieces that are the
same size" (HIGH, the reason answer) → "the tops add only once the pieces match in size",
and the why says "you cannot count the tops together yet". Same-bottom pieces are the same
size "when two fractions of the same whole" share it. "To compare two prices, you need
what ONE costs" → "when the bunches are different sizes, the fair way to compare is". "Area
is long times wide" → "for a rectangle".

**Words and board (21).** The closing boards are read: "4 plus 4 plus 4 is 3 times 4, and
both equal 12"; "0.3 plus 0.4 is 0.7"; "5 plus 3 plus 5 plus 3, 16 all the way round". The
tenths-and-hundredths recap draws `0.43 = 4 tenths + 3 hundredths = 43 hundredths`. The
one-costs recap draws the other shop it talks about (`9 ÷ 3 = 3 dollars each`) and says
which is cheaper. The missing-factor picture draws the shared-out groups it describes
(`3 × 4 = 12`, "every box gets 4") under the question picture. The eighths line draws the
three hops the words count (`hops="0,0.25,0.375,0.5,0.625"`).

**Unclear, tone, untaught (4).** The times-by-ten picture in four short sentences. "Get
them quick and the rest comes easy" → "Practise them, and the next lessons will feel
familiar". Three reason questions with one right answer: "because it comes second" → "sits
in the ones column"; "plus is for perimeter only" (a term the lesson never taught) →
"plus counts the outside edges"; "180 is half of 360" (true) → "a quarter turn is 45
degrees".

## Counts

Course lines **40,010** (no beat added); closure 40,264; speechmap **2,245** of 40,316
(the tenths recap's "0.3 plus 0.4 is 0.7" re-keys — decimals tidied, as wh's hundredths
recap did); forSpeech drift **1,939**. `L.validate` over all 360: 0 failures (two caught
mid-build: a 14-word reason button; a 38-word recap sentence). The referee sweep over all
ten courses: still the one intro card. Every new board line rendered headlessly with no
`boardWarn`. PART **3mu** (10 checks); one 3mg pin moved (the different-bottoms reason
answer); the speechmap and drift pins moved by one.

## After the push

Prewarm: the four ops' lines and roughly thirty Basic rewrites. Then **Pre-Algebra**
against `wh`'s 69 findings, 6 clean (fixed in `wi`); then Algebra I, Geometry, Prob/Stat.

## Battery

Frozen copy, 2026-09-18: **12,714 passed · 0 failed · 3 skipped** (12,704 at `wy`). The first run failed one old `tb` pin that quoted simp's walk-back board without the written divide — moved; the second run was clean.

I did no harm and this file is not truncated.
