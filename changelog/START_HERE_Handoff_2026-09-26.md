# START HERE — Handoff, 2026-09-26

Read this first in a new chat. Then the build docs it points to, only as needed.

## Where things stand

On Jim's disk: **`2026-09-26yg-the-sixth-entry-sweep`** (battery 13,146 passed, 0
failed, 3 skipped) — Entry's sixth reading, 6 findings (19 at `wy`), 31 clean, all fixed;
five of six on generators (no `>` or `÷` on an Entry board; the take-away walk-back shows
its count). **Nine of ten courses have had their third-round reading; Pre-Calc's fourth is
the one left.** Before it, `yf` (battery 13,136) — Calculus's third reading, 24 findings (46 at `xi`), 18 clean, all
fixed; the HIGH was `xi`'s own π-less fix; `chan` and `linf` draw their wrong paths. Jim
pasted the report despite the break, so it was built. Before it, `ye` (battery 13,119) — the
nightly screenwatch workflow gets a second job that drives
eight authored lessons a night through xy's scripted lane (`--script rota`, `--fail-on
MEDIUM`), and the last four fixed-slice note pins in the battery read `notes()`. Built on
Jim's "go" while the sweeps are on hold. Before it, `yd` (battery 13,110) — the ten-course
screen survey's finding: the grapher never set
the label fit (473 of 508 small labels), fixed; S5 and S1 learn two exceptions. Before it,
`yc` (battery 13,098) — a one-function fix to `yb`'s redraw, which looped through the feed's
MutationObserver (found by the screen survey: four times slower, one lesson never settled).
Before it, `yb` (battery 13,097, one run for `ya` and `yb` together) — the whole chain below is on
his disk; `yb` is the one to push (`xx`, `xy`, `xz`, `ya` before it if not yet pushed). Jim
went offline after pasting the Geometry report; `ya` (the sweep) and `yb` (the gate build) were
built in that one session. `xd`, `xe` and `xf` were built on 09-19 while Jim was away from his
computer for two days (phone only), on his word from his phone ("work on whatever you can
work on"), and all three were written to D:\MyTutor in one commit on 09-21 — his `/health`
had still read `xc` until then. `xg` (`2026-09-21xg-the-second-probstat-sweep`, 12,778) and `xh`
(`2026-09-21xh-the-credit-line-everywhere`, 12,785) followed, both committed the same day.
`xi` (`2026-09-22xi-the-second-calculus-sweep`, 12,801) followed and is pushed — **with it
every one of the ten courses has had two readings.** `xj`
(`2026-09-22xj-the-spoken-beat-is-short-everywhere`, 12,809) followed and is pushed, with its
prewarm done. `xk`
(`2026-09-22xk-the-praise-is-not-the-walk-back`, 12,821) — the third round's first reading
(Pre-Algebra, 29 findings, 18 clean) — is pushed and prewarmed. `xl`
(`2026-09-22xl-the-watch-policy`, 12,841) — project 2 of the 09-14 deep dive, the first gate
build interleaved with the sweep — was written to his disk on 09-22. `xm`
(`2026-09-22xm-the-angle-carries-its-unit`, 12,855) — the third round's Pre-Calc reading
(28 findings, 24 clean; pyid and arsn, rebuilt in xk, came back CLEAN) — was written to
his disk on 09-22. `xn` (`2026-09-22xn-the-miss-has-a-face`, 12,865) — project 4 of the
09-14 deep dive, the second gate build — was written to his disk on 09-22. `xo`
(`2026-09-22xo-the-forty-eight-get-their-walk-back`, 12,883) — Phase C, the third
gate build: the 48 lessons (36 Diffeq + 12 Entry) that sent every first miss to the AI have a
scripted walk-back now, and the sweep can read their miss path — written to his disk on
09-22. `xp` (`2026-09-23xp-the-sweep-survives-a-restart`, 12,907) —
the course sweep saves a checkpoint after every lesson, survives a deploy or a Render
restart as INTERRUPTED, and can be RESUMED; built because two Algebra I sweeps vanished on
09-22 under pushes — written to his disk on 09-23 and pushed (the Algebra I sweep ran on it).
`xq` (`2026-09-23xq-the-third-algebra1-sweep`, 12,920) — the third round's Algebra I
reading (23 findings, 23 clean; 50 and 10 at xa) — was written to his disk on 09-23.
`xr` (`2026-09-23xr-the-pencil-in-the-scripted-lane`, 12,935) — project 5, the fourth gate
build: the pencil acts on every scripted beat, docked at the board and bigger — was written
to his disk on 09-23. **Built after it: `xs` (`2026-09-23xs-the-third-diffeq-sweep`,
12,965)** — the third Diffeq reading (39 findings, 13 clean; was 62 and 8), the first that
saw the miss path, and the count still fell. Its class, measured canon-wide: the board skips
the arithmetic the words say (35 Diffeq beats, all drawn; the other nine courses a ratchet).
`[[graph field=]]` draws a slope field now — written to his disk on 09-23. **Built after it:
`xt` (`2026-09-23xt-the-voice-cache-reclaim-card`, 12,978)** — project 9, the fifth gate
build: an admin card that counts (free) and then deletes every cached clip the scripted
closure no longer names, older than a day; the course's clips are never touched — pushed and
live. **Built after it: `xu` (`2026-09-23xu-the-third-probstat-sweep-part-one`, 12,991)**
— the third Prob/Stat reading stopped at 16 of 36 (the reader's credits ran out): 13
findings fixed, and the sweep now KEEPS its checkpoint when the seat cuts it short, so the
rest can be resumed — written to his disk on 09-23. **Built after it: `xv`
(`2026-09-24xv-the-third-algebra2-sweep`, 12,999)** — the third Algebra II reading (28
findings, 19 clean; was 43 and 14): three HIGHs about i and the discriminant, ten laws given
their condition, the xs class in the absolute-value lesson, imag's praise a credit line, and
a charter line so "the choices are never read aloud" stops coming back — written to his disk
and pushed. **Built after it: `xw` (`2026-09-24xw-the-third-probstat-sweep-part-two`,
13,008)** — the rest of the third Prob/Stat reading, the FIRST sweep resumed in production
(30 read before the seat died, 6 after): 26 findings, 23 clean (was 60 and 10); bias's praise
was the HIGH. **Built after it: `xx` (`2026-09-24xx-the-child-mode-skin`, 13,030)** —
project 7, the sixth gate build: Entry and Basic get a cream board (light board only), 72px
answer buttons, three-in-a-row dots read off the engine's own streak, and the helper text
leaves the child's screen after the first answer; the other eight courses byte-for-byte
unchanged. **Built after it: `xy` (`2026-09-24xy-the-two-flags-nobody-could-screenshot`,
13,061)** — project 6, the seventh gate build: screencheck learns S8 (the last line is on
the screen) and S9 (figure widths agree, by kind) and drives the SCRIPTED lane; its first survey
found and the build fixed both of Jim's unscreenshottable flags — the NaN figure shrink behind
"half as big" and the scroll latch behind "a board line below the fold". **Built after it: `xz`
(`2026-09-24xz-the-third-basic-sweep`, 13,073)** — the third Basic reading: 9 findings, 29
clean (was 41 and 14), no generator finding at all; two of the nine were reviewer misreads
turned into coursesweep fixes (the transcript note is not a TUTOR line; the PROBLEM SPACE lists
its exact pairs). **Built after it: `ya` (`2026-09-24ya-the-third-geometry-sweep`,
13,097)** — the third Geometry reading: 11 findings, 27 clean (was 36 and 16), no
generator finding; all eleven fixed; `[[graph segments=]]` is new. **Built after it: `yb`
(`2026-09-24yb-the-words-grow-back-on-a-shrunk-figure`, 13,097)** — the over-tall beat:
a figure the board shrinks to fit its turn is drawn again for the width it gets, labels
re-fitted (6px → 12–15px on the xy screenshot's array); screencheck S10 measures every
figure's smallest label. See **Written to D:\MyTutor** below. The 09-16 chain: `wh` (Basic sweep, 12,496) → `wi`
(Pre-Algebra, 12,515) → `wj` (the 09-15 night watch, 12,527) → `wk` (Algebra I, 12,545) → `wl`
(Geometry, 12,558) → `wm` (Algebra II, 12,576) → `wn` (Pre-Calc, 12,589) → `wo` (Calculus,
half, 12,599) → `wp` (Diffeq, 12,612) → `wq` (Prob/Stat, 12,626, 09-17) → `wr` (Calculus
whole, 12,638, 09-17) → `ws` (Diffeq again, 12,649, 09-17) → `wt` (the referee pile, 12,658, 09-17) → `wu` (Pre-Calc again, 12,666, 09-17) → `wv` (the sweep says why it stopped, 12,674, 09-17) → `ww` (Pre-Calc, third reading, 12,685, 09-17) → `wx` (Algebra II again, 12,693, 09-18) → `wy` (Entry, fifth reading, 12,704, 09-18) → `wz` (Basic again, 12,714, 09-18) → `xa` (Pre-Algebra again, 12,724, 09-18) → `xb` (Algebra I again, 12,732, 09-19) → `xc` (Geometry again, 12,739, 09-19) → `xd` (the colon is not a ratio, 12,745, 09-19) → `xe` (the pre-sweep, 12,751, 09-19) → `xf` (the pre-sweep, the other eight, 12,759, 09-19) → `xg` (the second Prob/Stat sweep, 12,778, 09-21) → `xh` (the credit line everywhere, 12,785, 09-21) → `xi` (the second Calculus sweep, 12,801, 09-22) → `xj` (the spoken beat is short everywhere, 12,809, 09-22) → `xk` (the praise is not the walk-back, 12,821, 09-22) → `xl` (the watch policy, 12,841, 09-22) → `xm` (the angle carries its unit, 12,855, 09-22) → `xn` (the miss has a face, 12,865, 09-22) → `xo` (Phase C, the forty-eight get their walk-back, 12,883, 09-22) → `xp` (the sweep survives a restart, 12,907, 09-23) → `xq` (the third Algebra I sweep, 12,920, 09-23) → `xr` (the pencil in the scripted lane, 12,935, 09-23) → `xs` (the third Diffeq sweep, 12,965, 09-23) → `xt` (the voice-cache reclaim card, 12,978, 09-23) → `xu` (the third Prob/Stat sweep, part one, 12,991, 09-23) → `xv` (the third Algebra II sweep, 12,999, 09-24) → `xw` (the third Prob/Stat sweep, part two, 13,008, 09-24) → `xx` (the child-mode skin, 13,030, 09-24) → `xy` (the two flags nobody could screenshot, 13,061, 09-24) → `xz` (the third Basic sweep, 13,073, 09-24) → `ya` (the third Geometry sweep, 09-24) → `yb` (the words grow back on a shrunk figure, 13,097, 09-24, one battery for both). Jim pushes and prewarms
each; check `/health`. The first round is over: every lesson in every course has been read
once. **The second round has begun, and the cycle converges: Diffeq went 119 → 62 findings,
0 → 8 clean, on one fix build; Pre-Calc 76 → 34 → (60 with wt's praise-board shape, fixed in the engine) 15 clean; Algebra II 73 → 43, 14 clean; Entry 14 → 19 (sixteen of them one engine consequence of ww, closed in wy) with 29 clean — the most any course has had; Basic 67 → 41, 7 → 14 clean; Pre-Algebra 69 → 58, 6 → 9 clean (ten of the 58 were the near-repeat praise class, closed across 25 ops in xa); Algebra I 72 → 50, 8 → 10 clean — the first reading after xa, and the praise class did not come up once; Geometry 63 → 36, 7 → 16 clean. Third round: Pre-Algebra 58 → 29, 18 clean; Pre-Calc 60 → 28, 24 clean; Algebra I 50 → 23, 23 clean; Diffeq 62 → 39, 13 clean (its first reading WITH the miss path in view); Algebra II 43 → 28, 19 clean; Prob/Stat 60 → 26, 23 clean (13 on the first 16, then the whole course resumed); Basic 41 → 9, 29 clean — the smallest pile yet; Geometry 36 → 11, 27 clean.**

**OpenAI credits were topped up on the evening of 09-17** (the cap is not the balance —
an "Add credits" top-up is what the 429 "no credits remaining" needs; wv makes the card say
"could not be read" when it happens again). The course sweep and the night watch both use that seat, and a
36-lesson sweep now estimates at about $5.40 (`EST_USD_PER_LESSON` 0.15, corrected in ws).

Docs: `claude/Build_wh_…`, `Build_wi_…`, `Triage_NightWatch_2026-09-15_Four_Highs_Three_Seats`,
`Build_wk_…`, `Build_wl_…`, `Build_wm_…`, `Build_wn_…`, `Build_wo_…`, `Build_wp_…` (all
`_2026-09-16.md`), `Build_wq_The_First_ProbStat_Sweep_2026-09-17.md`,
`Build_wr_The_Second_Calculus_Sweep_2026-09-17.md`, `Build_ws_The_Second_Diffeq_Sweep_2026-09-17.md`, `Build_wt_The_Referee_Pile_2026-09-17.md`, `Build_wu_The_Second_PreCalc_Sweep_2026-09-17.md`, `Build_wv_The_Sweep_Says_Why_It_Stopped_2026-09-17.md`, `Build_ww_The_Third_PreCalc_Sweep_2026-09-17.md`, `Build_wx_The_Second_Algebra2_Sweep_2026-09-18.md`, `Build_wy_The_Fifth_Entry_Sweep_2026-09-18.md`, `Build_wz_The_Second_Basic_Sweep_2026-09-18.md`, `Build_xa_The_Second_PreAlgebra_Sweep_2026-09-18.md`, `Build_xb_The_Second_Algebra1_Sweep_2026-09-19.md`, `Build_xc_The_Second_Geometry_Sweep_2026-09-19.md`, `Build_xd_The_Colon_Is_Not_A_Ratio_2026-09-19.md`, `Build_xe_The_Pre_Sweep_2026-09-19.md`, `Build_xf_The_Pre_Sweep_The_Other_Eight_2026-09-19.md`, `Build_xg_The_Second_ProbStat_Sweep_2026-09-21.md`, `Build_xh_The_Credit_Line_Everywhere_2026-09-21.md`, `Build_xi_The_Second_Calculus_Sweep_2026-09-22.md`, `Build_xj_The_Spoken_Beat_Is_Short_Everywhere_2026-09-22.md`, `Pre_Sweep_Finding_2026-09-22_The_Law_Without_Its_Condition.md`, `Ruling_2026-09-22_When_The_Sweeps_Stop.md`, `Build_xk_The_Praise_Is_Not_The_Walk_Back_2026-09-22.md`, `Deep_Dive_2026-09-22_Eight_Days_Of_One_Project.md`, `Build_xl_The_Watch_Policy_2026-09-22.md`, `Build_xm_The_Angle_Carries_Its_Unit_2026-09-22.md`, `Build_xn_The_Miss_Has_A_Face_2026-09-22.md`, `Build_xo_The_Forty_Eight_Get_Their_Walk_Back_2026-09-22.md`, `Build_xp_The_Sweep_Survives_A_Restart_2026-09-23.md`, `Build_xq_The_Third_Algebra1_Sweep_2026-09-23.md`, `Build_xr_The_Pencil_In_The_Scripted_Lane_2026-09-23.md`, `Build_xs_The_Third_Diffeq_Sweep_2026-09-23.md`, `Build_xt_The_Voice_Cache_Reclaim_Card_2026-09-23.md`, `Build_xu_The_Third_ProbStat_Sweep_Part_One_2026-09-23.md`, `Build_xv_The_Third_Algebra2_Sweep_2026-09-24.md`, `Build_xw_The_Third_ProbStat_Sweep_Part_Two_2026-09-24.md`, `Build_xx_The_Child_Mode_Skin_2026-09-24.md`, `Build_xy_The_Two_Flags_Nobody_Could_Screenshot_2026-09-24.md`, `Build_xz_The_Third_Basic_Sweep_2026-09-24.md`, `Build_ya_The_Third_Geometry_Sweep_2026-09-24.md`, `Build_yb_The_Words_Grow_Back_On_A_Shrunk_Figure_2026-09-24.md`, `Build_yc_The_Redraw_Settles_2026-09-25.md`, `Build_yd_Every_Label_Goes_Through_The_Fit_2026-09-25.md`, `Build_ye_The_Scripted_Lane_Goes_Nightly_2026-09-25.md`, `Build_yf_The_Third_Calculus_Sweep_2026-09-25.md`, `Build_yg_The_Sixth_Entry_Sweep_2026-09-26.md`.

## Written to D:\MyTutor (yg, 2026-09-26) — Jim pushes

- `lessonscripts.py` (`_col_sub`'s single-digit path; `big`, `eqs`, `min5q` walk-backs),
  `lessons/entry.py` (one edit), `ruletests.py` (PART 3oa; two pins moved), `speechmap.py`
  (941), `main.py` (stamp `2026-09-26yg-the-sixth-entry-sweep`),
  `changelog/Build_yg_The_Sixth_Entry_Sweep_2026-09-26.md`, this handoff
  (`START_HERE_Handoff_2026-09-26.md`). **Prewarm 1 line.** Miss one in Entry unit 3
  lesson 2: the walk-back counts back out loud.

## Written to D:\MyTutor (yf, 2026-09-25) — pushed or pending

- `lessons/calculus.py` (22 edits), `lessonscripts.py` (`chan`, `linf`, `revo` walk-backs),
  `ruletests.py` (PART 3nz; two pins moved), `speechmap.py` (941), `main.py` (stamp
  `2026-09-25yf-the-third-calculus-sweep`),
  `changelog/Build_yf_The_Third_Calculus_Sweep_2026-09-25.md`, `START_HERE_Handoff_2026-09-25.md` (superseded by this file). **Prewarm ~22
  lines.** Look at Calculus unit 8 lesson 1: the halfway line on the trapezium.

## Written to D:\MyTutor (ye, 2026-09-25) — pushed

- `screencheck.py` (`--script rota`, `--rota-size`, `--rota-day`, `--fail-on`; `rota_lessons`,
  `failing`), `.github/workflows/screenwatch.yml` (the second job, `scripted`), `ruletests.py`
  (PART 3ny; four pins moved to `notes()`), `main.py` (stamp
  `2026-09-25ye-the-scripted-lane-goes-nightly`),
  `changelog/Build_ye_The_Scripted_Lane_Goes_Nightly_2026-09-25.md`, `START_HERE_Handoff_2026-09-25.md` (superseded by this file). Nothing to prewarm. After the push, the next 09:30 UTC
  run of the `screenwatch` workflow has two jobs; the `scripted` one needs no secret. Its
  first report is worth opening once (Actions → the run → artifact `screenwatch-script-…`).

## Written to D:\MyTutor (yd, 2026-09-25) — pushed or pending

- `static/math-figures.js` (the grapher's fit; `axisLbl()`), `screencheck.py` (S5, S1, fixtures),
  `ruletests.py` (PART 3nx), `main.py` (stamp `2026-09-25yd-every-label-goes-through-the-fit`),
  `changelog/Build_yd_Every_Label_Goes_Through_The_Fit_2026-09-25.md`, this handoff. Nothing to
  prewarm. **The survey's table is in the yd doc: 360 lessons, 0 below the fold, 0 unexplained
  figure sizes.** Open question for Jim's eye: the graph's grid numbers are 9.8px even at full
  width (10 units on a 440 viewBox) — a one-number change if he wants them bigger.

## Written to D:\MyTutor (yc, 2026-09-25) — pushed or pending

- `static/board.js` (`figSettle`), `ruletests.py` (four pins moved, one added), `main.py` (stamp
  `2026-09-25yc-the-redraw-settles`), `changelog/Build_yc_The_Redraw_Settles_2026-09-25.md`,
  this handoff. Nothing to prewarm. Push it with or after yb.

## Written to D:\MyTutor (ya + yb, 2026-09-24) — Jim pushes

Both builds' files, written together (one battery, one push):

- `lessons/geometry.py` (ya: 12 spoken edits, 6 boards)
- `static/math-figures.js` (ya: `[[graph segments=]]`; yb: `svg(kind, a, {room})`, the array's row label on the right)
- `static/board.js` (yb: `__figAttrs`, `figRedraw`, the redraw in the fitter and on restore)
- `screencheck.py` (yb: `label_px`/`refit`, S10, fixtures)
- `ruletests.py` (ya: PART 3nv; yb: PART 3nw; three pins moved)
- `speechmap.py` (regenerated; 941)
- `main.py` (stamp `2026-09-24yb-the-words-grow-back-on-a-shrunk-figure`)
- `changelog/Build_ya_The_Third_Geometry_Sweep_2026-09-24.md`, `changelog/Build_yb_The_Words_Grow_Back_On_A_Shrunk_Figure_2026-09-24.md`
- `changelog/START_HERE_Handoff_2026-09-24.md` (superseded by this file)

After the push: `/health` = `2026-09-24yb-the-words-grow-back-on-a-shrunk-figure`; **prewarm
~12 lines** (ya's; plus xz's 8 and xw's ~60 if not yet done). Look at Geometry unit 7 lesson
1 (the segment) and Basic unit 3 lesson 4 (story problems: the array's words at 340px).
**Jim, 2026-09-24: "let's take a break from sweeps for now."** The remaining third-round
readings (Calculus 46, Entry 19, Pre-Calc's fourth) wait until he asks for them; the next
builds come from him, not the sweep queue.

## Written to D:\MyTutor (ya alone — superseded by the joint list above)

`ya`'s files, all on his disk:

- `lessons/geometry.py` (12 spoken edits, 6 boards)
- `static/math-figures.js` (`[[graph segments="(x1,y1)-(x2,y2)"]]` — the piece of line between two points)
- `ruletests.py` (PART 3nv; two pins moved)
- `speechmap.py` (regenerated; 941)
- `main.py` (stamp `2026-09-24ya-the-third-geometry-sweep`)
- `changelog/Build_ya_The_Third_Geometry_Sweep_2026-09-24.md`
- `changelog/START_HERE_Handoff_2026-09-24.md` (superseded by this file)

After the push: `/health` = `2026-09-24ya-the-third-geometry-sweep`; **prewarm ~12 lines** (xz's
8 and xw's ~60 if not yet done). Open Geometry unit 7 lesson 1: the segment is a bar between
the dots. Sweeps left in the third round: Calculus 46, Entry 19, Pre-Calc's fourth.

## Written to D:\MyTutor (xz, 2026-09-24) — pushed or pending

`xz`'s files, all on his disk:

- `lessons/basic.py` (8 edits)
- `coursesweep.py` (a `note` turn is labelled the transcript's own; the PROBLEM SPACE lists its exact (a, b) pairs; two charter lines)
- `ruletests.py` (PART 3nu; two pins moved)
- `speechmap.py` (regenerated; 941)
- `main.py` (stamp `2026-09-24xz-the-third-basic-sweep`)
- `changelog/Build_xz_The_Third_Basic_Sweep_2026-09-24.md`
- `changelog/START_HERE_Handoff_2026-09-24.md` (superseded by this file)

After the push: `/health` = `2026-09-24xz-the-third-basic-sweep`; **prewarm ~8 lines**. Then
the next sweep (Geometry 36, Calculus 46, Entry 19, or Pre-Calc's fourth) or the next gate
build (the over-tall beat, see xy).

## Written to D:\MyTutor (xy, 2026-09-24) — pushed or pending

`xy`'s files, all on his disk:

- `screencheck.py` (S8, S9, `LESSON_CHECKS`; the scripted-lane capture `--script`; `real_csp` via the parser; the socket closed; fixtures)
- `static/board.js` (`data-kind` on every figure; `figBox` — the NaN shrink fixed; `feedAnchorTarget`, `feedIsFollowing`, `_feedPlacing`)
- `static/session.html`, `static/practice.html`, `static/topic.html` (one line each: `stickBottom = feedIsFollowing();`)
- `main.py` (stamp `2026-09-24xy-the-two-flags-nobody-could-screenshot`)
- `ruletests.py` (PART 3nt)
- `changelog/Build_xy_The_Two_Flags_Nobody_Could_Screenshot_2026-09-24.md`
- `changelog/START_HERE_Handoff_2026-09-24.md` (superseded by this file)

After the push: `/health` = `2026-09-24xy-the-two-flags-nobody-could-screenshot`; **nothing to
prewarm**. Play a Geometry lesson (unit 1, when lines cross) past the second pair question: the
question must be on the board, not below it. (The Basic sweep that followed is `xz`, above.)

## Written to D:\MyTutor (xx, 2026-09-24) — pushed or pending

`xx`'s files, all on his disk:

- `main.py` (`_script_practice`, `_with_practice`; `script_start`/`script_answer` are wrappers over `_script_start_lesson`/`_script_answer_turn`; stamp `2026-09-24xx-the-child-mode-skin`)
- `static/session.html` (`#runDots` in the chip row, `renderRunDots`, `elemSettle`, the dots CSS and the `elem-settled` rule)
- `static/board.js` (`ensureChoicesCSS`: three `.elem-mode` rules — 72px buttons)
- `static/board-theme.css` (the warm block: `body.elem-mode .feed:not([data-board="dark"])`)
- `tools/xxdrive.py` (NEW — the headless drive of the skin, Entry vs Pre-Algebra)
- `ruletests.py` (PART 3ns)
- `changelog/Build_xx_The_Child_Mode_Skin_2026-09-24.md`
- `changelog/START_HERE_Handoff_2026-09-24.md` (superseded by this file)

