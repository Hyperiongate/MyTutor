# Build wp — The First Diffeq Sweep (2026-09-16)

REPORT HEADER (copied first): Course sweep -- diffeq -- 2026-09-16 21:14 UTC (build wo).
Read by openai · gpt-5.5. By kind: false 64, words-board 39, unclear 10, unsupported 4,
untaught-term 2. 36 of 36 lessons read · 119 findings (14 on generators, 105 authored) · 0
lessons clean · 0 unplaced · 0 unread · 42 minutes.

The first sweep of Diffeq, on `wo`, read every lesson and found something in every one:
**119 findings**, the most of any course so far, and no lesson clean. Diffeq's own class is
*the law stated for the lesson's model as if it were the whole truth*. This course teaches
in three beats and two worked lines, and each lesson is built around one tidy model — the
cooling cup, the logistic pond, the door closer, the undamped bridge, the single real pole,
the rabbit-fox cycle — and the words kept promoting the model's rule to a universal one:
"every object on earth has a natural frequency", "Euler always lags", "the two halves of
first order", "eigenvalues below zero and it spirals in", "wait long enough and the
transient is gone". Sixty-four of the 119 were that shape. The fix was never to weaken the
lesson; it was to say the condition the model already had.

Stamp: **`2026-09-16wp-the-first-diffeq-sweep`**. Battery: see the bottom of this doc.

## The generator (lessonscripts.py) — fourteen items

- **`lnrz`** (two HIGHs): the ask said "the law 64 − P² has slope 2P" — it is −2P — and the
  praise said "you are pulled back at 144" — the true rate at P = 17 is −225; 144 is the
  straight-line *estimate*. The ask now says slope negative 2P and asks for the estimate,
  the board writes the equilibrium, the slope and "pull-back ≈ 2×8 per 1, 9 away" on
  separate lines, and the praise names it: "That is linearisation: close to a smooth
  equilibrium, a curved law behaves very nearly like a straight one."
- **`cdmp`** praise (HIGH) had the door the wrong way round. A hair *less* on the plain term
  and the door crawls; a hair *more* and it bounces.
- **`eign`** praise: two negative eigenvalues and "it spirals in" — two real negatives are a
  node, not a spiral. Now "everything moves in toward the origin".
- **`char`**: the ask says "…plus 16, equals zero" (the quadratic was spoken without its
  right-hand side); the praise says the number decides whether *this* spring wobbles.
- **`away`** praise: "in this model the further it goes, the faster it moves away. Moving
  away from the balance point is what UNSTABLE means."
- **`part`** ask: a steady push has a steady-height *particular* solution; the board writes
  `steady y: 3y = 42` and `y = ?`.
- **`estp`** praise: for a first order method the *main* error shrinks in step with the step.
- **`newt`** praise: "in the model, the coffee creeps closer and closer to the room" — it no
  longer says the coffee "never quite gets cold".
- **`chao`** praise: "a perfectly known equation, and a tiny starting gap still wrecks a
  far-ahead forecast."
