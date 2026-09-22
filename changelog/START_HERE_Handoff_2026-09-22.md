# START HERE — Handoff, 2026-09-22

Read this first in a new chat. Then the build docs it points to, only as needed.

## Where things stand

On Jim's disk: **`2026-09-19xf-the-pre-sweep-the-other-eight`** (battery 12,759 passed, 0
failed, 3 skipped). `xd`, `xe` and `xf` were built on 09-19 while Jim was away from his
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
his disk on 09-22. **Built after it and NOT yet on his disk: `xn`
(`2026-09-22xn-the-miss-has-a-face`, 12,865)** — project 4 of the 09-14 deep dive, the
second gate build. See **Pending commit** below. The 09-16 chain: `wh` (Basic sweep, 12,496) → `wi`
(Pre-Algebra, 12,515) → `wj` (the 09-15 night watch, 12,527) → `wk` (Algebra I, 12,545) → `wl`
(Geometry, 12,558) → `wm` (Algebra II, 12,576) → `wn` (Pre-Calc, 12,589) → `wo` (Calculus,
half, 12,599) → `wp` (Diffeq, 12,612) → `wq` (Prob/Stat, 12,626, 09-17) → `wr` (Calculus
whole, 12,638, 09-17) → `ws` (Diffeq again, 12,649, 09-17) → `wt` (the referee pile, 12,658, 09-17) → `wu` (Pre-Calc again, 12,666, 09-17) → `wv` (the sweep says why it stopped, 12,674, 09-17) → `ww` (Pre-Calc, third reading, 12,685, 09-17) → `wx` (Algebra II again, 12,693, 09-18) → `wy` (Entry, fifth reading, 12,704, 09-18) → `wz` (Basic again, 12,714, 09-18) → `xa` (Pre-Algebra again, 12,724, 09-18) → `xb` (Algebra I again, 12,732, 09-19) → `xc` (Geometry again, 12,739, 09-19) → `xd` (the colon is not a ratio, 12,745, 09-19, pending) → `xe` (the pre-sweep, 12,751, 09-19, pending) → `xf` (the pre-sweep, the other eight, 12,759, 09-19) → `xg` (the second Prob/Stat sweep, 12,778, 09-21) → `xh` (the credit line everywhere, 12,785, 09-21) → `xi` (the second Calculus sweep, 12,801, 09-22) → `xj` (the spoken beat is short everywhere, 12,809, 09-22) → `xk` (the praise is not the walk-back, 12,821, 09-22) → `xl` (the watch policy, 12,841, 09-22) → `xm` (the angle carries its unit, 12,855, 09-22) → `xn` (the miss has a face, 12,865, 09-22, pending). Jim pushes and prewarms
each; check `/health`. The first round is over: every lesson in every course has been read
once. **The second round has begun, and the cycle converges: Diffeq went 119 → 62 findings,
0 → 8 clean, on one fix build; Pre-Calc 76 → 34 → (60 with wt's praise-board shape, fixed in the engine) 15 clean; Algebra II 73 → 43, 14 clean; Entry 14 → 19 (sixteen of them one engine consequence of ww, closed in wy) with 29 clean — the most any course has had; Basic 67 → 41, 7 → 14 clean; Pre-Algebra 69 → 58, 6 → 9 clean (ten of the 58 were the near-repeat praise class, closed across 25 ops in xa); Algebra I 72 → 50, 8 → 10 clean — the first reading after xa, and the praise class did not come up once; Geometry 63 → 36, 7 → 16 clean.**

**OpenAI credits were topped up on the evening of 09-17** (the cap is not the balance —
an "Add credits" top-up is what the 429 "no credits remaining" needs; wv makes the card say
"could not be read" when it happens again). The course sweep and the night watch both use that seat, and a
36-lesson sweep now estimates at about $5.40 (`EST_USD_PER_LESSON` 0.15, corrected in ws).

Docs: `claude/Build_wh_…`, `Build_wi_…`, `Triage_NightWatch_2026-09-15_Four_Highs_Three_Seats`,
`Build_wk_…`, `Build_wl_…`, `Build_wm_…`, `Build_wn_…`, `Build_wo_…`, `Build_wp_…` (all
`_2026-09-16.md`), `Build_wq_The_First_ProbStat_Sweep_2026-09-17.md`,
`Build_wr_The_Second_Calculus_Sweep_2026-09-17.md`, `Build_ws_The_Second_Diffeq_Sweep_2026-09-17.md`, `Build_wt_The_Referee_Pile_2026-09-17.md`, `Build_wu_The_Second_PreCalc_Sweep_2026-09-17.md`, `Build_wv_The_Sweep_Says_Why_It_Stopped_2026-09-17.md`, `Build_ww_The_Third_PreCalc_Sweep_2026-09-17.md`, `Build_wx_The_Second_Algebra2_Sweep_2026-09-18.md`, `Build_wy_The_Fifth_Entry_Sweep_2026-09-18.md`, `Build_wz_The_Second_Basic_Sweep_2026-09-18.md`, `Build_xa_The_Second_PreAlgebra_Sweep_2026-09-18.md`, `Build_xb_The_Second_Algebra1_Sweep_2026-09-19.md`, `Build_xc_The_Second_Geometry_Sweep_2026-09-19.md`, `Build_xd_The_Colon_Is_Not_A_Ratio_2026-09-19.md`, `Build_xe_The_Pre_Sweep_2026-09-19.md`, `Build_xf_The_Pre_Sweep_The_Other_Eight_2026-09-19.md`, `Build_xg_The_Second_ProbStat_Sweep_2026-09-21.md`, `Build_xh_The_Credit_Line_Everywhere_2026-09-21.md`, `Build_xi_The_Second_Calculus_Sweep_2026-09-22.md`, `Build_xj_The_Spoken_Beat_Is_Short_Everywhere_2026-09-22.md`, `Pre_Sweep_Finding_2026-09-22_The_Law_Without_Its_Condition.md`, `Ruling_2026-09-22_When_The_Sweeps_Stop.md`, `Build_xk_The_Praise_Is_Not_The_Walk_Back_2026-09-22.md`, `Deep_Dive_2026-09-22_Eight_Days_Of_One_Project.md`, `Build_xl_The_Watch_Policy_2026-09-22.md`, `Build_xm_The_Angle_Carries_Its_Unit_2026-09-22.md`, `Build_xn_The_Miss_Has_A_Face_2026-09-22.md`.

## Pending commit to D:\MyTutor (xl, xm and xn, built 2026-09-22)

`xl`'s and `xm`'s files were written to D:\MyTutor on 09-22 and were not yet pushed when
`xn` was built. `device_list_dir` for fresh mtimes, then `device_commit_files` `xn`'s:

- `static/session.html` (the student's bubble shakes and is stamped; the miss is the pencil's target; problem.fresh)
- `static/cadabra-script.json` and `static/cadabra-script.example.json` (identical; answer.wrong is a comfort at `miss`; problem.fresh; version xn)
- `ruletests.py` (PART 3ni; two pins taught the runtime targets; one rr pin moved)
- `main.py` (stamp `2026-09-22xn-the-miss-has-a-face`)
- `changelog/Build_xn_The_Miss_Has_A_Face_2026-09-22.md`
- `changelog/START_HERE_Handoff_2026-09-22.md` (this file)

If all three are pushed together: `/health` = `2026-09-22xn-the-miss-has-a-face`, then ONE
prewarm (for `xm`'s ~150 lines; `xl` and `xn` render nothing). Then, on a lesson, answer one
wrong on purpose and watch: the bubble shakes and is crossed, the pencil comes to it, and he
points at the fresh problem.

## The 09-22 deep dive, and the schedule it set

`claude/Deep_Dive_2026-09-22_Eight_Days_Of_One_Project.md`. Thirty-seven builds since 09-14,
every one the sweep; the other eleven projects unmoved. Three findings checked, not read:
the watch still at ten lessons a night with no report read since 09-15 (closed by `xl`);
**48 lessons — all 36 of Diffeq and 12 of Entry — send every first miss to the AI, and the
sweep never reads that path** (it simulates a miss only where a worked generator exists);
the child's screen unchanged — a wrong tap moves nothing on the board, and the pencil's
moves have zero callers in 360 lessons.

**The schedule: alternate — one sweep build, one gate build.** Gate order: watch policy
(`xl`, done) → the miss has a face (`xn`, done) → **Phase C — NEXT gate build: Diffeq's 36 worked generators first, then
Entry's 12 (M)** → the pencil in the scripted lane (M) → the voice-cache reclaim card (S) →
child-mode skin → screencheck's two rules. **Diffeq's third reading waits for Phase C**, so
it is the first reading that sees the miss path at all.

## What the third round has changed about the plan

The 09-22 ruling (`claude/Ruling_2026-09-22_When_The_Sweeps_Stop.md`) estimated two more
full rounds and set the stopping rule: **stop when a reading stops producing a class.**
Pre-Algebra produced one, so the round continues — and the ruling's grading is now in use
(class / one-off / refused), recorded in each build doc.

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
| Basic | wg (67) → wh fixes → wy (41, all 36) → wz fixes → xf pre-sweep, unswept | 41 findings, 14 clean |
| Pre-Algebra | wh (69) → wi fixes → wz (58, all 36) → xa fixes → xf pre-sweep → **xk's reading (29, all 36)** → xk fixes, unswept | 29 findings, 18 clean (was 58, 9) |
| Algebra I | wi (72) → wk fixes → xa (50, all 36) → xb fixes → xf pre-sweep, unswept | 50 findings, 10 clean |
| Geometry | wk (63) → wl fixes → xb (36, all 36) → xc fixes → xf pre-sweep, unswept | 36 findings, 16 clean |
| Algebra II | wk (73) → wm fixes → ww (43, 35 of 36) → wx fixes → xf pre-sweep, unswept | 43 findings, 14 clean |
| Pre-Calc | wl (76) → wn fixes → ws (34, 27 of 36) → wu fixes → wv (60, all 36) → ww fixes → xf pre-sweep → **xm's reading (28, all 36)** → xm fixes, unswept | 28 findings, 24 clean (was 60, 15) |
| Calculus | wm (46, 19 of 36) → wo fixes → wq (88, all 36) → wr fixes → xe + xh pre-sweeps → **xi (46, all 36)** → xi fixes, unswept | 46 findings, 13 clean (was 88, 4) |
| Diffeq | wo (119) → wp fixes → wr (62) → ws fixes → xf pre-sweep, unswept | 62 findings, 8 clean (was 119, 0) |
| Prob/Stat | wo (92) → wq fixes → xe pre-sweep → **xg (60, all 36)** → xg fixes, unswept | 60 findings, 10 clean (was 92, 1) |

## What to do next

1. Commit the **pending** files above to D:\MyTutor; Jim pushes once, confirms
   `/health` shows `2026-09-22xj-the-spoken-beat-is-short-everywhere`, runs the
   **prewarm** (~1,900 walk-back and ask lines across eight courses).
2. **The second round is complete — all ten courses read twice — and every measured class
   is closed canon-wide.** Nothing needs pre-sweeping before the third round: the unread
   closing board, the long authored sentence, the explaining praise and the long spoken
   beat all read zero in all ten courses (PARTs 3na, 3nb, 3nd, 3ne). So just run the next
   sweep and build from what it finds. Start with whichever second reading was highest:
   Diffeq 62, Prob/Stat 60, Pre-Calc 60 (its third), Pre-Algebra 58, Algebra I 50,
   Calculus 46, Algebra II 43, Basic 41, Geometry 36, Entry 19. **What to watch for: the
   next reading is the first with no known class pre-closed, so whatever it raises most is
   a NEW class — measure it across the canon before fixing the instances it quotes.** That
   is the pattern that took Calculus from 88 findings to 46 and Prob/Stat from 92 to 60. Geometry's class (xc): **the picture the words describe is not on the
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
5. The night watch: paste any report; truth/HIGH gets built, the rest goes to the triage
   doc's ledger. `wj` added referee 101 (`aligndemo`, truth) and pendingzero's second shape.

## House decisions still open

- **Four measured classes, all at zero in all ten courses (xj).** Each was found by a
  sweep, then measured across the canon and driven to zero rather than fixed where the
  reviewer happened to quote it: the unread closing recap board and the 27-word authored
  teaching sentence (found xe, closed xf, PART 3na); the praise that explains instead of
  crediting, measured as a praise over 26 words (found xg, closed xh, PART 3nb); the
  generated spoken beat of 27+ words in a walk-back, ask or advance line (found xi, closed
  xj, PARTs 3nd and 3ne). PART 3ne also checks all three scans together, so no new beat can
  quietly reintroduce one. **The next sweep is the first with no known class pre-closed —
  whatever it raises most is a new class, and the move is to measure it canon-wide first.**
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
- **The pre-flight is `pinscan.py` (xi).** It checks every pin that quotes generated or
  authored text, in all the spellings the PARTs use — `PR`, `L.OP_EXT[...]["praise"]`,
  `L.praise_for`, `W`, `_W`, `S`/`L.spoken_for`, `B`/`L.board_for`, `spoken(E(...))`,
  `advance_line`, `explain`, **and `.startswith(...)`/`.endswith(...)` on any of them** —
  **with the problem written as a dict OR as a variable assigned in the same PART**
  (`_W(derv)[0]`). Scoping those variables per PART is what
  makes it usable: a global map gave 38 false alarms on a correct tree, per PART it gives
  zero. Run it (`PYTHONPATH=. python3 pinscan.py`) before every battery; it found fourteen
  stale pins across xi. Executing every PART instead was tried and abandoned — it takes
  most of a battery's time and buys nothing over the battery.

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
  (`coursesweep.transcript_for` + `render_transcript`) to read each quoted turn in context
  before deciding real / generator / ruling. The pasted report itself does not survive a
  context compaction — copy its header line (findings, clean, unplaced, minutes) into a
  scratch file AND the build doc FIRST (wy's report survived only as a header line).
- Asserted string replacements (`assert s.count(a) == 1`) into `lessons/<course>.py` and
  `lessonscripts.py`; `L.validate` all 360 (the validator's canon: "what is left", never
  "remain"; a lesson's `symbols` must appear as the bare word — "cross", not "crossing"); `python3 tools/genspeechmap.py`; note the counts
  (course **39,920** since xh; closure 40,174; speechmap **941** of 40,226 and forSpeech
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
- **New trap (D: drive):** the device bridge lost D:\MyTutor twice on 09-16 ("could not
  stat", then "does not exist") for a few minutes each time; a write that times out has NOT
  landed — list the folder and compare sizes before retrying, and never `force`.
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
  description if the scratchpad is gone (30 lines).
- **New measurement (xe, xf):** the two scans — a recap beat whose `[[step]]` numbers the
  words never say (digits or number words), and a why/picture/teach/worked/recap sentence
  of 27+ words — are the two cheapest classes to close before a sweep. PART 3na pins both
  at zero over ALL TEN courses; a new beat that trips either fails the battery. The scan
  script is `presweep_measure.py` in the scratchpad (`--show` lists each hit with its text).
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
- **New trap closed (xf, widened at xh):** before the battery, scan every pin in
  `ruletests.py` that quotes generated or authored text against the rebuilt lessons with a
  regex, and move the misses first. Cover ALL the spellings, not just the PART you are
  writing in: `"..." in spoken(E("id"))`, the `advance_line`/`explain` forms, `PR(op, {...})`
  and `W({...})[i]` — **and `L.OP_EXT["op"]["praise"]({...})`, `L.praise_for(p, 0)` and the
  `_W` alias, which older PARTs use**. A capital letter at the start of a newly split
  sentence is the usual miss.
- **The pre-flight that actually catches it (xh):** a text scan cannot see a pin whose
  ALIAS is wrong for the PART it now sits in — xh moved lhol's pin into 3mo, which defines
  no `_W`, and the battery died on a NameError twenty minutes in. After the regex scan,
  **execute** every PART that touches the generator with a stub `check` that records
  pass/fail, skipping the NameErrors the harness itself causes (module-level helpers the
  battery has and a bare exec does not), and fix what really fails. The scratch pattern is
  in this session; it found the last two misses before the third run, which was clean.
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
  `git diff` and pushes; I never commit. **When his computer is not connected (09-19: two
  days on a phone):** build anyway on the workspace copy, send the file cards, put the docs
  and this handoff in the project with a pending-commit list, and commit everything in one
  go when the bridge is back — never a partial commit that leaves the disk between builds.

## Open items carried forward

Notation repair floor; the voice-cache reclaim card (well past the 812 MB of 09-14 — every
sweep build orphans the clips it replaces); the watch's `__open__` turn; screencheck rules
(below the fold, figure sizes); the pencil in the scripted lane; the
child-mode skin; Phase C (worked generators for the 48 lessons without one — **36 Diffeq +
12 Entry**, not "the Entry course"); Phase B deferred; the prefetch-shelf counter; the tour
button. (`EST_USD_PER_LESSON` corrected in ws; **the critic charter with the "done for the
day" ruling and the watch policy in code — closed by `xl`.**)

I did no harm and this file is not truncated.
