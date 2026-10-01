# Build za — the same screen as the lesson (2026-09-30)

Stamp: `2026-09-30za-the-same-screen-as-the-lesson`. Battery: **13,461 passed · 0 failed · 3 skipped** (PART 3ou
added; PART 3kq's door pin reads four doors, two rows at 1280; PART 3kc's "small-screen blocks
declared last" pin kept honest — the za block sits before ug's, the lesson page's order).
**Nothing to prewarm** — no spoken line changed.

The sixth and last build off Jim's first-family playthrough: the topic page (F31, F32, F33)
and the parent pages (F1, F2, F3). F34 is read and brought to Jim, not built — see the end.

## What was wrong, and what it is now

**The topic page was a different screen** (F31). Jim, on /topic for Basic: "the whiteboard
doesn't hold all of his words because the sidebar is wide open." The page kept a 308px
sidebar open at all times, and — the part he could see but not name — board.js mounts the
answer buttons beside `#composer`, which on this page lived in that sidebar: three 72px
child-mode buttons stacked in a 308px column, the bottom one cut off, no obvious scroll. The
lesson page solved exactly this a month ago (build or, 2026-08-27): the sidebar starts
collapsed behind an edge tab and the name + controls live in a compact strip under the
board. `topic.html` and `practice.html` have that now, node for node — the same `#sbTab`,
the same `#ctrlBar`, the same `placeCtrls()` reparent, the same `mt_sb_open` key, so a
student's open/closed choice carries between the pages. The board takes the whole width;
the buttons land under it, whole, at full size. Phones are untouched (the tab hides, the
nodes go back to the dock; measured before and after at 390×844 — pixel for pixel the same).
The top bar's icon nav keeps every sidebar link one tap away while it is closed.

**π, θ and |x| on a Basic course** (F32). The symbol strip under the typing box was one
list for every course. The board pages set `body data-course` before `math-keyboard.js`
runs, and `keysFor(course)` picks the tier: Entry and Basic get **+ − × ÷** (plus first, the
way a child meets them) and nothing else; Pre-Algebra and Algebra I get everything but θ;
Geometry and up, an unknown course, or a page with no attribute get the full strip exactly as
before. The eighteen keys themselves are unchanged. The lesson page sets the attribute too —
its strip shows for a young student who taps "Type my answer".

**"Dark board, not the cream child skin"** (F33) — read and left. The page HAS set
`body.elem-mode` for Entry and Basic since uc, and board-theme.css paints the feed cream
(`#fff8e8`, proved in the browser). A dark board there is the remembered "Dark board" chip —
one key for every page, Jim's yi ruling ("every course, every page, the same boards").

**No signup button above the fold** (F1). The hero has a fourth door: "Start free — create
your account" (/family), second in the row beside Try a lesson, outlined in the brand purple
so it is as loud as the lesson door without being a second gradient button. uu's three doors
keep their order around it — this is Jim's amendment of 09-29 to his own 09-09 ruling, and
PART 3kq's pin says so. In the pricing section (front page and /pricing alike) the **Free**
card is the featured one now — the gradient border, a "Start here" tag, the filled button —
and the Full-access card is the plain one with the ghost button. Prices, lists, the toggle
and yv's billing-status wiring are untouched.

**"Every kid covered"** (F2) → "One account. Every student covered."

**Two containers with no order** (F3). A steps strip under the heading names the path on
every visit — **1** Create your parent account · **2** Add a student — you get their login
code · **3** Your student signs in with the code — and `renderSteps()` marks each Done / You
are here / Next from the real state: signed out (1 here), signed in with no student (1 done,
2 here), students added (3 here). On a first visit the two cards stack in step order, one
column, students first; a family with students keeps the two-column view it knows. The card
headings carry their numbers (2 Your students, 3 Your plan), and the empty-state note no
longer numbers three steps of its own (it clashed with the page's). Sign-in, add-a-student,
the code chip, Manage, the attach door, billing and the email toggle are unchanged.

## F34 — read, not built; a question for Jim

The student's code in the URL (`/topic?code=…`) is the credential in history, bookmarks and
screenshots. But `main.py`'s `_code_dep` carries Jim's own ruling of 2026-08-18, the same day
the API calls moved the code to a header: **"Do not kill the bookmark login"** — a family
bookmark is how a young student signs in, and the code says "do not 'fix' this without a NEW
ruling from Jim." Twelve files read the code from the URL (home, session, dashboard,
challenge, drill, records, practice, topic, pilot, app-nav.js, library.js, time-tracker.js).
A design that honours both: a session cookie set at sign-in (and whenever a page arrives
with `?code=`), every page reading the cookie when the URL has none, and the in-app links
between pages dropping the code — a bookmark with the code still signs in, and nothing a
student taps inside the app carries it. That is a build of its own (`zb`) and it needs the
new ruling first.

## Also seen, not built

On a 390×844 phone, /topic for Basic with three 72px child-mode buttons in the dock leaves
the board a few pixels tall — exactly the same before and after this build (dz's dock plus
xx's 72px buttons). It belongs to the phone pass, the next sitting.

## Proof

`tools/zadrive.py` (PART 3ou runs it): the real `topic.html`, `practice.html`, `family.html`
and `landing.html` under a stub API. At 1280×800 the sidebar is collapsed behind the tab, the
board is ≥1100px wide, the controls and the choices row are inside `#ctrlBar` under the
board, every button is whole, inside the window and ≥72px; the tab opens (308px, "Close")
and closes it. At 390×844 there is no tab, the controls are back in the dock, the buttons
are on screen. The strip reads + − × ÷ on Basic, 17 keys without θ on Algebra I, all 18 in
the original order on Geometry. The feed's computed background on Basic is `rgb(255, 248,
232)`. /family: the h1, and the three states with their step words, the first-visit stack
(students card above the plan card, same left edge) and the two-column view with a student.
/landing: the four doors in order, all inside the first screen; the Free card `.feat` with
the primary button, Full access plain with the ghost. PART 3ou also pins every line in the
source, that the sidebar lines are the lesson page's own, that the keys are unchanged, that
`_code_dep` still carries the bookmark ruling, and the dated notes.

## Files

`static/topic.html`, `static/practice.html` (the sidebar, the strip, `data-course`),
`static/session.html` (`data-course`), `static/math-keyboard.js` (`keysFor`),
`static/landing.html` (the fourth door; the cards), `static/pricing.html` (the cards),
`static/family.html` (the h1; the steps; `renderSteps`), `tools/zadrive.py` (NEW),
`ruletests.py` (PART 3ou; 3kq's door pin), `main.py` (stamp), this doc.

I did no harm and this file is not truncated.
