# START HERE — Handoff, 2026-09-15 (end of day)

Read this first in a new chat. Then the build docs it points to, only as needed.

## Where things stand

Deployed build (pushed by Jim): **`2026-09-15wg-the-fourth-clean-sweep`**. Battery 12,477
passed, 0 failed, 3 skipped. Every file on disk in D:\MyTutor matches what the battery ran.

Today was Project 1 of the 09-14 deep dive — **the course sweep** — from nothing to a
calibrated instrument, run four times on Entry:

| build | what | Entry sweep after it |
|---|---|---|
| wa | coursesweep.py: one reviewer reads every scripted lesson once | 219 findings (no student on the page) |
| wb | the sweep sits in the night watch's OpenAI seat; Anthropic empty-reply guard | — |
| wc | calibrated: STUDENT lines, tap buttons, rulings in the charter; generator class; validator 8b (plurals); answered_board | 70 (61 authored, 9 generator, 9 clean) |
| wd | the authored pile + 9 generator items (polygon/clock/array on the ask, count-on walk-back, LINE_FRESH_OTHER, "N right" on the end card) | 47 (12 clean) |
| we | min5q wording, count-ALL inside ten, PRACTICE_INTRO_REASON (house-wide, 258 lessons), 41 authored | 15 (24 clean) |
| wf | **PROBLEM SPACE line** on every transcript + charter; 9 authored | 14 (26 clean, 0 generator) |
| wg | 12 authored (the regrouping units were the one real defect); charter: why beats are unpictured by design | not yet run |

Docs: `Build_wa` … `Build_wg` in `changelog/` and `claude/`. The deep-dive project list is
`Deep_Dive_2026-09-14_The_Forever_War_And_The_Project_List.md`.

## What to do next (my recommendation, in the wg doc)

1. Jim runs the prewarm after wg (a dozen rewritten Entry lines).
2. **Do not run Entry a fifth time.** Run **Basic** from the Course sweep card: pick the
   course, dry-run for the price (~$2 for 36 lessons), run, paste the report whole.
3. Triage the Basic report the way the Entry ones went: generator findings first (fix
   once, fixed everywhere), then authored by kind; anything that is the reviewer's
   mistake becomes a charter line in `coursesweep.py`, once. Expect Basic's first run to
   look like Entry's wc run — a big pile with a few generator classes in it.
4. Then Prealgebra, and so on down the ten courses. Entry again at the next weekly deep
   dive.

## The method that worked (repeat it)

- Read the pasted report; it is the only copy reachable (reports live on Render).
- Edit `lessons/<course>.py` for authored, `lessonscripts.py` for generators, with
  asserted string replacements (`assert s.count(a) == 1`).
- `L.validate` all 360 (scratchpad `val.py`); `python3 tools/genspeechmap.py`; note the
  course-line count (`len(L.course_audio_lines())`, now **39,996**; closure 40,250;
  speechmap 2,244 of 40,302).
- Render any NEW board tag headlessly on `static/demo-lesson.html` served from the repo
  root (`window.__drawBoard`, capture `window.boardWarn`).
- Add a PART (next is **3mc**) pinning the classes; move the count pins; dated notes in
  every touched file; `APP_BUILD` stamp in main.py.
- Full battery on a frozen copy (~20 min): copy tree to scratchpad, rm `__pycache__` and
  `data/coursesweep`, `chmod -R a-w . ; chmod u+w .`, `nohup python3 ruletests.py > log &`.
  Kill only by PID — `pkill -f` / `pgrep -f` with the script name in the pattern kills
  your own shell (it did, three times today).
- Deliver: cp to `/mnt/user-data/outputs/MyTutor/...` → SendUserFile →
  `device_commit_files` (force) to `D:\MyTutor\...` → `project_write` the build doc to
  `claude/`. Jim reviews with `git diff` and pushes; I never commit.

## Traps the battery caught today (so the next build avoids them)

- A board that asks `X = ?` under its own answer on the same beat: rule 17. Pose the sum
  without `= ?` on a beat that works it to its answer.
- Every figure needs `caption=` — polygons included (rule 41).
- A tape whose words say "missing part" must mark a piece (`shaded="1"`, rule 63).
- The VOCABULARY canon: "over nine" only; "more than nine" / "ten or more" are banned.
  "makes" / "is the same as" are banned for "equals".
- Digit-colon-digit in a SPOKEN line ("11: 6") is read as a ratio — use a dash. The
  speechmap count moving is the tell.
- `[[array view="groups"]]` writes "3 × 4" unless `eq=` is set; Unit 9 never says "times".
- Reason options are capped at 12 words; beats at 80; sentences at 34.
- Text pins in ruletests quote authored sentences; grep for the old sentence before
  rewriting it (`grep -n "<phrase>" ruletests.py`).
- `answered_board` fills the LAST `[[step eq="…?…"]]` — keep the step line after any
  figure on an ask board.

## Open items carried forward (from the deep dive list)

Notation repair floor; the voice-cache reclaim card (~812 MB of orphaned old clips under
the 9,000 MB cap); the critic charter with the "done for the day" ruling; watch policy
(truth/HIGH only); the watch's `__open__` turn; screencheck rules (below the fold, figure
sizes); the pencil in the scripted lane (bigger, points and inks); the child-mode skin;
Phase C (worked generators for the 48 lessons without one — 12 Entry + 36 Diffeq); Phase
B deferred; the prefetch-shelf counter; the tour button (Jim to tap by hand); the 34
lessons with their own practice intro that may make the "three in a row and we're done"
promise before a reason question (their courses' sweeps will list them).

## Two things Jim asked today, outside the build

- Claude vs Claude Code, for his managers' talk: same model, two doors — the assistant
  for everyone vs the same assistant at a programmer's terminal inside a code project.
  This session (Cowork, linked to his disk) has the same reach on the project as Claude
  Code would; the difference is where the work runs, not what it can touch.
- Whether to hand the next sweep to Claude Code: no — the calibration knowledge is here,
  and the handoff docs are what carry it if a session starts cold.

I did no harm and this file is not truncated.
