# START HERE — Handoff, 2026-10-03

Read this first in a new chat. Then `claude/Playthrough_2026-10-02_The_Phone.md` (the open
ledger) and the build docs only as needed. **Everything before 10-02 — the first-family
playthrough and its eight builds (yu–zb), the sweeps, the quiz lane, the house decisions, the
method — is in `claude/START_HERE_Handoff_2026-09-29.md`, still true and not repeated here.**

## Where things stand

**Live on mrcadabra.com: `2026-10-01zb-the-code-leaves-the-address-bar`** — Jim pushed yu
through zb in one push on 10-02, confirmed /health, removed `PAYMENTS_OPEN` from Render, and
ran the prewarm. The first-family ledger (F1–F34) is closed: every flag built or ruled.

**On Jim's disk, not yet pushed: `2026-10-05ze-the-tour-lights-the-mic`** (battery 13,520 passed,
0 failed, 3 skipped; `claude/Build_ze_The_Tour_Lights_The_Mic_2026-10-05.md`) — P2 + P7: the tour's answer stops put
the lit look on the talk button while he names it and glow the mic with the demo buttons; the
buttons line says "right here"; the dashboard gets a ≤640px block (headings stack their notes,
nine numbered stops in one row, the pill under the unit's name). **Prewarm: 1 line.** Before it,
on the disk too: **`2026-10-03zd-the-phones-menu-and-the-parents-door`** (battery
13,514 passed, 0 failed, 3 skipped; `claude/Build_zd_The_Phones_Menu_And_The_Parents_Door_2026-10-03.md`) — P6 + P8:
on a phone a **☰ Menu** leads the top bar and the board pages' own nav opens as a stacked
full-screen sheet (the Curriculum stacked under it; `static/phone-menu.js`, one copy, the same
nodes moved); every board page has a **Sign out** (clears the zb cookie); the sign-in page's
Parent door leads to /family with the code form folded under it. **Nothing to prewarm.**
Before it, on the disk too: **`2026-10-03zc-the-buttons-go-on-the-board`** (battery
13,504 passed, 0 failed, 3 skipped; `claude/Build_zc_The_Buttons_Go_On_The_Board_2026-10-03.md`). The first build
off the **phone pass** of 10-02: P3 the blocker (on a phone the answer buttons took the whole
screen and "count the stars" had no stars — the buttons land on the board under his words now,
through `board.js`'s one `mountChoicesRow()`; the dock gives back two rows; 26px of board became
367px, measured), P5 (twenty stars as ten and ten; rows wrap), P1 (/family's steps in the
first screen). **Nothing to prewarm.** After the push: `/health` = the zc stamp; to see it,
any Entry lesson on a phone.

## Written to D:\MyTutor (ze, 2026-10-05) — Jim pushes (with zc and zd; one push)

- `static/session.html`, `lessonscripts.py`, `static/dashboard.html`, `speechmap.py`,
  `tools/zedrive.py` (NEW), `ruletests.py` (PART 3oy; 3os's pin), `main.py` (stamp),
  `changelog/Build_ze_The_Tour_Lights_The_Mic_2026-10-05.md` (NEW), this handoff. After the
  push: `/health` = the ze stamp; **prewarm 1 line** (the young tour's buttons line). To see it:
  a new Entry student's tour (or any lesson URL with `&tour=1`); the Progress dashboard on a phone.

## Written to D:\MyTutor (zd, 2026-10-03) — Jim pushes (with zc; one push)

- `static/phone-menu.js` (NEW), `static/student-code.js`, `static/session.html`,
  `static/practice.html`, `static/topic.html`, `static/index.html`, `tools/zddrive.py` (NEW),
  `ruletests.py` (PART 3ox), `main.py` (stamp),
  `changelog/Build_zd_The_Phones_Menu_And_The_Parents_Door_2026-10-03.md` (NEW), this handoff.
  After the push: `/health` = the zd stamp. To see it: any lesson on a phone — the ☰ at the
  top left; mrcadabra.com/login — the parent door.

## Written to D:\MyTutor (zc, 2026-10-03) — Jim pushes

- `static/board.js`, `static/session.html`, `static/practice.html`, `static/topic.html`,
  `static/family.html`, `tools/zcdrive.py` (NEW), `ruletests.py` (PART 3ow), `main.py` (stamp),
  `changelog/Playthrough_2026-10-02_The_Phone.md` (NEW),
  `changelog/Build_zc_The_Buttons_Go_On_The_Board_2026-10-03.md` (NEW), this handoff (NEW).

## What to do next — the phone pass's build order

1. ~~`zc`~~ — P3, P5, P1 — done (above).
2. ~~`zd` — P6 + P8, the phone's menu and the parent's door~~ — done (above). As planned: The dock's nav strip
   on a phone is one word per screen and the Curriculum opens as a thin column inside it:
   build a ☰ button in the top bar opening a full-screen sheet with the links in a plain
   vertical list, the Curriculum its own screen with the units stacked, and a plain **Sign
   out** on it that clears the `mt_student` cookie (zb). The sign-in page's Parent door asks
   for the student's code: send a parent with an account to /family (email + password); keep
   the code form only for a parent without one. Render at 390px before and after.
3. ~~`ze` — P2 + P7~~ — done (above). As planned: The tour names the microphone three times and never lights it (it is
   grey while the tour runs): the glow lands on the mic when a line names it, and the mic
   looks alive for that stop. The Progress dashboard at 390px: render it, then a layout fix
   or a shorter phone version (course tiles and "strengthen next" first).
4. **NEXT — P4** — Entry u1 l1 "counting to 10" never counts to ten: read the lesson against its
   title, then one straight count 1–10 with the stars ticking in before the first ask
   (a lesson edit; prewarm).

**Open for Jim:** the placement on the phone (not yet played) and its 45-question length;
F20's "is"/"eyes" sentence when he hears it again; the parent's dashboard on the phone and
the Friday email (not yet played); the live Stripe key before launch.

## House decisions added

- **The buttons belong with the question (zc).** A choices row lands through
  `mountChoicesRow()` and nowhere else: in the feed under his words on a screen ≤900px, beside
  `#composer` on a desktop. A new page or a new kind of row calls it; nobody writes
  `composer.parentNode.insertBefore` again. The measure is the board's height with the buttons
  up, at 390×844, before and after.
- **One way around on a phone (zd).** A board page's nav is ONE set of nodes: in the sidebar
  on a desktop, in the ☰ sheet on a phone, moved by `phone-menu.js` and never duplicated. A
  new link goes in the page's `.leftnav` and appears in both. Sign out is a `data-signout`
  link, last in the nav; `student-code.js` owns what it does.
- **Ten and ten (zc).** A plain row of things past ten is rows of ten. A phone cannot hold
  twenty in a row, and a child counts twenty as ten and ten anyway.
- **The phone pass has its own ledger (P-numbers) and its own doc**, the first-family
  ledger's F-numbers stay closed; a flag seen on both is one flag, listed where it was seen first.

I did no harm and this file is not truncated.
