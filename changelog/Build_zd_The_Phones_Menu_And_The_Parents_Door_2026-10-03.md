# Build zd — the phone's menu and the parent's door (2026-10-03)

Stamp: `2026-10-03zd-the-phones-menu-and-the-parents-door`. Battery: **13,514 passed · 0 failed · 3 skipped** (PART
3ox added; two older pins moved — a fixed 6,000-character note slice became `notes()`, and the
landscape phone's dock reads the nav in the ☰ sheet). **Nothing to prewarm** — no spoken line changed.

The second build off the phone pass: P6 and P8 together, because they are one question — how
does a family get around on a phone.

## What was wrong, and what it is now

**"Getting around is super cumbersome"** (P6). On a phone the board pages' sidebar is a dock at
the bottom (build dz), and its nav links were a sideways chip strip: one word per screen —
"Curriculum", scroll, "Course assessment" — and the Curriculum list opened as a thin column
*inside* the strip. Now, on a screen 900px wide or less, a **☰ Menu** button leads the top bar
and the page's own nav moves into a full-screen sheet as a plain stacked list: Curriculum first
(it opens the nine units stacked, full width, each its own row), then Course assessment,
Progress dashboard, Practice, Extra practice, Explore a topic, Final Exam, Look it up, and
Sign out last. A tap on any link or unit closes the sheet (a unit opens its card on its own);
so do ✕ and the dark backdrop. The pencil steps out while the menu is up. Above 900px nothing
changes — the nav is back in the sidebar where build or left it. One shared script,
`static/phone-menu.js`, loaded last on the three board pages; it moves the **same nodes**
(same ids), so the tour, library.js's "Look it up" and every page hook still find them. The
tour, which names the sidebar's buttons at one stop, points at the ☰ while the sheet is closed.

**Student → parent on one phone** (P8). A student had no way out at all — and since zb put the
code in a cookie, a shared laptop needs one. Every board page carries a **Sign out** link, last
in its nav (so last in the phone menu, in red), wired by `student-code.js` to clear the
`mt_student` cookie and go to the sign-in page. And the sign-in page's Parent door asked for
the *student's* code: it now leads with **"Sign in to my Family page"** (/family — email and
password, every student's code, their progress, the plan), and the student-code form folds
under "No account? Follow one student with their code" — same ids, same verified flow, for the
parent without an account.

## Proof

`tools/zddrive.py` (PART 3ox runs it): the real pages under a stub API. At 390×844 on
`session.html`: the ☰ is the first thing in the top bar, the nav is not in the dock, the sheet
is closed; a tap opens it with every link ≥330px wide on its own row, Curriculum first and Sign
out last, the pencil hidden; Curriculum opens nine units stacked; a unit tap closes the sheet
and shows the unit card; ✕ closes it; Sign out leaves no `mt_student` cookie and lands on
/login. `topic.html` and `practice.html` the same. At 1280×800: no Menu button, the nav in the
sidebar with Sign out last, no sheet. `index.html`: the parent door's link is /family and the
code form is folded (checkVisibility) and unfolds on a tap. PART 3ox pins the source lines.

## Files

`static/phone-menu.js` (NEW), `static/student-code.js` (the sign-out hook),
`static/session.html` (the link, the script, the tour's ☰), `static/practice.html`,
`static/topic.html` (the link, the script), `static/index.html` (the parent door),
`tools/zddrive.py` (NEW), `ruletests.py` (PART 3ox), `main.py` (stamp), this doc, the handoff.

I did no harm and this file is not truncated.
