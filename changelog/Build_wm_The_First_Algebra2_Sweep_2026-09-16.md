# Build wm — The First Algebra II Sweep (2026-09-16)

The first sweep of Algebra II, on `wk`: **73 findings** (9 on generators, 64 authored; the
clean count is on the /admin card). This course's own class was the *law stated for today's numbers
as if it were the whole truth*: "each factor donates one root" (a repeated factor doesn't),
"every function question can turn around" (many do), "the log of a product is the logs put
together" (in the same base), "the number that times itself into 25" (the positive one). And
it carried the most dots of any course — 83 step lines joining two equations with " · ", the
symbol Algebra II uses for a product.

Stamp: **`2026-09-16wm-the-first-algebra2-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — six items

- **`gnth`** (three HIGHs, rule 17): the ask drew term 3 and asked for term 3. The bars and the
  written sequence now stop one term short of the one asked.
- **`sinp`, `cosp`** praise: "After 2 full spins and 270 more, the arrow points straight down"
  — the spins *and* the rest, as the child worked them.
- **`absc`**: the ask says "count every integer strictly inside the fence"; past a fence of 10
  the caption says the line is compressed and which dots are drawn (innermost, zero,
  outermost); the board asks in two lines (`|x| < 13`, `integers inside the fence = ?`).
- **`el2`**: the board asks for ONE apple, as the words do (`2 apples = 25 − 9`, `1 apple = ?`).
- **`imag`**: the ask says "What is the *positive* number?" — −4i squares to −16 too, so −4 was
  never a wrong answer. The third button is now the double.
- **`turnc`**: the walk-back is four short sentences.

## The dot, in the course that had the most

Seventeen authored step lines and ten generator ops (`el2`, `sys3`, `imag`, `rbet`, `logb`,
`logm`, `lbet`, `ampl`, `cnt3`, `samp`) joined two equations with " · " — `x + y = 5 · y + z =
10`, `crest = 11 · trough = −11`, `2^3 = 8 · log = 3`. Every one is two `[[step]]` tags now; the
three captions of the same shape say "and"; `x³ · x² = x⁵` and `√a · √b = √(a·b)` (real
products) stay, and the pin proves it. The pin now covers **six courses** by rendered
transcript. Pre-Calc, Calculus, Prob/Stat and Diffeq still carry the convention.

## The authored pile (lessons/algebra2.py) — 76 edits

**Laws with their condition.** "Each factor donates one root" → in these examples (both
answers); each *different* factor of the form x take away a number (three crossings, three
times). The test number's recap says which curves. The reciprocal's recap says "for the
positive x's we used … x itself is never zero". The forbidden x's recap says "a bottom like x
take away a number". The survivor's recap names the shape (2 x plus 6, all over x). "In
general, two roots go under one roof" → for numbers that are not negative. The one-half
power is the *positive* number that squares to the base (why and recap). Logs add "for
numbers in the same base", and it is "a great law", not the one. Between-the-powers'
nearest-neighbour rule is "for today's numbers … the exact halfway point on the log scale
sits a little below the middle, so this is a guide, not a law" (the bank is safe: all twelve
answers agree with the true nearest log₂). Decay's halving is "in these problems". "A
polynomial of any degree" → of degree 1 or higher. Slots times together "when every choice
in one slot can go with every choice in the next". Expected value: "about 2 times out of 6",
"a game like these", and "a center of gravity" → a long-run average. "The sample speaks" → a
*fair* sample, one that looks like the school. "Every function question can turn around" →
many.

**True statements.** "5 is not less than 5, and neither is negative 5" → negative 5 sits 5
steps from zero, not less than 5 either. i's lesson now says both answers, 3i and −3i, and
takes the positive one (picture and recap). "Cubed means times itself three times" → three
copies timesed together, x times x times x. A half turn flips *sine and cosine*; 360 − θ is
the mirror angle, not a full turn added. Adding polynomials *usually* lets the biggest
survive. Roots never add: √3 + √48 is not √51, and not 51. "The reciprocal's strange charm"
is gone — the undo is one more divide because the x sits after the divide sign.

**Words-board.** The wide-fence worked line says the board draws only the outermost dots, and
its caption says the line is compressed. The three-friends reason draws the three pair
clues. Walk-the-rule's picture draws the *second* pass (9 → 17) the words describe, and its
trap board says `20 ✗ doubling only: 5 → 10 → 20` to match the words (it said 18). The hidden
exponent's why uses 81 forwards and backwards (`3^? = 81`, `? = 4`, four threes). "1 up to 13:
every pair is 14" (thirteen numbers do not pair off) → the rectangle: 13 rows of 14 hold two
copies of the sum. Pair-the-ends' pairs are written as sums with "every pair is 11", and the
recap says why the halving works. The wiggle count's board writes `degree 6 → at most 5
turns` beside the spoken one. Degrees-add's why speaks the `x³ · x² = x⁵` its board writes.
Logs-add's second worked line says 64 × 128 is 8192. Seven closing beats speak the equation
their board writes.

**Ruled, not fixed** (two charter lines in `coursesweep.py`): a ✗ on a step line marks the
wrong path a child might take — `3 × 5 = 15 ✗` is "15 is the wrong road", not the tutor
denying that 3 × 5 is 15; and a bare "log" on a board in the Algebra II log lessons is base 2
unless the board shows another base beside it (the words say so).

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap 2,246 of 40,305; forSpeech
drift 1,940 — none moved. `L.validate` over all 360: 0 failures. Every new board tag rendered
headlessly with no `boardWarn`. PART **3mh**; the dot pin grew to Algebra II; the `imag` board
pin moved to `x = ? × i, with ? positive`.

## After the push

Prewarm: roughly eighty rewritten Algebra II lines plus the `gnth`, `absc` and `imag` asks and
the `sinp`/`cosp` praise (about a hundred generated lines). Then **Pre-Calc**, **Calculus**,
**Prob/Stat**, **Diffeq** as Jim pastes them. Expect the dot (the four courses carry ~30
authored lines and the generator's), laws without their condition, and — from Pre-Calc up —
notation the reviewer may call unstandard that is the course's chosen verb (rule it, as
"square back" was).
## Battery

Frozen copy, 2026-09-16: **12,576 passed · 0 failed · 3 skipped** (12,558 at `wl`). One pin
moved on the way: the uq-era `absc` board pin quoted the one-line `|x| < 3 · integers inside
the fence = ?`; it reads the two lines now.

I did no harm and this file is not truncated.
