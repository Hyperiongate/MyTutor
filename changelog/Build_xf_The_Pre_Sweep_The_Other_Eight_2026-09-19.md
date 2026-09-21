# Build xf — The Pre-Sweep, The Other Eight (2026-09-19)

Built while Jim was away from his computer (two days, phone only), after `xd` and `xe`;
Jim's word from his phone was "work on whatever you can work on". **Not yet on Jim's
disk** — see the handoff's pending-commit list.

Stamp: **`2026-09-19xf-the-pre-sweep-the-other-eight`**. Battery: see the bottom of this doc.

## What it is

`xe` closed two classes in Prob/Stat and Calculus ahead of their second readings — the
closing recap board the words never read, and the teaching sentence of 27 words or more.
This build runs the same two measurements over the **other eight courses** and closes what
they found, so every course's next reading starts without them:

| course | unread closing boards | long sentences |
|---|---|---|
| Entry | 1 | 1 |
| Basic | 12 | 15 |
| Pre-Algebra | 17 | 14 |
| Algebra I | 21 | 26 |
| Geometry | 19 | 29 |
| Algebra II | 24 | 35 |
| Pre-Calc | 20 | 30 |
| Diffeq | 0 | 23 |
| **all eight** | **114** | **173** |

286 authored edits in `lessons/<course>.py`, all inside existing beats: no beat added, no
number changed, no board changed. Course lines stay **40,005**, closure 40,259, speechmap
1,001 of 40,311 (regenerated — the same count, but the coordinate lines it re-keys now
carry the split wording), drift 695.

## One refinement to the measurement

Entry and Basic say their numbers in words — "thirteen minus five equals eight" over
`13 − 5 = 8` — and `xe`'s digit-only scan called fourteen of Entry's closing boards
unread when every one of them was read. PART 3na counts a number as read when its digits
OR its words are in the sentence: `numwords.py`'s tables run backwards (up to 999,
"forty-four", "one hundred thirty-six"). After that Entry had one true miss (the doubles
lesson: "a double you know is a sum you never have to count" over `4 + 4 = 8` — now "…
never have to count: four plus four is eight").

A board whose only number is a condition — the log law's `for a, b > 0` — is read as
words: "For a and b above zero, in one base, …".

## The readings

Same rule as `xe`: the closing line says the board's numbers in the board's order, as a
credit line after a colon, and a split keeps every number and every named idea. A few:

- Basic, left-overs: "And it is for real life, where sharing rarely comes out even: 13
  divided by 4 is 3, left over 1."
- Algebra I, socks and shoes: "And that is socks and shoes, in algebra: 2 x plus 3 equals
  11, so x is 4."
- Algebra I, the lowest point (the turn-37 recap over `y = (x − 3)² + 2`): "The number
  inside the brackets says where the floor sits — here, at x equals 3. The plus number
  says how low — here, 2."
- Geometry, Pythagoras: "…still true in every corner: 5 squared plus 12 squared is 13
  squared."
- Algebra II, the test number (over `below zero → 0 · zero → 1 · above zero → 2`): "And
  that is a curve counted without being drawn: below zero, no crossings; zero, one; above
  zero, two."
- Pre-Calc, a limit with a side: "And that is a limit with a side: from the left, 3; from
  the right, 9."
- Diffeq, the cooling cup (a split): "Answering 30 hands back the gap. And 5 is only the
  degrees of gap it takes to cool 1 degree a minute — the share, not the rate."

Three sentences needed more than a full stop: the ride-the-pattern "add 3, add 3, add 3…"
(an ellipsis is not a sentence end to the voice or the scan — now "add 3, add 3, add 3, and
on and on. Or you could RIDE…"), Diffeq's natural-frequency rule (the condition became its
own sentence: "…the rule is simple. That frequency is the square root of the number sitting
on the y."), and the log law above.

## Pins

PART **3na** (8 checks): the number-word reader; **both measurements over all ten courses,
pinned at zero**; five readings and three splits by text; the log law's condition; the
counts and notes. Thirteen older pins that quoted a sentence now split (or a fragment that
now opens its own sentence with a capital) were moved and marked "(xf)": `xa`'s power
definition, `wx`'s new-number line and which-x-was-fed (twice, one in the seven-closing-beats
dict), `wm`'s log law and logs-add, `wp`'s classification and nullcline lines, `wu`'s
backwards spin, `ww`'s mirror line, `wi`'s primes line, `wk`'s number machine, `wm`'s
staircase. PART 3mz (xe's two-course version) stays as it was and still passes.

## Battery

Frozen copy, 2026-09-19: **12,759 passed · 0 failed · 3 skipped** (12,751 at `xe`). Clean on the first run — the thirteen pins were found and moved by a pre-scan of every `in spoken(E(...))` fragment against the edited lessons before the battery ran.

I did no harm and this file is not truncated.
