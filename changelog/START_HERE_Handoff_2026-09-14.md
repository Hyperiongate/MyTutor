# START HERE — Handoff, 2026-09-14 (after `vz`, Phase A)

**Read this first.** It supersedes `claude/START_HERE_Handoff_2026-09-12_night.md` for STATE and
what is next. That doc still holds the container notes (PyPI is 403, GitHub works, use a `.pth`
not `ln -s`) and the staging law; the 09-12 evening doc holds the `vr` story.

Five builds landed since that handoff — `vv`, `vw`, `vx`, `vy`, `vz` — and **all of them are
pushed and live**. Jim ran the full prewarm on the evening of 09-14.

---

## 0. ⚠️ THE THREE THINGS THAT MATTER MOST

### (a) PHASE A IS IN. A FIRST MISS NO LONGER WAKES THE MODEL.
`vz` is the build Jim asked for on 09-12 and ruled on 09-13. On the **first miss in a row** the
engine speaks its own worked solution of the problem the student missed — the same `(spoken,
board)` pair the walk-back has always drawn — then asks a **fresh problem of the same shape**.
The AI's door opens on the **second miss in a row**, unchanged in every respect downstream.
A right answer resets the counter (`state["consec_miss"]`).

Two consequences to hold on to:

- **`interventions` now counts MODEL turns only.** The scripted explanation sits *above* the
  ladder, so a student who misses and recovers costs the ladder nothing. The level drop, the
  warm close and `MAX_PROBLEMS` all still work; measured on an all-wrong walk: 4 turns, **one**
  model turn where the old engine spent two.
- **The walk-back opener moved in all 320 generators**: `"Look what you did: "` →
  `"Here it is, step by step: "`. The same line now answers a wrong answer, where the old
  opener was false. The praise line above it still does the celebrating.

The 48 lessons whose ops have no worked generator keep the old path on the very first miss.
That is **Phase C**'s job. Phase B (an authored `reteach` beat per lesson) is still ahead.

### (b) THE VOICE CACHE CAP IS 9,000 MB NOW, AND ~812 MB OF IT IS DEAD
Jim raised `TTS_CACHE_MAX_MB` to 9000 on Render before the `vz` render — correctly: at 8,000 the
money guard would have **refused** the job with a 409 (7,464 MB in use + ~838 MB for the
re-rendered worked lines ≈ 8,300 MB projected).

⚠️ **The old worked clips did not go away.** They are orphaned, not deleted: about **812 MB** of
mp3s whose text no longer exists in the closure. The evictor only runs when the cache goes
*over* cap, so at 9,000 with ~8,300 in use, nothing will ever reclaim them.

There is no admin action that does this today — `tts-cache-repair` removes damaged clips only.
**The fix is a small, safe build and it is offered but not started:** an admin card that lists
(dry run, FREE) and then deletes cached clips no longer in `_script_closure_paths()` — exactly
the class the evictor already spends first. Ask Jim before building; he knows about it.

### (c) THE 09-14 WATCH WAS THE HOLE WATCH: FIVE OF TEN
Ten confirmed findings, **five of them holes** — nothing objected to what the student saw. A
hole is the expensive kind: no nudge and no retry could have helped. `vy` closed six (five holes
and one pass-through) with three new referees. **Read the pass-through and hole split on every
watch from now on** — it is the number that says whether the referees are the problem or the
nudges are.

---

## 1. State of the tree (verified 2026-09-14 evening)

| | |
|---|---|
| **LIVE on Render** | `vz` — `APP_BUILD = "2026-09-14vz-the-scripted-second-explanation"` |
| **On disk, unpushed** | nothing |
| **Battery** | **12,333 passed · 0 failed · 3 skipped** (frozen `vz` tree; 12,312 at `vy`, 12,286 at `vx`). Newest PART **3lu** |
| **Referees** | **100** (97 until `vy`) · truth 11 · first-use entries 22 (`≠` joined at `vy`) |
| **Closure** | **40,248** = course **39,994** + 254 demo lines · `speechmap.MAP` 2,244 of 40,300 |
| **Per-lesson audio ceiling** | **25,000 chars** / $5.50 (24,500 until `vz`; raised in writing, with the reason, at the check itself) |
| **Voice cache** | cap **9,000 MB** (`TTS_CACHE_MAX_MB` on Render) · ~8,300 MB in use after the `vz` render · **~812 MB orphaned** |

## 2. The five builds

