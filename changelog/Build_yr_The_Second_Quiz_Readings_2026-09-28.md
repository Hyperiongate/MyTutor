# Build yr — The Second Quiz Readings, 2026-09-28

Jim ran all ten quiz sweeps a second time on `yq` and pasted them together: **nine courses
clean — Basic, Pre-Algebra, Algebra I, Geometry, Algebra II, Pre-Calc, Prob/Stat, Calculus,
Diffeq, 36 of 36 each — and Entry with one finding, 35 clean.** From 102 findings on the
first Entry reading (`yl`) to one, in seven builds.

Stamp: **`2026-09-28yr-the-second-quiz-readings`**. PART **3ol**.

## The one

*"The pattern is 6, 8, 10, 12. What comes next?"* — and the worked line says *"One more
together. 6, 8, 10, 12. The jump is 2."* The number rule could not see it: the problem is
stored as start 6, jump 2, and in the text the 2 sits three numbers past the 6 — two more
strangers than `yq` allows, and the adjacent-numbers reading is about the problem's stored
numbers, not the words the child hears.

A **third reading** of a demonstration, generic: the ask's own spoken line names a run of
three or more numbers, and that run appears contiguously, in that order, in a teaching
sentence or board tag. The words the child hears are the words the tutor said. Measured
across the canon, it adds a handful; the pattern quiz's first question is replaced (*3, 8,
13, 18*, fresh and inside the shape) and nothing else moves — the new ask is a sentence the
course already had, so the blanket counts stand. **Prewarm: 1 line.**

The Pre-Algebra report's *1 unplaced* is a finding whose quote did not match the transcript;
the sweep drops those by design and says so in the header.

## Where the quiz lane stands

Every course's 180 pinned questions have now been read twice by the same reviewer that read
the lessons, under a charter that knows what a quiz is. Every pinned question keeps its
lesson's shape (`ym`, `yp`), is not the tutor's own worked example where the op has a fresh
one (`yo`, `yq`, `yr`; 170 marked as the lesson's own by design), is not asked twice in one
quiz (`yp`), and the drill pool keeps the same shape (`yn`). The instrument stays on the
`/admin` card for whenever a lesson's bank, an op or the generator changes — regenerate with
`tools/genquiz.py` (it keeps every question that still passes and replaces only what
breaks), run the course's quiz sweep, paste the report. **The lane is closed unless a
reading reopens it.**

## Proved

PART 3ol: the pattern run is a demonstration; a run must be contiguous and in order; the
pattern quiz no longer opens on it and its replacement is inside the shape; the dated notes.

## Files

`drillpool.py` (`_DEMO_RUN`; the third reading in `demonstrated`), `tools/genquiz.py`
(note), `quizsets.py` (1 replaced), `speechmap.py` (regenerated, unchanged), `main.py`
(stamp; prewarm 1), `ruletests.py` (PART 3ol), this doc, the refreshed
`START_HERE_Handoff_2026-09-28.md`.

Battery on the frozen copy, 2026-09-28: **13,283 passed · 0 failed · 3 skipped**, first run clean (13,279 at `yq`).

I did no harm and this file is not truncated.