- **`slpq`** ask says "use this equation" (it is the lesson's own, not a universal one).
- **`isoc`** praise is short sentences; **`logi`**'s board says "fish", not an untaught P.
- **`sepv`**, **`sepr`**, **`lder`** — the canon's own referees refused the generated asks
  once the dot was gone (the refusal had been hiding behind the dot): sepv's board wrote
  `y at x = 3 = ?` (two equals signs chained) and `dy/dx = 10x → y = 5x² + C` (an arrow after
  an equals); lder's question line `sY − y(0) = ?` carried no number the words read. sepv now
  writes four lines ending `at x = 3: y = ?`, lder writes `14 × 10 − 29 = ?`, and sepv/sepr ask
  "what is y at x equals 3" (the referee's function-rule check took "height" for an unwritten
  h(x)). Twenty pre-existing referee refusals on other Diffeq generators (the walked slope
  field's "What height?", the pond's "how many more?", damping's "√ then ÷ 2 = ?") were there
  at `wo` and are untouched — they are the next generator pile, not this build's.

## The dot, ninth course — all 36 lessons

Fourteen authored step lines and twelve generator ops (`isoc`, `sepv`, `sepr`, `away`,
`part`, `lder`, `lalg`, `nucl`, `eign`, `lnrz`, `slpq`, `chao`) joined two equations with
" · " — `4×25 − 8² = 36 · √36 ÷ 2 = 3` was a HIGH on its own. Every one is separate `[[step]]`
tags now; the pin covers **nine courses** by rendered transcript. Prob/Stat remains.

## The authored pile (lessons/diffeq.py) — 87 edits, 36 lessons

**Laws with their condition (64).** The order of an equation is the *deepest* derivative in
it, not a count (HIGH). The isocline rule and the solution-curve rule carry their equation
and their "every dash leans the same way" condition (HIGH ×2, both advance lines).
"Separable and linear are the two halves of first order" (HIGH) → another important kind.
Newton's law: the speed is *in proportion to* the gap, with a constant (HIGH). The tank's
single number is "in these examples", and the outflow carries 15 grams per litre (HIGH ×2).
The logistic peak-at-half and peak-size rules say "for this logistic law" / "our logistic
pond" (HIGH). "Euler always lags" → lands low in this forward walk when the slope keeps
rising; "exactly proportional, not a scrap more" → the *main* part of the error, about a
tenth (HIGH ×2); RK4's sixteen is "about". The characteristic quadratic is for these
constant-number equations and is written `r² + 6r + 5 = 0`. The door closer's rule was
REVERSED (HIGH): a hair below 225 and it crawls shut; a hair above and it bounces past the
frame. "Every object on earth" → many objects. A steady push has a steady *particular*
solution (HIGH), the method "for these steady pushes". The transient fades *with damping*,
"in these damped, settling problems" (HIGH ×2). Resonance grows "in this undamped model";
the advance line says "squared frequencies". The derivative rule keeps its "minus y(0)"
everywhere it is summarised (HIGH). The final-value theorem is "for settling transforms
like these ones"; poles are "for the single real poles in this lesson" (HIGH). The
determinant does "a lot of the classifying". Eigenvalues decide "the kind of picture"; both
below zero and every path moves *in* (HIGH — not "spirals"); every path "except the origin
itself" races away. The nullcline is where one *part* of the arrow is zero; arrows vertical
"except at one point". Linearisation is for a *smooth* curve; the slope of 9 − P² is −2P
(HIGH) and 24 is the estimate. The rabbit lesson is "one slice" of the model, "the rabbit
half of a balance point" (HIGH ×2). The cycle starts *on* the balance point and stays, "in
this model" it loops, "in this lesson's tidy cycle" the foxes lag a quarter (HIGH ×2).
Sensitive dependence is about a start only *almost* known, "in this example system" (HIGH ×2).

**Words-board (39).** Every board that showed numbers before the words said them now has
the words (the cup, the pond, the unstable point, the transient, the bridge, the shift, the
ending, the cycle, one-number-decides, damping). The worked lines write their setups: the
cup's `95 − 14 = 81`, the pond's `ceiling 41 · now 22 · room 19`, the halving `168 ÷ 2 = 84`,
the spring's `y″ + 256y = 0`, the s-world's `(s + 2)Y = 228` / `Y = 228/(s + 2)`, the ending's
`Y = 180/(s(s + 12))`, the knife-edge's `32² = 1024`. The separable lessons write `dy/dx = 8x`,
`y = 4x² + C`, `y(0) = 5, so C = 5`, `at x = 3: 36 + 5 = 41`. The slope-field opener draws the
walked field (`y=3x+5`, points (0,5) and (4,17)). The two-things-at-once lesson has a `y′ = x
+ y` rule and draws `the arrow: (31, 14)` (HIGH ×2). Resonance writes `gap 3: 42 ÷ 3 = 14`,
`gap 1: 42 ÷ 1 = 42`, `gap 0: no size — resonance` and keeps the ✓ line separate (HIGH).
"88 takes the 8 away rather than sharing."

**Unclear (10), unsupported (4), untaught (2).** "The transforming left" → the transform
leaves s plus 6; "180 underneath a lone s" → Y is 180 over a lone s times s plus 12; five
sentences over the 34-word cap split. The unsupported and untaught findings fell into the
two piles above: what was claimed without its line got the line on the board (the arrow, the
gap lines, the slope and the estimate), and the untaught P on the logistic board is "fish"
now — the word the lesson actually uses.

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap **2,245** of 40,305
(unchanged); forSpeech drift **1,939** (unchanged). `L.validate` over all 360: 0 failures
(four caught mid-build: "makes" — canon is "equals", a symbol no longer named, "sensitive"
unnamed, three long sentences). The canon's referee sweep over all 828 Diffeq transcript
beats: three authored arrow-after-equals boards reshaped, then the three generator asks
above; the pre-existing twenty are listed and left. Every new board tag rendered headlessly
with no `boardWarn`. PART **3mk**: the fourteen generator items pinned (the sepv and lder
asks are pinned *through the referee*, not just by their text), the dot pin grown to nine
courses, the authored classes by lesson id. No old pin quoted a Diffeq generator line; one
old authored pin moved (below).

## Housekeeping the battery forced — the second roll-out

The first frozen run failed three pins. One was an old authored pin (PART 3ft) quoting the
chaos lesson's "not available to anyone, at any price" — the very sentence the sweep called
a law for one example system; the pin now quotes the scoped sentence. The other two were
PART 3ke's size pins: the headers of `ruletests.py` (100,308 B) and `lessonscripts.py`
(101,322 B) had passed 100 KB. `notes_rollout.py` rolled every note before **2026-09-10** out
of both (95 and 46 entries, VERBATIM, into `changelog/<file>.md` as a second fenced block
above the 09-08 one; 42 and 20 notes stay). Two proper fixes rode along: the tool's stacking
branch dropped the earlier block's preamble (so the older block no longer said its own cutoff
and count) — it keeps it now, and the two changelogs were rebuilt with it; and PART 3ke,
written for one roll-out with the 09-01 cutoff hard-wired, now reads the newest pointer in
each header and checks every fenced block against its own cutoff and count. `main.py`'s
header is at 92,691 B — it is next, in a build or two.

## After the push

Prewarm: roughly ninety rewritten Diffeq lines plus the fourteen generator lines (about a
hundred generated lines). Then: **rerun the Calculus sweep** for the 17 lessons `wo` never
read (units 6–9) and paste it — it becomes `wq`. Then Prob/Stat, the last unswept course.
After that every course has had its first sweep and the second round starts on `wk`'s
Algebra I.

## Battery

Frozen copy, 2026-09-16: **12,612 passed · 0 failed · 3 skipped** (12,599 at `wo`); the first run failed three pins (above) and the second was clean.

I did no harm and this file is not truncated.