| build | one line |
|---|---|
| `vv` | five from the 09-13 watch — the critic classifier's leak, the imperative gate on `unspoken`, ordinal fraction words, the colon pointer, the unearned-mark floor |
| `vw` | the marketing demo joins the closure: `DEMO_VOICE_LINES` (254) are prewarmed, evictor-protected and voiced on the course's script model |
| `vx` | Jim's twelve corrections-queue flags — "x **is equal to** 4" everywhere, the receipt's wrong 20 shown on the board, the pause after the value, the cookies story gone, the teach beat no longer repeating the picture |
| `vy` | six from the 09-14 watch — new referees `pendingzero` (rule 15, the night's HIGH), `pythaglaw` (rule 61), `firsttry` (false first-try praise); widened `unspoken` (the unknown is the LETTER) and `_FN_ASK` ("what's f of **two**?"); `≠` in the notation registry; `"factor"` out of the touching-brackets reading gate. Count 97 → 100, here and on the public methodology page |
| `vz` | **Phase A** — see §0(a) |

## 3. Rulings on the books

- **The redo after a worked solution is a FRESH problem** (09-13). Implemented in `vz`.
- **"Done for the day" is respected** — one warm closing line, a note of where they are, no
  persuading (09-13). ⚠️ **NOT YET IMPLEMENTED.** It belongs in the critic's charter, and the
  charter does not exist yet. This is the oldest unpaid ruling on the list.
- **The watch opens scenarios with an `__open__` turn** like the app (09-12). Not built. It
  changes every scenario's transcript, so build it in daylight, before a watch, never mid-week.
- **One opener for both paths** (09-14, Jim's call): the walk-back line had to be true after a
  wrong answer, and re-rendering 3,686 clips was worth it because the cache does not grow.

## 4. What is next, in the order I would take it

1. **The notation repair floor.** The 09-14 watch's calculus arrow (`0/0 → undefined`) is a
   pass-through: `notation` fires and the model will not satisfy it. For a symbol whose reading
   is FIXED, appending one true sentence is a safe code repair — the pattern the dangling-colon
   and unearned-mark floors already use. Smallest high-value item on the list.
2. **The cache reclaim card** (§0(b)) — ~812 MB, and it will recur every time authored text
   changes.
3. **The critic charter**, carrying the "done for the day" ruling.
4. **The watch's `__open__` turn.**
5. **Phase B** — an authored `reteach` beat per lesson, course by course, Entry/Basic first.
   Then **Phase C**, worked generators for the 48.
6. **Standing/open**: the four carried triage rulings (rule 61 same-sentence condition, the
   rule-7 table referee, the `lim` re-read, `"= ?"` vs "equals zero"); the prefetch-shelf probe
   wants its own counter instead of riding `clienterror · /session`; the ~9 "pedagogy
   preference" critic objections.

## 5. Closed, deliberately

- **"A board line below the fold"** (Jim's corrections queue, twice). No screenshot exists and
  the moment has passed; guessing at a layout fix would be duct tape. **The right answer if it
  recurs is structural, not a patch:** `screencheck.py` already judges the rendered screen in
  the battery, so teach it to fail a board whose last line lands below the visible area. Off the
  open list until it is seen again.
- The unplaced `6 ÷ 2 = 3` rule-48 item — too close to the 09-08 ruled-allowed shape to widen a
  gate the reviewer itself refutes four other findings for.

## 6. Laws this session paid for

- **Measure the audio bill before you assume it.** Phase A looked like thousands of new clips.
  It was six: the 48 lessons without `show_work_on_correct` are *exactly* the 48 whose ops have
  no worked generator, so every line the second explanation can speak was already rendered.
- **The referee catches its author.** `vx`'s new advance line said "Times before add, every
  time" and the battery's own canon sweep rejected it under rule 61 — a precedence rule spoken
  as a law with no grouping-symbol condition. Ship the referees and then obey them.
- **A gate word is not a reading.** `"factor"` sat in the touching-brackets first-use gate, so
  "it factors into those two pieces" counted as reading `(x − 2)(x − 3)`. A word that names the
  OPERATION is not a word that READS the notation.
- ⚠️ **Watch `sys.path[0]` when running helper scripts.** Stale copies of `lessonscripts.py`,
  `main.py`, `algebra1.py` and `prealgebra.py` were sitting in the scratchpad root from an
  earlier session, and any script run from there imported *those* instead of the real tree —
  which silently produced wrong answers in two hand-run checks. They have been moved to
  `scratchpad/_stale_modules/`. **The battery is the authority precisely because it runs from a
  frozen copy of the tree with its own `sys.path[0]`.** Never trust a hand-run sweep over it.
- **Never `pkill -f "ruletests.py"`** — the pattern matches the shell running the command and
  kills it (learned at `vx`, exit 144). Kill by PID.

## 7. Battery

Final run on the frozen `vz` tree: **12,333 passed · 0 failed · 3 skipped.**

I did no harm and this file is not truncated.
