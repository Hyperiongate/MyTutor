# Build yz — the picture starts where the words start (2026-09-30)

Stamp: `2026-09-30yz-the-picture-starts-where-the-words-start`. Battery: **13,408 passed · 0
failed · 3 skipped** (PART 3ot added; three pins moved to the new shapes — the choices-tag set,
"the stars are built visible", and 3gw's count of counting drawings; the cadabra VERSION pin).
**Prewarm: the count-on walk-backs** — every `_col_add` walk-back whose second number is the
bigger one now says the swap ("5 plus 8 equals 8 plus 5, so start at 8…"), and Entry u2's
add-past-ten worked example changed its words. The prewarm lists them after the push.

Four of Jim's first-family flags, all of them the same shape: the words were right and the
thing on the screen was not what the words described. A child cannot tell which one to
believe, so both have to agree.

## What was wrong, and what it is now

**Count-on drew the picture in the wrong order** (F21). The lesson says "start with six, the
bigger one, and count on: seven, eight, nine, ten, eleven" — and the board drew five stars,
then six, every star numbered from one. Now the generator (`_col_add`'s count-on branch) and
Entry u2's worked example draw the BIGGER group first, say the swap out loud when the numbers
came the other way round (`5 + 6 = 6 + 5` as a step line, "five plus six equals six plus
five"), and the board has a new attribute: `[[objects counton="1"]]` lands the first group
plain — it is already counted — and numbers only the added stars from the group's size plus
one. Six stars, then ✓7 ✓8 ✓9 ✓10 ✓11, ticking in with the count-along. `counton` refuses a
take-away, two rows, no adds, or more than twenty on the board, and `count="1"` wins when both
are set. The lesson's picture and teach beats use it too (they used `count="1"` — every star
numbered from one under words that said start at eight).

**The 24 squares were not there** (F28). The Geometry review says "a rectangle 6 long and 4
tall covers 24 squares" over one plain rectangle. `[[rectangle]]` in area mode draws its unit
squares now — alternating shades, the figure's own colour for the lines, and each cell
numbered 1 to w×h when there are thirty or fewer — so a child can count them. An ask (`ask="1"`,
"count the squares inside") draws the cells and no numbers: the answer is never on the board.
Half-shaded rectangles are left as they were.

**The pencil's mouth moved with nothing playing** (F24). A clip cut off by the next line, or
paused by a deadline, never fires `ended`, so `mt:silent` never came and the mouth stayed
open through the ready gate and past a lesson's end. The frame loop now also reads the page's
audio element and the browser's synth: 600 ms with neither sounding closes the mouth. The
events are still trusted first; this only ends a voice that has already ended. `Cadabra.speaking()`
is a read-only hook for the battery's drive.

**The right answer sat in the same seat** (F7). Jim tapped the second choice on all 45 Entry
questions and "did pretty well": the bank puts the key at index 1 in 28 of Entry's 45 and at
index 3 in none. `challenge.html` deals the four choices in a fresh random order on every
render and grades against where the key landed; the banks' verified `a` is untouched. The
same tilt lived in the scripted lane: `choices_for`'s rotation was `(3a + b + c) % 3`, and 3a
is 0 mod 3, so `a` never counted and the first button held the key in 43% of the canon's asks
(1,537 / 1,165 / 887 over 3,589). Weighted by three primes and the op's letters it deals
1,190 / 1,164 / 1,235 — still fixed per problem, so a replay renders identically.

**Read and left** — **F8** (the placement showed every unit's score and recommended unit 2 over
a better unit 3 and 4): that is the Course Assessment's design of 07-28 — foundation-first,
the EARLIEST unit under 70% is where the path starts, and every unit is scored and shown. The
45-tap length for a six-year-old's first sitting stays Jim's call (open).

## Proof

`tools/yzdrive.py` (PART 3ot runs it): the real `session.html` and `challenge.html` under a
stub API. It proves: the count-on row lands six plain stars and ✓7..✓11 on the added ones;
the 6×4 rectangle draws 24 unit squares in the figure's colour numbered 1 to 24, and the ask
draws its 15 with no numbers; the mouth opens on `mt:speaking`, closes on `mt:silent`,
opens again, and closes within a second when nothing is sounding; over 200 renders of the
Entry bank the key lands on every one of the four buttons, none above 45%. PART 3ot also
pins the generator's walk-backs (swap said when needed, not said when the bigger number was
already first), the worked example's words, the board and figure code, the deal in
`challenge.html`, and `choices_for`'s spread over the whole canon. PART 3gw now counts twenty
drawings that count from one and three that count on (add-past-ten's picture, first teach
beat and worked example).

## Files

`static/board.js` (`counton`, `.objhad`), `static/math-figures.js` (`rectangle()` cells),
`static/cadabra.js` (the sound check; `Cadabra.speaking()`; VERSION `2026-09-30yz`),
`static/challenge.html` (the deal), `lessonscripts.py` (`_col_add`'s count-on branch;
`choices_for`), `lessons/entry.py` (u2 add-past-ten), `tools/yzdrive.py` (NEW),
`ruletests.py` (PART 3ot; 3gw's count; two pins moved), `main.py` (stamp), `speechmap.py`
(regenerated), this doc.

I did no harm and this file is not truncated.
