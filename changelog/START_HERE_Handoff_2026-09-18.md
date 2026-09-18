# START HERE — Handoff, 2026-09-18

Read this first in a new chat. Then the build docs it points to, only as needed.

## Where things stand

On Jim's disk, the newest: **`2026-09-18wy-the-fifth-entry-sweep`**. Battery
12,704 passed, 0 failed, 3 skipped (frozen copy, 2026-09-18). The 09-16 chain: `wh` (Basic sweep, 12,496) → `wi`
(Pre-Algebra, 12,515) → `wj` (the 09-15 night watch, 12,527) → `wk` (Algebra I, 12,545) → `wl`
(Geometry, 12,558) → `wm` (Algebra II, 12,576) → `wn` (Pre-Calc, 12,589) → `wo` (Calculus,
half, 12,599) → `wp` (Diffeq, 12,612) → `wq` (Prob/Stat, 12,626, 09-17) → `wr` (Calculus
whole, 12,638, 09-17) → `ws` (Diffeq again, 12,649, 09-17) → `wt` (the referee pile, 12,658, 09-17) → `wu` (Pre-Calc again, 12,666, 09-17) → `wv` (the sweep says why it stopped, 12,674, 09-17) → `ww` (Pre-Calc, third reading, 12,685, 09-17) → `wx` (Algebra II again, 12,693, 09-18) → `wy` (Entry, fifth reading, 12,704, 09-18). Jim pushes and prewarms
each; check `/health`. The first round is over: every lesson in every course has been read
once. **The second round has begun, and the cycle converges: Diffeq went 119 → 62 findings,
0 → 8 clean, on one fix build; Pre-Calc 76 → 34 → (60 with wt's praise-board shape, fixed in the engine) 15 clean; Algebra II 73 → 43, 14 clean; Entry 14 → 19 (sixteen of them one engine consequence of ww, closed in wy) with 29 clean — the most any course has had.**

**OpenAI credits were topped up on the evening of 09-17** (the cap is not the balance —
an "Add credits" top-up is what the 429 "no credits remaining" needs; wv makes the card say
"could not be read" when it happens again). The course sweep and the night watch both use that seat, and a
36-lesson sweep now estimates at about $5.40 (`EST_USD_PER_LESSON` 0.15, corrected in ws).

Docs: `claude/Build_wh_…`, `Build_wi_…`, `Triage_NightWatch_2026-09-15_Four_Highs_Three_Seats`,
`Build_wk_…`, `Build_wl_…`, `Build_wm_…`, `Build_wn_…`, `Build_wo_…`, `Build_wp_…` (all
`_2026-09-16.md`), `Build_wq_The_First_ProbStat_Sweep_2026-09-17.md`,
`Build_wr_The_Second_Calculus_Sweep_2026-09-17.md`, `Build_ws_The_Second_Diffeq_Sweep_2026-09-17.md`, `Build_wt_The_Referee_Pile_2026-09-17.md`, `Build_wu_The_Second_PreCalc_Sweep_2026-09-17.md`, `Build_wv_The_Sweep_Says_Why_It_Stopped_2026-09-17.md`, `Build_ww_The_Third_PreCalc_Sweep_2026-09-17.md`, `Build_wx_The_Second_Algebra2_Sweep_2026-09-18.md`, `Build_wy_The_Fifth_Entry_Sweep_2026-09-18.md`.

| course | sweeps so far | last result |
|---|---|---|
| Entry | wa (219) → wc (70) → wd (47) → we (15) → wf (14) → wg fixes → wx (19, all 36) → wy fixes, unswept | 19 findings (16 of them ww's praise-board consequence), 29 clean |
| Basic | wg (67) → wh fixes, unswept | 67 findings, 7 clean |
| Pre-Algebra | wh (69) → wi fixes, unswept | 69 findings, 6 clean |
| Algebra I | wi (72) → wk fixes, unswept | 72 findings, 8 clean |
| Geometry | wk (63) → wl fixes, unswept | 63 findings, 7 clean |
| Algebra II | wk (73) → wm fixes → ww (43, 35 of 36) → wx fixes, unswept | 43 findings, 14 clean |
| Pre-Calc | wl (76) → wn fixes → ws (34, 27 of 36) → wu fixes → wv (60, all 36) → ww fixes, unswept | 60 findings (25 of them wt's praise-board shape, fixed in the engine), 15 clean |
| Calculus | wm (46, 19 of 36) → wo fixes → wq (88, all 36) → wr fixes, unswept | 88 findings, 4 clean |
| Diffeq | wo (119) → wp fixes → wr (62) → ws fixes, unswept | 62 findings, 8 clean (was 119, 0) |
| Prob/Stat | wo (92) → wq fixes, unswept | 92 findings, 1 clean |

## What to do next

1. Jim pushes `wy`, confirms `/health`, runs the **prewarm** (three Entry ops' lines, five
   credit lines in Pre-Calc and Prob/Stat, eight Entry rewrites).
2. **Basic** next, against `wg`'s floor of 67 findings and 7 clean (fixed in `wh`); the report
   becomes `wz`. Then Pre-Algebra, Algebra I, Geometry, Prob/Stat in first-round order. Expect the praise beats to read differently now: in a walk-back lesson
   the praise carries the WORKED board (ww), so "the praise says N and the board shows only
   the answer" should be gone everywhere — if a sweep still raises it, it is a wrong-path
   number the worked board does not draw (draw it with a ✗, as ww did for four ops). And
   **"the walk-back repeats the praise"** should be gone everywhere too: wy measured every
   praise/walk-back pair in every course (six ops repeated; all six are credit lines now)
   and PART 3mt runs the measurement every battery. Each rerun is a new letter. Diffeq's rerun is the
   template: expect roughly half the findings, the same class one layer down, and a handful
   of clean lessons. The weekly deep dive can wait for two or three of those.
3. Triage the same way: generate the course's transcripts locally, read each quoted turn in
   context; generator first, then authored by kind in `lessons/<course>.py`; a reviewer
   mistake becomes a charter line in `coursesweep.py` (wk added two: `[[graph]]` range= is the
   x-window; a walk-back's "not N" names the common wrong answer; wl one: "square back" is
   Geometry's verb for the square root; wm two: a ✗ on a step marks the wrong path, never a
   false equation; a bare "log" on an Algebra II board is base 2).
4. Patterns every remaining course will show: laws without their condition; a picture beat
   describing the *before* over the *after* board; the second-recap board (speak it); from
   Algebra I up, **"the whole of"** for a spoken bracket ("3 times the whole of 2 x plus 3")
   and **the dot between two equations** (split into two `[[step]]` tags; the pin now covers
   Entry–Calculus by rendered transcript, generated lines included; `x³ · x² = x⁵` and
   `√a · √b` are one product each and stay). Pre-Calc's class: a standard-form rule stated
   as a law ("un-square the right-hand number, every time") — say "in this form".
   Calculus's class (half seen): calculus *named* but not done ("calculus finds the best
   where the slope is zero" over a board that divided 40 by 4) — write the derivative line.
   Algebra II's own class, which the upper courses share: a law stated for today's numbers
   as if it were the whole truth — scope it ("in these examples", "for numbers in the same
   base", "the POSITIVE number that squares to"). Diffeq's version, the biggest pile yet
   (64 of 119): a law stated for the lesson's *model* as the whole truth ("every object on
   earth has a natural frequency", "Euler always lags", "both below zero and it spirals in")
   — say the model's condition ("in this undamped model", "in this forward walk", "for the
   single real poles in this lesson"). Prob/Stat's version (45 of 92): a rule of thumb
   stated as a law of nature ("the bell always shares itself out the same way, so 68
   percent of ANY group", "play it a thousand times and you end up level", "every dot is on
   one side or the other") — the honest words are "about", "on average", "in the long run",
   "when a group follows a bell curve", "when no dot lands on the line". Entry's version
   (wy): a rule stated for the lesson's numbers as if it were general ("any number up to
   999", "add the carried ten") — scope it ("a three-digit number", "if there is one").
5. The night watch: paste any report; truth/HIGH gets built, the rest goes to the triage
   doc's ledger. `wj` added referee 101 (`aligndemo`, truth) and pendingzero's second shape.

## House decisions still open

- **The praise beat and the walk-back are two different sentences (wy).** The praise is a
  credit line — the answer and its one reason, every number of it on the board it carries;
  the walk-back is the steps, over the same board. Where an op's praise WAS its walk-back
  (six ops at wx), the child heard one sentence twice. PART 3mt pins that no praise equals
  its walk-back in any course. When writing a new op: write the walk-back first, then the
  praise as the shorter line.
- **The stars stand for something (wy).** A story problem's star walk-back opens "each star
  stands for one of the rocks" — `_story_noun` reads the story's first counted noun. If a
  story ever has no counted noun, the walk-back reads as it always did.
- **The " · " between two equations** is gone from all ten courses (the pin checks rendered
  transcripts, generated lines included). Closed.
- **A sweep stops when the seat is dead (wv).** Three identical hard failures in a row
  (429, 401/403, no credits, quota, key not set) end the sweep; the rest are "not
  attempted", the report carries a STOPPED banner, the card says "N of N lessons could not
  be read: …" and the dropdown labels the report NOT READ. A flaky reader (different
  errors, or a timeout then an answer) is never cut short.
- **The admin card's report list is newest first** (wr) — by the sweep's own time, so the
  report to paste is always at the top of the dropdown. While a sweep is running the card's
  status line says so; the new report appears in the list only when it finishes.
- **`[[dotplot mark="8"]]`** (wq) draws the line a count-past-the-line beat talks about —
  the same idea as `[[numberline mid=]]`. If another figure's words ever "draw a line in
  your mind", give the figure the attribute rather than rewording the beat.
- **What the praise beat's board is (ww).** A lesson WITH a walk-back: the worked board
  (the walk-back's), so the praise's own working is drawn under it; the walk-back re-reads
  the same board. A lesson WITHOUT a walk-back: the ask's single answered line (wc) — so
  `chao`'s "25 is not on the praise board" (ws) stays declined, and any "intermediate value
  not on the praise board" in a no-walk-back lesson is the same ruling. wt's "answered line
  everywhere" lasted one build: it created 25 findings in one sweep. The answered line
  keeps the pending line's unit (wy: cube's `= ? cubes` → `6 cubes`) — a pending line that
  ends in a bare `?` answers bare.
- **The referee pile is gone (wt).** The canon's referees over every scripted beat of all
  ten courses: 56 refusals → 1 (an intro title card naming "the number line"; rule 7 is
  right in general, a title card is not a board claim — left alone). Two were referee
  misreadings now fixed in `tutor.py` ("What height" read as h(eight); "40 = 8 × ?" judged
  as if the blank were 40). PART 3mo re-runs the whole-canon referee sweep every battery.
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

## The method (unchanged from 09-15, three additions)

- Read the pasted report; generate the course's transcripts locally
  (`coursesweep.transcript_for` + `render_transcript`) to read each quoted turn in context
  before deciding real / generator / ruling. The pasted report itself does not survive a
  context compaction — copy its header line (findings, clean, unplaced, minutes) into a
  scratch file AND the build doc FIRST (wy's report survived only as a header line).
- Asserted string replacements (`assert s.count(a) == 1`) into `lessons/<course>.py` and
  `lessonscripts.py`; `L.validate` all 360 (the validator's canon: "what is left", never
  "remain"; a lesson's `symbols` must appear as the bare word — "cross", not "crossing"); `python3 tools/genspeechmap.py`; note the counts
  (course **40,010** since wy; closure 40,264; speechmap 2,244 of 40,316; forSpeech drift 1,938;
  referees **101**, truth class **12**, falsehood rows **25**; methodology tile 101).
- **New trap (counts, wy):** a generated line that shares text across lessons is ONE course
  line — make it differ per lesson (a story noun) and the count moves by the number of
  lessons that now differ. Diff `course_audio_lines()` against the frozen copy to see
  exactly which lines were added and which went, before moving the pins. Nineteen pins
  key on the course count (`len(L.course_audio_lines()) == N`) plus one `len(closure)`;
  move them with one replace — but a pin that shares its line with more code cannot take a
  trailing comment (it swallowed the rest of the line and cost wy a parse).
- **New trap (walk-backs):** a generated walk-back must open with the literal
  `Here it is, step by step: ` — colon and space. The engine's walk-back detection and a
  count pin (≥ 320 in `lessonscripts.py`) key on it; wr's first battery failed six lessons
  for a full stop in that place. Split the sentence AFTER the colon, never at it. And the
  text that follows the colon is pinned lower-case by the wd/we pins — a new opening
  sentence goes in FRONT of it, and the old text stays byte-identical when the new
  sentence is absent (wy's `_stars_stand_for`).
- **New trap (referees):** the canon's referee sweep (PART 3eu) refuses an arrow after an
  equals on a step line (`20 − 2x = 0 → x = 10`) and more than six lines on one teach
  board. Run `TT.prose_board_conflict` over the edited course before the battery — it
  cost wn a rerun until it was part of the pre-flight. Feed it `spoken + "\n" + board`
  (with `heard=` the same and `course=`), skip the three exempt phrases, and **diff against
  the frozen copy** — the referee returns only its FIRST finding per beat, so fixing one
  refusal can reveal the next behind it (wp's sepv: the chained equals hid an arrow, the
  arrow hid a "height" with no h(x)). Pre-existing refusals are not the build's to fix.
- **New trap (D: drive):** the device bridge lost D:\MyTutor twice on 09-16 ("could not
  stat", then "does not exist") for a few minutes each time; a write that times out has NOT
  landed — list the folder and compare sizes before retrying, and never `force`.
- **New trap (forSpeech):** "up 12: 25 plus 144" re-keys as a ratio (digit-colon-digit) and
  moves the speechmap and drift pins by one each — use a dash, not a colon, before a number.
- **New trap (headers):** PART 3ke fails a file whose header passes 100 KB. wp rolled
  `ruletests.py` and `lessonscripts.py` out a second time (`python3 notes_rollout.py --root
  . --cutoff 2026-09-10 --build xx --apply FILE`); 3ke now reads each header's newest pointer
  and checks every fenced block against its own cutoff, so a third roll-out needs no pin
  change. `main.py` is at ~95 KB — it goes next, with whatever cutoff leaves ~30 KB.
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
- A new PART's checks can be smoke-run alone before the 25-minute battery: exec the
  function's source with a stub `check` and `notes` (scratch pattern in this session). It
  caught a missing `rd`, a wrong op name, and (wy) a capitalisation change before they
  cost a run.
- **New trap (counts):** a new beat with coordinates or decimals moves THREE counts —
  course lines, speechmap re-keys, and the forSpeech drift pin (`n == 1938` since wu, PART 3ky's
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
  with `expectedMtimeMs` from a fresh `device_list_dir` → `project_write` the build doc. Jim reviews with
  `git diff` and pushes; I never commit.

## Open items carried forward

Notation repair floor; the voice-cache reclaim card (~812 MB orphaned); the critic charter
with the "done for the day" ruling; watch policy in code (lead with truth/HIGH, one-line
"nothing actionable"); the watch's `__open__` turn; screencheck rules (below the fold,
figure sizes); the pencil in the scripted lane; the child-mode skin; Phase C (worked
generators for the 48 lessons without one); Phase B deferred; the prefetch-shelf counter;
the tour button. (`EST_USD_PER_LESSON` corrected to 0.15 in ws — closed.)

I did no harm and this file is not truncated.
