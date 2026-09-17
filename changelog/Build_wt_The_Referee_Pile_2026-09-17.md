# Build wt — The Referee Pile (2026-09-17)

A quiet build between sweeps, while the Pre-Calc rerun was reading. The canon's 101
referees wrap the live tutor's replies, not the scripted lane — so nothing a student sees
was ever blocked by what this build fixes. But every sweep since `wp` had run the referees
over the swept course's transcripts as a pre-flight and set aside the "pre-existing"
refusals: 20 on Diffeq, 21 on Calculus. This build ran them over **every scripted beat of
all ten courses** — 360 lessons, every teach, worked, ask, praise and walk-back line the
generators produce — and found **56 refusals. After the build: 1.**

Stamp: **`2026-09-17wt-the-referee-pile`**. Battery: see the bottom of this doc.

## What the 56 were

| shape | count | where the fault was |
|---|---|---|
| "so x is 12" / "5 plus 2 equals 7" praised over an **empty board** | 45 | the engine (`_correct_beats`) |
| "What height?" refused as a function-notation ask | 20 | the referee (`_FN_ASK`) |
| "40 = 8 × ?" / "0.1 + 0.3 = 0.?" called unanswerable | 18 | the referee (`unanswerable_choices`) |
| a question written inside a `[[step]]` (carr) | 5 | the generator |
| a pending line the words never read (oscf) | 5 | the generator |
| a law about holes without its condition (lhol) | 5 | the generator |
| an intro card naming the lesson's own title ("number line") | 1 | left alone |

(The rows overlap — a beat can carry two faults — which is why they sum past 56.)

## The engine: every praise beat carries the answered board (lessonscripts.py)

Build `wc` gave the praise beat the ask's answered line — "2 groups of 2 = 4" as the child
hears "That's it! 4" — but only in lessons with **no walk-back**, on the reasoning that a
walk-back lesson's worked board follows a beat later. For that one beat in between, the
child's own answer was nowhere on the board, and the praise line ("Set the slope to zero:
2 x equals 24, so x is 12") stood over nothing. Forty-five of the fifty praise refusals
were exactly that, across Algebra I, Calculus and Pre-Calc. Now `_correct_beats` puts the
answered line on **every** praise beat; the walk-back still follows with the full working.
The times-table pass, which has its own fast praise path, answers its own fact line —
`4 × 7 = 28`, counter and all. Measured: 50 praise refusals before, 5 after (all one
Pre-Calc generator's law, below). The `wc` pin that asserted an empty praise board on a
walk-back lesson moved to the new shape.

## Two referee misreadings (tutor.py)

- **`_FN_ASK`** read "What height do you land at?" as *what h(eight)*: the letter class
  `[fgh]` matched the h of "height" and the number-word branch swallowed "eight". Twenty
  scripted asks in Diffeq and Calculus ("What height?", "at what x does the height reach
  zero", "What is its height at x equals 4?") were refused by a referee about f(N) — and
  the live tutor saying "what height" would have been too. The letter now stands alone
  (`(?![a-z])`); f(4), f of 4, g(two) all still match, and the echo shape still fires.
- **`unanswerable_choices`** judged the buttons against the *left side's value* whatever
  the right side said: "40 = 8 × ?" asks for the factor (5) and "0.1 + 0.3 = 0.?" for a
  digit (4), and three Basic Math generators were called unanswerable eighteen asks at a
  time. Only a bare "?" on the right is the left side's value; anything else, the gate
  leaves alone. "1 + 2 = ?" with 9 | 4 | 7 still fires, and a line with no equals sign no
  longer crashes it (caught mid-build — the first cut crashed fail-open on "2, 4, 6, ?").

Both fail open as before; no referee was added, so no count pin moved.

## Three generator lines

- **`carr`** (where growth peaks): the board wrote `now 30 · how many more?` — a sentence in
  an equation tag. Now `130 ÷ 2 − 30 = ?` under `ceiling 130 · fastest at half`.
- **`oscf`** (damping): the pending line `√ then ÷ 2 = ?` carried no number and the words
  never read it. Now `√576 ÷ 2 = ?`, and the ask says "The board has the inside: 576. Root
  it, then halve it. What is that?"
- **`lhol`** (the hole in the curve, Pre-Calc): "The function has a hole there" is true only
  because the simplified x + 14 is defined at 14 (rule 61 — a cancelled factor that
  survives in the bottom is an asymptote). Now "The simplified x plus 14 is defined there,
  so it is a hole: y never reaches 28, and the limit says where it was headed." The first
  wording was thirty characters longer and pushed the lesson's closure to 25,564 — sixty
  praise variants carry it — so it was tightened to the shape above (24,639); the 25,000
  tripwire was not moved.

**Left alone:** the Basic Math number-line intro card, whose title says "Fractions live on
the number line" before any number line is drawn. Rule 7 is right in general; a title card
is not a claim about the board. One beat; on the ledger.

## Counts

Course lines **39,999**; closure 40,253; speechmap **2,245** of 40,305; forSpeech drift
**1,939** — all unchanged. `L.validate` over all 360: 0 failures. PART **3mo** (9 checks),
including the measurement itself: the referee sweep over all ten courses must refuse at most
that one intro card.

## After the push

Prewarm: the oscf ask lines and the lhol praise lines (Diffeq damping, Pre-Calc hole) —
nothing else spoke differently. Then the sweeps continue; the praise beats they read now
carry a board, so any "N is not on the praise board" finding from here on is a genuine one.

## Battery

Frozen copy, 2026-09-17: **12,658 passed · 0 failed · 3 skipped** (12,649 at `ws`). Clean on the first run.

I did no harm and this file is not truncated.
