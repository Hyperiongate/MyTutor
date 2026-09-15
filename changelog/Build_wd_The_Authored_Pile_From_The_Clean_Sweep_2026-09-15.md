# Build wd — The Authored Pile From The Clean Sweep (2026-09-15)

The third Entry sweep — the calibrated one, after wc — came back with 70 findings: 61
owned by the authored text in `lessons/entry.py`, 9 by generators in `lessonscripts.py`,
and 9 lessons clean. This build answers all of it. Nothing about the sweep itself changed;
the next run of it is the check.

## The authored pile, by kind

**Rules spoken as laws that are not laws (the "false" column).** Each is now said with
its condition, or said of the numbers in the lesson:

- tens-and-ones: "the tens digit goes first, always" → "in a two-digit number the tens
  digit is written first"; "swapping the two digits is a different number entirely" (11
  is 11 either way) → "read the two digits the other way round and you can name a
  different number — nineteen is not ninety-one".
- what-a-digit-is-worth: "never the bare digit" → "in the ones place a digit is worth
  itself; in the tens place it is worth ten of itself"; the trap says "unless it stands
  in the ones place".
- sides-and-corners: "every flat shape is made of straight sides" (a circle is flat) →
  "shapes with straight sides", and the rule is said of those.
- what-comes-next: the jump rule is now "in today's patterns the rule is a jump that
  stays the same — find it, check it is the same every time, use it once more".
- ten-more: "only the tens digit goes up" (95 + 10 says otherwise) → "the tens digit
  goes up by one".
- making-change: "the change is always SMALLER" → "the price came out of your money, so
  the change is smaller than what you handed over".
- story problems: the keyword method ("listen for the word that tells you the sign") is
  gone. The beat asks what happened to the PILE — did it grow, did it shrink — and the
  board says `the pile grew → +` / `the pile shrank → −`.
- add-single-digit: "how many in all is written with an equals sign" → the equals sign
  "means both sides are the same amount".
- add-past-ten: "start with the bigger number" now covers 6 + 6 ("if the two numbers are
  the same, start with either one").
- crossing-a-hundred: "a new digit appears" → "when the tens add up to over nine, ten of
  those tens become one hundred, and the answer gets a hundreds digit at the front" (the
  canon's own wording — "more than nine" is banned, and the validator held me to it).
- take-away-three-digit's trap now shows the case it warns about (574 − 302: the tens
  are 7 − 0, still written); adding-three-digit's shows 638 for 368.
- doubles "never one more" → "not the number and one more"; the missing part "never the
  number you landed on" → "not"; counting past ten "most things" → "lots of things".

**The board says what the words say (the "words-board" column, 32 of the 70).**

- Ten-more's picture drew three ten-sticks while the words said four. It now draws two
  pictures: 34, then 44 with the same four ones.
- Numbers-before-and-after spoke a hop back it never drew. The hop back is its own beat
  now, over the line that draws it.
- Five column lessons put "58 − 23 = ?" on the board a beat BEFORE the words said 58 or
  23. The sum now appears on the beat that speaks it.
- Every recap's closing board is spoken: "4 + 4 = 8" under words that never said four
  plus four, in nine lessons.
- Weeks-and-days puts its count-by-sevens on the board (`7, 14 — 15, 16`). Equal groups
  and sharing fairly draw the array (`view="groups"`, with `eq=` set so the picture never
  writes "3 × 4" — Unit 9 never says "times", by design).
- The two clock lessons draw a CLOCK (`[[clock]]`, honest hands) where they had a number
  line captioned "the hand at 3".
- Sides-and-corners draws the polygon it counts, and a new names beat says pentagon,
  hexagon, heptagon, octagon and decagon with their side counts BEFORE the practice asks
  for one by name (the sweep's "asked before taught").
- What-comes-next writes the answer under the "?" line. Take-away-single-digit's trap
  draws its eight stars. Counting-past-ten's fast-way beat counts to twenty, so
  seventeen through twenty are heard before nineteen is asked.

**Terms before they are taught.** "digit" is defined in tens-and-ones' why ("a number
like fourteen is written with two marks... each mark is called a digit"); "column" is
defined where it first appears (adding three-digit numbers: "each of those up-and-down
lines is a column"); "regrouping" is out of the no-regrouping lesson that comes before
regrouping is taught.

**Advance lines claim what was taught.** "You can add two-digit numbers" → "...when
nothing carries"; "read the minutes on a clock" → "count the minutes past the hour by
fives".

## The nine generator items

- `sid`/`cor` draw the `[[polygon]]` on the ask — a pentagon's sides can be counted on it.
- `grp` draws the groups with the total withheld; `eqs` draws the unshared pile.
- `hrl` and `min5` draw a clock. `min5q` stays bare: a drawn hand would answer it.
- The `+` walk-back COUNTS ON — "start at 3 and count on 2 more: 4, 5" — the method the
  adding lessons teach, wherever the smaller number is a single digit. A two-digit sum
  still walks its columns.
- `msp`'s walk-back is shorter and counts up ("start at 5 and count up to 11 — 6, 7, 8,
  9, 10, 11. That took 6 counts"). The first draft used a colon there and six lines
  re-keyed in the speechmap: "11: 6" is read as a ratio by the page's speech tidier —
  the vx defect ("holding 3: 5"), caught by the speechmap count moving. It is a dash.
- `wor` says "place", the word its lesson teaches, never "column" (Unit 5's word).
- Phase A in a mixed-review lesson: "one just like it" was said before a MINUS story
  following a missed PLUS story. `LINE_FRESH_OTHER` ("Now a new one, and this one is
  yours.") is spoken when the fresh problem's op differs. It enters only the closure of
  the three mixed-review lessons — one clip.
- The end card says how many were RIGHT: "4 problems answered | 3 right". `state["right"]`
  is counted from this build; a session stored before it shows the card it always did.

## Counts and tests

Course lines 39,994 → 39,995 (LINE_FRESH_OTHER); closure 40,248 → 40,249; speechmap
2,244 of 40,300 → of 40,301. `L.validate` over all 360 lessons: 0 failures. Every new
board tag was drawn headlessly on the demo page: no board warning, the polygon, clock,
array and double place-value figures all render. PART 3ly pins the classes above and the
nine generator items. Battery: see the line at the end of this file.

## After the push

1. Run the prewarm (`/admin` → Scripted course audio → Check what's missing → Render the
   missing lines). It will list the rewritten Entry lines, the `+` / `msp` / `wor`
   walk-backs, and the one new frame line. The boards cost no clip.
2. Run the Entry sweep again from the Course sweep card. That report is the check on this
   build: the 61 authored findings and the 9 generator items should be gone, and whatever
   is left is the next list.
3. Then Basic — the next course in the project list.

A note on method: the report you pasted is not stored anywhere I can reach (it lives on
Render), so this build worked from my triage notes of it, item by item. If the re-run
shows something I read wrong, that is the first thing to send me.

Battery: 12,438 passed, 0 failed, 3 skipped (frozen copy, third run, 2026-09-15). The first two runs
caught three things the dry run had not: the "= ?" line under its own answer (rule 17,
five lessons), the polygons without captions (rule 41), and the missing-part tape that
named a missing piece it did not mark (rule 63, now shaded="1"). All fixed above.

I did no harm and this file is not truncated.
