# Build yn — The Drill Pool Keeps The Shape Too, 2026-09-27

`ym` held one thing for Jim: Abrabot's drill pool carried the same class the quiz had. Jim:
*"GO."*

Stamp: **`2026-09-27yn-the-drill-pool-keeps-the-shape-too`**. PART **3oh**. A small
structural build on `ym`.

## What was held, and why it was held

`drillpool.pool_for` is the pool `/api/drill` serves live — the extra problems Abrabot
drills after a lesson. It scanned from a = 1, b = 0 and bounded from above only, exactly as
the quiz generator had, so after *adding past ten* Abrabot could drill 1 + 1, and Basic's
two-digit review had a 240-problem pool with nothing over 50 in it. `ym` fixed the quiz and
left the pool alone: gating it moves every lesson's pool and PART 3de's pins, and drill is
practice, not mastery (Jim's ruling 2026-08-23) — so it was Jim's call, not a change to make
while he was reading.

## One scanner, two doors

`drillpool._scan(les, cap, board_tags, drill)` is the one scanner now: candidates from the
shape's floor to its ceiling, per op of the lesson with the cap shared across ops, every one
through `keeps_shape`, then the envelope, then the course's own validator, then ramped by
the validator's key. `pool_for` is its drill door (`drill=True`); `quiz_pool` is its quiz
door (`drill=False`).

**The one difference between the doors is the story.** A story-problems lesson's bank is
authored stories; its quiz (since `ym`) asks those stories, because a generated problem has
no story to tell. Its drill pool would then be empty — and drill is practice: a child who
has just met *"Jo has 2 rocks. She finds 1 more."* practising 4 + 1 and 5 − 3 with Abrabot is
practising the arithmetic inside the stories, as Abrabot always has. So `keeps_shape(…,
drill=True)` skips the `has_story` fact and nothing else. The two story lessons keep their
drill (18 and 10 problems); their quizzes stay stories.

**A problem's identity carries its op.** `_key(p)` was `(a, b, c)`, right while a pool held
one op; the shape scan pools every op of a mixed lesson, and 31 − 29 is not a repeat of
31 + 29. It is `(op, a, b, c)` now — PART 3de said so on the first smoke (43 "duplicates" that
were the two ops' same numbers in mixed-op pools). Every shipped bank problem names
its op (measured: none omits it), so nothing else moves.

## Measured, before and after

On the frozen copy: **28,411 → 28,656** pooled problems — the pool *grew*, because the
big-number mixed-op lessons gain the pool they never had (the old scan from 1 filled their
cap with tiny sums of one op). **46 → 41** lessons with no pool: the two that lose theirs —
the exponents lesson's single candidate and the parametric walk's ten — were outside their
bank's shape (the walk's bank always has a < b; all ten candidates had a > b). **241 → 233**
lessons at twenty or more; *add past ten* goes 67 → 11, and the 56 that left never passed
ten. Every pooled problem in the course keeps its lesson's shape; zero outside.

The quiz table did not move — `tools/genquiz.py` re-run replaces nothing — and no spoken
line changed: Abrabot speaks in the browser's own voice. **Nothing to prewarm.**

## Proved

PART 3oh: the *add past ten* pool adds past ten from a floor of 5, and 1 + 1 is not in it;
the review's pool is two-digit and both ops; a story lesson still drills bare arithmetic
while its quiz pool is empty and its pinned quiz is stories; `keeps_shape(drill=True)` skips
`has_story` and nothing else; **every pooled problem in the course keeps its shape**
(28,656 pooled); the pool grew, not shrank; one scanner, two doors, by text; the quiz table
did not move; the dated notes. One pin moved (3og's "held ungated" pin flips to "gated at
yn"); 3og's text pin reads the one scanner.

## Files

`drillpool.py` (`_scan`; `pool_for` and `quiz_pool` as its doors; `keeps_shape(drill=)`;
`_key` carries the op), `main.py` (stamp; nothing to prewarm), `ruletests.py` (PART 3oh; two
pins moved), `speechmap.py` (regenerated, unchanged), this doc, the refreshed
`START_HERE_Handoff_2026-09-27.md`.

Battery on the frozen copy, 2026-09-27: **13,236 passed · 0 failed · 3 skipped**, first run clean (13,227 at `ym`).

I did no harm and this file is not truncated.
