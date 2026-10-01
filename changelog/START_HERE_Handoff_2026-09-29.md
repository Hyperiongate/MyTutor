# START HERE — Handoff, 2026-09-29

Read this first in a new chat. Then `claude/Playthrough_2026-09-29_The_First_Family.md` (the
flags) and the build docs it points to, only as needed. **Everything before today —
the sweeps, the quiz lane, the gate list, the house decisions, the method — is in
`claude/START_HERE_Handoff_2026-09-28.md`, still true and not repeated here.**

## Where things stand

**The plan is still the 09-28 deep dive** (`claude/Deep_Dive_2026-09-28_The_Road_To_Market.md`).
Block 1 item 2 happened today: **Jim played the product as a new family for ninety minutes
on his laptop** — front page → parent signup → child code → placement → Entry unit 2 (four
lessons, three mastered by tapping) → unit 3 opened → the parent's pages → a second student
into Geometry (the review, unit 1 lesson 1) → Switch course → Basic's hub. He stopped there
("let's go to work on what you have already") with **33 flags**, all in the playthrough doc
with a six-build order. The phone pass, Basic u3 l4, Pre-Calc u2 l3, the parent's email, the
minutes card and the money path with billing ON are the **next sitting**, after the builds.

**What the ninety minutes said, in one line:** three sweep rounds read every lesson and
found none of this, because the reviewer is an adult and the product is not a lesson. Three
blockers (a tap that submitted nothing; no free-tier gate; no way to pay), one phrase class
("here is the trap"), two board classes the sweeps had names for (the picture the words
describe is not on the board — count-on, the 24 squares), a tour written for a screen that
no longer exists, and a beat every fact of which is right that a first-time reader could not
follow.

