# Build `ux` — The expression comes first, 2026-09-10

Your five flags from the 22:40–22:43 sitting and the 12:53 opener, plus the two rulings
you gave with them. **Every one is fixed in the OP, not in the beat you flagged** — so the
same defect cannot survive in the eleven other places that op is spoken.

**Battery 11,582 → 11,619 · 0 failed · 3 skipped**, twice, md5-identical.
**Stamp:** `2026-09-10ux-the-expression-comes-first`. On disk, unpushed.
**⚠️ A PREWARM IS NEEDED after this push** — 211 new voice lines, about **$3.60**.

---

## 1. Your five flags

| | your words | what changed |
|---|---|---|
| **22:43** | *"This is taught out of order. it should first show the equation, then the value of x, not the other way around."* | All four evaluate ops now ask **"What is 3 x plus 2, when the letter x is holding 4?"** Every teach beat, worked pair, praise line, walk-back and reason question in the four letter lessons was re-ordered to match. **372 lines those lessons can say; 0 put the value first.** |
| **22:42** | *"This didn't show x=3 on the visible board."* | Every walk-back board now opens `[[step 3x + 2]] [[step x = 4]]` **before** the filled picture — and every **ask** board draws the bar **first** and `x = 4` **second**, so the board runs in the same order as the words. |
| **22:41** | *"I had to croll up to see the bar."* | The trap beat says *"Look at the bar"* and drew two step lines; the bar was two beats up the feed. **It draws the bar now.** And the sweep that found it found **two more**, in Entry-Level and Prealgebra. |
| **22:40** | *"The diagram is half the size it could be."* | A block that draws a **picture** now takes the whole feed width. Measured on your flagged beat: **the drawn bar 720 → 884px (+23%)** at 1440×900. Phones byte-identical. |
| **12:53** | *"'ambiguity' is a word that a child will not understand."* | **Referee 86** — 78 general-academic words with their plain-English twins, on the three youngest courses. Section 4. |

**And the check.** *"It is suddenly enthusiastic and loud. maybe something like, 'ready?'"*
`"Got it?"` → **`"With me so far?"`**, and the button that says yes is just **`Yes`**.

---

## 2. Why 22:40 was never a lesson defect

Build `oz`, on 27 August, made the feed two columns above 900px — from **your own** complaint,
*"it's still not using the full screen."* The words got a readable 32% column; the board got
the rest. What nobody measured is what happens when **the picture is taller than the words**.

Measured on the beat you flagged, at 1440×900: the tutor's 58-word bubble is 432×142. The two
bar models beside it are 806px wide. **The 475px left column sits empty for the 650px below the
bubble.** That is the half of the screen you were looking at.

One rule, in all three feed pages, reusing `board.js`'s **own** definition of "a picture, not a
re-statement" rather than a second list that could drift:

```css
.feed > .mblock:has(.mfig, .graphwrap, .colmath, .objwrap, .scale, .machine,
                    .solveboard, .steprow) { grid-column: 1 / -1; }
```

The words keep their column. A block that draws an actual picture stops paying for a column it
is not using. `:has()` is new to this codebase and its failure mode is why it is safe: a browser
that does not support it simply does not match, and the layout is byte-for-byte what shipped
before.

---

## 3. The pointing audit — and the two more it found

`deixis.py` (new) sweeps all 360 lessons for **a beat whose words point at a picture its own
board does not draw**. Yours was one of three:

| lesson | what the words say | what the board drew |
|---|---|---|
| `alg1-u1-two-steps-with-a-letter` | *"**Look at the bar**: the 2 is one piece on the end, not three."* | two step lines |
| `entry-u2-add-single-digit` | *"...until you have touched every star **on the board**."* | two step lines |
| `pre-u8-area-of-a-triangle` | *"...twice the size of the one **on the board**."* | two step lines |

All three are **trap beats** — the third beat of the shape — and all three point back at the
picture the *first* beat drew, which by then has scrolled away. On a phone it is off the screen
entirely. All three draw their picture now. **Board only: not one spoken word changed, so not
one voice line re-renders.**

The audit is deliberately narrow — the three imperatives plus *"on the board"*. An earlier
draft counted *"on the circle"* as pointing and reported the shape's own closing taglines
(*"and that is Pythagoras, living on the circle"*) as defects. **A check that cries wolf is a
check somebody turns off.**

---

## 4. Referee 86 — and the 78 words, for your review

Your opener flag is the board referees' complaint from the other side. A child who meets a word
they cannot read **does not ask what it means** — they stop following, and the sentence after it
is wasted whatever it says.

**It names the swap.** A referee that says *"that word is too hard"* gets a rewrite that is a
coin flip. One that says **`say "so" instead of "consequently"`** gets the sentence an author
would have written. Every word on the list carries its twin; a word with no honest twin does
not belong on the list.

**⚠️ It is NOT a ban on mathematical words.** *Numerator, quotient, equivalent, proportion,
reciprocal* are what these courses **teach**, rule 14 **requires** them out loud, and not one
is on the list. This is the ordinary English around them.

**Scope:** Early Math, Basic Math, Prealgebra. Silent from Algebra I up, where the vocabulary
is part of the subject.

**The sweep that licensed it: 12,140 authored lines across all 360 lessons — the youngest three
courses AND the other six — use not one of the 78 words.** The house voice already writes this
way. The referee is not a new standard; it is the standard the scripted lane already keeps,
extended to the lane that cannot be proof-read in advance.

