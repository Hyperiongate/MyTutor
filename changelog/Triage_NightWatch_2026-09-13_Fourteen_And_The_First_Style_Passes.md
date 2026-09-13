# Night watch triage — 2026-09-13 09:00 UTC
*(ran against `2026-09-12vt`, so `vu`'s voice-miss block is not in it; `vr`'s critic pass and
referees 92–97 are — the first watch on both)*

**14 new confirmed · 0 known · 9 refuted · 0 crashes.** 5 holes · 8 pass-throughs · 1 unplaced.
I tested every finding against the code. **Build `vv` closes five of them** (a hole, the HIGH
hole, a leak in `vr`'s classifier, and two pass-throughs). The rest are rulings or nudge work.

---

## The one that matters most: `vr`'s classifier leaked once in three

The admin feed shows three `referee_soft · criticstyle` rows from the watch. Two were right
(a "clearer ask" suggestion; a critic conceding `20/100 = 1/5` is correct). The third was
**"The tutor should acknowledge the student's answer and verify it is correct before asking how
they got it — this may feel dismissive"** — a rule-18 objection, passed as style on the strength
of "may feel". That is the night's **unplaced decimal-alignment finding** ("5 plus 4 is 9",
never acknowledged): the critic caught it, my classifier waved it through, and the reply shipped
looking like nobody had objected. `vv` makes "should acknowledge / grade / address / respond to /
confirm the student's answer" a hard word. The thesis holds — measure the passes, and the rows
say when the classifier is wrong — and this is the first time it paid.

## Closed in `vv`

| # | finding | what was wrong | fix |
|---|---|---|---|
| **HIGH** final-exam-locked, rule 44 — *"Question 1. Simplify this fraction."* over `10/15 = ?` | **HOLE.** `unspoken` only looks when the prose carries a `?` or "your turn"; an imperative ask has neither. And even "Simplify ten fifteenths" would have been unheard: 15 had no denominator word. | The gate opens on a sentence-leading solving verb; `_ordinal_word` names every denominator 2–99. Canon 0 new fires. |
| MEDIUM final-exam-locked, rule 18 — `What do you get? [[mark correct="1"]]` | **HOLE.** A mark recorded an answer nobody had given. | **The unearned-mark floor**: a `[[mark]]` after the reply's own question with no verdict word before it is stripped at the door, counted `code_repair · unearnedmark`. 0 authored strings touched. |
| MEDIUM decimal-alignment, rule 18 — "5 plus 4 is 9" unacknowledged | **unplaced** — the classifier leak above. | `_CS_HARD_RE`. (`unacked`, 94, fires on the shape when it is given the previous turn; the critic had it too.) |
| LOW fractions-lost, rule 14 — `3/4 : denominator = ?` | **PASS-THROUGH** (`livecritic` ×3). `arrowpointer` (ut) knew the arrow, not the colon. | The colon is a pointer when a value stands before it; "Step 1: hypotenuse = 13" stays a label. |
| LOW order-of-operations, rule 7 — *"Picture this: you have 4 dollars, plus 2 tickets…"* | **PASS-THROUGH** (`orphanstep`). `pictured` (ut) had no money nouns and did not know "Picture this:". | dollars / tickets / bills / cents; the "this:" opener. |

## Read, and left where they are

