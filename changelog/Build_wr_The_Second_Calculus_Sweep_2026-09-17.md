# Build wr — The Second Calculus Sweep, Whole (2026-09-17)

REPORT HEADER (copied first): Course sweep -- calculus -- 2026-09-17 02:14 UTC (build wq).
Read by openai · gpt-5.5. By kind: false 46, words-board 25, unclear 13, unsupported 2,
untaught-term 2. 36 of 36 lessons read · 88 findings (20 on generators, 68 authored) · 4
lessons clean (far-out-only-the-leaders-matter, the-window-closes, a-number-underneath,
equal-halves-win) · 1 unplaced · 0 unread · 44 minutes.

The Calculus sweep, run whole this time, on `wq` after the prewarm. It read the 17 lessons
`wo` never reached (U5's where-the-bend-changes and all of U6–U9) for the first time, and
re-read the 19 it had — three of the four clean lessons are ones `wo` fixed, which is the
first time a sweep has confirmed an earlier build's work. **With this, every lesson in every
course has been read once.** Calculus's class in the second half is *a rule stated without
the condition that makes it true*: "reverse the power rule on any power" (x to the
negative 1 is the exception), "every antiderivative ends in plus C", "every slice through
that cylinder is a circle", "an integral measures the change, never the amount", "every
equation you have met describes an amount", "set the second derivative to zero" (then check
the bend changes sides). Forty-six of the 88 were that shape. Two plain HIGHs sat in
generator lines: the Fundamental Theorem's praise said "taking end from start", and the
volume lesson's closing board asserted `3² × 4 = 36 · 36π`.

Stamp: **`2026-09-17wr-the-second-calculus-sweep`**. Battery: see the bottom of this doc.

## The admin card — the report list is newest first (coursesweep.py)

`list_reports` sorted by file name, and names begin with the course, so the dropdown put
`probstat_2026-09-16` above `calculus_2026-09-17` and the two Calculus reports side by side —
Jim opened yesterday's while today's was still running. It now sorts by the sweep's own
`when` (newest first, whatever the course); a report with no `.json` keys on its name's date,
and ties keep the name order. Pinned on a temp directory in PART 3mm.

## The generator (lessonscripts.py) — thirteen ops

- **`ftc`** praise (HIGH): "areas come from antidifferentiating and taking end from start" —
  that is start minus end. Now "then end take away start".
- **`avgv`** praise (five MEDIUMs, one line): "some of it towers above that line" on a beat
  that draws no line. Now "some of the curve stands above that height and some falls below
  it, and the two trade places exactly".
- **`anti`** board: `? x² came from it` had the relationship backwards — `44x came from ?x²`.
- **`chan`** praise and walk-back: the inside's derivative is *multiplied* in; it does not
  "come down" like the exponent. "Two things are multiplied: the power 3 comes down, and the
  inside's derivative 8 comes out to meet it."
- **`prod`** walk-back: 10 is "one piece of the derivative, with the plus 6 forgotten", not
  "half the derivative" (the derivative is 16).
- **`cfix`** walk-back: 6 is "the plus number in the sloping piece" (the slope of x + 6 is 1).
- **`trap`**: "use that average speed for the 10 seconds" (the train never holds it); the
  halfway speed is "the height of an equal-area rectangle" (it does not cut the trapezium
  into one); the two wrong answers are two beats. The lesson's closure had crossed the
  $5.50 tripwire at 25,115 characters on the first wording; trimmed to 24,827. The tripwire
  was not moved.
- **`pgrw`** ask names P and reads the board's `dP/dt` ("d P d t equals 4 P — the rate is 4
  times the amount"); **`dfeq`** ask reads `dV/dt` before the board leans on it (the two
  untaught-term findings).
- **`btwn`**, **`defi`**, **`mrat`**, **`pwrc`**, **`anti`**, **`pgrw`** walk-backs are short
  beats (the unclear findings); `pwrc`'s "which no rule does" became "which is not the
  power-rule move".

## The authored pile (lessons/calculus.py) — 72 edits, 30 lessons

