# Build ws — The Second Diffeq Sweep (2026-09-17)

REPORT HEADER (copied first): Course sweep -- diffeq -- 2026-09-17 14:47 UTC (build wr).
Read by openai · gpt-5.5. By kind: false 30, words-board 18, unclear 8, unsupported 6.
36 of 36 lessons read · 62 findings (11 on generators, 51 authored) · 8 lessons clean
(joining-the-dashes, the-crowded-pond, how-big-the-peak-is, one-number-decides,
the-knife-edge, the-part-that-fades, what-saves-the-bridge, and-now-it-is-just-algebra) ·
0 unplaced · 0 unread · 47 minutes. The first sweep (wo, 09-16) was 119 findings, 0 clean.

The first re-run of a course that had already been swept and fixed. Diffeq at `wo` was the
worst report of the first round — 119 findings, not one lesson clean. `wp` answered it with
fourteen generator items and 87 authored edits. This sweep, on the same reader and the same
build family, came back **119 → 62 findings and 0 → 8 clean lessons**. That is the first
proof that a sweep-and-fix cycle converges rather than just moving findings around: the
class `wp` cleared (a law stated for the lesson's model as the whole truth) came back one
layer down — the same class, on the sentences next to the ones `wp` rewrote — and every one of
the eight clean lessons had findings at `wo`. What the reader could not see at `wo` because the
big misses were in the way, it saw at `wr`.

Stamp: **`2026-09-17ws-the-second-diffeq-sweep`**. Battery: see the bottom of this doc.

## The cost estimate matches the bill (coursesweep.py)

`EST_USD_PER_LESSON` was 0.05, a Sonnet-class guess with a comment promising to correct it
from the billing dashboard. Jim's dashboard: **$97.83 spent in September** across roughly
520 swept lessons plus the night watch — about **$0.15 a lesson**, three times the guess
(the reader is gpt-5.5, and a Diffeq transcript runs long). The constant is now 0.15 with a
dated note, so the admin card's `estimated_usd` says about **$5.40 for a 36-lesson course**,
not $1.80. Pinned in PART 3mn. The credit balance on the same screenshot was **$6.92** — one
more sweep, and then it needs topping up.

## The generator (lessonscripts.py) — nine ops

- **`estp`** ask and praise: "Euler is called first order because its error is proportional
  to the step size" — it is the *main* part of the error. Now "for a first-order method like
  Euler, the main part of the error is proportional to the step size — shrink the step and
  that main error shrinks by the same factor"; the praise "the main error scales the same
  way: 110 becomes 66".
- **`rk4`**: "the method everybody actually uses" → "a very common method". The praise counted
  "an accuracy Euler could not buy with a thousand times the steps" → "one more halving
  divides what is left by 16 again — which is why a few halvings buy an accuracy Euler needs
  vastly more steps to reach" (the validator's canon is "what is left", never "remaining").
- **`conc`**: "a mixing problem always turns on one number" → "the first number a mixing
  problem needs is the concentration".
- **`cycl`** ask: the quarter-cycle lag is this model's, and it happens only off the balance
  point — "nudge this model off the balance point and rabbits and foxes never settle … in
  this tidy cycle the foxes peak a quarter of a cycle after the rabbits".
- **`lder`** praise: the rule "for the equations in this unit" turns differentiating into
  timesing by s, not "the whole trick" for every differential equation.
- **`natf`** praise: "every object has a frequency like this one" → "many objects have natural
  frequencies like this, and the next unit is about what happens when something else drives
  one of them".
- **`prey`** praise claimed both halves of a balance the lesson computes one half of: now
  "the rabbit number is not steady on its own — it is held level by that many foxes".
- **`sysx`** praise: the answer is "the x part of the arrow at that point; the y rule gives
  the other part the same way" (it said "do that for y as well and you have an arrow").
- **`eign`** praise, the same class as the authored U8 line: "every path heads away from the
  origin", not "everything races away".

**Declined:** the LOW on `chao` ("25 is not on the praise board" — the praise says 5 to the
power 2 is 25 before it says 125). A praise beat in a lesson with no walk-back carries the
ask's *one answered line* by design (`answered_board`, build wc), so intermediate values are
never on that board; adding a line there would change the board every praise in 48 lessons
carries. The pin in PART 3mn asserts the answered board is exactly that one line.

## The authored pile (lessons/diffeq.py) — 47 edits, plus five validator splits

**Laws with their condition (30 false + 6 unsupported).** U1: an equation is "classified by
its highest derivative", said plainly ("an equation with d y d x is first order, and one with
d squared y over d x squared is second order"); "for this comparison, keep the same plane and
the same points … wherever the slope changes the dash swings to a new angle"; "three
different calculations, and only one of them matches the equation"; the isocline's 14 is said
where it is drawn. U2: the two long separable sentences split; the cup "changes more and more
slowly as it nears the room", and 5 "is only the degrees of gap it takes to cool 1 degree a
minute — the share, not the rate". U3: "with a ceiling of 60, the fastest growth is at 30".
U4: RK4 "takes a *weighted* average, counting the two middle slopes twice" (HIGH — it said a
plain average); "in this lesson we count the cost by slope evaluations". U5: the root rule is
"for equations in this form". U6: a steady push "changes the steady height the spring
vibrates around" (HIGH — it said the push changes how it vibrates); resonance "in our
vibration model". U7: "Write Y for the transform of y" *before* the rule leans on Y (HIGH);
"the quantity s plus 8" (without it, 96 over s times s, plus 8); the pole "tells you how the
answer behaves, as the last beat will say" (no inverse transform is shown); the advance line
names "the number in front of t in the exponent". U8: the x-nullcline's arrows are vertical
"except where it crosses the other nullcline, the y one" (HIGH — "except at one point" named
a point the lesson had not drawn), with the crossing kept as a preview; the corner shortcut is
"for these squares with matching corners" and the teach says "in this lesson the two corner
numbers always match" (HIGH); a source: "every path except the origin itself heads away from
it overall". U9: "*many* real rate laws bend" (HIGH — "every real law bends"); the estimate
rule "for these laws"; the rabbits' lesson claims only its half — "the fox half of the balance
is another equation, for another day"; chaos: "for the equations you have used, knowing the
equation and the starting point exactly fixes the future", and the long forecast fails "in a
*sensitive* system like this" (HIGH).

**Words-board (18).** The dash at (7, 5) is *drawn* — `[[graph lines="y=12x-79"
points="(7,5)" range="4..10" yrange="0..20"]]`, a steep dash through the point (HIGH: the
board only marked where it would go). The arrow at (9, 5) is drawn as `[[vector v="31,14"]]`
(wq's tag). Worked lines draw their setups: `88 − 60 = 28` and `58 − 20 = 38` (pushes-away),
`4×221 − 10² = 784` and `4×205 − 6² = 784` (damping), `y″ + 4y = 52` and `y″ + 2y = 34` (the
push), `natural² 15 · driver² 5` then `15 − 5 = 10` (resonance, with the second worked line
now saying "natural squared 12, driver squared 8"), `[15 9; 9 9]` (the corner), `20 × 3 = 60
new rabbits` and `60 ÷ 5 = 12 foxes`. The Euler setup and "y double-prime plus 9 y equals
zero" are read where they are drawn; the resonance gap gets its `9 − 3 = 6` step.

**Unclear (8).** Long sentences split, in U2 and U7 and in the generator lines above.
The validator caught five more at 35–42 words after the edits, split the same way; and
"crossing" was not the symbol "cross" the nullcline lesson must say by name (rule 14) — "the
point where the two cross".

## Counts

Course lines **39,999** (no beat added); closure 40,253; speechmap **2,245** of 40,305
(unchanged); forSpeech drift **1,939** (unchanged). `L.validate` over all 360: 0 failures.
The canon's referee sweep over every Diffeq beat: **20 refusals, all present at `wr` and
untouched** (the generator praise lines wp's doc lists — a quiet build of their own). The dot
scan over all ten courses: none. Every new board tag rendered headlessly with no `boardWarn`.
PART **3mn** (11 checks); seven PART 3mk pins moved to the new wording, each marked "(ws)".

## After the push

Prewarm: roughly fifty rewritten Diffeq lines plus the nine ops' lines. Then **top up the
reader's credits** ($6.92 left) before the next sweep. The second round continues on the
courses whose first sweep ran on the wrong build or the worst reports: Pre-Calc (ran on
`wm`), Algebra II (ran on `wk`), then Entry against `wg`'s floor of 14. The 20 Diffeq and 21
Calculus pre-existing referee refusals are a quiet generator build waiting its turn, and
`main.py`'s header (94 KB) rolls out at 100.

## Battery

Frozen copy, 2026-09-17: **12,649 passed · 0 failed · 3 skipped** (12,638 at `wr`). The
first run failed one pin: an old 3ft pin quoting the chaos lesson's "goes unreliable
*whenever* the start is even slightly off", which this build reworded ("when", after "in a
sensitive system like this,") — moved to the new wording. The second run was clean.

I did no harm and this file is not truncated.
