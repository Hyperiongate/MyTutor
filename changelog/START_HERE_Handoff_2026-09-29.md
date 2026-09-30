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

**On Jim's disk: `2026-09-29yu-an-answer-ends-a-pause`** (battery 13,334 passed, 0 failed, 3 skipped) — the first
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
2. **`yv` — the money path (F26 + F27).** Nobody can pay and nobody is gated. Find the
   beta/billing switch in `main.py` (Jim's read: the site is in beta, checkout off); what it
   turns off; whether the free-tier gate is under it. `/family`'s plan box must carry the
   Upgrade button; `/pricing`'s Full-access button must start checkout for a signed-in parent
   (or say "free during beta" while the switch is off — never a $29 button that lands on
   /family); the gate must count "a first unit" as the unit the student was PLACED INTO, not
   unit 1. Then Jim walks it again with Stripe test keys — the paid path has never been walked.
3. **`yw` — the tour (F4, F5, F6, F9, F10, F11) + the first-minute words (F13, F14).** One
   pass over the tour script against today's screen: no glowing face, "the big board" not
   "whiteboard", a tap demonstrated, the pointer ABOVE its target (it bobbed behind the
   laptop's toolbar), the dashboard named once, played once per student (it played twice —
   after sign-in and again after placement). Tap-first helper line in child mode; the title
   once, not in the bubble and on the board.
4. **`yx` — the words a child hears (F17, F22, F25, F29, F15).** Measure "trap" canon-wide;
   Jim's ruling: "trap has to go", the meaning to keep is "here's a very common mistake to
   look out for" (ask whether the upper courses change too). Entry u2 l4: the make-ten idea
   is claimed in the trap beat and the recap and taught nowhere — teach it or drop the
   claim; the fixed-number trap beat after a generated worked example reads the worked
   numbers or announces its own. Geometry u1 l1's complementary beat rewritten plainly,
   pointing at the review's 90/180/360 a minute earlier. The Pathfinder award: never
   mid-intro, never "for completing a unit" the placement skipped.
5. **`yy` — the pictures (F21, F28) + the pencil (F24) + placement (F7, F8).** Count-on
   draws the bigger group FIRST with 7..11 under the added stars (the board drew 5 + 6 while
   the words said start at 6); the Geometry review draws its 24 squares (read the other
   eight reviews for the same — `bridges.py` has never been swept); the pencil goes idle or
   points when the page waits on a tap (his mouth moved with nothing playing); the placement
   key's position is shuffled and pinned (Jim tapped choice 2 throughout and "did pretty
   well"; choice 4 was never right — scan the quiz and reason choices too); 45 questions for
   a six-year-old's first sitting is Jim's call.
6. **`yz` — the topic page and the parent pages (F31, F32, F33, F34, F1, F2, F3).** The
   topic page's board width with the sidebar open; the symbol strip by course (π, θ, |x| on
   Basic); the child skin on every board page; the code out of the URL. Front page: a signup
   button in the first screen and the free box highlighted for a stranger; `/family` as
   steps 1-2-3 for a first visit; "every student", not "every kid".

**Open for Jim:** F20 (the voice said "is" as "eyes" — need the sentence); "trap" canon-wide
or the two child courses only; the placement's length; and **the hub question from F30** —
should the Entry and Basic hubs show a six-year-old the two live-lane tiles ("Get help with
a problem", "Explore a topic") beside the lesson at all?

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
- **A playthrough flag is read against the code before it is built (yu).** Three of
  today's five flags in this build were settled by reading (F18, F12, F30) — one was by
  design, one was the student's own button, one was a tile Jim chose. The ledger records the
  reading; the playthrough doc is corrected, not rewritten.

I did no harm and this file is not truncated.
