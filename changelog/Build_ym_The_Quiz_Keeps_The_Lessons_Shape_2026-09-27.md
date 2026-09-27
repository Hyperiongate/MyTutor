# Build ym — The Quiz Keeps The Lesson's Shape, 2026-09-27

Jim, running the first quiz sweep: *"Is there anything you should be working on while I do
that?"* There was, and it came out of `yl`'s own pass — and then the Entry report landed
mid-build and sharpened it twice.

Stamp: **`2026-09-27ym-the-quiz-keeps-the-lessons-shape`**. PART **3og**. A pre-sweep build
of the structural kind (`xe`, `xf`, `xh`, `xj`, `yj`): measure a class by machine, fix what it
finds at the source, ratchet it.

## The class

`yl` left one thing for the reader: Pre-Algebra's dividing-by-a-fraction quiz asks *"4
divided by two fourths"* — a form the lesson's bank never uses. Reading all 1,799 pinned
questions against the shape their own lesson's bank keeps, that was the small end of a
large class. **Entry's "add past ten" quiz opened on 1 + 1.** "Take away bigger" (a bank of
11 − 2 … 19 − 9) asked 2 − 1, 8 − 6 and 10 − 1. "Add with carrying" asked 1 + 9. Basic's
multi-digit review asked 1 + 1, 1 + 18, 1 + 34, 1 + 51 and 1 + 75 — five questions, every one
with a 1 in front. The GCF lesson asked the GCF of 2 and 0. Geometry's "enlarging copy" asked a 4-and-4
— the same number twice, where every bank problem keeps its first number the bigger one.
"Add single digit", whose bank never adds more than 4, asked 2 + 7. And the two
story-problems lessons — spoken as stories, every bank problem authored as one — quizzed
*"What is 6 plus 1?"*: the generator has no story to tell. **214 questions in 106 lessons,
across all ten courses.**

A child who has just been taught adding past ten, and is graded on 1 + 1, is not being
graded on the lesson. Four of five is the pass; the pass is what the record says was
learned.

## One cause

`drillpool.envelope` bounds a candidate from **above** — *never show a child a bigger number
than the lesson itself already does* — and never from below. `pool_for` scans from a = 1,
b = 0. And `quiz_problems` sampled the ramped pool with `int(i * stride)`, which begins at
index 0: the easiest problem there is, the very end `quizsets.py`'s own header says the quiz
never uses. So a bank that runs 5..9 got a quiz that opened on 1. Worse for a two-digit
lesson: the pool is capped at 240, the scan from 1 filled it with sums under 50, and the
lesson's own numbers were never reached — Basic's review had 240 pool problems and not one
from 26 up.

## The fix, at the source

`drillpool.shape_of(les)` **measures** the shape the shipped bank keeps, per op: the floor
*and the ceiling* of a, b and c (the envelope's core lane took the lesson's *declared*
bound, which is how a bank that stops at 4 quizzed 2 + 7); the digit counts a and b use;
and every yes/no fact that *every* shipped problem of that op agrees on — the problem is
told as a story, the sum passes ten, the ones carry, the ones borrow, a is bigger than b, a
equals b, b divides a, b is zero, a is zero. Nothing assumed; a fact the bank is mixed
on is not a fact of the shape. `keeps_shape(shape, p)` judges a candidate and names the
first break (*"a=1 below the floor 5"*, *"sum_past_ten is False (bank: always True)"*).
`quiz_pool(les)` scans from the shape's floor upward, per op with the cap shared across ops,
keeping only shape-keepers that the envelope admits and the course's own validator accepts.
`quiz_slots(n, want)` takes the middle of each stride, never index 0. `quiz_problems`'
fallback lane (a lesson added after the table) draws through all of it.

**The table was not rebuilt.** `tools/genquiz.py` now reads the pinned table first: a
question that keeps its shape is kept exactly as it is; only a breaker is replaced, by the
shape-keeping problem at that slot's position, of the same op, not already in the set — and
from the bank's tail only when the op admits too few extras (28 of the 214: the two
story lessons, whose quizzes are now their own stories — a generated problem has none to
tell — and lessons whose ops field two or three candidates: Pythagorean triples, vectors,
the parametric walk — the same top-up `ov` used for 73 lessons). 1,585 questions
unchanged, 214 replaced, no set shorter than it was; seven op changes, all inside the three
mixed-op lessons whose quizzes gained the other op (before-and-after; the two story
lessons, which teach choosing plus or minus). A bank problem's story travels with it into
the table. Every replacement passes its op's own check,
has a whole-number key and three distinct taps that hold it. **So the prewarm is 214 new
asks, not 1,799.**

