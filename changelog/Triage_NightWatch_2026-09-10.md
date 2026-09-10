# Night watch triage — 2026-09-10 08:38 UTC
*(ran against `2026-09-09uw`, so `ux` and `uy` are not in it)*

**10 new confirmed · 2 known · 3 refuted · 0 referee crashes · 0 browser-voice fallbacks.**

I checked each finding against the code rather than taking the reviewer's word for it.
**Eight of the ten are closable, six of those without adding a referee at all** — the
mechanisms already exist and are missing rows or forms. Two are yours to rule on.

---

## The shape of the ten

Five of the ten are **one defect**: notation written on the board and never said. And the
reviewer *refuted* three more of the same shape by the 2026-09-08 ruling ("an equation
built entirely from symbols already introduced need not be read in full").

**The reviewer is being consistent, and the line it is drawing is the right one.** Every
confirmed one introduces a new notational **use** — `2(4)` (juxtaposition means times),
`(x−2)(x−3)` (a juxtaposed product), `?/3` (a question mark as a numerator). Every refuted
one re-uses a form already taught. So the gap is not in the ruling; it is that the
first-use gate knows **symbols** and not **forms**.

---

## Closable now, no new referee

| # | finding | mechanism that already exists | what it needs |
|---|---|---|---|
| **2** | *"anytime you see multiplication next to addition…"* with no parentheses condition (rule 61) | `overgeneralized_precedence_conflict` — the live precedence referee | **a widening.** I tested the exact sentence: it does **not** fire today. Its law pattern does not recognise "next to". |
| **10** | *"the square root of a number asks 'what positive number times itself gives this?'"* (rule 61) | the **known-false table** (`knownfalse`, 4 fires this week) — a table of named falsehoods, each with the condition that buys silence | **one row.** Tested: silent today. |
| **3** | *"we read f(x) … the name of a machine"* (rule 13) | same table, or the `funcrule` family | **one row.** Tested: silent today. The true sentence is dictated: *the function is named f; f(x) is its output at x.* |
| **4, 5, 8, 9** | four rule-44/48 findings — a new notational **form** written and never read | the first-use notation gate (`notation`, 30 fires) | **three forms**: juxtaposed multiplication `2(4)` / `(a)(b)`, a juxtaposed product of two brackets, and `?` standing as a term inside a written expression. |

None of these moves the referee count. The known-false table and the first-use list were
both built to be extended one row at a time, which is exactly what this asks for.

---

## Closable, but it is a new referee

| # | finding | why |
|---|---|---|
| **7** | the locked Final Exam was explained by naming **only Unit 4** while Unit 7 was also below mastery (rule 50) | This is **mechanically checkable and record-driven**: the referee sweep is already handed the record. A reply that explains a locked exam and names fewer than all the below-mastery units is a definite, decidable defect — and it is the kind that costs trust, because the student finds the second blocker on a later card. Referee 87. |

---

## Yours to rule on

| # | finding | the question |
|---|---|---|
| **1 (HIGH)** | the candy picture drew *3 groups of 2 candies* under a story where 3 × 2 was *3 candies at 2 dollars each* — 6 candies cannot be added to 5 dollars | The general rule ("a picture's units must match the story's") is not mechanically checkable. The **narrow** one is: *a price-per-item story must not be drawn with `[[objects]]` at all* — objects can only ever count one kind of thing; a price story needs a labelled array or a tape. That is checkable, and it is a real teaching rule. Do you want it as a rule, and enforced? |
| **6** | *"line them up by the last digit, like you said, and add it up"* — the wrong alignment was asked for but never drawn (rule 15) | Asking a student to compute from a setup that is **not on the board** is squarely rule 15, and `pendcheck` exists. But this is the deliberate *"let's see what your way gives"* move, which is good teaching — the defect is only that the wrong setup was not drawn. Widening rule 15's referee to cover "compute from a described-but-undrawn arrangement" risks firing on legitimate talk. My recommendation: **prompt, not referee** — rule 15 gains a clause saying that if you invite a student to try their own method, you draw their method first. |

---

## The telemetry line that matters more than any of the ten

> **replies shipped WITH a known finding: 176 ← should be zero**

The named offenders are `pass_through · livecritic: 123×` and `pass_through · prosecheck:
52×`. That is not a referee failing — it is `_settle` shipping the least-bad draft after
three attempts, which is the designed behaviour. But **176 in a week** means the model is
being asked to fix something it will not fix, 176 times, and a child sees the flawed reply
each time.

Worth a build of its own: take the top few `livecritic` reasons, read what the model
actually produced on attempt 3, and decide per-reason whether the nudge is wrong, the
rule is wrong, or code should repair it (the `elembuttons` / `quizmark` pattern, where
code fixes what the model would not).

## And one live floor, 5 minutes old at the time of the run

```
floor · mathcheck — the board line "5 1/4 - 2 3/4 = 2 1/2" is FALSE
```

The truth floor did its job — the child got the fallback line rather than a false one —
but a mixed-number subtraction going wrong on the board is worth a look on its own.

---

## What I would do next, in order

1. **The four rule-48 forms** — one gate, four of the ten findings, no referee count change.
2. **The three table rows** (precedence widening, square root, `f(x)`) — cheap, and each is a sentence a child would have believed.
3. **Referee 87, the blockers list** — small, decidable, and it is about trust.
4. **The 176.** The biggest number on the page, and the only one that is about the system rather than a sentence.

Findings **1** and **6** wait for your ruling.

I did no harm and this file is not truncated.
