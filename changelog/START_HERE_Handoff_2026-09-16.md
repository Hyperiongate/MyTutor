# START HERE — Handoff, 2026-09-16

Read this first in a new chat. Then the build docs it points to, only as needed.

## Where things stand

On Jim's disk, not yet pushed as of this writing: **`2026-09-16wh-the-first-basic-sweep`**.
Battery 12,496 passed, 0 failed, 3 skipped (frozen copy, 2026-09-16). Previous deployed
build: `2026-09-15wg-the-fourth-clean-sweep` (12,477 / 0 / 3).

Jim ran the **first Basic sweep** on `wg`: 67 findings (3 generator, 64 authored), 7 of 36
clean. Build `wh` answered it: `claude/Build_wh_The_First_Basic_Sweep_2026-09-16.md`.

| course | sweeps so far | last result |
|---|---|---|
| Entry | wa (219) → wc (70) → wd (47) → we (15) → wf (14) → wg fixes, unswept | 14 findings, 26 clean |
| Basic | wg (67) → wh fixes, unswept | 67 findings, 7 clean |
| Pre-Algebra … Diffeq | not yet | — |

## What to do next

1. Jim pushes `wh`, confirms the stamp at `/health`, runs the **prewarm** (about sixty
   rewritten Basic lines plus 33 corrected practice intros).
2. **Run Pre-Algebra** from the Course sweep card (price, run, paste whole). Do not re-run
   Basic or Entry yet; both wait for the weekly deep dive.
3. Triage the same way: generator first (grep the quote in `lessonscripts.py`), then
   authored by kind in `lessons/prealgebra.py`, reviewer mistakes become charter lines in
   `coursesweep.py` — but read `wh`'s "Ruled, not fixed" first: the problem-space listing now
   answers the "case outside the bank" class without a charter word.
4. Expect Pre-Algebra to show the **second-recap board class** again (the closing beat
   writes an equation over a real-life sentence; Entry and Basic now speak them). Decide
   once whether every course speaks them — I would.

## Two house decisions still open (from wh)

- **The " · " between two equations.** Removed from Entry/Basic/Pre-Algebra step lines (a
  pin forbids `<digit> · <digit>` there). The upper courses use it ~350 times, where the dot
  *is* a times sign. Splitting those into two `[[step]]` tags is mechanical; it is a
  Pre-Algebra-and-up ruling for Jim.
- **The night watch's cost.** Jim says ~$10 a night. The cost lever is `NIGHTWATCH_LESSONS`
  in Render (10 now; each lesson is roughly a dollar). During sweep weeks I recommended 2;
  `NIGHTWATCH=off` stops it entirely; leave `NIGHTWATCH_VERIFY` on. The morning report will
  print a "budget moved" banner — expected.

## The method (unchanged from 09-15, two additions)

- Read the pasted report; generate the course's transcripts locally
  (`coursesweep.transcript_for` + `render_transcript`) to read each quoted turn in context
  before deciding real / generator / ruling.
- Asserted string replacements (`assert s.count(a) == 1`) into `lessons/<course>.py` and
  `lessonscripts.py`; `L.validate` all 360; `python3 tools/genspeechmap.py`; note the counts
  (course **39,997**; closure 40,251; speechmap 2,245 of 40,303; forSpeech drift 1,939).
- **New trap:** a pin can quote an authored sentence *split across two source lines* — grep
  the first half AND the last half in `ruletests.py`. Two such pins bit this build (the
  rounding closure line; "a lesson with its own intro speaks its own").
- **New trap:** `[[numberline denom="10"]]` draws fraction labels (1/10, 2/10) — never use
  it on a decimals lesson. The plain line already draws 0.1, 0.2 … on its own.
- Render new board tags headlessly (`window.__drawBoard` on `static/demo-lesson.html`,
  capture `window.boardWarn`) — scratch script pattern in this session: a stub
  `http.server` on the repo root + Playwright.
- Battery on a frozen copy; kill only by PID. This session the mount under `device_bash`
  failed, so the tree was staged file-by-file: root `.py`, `lessons/`, `tools/`, `static/`
  (incl. `shots/` and `mockup/`), `changelog/*.py.md`, `.github/workflows`, `RECOVERY.md`,
  `README.md` — the battery needs all of those to reach 0 failed.
- Deliver: cp to `/mnt/user-data/outputs/MyTutor/...` → SendUserFile → `device_commit_files`
  with `expectedMtimeMs` from staging → `project_write` the build doc. Jim reviews with
  `git diff` and pushes; I never commit.

## Open items carried forward

Notation repair floor; the voice-cache reclaim card (~812 MB orphaned); the critic charter
with the "done for the day" ruling; watch policy in code (lead with truth/HIGH, one-line
"nothing actionable"); the watch's `__open__` turn; screencheck rules (below the fold,
figure sizes); the pencil in the scripted lane; the child-mode skin; Phase C (worked
generators for the 48 lessons without one); Phase B deferred; the prefetch-shelf counter;
the tour button; `EST_USD_PER_LESSON` in `coursesweep.py` still the assumed $0.05 — correct
it from the billing page now that two courses have run.

I did no harm and this file is not truncated.
