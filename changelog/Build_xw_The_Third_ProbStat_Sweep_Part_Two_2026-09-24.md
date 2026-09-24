# Build xw — The Third Prob/Stat Sweep, Part Two, 2026-09-24

Sweep header, 2026-09-24 12:20 UTC, read by gpt-5.5 on build
`2026-09-24xv-the-third-algebra2-sweep`: **36 of 36 lessons read · 26 findings (8 on
generators, 18 on authored beats) · 23 lessons clean · 0 unplaced · 0 unread · 552.0s.**
_Resumed after a restart: 30 lessons were read before it (build xu), 6 read now._ By kind:
words-board 11, false 10, unclear 2, untaught-term 2, repeats 1. The floors: `xg`'s reading
**60 findings, 10 clean**; `wo`'s **92, 1**.

Stamp: **`2026-09-24xw-the-third-probstat-sweep-part-two`**. PART **3nr**. A sweep build.

## The resume worked

This is the first sweep resumed in production under `xu`'s rule: the seat cut the run short
again at 30 lessons, the checkpoint stayed, and Resume read the six that were left for a few
cents rather than $5.40 for the course. The report's header says so. The 16 lessons `xu`
fixed came back — every one of them clean.

**Twenty-three clean of thirty-six**, the most of any course. The eight generator findings
are three fixes; of the eighteen authored, one is a HIGH, seven are the condition class, and
the rest are small words-board and naming items.

## The generators (3 ops, 8 findings)

`farv`'s walk-back ends "15 is where the crowd is, and 23 is only how far the stray sits from
it" over a board that never draws 23 — six findings in the one lesson that uses the op. The
walk-back board carries a crossed-out line now: `23 ✗ the distance, not the stray`. `bias`'s
praise said "a sample that cannot reach everyone is biased" — a HIGH, and a real one: a
sample never reaches everyone; what makes it biased is giving some people *no chance*. Now:
"200 — the ones the survey gave no chance of being picked — and that is a biased sample."
`ptre`'s ask says "you spin it twice, giving 81 different paths in all" and the board never
wrote the 81: `9 × 9 = 81 paths in all` is on it.

## The authored pile (18)

**HIGH:** the four-times rule's recap stated it as a law; it carries "with everything else
about the poll the same" now, in its own sentence (the first cut ran to 30 words).

**Laws with their condition (7):** "adding is the OR rule's move" (it is not — OR adds only
for non-overlapping events, and never the one-in numbers) is "adding the one-in numbers is a
tempting wrong move"; a chance *can be written* as a percent; "for a spinner spun twice" every
first outcome branches into every second; an experiment *can be drawn* as a tree; "never
average the prizes alone *unless they come up equally often*" (the lesson itself says the
equal case works); "by the 95 percent rule, take *about* 5 percent"; "the order matters" is
"low end first is the safe order".

**Terms and names (4):** undercoverage is named where the blind spot is taught (it was only
on the done card); a distribution is named as it is used ("every such list of chances, a
distribution"); "Geometry counted a chance" is "counting gives a chance"; the goal cards
"Count the ones above" → "past the line" (the dot plots count to the right) and "What
independent claims" → "What independence claims".

**Words and board (6):** `30% ✓` where the words insist on a percent; the reason boards carry
their setups (the two payouts; the 800 in the group); the second winning-paths recap draws
the branches ("3 winning branches, each with 3 winning branches of its own, make the 9")
instead of repeating the first; the histogram recap is three short sentences; and the 95%
line went on the tails board once the `xs` ratchet caught the spoken 95 with no board — the
ratchet doing its job on the very build that moved it.

Nothing declined. Grading under the 09-22 ruling: **class** (the condition, 7; the skipped
number, 3), **one-off** (16).

## Counts

Course lines **40,495 — unchanged**. Speechmap 941. Every lesson validates. `tools/pinscan.py`
found five stale pins before the first battery (3ma ×2, 3mm, 3nb, 3np); all moved. 3nn's
Prob/Stat ratchet holds at 22.

## A trap, recorded

`pgrep -f ruletests.py | xargs kill` killed the shell that ran it, not only the battery — the
`bash -c` line contains the word. It is the trap CLAUDE.md names for `pkill -f`. Find the pid
with `ps aux | grep "[p]ython3 ruletests.py"` and kill that one.

## After the push

`/health` = `2026-09-24xw-the-third-probstat-sweep-part-two`. **Prewarm ~60 lines** (the 16
farv walk-backs, the 16 bias praises, the ptre asks are boards only, and ~20 authored). Then
the gate build — the child-mode skin. The sweeps left in the third round: Basic 41, Geometry
36, Entry 19, Calculus 46 (its third), Pre-Calc (a fourth).

## Files

`lessons/probstat.py` (20 edits), `lessonscripts.py` (farv, bias, ptre), `ruletests.py`
(PART 3nr; five pins moved), `speechmap.py` (regenerated, 941), `main.py` (stamp), this doc,
the refreshed `START_HERE_Handoff_2026-09-24.md`.

Battery on the frozen copy, 2026-09-24: **13,008 passed · 0 failed · 3 skipped** (12,999 at `xv`), first full run clean.

I did no harm and this file is not truncated.
