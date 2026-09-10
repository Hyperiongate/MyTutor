# Build `uz` — A picture counts one kind of thing, 2026-09-10

Your four rulings on the 09-10 night watch, all of them closed.

**Battery 11,646 → 11,674 · 0 failed · 3 skipped**, twice, md5-identical.
**Stamp:** `2026-09-10uz-a-picture-counts-one-kind-of-thing`. On disk, unpushed, on top of `uy`.
**15 new voice lines, about $0.29** — see §4; the running total for the unpushed stack is
**227 lines, about $3.90**.

---

## ① The candy picture — referee 87

The story the tutor told was **true**: *"5 dollars, plus 3 candies at 2 dollars each"* — the
3 × 2 in it is three candies times two dollars, which comes to six **dollars**, and six
dollars joins five dollars perfectly well. Rule 32(c) already guards that much.

What it drew underneath was three groups of two **candies**. Six candies. A child looking at
that picture is looking at a model of a different problem, and the sum on the board cannot be
performed on the things in the picture.

The general rule — *a picture's units must match the story's* — is not decidable by any
pattern I can write. **The narrow one is, and it is the one you ruled on:** an `[[objects]]`
card counts **one kind of thing**. That is the whole of what it draws. So a story that gives
each item a **price** has two units in it and cannot be drawn with objects at all, however
the caption is worded. A bar can carry it — one part per item, each labelled with its price,
the whole bar the money — and so can the area model.

Referee 87 owns exactly that collision — a per-item price in the words, an objects card on
the board — and says nothing about any other picture. It knows the four shapes English
actually uses (*at $2 each*, *2 dollars apiece*, *each candy costs 2 dollars*, *sells for 3
dollars each*), and the nudge names the picture that **can** carry the story rather than just
refusing the one that can't.

**The sweep that licensed it: 11,021 authored beats and asks across all 360 lessons, 0
fires.** The scripted lane never draws a price story with objects — which is exactly why this
only ever showed up in the live lane. Rule 32(d) is its prompt twin, sitting with (b) and (c),
which already hold the story itself.

---

## ② The un-drawn alignment — rules, not a referee

Your ruling, and I think it's the right one. The tutor said *"Go ahead — line them up by the
last digit, like you said, and add it up"* over a board still showing the ordinary sideways
problem. **Letting a student's own method fail where they can see it is good teaching** — the
defect is only that the arrangement they were asked to add up existed nowhere but in their
head, so two students imagining it differently get two different answers and neither is wrong.

**Rule 15(f): invite their method, draw their method.** The night watch reports whether it
recurs. And PART 3kv pins that **the referee count moved by exactly one this build** — so
"rules, not a referee" stays a decision rather than something that quietly drifts.

---

## ③ The assessment goes quiet

`voiceclosure.py` (built yesterday for `uy`) is what finally said this out loud: two of the
lines `challenge.html` speaks were written in the page, so they were in no closure, so **every
assessment reached for `/api/speak` — the paid renderer — on demand**, for a line that could
never be cached. One of them interpolates the question number, so it could not be
pre-rendered even in principle.

Rule 18 has always said a quiz, a test or a timed challenge gets **no character at all**, and
the Course Assessment is a test. Gone: the audio element, the ElevenLabs ticket fetch, the
browser-voice fallback, the voice picker, the iPad audio unlock, and the `/api/voice-status`
call that existed only to choose between them. **Unchanged: every word a student reads.**

`say()` is `showLine()` now — a function named `say()` that says nothing is a lie in the code,
and it is the name the audit reads.

**Every page in `static/` now has zero page-local spoken lines outside the closure** — not
just the cache-only ones.

---

## ④ The 21 giveaway candidates, read

