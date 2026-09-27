# Build yo — The Quiz Prefers What The Lesson Did Not Demonstrate, 2026-09-27

The second Entry quiz sweep, read on `yn`: **102 → 25 findings, 23 lessons clean**. The
reader behaves now (`ym`'s QUIZ SPACE did its job — the seventy-one "not one of the listed
exact problems" are gone, and so are the thirty-one that `ym` fixed in the data). The 25
are three classes, all the instrument's or the data's, none the reader's.

Stamp: **`2026-09-27yo-the-quiz-prefers-what-the-lesson-did-not-demonstrate`**. PART
**3oi**.

## Class one — the quiz asked the example the tutor just worked (18)

*"Let's count together. 9 stars, then 6 more stars"* — and the teach beat's board says
`9 + 6 = 15`. *"4 groups with 2 stars"*, *"12 stars shared into 4"*, *"1 nickel and 2
pennies"*, *"In the number 258, what is the 5 worth?"* — each the very example the tutor
drew on the board a minute earlier. Not bank problems, so the shape let them through. A
child graded on the example they just watched is a weaker test than a new problem.

`drillpool.demonstrated(les, p)` reads it: the problem's numbers side by side among the
numbers of one teaching sentence or one board tag of the lesson's why, picture and teach
beats or its worked lines (`9 + 6 = 15`; `groups="4" each="2"`); a one-number problem
(count the stars, doubles) when a teaching tag carries it as an attribute's own value or
inside an `eq=` — a figure's `to="20"` is a window, not twenty stars, and a passing mention
in a sentence is not a demonstration. A measured rule, not a perfect one: a false hit costs
one candidate, a miss is the reader's to catch. **Across the canon, 357 of the 1,799 pinned
questions were demonstrated.** `tools/genquiz.py` now replaces a demonstrated question when
its op has a fresh, undemonstrated, shape-keeping candidate the set does not already hold:
**236 replaced, in 142 lessons**; every replacement is fresh. The other **121 stay** — thin
ops where every number was demonstrated (doubles: 4 through 8 all on the board; equal
groups, whose whole pool is five; *add past ten*, whose eleven candidates are all in the
worked walk-backs) — and the quiz page now marks each one: *"(the lesson's own example —
its op admits no more new problems; by design)"*, on the line and never in the spoken text.
The charter's Do-NOT list names the marker. `fresh_first` orders a pool undemonstrated
first and the fallback lane draws that way.

## Class two — "never told as a story" (5, all on making change)

The QUIZ SPACE printed every yes/no fact the bank agrees on, and one of them was *"never —
the problem is told as a story"* — true of the bank's `story` FIELD, false of an op whose
spoken form is *"A toy costs 49 cents. You pay 50 cents."* The reader read it as written.
The page says the story fact only when it is true (*"always — the problem is told as a
story"*, the two story lessons) and nothing otherwise.

## Class three — counting to 10 offered 11 (1)

`cnt`'s taps were the default neighbours, so ten stars offered `9 | 10 | 11` — a number the
course has not reached, in the quiz and in the lesson's own practice alike. `cnt` declares
its choices now: the neighbours in the middle, `8 | 9 | 10` at ten, `1 | 2 | 3` at one.
Nothing spoken changes.

## Proved

PART 3oi: `demonstrated` on a fixture (a worked equation and a tag's own value are; a pair
apart in a sentence and a figure's window are not); `fresh_first`; **the ratchet — no pinned
question is a demonstrated example while its op has a fresh problem to offer, 1,799 judged,
121 stay**; two named ones gone and three thin ones kept with the marker on the page; the
marker on the line and not in the spoken text; a fresh question carries none; the charter
names it; the QUIZ SPACE's story wording; `cnt`'s taps; the generator's order by text; the
dated notes. The three blanket counts re-anchored (course lines 40,541; closure 40,795;
speechmap scan 40,847).

## What Jim does

Push; `/health` says the yo stamp. **Prewarm: 236 replaced questions are 236 new spoken
asks** — Price it, then render. Then the quiz sweeps: Entry a third time if you want the
proof (the 25 should read as ≤ a handful, all marked), else straight on to the other nine,
back to back, pasting each. What a reading raises now that is not "outside the shape" or
"the lesson's own example" is a new class.

## Files

`drillpool.py` (`demonstrated_units`, `demonstrated`, `fresh_first`; the fallback lane),
`tools/genquiz.py` (replace a demonstrated question when a fresh one exists), `quizsets.py`
(236 replaced), `coursesweep.py` (the marker on the quiz page; the story wording; the
charter), `lessonscripts.py` (`cnt` choices), `speechmap.py` (regenerated), `main.py`
(stamp; prewarm 236), `ruletests.py` (PART 3oi; counts re-anchored), this doc, the refreshed
`START_HERE_Handoff_2026-09-27.md`.

Battery on the frozen copy, 2026-09-27: **13,251 passed · 0 failed · 3 skipped**, first run clean (13,236 at `yn`).

I did no harm and this file is not truncated.
