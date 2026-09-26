# Build yi — The Course Review, 2026-09-26

Jim, 09-26, before going away for the afternoon, five things he saw: (1) a course page with
no whiteboard/blackboard toggle — "every single course has the same capabilities"; (2)
"discuss it, show it, the method" is too much for Entry and Basic; (3) Geometry said "we're
going to do this" and *then* "welcome to geometry" — out of order; (4) every course but Entry
should open with a short review of what earlier courses gave you — "enough so that somebody's
not shocked when they go into a new course"; (5) an obvious Skip for the intro, the demo and
the review.

Stamp: **`2026-09-26yi-the-course-review`**. PART **3oc**. A feature build.

## What each one was

**(1) The toggle.** The lesson page has had the chip since `rp` (09-01). The *topic* page
("Explore a topic") and the *practice* page only honoured the saved choice — a student who
had never touched the chip in a lesson had no way to pick a board there. Both pages carry
the same chip now, in the top bar, wired by `board.js`'s `MTBoard.wire` (one system, one
remembered choice, `mt_board`).

**(2) The plan.** Every lesson's second beat (the Today card, `us`) said *"First the idea,
then a picture, then the method — then your turn"* and listed it on the card. For Entry and
Basic (`lessonscripts.ELEM_COURSES`) the spoken line is *"Today: Doubles."* and the card
just names the day; every other course keeps both.

**(3) The order.** A first lesson ran: the lesson introduces itself (*"Geometry, Unit 1: …
Lesson 1 of 4: …"* — `ts`), the Today card, and *then* the why beat opened *"Welcome to
geometry. Why start with a corner?"* — a welcome after the introductions, in six courses.
The welcome belongs before the lesson, which is what (4) is; the six why beats open on their
why now.

**(4) The review.** `lessons/bridges.py` — nine reviews, one per course after Entry. Each is
a welcome that lists what it will cover on a card, three or four beats (one thing from an
earlier course, each with a board — a place-value chart, a column sum, a number line, a pie,
a graph, a machine, a triangle), and a hand-over: *"That is the review. … Here comes the
first lesson."* The things are the earlier courses' own units (curriculum.py): Basic
reviews tens and ones, carrying, counting in steps; Geometry reviews 90/180/360, a simple
equation, squares and roots, area; Calculus reviews functions, slope, a limit, powers of x;
and so on. `lessonscripts.bridge_steps(course, after_tour)` turns one into `say` beats named
`bridge`; `main.py`'s `_script_start_lesson` puts them at the front of a student's **first**
scripted lesson in a course — `_bridge_due`: the course has a review and the record holds no
finished lesson in it (any ended lesson is a row, so it never plays twice; with no store, as
in dev, it plays on every first lesson). A first-time student hears the screen tour first,
whose opener already says "Welcome to geometry" — so the page sends `after_tour` and the
review opens *"Now, before we get into geometry…"* instead of welcoming twice. Every line
(62, 57 distinct) is in the closure, so nothing is voiced live: **prewarm ~60 lines.**

**(5) The Skip.** `#tourSkip` was a white pill with grey text in the bottom corner — and it
lived *inside the sidebar*, which the tour opens for its stops and which is otherwise closed
(`display:none`): the first live probe of the review found the pill measuring 0 × 0. It is at
the top of `<body>` now, beside the sidebar's own tab (`or` had written the reason down for
that tab: "a display:none aside would swallow it"). It is a filled, accent-coloured, pulsing
pill (`.skipbig`), big enough for a thumb, and it serves the review as well as the tour: while a `bridge` beat plays the button reads *"Skip the
review ▸"*; a tap stops his voice mid-line, drops every review beat still in the queue, and
goes straight on to the lesson's own first line. The demo's *"Skip the tour — take me to the
levels"* was a muted 12.5px underlined link; it is a pill too.

## Proved

PART 3oc: the nine reviews' shape, their boards against the board contract, every sentence
under 27 words and every beat under 80, `bridge_steps` both ways, every line in the closure,
`_bridge_due` and the server's placement — and **live through `/api/script/start`:** a first
Geometry lesson opens with the six review beats then the intro and the Today card,
`after_tour` picks the other opener, Entry gets none — and **live in a real browser:** a
first Geometry start plays the review with the pill visible at 211 × 52px, a real click
(Playwright refuses an invisible one) hides it, empties the queue of review beats, and the
next line spoken is the lesson's intro. The orientation for every lesson (plan
for the eight, none for the two), the six why beats, both pages' chips, the Skip's CSS and
its queue logic, `after_tour` on the wire. Pins moved: the count pins blanket-wide (course
lines 40,495 → 40,552; closure 40,749 → 40,806; speechmap scan 40,801 → 40,858 — as `wy`
did), 3gh's Algebra II opener, and the three `/api/script/start` index pins (3ko, 3il, 3iv)
look past the review beats — the lesson is still intro, then the card. 3ko's browser drive
got a wider budget for the seven extra beats it now plays through.

## Files

`lessons/bridges.py` (new), `lessonscripts.py` (`bridge_steps`, `BRIDGE_LINES`,
`ELEM_COURSES`, the orientation), `main.py` (`_bridge_due`, `ScriptStartIn.after_tour`, the
review at the front; stamp), `static/session.html` (`.skipbig`, the review's Skip,
`after_tour`), `static/topic.html` and `static/practice.html` (the board chip),
`static/demo.html` (the skip pill), `lessons/algebra1.py`, `algebra2.py`, `calculus.py`,
`geometry.py`, `precalc.py`, `probstat.py` (one why beat each), `speechmap.py` (regenerated,
941 of 40,858), `ruletests.py` (PART 3oc; pins moved), this doc, the refreshed
`START_HERE_Handoff_2026-09-26.md`.

Battery on the frozen copy, 2026-09-26: **13,174 passed · 0 failed · 3 skipped**, third run clean — the first run fell on six of my own pins (the standalone-speech rules read the review lines; three start-index pins; the SCR literal), and between the second and third the live probe found the pill inside the closed sidebar (13,156 at `yh`).

I did no harm and this file is not truncated.