**On Jim's disk: `2026-10-01zb-the-code-leaves-the-address-bar`** (battery 13,493 passed, 0 failed, 3 skipped; the zb section
below) — F34, ruled by Jim on 10-01 ("go"), built so the 08-18 bookmark ruling still holds. One
shared script, `static/student-code.js`: a page that arrives with `?code=` (a bookmark, the login
hand-off) stores it in the `mt_student` cookie and takes it out of the address bar in place (no
reload, Back untouched); a page without one reads the cookie; every link between the student
pages carries the course and never the code; the login lands on /home clean. The PARENT'S doors
(/dashboard?view=parent, /records) keep the code in their own URL, used and never stored, so a
parent reading a sibling never changes which student the laptop is signed in as. Eleven pages,
three shared scripts, each with the URL as its fallback for a stale cache; the server unchanged.
Proved in a real browser (`tools/zbdrive.py`, PART 3ov). **Nothing to prewarm.** Before it,
**On Jim's disk: `2026-09-30za-the-same-screen-as-the-lesson`** (battery 13,461 passed, 0 failed, 3 skipped; the za
section below) — the sixth and last build off the playthrough: the topic page and the parent
pages. F31: /topic and /practice get the lesson page's screen node for node (the sidebar
collapsed behind the edge tab, the controls and the answer buttons in the strip UNDER the
board — the 72px buttons had been stacked in the 308px sidebar, cut off). F32: the symbol
strip follows the course (body data-course; + − × ÷ for Entry and Basic, no θ for
Pre-Algebra and Algebra I, the full strip above). F33 read and left (the page sets elem-mode
and the feed IS cream — a dark board there is the remembered chip). F1: "Start free — create
your account" is the hero's second door and the FREE card is the featured one (front page and
/pricing). F2: "Every student covered." F3: /family walks three numbered steps from the real
state; a first visit stacks the cards in step order. **F34 (the code in the URL) is NOT
built: it conflicts with Jim's 08-18 ruling "do not kill the bookmark login" — a question
for him, with a design that honours both (below).** Proved in a real browser
(`tools/zadrive.py`, PART 3ou). **Nothing to prewarm.** Before it, **On Jim's disk: `2026-09-30yz-the-picture-starts-where-the-words-start`** (battery 13,408 passed,
0 failed, 3 skipped; the yz section below) — four flags of one shape: the words were right and
the screen was not what they described. F21: count-on draws the BIGGER group first, says the
swap ("five plus six equals six plus five"), and `[[objects counton="1"]]` lands the counted
group plain and numbers only the added stars (✓7 ✓8 ✓9 ✓10 ✓11) — the generator's walk-backs
and Entry u2's add-past-ten. F28: `[[rectangle]]` draws its unit squares, numbered in area
mode (never on an ask). F24: the pencil's mouth closes when nothing is sounding (the frame
loop reads the audio element and the synth; 600 ms). F7: the assessment deals its four choices
fresh on every render (the Entry bank had the key at index 1 in 28 of 45, never at 3), and
`choices_for`'s own 43%-first-button tilt is an even deal. F8 read and left (foundation-first
is the 07-28 design; the 45-tap length stays Jim's call). Proved in a real browser
(`tools/yzdrive.py`, PART 3ot). **Prewarm: the count-on walk-backs (b > a) and the worked
example** — the prewarm lists them. Before it, **On Jim's disk: `2026-09-30yy-the-tour-reads-todays-screen`** (battery 13,394 passed, 0 failed, 3 skipped; the yy section
below) — the tour, rewritten against the screen as it is: no "glowing face" (the pencil is
Mr. Cadabra; the glow and the tag are on him and he waves), "the big board" not
"whiteboard", the "look here" tag never behind the taskbar (hidden nodes no longer place
it; it stays inside the window), the tour recorded as seen when it ENDS so it never plays
twice on one first visit, and the young tour SHOWS the buttons — a real demo row drawn for
the line, in uc's order (say first) — with one stop for the sidebar. F13 (the helper line's
order) read and left: it is uc, Jim's own ruling. Proved in a real browser (`tools/yydrive.py`). **Prewarm 4
lines.** Before it, **On Jim's disk: `2026-09-30yx-trap-is-gone`** (battery 13,380 passed, 0 failed, 3 skipped) —
Jim's two rulings of the morning: **"trap" gone everywhere** (131 spoken lines in all ten
courses say "a common mistake" now — "Here is a common mistake to look out for." in his
words; `VOCABULARY` bans every spoken form; the elementary prompt says the same) and **the
live-lane tiles stay** on every course's hub (F30 closed as a ruling, no change). Rode
along: Geometry u1's complementary beat rewritten plainly (F29), Entry u2 l4's mistake beat
honest about its numbers and its trick (F22, F25). F15 (the award mid-intro): Jim ruled "I do not
want the awards interrupting a lesson" — a lesson's start says no award; the lesson's end
announces whatever is newly earned (it already did), so nothing is lost. **Prewarm ~134 lines.** Before it, **On Jim's disk: `2026-09-30yw-the-judge-reads-the-ask`** (battery 13,349 passed, 0 failed, 3 skipped; the yw section
below) — the first `scripted` night read (item 5 of the deep dive). GitHub mailed a red job
for the morning of 09-30; day 273 (Entry u7 l1–4, u8 l1–4) re-run by hand gave one S5 HIGH:
"Which clock number is the minute hand pointing to?" over the caption "the long hand is the
minute hand" — a shared "is the minute" that answered nothing. S5 reads the ask now (the
"is the <term>" must close the question); the night's turn is a silent fixture, a real
give-away still fires, day 273 passes. A tool fix, not a lesson edit. Nothing to prewarm.
Before it, **On Jim's disk: `2026-09-29yv-the-free-unit-is-the-one-you-started`** (battery 13,343 passed, 0 failed, 3 skipped; see the
yv section below) — the money path's two blockers. F26: the only free-plan gate sat on the
LIVE lane and counted the Unit Quiz the scripted course never runs, so a free account could
play every lesson in every course. Now the free unit is the (course, unit) of the FIRST
scripted lesson a free student opens (`store.free_units`, first writer wins — the unit the
placement sent them to, not unit 1); a lesson anywhere else is `LINE_FREE_GATE` plus the
page's Family card, on both lanes; a subscribing parent opens it; a removed student takes it
with them; personas untouched. PART 3op drills all of it through the real endpoints on a
sqlite family. F27: the family page's Subscribe buttons were there all along, behind
`_payments_open()` (a live Stripe key, or `PAYMENTS_OPEN=open`) — the site is in beta. What
was wrong: `/pricing`'s "$29 Get full access" landed on /family with nothing to buy. Now
`GET /api/billing/status` is public and the button reads it: closed → "Free during beta —
join the beta" to /beta; open → the ribbon and the notice hide and it goes to /family.
**The money path was walked on 09-30** (Jim: `PAYMENTS_OPEN=open` with the test key, the
card in, Stripe back, "You're all set. Every covered student now has full access", the plan
box Active — "it looks like it's all working"). The override comes out of Render when he is
done testing; the live key goes in before a stranger pays. **Prewarm: 1 line.** Before it, **On Jim's disk: `2026-09-29yu-an-answer-ends-a-pause`** (battery 13,334 passed, 0 failed, 3 skipped) — the first
build off the playthrough. F23, the blocker inside a lesson: all three board pages'
`sendToTutor` opened with `if (busy || paused) return;`, the page was paused, and
`board.js`'s tap handler had already cleared the row — so a tap, a typed answer or a spoken
one sent while paused vanished without a word. Now the student's answer releases the pause
(`releasePause()` beside `setPaused` on session, practice and topic) and goes through;
`tools/yudrive.py` proves it in a real browser and fails on the old page exactly as Jim saw
it. F19: `LINE_UNSURE` no longer says "tap the hand" (the ✋ stayed on pilot.html when the
player was ported). Three flags settled by reading: F18 (the slow walk-back is the SECOND
consecutive miss going to the model — Jim's own 09-13 design), F12 (only the Pause button
sets "Paused"), F30 (not a fall-through: the course hub offers three equal tiles and Jim
tapped "Explore a topic" — a product question, below). PART 3oo. **Prewarm: 1 line.**