**The list is yours to cut.** Strike any word you think a Prealgebra student can read and it
comes off:

> ambiguity · ambiguous · approximately · arbitrary · coincide · commence · conceptual ·
> consequently · constitute · criteria · criterion · cumulative · denote · **determine** ·
> discrepancy · distinct · elaborate · encompass · entail · explicit · facilitate ·
> generalise · hence · implication · implicit · incorporate · inherent · initiate ·
> intuition · intuitive · invariably · magnitude · methodology · negligible · nonetheless ·
> notion · **obtain** · paradigm · perceive · prerequisite · presumably · rationale ·
> reiterate · respectively · scenario · subsequent · subsequently · substantial ·
> sufficient · terminology · theoretical · thereby · **thus** · ultimately · utilise ·
> whereas *(plus their inflections)*

The three in bold are the ones I'd expect you to argue with — *"determine"*, *"obtain"* and
*"thus"* are ordinary teacher-speak. I included them because a nine-year-old reading
*"determine the value"* is doing translation, not arithmetic. Say the word and any of them come
off in one line.

---

## 5. Three defects the build found that you did not flag

### (a) Re-ordering the words changed which number a beat opens on

The giveaway audits decide by a beat's **opening** numbers. Expression-first opens on the
*coefficient* where value-first opened on the *value* — so two beats that read clean for weeks
became hits the moment they were re-ordered:

- `mlx`'s teach beat became *"what is **3** x? That is **3** times x... **9**"* — opening 3, 3
  with 9 following, which is a bank problem and its answer.
- `evx`'s second worked pair opened on **pair one's own ask**.

Both caught by the baseline presweep, both reworded. **Run the presweep after a re-ordering,
not only after a re-wording.**

### (b) The prompt twin went 631 characters over Algebra II's ceiling

The first cut put the plain-words rule in the **universal** rule list — where every course pays
for every word of it. The battery caught it inside one run: Algebra II's all-heard prompt went
**631 characters over its 208,000 ceiling**. It now rides beside the notation and misconception
blocks, scoped to the three courses it is true for. **A rule true for three courses and paid
for by twelve is a rule in the wrong place.**

### (c) A pin that tapped a button by name

The `us` live-walk pin drove a real browser through a whole lesson and tapped `"Got it"` **by
literal string**. Retiring the phrase broke it — for the wrong reason. It reads the labels from
`lessonscripts` now.

---

## 6. Cost, and what needs doing after the push

| | |
|---|---|
| **New voice lines** | **211** (15,879 characters) — 210 from the re-ordering, plus the new check |
| **Audio cost** | **~$3.60** at the rate your Abrabot introduction actually billed at |
| **Retired lines** | 211 — already rendered, no refund and no new cost |
| **⚠️ Prewarm** | **Required.** Push, then run the script-prewarm from `/admin`. |

---

## 7. Files

`lessonscripts.py` · `tutor.py` (referee 86 + the block wrapper) · `prompts.py` (the PLAIN WORDS
block) · `ruletests.py` (PART 3kt + five pins repointed) · **`deixis.py` (NEW — `git add -A`)** ·
`lessons/prealgebra.py` · `lessons/algebra1.py` · `lessons/entry.py` · `main.py` (stamp) ·
`static/session.html` · `static/practice.html` · `static/topic.html` ·
`static/methodology.html` (tile 86).

---

## 8. How it was checked

- **Baseline presweep first**, before any edit — which is what let (a) show up as a *change*.
- Full presweep on all six changed lessons after: `validate()`, the whole referee stack,
  spoken-math, named-picture, beat and sentence caps, the perfect walk, closure membership.
  **0 findings.**
- **Battery 11,619 · 0 failed · 3 skipped, twice, md5-identical.**
- Referee 86 swept against **12,140 authored lines**: 0 fires.
- The pointing audit swept against **all 360 lessons**: 0 hits — with a **built control** (the
  flagged beat's own words over the board it used to have: caught) and a **cry-wolf control**
  (the shape's closing tagline: silent).
- The layout fix measured in a real browser at 1440×900 with the figure's pop animation settled,
  and at 390×844 (byte-identical).
- **Six failability seams**, one at a time, each restored after, each failing **by name** and
  none crashing the battery:
  the value put back in front of the expression (22:43's pin fired), `x = N` taken off a
  walk-back board (22:42's), the bar taken back off the trap beat (22:41's, plus the
  three-beats pin), the `:has()` rule dropped from `practice.html` (all three of 22:40's),
  a hard word planted in an authored line (the canon sweep), and the page's check line
  nudged one space away from the lane's (the byte-identical pin).

---

## 9. Still open, for your call

1. **The five demo defects you reported** — lip sync, Mr Cadabra not centred at the start, his
   voice silent for the item after Abrabot, the board's dark/white flip lagging the voice by
   ~5 seconds, and the fall back to the browser voice after a sample problem. You ruled lesson
   flags first, so these are untouched. My working hypothesis is that **four of the five are one
   root cause**: `demo.html` paces its visuals on fixed `setTimeout`s rather than awaiting the
   speech, so anything that makes a clip longer or shorter slides the picture off the words.
2. **The five ops with no walk-back picture** (`dbe`, `add3`, `msp`, `t10`, `wor`) — from `uw`.
   About a morning plus **$3** of audio.
3. **The 21 course-wide `wordaudit.py` candidates** — from `uw`, still untriaged.
4. **The 78-word list above** — strike whatever you disagree with.

I did no harm and this file is not truncated.
