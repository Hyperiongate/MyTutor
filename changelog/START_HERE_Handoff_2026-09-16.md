# START HERE — Handoff, 2026-09-16 (night)

Read this first in a new chat. Then the build docs it points to, only as needed.

## Where things stand

On Jim's disk, the newest: **`2026-09-16wl-the-first-geometry-sweep`**. Battery 12,558
passed, 0 failed, 3 skipped (frozen copy, 2026-09-16). Today's chain: `wh` (Basic sweep,
12,496) → `wi` (Pre-Algebra, 12,515) → `wj` (the 09-15 night watch, 12,527) → `wk` (Algebra
I, 12,545) → `wl` (Geometry, 12,558). Jim pushes and prewarms each; check `/health`.

Docs: `claude/Build_wh_…`, `Build_wi_…`, `Triage_NightWatch_2026-09-15_Four_Highs_Three_Seats`,
`Build_wk_…`, `Build_wl_…` (all `_2026-09-16.md`).

| course | sweeps so far | last result |
|---|---|---|
| Entry | wa (219) → wc (70) → wd (47) → we (15) → wf (14) → wg fixes, unswept | 14 findings, 26 clean |
| Basic | wg (67) → wh fixes, unswept | 67 findings, 7 clean |
| Pre-Algebra | wh (69) → wi fixes, unswept | 69 findings, 6 clean |
| Algebra I | wi (72) → wk fixes, unswept | 72 findings, 8 clean |
| Geometry | wk (63) → wl fixes, unswept | 63 findings, 7 clean |
| Algebra II | run on wk, report not yet pasted | — |
| Pre-Calc, Calculus, Prob/Stat, Diffeq | not yet | — |

## What to do next

1. Jim pushes `wl`, confirms `/health`, runs the **prewarm** (about a hundred lines: sixty
   Geometry rewrites plus the `mid`/`mid2` asks that now say "line segment").
2. **Paste the Algebra II report** (Jim ran it on `wk`) — it becomes `wm`. Then Pre-Calc,
   Calculus, Prob/Stat, Diffeq. The five swept courses wait for the weekly deep dive.
3. Triage the same way: generate the course's transcripts locally, read each quoted turn in
   context; generator first, then authored by kind in `lessons/<course>.py`; a reviewer
   mistake becomes a charter line in `coursesweep.py` (wk added two: `[[graph]]` range= is the
   x-window; a walk-back's "not N" names the common wrong answer; wl one: "square back" is
   Geometry's verb for the square root).
4. Patterns every remaining course will show: laws without their condition; a picture beat
   describing the *before* over the *after* board; the second-recap board (speak it); from
   Algebra I up, **"the whole of"** for a spoken bracket ("3 times the whole of 2 x plus 3")
   and **the dot between two equations** (split into two `[[step]]` tags; the pin now covers
   Entry–Algebra I by rendered transcript, generated lines included; `x³ · x² = x⁵` is one
   product and stays).
5. The night watch: paste any report; truth/HIGH gets built, the rest goes to the triage
   doc's ledger. `wj` added referee 101 (`aligndemo`, truth) and pendingzero's second shape.

## House decisions still open

- **The " · " between two equations** is gone from the five swept courses (the pin checks
  rendered transcripts, generated lines included). Algebra II carries 83 such lines; the
  three courses after it fewer. Per-sweep is working; one pass is still Jim's option.
- **"Times the whole of"** as the house phrase for a spoken bracket — worth a canon line if
  Jim agrees (wk used it in Algebra I).
- **`pendingzero` truth or conduct** — a board that poses a different equation from the
  words (the 09-15 HIGH). `exprswap` (09-04) is the precedent for truth. One-line move.
- **The night watch's cost.** Jim says ~$10 a night. The cost lever is `NIGHTWATCH_LESSONS`
  in Render (10 now; each lesson is roughly a dollar). During sweep weeks I recommended 2;
  `NIGHTWATCH=off` stops it entirely; leave `NIGHTWATCH_VERIFY` on. The morning report will
  print a "budget moved" banner — expected.
- **Render settings Jim changed 2026-09-16:** disk 15 GB; `TTS_CACHE_MAX_MB=10000` (read at
  startup — takes effect on the next deploy; the /admin cache line should say 10,000 MB).

## The method (unchanged from 09-15, two additions)

- Read the pasted report; generate the course's transcripts locally
  (`coursesweep.transcript_for` + `render_transcript`) to read each quoted turn in context
  before deciding real / generator / ruling.
- Asserted string replacements (`assert s.count(a) == 1`) into `lessons/<course>.py` and
  `lessonscripts.py`; `L.validate` all 360; `python3 tools/genspeechmap.py`; note the counts
  (course **39,999**; closure 40,253; speechmap 2,246 of 40,305; forSpeech drift 1,940;
  referees **101**, truth class **12**, falsehood rows **25**; methodology tile 101).
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
- A new PART's checks can be smoke-run alone before the 20-minute battery: exec the
  function's source with a stub `check` and `notes` (scratch pattern in this session). It
  caught a missing `rd` and a wrong op name before they cost a run.
- **New trap (counts):** a new beat with coordinates or decimals moves THREE counts —
  course lines, speechmap re-keys, and the forSpeech drift pin (`n == 1939`, PART 3ky's
  neighbour) — the third is easy to forget; it cost wl one battery run.
- **New trap (referees):** adding a `*_conflict` function moves ~30 count pins (`== 100`,
  `n_ref == 100`, `len(T.TRUTH_REFEREES) == 11`), the falsehood-row pins (`== 24`, the
  "last two are vp's" order pin), and `static/methodology.html`'s tile + both
  `data-referees` spans. Move them all in one regex pass, then the order pin by hand.
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
