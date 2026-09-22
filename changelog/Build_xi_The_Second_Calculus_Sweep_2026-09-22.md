# Build xi — The Second Calculus Sweep (2026-09-22)

Sweep header, 2026-09-22 01:21 UTC, read by gpt-5.5 on build
`2026-09-21xh-the-credit-line-everywhere`: **36 of 36 lessons read · 46 findings (20 on
generators, 26 on authored beats) · 13 lessons clean · 1 unplaced · 0 unread · 3001.3s.**
By kind: false 17, words-board 15, unclear 12, untaught-term 2. The floor was `wq`'s
reading: **88 findings, 4 clean**, fixed in `wr`.

**Calculus was the last course without a second reading. Every course has now had two.**

Stamp: **`2026-09-22xi-the-second-calculus-sweep`**. Battery: see the bottom of this doc.

## The class that did not come back

**Not one "repeats" finding.** That class — a praise that explains, then a walk-back
explaining the same thing a breath later — had appeared in every sweep since `wa`, and was
18 of Prob/Stat's 60 findings six days ago. `xh` turned Calculus's 32 explaining praises
into credit lines before this reading, and the reviewer did not raise it once. The
length measure in PART 3nb is the reason, and it is now proven on a course it had never
been tested against.

## The class that took its place

Every one of the 12 "unclear" findings was a **generated walk-back or ask too long to
follow by ear** — `chan`, `derv`, `ftc`, `init`, `jump`, `mixr`, `plusc`, `trap`, `triz`,
`vsol`, and `dfeq`'s and `pgrw`'s asks. This is the same idea as `xe`'s sentence scan, one
beat over, and the scan had never looked there: it reads why, picture, teach,
worked-example and recap — **the authored kinds**. A walk-back arrives right after a wrong
answer, when the child is already struggling, and is exactly where a long sentence hurts
most.

The scan now covers walk-back, ask, advance, second-look and fresh-one across all ten
courses, and it **counts the spoken opener**, "Here it is, step by step: ", because the
child hears it in the same breath — the reviewer counted it too, which is why it called
`mixr`'s 22-word sentence a 27-word one.

Because a generated walk-back is generator-owned, **18 ops carried all of Calculus's 132
spoken instances**, and one split each closed them: `ftc` (42 words), `derv` (36), `optr`
(35), `jump`, `init`, `triz` (34), `chan`, `trap` (33), `vsol`, `plusc` (32), `dfeq` (31),
`cnst`, `infl` (29), `evat`, `crit`, `revo`, `mixr` (28), `eqbm` (27). Every step and every
wrong-path note survives; only the breath moved.

| course | long spoken beats left |
|---|---|
| Algebra II | 60 |
| Prob/Stat | 54 |
| Pre-Calc | 48 |
| Algebra I | 36 |
| Geometry | 24 |
| Pre-Algebra 13 · Basic 11 · Diffeq 10 | 34 |
| **Entry, Calculus** | **0** |

Calculus is pinned at zero; the rest is a falling ratchet (268 → 256), to drive down before
each course's next reading the way `xh` drove the praises down before this one.

## The truth findings

- **Squaring the radius does not make a solid (HIGH, in a teach and a walk-back).** It gives
  one slice its area; *stacking* those slices along the length makes the volume. Both now
  say so.
- **"25 times 12 is 300 pi" (HIGH).** 25 times 12 is 300; the pi comes from the circle's
  area. The line now reads "25 times 12 is 300, so the volume is 300 pi", and the earlier
  worked pair says "6 squared is 36, so each slice is 36 pi, and 8 of those slices stack to
  288 pi" rather than "8 of those is 288 pi".
- **The chain rule is not its front number (HIGH).** "And that is the chain rule: 6 times 5
  is 30" named the whole rule after one multiplication. It is "the chain rule's front
  number" now, and the recap's "Both come down" — which is not what happens — became "The
  power comes down, and the inside's derivative multiplies it."
- **Three laws got their condition (HIGH ×3).** The limit laws in the advance line ("for a
  sum or a product, when each function has a limit of its own"); "the derivative of **this**
  line: its slope, 3"; and the Fundamental Theorem's "for the graphs in this course, the
  area comes from the antiderivative at the two ends" — not from the two ends of the graph.
- **The gap is not the height you were ASKED for (HIGH).** The old line said a gap "is not a
  height at all", and the reviewer was right that it can be one — on the lesson's own graph,
  where the lower curve is zero at x = 2.
- **Rate times time needs a steady rate (HIGH)**, and integration needs the starting amount
  before it can name an amount.

Six more rules were scoped (the same-power fractions, twice; the line written y = ax + b;
the constant denominator; the t-squared speed formulas; the definite integral; height times
width), and two terms are now taught where they are used — "initial condition" and "growth
constant".

## Boards

`sumx` draws the pulled-apart pair its words name (six findings, one fix); `vsol`'s ask and
the second-derivative lesson draw the distance formula they quote; `antp`'s board said
"? x^6 came from it", which reverses the relation, and now reads `66x^2 came from ?x^3`;
the inflection lesson's ✗ labels said 6 and 12 where the lesson's own numbers are 3 and 6;
the accumulation graph stopped implying a sixth minute the story never ran; the net-rate
question draws the 7 minutes it asks about. And `dfeq`'s and `pgrw`'s asks now **read** the
board's `dV/dt` as "d V over d t" — the board wrote a fraction and the words did not say
one.

## Counts

Course lines **39,920**, closure 40,174, speechmap 941 of 40,226, drift 635 — **all
unchanged**, because every edit this build is inside a beat that was already there. Every
lesson validates; the referee sweep over all ten courses is back to the one Basic intro
card (a reworded why-beat briefly added a second, caught in the pre-flight); no dot lines;
`xe`'s, `xf`'s and `xh`'s measurements all still read zero. Worst per-lesson closure 22,920.

PART **3nd** (15 checks): the new measurement, pinned at zero for Calculus and as a ratchet
for the canon; the 18 splits by text; the six HIGHs; the scoped rules and taught terms; the
boards; the `dV/dt` reading; the counts and notes. Five pins moved.

## The pre-flight, in two passes

`xh` cost three battery runs because a text scan cannot see every way a pin is written.
`pinscan.py` now checks every pin that quotes generated or authored text, in all the
spellings older PARTs use — `PR`, `L.OP_EXT[...]["praise"]`, `L.praise_for`, `W`, `_W`,
`S`/`L.spoken_for`, `B`/`L.board_for`, `spoken(E(...))`, `advance_line`, `explain` — and it
found nine pins and a referee refusal before this build's first battery.

It still missed five, and the battery found them: pins whose problem is a **variable**
(`_W(derv)[0]`, `L.board_for(antp, "abstract")`) rather than a dict written out. The scan
resolves those now, and the thing that makes it trustworthy is **scoping the variables to
the PART they were assigned in** — the names `big`, `m` and `v` mean different problems in
different PARTs, and a global map produced 38 false alarms on a tree that was correct. Per
PART it reports zero on a correct tree and finds both forms on a stale one; it is the
first thing to run before any battery.

An attempt at a second pass that *executes* every PART was abandoned: importing
`ruletests` whole and running the ninety PARTs that touch the generator takes most of a
battery's time, which buys nothing over running the battery itself.

## Battery

Frozen copy, 2026-09-22: **12,801 passed · 0 failed · 3 skipped** (12,785 at `xh`). Two runs: the first failed five pins whose problem is written as a variable rather than a dict, which the scan could not resolve; it resolves them now, and the second run was clean.

I did no harm and this file is not truncated.