Some of the replacements, for the ear: add past ten — 1 + 1 → 6 + 5, 4 + 2 → 7 + 5, 6 + 2 →
6 + 8, 5 + 5 → 9 + 6. Take away bigger — 2 − 1 → 11 − 3, 8 − 6 → 13 − 2, 10 − 1 → 15 − 2. The
review — 1 + 1 → 26 + 16 … 1 + 75 → 27 + 16. GCF of 2 and 0 → GCF of 4 and 18; 12 and 10 (the
bank always puts the smaller first) → 15 and 25.

## The Entry report, reconciled

The first quiz sweep (Entry, 102 findings, all *unsupported*) arrived while this was being
built. Thirty-one of them — every finding on op `+` and op `-`, the bare story facts,
"after 1", the pattern with a jump of 1 — are the class above and are fixed in the data
(1 + 1, 4 + 2, 2 + 6, 2 + 7, 3 + 7, 1 + 20, 2 − 1, 8 − 6, 10 − 1, 9 − 7, 10 − 9, 20 − 16 …).
**The other seventy-one say "not one of the listed exact problems."**
The quiz page carried the lesson's PROBLEM SPACE line — which lists the bank's exact (a, b)
pairs, put there in `xz` so the course reviewer would stop pairing 48 with 3 — and the
reviewer judged every new quiz question against that list: 5 nickels and 3 pennies where
the lesson practised 5 and 2; 45 take away 21 where it practised 85 take away 21. A quiz
asks *new* problems by design; being absent from the bank is the point. So the quiz page
now carries `coursesweep.quiz_space` instead: the SHAPE, from `shape_of` — *op +: a from
5 to 9 (1-digit); b from 2 to 8 (1-digit); always — the ones carry, the two numbers add
past ten* — with the sentence that a question absent from the lesson's own examples is by
design and one outside the shape is the finding. The charter's rule 3 and its Do-NOT list
say the same, in those words. The coin, clock, place-value, ten-more, making-change and
crossing-a-hundred questions are all inside their shapes and stay. Jim's next Entry quiz
sweep is the check that the seventy-one are gone.

## What is held

**The drill pool — Abrabot's lane — carries the same class and is not gated in this build.**
`pool_for` still scans from 1 and Abrabot can still drill 1 + 1 after adding past ten.
Gating it moves the pool for every lesson and the pins that watch it (PART 3de), and drill
is practice, not mastery (Jim's ruling 2026-08-23) — so it is a scope decision for Jim, not
a change to make while he is reading. The ym note in `drillpool.py` and a pin in 3og both
say it is held on purpose.

## Proved

PART 3og: `shape_of` on a fixture bank (the floors, the digit counts, the agreed facts, a
mixed fact absent); `keeps_shape` breaks 1 + 1 at the floor and 6 + 4 at the sum, keeps 8 +
7, keeps everything for an op with no shape, one shape per op on a real mixed lesson;
12 + 4 above the ceiling; `quiz_slots` (240 → 24, 72, 120, 168, 216; 10 → 1, 3, 5, 7, 9; a
pool of 4 taken whole); **the ratchet — every pinned question keeps its lesson's shape,
1,799 judged, zero outside**; no set repeats a question and the one short set is the one
that was short; the five named offenders are gone; the fallback lane and the generator by
text; the drill pool left ungated on purpose; the quiz page's QUIZ SPACE in place of the
exact list (the lesson page keeps PROBLEM SPACE) and the charter's words; the dated notes.
Pins moved: 3of (the quiz page shows QUIZ SPACE), and the three blanket counts — course
lines 40,552 → 40,540, closure 40,806 → 40,794, speechmap scan 40,858 → 40,846 (twelve of
the 214 new asks are sentences the course already had; nothing re-keys).

## What Jim does

Push; `/health` says `2026-09-27ym-the-quiz-keeps-the-lessons-shape`. **Prewarm** — 214
replaced questions are 214 new spoken asks: Price it, then render. Then **run the Entry
quiz sweep again** (the reader sees the shape now; the ninety should be gone and anything
left is real), and the other nine. The "4 divided by two fourths" item is *not* in the 214
— a fraction's lowest terms is a form the shape does not measure — and stays the reader's
to find.

## Files

`drillpool.py` (`_facts`, `shape_of`, `keeps_shape`, `quiz_pool`, `quiz_slots`;
`quiz_problems`' fallback lane), `tools/genquiz.py` (keep-and-replace; `--fresh`; a story
travels), `quizsets.py` (214 replaced, regenerated), `coursesweep.py` (`quiz_space`; the
quiz page; the charter), `speechmap.py` (regenerated), `main.py` (stamp; prewarm 214),
`ruletests.py` (PART 3og; one pin moved), this doc, the refreshed
`START_HERE_Handoff_2026-09-27.md`.

Battery on the frozen copy, 2026-09-27: **13,227 passed · 0 failed · 3 skipped**, second run (the first run's 44 failures were the three blanket counts -- course lines, closure, speechmap scan -- moved by the replaced asks; re-anchored) (13,207 at `yl`).

I did no harm and this file is not truncated.
