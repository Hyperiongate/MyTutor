# Build vx — The Corrections Queue (2026-09-14)

Jim's 12 flags from the corrections queue (09-13/09-14): six on algebra1 "Two steps with a
letter" (00:35–00:42), six on prealgebra "Times before add" / "Parentheses first" (16:28–16:44).
Nine are closed here; three need a screenshot or a detail from Jim (listed at the end).

## What changed, flag by flag

**"Instead of saying 'X holds 4' we should be saying 'X is equal to 4'."**
Every variable line across `lessons/algebra1.py`, Prealgebra Unit 9, and the `lessonscripts.py`
generators (spoken, worked, and question lines) now says "x is equal to 4" / "with x equal to 4"
/ "What number is x equal to?". The two board captions that still read "x holds 4" now read
"x = 4". The old "is holding" / "holds" wording is gone from the spoken lane.

**"Need to pause after 'holding 3' — sounded like 'holding 3 five times 3'."**
The worked lines now break the value from the arithmetic: "with x equal to 5. Times first: …
Then the add: …" — a full stop after the value, so the voice breathes before the numbers start.
The battery then showed the real cause: the old line read "with x holding 3: 5 times 3", and
the page's speech tidier reads a digit-colon-digit ("3: 5") as a ratio, which is exactly the
run-together Jim heard. The two lines no longer carry anything to tidy (kx history pin
1,940 → 1,938).

**"'The plus cannot reach the x before the times has had it' is a poorly worded statement."**
Reworded: "The 2 is added after the three copies are counted, not to each copy."

**"This repeats the previous."** (teach beat replaying the picture)
Algebra1 teach[0] is now a method statement with its own board — `x = 4`, then
`3x + 2 = 3 × 4 + 2 = 12 + 2 = 14` — instead of a second run through the bar picture.

**"It could be confusing when the value of X and the value of the 'add' are the same."**
The bank was reworked so no problem has the variable's value equal to the added constant
(entries such as a=2,b=3,c=5 and a=3,b=4,c=7 — c is never equal to a).

**"Should show how we got 20 instead of just saying …" / "The example mentions $20 as the
wrong answer without showing how that wrong answer was arrived at."**
The "Times before add" why beat and teach[0] now walk the wrong path on the board: add first,
2 + 3 = 5, 5 × 4 = 20 ✗ — then the right path, 3 × 4 = 12, 2 + 12 = 14 ✓. The advance line
ends "On a line like these, the times goes first, then the plus." (My first draft said "Times
before add, every time" — and the battery's own canon sweep rejected it: rule 61, a
precedence rule spoken as a law with no grouping-symbol condition is false. The referee
caught its author. The line now says what is true of the problems in this lesson.)

**"Get rid of the cookies and candy thing unless you are going to show it graphically."**
The parentheses-first why beat drops the cookies/candy story; it teaches from the board line.

**"This is a reference to an earlier problem out of nowhere."**
Same beat — the stray back-reference went with the story.

## Beat caps

Two rewrites overshot the caps (why beat 83 words > 80; an explain option at 13 words) and
were trimmed. `L.validate` over all 360 lessons: 0 failures.

## Pins and tests

`ruletests.py` — the 3kt VALUE regex accepts `is equal to | equal to | equals` (and still the
old forms so nothing that quotes history breaks); the asks pins quote the new lines ("when x
is equal to 5?"); speechmap pin 2,244 of 40,294; closure unchanged at 40,242 (line text
changed, counts did not). Battery: 12,286 passed, 0 failed (frozen copy, 2026-09-14).

## Still owed to Jim

Three flags need something only he can give:

1. "This was not visible as it rested below the board without scrolling" (prealgebra) and
   "I had to scroll down to see what he was talking about" (algebra1) — a screenshot of the
   board at the moment, so the layout fix is to the right thing.
2. "This graphic is the right size but completely inconsistent with the size of graphics
   earlier in the session" / "The graphic is half the size it should be" — same screenshot
   (or two), to see which tape/balance widths differ.
3. "This does not answer my question" — what was asked.

## After the push

Run the prewarm once (`/admin` → Scripted course audio → Check what's missing → Render the
missing lines). It will list the rewritten lines from this build plus, if not yet rendered,
vw's 254 demo lines.

I did no harm and this file is not truncated.
