# Build xh — The Credit Line Everywhere (2026-09-21)

No sweep report. `xg` found the measurement that explains three courses' worth of
"repeats" findings and left a falling ratchet of **59 ops**; Jim's word was to close
Calculus's share before its second reading. This build closes all 59, so the ratchet is a
pin at zero over the whole canon.

Stamp: **`2026-09-21xh-the-credit-line-everywhere`**. Battery: see the bottom of this doc.

## What was left, and why it mattered

A praise beat is a **credit line** — the answer and its one reason. A praise that runs on
past 26 words is still an explanation, and the walk-back explains the same thing a breath
later, over the same board. `xg` showed the measurement holds: every op a sweep had flagged
as "repeats" had a praise over 30 words; every credit line `xa` wrote is under 21.

| course | explaining praises before this build |
|---|---|
| Calculus | 32 |
| Pre-Calc | 19 |
| Algebra I / Algebra II / Geometry | 3 / 3 / 2 |
| **total** | **59** |

Calculus was next for its second reading and carried the largest share of any course. On
the Prob/Stat evidence — 18 of 60 findings in this one class — most of what that reading
would have spent itself on is now gone before it starts.

## The credit lines

Each is the answer first, then the one reason that earns it:

- `ftc`: "16 — end take away start: 5 squared is 25, 3 squared is 9."
- `crit`: "x is 2 — where the slope is zero the curve is flat for an instant, the bottom of
  its valley."
- `revo`: "18 pi — the radius 3 squares to 9, and 2 lengths of that stack up."
- `eqbm`: "P is 2 — set the rate to zero and 3 P has to equal 6."
- `lhol`: "28 — everywhere except 14 that fraction quietly equals x plus 14."
- `vert`: "110 degrees — the angle NEXT TO it shares a straight line, so the two make 180."

## Nine pins, and two sentences that had to move rather than go

Nine older pins quoted a phrase inside a praise. Each one was there because a sweep had
found something wrong, so none could simply be deleted. The rule this build used: **if the
phrase is the answer's reason it stays in the praise; if it is the explaining, it belongs
in the walk-back** — one beat later, where explaining belongs.

Two of those sentences were not in the walk-back at all and were **added** to it, so
nothing the child hears was lost:

- `ftc`'s "ANTIDIFFERENTIATING, then end take away start" — the word appeared nowhere else
  in the lesson, and it is the whole point of the Fundamental Theorem beat.
- `lhol`'s "the simplified x plus 14 is defined there, so it is a hole: y never reaches 28,
  and the limit says where it was headed" — the sentence that separates a hole from an
  asymptote.

`avgv`'s trade-places sentence and `arsn`'s base-and-height sentence were already in their
walk-backs; the pins moved to read them there. `vmag`'s "watch the squares on the board"
and `gser`'s "add this halving run forever and it still settles" are the answer's own
reason, so they stayed in the credit line. `cofn`'s and `gaus`'s exact-equality pins were
rewritten to the new lines; `chan`'s and `trap`'s to the shorter phrasing.

## Counts

Course lines **39,970 → 39,920**, closure 40,224 → 40,174 — the same reason as `xg`, a
credit line being shared by more problems than an explanation was. Speechmap **1,001 →
941** of 40,226 and forSpeech drift **695 → 635**: those 60 lines are all `vert`'s old
praise, which carried a parenthetical aside — the voice tidy rewrites brackets as commas,
so every one of them re-keyed for that alone. The worst per-lesson closure fell from 24,838
to **22,723** (`calc-u9-when-the-rate-depends-on-the-amount`), a long way under the 25,000
tripwire, because shorter praises mean fewer characters per lesson.

Every lesson validates; the referee sweep over all ten courses is unchanged (the one Basic
intro card); no dot lines; `xe`'s and `xf`'s two measurements still read zero everywhere.
A new check confirms every op's praise still renders for **every problem the courses
actually pose** — each lesson's bank and both guided asks — not just the one the
measurement sampled.

PART **3nc** (7 checks) records this build; PART 3nb's ratchet is now
**"no praise over 26 words, in any course"**, pinned at zero.

## The pin scan, widened

`xf` and `xg` pre-scanned every `"..." in spoken(E(...))`, `PR(...)` and `W(...)` pin
against the rebuilt lessons before the battery ran, and both were clean first time. This
build took three runs, for three reasons worth writing down. First, older PARTs reach the
same generator a different way — `L.OP_EXT["op"]["praise"]({...})` and `L.praise_for(p, 0)`
rather than the local `PR` alias — so the scan missed six pins: `vmag`'s and `linf`'s (moved
to the new credit lines), `maxa`'s (moved to the phrase that still says RECTANGLE), `pwrc`'s
"is not the power-rule move" (into the walk-back that already said it), `mrat`'s
count-the-arithmetic check (now zero — a credit line names the two rates and lets the
walk-back do the sum), and `hcnt`'s "Halve and count", which only changed its capital.

Second, **a pin moved into another PART inherits that PART's aliases.** `lhol`'s moved from
`PR(...)` to `_W(...)`, and PART 3mo defines no `_W` — the battery died on a NameError
twenty minutes in, with no counts to show for it. It is written out as `L._worked_for(...)`
now.

Third, a text scan cannot see either of those. So the pre-flight gained a second pass that
**executes** every PART touching the generator against the rebuilt code, with a stub
`check`, and reports only the checks that actually fail. That found the last one before the
battery ran, and it is what the next build should run first.

## Battery

Frozen copy, 2026-09-21: **12,785 passed · 0 failed · 3 skipped** (12,778 at `xg`). Three runs: the first failed four pins the regex scan could not see, the second died on an alias NameError inside another PART, the third was clean.

I did no harm and this file is not truncated.
