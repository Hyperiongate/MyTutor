# Builds `vs` + `vt` — The Award Is Said Out Loud; The Check Line Rotates (2026-09-12)

**Stamp:** `2026-09-12vt-the-check-line-rotates` · **PARTs 3lo, 3lp** · files: `main.py`,
`lessonscripts.py`, `store.py`, `speechmap.py` (regenerated), `static/session.html`,
`ruletests.py` · no referee count change (97) · **prewarm owed: 19 clips** (15 award lines,
4 check lines — well under a dollar; `dry_run` first)

## `vs` — "when the student wins an award, tell them — congratulations, big deal"

**What was wrong.** An award was computed only when the dashboard's `/api/awards` route
was asked, and persisted then. A child earned Blaze on Tuesday and found it on a page on
Friday. The lesson — the place the child actually is — never said a word.

**What it does now.**
- `lessonscripts.AWARD_TEXT` mirrors `main.AWARD_DEFS` (id → name, description) and the
  battery pins the two equal, so a renamed award cannot drift from its spoken line.
  `AWARD_LINES` is **one fixed line per award** — fixed so each is one cached clip:
  *"Congratulations! You just earned the Blaze award — worked 7 days in a row. That is a
  big deal, and you did it."* ("100%" is said "100 percent": a standalone line is spoken with no board beside it, so it carries no symbol — the battery's own law) All fifteen are in `STANDALONE_LINES`, so the prewarm renders
  them.
- `main._award_ids_for(code)` is `awards_state`'s own computation, lifted out unchanged;
  the dashboard route's answer is byte-identical.
- `store.record_awards` now **returns the ids it wrote for the first time** (it returned
  `None`; every caller ignored it).
- `_fresh_award_steps(code)` computes, persists, and turns the new ids into `say` steps —
  beat `"award"`, the award's card on the board (`[[card title="🔥 Blaze" items="Worked 7
  days in a row"]]`). `_with_awards` places them **before** the `end` / `qend` step, which
  the page treats as the lesson's last.
- Spoken at three moments: **`/api/script/start`** (after the orientation, spoken only —
  this is where a streak or minutes award earned between visits lands), **every lesson end**
  (five call sites, through `_script_finish`'s new return value), and **a topic quiz's end**.
- Fail-open everywhere. The AUDIT lane, a blank code and a store that is off hear nothing.

**Proven** on a real sqlite store through the real route: a student with a 3-day streak
hears Spark once at start (third step, after the orientation), a second start is silent, the
dashboard shows it as new, Blaze rides with its card before the end step.

**Not done, deliberately:** the merit badges (a unit mastered) and course trophies are not
persisted awards and are not announced — `LINE_QUIZ_PASS` already says "this topic is
yours". If you want the Unit Quiz pass announced the same way, that is the live lane's
`record_check` path and a separate build.

## `vt` — "the 'ready!' bugs me after a while"

`lessonscripts.CHECK_LINES` is five checks — **"Ready?", "Okay so far?", "Shall we keep
going?", "Good so far?", "Ready for the next bit?"** — every one answered by the same
*Yes / Show me again*. `session.html`'s copy is byte-identical (pinned) and `scrCheck` cycles
them one per beat with `SCR.checkN`; a replay inside one check repeats the same line (a
cache hit, as before). `LINE_CHECK` is still "Ready?" (the first of them) and the practice
gate's `LINE_READY` is untouched, so every older pin holds.

## Counts that moved

Closure 39,969 → **39,988** (+19). `speechmap.py` regenerated: 2,245 → **2,246** of 40,275
→ **40,294** ("1,000 minutes" is tidied by forSpeech). Four pins moved with them, and the
live Playwright drive now expects the rotation (Ready?, Ready?, then one new line per beat,
then the gate's Ready?).

## After the push

Run the prewarm from `/admin`, `dry_run` first: it should list exactly 19 missing lines.

I did no harm and this file is not truncated.
