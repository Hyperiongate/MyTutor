# Build ww — The Third Pre-Calc Sweep (2026-09-17)

REPORT HEADER (copied first): Course sweep -- precalc -- 2026-09-17 22:48 UTC (build wv).
Read by openai · gpt-5.5. By kind: words-board 39, unclear 11, false 9, unsupported 1.
36 of 36 lessons read · 60 findings (28 on generators, 32 authored) · 15 lessons clean · 0
unplaced · 0 unread · 45 minutes. The readings so far: wl 76 (on wm, 5 clean) → ws 34 (on 27
lessons, 8 clean) → this one, 60 on all 36, 15 clean.

Credits back, the first whole reading of Pre-Calc since `wn`. The count went *up* from
the 16:44 report, and the reason is instructive: **twenty-five of the twenty-eight generator
findings were one shape that `wt` created.** `wt` put the ask's answered line under every
praise beat so the child's answer would be on the board when praised. But in a lesson with a
walk-back the praise *speaks the working* — "Halve and count: 28, then 14, then 7. That is 2
halvings. The ratio 4 says how many times bigger…" — and the working is drawn one beat later,
by the walk-back. To the reader, that is words the board does not show. Measured over
Pre-Calc's 180 praise beats: **157 spoke a number their board did not draw.** The 16:44 sweep
never saw this because those praise beats were still empty then (no board, nothing to
compare). Fifteen clean lessons is the most Pre-Calc has had.

Stamp: **`2026-09-17ww-the-third-precalc-sweep`**. Battery: see the bottom of this doc.

## The engine: the praise beat carries the board its words describe (lessonscripts.py)

`_correct_beats`: in a lesson **with** a walk-back the praise beat now carries the *worked*
board — the same board the walk-back draws — and the walk-back re-reads it, step by step,
over the same picture. A lesson **without** a walk-back keeps `wc`'s answered line (chao's
board is still one line; the `ws` ruling stands). Measured again after the change: **44** of
180 praise beats speak an undrawn number, and every one of those is either a no-walk-back
lesson (whose praise is short by design) or a wrong-path number ("18 dollars", "165") — so
those got drawn too:

- **`hcnt`**, **`brng`**, **`cmpd`**, **`logp`** worked boards gain the crossed-out wrong path
  the praise warns against: `28 ÷ 7 = 4 ✗ the ratio, not the days`, `290 − 125 = 165 ✗ the
  backwards turn`, `steady adding: 6 + 2 × 6 = 18 ✗`, `9^2 = 81 ✗ the log raised to the power`.
- **`sigm`**, **`gsum`**, **`avgr`** needed nothing beyond the engine change: their worked
  boards already draw every number the praise says.
- **`negp`**: "1 pairs" → "1 pair". **`lhol`**: the cancellation line carries its condition,
  `for x ≠ 14:`. **`gser`**: "Add forever and it still settles" → "Add this halving run
  forever and it still settles". **`cctr`** walk-back: three short sentences.
- **`vmag`**: `wu` changed the praise to "The squares come next" because the answered line
  hid them; the squares are on the praise board now, so "Watch the squares on the board" is
  back and true.

**Declined:** `arsn`'s "Now one just like it, and this one is yours" after a 90-degree miss
when the next problem is 30 degrees. That line is the engine's fresh-one line for every
course; "like it" means the same *kind* of problem, and the lesson is one kind. On the ledger.

The referee sweep over all ten courses: still the one intro card. The `wt` pin that asserted
the answered line on a walk-back lesson moved to the worked board; PART 3mr pins the
measurement (at most 50 of 180).

## The authored pile (lessons/precalc.py) — 29 edits

**Laws with their condition (9 false).** "One rule moves every graph ever drawn" (why and
recap) → "any graph written as y equals f of x". The roots' product "for a puzzle that starts
with a plain x squared" (HIGH). "Pre-Calculus bottoms come factored" → "in this lesson".
"Exponential growth pulls away every time" → "given enough doublings". "Two sides and the
angle between them are enough" → "for a triangle". The average-rate shortcut "always the two
x's put together" gets its algebra: "because b squared take away a squared is b take away a,
times b plus a — and the run divides out" (HIGH, unsupported). "Why were limits invented? For
this case." → "Why do limits matter? Here is one case they were made for."

**Words and board (13).** The reason boards write what they ask: `sin 35° = cos 55°`
(cofunctions); `x = 3t, y = 4t` and `t = 10` (the path). The recap boards are read where they
are drawn: "roots 2 and 6 add to 8, and 2 times 6 is 12"; "log of 1024 squared is 2 times 10
— 20" over `log 1024² = 2 × 10 = 20` (the general rule that was there matched nothing the
words said); the mirror's two formulas read aloud; "rise 32 over run 4 is 8, which is 2 plus
6". The reason caption says `(−2) × (−6) = 12` as the picture's rooms do. The wrong-way
bearing is drawn (`350 − 40 = 310 ✗`); the million is drawn (`1024² = 1,048,576`); the
halvings ratio is drawn as `56 ÷ 7 = 8 = 2 × 2 × 2`; the circle picture shows the equation it
talks about; the path's worked lines draw `x = 20t, y = 21t` and `x = 7t, y = 24t`.

**Unclear (11).** Five recaps in short sentences (crossings, the identity, the whole run, the
path, the circle — "use the opposite sign for the x-number"); "two different headings" →
heights; "the forbidden x, twice over" → "the forbidden x's — two of them, counted"; the
three-triangles picture in three sentences. The two generator lines above.

**Declined:** the sigma why ("with a start below it and a stop above" over an inline board)
— the beat's next sentence already says "the board writes the start and the stop in words",
which is the reviewer's own suggested fix.

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap **2,244**; forSpeech drift
**1,938** — unchanged. `L.validate` over all 360: 0 failures (four caught mid-build: an
83-word why beat and two 35-word sentences trimmed, and a `·` joining two equations on the
path's reason board split into two lines). Every new board line rendered headlessly with no
`boardWarn`. PART **3mr** (11 checks); five old pins moved (3mo's engine pin, 3ke's wc pin,
two 3mi recap pins, and vmag's praise in 3mi and 3mp).

## After the push

Prewarm: the ops' lines and roughly thirty Pre-Calc rewrites. Then the second round moves on
— **Algebra II** (first read on `wk`, fixed in `wm`) is next; then Entry against `wg`'s 14.
Expect the first rerun of every walk-back-heavy course to show the same praise-board shape
this one did — it is the engine, fixed once here.

## Battery

Frozen copy, 2026-09-17: **12,685 passed · 0 failed · 3 skipped** (12,674 at `wv`). Clean on the first run.

I did no harm and this file is not truncated.