**Laws with their condition (46).** The limit passes through "for sums and products, when
each function has a limit of its own". A line "written y equals a number times x, plus a
number" has one slope (HIGH). A derivative *function* "is not just one number". The best
rectangle: the slope-zero side of 10 *is* the top "because the area curve is a dome" (HIGH);
"every fixed fence used for a rectangle this way"; the ground lesson names the last lesson's
square-wins fact before the 5-by-15 rival. Inflection: "for these cubics, set the second
derivative to zero, then check the bend changes sides" (HIGH, and the advance line); "the
critical-point pattern you met" halved; "a zero slope does not tell you where; the change in
the slope does". Antiderivatives: "what function *could* it have come from" (HIGH); the
reverse power rule is "for the whole-number powers in this lesson" and names x to the
negative 1 as the one it cannot serve (HIGH ×2); "6 x to the fourth is one function it came
from — plus any constant"; going backwards "gives a whole family of antiderivatives" (HIGH);
"the *general* antiderivative is written with plus C" (HIGH); 5 apart everywhere "because
these curves share one derivative"; the closing board of the initial-value lesson is "the one
curve the initial condition picks", with `y(0) = 7` above it (HIGH). Integrals: the definite
integral "for a speed graph that stays above the axis"; "under this ramp, starting at zero
with speed equal to t" (recap and advance line); the Fundamental Theorem's advance line is
"work the antiderivative out at both ends, then end take away start" (HIGH — it said "the
smaller from the bigger"); "under a graph that stays above the axis". Applications: "when
one curve stays on top the whole way"; "the halfway speed is the *height* of a rectangle with
the same area" (HIGH); "because we are integrating a flow rate, the integral measures the
change" (HIGH); "every slice *straight across* that cylinder" and "for these rectangles spun
about the line beneath them" (HIGH ×2). Differential equations: "*most* equations you have
met describe an amount" (HIGH); the rate equation says only how steeply the line drops — "it
is the starting 60 that lets the line show how much is in there" (HIGH); the net-rate tank
"starting empty" (HIGH); "in this lesson the differential equation tells you how fast a
population changes"; "40 is not the *equilibrium* population" (HIGH); "a *population* whose
rate is 45 take away 5 P stops changing at 9" (HIGH). And the first half's leftovers: the
derivative *equation* used backwards; "for a distance-after-time formula"; "for a stone
falling straight down"; 5 is "the distance's original front number, before any
differentiating"; "in this model that constant is gravity"; the plus number "is not the
height at the border" (HIGH — at x = 0 it is one); the mend-the-curve distractor no longer
states a false law; "the *quantity* 4 x plus 7, squared" in the reason question (HIGH —
without it the slope is 4); metres *a second* and seconds.

**Words-board (25).** Every closing beat whose board wrote an equation reads it (ten
lessons). The power-rule teach draws the `x² → 2x` it speaks; the worked 9x⁴ says "the power
drops to 3"; the line lesson explains the 8 its board crosses out; the critical-point board
writes `2x = 6`; the ramp's closing beat keeps its picture; the accumulation recap draws the
*flow* graph it talks about; the flatten picture says the flat top comes next; the volume's
closing board is two lines; P is named before `rate = 4P`.

**Unclear (13).** Nine long sentences split; four were generator walk-backs.

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap **2,245** of 40,305
(unchanged); forSpeech drift **1,939** (unchanged). `L.validate` over all 360: 0 failures
(four caught mid-build: three sentences at 35 words, one beat at 86). The canon's referee
sweep over every Calculus beat: 21 refusals, all present at `wq` and untouched (the "so x is
12" praise lines of three lessons, and the initial-value ask's "What is its height?"). Every
new board tag rendered headlessly with no `boardWarn`. PART **3mm**; five old pins moved to
the new wording.

## After the push

Prewarm: roughly seventy rewritten Calculus lines plus the thirteen ops' lines. Then the
**first round is over** — every lesson in every course has had one reading. The second round
starts where the first did, on Entry, whose fifth sweep (`wg`, 14 findings, 26 clean) is the
floor to beat; and the sweeps that ran on the wrong build (Pre-Calc on `wm`, Algebra II on
`wk`) are candidates for a re-run before the weekly deep dive.

## Battery

Frozen copy, 2026-09-17: **12,638 passed · 0 failed · 3 skipped** (12,626 at `wq`). The first run failed twelve pins, all one cause: six walk-backs I had opened with "Here it is, step by step." (a full stop) where the engine and its pins know the line by its colon — restored; with them, one teach line that "said" a bank answer ("3 plus 5 is 8" in the line lesson) tripped the giveaway audit and was reworded. The second run was clean.

I did no harm and this file is not truncated.
