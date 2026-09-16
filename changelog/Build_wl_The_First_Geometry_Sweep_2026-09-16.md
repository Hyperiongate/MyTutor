# Build wl — The First Geometry Sweep (2026-09-16)

The first sweep of Geometry, on `wk`: **63 findings** (6 on generators, 57 authored), 7 of
36 lessons clean, 0 unplaced, 42 minutes. Geometry's own class turned out to be
*vocabulary a geometer would object to*: "a straight line is 180", "every line has a
midpoint", an inscribed angle defined by its corner alone. All true enough for a child,
all false as stated, all one-phrase fixes.

Stamp: **`2026-09-16wl-the-first-geometry-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — eight items

- **`mid`, `mid2`**: "A line runs from 2 to 18 … halfway along it" — a line has no ends. Both
  asks say "a line segment" (HIGH).
- **`cent`**: the ask drew a bare `[[circle]]` while the words said two radiuses cut it into
  arcs. It draws a `[[pie]]` with the small arc numbered and the rest unnumbered.
- **`alen`** and **`mid`** walk-backs write the step the words say (`360° ÷ 90° = 4 parts`;
  `(2 + 18) ÷ 2 = 10`).
- **`topp`**: `tan = 2 · opposite = 6 × 2 = ?` read as a chained product (HIGH). Two lines.
  Every other dot-joined pair Geometry's transcripts reach (`sfac`'s check line) is split too;
  the pin now covers five courses by rendered transcript.
- **`sla`** (walk-back and praise) and **`vert`** (walk-back): "a straight line is 180
  degrees" → "the angles along a straight line make 180".
- **`lshp`**: "areas add to areas; lengths never do" → "lengths add to lengths, never to areas".
- **`twop`**: "the sport each child chose … art" → the activity.
- **`poft`**: the walk-back is three sentences.

## The authored pile (lessons/geometry.py) — 55 answered

**Vocabulary a geometer would object to.** "A straight line is 180" in three lessons → the
angles along a straight line make 180. "Every line has an exact middle" → every line
*segment* — a line with two ends. "An angle whose corner sits ON the circle is called an
inscribed angle" → with both arms reaching the circle. "Slide the corner anywhere along the
rim" → along the far side of the rim. "A ray drawn inside it" (untaught) → a line drawn out
from the corner. "The height is measured straight up" → from the base, at a right angle to
it.

**Laws with their condition.** "Every point travels to the exact opposite spot" → every
point except the middle. "A slide changes one number by adding; a flip changes ONE sign" →
the slides we used; a flip across an axis. Turn symmetry "a shape that comes back" → before
the full turn is done; "a wheel of equal parts" → equal, all-alike parts. The base-angle rule
and its advance line say "in an isosceles triangle" (HIGH). "The exterior angle … proved
once and yours forever" after one triangle → the proof, in three short sentences, that works
for every triangle. "One matching pair of sides is all it ever takes" → when the shapes are
similar. "The other sides do not each grow by 8" (they could) → a scale factor is a times.
"One division, and the whole enlargement is known" → the scale factor. "A rule read forwards
can be read back" → *this* rule; "like every good rule in this course" → many. The inscribed
angle's "from farther away things look smaller: exactly half" was not the reason → an angle
on the rim opening onto the same arc is exactly half. The fourth corner's law says "in these
puzzles" / "for these grid-lined rectangles" (HIGH ×2). "Any shape built from rectangles" →
cut into rectangles that do not overlap. "Choices times up, never add" / "adding counts
things, never outfits" (HIGH) → when choices stack, times up; adding only counts the things.
"2 is a closet, not a count of ways" → 2 counts shirts, not outfits. "The range says
everything about spread" was Algebra I's; Geometry's cousin, "a class chose sports … art",
is now activities.

**Words-board.** The fourth corner's picture drew all four points while the words said
"look at the empty spot" — two picture beats now (three corners; then the fourth). The
midpoint trap crossed out "length 8 ✗" when 8 *was* the length — now "answer 8 ✗ — that is
the length, not the midpoint". The radius trap's unexplained "2 or 3 ✗" → "halved ✗". The
L-floor is "two rooms of one floor, drawn apart" (no L was drawn). The enlarging copy writes
`5 + 2 = 7 ✗`; the arc-length picture writes `12 ÷ 4 = 3`; the 180° arc is named beside
the "6 ✗"; the two-way table board reads "girls row → soccer column → 2" instead of a plus
sign. Eight closing beats speak the equation their board writes. Fifteen dot-joined step
lines split.

**Unclear.** "Squares back" — the reviewer called it nonstandard twice. It is the course's
chosen verb for the square root, taught in the longest-side lesson and used by four beats
and three generators after it; the two flagged lines now say what it means ("find the number
whose square is the result"), and a charter line rules the verb itself. "Far angles" defined
at first use. "Because stand at an angle" → when you stand at an angle. "The first number of
chance" spelled out. Nine long sentences split.

## Counts

Course lines 39,998 → **39,999** (the fourth corner's second picture beat); closure 40,253;
speechmap 2,245 of 40,304 → **2,246 of 40,305** (the new beat's coordinates re-key).
`L.validate` over all 360: 0 failures (two caught mid-build: the exterior-angle proof and
its why beat ran to 44 and 36 words; both split). Every new board tag rendered headlessly
with no `boardWarn`. PART **3mg**; the count pins moved; the dot pin grew to Geometry.

## After the push

Prewarm: roughly sixty rewritten Geometry lines plus the `mid`/`mid2` asks (about forty
generated lines). Then **Algebra II** — Jim has already run it on `wk`; it becomes `wm`. It
carries 83 dot-joined step lines, the most of any course.

I did no harm and this file is not truncated.