| | |
|---|---|
| **2 real, and closed** | `pre-u9-a-number-against-a-letter` and `alg1-u6-copies-of-copies`. Both closed by moving a **bank problem** — no authored sentence was rewritten. |
| **15 exhausted** | The ten doubles. Counting to ten. The four quarter turns in a circle. The whole times table. The twelve exponents under 216. In each, every possible demonstration is also an ask, because the demonstrations *are* the content. Same situation `uw` documented for `doubles`. |
| **3 honest** | The rule sentence in *minutes past the hour* (*"from one number to the next is five minutes"* — you cannot teach it without saying it); a number coincidence in *two machines*; and *the climb* reading its own picture's points. |
| **1 blind spot in the audit** | `pc-u2-the-minus-parade` opens *"Unit Two turns to polynomials"*, and the audit read a **2**. That lesson's first bank problem is (−1)². A sentence about the **syllabus** was being reported as a beat handing away an answer. |

`alg1-u6` was the one worth having: its very **first ask** was the problem its teach beat had
just worked (*two copies of three x's is 6*). A student watched the answer and was
immediately asked for it.

**21 → 18, and every one of the 18 has now been read.**

---

## The ceiling, and the cliff underneath it

Two of your rulings landed in the **shared** rule block, and Algebra II's all-heard prompt
came out **504 characters over** the 208,000 ceiling. The file's own law, written fourteen
times in its own ledger, is unambiguous:

> *"teaching is never trimmed to duck a tripwire; the raise is deliberate and this is its
> dated note."*

So: **208,000 → 209,000**, fifteenth verse, dated like the fourteen before it.

**But fifteen verses are telling us something, and I've written it down rather than let the
sixteenth be a reflex.** Before this raise Algebra II had **442 characters of headroom**, and
every course above Prealgebra sits behind the *same one-shot deferral*: drop the heard-script
wording, and if that isn't enough, ship over and shout about it. That is a cliff, not a
mechanism — the next universal rule anybody writes breaks the build again. **A second
deferral tier, or per-course rule blocks** (which is what `ux`'s plain-words block and `ox`'s
elementary buttons both chose instead), is the structural answer. That one's yours.

---

## What the battery caught me doing

The edit that took the voice out of `challenge.html` was written as a **character-offset cut**,
and it ran 400 characters past its target — swallowing `const ORDER = []`, the declaration the
entire assessment run walks. The page would have thrown on the first question.

The battery found it on the first run, by name: *"ORDER — never declared on this page"*. That
check exists because of a build in August that did the same class of thing. **Never cut by
offset: name both ends.**

It also caught a pin **reading its own documentation** — the "the assessment has no voice"
check searched the whole file for `ttsAudio` and `/api/speak` and found them, in the note that
explains they were removed. It strips comments first now. Same family as `ux`'s pin that
required the very declaration it was meant to guard.

---

## Files

`tutor.py` (referee 87 + the ceiling) · `prompts.py` (rules 15(f) and 32(d)) ·
`static/challenge.html` · `wordaudit.py` · `lessons/prealgebra.py` · `lessons/algebra1.py` ·
`ruletests.py` (PART 3kv + the count and two repointed pins) · `static/methodology.html`
(tile 87) · `main.py` (stamp).

## How it was checked

- **Battery 11,674 · 0 failed · 3 skipped, twice, md5-identical.**
- Referee 87 swept against **11,021 authored beats and asks**: 0 fires.
- **Five failability seams**, each restored, each failing **by name**: the referee losing the
  "each" shape, the assessment speaking again, `alg1-u6`'s first ask going back to the
  demonstrated one, the ceiling moving with no dated note, and rule 15(f) deleted.
- Every lesson in the course still validates; the two changed lessons presweep clean.

---

## Still open, for you

1. **The prompt-size cliff** — a second deferral tier, or per-course rule blocks. §above.
2. **`va` and `vb`** — Entry Units 5–7 (with the five missing walk-back pictures folded in)
   and 8–9. Starting `va` next.
3. **The 176** — after Entry 5–9, per your ruling.
4. **The stack is five builds deep and unpushed**, and needs a prewarm of about **$3.90**
   when it goes.

I did no harm and this file is not truncated.