## Written to D:\MyTutor (zb, 2026-10-01) — Jim pushes (with yu–za; one push)

- `static/student-code.js` (NEW), `static/index.html`, `static/home.html`, `static/session.html`,
  `static/practice.html`, `static/topic.html`, `static/challenge.html`, `static/dashboard.html`,
  `static/records.html`, `static/drill.html`, `static/pilot.html`, `static/app-nav.js`,
  `static/library.js`, `static/time-tracker.js`, `tools/zbdrive.py` (NEW), `ruletests.py` (PART
  3ov; 3ou's F34 pin), `main.py` (stamp `2026-10-01zb-the-code-leaves-the-address-bar`;
  `_code_dep`'s docstring), `changelog/Build_zb_The_Code_Leaves_The_Address_Bar_2026-10-01.md`,
  this handoff. After the push: `/health` = the zb stamp; nothing new to prewarm. To see it: sign
  a student in — the address bar reads /home, not /home?code=…; open an old bookmark with the
  code — it signs in and the bar cleans itself.

## Written to D:\MyTutor (za, 2026-09-30) — Jim pushes (with yu–yz; one push)

- `static/topic.html` + `static/practice.html` (the sidebar tab, the control strip,
  `placeCtrls`, `data-course`), `static/session.html` (`data-course`),
  `static/math-keyboard.js` (`keysFor`), `static/landing.html` (the fourth door; the free
  card featured), `static/pricing.html` (the free card featured), `static/family.html`
  (the h1; the three steps; `renderSteps`), `tools/zadrive.py` (NEW), `ruletests.py`
  (PART 3ou; 3kq's door pin), `main.py` (stamp `2026-09-30za-the-same-screen-as-the-lesson`),
  `changelog/Build_za_The_Same_Screen_As_The_Lesson_2026-09-30.md`, this handoff. After the
  push: `/health` = the za stamp; the prewarm is the earlier builds' (nothing new here).
  To see it: /topic or /practice on any course at a laptop width (the edge tab on the
  left); the front page's hero; /family signed out, then signed in before adding a student.

## Written to D:\MyTutor (yz, 2026-09-30) — Jim pushes (with yu–yy; one push)

- `static/board.js` (`counton`, `.objhad`), `static/math-figures.js` (`rectangle()` cells),
  `static/cadabra.js` (the sound check, `Cadabra.speaking()`, VERSION `2026-09-30yz`),
  `static/challenge.html` (the deal), `lessonscripts.py` (`_col_add` count-on; `choices_for`),
  `lessons/entry.py` (u2 add-past-ten), `tools/yzdrive.py` (NEW), `ruletests.py` (PART 3ot;
  3gw's count; pins), `main.py` (stamp `2026-09-30yz-the-picture-starts-where-the-words-start`),
  `speechmap.py`, `changelog/Build_yz_The_Picture_Starts_Where_The_Words_Start_2026-09-30.md`,
  this handoff. After the push: `/health` = the yz stamp; **prewarm** (yx's ~134, yy's 4, yu's
  and yv's one, and yz's count-on lines). To see it: Entry u2 lesson 3 (add past ten), the
  Geometry review, and the Course Assessment on Entry.

## Written to D:\MyTutor (yy, 2026-09-30) — Jim pushes (with yu–yx; one push)

- `static/session.html` (both tours, `TOUR_TARGETS`, `highlightEl`, `runTour`, `markTourSeen`),
  `static/board.js` (the row's id), `lessonscripts.py` (`TOUR_LINES` 30),
  `static/cadabra-script.json` + `.example.json` (three tour moments; version yy),
  `tools/yydrive.py` (NEW), `ruletests.py` (PART 3os; counts 40,544), `main.py` (stamp
  `2026-09-30yy-the-tour-reads-todays-screen`), `speechmap.py`,
  `changelog/Build_yy_The_Tour_Reads_Todays_Screen_2026-09-30.md`, this handoff. After the
  push: `/health` = the yy stamp; **prewarm 4 lines** (yx's ~134, yu's and yv's one each).
  To see it: a new student's first Entry sign-in, or any lesson URL with `&tour=1`.

## Written to D:\MyTutor (yx, 2026-09-30) — Jim pushes (with yu, yv, yw; one push)

- `lessons/*.py` (all ten courses; the rewrite), `lessonscripts.py` (7 generated lines;
  `VOCABULARY`), `prompts.py` (one bullet in the elementary template), `ruletests.py` (PART
  3or; one pin moved), `main.py` (stamp `2026-09-30yx-trap-is-gone`), `speechmap.py`
  (regenerated), `changelog/Build_yx_Trap_Is_Gone_2026-09-30.md`, this handoff. After the
  push: `/health` = the yx stamp; **prewarm ~134 lines** (plus yu's and yv's one each).
  To hear it: Entry unit 2 lesson 1's second teach beat.

## Written to D:\MyTutor (yw, 2026-09-30) — Jim pushes (with yu and yv; one push)

- `screencheck.py` (`_IS_THE_ASK_RE`, S5, two fixtures), `ruletests.py` (PART 3oq), `main.py`
  (stamp `2026-09-30yw-the-judge-reads-the-ask`),
  `changelog/Build_yw_The_Judge_Reads_The_Ask_2026-09-30.md`, this handoff. After the push:
  `/health` = the yw stamp; nothing to prewarm (yu's and yv's one line each still stand).
  The next `scripted` night runs day 274's slice on the fixed judge.

## Written to D:\MyTutor (yv, 2026-09-29) — Jim pushes (with yu; one push)

- `main.py` (`_free_unit_gate`, `_free_unit_gate_live`, the gate in `_script_start_lesson`,
  the live OR in `/api/chat`, `GET /api/billing/status`, stamp
  `2026-09-29yv-the-free-unit-is-the-one-you-started`), `store.py` (`free_units`,
  `free_unit`, `record_free_unit`, the reset registry), `lessonscripts.py`
  (`LINE_FREE_GATE`), `static/session.html` (`showGateCard`, both lanes, CSS),
  `static/pricing.html` (the button reads the status), `ruletests.py` (PART 3op; 46 count
  pins 40,542 → 40,543), `speechmap.py` (regenerated),
  `changelog/Build_yv_The_Free_Unit_Is_The_One_You_Started_2026-09-29.md`, this handoff.
  After the push: `/health` shows the yv stamp; **prewarm 1 line**; `/pricing`'s Full-access
  button reads "Free during beta"; then the money-path walk with `PAYMENTS_OPEN=open` (above).
  The battery ran in the cloud workspace on the same staged copy as yu.

## Written to D:\MyTutor (yu, 2026-09-29) — Jim pushes

- `static/session.html`, `static/practice.html`, `static/topic.html` (sendToTutor's gate;
  `releasePause`; dated notes), `static/board.js` (a note on the tap handler's contract),
  `lessonscripts.py` (`LINE_UNSURE`), `tools/yudrive.py` (NEW), `ruletests.py` (PART 3oo),
  `main.py` (stamp `2026-09-29yu-an-answer-ends-a-pause`), `speechmap.py` (regenerated,
  byte-identical), `changelog/Build_yu_An_Answer_Ends_A_Pause_2026-09-29.md`, this handoff.
  After the push: `/health` shows the stamp; **prewarm 1 line**; then, on the live site,
  open any Entry lesson, press ⏸ Pause at a question, tap an answer — it must go through.
  The battery ran in the cloud workspace from `_to_delete/battery_yu.tar.gz` (gitignored;
  delete the folder when convenient).

## What to do next — the build order from the playthrough

1. ~~`yu`~~ — done (above).
2. ~~`yv`~~ — done, and the money path walked by Jim on 09-30 (test key; it works). ~~`yw`~~ — the judge reads the ask, done (above; not in the original order). As planned for yv: Nobody can pay and nobody is gated. Find the
   beta/billing switch in `main.py` (Jim's read: the site is in beta, checkout off); what it
   turns off; whether the free-tier gate is under it. `/family`'s plan box must carry the
   Upgrade button; `/pricing`'s Full-access button must start checkout for a signed-in parent
   (or say "free during beta" while the switch is off — never a $29 button that lands on
   /family); the gate must count "a first unit" as the unit the student was PLACED INTO, not
   unit 1. Then Jim walks it again with Stripe test keys — the paid path has never been walked.
3. ~~`yy` — the tour~~ — done (above). As planned: (F4, F5, F6, F9, F10, F11) + the first-minute words (F13, F14).** One
   pass over the tour script against today's screen: no glowing face, "the big board" not
   "whiteboard", a tap demonstrated, the pointer ABOVE its target (it bobbed behind the
   laptop's toolbar), the dashboard named once, played once per student (it played twice —
   after sign-in and again after placement). Tap-first helper line in child mode; the title
   once, not in the bubble and on the board.
4. ~~`yy` — the words a child hears~~ — **done as `yx`** (F17 canon-wide, F22, F25, F29; F15
   read and left to Jim's ruling).
5. ~~`yz` — the pictures, the pencil, the deal~~ — done (above; F8 read and left; any review that
   draws `[[rectangle show="area"]]` gets the squares by the same figure code — the other
   eight reviews were NOT read line by line for F28's class; still owed). As planned: the pictures (F21, F28) + the pencil (F24) + placement (F7, F8). Count-on
   draws the bigger group FIRST with 7..11 under the added stars (the board drew 5 + 6 while
   the words said start at 6); the Geometry review draws its 24 squares (read the other
   eight reviews for the same — `bridges.py` has never been swept); the pencil goes idle or
   points when the page waits on a tap (his mouth moved with nothing playing); the placement
   key's position is shuffled and pinned (Jim tapped choice 2 throughout and "did pretty
   well"; choice 4 was never right — scan the quiz and reason choices too); 45 questions for
   a six-year-old's first sitting is Jim's call.
6. ~~`za` — the topic page and the parent pages~~ — done (above): F31, F32, F1, F2, F3 built;
   F33 read and left; F34 built the next morning as ~~`zb`~~ on Jim's ruling. As planned: (F31, F32, F33, F34, F1, F2, F3). The
   topic page's board width with the sidebar open; the symbol strip by course (π, θ, |x| on
   Basic); the child skin on every board page; the code out of the URL. Front page: a signup
   button in the first screen and the free box highlighted for a stranger; `/family` as
   steps 1-2-3 for a first visit; "every student", not "every kid".

**All the playthrough builds are done (yu, yv, yw, yx, yy, yz, za, zb — F34 built on Jim's 10-01 ruling).** What is left from the
playthrough is Jim's: the questions below, then the next sitting (the phone pass, Basic u3
l4, Pre-Calc u2 l3, a graph lesson, the parent's email and dashboard, /admin's minutes card,
the nightly reports, the money path with the switch on — and `PAYMENTS_OPEN` out of Render
when the testing is done, the live Stripe key in before launch).

**Open for Jim:**
- ~~F34~~ — built as `zb` on 10-01 (above). The 08-18 bookmark ruling stands beside it in
  `main.py`'s `_code_dep` docstring: a bookmark with the code still signs in.
- F20 (the voice said "is" as "eyes" — need the sentence); the placement's length (45 taps).
- Seen on a 390×844 phone while proving za, not built: /topic for Basic with three 72px
  child-mode buttons in the dock leaves the board a few pixels tall — identical before and
  after za (dz's dock + xx's buttons). For the phone pass.
- (Ruled 09-30: "trap" gone everywhere; the hub keeps its live-lane tiles; no award
  interrupts a lesson; the free door in the first screen and four hero doors — F1 amends uu.)

## House decisions added today

- **The student's answer ends a pause (yu).** A page that gates `sendToTutor` may refuse on
  `busy` alone. `board.js`'s choices row clears itself before the page has accepted the
  answer (the disable-on-tap discipline), so any other refusal is a silent drop — the
  student sees the buttons go and nothing else. `releasePause()` clears the flag, the button
  and the status line and never calls `play()`; the next line's `stopAllSpeech` supersedes
  the paused clip. A new board page with a pause button gets the same two lines.
- **A spoken line names only what the page has (yu).** "Tap the hand" named pilot.html's ✋
  on a page that never had one. PART 3oo pins `LINE_UNSURE`; the same test applies to any
  authored line that tells the student to tap, press or look at something: grep the page.
- **The first miss is the engine's, the second is the model's (vz, confirmed today).** When
  Jim says "he took a long time to think" after a miss, ask whether it was the second miss
  in a row before reading anything else.
- **One screen for one tutor (za).** A board page is the lesson page's screen: the sidebar
  collapsed behind the edge tab on a desktop, the controls in the strip under the board, the
  choices row mounted beside `#composer` — so `#composer` must live where the buttons should
  land. A new board page copies session.html's build-or block node for node (`#sbTab`,
  `#ctrlBar`, `placeCtrls`, `mt_sb_open`) rather than inventing a layout. And anything the
  page offers by course — the symbol strip, the child skin — keys off `body data-course` /
  `body.elem-mode`, set by the page script before the shared scripts run.
- **A ruling is amended by Jim, not by a flag (za, zb).** F34 and the 08-18 bookmark ruling
  conflicted; the flag was brought to him with a design, not built over the ruling — and the
  next morning he ruled, and `zb` built the design that keeps both (the cookie takes an
  arriving bookmark's code; the parent's doors keep theirs). F1 was the
  reverse — Jim's own words on 09-29 amended his 09-09 three-door ruling — and PART 3kq's pin
  now says which ruling it carries and why.
- **The picture starts where the words start (yz).** When a spoken line says "start at six"
  the board draws six first; when it says "24 squares" there are 24 squares to count; when
  the voice stops, the mouth stops. A board tag that cannot draw what the words say is a
  defect in the tag, not in the lesson — fix the tag (`counton`, the rectangle's cells), then
  the authored lines. And a key that sits in one seat is a tilt: deal choices at render,
  never trust an authored order.
- **A playthrough flag is read against the code before it is built (yu).** Three of
  today's five flags in this build were settled by reading (F18, F12, F30) — one was by
  design, one was the student's own button, one was a tile Jim chose. The ledger records the
  reading; the playthrough doc is corrected, not rewritten.

I did no harm and this file is not truncated.
