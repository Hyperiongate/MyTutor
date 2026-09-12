# Build `vr` — The 166, Read Per Reason (2026-09-12)

**Stamp:** `2026-09-12vr-the-166-read-per-reason` · **PART 3ln** (58 pins) · files: `tutor.py`,
`nightwatch.py`, `main.py`, `ruletests.py` · **no referee count change (97)** · no prompt file
change (the critic's charter lives in `tutor.py`) · no prewarm owed

## What the number actually is

I read the 48 newest `pass_through` rows out of `system_events` through the admin feed
(`/api/admin/events`, from the /admin tab's own stored key — read-only, nothing written).
The week's counters: `livecritic` 117, `prosecheck` 45, `quizverdict` 1.

**43 of the 48 carry `code = AUDIT`.** They are the night watch's own scenarios — the
09-11 and 09-12 runs, 08:00–09:05 UTC, seventeen to twenty-six pass-throughs a night. Five
are live (code `0000`, Entry and Basic, 09-10 and 09-11). So "166 a week, a child sees the
flawed reply each time" is mostly "the watch's twenty scenarios ship ~20 flawed replies a
night." The defect rate is real and it is the same model on the same lane — but the number
was never a count of children. The report now says which is which (below).

## Per reason — 35 `livecritic`, 13 `prosecheck`

| class | rows | verdict | what `vr` does |
|---|---|---|---|
| **The critic outside its charter** — concedes the draft is right ("which is indeed correct… however, the tutor should show the work"), or is advice ("to be clear, or better:", "could confuse", "risks the explanation feeling abstract", "sounds like an arbitrary rule", "potentially confusing") | 8 of 35 | **rule wrong** (the critic's, not ours) | `critic_objection_is_style()` — a conceding or advisory verdict with no error word outside the quotes is a PASS, no retry, counted `referee_soft · criticstyle` with the sentence. `_CRITIC_SYSTEM` says it in words too. |
| **Pedagogy preferences with no error named** ("should verify before marking", "should show the work", "without first finding out what topic", "should check progress first") | ~9 of 35 | rule wrong, but not decidable by shape | The prompt clarification only. Still retried. Watch `criticstyle` next week to see whether the words moved the critic. |
| **The critic wrong on the math** (3 tenths of a dollar *is* 30 cents; the square-root-method sentence) | 2 | critic wrong | Nothing mechanical can know. Left. |
| **The critic contradicting itself across drafts** — entry "done for the day": attempt 2 *"overrides the student's request to stop"*, attempt 3 *"should gently encourage one more problem"* | 2 (one turn) | **ruling** — the standing "done for the day" flag; no draft can satisfy both | Yours. |
| **Turn-one objections on the watch's lane** — "launches into a lesson plan without acknowledging '70' / 'what were we doing again' / 'I want to take the final exam'" | ~5 | **harness shape** | `run_scenario` feeds the scenario's opening line as a student message on turn one with empty history; the live app's turn one is `__open__` (no student text, the opener branch). The prompt's opener behaviour and the critic's item 1 collide on a turn that does not exist live. Noted, not changed — your call whether the watch should open with `__open__` like the app. |
| **Real item-1 defects** the model would not fix (pivots to a different equation; "still doing it wrong" unacknowledged) | ~4 | nudge / referee | `vp`'s `unacked` (94) is the referee for the second; the first is the rule-18 class the critic already names in the first sentence. Left to the next watch's stamps. |
| **Legit item-3 defects** (`≠` unexplained; "denominator" unexplained) | 2 | referee-shaped | Notation entries are `vm`'s territory (`≠` is a first-use candidate). Not built here. |
| `finiteanswer` — "three fifths or five eighths?" captured as **"Fifths \| Five"**; the nudge asked for nonsense buttons and the model refused three times | 1 of 13 | **nudge wrong (ours)** | `_EITHER_OR_RE` carries a number word into each label: `Three fifths \| Five eighths`. Articles are not carried; canon swept, 0 new fires. |
| `danglingcolon` — a spoken colon pointing at a tag, three lessons, three attempts each | 3 of 13 | **nudge wrong by omission + code repair** | The detail now names the fix. `repair_dangling_colon` is a floor at the door: `:` → `.`, or `what's on the board.` after a pointer word (`that's:`); re-checked by referee 57; counted `code_repair · danglingcolon`. |
| `problemnumbers` — "the column adds 3.50 and 0.47 and the words never say them" | 2 of 13 | **referee wrong** | `0.47` only counted as "zero point four seven". Now "forty-seven cents", "forty-seven hundredths", "47 cents" and "point four seven" read it; a whole part above zero must still be said; gw's guard holds. |
| `secondtriangle`, `coldquiz`, `spokenlen`, `staleboard`, `boardflood` (7 lines), `varcase` (pre-`vh`), the rewrite arrow | 7 of 13 | mixed | `varcase` has its floor since `vh`. The rest are one row each — no pattern yet. |

## The eyes

The report's "what they actually said" block asked `recent_events` for every alarming kind
**except `pass_through`** — the biggest number on the page never had a reason under it.
`nightwatch.pass_through_lines()` prints the newest 200 rows grouped by the referee in the
detail's parentheses (`vg`), with the **AUDIT / live split** on the first line and each
referee's distinct reasons newest-first with the ghost test. `/api/admin/events` takes
`?kind=pass_through&limit=200` (store caps at 200); with no parameters it is byte-identical.

## Pins (PART 3ln)

The eight style verdicts pass and twelve real ones stay (quoted text blind; "verify … is
correct" is not a concession; "their error" is not an error word) · the verdict path calls
the classifier before returning and counts it · the charter's three new sentences · the
fraction labels, the old labels, the article case · 57's detail names the fix · the floor on
Jim's diffeq reply, a plain clause, two colons in one reply, a healthy reply byte-for-byte,
wired after the case floor and counted · the five readings of 0.47, the whole-part law,
"point four seven" is not 0.4, gw's guard, tenths ≠ hundredths · the 09-12 column reply
read as money · `pass_through_lines` on a fake store (the query, the split, the grouping,
the pre-`vg` fallback, the repeat, empty, raising) · the report and endpoint wiring · 97 /
11 · no `\x08` · the dated notes.

## What to watch next

`referee_soft · criticstyle` (how many objections the classifier passed, and their
sentences — if one is a real defect, the classifier is wrong and the row says so),
`code_repair · danglingcolon`, and whether `pass_through · livecritic` drops from ~117.
The next watch's pass-through block will say, per referee, which nudges the model still
ignores.

I did no harm and this file is not truncated.