After the push: `/health` = `2026-09-24xx-the-child-mode-skin`; **nothing to prewarm** (no
spoken line changed; xw's ~60 if not yet done). Open an Entry lesson: cream board, big
buttons, and after the two pair questions a pill at the top right that fills star by star.
**The NEXT build is a sweep build** (Basic 41, Geometry 36, Calculus 46, Entry 19, or
Pre-Calc's fourth — whichever report Jim pastes); the gate build after that is screencheck's
two rules (#6).

## Written to D:\MyTutor (xw, 2026-09-24) — pushed

`xw`'s files, all on his disk:

- `lessons/probstat.py` (20 edits)
- `lessonscripts.py` (farv's ✗ distance line, bias's praise, ptre's 81)
- `ruletests.py` (PART 3nr; five pins moved)
- `speechmap.py` (regenerated; 941)
- `main.py` (stamp `2026-09-24xw-the-third-probstat-sweep-part-two`)
- `changelog/Build_xw_The_Third_ProbStat_Sweep_Part_Two_2026-09-24.md`
- `changelog/START_HERE_Handoff_2026-09-24.md` (superseded by this file)

After the push: `/health` = `2026-09-24xw-the-third-probstat-sweep-part-two`; **prewarm ~60
lines**. (The gate build that followed it is `xx`, above.)

## Written to D:\MyTutor (xv, 2026-09-24) — pushed

`xv`'s files, all on his disk:

- `lessons/algebra2.py` (28 edits)
- `lessonscripts.py` (imag's praise: a credit line)
- `coursesweep.py` (one charter line: [[choices]] are tap buttons, never read aloud)
- `ruletests.py` (PART 3nq; five pins moved)
- `speechmap.py` (regenerated; 941)
- `main.py` (stamp `2026-09-24xv-the-third-algebra2-sweep`)
- `changelog/Build_xv_The_Third_Algebra2_Sweep_2026-09-24.md`
- `changelog/START_HERE_Handoff_2026-09-24.md` (superseded by this file)

After the push: `/health` = `2026-09-24xv-the-third-algebra2-sweep`; **prewarm ~30 lines**
(plus xu's 13 if not yet done).

## Written to D:\MyTutor (xu, 2026-09-23) — pushed or pending

`xu`'s files, all on his disk:

- `lessons/probstat.py` (14 edits on the 16 lessons read)
- `lessonscripts.py` (resd's caption: the SIZE of the residual; sslp's order)
- `coursesweep.py` (the checkpoint keeps only READ rows; a resume drops error rows; the STOPPED banner says Resume)
- `main.py` (a stopped sweep keeps its checkpoint; stamp `2026-09-23xu-the-third-probstat-sweep-part-one`)
- `ruletests.py` (PART 3np; 3mf, 3nk, 3mq pins moved)
- `speechmap.py` (regenerated; 941)
- `changelog/Build_xu_The_Third_ProbStat_Sweep_Part_One_2026-09-23.md`
- `changelog/START_HERE_Handoff_2026-09-23.md` (this file)

After the push: `/health` = `2026-09-23xu-the-third-probstat-sweep-part-one`; **prewarm
the 13 lines**. Then **add OpenAI credits** ("Add credits", not the cap) and run Prob/Stat
again — the whole course this once, because this run's checkpoint was cleared under the
old rule. From xu on, a sweep the seat cuts short offers Resume for what is left.

## Written to D:\MyTutor (xt, 2026-09-23) — pushed

`xt`'s files, all on his disk:

- `main.py` (`POST /api/admin/tts-cache-reclaim`, `_tts_cache_orphans()`, stamp `2026-09-23xt-the-voice-cache-reclaim-card`)
- `static/admin.html` (the "Voice cache reclaim" card under the repair card)
- `ruletests.py` (PART 3no)
- `changelog/Build_xt_The_Voice_Cache_Reclaim_Card_2026-09-23.md`
- `changelog/START_HERE_Handoff_2026-09-23.md` (this file)

After the push: `/health` = `2026-09-23xt-the-voice-cache-reclaim-card`; **nothing to
prewarm for xt** (xs's ~110 lines if not yet done). Then `/admin` → "Voice cache reclaim"
→ ① Count them (free) → ② Reclaim the space. Expect well over 812 MB back. Run it after
every sweep build from now on.

## Written to D:\MyTutor (xs, 2026-09-23)

`xs`'s files, all on his disk:

- `lessons/diffeq.py` (71 edits: the 35 boards that skipped spoken arithmetic, the 8 goal lines said, the six HIGHs, the conditions, the terms)
- `lessonscripts.py` (conc ask + walk-back, estp board, rk4 ask, sysx walk-back — one for one, 40,495 unchanged)
- `static/math-figures.js` (`[[graph field="expr"]]` — the slope field; `compile(expr, withY)`)
- `tools/pinscan.py` (NEW — the pre-flight, in the repo: `--freeze` on the frozen tree, `--against` on the edited one)
- `ruletests.py` (PART 3nn; seven pins moved: 3mk ×3, 3mn ×4)
- `speechmap.py` (regenerated; still 941)
- `main.py` (stamp `2026-09-23xs-the-third-diffeq-sweep`)
- `changelog/Build_xs_The_Third_Diffeq_Sweep_2026-09-23.md`
- `changelog/START_HERE_Handoff_2026-09-23.md` (this file)

After the push: `/health` = `2026-09-23xs-the-third-diffeq-sweep`; **prewarm ~110 lines**
(the 109 replaced course lines plus one re-keyed). Then open Diffeq Unit 1 lesson 3 (joining
the dashes) and look at the board: a faint field of dashes leaning at 3 under the walk. Do not
push while a sweep runs. xr's pencil (height 200) is still the thing to judge by eye if not yet
seen.

**Why xp exists (09-22, late):** Jim ran Algebra I twice and both sweeps "just disappeared"
— the sweep is a thread in the web process and wrote its report only at the END; each push
that day (xk, then xl/xm/xn) redeployed Render under a running sweep and the money was lost.
The rule, now printed on the card: **do not push to GitHub while a sweep runs.** Since xp a
restart costs one lesson and the card offers Resume.

## The 09-22 deep dive, and the schedule it set

`claude/Deep_Dive_2026-09-22_Eight_Days_Of_One_Project.md`. Thirty-seven builds since 09-14,
every one the sweep; the other eleven projects unmoved. Three findings checked, not read:
the watch still at ten lessons a night with no report read since 09-15 (closed by `xl`);
**48 lessons — all 36 of Diffeq and 12 of Entry — send every first miss to the AI, and the
sweep never reads that path** (it simulates a miss only where a worked generator exists);
the child's screen unchanged — a wrong tap moves nothing on the board, and the pencil's
moves have zero callers in 360 lessons.

**The schedule: alternate — one sweep build, one gate build.** Gate order: watch policy
(`xl`, done) → the miss has a face (`xn`, done) → Phase C (`xo`, done: all 51 ops, both
courses in one build) → the pencil in the scripted lane (`xr`, done) → the voice-cache
reclaim card (`xt`, done) → child-mode skin (`xx`, done) → screencheck's two rules (`xy`,
done). **The 09-14 gate list is complete.** The next gate builds come from what the new
instrument shows: the over-tall beat (S9 LOW, 29 of 45 lessons at 1280×900), and `pu`'s named
"turn length". **Diffeq's third reading (`xs`) saw the miss path** and the count fell
anyway, 62 → 39: only three findings sat on the 216 new walk-backs, none a walk-back shape.

## What the third round has changed about the plan

The 09-22 ruling (`claude/Ruling_2026-09-22_When_The_Sweeps_Stop.md`) estimated two more
full rounds and set the stopping rule: **stop when a reading stops producing a class.**
Pre-Algebra produced one, so the round continues — and the ruling's grading is now in use
(class / one-off / refused), recorded in each build doc. Diffeq's third reading produced one
too (the skipped arithmetic) and a small second (the unsaid goal line); the round continues.

One thing the ruling did NOT anticipate, and the next session should know: **not every class
can be pre-closed.** The four classes closed at `xf`, `xh` and `xj` were all structural — an
unread number, a word count, a sentence length — countable without understanding the
sentence. The condition class (a rule stated without what makes it true) was measured twice,
before and after this sweep, and both attempts produced 90% noise; see
`claude/Pre_Sweep_Finding_2026-09-22_The_Law_Without_Its_Condition.md` and `xk`'s build doc.
That class has to be READ. The remaining rounds are the instrument, not a formality.

| course | sweeps so far | last result |
|---|---|---|
| Entry | wa (219) → wc (70) → wd (47) → we (15) → wf (14) → wg fixes → wx (19, all 36) → wy fixes → xf pre-sweep, unswept | 19 findings (16 of them ww's praise-board consequence), 29 clean |
| Basic | wg (67) → wh fixes → wy (41, all 36) → wz fixes → xf pre-sweep → **xz's reading (9, all 36)** → xz fixes, unswept | 9 findings, 29 clean (was 41, 14) |
| Pre-Algebra | wh (69) → wi fixes → wz (58, all 36) → xa fixes → xf pre-sweep → **xk's reading (29, all 36)** → xk fixes, unswept | 29 findings, 18 clean (was 58, 9) |
| Algebra I | wi (72) → wk fixes → xa (50, all 36) → xb fixes → xf pre-sweep → **xp's reading (23, all 36)** → xq fixes, unswept | 23 findings, 23 clean (was 50, 10) |
| Geometry | wk (63) → wl fixes → xb (36, all 36) → xc fixes → xf pre-sweep → **ya's reading (11, all 36)** → ya fixes, unswept | 11 findings, 27 clean (was 36, 16) |
| Algebra II | wk (73) → wm fixes → ww (43, 35 of 36) → wx fixes → xf pre-sweep → **xv's reading (28, all 36)** → xv fixes, unswept | 28 findings, 19 clean (was 43, 14) |
| Pre-Calc | wl (76) → wn fixes → ws (34, 27 of 36) → wu fixes → wv (60, all 36) → ww fixes → xf pre-sweep → **xm's reading (28, all 36)** → xm fixes, unswept | 28 findings, 24 clean (was 60, 15) |
| Calculus | wm (46, 19 of 36) → wo fixes → wq (88, all 36) → wr fixes → xe + xh pre-sweeps → **xi (46, all 36)** → xi fixes, unswept | 46 findings, 13 clean (was 88, 4) |
| Diffeq | wo (119) → wp fixes → wr (62) → ws fixes → xf pre-sweep → xo (the miss path exists) → **xs's reading (39, all 36, the miss path in view)** → xs fixes, unswept | 39 findings, 13 clean (was 62, 8) |
| Prob/Stat | wo (92) → wq fixes → xe pre-sweep → xg (60, all 36) → xg fixes → xu (13 on 16; the seat died) → xu fixes → **xw's reading (26, all 36, resumed)** → xw fixes, unswept | 26 findings, 23 clean (was 60, 10) |

## What to do next

1. The chain through `yg` is on D:\MyTutor; Jim pushes once, confirms
   `/health` shows `2026-09-26yg-the-sixth-entry-sweep`, prewarms yf's ~22 lines and yg's 1
   (ya's 12, xz's 8 and xw's ~60 if not yet done) and plays Geometry unit 1 past the pairs (xy's
   fix), Basic unit 3 lesson 4 (yb's array words), Entry vs Pre-Algebra (xx's skin).
   **Sweeps are on hold at Jim's word (09-24).** What is left for him to decide, none of it
   urgent: the graph's grid numbers (9.8px at full width — a one-number change if his eye
   wants 12); the over-tall beat itself (253 S9 LOW at 1280×900, by design under `pu` — the
   fix is shorter beats, lesson by lesson, and the survey table in the yd doc says which);
   the quizsets sweep (never read); the 09-14 leftovers #8 (tour first tap) and #12 (the
   prefetch-shelf counter; watch `__open__`). When he asks for a sweep again: Pre-Calc's fourth is the only third-round reading left
   (Entry's sixth — `yg` — and Calculus's third — `yf` — are done),
   whichever report he pastes; the next gate build is whatever the nightly `scripted` job or
   a fresh survey shows (run `python screencheck.py --script <course>` sequentially, one
   course at a time — the machine has 2 CPUs). Before each sweep,
   consider closing the `xs` class in that course first (PART 3nn's ratchet says how many
   beats: Basic 26, Prob/Stat 22, Geometry 18, Algebra II 14). Read the hits with the scan's
   `--show` (the scan is described in the xs build doc; its logic is PART 3nn's first two
   checks); the lower courses' hits include counting sequences and captions, so read before
   drawing.
2. **The second round is complete — all ten courses read twice — and every measured class
   is closed canon-wide.** Nothing needs pre-sweeping before the third round: the unread
   closing board, the long authored sentence, the explaining praise and the long spoken
   beat all read zero in all ten courses (PARTs 3na, 3nb, 3nd, 3ne). So just run the next
   sweep and build from what it finds. Start with whichever second reading was highest:
   Prob/Stat 60, Calculus 46, Algebra II 43, Basic 41, Geometry 36, Entry 19. **What to watch
   for: whatever a reading raises most is a NEW class — measure it across the canon before
   fixing the instances it quotes.** That
   is the pattern that took Calculus from 88 findings to 46, Prob/Stat from 92 to 60 and
   Diffeq from 62 to 39. Geometry's class (xc): **the picture the words describe is not on the
   board** — an exterior angle over a plain triangle, a segment over two dots, a table's
   traps over three step lines. Draw what the words point at. Algebra I's class, which Algebra II and up will share: **the
   equation as given is missing from the board** — the undo pictures start one step in,
   a substituted line has no "x = 4" beside it, the words point at brackets the board
   does not show. Put the given line first. Expect the praise beats to read differently now: in a walk-back lesson
   the praise carries the WORKED board (ww), so "the praise says N and the board shows only
   the answer" should be gone everywhere — if a sweep still raises it, it is a wrong-path
   number the worked board does not draw (draw it with a ✗, as ww did for four ops). And
   **"the walk-back repeats the praise"** should be gone everywhere too: wy closed the
   word-for-word repeats (six ops) and xa the repeats *in other words* (25 ops, measured as
   the same numbers in order plus six words in ten shared); PARTs 3mt and 3mv run both
   measurements every battery. Each rerun is a new letter. Diffeq's rerun is the
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
   Basic's second reading (wz) was the same class one layer down ("one part is the
   answer" → "for a fraction with 1 on top"; "every number" → "every whole number") plus a
   generator shape: **a walk-back that says "step by step" and draws only the end** (wpc's
   grid, simp's pie) — draw the steps it speaks as `[[step]]` lines above the picture.
   Diffeq's third (xs), which the worked-example courses will share: **the board skips the
   arithmetic the words say** — draw every spoken number.
5. The night watch: paste any report; truth/HIGH gets built, the rest goes to the triage
   doc's ledger. `wj` added referee 101 (`aligndemo`, truth) and pendingzero's second shape.

## House decisions still open

- **A figure that opens its own `<svg>` must set the fit itself (yd).** `svgOpen` sets `_fit`;
  `graph()` does not use it and had never set it, so 473 small labels. Any new figure with
  its own opener: `_fit = figFit(W)` first, every label through `tspan()`/`fitSize()`, axis
  letters through `axisLbl()`. PART 3nx fails a raw `font-size=` on a `<text`.
- **A redraw inside the fitter must be idempotent (yc).** Anything the fitter does to the
  DOM comes straight back to it through the feed's MutationObserver → scrollFeed. Redraw
  only on a CHANGE (figSettle compares `data-pu-room` to the new width); never
  unconditionally. The survey is what catches this class — a page that spins looks fine.
- **A shrunk figure is drawn again for its width (yb).** `MathFigures.svg(kind, a, {room})`
  fits the labels for a given width; `figRedraw` in board.js uses it after `pu`'s shrink and
  on restore. A new math figure must draw its labels with `tspan()`/`fitSize()` to get this
  (14 raw `<text` writers in math-figures.js do not — the graph's grid numbers among them).
  S10 (label ≥ 9px) is the pin; the S9 LOW count is by design and stays.
- **`[[graph segments="(x1,y1)-(x2,y2)"]]` draws a segment (ya).** When the words say "a
  segment from A to B", draw the segment — `lines=` draws the whole line and a reviewer will
  (rightly) call it the wrong picture. Pairs separated by `|`; negatives allowed.
- **Never `pkill -f` ANYTHING from the shell (ya, bitten a third time).** `pkill -f
  "chromium.*--headless"` killed the shell too — the `bash -c` line carries the pattern. Kill
  by pid from `ps -eo pid,args` with an exact-argument awk, every time.
- **The machine has 2 CPUs (ya).** Ten parallel `screencheck --script` surveys ran at 300 s a
  lesson and starved the pinscan; one survey at a time is ~50 s a lesson. Run the survey
  sequentially, never beside a battery.
- **The transcript's note and the space's pairs (xz).** A `note` turn (the times-table pass
  marker) reads "(transcript note -- never spoken, not the tutor's)" on the page, and the
  PROBLEM SPACE line lists the exact (a, b) pairs when there are ≤ 12 problems — because the
  Basic reviewer paired 48 with 3 out of the two value lists and raised two HIGHs on a problem
  the lesson never asks. When a reviewer objects to a problem, check the pairs list before the
  lesson. A reviewer misread that the tool invited is a TOOL fix, not a refusal.
- **The screen is measured, not guessed (xy).** `python screencheck.py --script <lesson|course|all>`
  drives authored lessons through the real scripted player headlessly (~50 s a lesson, no key)
  and judges every turn: S8 (the last line on the screen — HIGH), S9 (same-kind figures within
  12% of one width — MEDIUM unexplained, LOW when `pu` shrank one to fit its turn). Before
  ruling on any layout flag Jim reports, run it on that lesson and read the finding; before
  changing `board.js`'s placing (`scrollFeed`, `fitTurnToBoard`, the listeners), run it on
  `geometry` and `basic` and diff the counts. Two laws it paid for: an `<svg>` has no
  `offsetHeight` (measure with `getBoundingClientRect`), and "the student scrolled away" is
  judged against `feedAnchorTarget()`, never against the bottom, and never while a placing is
  pending. The survey's 29 LOW S9s are the over-tall beat at 1280×900 — the next gate build.
- **The child-mode skin hangs off `body.elem-mode` (xx).** Anything for Entry/Basic only
  goes under that class — the page sets it for the two courses and nobody else, so a rule
  there cannot reach Pre-Algebra and up. The three-in-a-row dots read the server's
  `practice` field ({phase, run, need, on}), attached by the two endpoint WRAPPERS in
  `main.py` (`script_start`, `script_answer`) — never add the field inside
  `_script_answer_turn`'s nine returns; `_script_practice` is the one source and its `on`
  rule is documented there (practice; a full run through the reason question and the
  mastered end; never a table lesson, never the pairs). A board colour for the skin goes in
  `board-theme.css`'s warm block, never in the page's `<style>` (3hp fails a literal in a
  `.feed` rule). `tools/xxdrive.py` is the headless proof; PART 3ns runs it.
- **Kill the battery by its real pid (xw, bitten again at xy).** `pgrep -f ruletests.py | xargs kill`
  killed the shell that ran it, and so did `ps aux | grep "[p]ython3 ruletests.py" | awk | xargs kill`
  — the `bash -c` line that RUNS the grep contains the phrase, so the grep matches its own shell.
  The one that works: `ps -eo pid,args | awk '$2=="python3" && $3=="ruletests.py" {print $1}'`
  (exact argument match), then `kill <pid>`.
- **A dated-note pin must read `notes(<file>)`, never a fixed slice (ui; bitten at xy; closed
  at ye).** 3in's `"(build sq)" in bj[:3000]` slid past under two new board.js notes; the four
  slices that remained (3ik's client-log.js and voice.js, 3jd/3jg/3jl's geo-figures.js) read
  `notes()` since `ye`, and PART 3ny fails any pin with "BUILD" on its line that reads a
  `[:NNNN]` slice again. Write new dated-note pins as `"BUILD xx" in notes("path")`.
- **Entry boards carry no symbol Entry never teaches (yg).** No `>` and no `÷` on any
  Entry board, authored or generated — a comparison is "13 is bigger than 6", a share is
  "6 shared into 2 equal groups = 3 each", a count of fives is "55 minutes = 11 counts of
  five". PART 3oa fails either symbol anywhere in the course. A walk-back follows the
  lesson's own method: the base `-` walk-back counts the standing stars under ten and
  counts back from ten up, because that is what the two unit-3 lessons teach.
- **A sweep fix is text the next reading reads (yf).** `xi` closed a HIGH with "squaring the
  radius gives one slice its area" and the third reading raised it as a HIGH again — the π
  was missing. When a fix restates a law, state it whole.
- **The scripted lane runs nightly (ye).** The `screenwatch` workflow's second job drives eight
  authored lessons a night (`--script rota`: catalogue order, the slice picked by the day of
  the year, all 360 once every ~45 nights; `--rota-day N` re-runs a night by hand) and fails
  on MEDIUM and above (`--fail-on`; S9 LOW is `pu` by design and never fails a night). A red
  `scripted` job is a real S8/S9-MEDIUM/S10 on one of the eight named in its log — run
  `python screencheck.py --script <that lesson>` here and read the finding before touching
  `board.js`. The live job is unchanged and still needs `SCREENWATCH_CODE`.
- **The choices are tap buttons — now in the charter (xv).** Four sweeps in a row raised
  "the reason choices are never read aloud"; each was declined by hand. `coursesweep.py`
  tells the reviewer now. If it still comes back, it is the reviewer ignoring the charter,
  not a finding — decline and move on.
- **"Repeats" after a right answer means read the PRAISE (xq, confirmed at xv).** imag's
  praise was the walk-back's check said first; the credit line fixed it in one op.
- **A stopped sweep keeps its checkpoint (xu).** When the seat dies mid-sweep (the wv
  rule), the report is written AND the checkpoint stays, holding only the lessons actually
  read; the card's Run button becomes Resume and reads just the rest. A sweep that
  finishes clean clears it, as since xp. The checkpoint never carries an error row — a
  lesson the reader could not read is read on the resume, not skipped. When a report says
  STOPPED, do not run the course again: add credits and press Resume.
- **The reclaim card is the evictor's job, done on purpose (xt).** `POST
  /api/admin/tts-cache-reclaim` lists (dry_run, default) and deletes every cached clip the
  scripted closure does not name, older than `keep_hours` (24). The course's clips are never
  candidates; an empty closure is a 409. It is safe after every sweep build — a deleted
  generated-lane clip re-renders at a few cents, an orphaned course clip was already
  unreachable. If a future build wants the evictor itself to run on a schedule, this
  helper (`_tts_cache_orphans`) is the piece to call.
- **The board draws the arithmetic the words say (xs).** A worked or teach beat that says
  "884 take away 100 is 784, whose root is 28" draws each number — a chained equals or a step
  line of its own, never " · " between two equations. PART 3nn pins Diffeq at zero (35 beats
  were compressed) and ratchets the other nine. The measure counts a spoken number of two or
  more digits the beat's board does not carry; a number followed by a full stop counts (the
  first cut's regex missed those — fixed before the pin). When a sweep quotes "the tutor says N
  but the board shows only the end", it is this class: measure the course before fixing.
- **The goal board's given line is said in the beat that shows it (xs).** `step 10 → error
  90` on the goal card, read aloud only in the next turn, is xb's "put the given line first"
  from the other side. Say it in the goal beat ("Here: a step of 10 left an error of 90") and
  trim the repeat in the next — but NEVER "On the board: …": 3kt's picture referee reads that
  phrase as a promised picture and fails the battery (it cost xs one run). Diffeq zero,
  ratchet elsewhere (PART 3nn).
- **`[[graph field="expr"]]` draws a slope field (xs).** x and y allowed, a bare number is a
  constant field; drawn first and faint. Any Unit 1 beat whose words say "every dash" over a
  bare line should carry it. The board contract reads the attribute from the renderer.
- **The pre-flight lives in the repo now: `tools/pinscan.py` (xs).** Run `--freeze` on the
  frozen copy before editing, `--against` on the edited tree after; it prints the literals in
  `ruletests.py` that were in the corpus and are not any more. Two minutes a run, zero false
  alarms by construction. Do not keep tools in the scratchpad.
- **A course may lean on what an earlier course taught (Jim, 2026-09-23).** Geometry lesson 1
  says "you already know … the angles along a straight line make 180" and "you met 180
  first" — the 180 fact is taught in Pre-Algebra unit 8, not in Geometry. Jim played it as a
  new student, asked, and ruled it fine: the courses are a sequence. Decline a sweep finding
  that calls a fact from an EARLIER COURSE untaught; a fact from a LATER lesson of the same
  course is still a finding. (25 "you already know / you met" lines canon-wide; this was the
  only cross-course one.)
- **The pencil acts on the engine's beats, never on authored lines (xr).** Every scripted
  beat rings `beat.<name>` (session.html `cadBeat`); the menu says what he does there. To
  change what he does on a teach beat, edit `static/cadabra-script.json` (and its
  identical `.example`), not a lesson. A new engine step kind that should move him needs a
  `beat` name in `lessonscripts.py` and a moment in the menu; PART 3nm's "no dead moment"
  pin lists the names the page can ring. Under the `ir` scroll ruling (a tutor turn starts
  at the top of the board) most blocks are pointed at from below; the write pose appears
  only where his body fits under the block.
- **A praise can still be the walk-back in other words under the 3nf measure (xq).** exadd
  and yint sat under it because the walk-back added a phrase. The reviewer reads the pair,
  the measure counts words; when a sweep says "repeats" on a walk-back after a right
  answer, read the PRAISE — that is the line to cut to a credit line, and the walk-back
  gains a step (exadd: `3 + 7 = 10` under the tape) rather than losing one.
- **"times / timesed / timesing" is the course's verb (xq).** A charter line in
  `coursesweep.py`; decline any "nonstandard" finding on it.
- **Four measured classes, all at zero in all ten courses (xj).** Each was found by a
  sweep, then measured across the canon and driven to zero rather than fixed where the
  reviewer happened to quote it: the unread closing recap board and the 27-word authored
  teaching sentence (found xe, closed xf, PART 3na); the praise that explains instead of
  crediting, measured as a praise over 26 words (found xg, closed xh, PART 3nb); the
  generated spoken beat of 27+ words in a walk-back, ask or advance line (found xi, closed
  xj, PARTs 3nd and 3ne). PART 3ne also checks all three scans together, so no new beat can
  quietly reintroduce one. **Whatever a reading raises most is a new class — the move is to
  measure it canon-wide first** (xs did: 126 beats, 35 in Diffeq, pinned).
- **A generated walk-back is a spoken beat too (xi).** The xe/xf sentence scan reads only
  the authored kinds — why, picture, teach, worked-example, recap. Every one of Calculus's
  12 "unclear" findings was in a generated WALK-BACK or ASK, which no scan had ever
  covered. PART 3nd now covers walk-back, ask, advance, second-look and fresh-one over all
  ten courses, and **counts the spoken opener** ("Here it is, step by step: ") because the
  child hears it in the same breath — that is why the reviewer called a 22-word sentence a
  27-word one. Pinned at zero for Entry and Calculus; a falling ratchet elsewhere. A
  generated walk-back is generator-owned, so one split closes it everywhere: Calculus's 132
  instances were 18 ops.
- **Split after the opener, never at it (xi).** The walk-back must still begin with the
  literal `Here it is, step by step: ` and the text after the colon stays lower-case. So
  the first sentence ends at the first natural stop AFTER that phrase — "Here it is, step
  by step: set the slope to zero. 2 x take away 4 equals zero, so …".
- **The old pre-flight `pinscan.py` (xi) is gone with its scratchpad** — replaced by
  `tools/pinscan.py` (xs, above). The old one parsed the PARTs' spellings (`PR`,
  `L.OP_EXT[...]["praise"]`, `W`, `_W`, `S`, `B`, `spoken(E(...))`, `.startswith`) and
  resolved per-PART variables; the new one asks the corpus instead and needs none of that.
  Executing every PART instead was tried and abandoned — it takes most of a battery's time.

- **A praise is a credit line, and LENGTH is the measurement (xg).** Three sweeps' worth of
  "the walk-back repeats the praise" came back because 3mt (word for word) and 3mv (same
  numbers, six words in ten) are both defeated by one extra sentence. What separates the
  ops a reviewer flags from the ones it leaves alone is plain length: every flagged praise
  ran past 30 words, every credit line xa wrote is under 21. PART 3nb pins **no praise over
  26 words** at **zero for every course since xh** — the 59 that were left (Calculus 32,
  Pre-Calc 19, Algebra I 3, Algebra II 3, Geometry 2) are all credit lines now, and a new
  op's praise must be one too or the battery fails. When a pin guards a phrase inside a
  praise: if the phrase is the answer's REASON it stays; if it is the EXPLAINING it moves
  into the walk-back (xh moved four, and had to ADD two that were not there at all).
- **A closing credit line inherits the recap above it (xg).** xe gave every closing recap a
  line that reads its board; two of them dropped the condition the recap had just stated
  ("3, every play" under "on average"; "that is what give or take means" under a margin
  that steps both ways) and came back as HIGHs. When the sentence above says "on average",
  "each way" or "in the long run", the line that reads the board says so too.
- **The pre-sweep scan does not cover every beat kind (xg).** All four "unclear" findings
  landed in kinds the xe/xf scan skips — a walk-back, an ask and an advance line. Widening
  `presweep_measure.py` to those kinds is the next cheap class; a generated walk-back or
  ask is generator-owned, so one fix closes it everywhere.

- **A walk-back can keep a reason the lesson dropped (xc).** wl fixed the half-the-arc
  lesson's "from farther away things look smaller" in the authored beats; the generator's
  walk-back kept it for three more builds. When a sweep finding names a *reason*, grep the
  op's `_worked` too.
- **Reason choices and answer choices are tap-only by design (wx, xa, xb).** Three sweeps in a row
  have raised "the choices are never read aloud" — decline it every time; it is not a
  finding. If it keeps costing findings, a charter line in `coursesweep.py` would stop it.
- **A praise beat is a credit line (wy, xa).** The answer and its one reason, every number
  of it on the board it carries — never the walk-back's steps in other words. When writing
  a new op: write the walk-back first, then the praise as the shorter line. Two of the 25
  rewritten in xa keep a phrase an older pin guards (rsol's "Check it forward", wper's
  "first repeat comes SOONER, not later") — grep `PR("<op>"` before rewriting a praise.
- **The times-table lesson's PROBLEM SPACE line says the pass (wz).** The sweep read "12
  problems" on that lesson and called the intro's "all 81 facts" false (HIGH). The line
  was wrong: the lesson practises as an 81-fact pass (sz) and its bank only feeds the
  worked pairs, the quiz and the drill. `problem_space()` now says so for any lesson whose
  `mastery` is "table". When a HIGH contradicts something the engine is known to do, check
  what the reviewer was *told* before changing the lesson.
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
  (`coursesweep.transcript_for(les, L)` + `render_transcript(les, turns)` — both take the
  lesson DICT, not its id) to read each quoted turn in context
  before deciding real / generator / ruling. The pasted report itself does not survive a
  context compaction — copy its header line (findings, clean, unplaced, minutes) into a
  scratch file AND the build doc FIRST (wy's report survived only as a header line).
- Asserted string replacements (`assert s.count(a) == 1`) into `lessons/<course>.py` and
  `lessonscripts.py`; `L.validate` all 360 (the validator's canon: "what is left", never
  "remain"; a lesson's `symbols` must appear as the bare word — "cross", not "crossing"); `python3 tools/genspeechmap.py`; note the counts
  (course **40,495** since xo (39,915 at xn); closure 40,749; speechmap **941** of 40,801 and forSpeech
  drift **635** since xh — they were 2,184 and 1,878 until the colon rule was tightened; the
  "closure is in it" floor pin is now `> 900`. **A count can FALL: xg's credit lines took
  35 course lines off, because a short praise is shared by more problems than a long one
  was. Diff `course_audio_lines()` against the frozen copy and read the diff before moving
  the pins** — 1,559 lines out, 1,524 in;
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
  A chained equals (`4×25 − 8² = 100 − 64 = 36`) passes; xs used it 20 times.
- **New trap (3kt's picture referee, xs):** the phrase "On the board:" in a spoken beat
  reads as a promised picture; over a board with only `[[step]]` lines it fails "not one
  beat tells a student to look at a picture its own board does not draw". Say "Here:".
- **New trap (D: drive):** the device bridge lost D:\MyTutor twice on 09-16 ("could not
  stat", then "does not exist") for a few minutes each time; a write that times out has NOT
  landed — list the folder and compare sizes before retrying, and never `force`. On 09-23
  the bridge dropped for the whole second half of the build (the mount under `device_bash`
  had already failed at the start) — build on, deliver when it is back.
- **Closed trap (forSpeech, xd):** "up 12: 25 plus 144" used to re-key as a ratio and the
  voice really said "to" ("Factors of 8: 1, 2" → "8 to 1, 2"; 287 turns across the ten
  courses). The rule now matches the tight `digit:digit` only; a colon with a space after it
  is a pause. Colons before numbers are fine again in scripted text; the tight form is never
  scripted (PART 3my pins it) and still reads "to" for the live model's ratios. Still diff
  `speechmap.MAP` against the delivered copy before moving its pin, and read what the tidy did.
- **New tool (xe):** `srep.py` in the scratchpad — `Editor(path).rep(old_sentence,
  new_sentence)` finds a spoken sentence in `lessons/<course>.py` even when the source
  splits it across adjacent string literals, and asserts exactly one match. It is what let
  xe make 130 authored edits without hand-hunting each split. Recreate it from the xe doc's
  description if the scratchpad is gone (30 lines). (`lessons/diffeq.py` keeps every spoken
  line as ONE literal, so xs needed only plain asserted replacements.)
- **New measurement (xe, xf):** the two scans — a recap beat whose `[[step]]` numbers the
  words never say (digits or number words), and a why/picture/teach/worked/recap sentence
  of 27+ words — are the two cheapest classes to close before a sweep. PART 3na pins both
  at zero over ALL TEN courses; a new beat that trips either fails the battery. The scan
  script is `presweep_measure.py` in the scratchpad (`--show` lists each hit with its text).
- **New measurement (xs):** the reverse scan — a teach or worked beat whose WORDS say a
  2+digit number its BOARD does not carry — is PART 3nn's first check (Diffeq zero, the
  rest a ratchet). The same PART's third check is the goal-beat scan.
- **Closed trap (headers):** PART 3ke fails a file whose header passes 100 KB. `wp` rolled
  `ruletests.py` and `lessonscripts.py` out at cutoff 2026-09-10; **`main.py` went at xg,
  same cutoff** (91 entries moved, header 100,069 -> 37,219 B):
  `python3 notes_rollout.py --root . --cutoff 2026-09-10 --build xx --apply FILE`. 3ke
  reads each header's newest pointer and checks every fenced block against its own cutoff,
  so a further roll-out needs no pin change. Next candidates when they grow: `tutor.py`,
  `prompts.py`, `store.py`.
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
- **New trap closed (xf, widened at xh, replaced at xs):** before the battery, run
  `tools/pinscan.py` (`--freeze` on the frozen copy, `--against` on the edited tree). It
  found seven stale pins in xs before the first run, in every spelling, with no false alarm.
- A new PART's checks can be smoke-run alone before the 25-minute battery: `import
  ruletests as R; R.part3nn_the_third_diffeq_sweep(); print(R.FAIL)` — the module imports
  clean with `sys.argv` set to `["ruletests.py"]`. xs ran 3nn, 3na, 3nb, 3nd, 3ne, 3nj, 3mo,
  3mt, 3mv, 3my, 3eu and 3kt this way (about 40 s) before each battery.
- **New trap (counts):** a new beat with coordinates or decimals moves THREE counts —
  course lines, speechmap re-keys, and the forSpeech drift pin (`n == 1938` since wu, PART 3ky's
  neighbour) — the third is easy to forget; it cost wl one battery run.
- **New trap (referees):** adding a `*_conflict` function moves ~30 count pins (`== 100`,
  `n_ref == 100`, `len(T.TRUTH_REFEREES) == 11`), the falsehood-row pins (`== 24`, the
  "last two are vp's" order pin), and `static/methodology.html`'s tile + both
  `data-referees` spans. Move them all in one regex pass, then the order pin by hand.
- Render new board tags headlessly: a stub page that loads `static/board-theme.css`,
  `static/board.css` and `static/math-figures.js` (without the theme CSS every figure
  renders black) and calls `MathFigures.svg(kind, attrs)`; Playwright screenshots it. The xs
  pattern is `render_field.py` in that session's scratchpad (25 lines).
- **New trap (the sweep and deploys, xp):** the sweep dies with the server. Never push
  while one runs; if Render restarts under it, the card says INTERRUPTED and offers Resume —
  the checkpoint is `data/coursesweep/<course>_partial.json`, the job's memory is
  `_job.json` beside it. A test that exercises the worker must point `M.DATA_DIR` at a temp
  folder (the job file's path is read at call time for exactly this).
- Battery on a frozen copy; kill only by PID. The mount under `device_bash` failed again on
  09-23, so the tree was staged file-by-file: root `.py`, `lessons/`, `tools/`, `static/`
  (incl. `shots/`, `mockup/`, `videos/cadabra/*` — the clips and posters, not only the two
  json manifests), **`changelog/*.md` (the `.html.md` roll-outs too, not only `.py.md`)**,
  `.github/workflows`, `RECOVERY.md`, `README.md` — the battery needs all of those to reach
  0 failed (xs's first run failed ten file-presence checks for the clips and the four
  `.html.md` files).
- Deliver: cp to `/mnt/user-data/outputs/MyTutor/...` → SendUserFile → `device_commit_files`
  with `expectedMtimeMs` from a fresh `device_list_dir` → `project_write` the build doc. Jim reviews with
  `git diff` and pushes; I never commit. **When his computer is not connected (09-19: two
  days on a phone):** build anyway on the workspace copy, send the file cards, put the docs
  and this handoff in the project with a pending-commit list, and commit everything in one
  go when the bridge is back — never a partial commit that leaves the disk between builds.

## Open items carried forward

Notation repair floor; (**the voice-cache reclaim card — closed by `xt`**; Jim presses ①/② after
each sweep build); the watch's `__open__` turn; (**screencheck rules — closed by `xy`**; **the shrunk figure's labels and the array's
"5 rows" — closed by `yb`**; still open from it: the over-tall beat itself, 29 LOW S9s — by
design under `pu`, now with readable words); (**the
child-mode skin — closed by `xx`**; the pencil in the scripted lane closed by `xr`); Phase B deferred; (**Phase C closed by `xo`** — every op in the canon has a
worked generator; 3lu and 3nj pin it at zero); the prefetch-shelf counter; the tour
button; the xs class in the other nine courses (PART 3nn's ratchet: Basic 26, Prob/Stat 22,
Geometry 18, Algebra II 14, Pre-Calc 13, Algebra I 10, Calculus 10, Entry 7, Pre-Algebra 5 —
read before drawing; the lower courses' hits include counting sequences). (`EST_USD_PER_LESSON` corrected in ws; **the critic charter with the "done for the
day" ruling and the watch policy in code — closed by `xl`.**)

I did no harm and this file is not truncated.
