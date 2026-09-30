# Build yy — the tour reads today's screen (2026-09-30)

Stamp: `2026-09-30yy-the-tour-reads-todays-screen`. Battery: **13,394 passed · 0 failed · 3 skipped** (PART 3os added;
three count pins moved, 40,543 → 40,544). **Prewarm: 4 lines** (`TOUR_LINES` 29 → 30; three
lines changed, one new).

The tour is the first minute a new student ever hears, and Jim's first-family playthrough
flagged it five times in that minute (F4, F5, F6, F9, F11) with F10 and F13 beside it. Every
one was the tour describing a screen that no longer exists, or pointing at it badly. One pass
over the tour against the screen as it is today, proved in a real browser.

## What was wrong, and what it is now

**"See that glowing face? That's me"** (F4). No face has been on the screen since `rj`
retired the orb — the pencil is Mr. Cadabra. The stop glowed the name panel. Now the line is
"See me waving? I'm Mr. Cadabra — the pencil with the hat!", the glow target for `tutor` is
the pencil's own body (an SVG group — measured for the tag, never boxed; the name panel is
the fallback when he is not up), and the tour rings `tour.tutor`, which the pencil's menu
answers with a wave. The grand tour's version says the same.

**"The big whiteboard is mine"** (F5). Entry's board has been cream since `xx`. "The big
board" — both tours.

**The "look here" tag bobbing behind the taskbar** (F6). The answer stop names the talk
button AND the composer; the composer is `display:none` until "Type my answer" is tapped, so
its rect is 0×0, the group's top read as 0, and the tag went BELOW the group — off the
bottom of a laptop window. Hidden nodes are dropped before the tag is placed, and the tag
goes below a target only when there is room below it; never past the window's edge.

**The tour played twice on one first visit** (F9). The seen-fact was written by
`tourHandoff` — which the assessment invitation's "Yes" button never reached, because it
navigates to `/challenge`. `markTourSeen()` (keepalive) runs when the tour ends, before the
invitation; the handoff's own write stays and is idempotent.

**The young tour showed talking and never tapping** (F11). The elementary answer stop was
picked by `canRecord`, so on any laptop with a microphone a six-year-old heard the typing
courses' microphone line with "the answer buttons always work as well" tacked on the end,
and never saw a button. Entry and Basic have their own stop now (`taps`): it draws a real
demo row (`showChoices`, the same 72px buttons, glowing; a tap sends nothing because the
tour runs busy; the row leaves with the stop) and says — in `uc`'s order, Jim's own ruling
of 09-07 (speak first, type if you'd rather, tap if you like) — "when it's your turn, the
microphone lights up — tap it and just SAY your answer out loud. And big answer buttons pop
up right down here at the bottom — like these. Tap the one you think is right…" The pencil
points at the row (`tour.taps`).

**The sidebar never named** (F10). One stop, one breath: "Over here are the buttons for your
lessons, your progress, and extra practice. A grown-up can show you those later — today,
everything you need is right here on the board." Still no Course Assessment, no Final Exam,
no layout words (the `uh` rules hold). Four stops now; the glow is the Progress button.

**"How to answer" led with the microphone** (F13) — read and left. I had logged it as
cosmetic on the day; the line's order is `uc`, Jim's ruling: the same three doors, in the
same order, in every course. It stands as he wrote it.

Left as it is: **F14** (the title in the bubble and on the board) — the bubble is the
transcript of what he says, the card is the board; a deaf child reads the one and everyone
sees the other. **F12** was the Pause button (`yu`).

## Proof

`tools/yydrive.py` (PART 3os runs it): the real `session.html` under a stub API, a brand-new
Entry student with the tour forced and no placement. It samples the screen every 300 ms
through the whole tour and proves: the four stops play in order and no spoken line says
"face" or "whiteboard"; on the taps stop real buttons 3 | 4 | 5 are on the screen at child
size with the row glowing, and they are gone when the invitation is up; the "look here" tag
is inside the window every time it is shown; `/api/tour-seen` is POSTed before the
assessment invitation appears.

## Files

`static/session.html` (the two tours; `TOUR_TARGETS`; `highlightEl`; `runTour`;
`markTourSeen`), `static/board.js` (`row.id = "choiceRow"`),
`lessonscripts.py` (`TOUR_LINES`), `static/cadabra-script.json` + `.example.json`
(`tour.tutor`, `tour.taps`, `tour.answer`; version `2026-09-30yy`), `tools/yydrive.py` (NEW),
`ruletests.py` (PART 3os; two pins moved; the counts), `main.py` (stamp), `speechmap.py`
(regenerated), this doc.

I did no harm and this file is not truncated.