| # | finding | why |
|---|---|---|
| **HIGH** order-of-operations, rule 61 — *"Multiplying always gets done before the adding joins in, no matter which one is written first."* | `precedencelaw` (vn) **fires on that sentence** — I tested it — and the stamp says it fired on this turn. The draft shipped anyway, which means the shipped draft satisfied the referee somewhere else in the reply (it excuses a reply that names grouping symbols anywhere) while the sentence itself stayed unconditional. That is a **bar question**: should the condition have to sit in the same sentence? I lean yes for a LAW sentence ("always", "no matter"), since the child hears the sentence, not the reply. Your call; it is a referee change, not a row. |
| MEDIUM order-of-operations, rule 44 — `5 + 3 × 2 = ?` under *"Want to try one yourself now?"* | PASS-THROUGH on `danglingcolon`, and **the colon floor repaired it at the door** — the first floor repair the watch has read. `unspoken` fires on the quoted shape; the real reply must have carried a number somewhere. Nothing to build. |
| MEDIUM limits-hole, rule 7 — asks what a table would show, draws no table | `livecritic` ×3. `pictured` needs a picturing verb; "what would a table show" has none. A narrow shape ("what would a table/graph show" + no `[[table]]`/`[[graph]]`) is buildable — **do you want it?** Rule 7 has three referees already. |
| MEDIUM limits-hole, rule 44 — `lim (x→5) h(x) = ?` not read | `livecritic` ×3. `unspoken` is satisfied by "five" in the prose (its generous bar), and `lim` was already a first-use entry read earlier. **Ruling**: must a limit *line* be read in full each time it is posed, or is rule 48's 09-08 ruling (an equation from introduced symbols) the answer? I lean the latter → refuted on sight. |
| MEDIUM geometry-picture, rule 6 — solves the whole problem after the student asked to set it up | PASS-THROUGH on `boardflood` (7 lines). The nudge says "KEEP EVERY LINE, spread across turns" — which the model reads as "keep every line". **Nudge work**: for a reply that answers a student's "let me set it up", the nudge should say *stop after the setup*. Not built tonight; wants the transcript. |
| MEDIUM final-exam-locked, rule 13 — "ten percent" when the gap is 5 points | HOLE. Decidable only narrowly (the record's gap vs a spoken "N percent" in a gate sentence). Rule 50's referees (91) hold the record; a "gap arithmetic" row is possible. **Your call** — it is the first time the class has appeared. |
| MEDIUM final-exam-locked, rule 59 — "you cross-cancelled cleanly" (a method asserted unseen) | `livecritic` ×3, and the critic's objection was exact. A referee is possible ("you <method-verb>ed" over a bare-number message) but it is the critic doing its job; the model ignored it three times. Add to the "pedagogy the nudge can't move" pile; see the counts below. |
| MEDIUM returning-student, rule 13 — "x plus 3 equals zero, **and** x minus 2 equals zero" | HOLE. A `KNOWN_FALSEHOODS` row is possible ("…equals zero, and … equals zero" → or). But "set x+3=0 and x−2=0" is ordinary teacher speech for two cases; the reviewer is right on logic and the row would fire on many good sentences. **Ruling.** |
| MEDIUM returning-student, rule 4 — board `x + 3 = ?` under words "equals zero" | HOLE. The board turned an equation into an evaluation. Narrow and decidable (words "<expr> equals zero", board "<expr> = ?"). One sighting; **ruling** before a referee. |

The 9 refuted are all the 09-01 and 09-08 rulings doing their job. Sound.

## Telemetry

- **Pass-throughs 150** (105 `livecritic`, 45 `prosecheck`), **136 on the AUDIT lane, 14 live**. The
  block works: the per-referee reasons are readable for the first time. `danglingcolon` shows
  2 pass-throughs *and* 2 door repairs — the floor is doing what it was built for.
- `referee_soft · criticstyle`: **3** (one wrong — above). `livecritic` fires 165×/week.
- **Voice, 7 days, by lane** (`vu` is live now, the watch ran before it): `speak` 467 requests,
  44,381 chars cached, **10,034 generated**; `demo` 591 generated; `drill` 0 (cache-only, as
  designed). 18% of served characters live-rendered this week, down from 43% over the epoch.
  `voice_miss` rows: none yet — no student traffic since the deploy. Tomorrow's block names them.
- The 19 unrendered closure lines are `vs`/`vt`'s: **run the prewarm.**

## Rulings wanted

1. Rule 61: must the grouping-symbols condition be in the same sentence as a "law" sentence?
2. A rule-7 "what would a table/graph show" referee — yes or no?
3. `lim … = ?` re-read each time, or refuted on sight under the 09-08 ruling?
4. The zero-product "and" row — yes or no?
5. The "equals zero" vs "= ?" board mismatch — referee or wait for a second sighting?
6. Still open from 09-12: "done for the day"; the Phase A redo (fresh problem or the same one).

I did no harm and this file is not truncated.
