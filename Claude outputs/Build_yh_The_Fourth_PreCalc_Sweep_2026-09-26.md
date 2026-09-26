# Build yh — The Fourth Pre-Calc Sweep, 2026-09-26

Sweep header, 2026-09-26 13:40 UTC, read by gpt-5.5 on build
`2026-09-26yg-the-sixth-entry-sweep`: **36 of 36 lessons read · 15 findings (3 on generators,
12 on authored beats) · 25 lessons clean · 0 unplaced · 0 unread · 932.4s** (resumed after a
restart: 18 before it, 18 after — `xp`'s resume working). By kind: words-board 8, false 5,
unsupported 1, unclear 1. The floors: `xm`'s reading **28 findings, 24 clean**; `ww`'s **49, 10**;
`wu`'s **93, 4**.

Stamp: **`2026-09-26yh-the-fourth-precalc-sweep`**. PART **3ob**. A sweep build — and **the
third round's last reading: every one of the ten courses has now been read three times**
(Entry six, Pre-Calc four).

## Where the third round ends

| course | first | second | third | clean after the third |
|---|---|---|---|---|
| Pre-Algebra | 69 | 58 | 29 (xk) | 18 |
| Pre-Calc | 76 | 34 · 60 (wu) · 28 (xm) | 15 (yh, its fourth) | 25 |
| Algebra I | 72 | 50 | 23 (xq) | 23 |
| Diffeq | 119 | 62 | 39 (xs) | 13 |
| Prob/Stat | 92 | 60 | 26 (xu + xw) | 23 |
| Algebra II | 73 | 43 | 28 (xv) | 19 |
| Basic | 67 | 41 | 9 (xz) | 29 |
| Geometry | 63 | 36 | 11 (ya) | 27 |
| Calculus | 88 | 46 | 24 (yf) | 18 |
| Entry | 14 | 19 (fifth) | 6 (yg, its sixth) | 31 |

The 09-22 ruling said the sweeps stop when a reading is mostly one-offs
and reviewer misreads. Pre-Calc's fourth is 15 findings with no reviewer finding and two
HIGHs — so it earned its build — but the trend across the ten is unambiguous: the class
findings are running out, and what remains is a lesson here and there. That is the case for
the ruling to take effect now, which the handoff records.

## The two HIGHs

**A distractor that was true.** Vieta's reason question — *"A puzzle with roots 2 and 6 ends
in the number 12"* — offered *"because the end number is the bigger root, doubled"*. For 2
and 6, the bigger root doubled *is* 12. A child could tap it and be right by the numbers and
wrong by the reason. It is *"the bigger root, squared"* (36) now, and the question names its
condition: *"A puzzle that starts with a plain x squared, with roots 2 and 6, ends in the
number 12."* PART 3ob checks both distractors are numerically false for the example. This is
a new class worth a pre-sweep across the canon: **every reason-question distractor must be
false for the example the question names** — recorded in the handoff for a future gate build.

**The sine, said as a definition.** *"The sine of an angle is the rise divided by the slope's
length"* — true for the ramp's angle to the ground, false as a definition. *"For the ramp's
angle to the ground, the sine is the rise divided by the ramp's length, so the rise equals
length times sine."* And the closing board says `30° ramp: rise = ½ × length` — which put a
number on a closing board its words did not say, and the unread-closing-board measure (`xe`)
caught it on the second battery run: the beat says *"And that is a 30-degree ramp, measured
without climbing it: it rises half its length."*

## The generator (1 op, 3 findings)

`vasy`'s same-x walk-back caption read `y = 1 ÷ (x − 7)(x − 7)` — the very ambiguity `wn`
closed on the ask board and the two-zero branch. It groups the whole bottom now:
`y = 1 ÷ ((x − 7)(x − 7))`. PART 3ob checks no `vasy` walk-back in the bank has an ungrouped
bottom.

## The rest (11)

The spoken bracket — *"y equals f of the whole of x take away 3"* — in the why beat the sweep
quoted and in the teach beat it did not (*"like f of the whole of x take away 3"*), Algebra
I's rule. The machines picture says the 10 and the 13 its boards write. The reference-angle
teach: *"the trig values at 175 are the same size as the ones at 5. Only the sign can differ,
by quarter."* *"Equals 1 once each turn."* *"The angle and its partner are the two sharp
corners of one right triangle."* The faster-wave board writes `y = sin 2x`. The 196 worked
pair draws and speaks its whole equation (`(x − 2)² + (y − 3)² = 196`), not a fragment. The
shrinking window names a and b and draws `b² − a² = (b − a)(b + a)` and `rise ÷ run = b + a`
under the words — which made the beat seven board lines, and the flood referee (`se`: six is
the ceiling) caught it in the battery; its `3 + 5 = 8` line went, since `3 → 5: rise 16 ÷ run
2 = 8` already carries the numbers. Two beats trimmed to the 80-word cap and two 27-word
sentences split.

Grading under the 09-22 ruling: **class** (the condition 4, words-and-board 7, the true
distractor 1 — new), **one-off** (1), **reviewer** (0).

## Counts

Course lines **40,495 — unchanged**. Speechmap 941. Every lesson validates. Four pins moved
with the text (3mi's 196 line and once-each-turn; 3mp's f-of-x sentence; 3mr's
run-divides-out sentence). `tools/pinscan.py`: its reports were those pins before they moved
and 3nu's own negative pin.

## After the push

`/health` = `2026-09-26yh-the-fourth-precalc-sweep`. **Prewarm ~11 lines.** Open Pre-Calc
unit 2 lesson 3 (Vieta) to the reason question: no tap is right by accident. The third
round is complete; the handoff says what comes next.

## Files

`lessons/precalc.py` (13 spoken/board edits), `lessonscripts.py` (`vasy` caption),
`ruletests.py` (PART 3ob; four pins moved), `speechmap.py` (regenerated, 941), `main.py`
(stamp), this doc, the refreshed `START_HERE_Handoff_2026-09-26.md`.

Battery on the frozen copy, 2026-09-26: **13,156 passed · 0 failed · 3 skipped**, third run clean — the first two fell on my own lines (the seven-line flood; the unread 30 on the closing board), both recorded above (13,146 at `yg`).

I did no harm and this file is not truncated.
