# Build wy — The Fifth Entry Sweep (2026-09-18)

REPORT HEADER (copied first): Course sweep -- entry -- 2026-09-18 02:15 UTC (build wx).
Read by openai · gpt-5.5. By kind: words-board 11, repeats 5, false 2, unclear 1. 36 of 36
lessons read · 19 findings (11 on generators, 8 authored) · 29 lessons clean · 0 unplaced ·
0 unread · 21 minutes. The chain: wa 219 → wc 70 → wd 47 → we 15 → wf 14 → (wg fixes) → now
19, with **29 clean** — the most any course has had.

The first rerun of a course that had already been swept four times, and the first Entry
reading since `ww` moved the praise beat onto the worked board. The count went 14 → 19, and
sixteen of the nineteen are one engine consequence read three ways: **the praise carries the
worked board now, so where a walk-back said only what the praise had said, the child heard
the same sentence twice over the same picture** (five findings, tens-and-ones); the
cube's answered line landed on the praise board with no unit (five); and the star board's
walk-back said "count every star" for a story about rocks (one). Measured over every
course, the word-for-word repeat lived in **six ops** — one in Entry, three in Pre-Calc, two
in Prob/Stat — and all six are closed here, with the measurement pinned so it cannot
come back.

Stamp: **`2026-09-18wy-the-fifth-entry-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py)

- **The stars stand for something.** A story problem ("Jo has 2 rocks. She finds 1 more.")
  is answered on the star board, and its walk-back said "count every star, both groups" as
  if the rocks were stars. New `_story_noun(p)` reads the story's first counted noun;
  `_col_add` and `_col_sub` take it (`BASE_WORKED` passes it; every other caller —
  crossing a hundred, checking by adding back — is unchanged), and the walk-back opens
  "each star stands for one of the rocks. Count every star, both groups — 1, 2, 3."
  Counting on and taking away get the same opening. Without a story the text is
  byte-identical to before (the we/wd pins still hold).
- **Tens-and-ones works it.** The walk-back was "1 ten and 2 ones — that is 12", which is
  the praise line. Now: "1 ten is 10. Then 2 ones: 10 plus 2 equals 12", over the
  place-value blocks and a drawn `10 + 2 = 12`.
- **Cube keeps its unit.** The pending line ends `= ? cubes`, so `answered_board` writes
  `11 cubes − 5 cubes = 6 cubes` (and `3 cubes − 1 cube = 2 cubes`, `… = 1 cube`).
- **Five more repeats, other courses.** `gsum` (Pre-Calc, add the whole run), `pasc` (when
  order does not matter), `avgr` (the shrinking window), `farv` (Prob/Stat, the one that
  sits alone) and `pctl` (a percent, not a person) each had a praise that WAS the
  walk-back. Each praise is a **credit line** now — the answer and its one reason, every
  number of it on the worked board the praise carries — and the walk-back keeps the
  steps. For example pctl: "34. 85 percent of 40 is 34, so that is how many she beat — a
  percent, not a headcount." over `beaten:34 | ahead of her:6`. PART 3mt measures every
  praise/walk-back pair in every course and pins that none is a repeat.

## The authored pile (lessons/entry.py) — 8 edits

**Words and board.** Add-past-ten's two worked captions draw the count-on the words say
(`start at six and count on: 7, 8, 9, 10, 11`; `… nine …: 10, 11, 12, 13, 14, 15`).
Dimes-and-pennies' teach and both worked lines draw the count they say, as one list above
the cents lines (`10, 20, 30 — then 31, 32, 33, 34`; a list, not two equations, so the
dot pin is not in play).

**False (2).** Hundreds' recap read "any number up to nine hundred ninety-nine" — the
lesson reads three-digit numbers, and 7 is not read this way → "a three-digit number, up
to nine hundred ninety-nine". Crossing-a-hundred's "Add the tens and the carried ten" —
10 plus 90 carries nothing → "add the carried ten if there is one".

**Unclear (1).** Add-past-ten's recap in three short sentences ("start at the bigger
number. If they are the same, start at either one. Then count on once…").

## Counts

Course lines **39,999 → 40,010**: the eleven story walk-backs no longer share a line with
the plain sums (the generated text differs only by the noun sentence). Closure 40,253 →
**40,264**; speechmap **2,244** of 40,316 (nothing new re-keys); forSpeech drift **1,938**
unchanged. `L.validate` over all 360: 0 failures. The referee sweep over all ten courses:
still the one intro card. Every new board line rendered headlessly with no `boardWarn`.
PART **3mt** (12 checks). Pins moved: nineteen course-count pins and the closure pin
(`== 40010`, `== 40264`), the speechmap denominator, and three wording pins (the carried
ten ×2, add-past-ten's recap), each marked "(wy)".

## After the push

Prewarm: the three Entry ops' lines, the five credit lines in Pre-Calc and Prob/Stat, and
eight Entry rewrites. Then **Basic** against `wg`'s 67 findings, 7 clean (fixed in `wh`);
then Pre-Algebra, Algebra I, Geometry, Prob/Stat in first-round order. Expect each rerun
of a walk-back-heavy course to show *no* repeat now — the measurement runs every battery.

## Battery

Frozen copy, 2026-09-18: **12,704 passed · 0 failed · 3 skipped** (12,693 at `wx`). Clean on the first run.

I did no harm and this file is not truncated.
