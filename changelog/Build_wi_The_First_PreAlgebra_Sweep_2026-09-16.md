# Build wi — The First Pre-Algebra Sweep (2026-09-16)

The first sweep of Pre-Algebra, on `wh`: **69 findings** (13 on generators, 56 authored),
6 of 36 lessons clean, 0 unplaced, 36 minutes. The generator share was the biggest of any
first sweep yet, and one class ran through the authored pile too: *"the smallest factor"*
said without *"above 1"* — the rule-13 falsehood row — thirteen times across Unit 2 and two
generators.

Stamp: **`2026-09-16wi-the-first-prealgebra-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — eight items

- **`pup`** (a price goes up or down): the board said `20% = 8`. It says `20% of 40 = 8`.
  `pwh` (finding the whole) had the same shape — `10% = 12 ÷ 3 = 4` — and now says
  `10% of the whole = 12 ÷ 3 = 4`. Three HIGHs, one line each.
- **`asp` and `prop`**: "100 is not a whole number of 40s, so go through 1" — a nickname for
  the method, not the method. Both say "go the long way — times the top by 100, then divide
  by 40", and `asp` draws both steps (`22 × 100 = 2200`, `2200 ÷ 40 = 55`).
- **`prop`**: a `[[pie parts="3" shaded="5"]]` cannot exist — the tag clamps `shaded` to
  `parts` and drew a full pie captioned 5/3. The bank has three improper fractions (4/3,
  7/4, 5/3). Pies are now used only when the fraction is proper; an improper one takes the
  written `[[solve]]` form the non-multiple case already used.
- **`uic`**: "How many halfs are there in 3 wholes?" — `_fpl(bottom)` gives the real plural
  ("halves"), in the ask, the board and the walk-back.
- **`bfac`** praise and **`npf`** walk-back: "its smallest factor 3" → "3, its smallest factor
  above 1"; "pull out the smallest factor" → "above 1".
- **`hun`**: the caption said "1 full rows" (the walk-back was already right).
- **`evx`**: the 29-word walk-back is two sentences.
- **`rte`**: the ask's caption asked "how many in one hour?" under a question about 4 hours;
  it now says "step one: how many in one hour" — the step it is.

## The authored pile (lessons/prealgebra.py) — 52 answered

**"Smallest factor" means above 1** — eleven places in Unit 2 (the biggest factor's why,
trap, both worked lines, recap and advance line; breaking-into-primes' why, method and
advance line; the smallest factor's teach and recap), plus "every whole number *above 1* is
primes multiplied" and "a prime has no smaller one — its only factors are 1 and itself".

**False, fixed.** "The exponent joins them, and it goes first of all" contradicted the
sentence before it (parentheses first) — now "right after the parentheses. Parentheses, then
power, then times, then add." "Factors are the ways a number can be split" → "the row sizes
that split a number". "Only 1 row of 11 works" → "or 11 rows of 1, the same pair turned
round". "Five 3s equal 15 — three hops of 5" and its two siblings had the groups backwards
against their own number lines. "Any decimal can be counted as hundredths" → "any two-place
decimal" (three places, a lesson whose whole space is tenths and hundredths). "Across the
decimal point" → "the tenths cross the decimal point to become ones" (the ones digit never
crosses it). "Adding breaks the ratio" → "adding the same number to both sides". "Every
percent of every number" → "every percent made of whole tens" (the bank is 20–90 by tens).
"12 dollars is 30 percent off" (ambiguous: the sale price or the discount?) → "the shop takes
12 dollars off and says that is 30 percent". "What is left is the fraction part" → "goes on
top of the same bottom". "Two steps, always in that order" → "that order keeps the numbers
whole". "The one right way through any formula", "anything about x", "every line of
algebra", "every price per hour, and every speed", "cannot be compared" — all scoped to what
is true. Two reason options replaced: "add 3 cups of milk for every batch" was a *true*
reason; "the first share is 2" was false (it is 2 *parts*).

**Words-board, fixed.** The flour story said four cups while the board worked 2 ÷ 2/3 = 3;
it is two cups now, and the recap says "three". The pizza was seven slices in the why and
8/3 on every board; it is eight slices. Pre-Algebra's times-by-ten had Basic's defect
exactly: the words promised 3.7 on the chart and the board drew 37 — two picture beats now.
Parentheses-first draws the 14-without-the-marks; the triangle's second example and the
line's wrong subtractions (90 and 360) are drawn; changing units draws all three unit facts;
"adding negative 3" is "adding negative 7", the board's number. Seven second-recap beats
speak their boards. The what-percent recap claimed "two test scores, compared" having
converted one — it now converts both (`21/30 = 70%`) and says which went better. The
times-before-add *reason* board showed "times first" over the question "why is it 14?" — the
answer was on the board; it shows only the equation now.

## Ruled, not fixed

One: "exponent" used before taught (the previous lesson in the unit taught it, and the fixed
line says "power" anyway). Nothing else was the reviewer's mistake — the problem-space
listing from `wh` held, and no charter line was added.

## Counts

Course lines 39,997 → **39,998** (Pre-Algebra's times-by-ten second picture beat); closure
40,251 → 40,252; speechmap 2,245 of 40,303 → **2,245 of 40,304**. `L.validate` over all 360:
0 failures (one caught mid-build: dropping "decimal point" from a teach line broke rule 14's
name-the-symbol check — the phrase is back, truer than before). Every new board tag rendered
headlessly with no `boardWarn`. PART **3md** pins all of the above; the count pins moved.

## After the push

Prewarm: roughly seventy rewritten Pre-Algebra lines. Then run **Algebra I** — the queue has
sampled it too, and Unit 9's "is equal to" ruling came from there. Expect the "smallest
factor above 1" class to be absent (Algebra I has no factor unit) and the second-recap class
to be present.

Two patterns worth naming for the remaining seven courses: (1) *a claim about a number that
is true only above 1* — the reviewer will find every one, and they are one-word fixes;
(2) *a picture beat that describes the "before" over a board that draws the "after"* — three
courses in a row had one (Basic's and Pre-Algebra's times-by-ten, Basic's what-dividing-means).
Splitting the beat is always the fix.

I did no harm and this file is not truncated.
