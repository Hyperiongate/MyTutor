# Build wh — The First Basic Sweep (2026-09-16)

The first sweep of Basic, on `wg`: **67 findings** (3 on generators, 64 authored), 7 of 36
lessons clean, 0 unplaced, 39 minutes. As predicted, it looked like Entry's `wc` run — a big
pile with a few generator classes hiding in the authored section. Read whole, it sorted into
five generator fixes, one sweep fix, one charter line, and fifty-odd authored rewrites.

Stamp: **`2026-09-16wh-the-first-basic-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — fixed once, fixed everywhere

- **Rounding to hundreds, `r100`**: "253 … the tens digit is 5 — right at halfway". Halfway is
  250; a tens digit of 5 is only exactly halfway when the ones digit is 0. Now "just past
  halfway" for 253 and 578, "right at halfway" for 350. Rounding to tens is untouched (a ones
  digit of 5 *is* halfway).
- **The split walk-backs, `*` and `/`**: "80 plus 6 equals 86" was spoken and the caption
  stopped at the two pieces. Both captions now carry the sum (`… 80 + 6 = 86`, `… 20 + 1 = 21`).
- **`t2h`**: "1 full rows" → "1 full row", on the board and in the walk-back.
- **The promise, again.** Build `we` made the *house* practice intro honest ("three right
  answers in a row, then one reason to tap, and we're done") and noted 34 lessons with their
  own intro that might make the same broken promise. The sweep found one; the code found 33 —
  every one of them Basic. `practice_intro_line` now corrects the promise inside a lesson's own
  intro too, keeping the lesson's hint sentence. 33 clips to prewarm.
- **The times-table card.** The intro says "all 81 facts, one after another"; the card under it
  said "Three right answers in a row". The sweep's one HIGH words-board. A table lesson now
  gets `PRACTICE_INTRO_BOARD_TABLE` ("All 81 facts, one after another | … | A slip means we look
  at its picture, then start again") — no "I'm not sure" line, because the pass has no such
  answer.

## The sweep (coursesweep.py)

- **The problem space lists its values.** "a from 10 to 50" invited the reviewer to object that
  30 percent breaks the percent-of rule (two HIGHs) — the bank is 10, 25 and 50 and nothing
  else; likewise 52 ÷ 4 in a lesson whose every tens digit divides, and an exact hundred in
  rounding. A field with 12 or fewer distinct values is now listed ("a is one of 10, 25, 50");
  past that, the range. A padding field (b always 0) is not printed.
- **One charter line**: a `[[numberline]]` draws its own tick labels between min and max; `hops=`
  and `points=` are the jumps and the marked spots, not the ticks. (The tenths lesson was asked
  to "draw the ten tenth marks" that the figure already draws. My first fix put `denom="10"` on
  the tag — and rendered the ticks as 1/10, 2/10 in a decimals lesson. Reverted; the ruling is
  right and the tag was.)

## The authored pile (lessons/basic.py) — 52 answered, by class

**False, fixed.** Factor pairs: "the partner is what you DIVIDE by" → "what you GET when you
divide" (HIGH, and simply wrong). Tenths and hundredths: "a tenth is ten times the bigger
coin" → "a tenth is the bigger coin — ten times a hundredth" (HIGH, wrong). Simplest form:
"whatever you do to the top, do to the bottom" → "whatever you *divide* the top by" (HIGH); the
recap finds "the biggest number they share … if they still share something, divide again"
(HIGH); "nothing divides 3 and 4" → "nothing but 1" (the rule-13 falsehood row, again); the
board's `10/16 ÷ 2 → 5/8` (which says 5/16) → "10/16 → 5/8, both divided by 2". Number line:
"top and bottom the same means the whole line" → "one whole, the point 1". LCM caption: "count
by 3 lands on 6 first" → "before 12". Times by ten's trap taught "count your zeros" as the
*reason* — the very reason the lesson's own question rejects — now "the zeros are not copied,
they hold the empty places". Both rounding rules carry the halfway condition. Different
bottoms' recap is scoped to "one bottom fits inside the other" (its whole space) and its
reason answer says *add* pieces, not *count* them. Times tables: "every bigger sum you will
ever do" → "nearly every"; "one fact learned is two facts known" → "learn six times seven and
you know seven times six as well". "The times tables (you know) stop at nine"; "no times table
(you know) goes that far". "Count the rows: 3, 6, 9" → "count by threes, one group at a time".
Area "is the carpet" → "is how much carpet covers". Dividing's recap law → "pieces you know how
to divide — here, the tens and the ones". Percent-of's "take one" scoped to its three percents.
"Not 7 of anything" → "not 7 tenths and not 7 hundredths". "Counting one at a time stops
working" → "gets slow".

**Words-board, fixed.** Fourteen second-recap beats now *speak* the equation their board
writes — the rule Entry's `wg` set ("the recap says what the board shows"), applied to Basic.
Times by ten's picture is two beats: 46 on the chart, *then* the move to 460 (the words promised
46 and the board drew 460). What-percent's worked example draws its times-20 steps. The
quarter-turn caption names 90°, 180° and 360°, as the words do. Unlike-bottoms' trap names the
3/7 its board crosses out. What-dividing-means no longer says "every box ends up with 4" over
the un-dealt board. **The dot**: `4 × 3 = 12 · 12 ÷ 3 = 4` reads as twelve times twelve (HIGH).
Every step line in Basic that joined two equations with " · " is now two `[[step]]` tags —
and so are Pre-Algebra's four, where the dot *is* a times sign and the reading is not just
plausible but correct. A pin now forbids `<digit> · <digit>` inside a step line in Entry,
Basic and Pre-Algebra.

**Untaught and unclear, fixed.** "Finer line" → "the line with the smaller pieces" (four
places, two lessons). "Unit squares" defined on first use. "Real numbers" → "many numbers".
"40%" → "40 percent" before the sign is taught. "Three digits say it all: 3, 4, 2". Eight
long sentences split (multi-digit review's regrouping, place value's recap, GCF's why, the
number line's why and teach, story problems' why, divide-two-digit's picture, percent-off's
trap). Two reason distractors that were *true* replaced ("9 is half of 18"; "3 plus 4 is less
than 10").

## Ruled, not fixed

Two rounding findings asked for the exact-hundred case (the space excludes it); two percent
findings asked about 30 percent (the space is 10, 25, 50); one dividing finding about 52 ÷ 4;
the tenths why beat introducing "0.1" with no board (a why beat is told over the goal card, by
design — `wg`'s line). The problem-space listing answers the first five without a charter word.

## Counts

Course lines 39,996 → **39,997** (times by ten's second picture beat); closure 40,250 →
40,251; speechmap 2,244 of 40,302 → **2,245 of 40,303** (the hundredths recap's "0.25 plus
0.13 — 0.38" is tidied by forSpeech and re-keys). `L.validate` over all 360: 0 failures. Every
new board tag rendered headlessly through `window.__drawBoard` on `demo-lesson.html` with no
`boardWarn`. PART **3mc** pins all of the above; the count pins moved.

## After the push

Prewarm: roughly sixty rewritten Basic lines plus the 33 corrected intros. Then **do not run
Basic again yet** — run **Pre-Algebra** (the queue has sampled it; expect fewer generator
items and the same second-recap class). Basic's second run can wait for the weekly deep dive,
where I expect it to land near Entry's `wd` (a few dozen, mostly refinements).

Two things to carry forward: (1) the *second-recap board* class is house-wide — every course's
closing beat writes an equation over a real-life sentence; the sweeps will keep listing them
one course at a time unless we decide once (speak them, as Entry and Basic now do); (2) the
" · " separator between two equations is used ~350 times across the upper courses' step lines,
where the dot is a times sign; that is a Pre-Algebra-and-up decision, not a Basic one.

I did no harm and this file is not truncated.
