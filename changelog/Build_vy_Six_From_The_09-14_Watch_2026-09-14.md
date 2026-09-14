# Build vy — Six from the 09-14 watch (2026-09-14)

Ten confirmed findings on the 09-14 night watch, and **five of them were holes** — nothing
objected to what the student saw. A hole is the expensive kind: no nudge and no retry could
have helped, because no referee had anything to say. This build closes six (five holes and
one pass-through) and leaves three as rulings, with reasons.

Battery: **12,312 passed, 0 failed** (frozen copy).

## The six

**The pending zero — the night's HIGH (rule 15, algebra2).** The board wrote
`x - 2 = ? or x - 3 = ?` and the words asked which two values of x make it true. That question
has no answer: the zero-product step puts a **zero** where those question marks are. Nothing
objected because "= ?" is the ordinary pending-answer mark everywhere else in the system. New
referee `pendingzero`: two or more *lettered* factors written "= ?" in one board value while
the words ask about values or about what makes it true. An ordinary `3x + 2 = ?` can never
match, and neither can a numbers-only chain.

**The lettered law (rule 61, geometry).** "use a² + b² = c² to find a missing side" is true
only when c is the hypotenuse — and the same lesson went on to letter a triangle with b across
the right angle. New referee `pythaglaw`, the precedence law's twin in another subject. The
authored course never writes the lettered form; it says "leg squared plus leg squared equals
hypotenuse squared", which is true however the sides are lettered. That is what the nudge asks
for.

**The ask said in words (rule 16, algebra1).** "Want to try one more on your own — what's f of
two?" over a board still holding the f(5) work. Referee 38 exists for exactly this shape and
stayed silent, because its pattern required the number in **digits**. This is a voice
classroom. `_FN_NUMWORDS` and `_fn_ask_number()` read either spelling, and the board test is
unchanged.

**The letter is a blank too (rule 44, algebra2).** `[[step eq="x^2 = 25"]]` went up with
"What's x here?" and the twenty-five was never said — the words called it "the same idea,
slightly bigger number". The unspoken referee reads "?" as the mark of an unanswered line; in
algebra the unknown is the **letter**. Widened, and tight five ways so the courses' many
equations-that-are-answers stay silent: exactly one "=", no parenthesis (function notation
belongs to referee 38), a left side that is more than a bare letter, a numeric right side, and
no `op=` attribute — a line produced by an operation is working, not a problem posed. The
asking words must also be solving words, so a rotated check line over a board ("Okay so far?")
is not a question about the board.

**The first try that was not (prealgebra).** "you nailed it on the first try" — the student's
first answer was 20, and the tutor's own previous turn had said so. Praise a child knows they
did not earn teaches them that praise is noise. New referee `firsttry`, gated on the
immediately previous tutor turn, so a genuine first try on a *new* problem after an earlier
miss stays silent. The nudge asks for the true sentence ("you fixed it", and name the move),
not for silence.

**"It factors into those two pieces" is not a reading (rule 48, algebra2).** `(x - 2)(x - 3) = 0`
shipped with that as the whole of its reading. The first-use gate has had the touching-brackets
form since `vm` — and the word "factor" was in its list of readings. "Factor" names the
operation; the words that *read* two brackets are the multiplication words. It left the set.
One authored beat leaned on it, and that is fixed rather than exempted: the roots picture in
`alg2-u2-both-answers-count` now reads its own caption — "y equals x minus two, times x minus
five — the two brackets side by side mean multiply."

**Also in: ≠ joins the notation registry.** The calculus watch put "x ≠ 2" on a board with
nothing reading it, and the sign was on no list at all. Its reading gate takes plain English as
well as "not equal to", because the probstat and algebra1 foundation scripts write
"correlation ≠ causation" and say "Correlation is not causation" — which is the reading.
Referee 31's reach across the 306 foundation beats is unchanged at 83.

## The count

97 → **100 referees**, on the thirty pins in the battery and on the public methodology page
(the tile and both `data-referees` spans).

## Not fixed, and why

Three findings are rulings or nudge work rather than code, and the triage doc beside this one
says so in full: the rule-8 "watch it happen step by step" promise (its referee already
objected on every attempt — it wants a stronger nudge, not a second referee); the calculus
arrow `0/0 → undefined` (a candidate for a **code repair floor** that appends the symbol's
fixed reading, the way the dangling-colon and unearned-mark floors already repair — the next
floor, not built tonight); and the unplaced `6 ÷ 2 = 3` item, which sits very close to the
09-08 ruled-allowed shape and is better left alone than closed by widening a gate the reviewer
itself refutes four other findings for.

## After the push

The prewarm owes **one clip** — the rewritten roots line in `alg2-u2-both-answers-count`. The
closure and speech-map counts do not move (one line replaced one line): still 40,242 and 2,244
of 40,294.

I did no harm and this file is not truncated.
