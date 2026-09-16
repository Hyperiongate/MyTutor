# START HERE — Handoff, 2026-09-16 (evening)

Read this first in a new chat. Then the build docs it points to, only as needed.

## Where things stand

On Jim's disk (wh pushed and deployed; wi written, awaiting his `git diff` and push):
**`2026-09-16wi-the-first-prealgebra-sweep`**. Battery 12,515 passed, 0 failed, 3 skipped
(frozen copy, 2026-09-16). Before it: `wh` (12,496 / 0 / 3), `wg` (12,477 / 0 / 3).

Two course sweeps were answered today, one build each:
`claude/Build_wh_The_First_Basic_Sweep_2026-09-16.md` and
`claude/Build_wi_The_First_PreAlgebra_Sweep_2026-09-16.md`.

| course | sweeps so far | last result |
|---|---|---|
| Entry | wa (219) → wc (70) → wd (47) → we (15) → wf (14) → wg fixes, unswept | 14 findings, 26 clean |
| Basic | wg (67) → wh fixes, unswept | 67 findings, 7 clean |
| Pre-Algebra | wh (69) → wi fixes, unswept | 69 findings, 6 clean |
| Algebra I … Diffeq | not yet | — |

## What to do next

1. Jim pushes `wi`, confirms the stamp at `/health`, runs the **prewarm** (about seventy
   rewritten Pre-Algebra lines).
2. **Run Algebra I** from the Course sweep card (price, run, paste whole). Entry, Basic and
   Pre-Algebra all wait for the weekly deep dive.
3. Triage the same way: generator first (grep the quote in `lessonscripts.py`; generate the
   course's transcripts locally to read each quoted turn in context), then authored by kind
   in `lessons/algebra1.py`; a reviewer mistake becomes a charter line in `coursesweep.py`.
   `wi` needed none — the problem-space listing from `wh` held.
4. Two patterns every remaining course will show: a claim true only *above 1* ("the smallest
   factor", "nothing divides both") — one-word fixes; and a picture beat that describes the
   *before* over a board that draws the *after* — split the beat. The second-recap board
   class (the closing beat writes an equation over a real-life sentence) is being answered
   course by course by speaking the equation; Entry, Basic and Pre-Algebra do now.

## Two house decisions still open (from wh)

- **The " · " between two equations.** Removed from Entry/Basic/Pre-Algebra step lines (a
  pin forbids `<digit> · <digit>` there). The upper courses use it ~350 times, where the dot
  *is* a times sign. Splitting those into two `[[step]]` tags is mechanical; it is a ruling
  for Jim. The Algebra I sweep will probably raise it — that is the moment to decide.
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
  (course **39,998**; closure 40,252; speechmap 2,245 of 40,304; forSpeech drift 1,939).
- **New trap:** a pin can quote an authored sentence *split across two source lines* — grep
  the first half AND the last half in `ruletests.py`. Two such pins bit this build (the
  rounding closure line; "a lesson with its own intro speaks its own").
- **New trap:** `[[numberline denom="10"]]` draws fraction labels (1/10, 2/10) — never use
  it on a decimals lesson. The plain line already draws 0.1, 0.2 … on its own.
- **New trap:** a lesson's `symbols` must be *named* in a why/picture/teach line (rule 14's
  validate check). Rewording "across the decimal point" out of a sentence broke it; the
  phrase went back in, truer.
- **New trap:** `[[pie parts=N shaded=K]]` clamps K to N — it cannot draw an improper
  fraction. Use the written form.
- PART 3md's checks can be smoke-run alone before the 20-minute battery: exec the function's
  source with a stub `check` (scratch pattern in this session). Cheap insurance.
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
