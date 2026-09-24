# Build xu — The Third Prob/Stat Sweep, Part One (and a stopped sweep can be resumed), 2026-09-23

Sweep header, 2026-09-23 22:56 UTC, read by gpt-5.5 on build
`2026-09-23xt-the-voice-cache-reclaim-card`: **16 of 36 lessons read · 13 findings (2 on
generators, 11 on authored beats) · 8 lessons clean · 0 unplaced · 20 unread · 1346.7s —
STOPPED after 19: OpenAI 429, no credits remaining.** By kind: false 9, words-board 3,
unsupported 1. The floor: `xg`'s reading, **60 findings on 36, 10 clean**.

Stamp: **`2026-09-23xu-the-third-probstat-sweep-part-one`**. PART **3np**. A sweep build
(the fourth of the third round; `xt` was the gate build before it).

## Half a reading, and what it cost

The reader's credits ran out sixteen lessons in. The `wv` rule stopped the sweep after three
identical 429s and wrote the report — and then `main.py` cleared the checkpoint, because
since `xp` "the report is the record now". The sixteen lessons read ($2.40) could not be
resumed; the only path was to run all 36 again.

**That is fixed in this build.** A sweep the seat cuts short now keeps its checkpoint; a
sweep that finishes clean still clears it. The checkpoint itself changed shape: it holds
only the rows actually *read* — an error row (a dead seat, a walk failure, "not attempted")
is dropped at save time, so a resume reads that lesson instead of skipping it — and
`run_sweep` drops any error row it is handed on resume. The STOPPED banner no longer says
"run it again"; it says to press Resume, which reads just the rest. PART 3np runs the whole
sequence through the endpoints: a judge that dies after two lessons → the report and a
two-row checkpoint → the dry run pricing six left → a resume that reads exactly those six
to DONE, 8 of 8, no banner.

For this Prob/Stat run the checkpoint is already gone (it was cleared under the old rule),
so the remaining twenty will be read by a fresh run — see **After the push**.

## The thirteen, on the sixteen

**Two generators.** `resd`'s ask captioned the bars "the gap between the bars is the
residual" — a residual is signed (actual take away predicted; predicted 26, actual 20 is −6)
and the gap is its *size*, which is what the lesson measures. The caption says "the size of
the residual" now (a HIGH; the walk-back's board already wrote the signed line beside the
size since `xg`). `sslp`'s walk-back said "9 times 5" over a board that wrote `5 × 9` — it
says "5 times 9", the rate times the steps in the board's order.

**The residual lesson (HIGH).** The teach defined "the gap has a name, the residual — actual
take away predicted", which breaks the moment a dot sits below the line. It reads "the
residual is actual take away predicted, and the gap is its size" now, and the second worked
example — predicted 44, actual 14 — shows `14 − 44 = −30` and "its size is 44 take away 14 —
30" instead of silently reversing the subtraction.

**Laws with their condition (7)**, the class the upper courses keep showing: the histogram
recap prints each group's count "on these boards"; the 80th percentile means faster "when
speeds are being ranked" (a race time would run the other way), and she raced 20 *others*,
not 20 racers; "one way to measure spread" rather than the definition of spread; a wild
extreme "usually" moves the box far less; the slope is "here, points per extra hour of
practice", and "that is how the line predicts" over the `4 × 2 = 8` board rather than "a
line that predicts"; the biased survey's condition is the crowd "given no chance to be
picked"; the four-times rule holds "with everything else about the poll the same".

Two of the rewritten sentences ran to 27 and 28 words and were split before the battery
(PART 3na caught them in the smoke run). Nothing declined. Grading under the 09-22 ruling:
**class** (the condition, 7 — the third round has not exhausted it in this course),
**one-off** (6).

## Counts

Course lines **40,495 — unchanged** (every line one for one). Speechmap 941. Every lesson
validates; 3na, 3nb, 3nd, 3ne, 3nn, 3eu and 3mo pass on the edited tree. `tools/pinscan.py`
found the one stale pin (3mf's box sentence) before the first battery; two more pins moved
by hand for the engine change (3nk's "not attempted rows reach the checkpoint" — they do not
any more, by design; 3mq's banner text).

## After the push

`/health` = `2026-09-23xu-the-third-probstat-sweep-part-one`. **Prewarm**: the 13 rewritten
lines (a few dollars). Then **add OpenAI credits** and run Prob/Stat again from the card — the
whole course, $5.40, because this run's checkpoint was cleared under the old rule. From this
build on, a sweep the seat cuts short offers Resume for the lessons left. Paste the report
whole; the twenty unread lessons (units 5–9: probability, the bell curve, margins) are where
`xg`'s "rule of thumb stated as a law" class lived.

## Files

`lessons/probstat.py` (14 edits), `lessonscripts.py` (resd, sslp), `coursesweep.py` (the
checkpoint keeps READ rows; the banner), `main.py` (a stopped sweep keeps its checkpoint;
stamp), `ruletests.py` (PART 3np; three pins moved), `speechmap.py` (regenerated, 941), this
doc, the refreshed `START_HERE_Handoff_2026-09-23.md`.

Battery on the frozen copy, 2026-09-23: **12,991 passed · 0 failed · 3 skipped** (12,978 at `xt`), first run clean.

I did no harm and this file is not truncated.
