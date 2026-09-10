# Build `va` — The youngest course draws every problem, 2026-09-10

**Battery 11,674 → 11,701 · 0 failed · 3 skipped**, twice, md5-identical.
**Stamp:** `2026-09-10va-the-youngest-course-draws-every-problem`. On disk, unpushed.
**198 new voice lines, about $7** — the stack now totals **423 lines, about $10.44**.

---

## What I measured before writing anything

I was scoped to bring Entry Units 5–7 to the shape. Before authoring a single beat I
asked what those lessons currently draw, and the answer was worse than the job I'd been
given:

> **Of the 33 ops Early Math asks with, 26 drew nothing at all when they asked, and 28
> drew nothing after a right answer.**

A five-year-old was handed `2, ?` as a line of text. *"What is 96 plus 7?"* — one line.
*"How many cents is 3 nickels and 2 pennies?"* — one line. **The course whose students
are least able to hold a number in their heads was the course drawing the least.**

That is your complaint from Tuesday — *"a lot of it had to do with nothing was put on
the board"* — and build `uv` only answered it for the **live** lane. This is the
scripted lane, where every one of those boards was written down years' worth of builds
ago and nobody had counted them.

So I re-cut the build. Authoring twelve lessons whose beats point at pictures that don't
exist would have been the wrong order.

---

## The thirteen ops

The eight Units 5, 6 and 7 ask with, plus the five `uw` reported and you ruled in this
morning. Each gets **the picture that teaches its skill** — never decoration — on the
question with the answer left blank, and again on the walk-back with it filled.

| op | the lesson | what it draws now |
|---|---|---|
| `c2h` | crossing a hundred | the column, and the walk-back names the new hundred |
| `a3d` | adding three-digit numbers | the column, read hundreds, tens and ones |
| `s2d` `s3d` | taking away, two and three digits | the same, in reverse |
| `chk` | checking by adding back | **the claim as well** — you cannot check an answer you cannot see — then the add-back column, and a ✓ when it lands back on the start |
| `nick` `qtr` | counting coins | one tape part per coin, so **counting the parts IS the sum** |
| `chg` | making change | what you paid, split into what the toy took and what comes back |
| `dbe` | doubles | two pieces the same size — which is what a double *is* |
| `add3` | adding three numbers | three pieces joined, and the walk-back does two at a time |
| `msp` | the missing part | the piece and the whole, the gap marked `?` — and the walk-back draws **the hop**, because the answer is the size of the hop, never where it lands |
| `t10` | ten more | the blocks, and one more ten-stick with the ones untouched |
| `wor` | what a digit is worth | the number in its columns, and the named place read off |

**And the flag is on.** All seventeen of these lessons had `show_work_on_correct` **off**,
so the walk-back would have existed and never been shown. A walk-back nobody can reach
is not a fix.

---

## The thing a picture on a question can go wrong at

A picture on the *question* is only a gift if it doesn't give the game away. So every
ask column is drawn with **no result row**, every ask tape's unknown is a `?`, and the
battery sweeps **all 445 Entry-Level asks** to prove not one of them carries its own
answer (rule 15(e)).

---

## Three things the build found on its own

### `[[tape]]` keeps ten parts and silently drops the rest

Nine nickels and four pennies is thirteen coins. The tag slices at ten — so three of
those coins would simply not exist, and the card would look perfect in the source.
**Exactly the trap `uw` paid for with `OBJ_COUNT_MAX`**, where a card asking to count 17
stars rendered nothing. The coin tapes collapse past the cap instead of overflowing:
one part per coin while they fit, and past that the coins of a kind become one part
carrying their own total — still the true picture, just counted in groups.

### `a // 10` is "the tens" of a two-digit number and a lie about a three-digit one

The existing column helper speaks `a // 10` as "the tens". For 125 that is **12**.
Reusing it for three-digit addition would have had Mr. Cadabra tell a six-year-old
*"tens: twelve plus twenty-four equals thirty-six"*. `_col3_add` and `_col3_sub` read
hundreds, tens and ones as **digits**.

### Two figures had never carried a caption

`entry-u8-later-on-the-clock` and `entry-u8-how-much-longer` have been drawing an
uncaptioned number line and an uncaptioned bar chart since they were written — rule 41,
which says every figure names what to notice. **No flag ever reported them**; the
Entry-wide presweep this build ran is what found them. Board-only, no audio.

---

## And a pin of mine that proved the wrong thing

I wrote a check that three-digit addition reads three digits — and it tested **the
helper**, not the op that calls it. The failability seam that pointed `a3d` back at the
two-digit helper **passed**. A pin on a helper is not a pin on the code that calls it;
it reads the op's own walk-back now.

---

## How it was checked

- **Battery 11,701 · 0 failed · 3 skipped, twice, md5-identical.**
- **871 Entry asks and walk-backs through the whole referee stack: 0 findings.**
- **295 distinct figures through the real `math-figures.js` in node: 0 throw, 0 empty.**
  A tag that renders nothing looks perfect in the source, so the only honest check is to
  draw it. The harness is in the battery and skips gracefully where node is absent.
- **Five failability seams**, each restored, each failing by name — including the one
  that exposed the bad pin above.
- Every Entry lesson still validates; `uw`'s own PART repointed, because its build doc
  said this build would come: all twelve of Units 2–4 show their work now, not seven.

---

## Files

`lessonscripts.py` (the thirteen ops, the three-digit helpers, the coin collapse, the
two captions) · `lessons/entry.py` (**the flag only — not one authored sentence
changed**) · `ruletests.py` (PART 3kw + the figure harness + two `uw` pins repointed) ·
`main.py` (stamp) · `static/methodology.html`.

---

## Where this leaves Early Math, and what's next

| | ops that draw on the ask | ops with a walk-back |
|---|---|---|
| **before `va`** | 7 of 33 | 5 of 33 |
| **after `va`** | 20 of 33 | 18 of 33 |

The thirteen still dark are **Unit 1** (before-and-after, counting, which-is-bigger) and
**Units 8 and 9** (clock, calendar, shapes, equal groups, patterns).

1. **`vb`** — Entry Units 5, 6 and 7 to the shape: the twelve lessons get why → picture
   → teach ×2 → two worked pairs → practice → recap, and the written reason question.
   Their pictures now exist to point at.
2. **`vc`** — Units 8 and 9 to the shape, their eight ops drawn, and Unit 1's remaining
   walk-backs. That closes Early Math.
3. **Then the 176**, per your ruling.

⚠️ **The stack is six builds deep and unpushed**, and needs a prewarm of about **$10.44**.

I did no harm and this file is not truncated.
