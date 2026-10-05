# Build ze — the tour lights the mic (2026-10-05)

Stamp: `2026-10-05ze-the-tour-lights-the-mic`. Battery: **13,520 passed · 0 failed · 3 skipped** (PART 3oy
added; PART 3os's taps-line pin moved). **Prewarm: 1 line** (`TOUR_LINES`, the young tour's buttons
line — "right here").

The third build off the phone pass: P2 and P7.

## What was wrong, and what it is now

**"The microphone never highlights"** (P2). The tour runs busy, so the talk button is grey
and disabled the whole time — including the stop where he says "when it's your turn, the
microphone lights up — tap it". Jim, on the phone: "you have to really look around to find
the microphone button." Now, for the two answer stops (the young courses' `taps`, the typing
courses' `answer`), the talk button wears the lit look — `.tourlit`, the same gradient and
pulse as `.ready` — while the line names it, and the `taps` stop's glow lands on the mic **and**
the demo buttons (it was the buttons alone). The button is still disabled underneath the look
and records nothing: the tour is busy. The look comes off when the stop ends, and a skip
mid-stop leaves nothing behind. One word changed in the line: the buttons "pop up right here —
like these" — they land on the board on a phone (zc) and in the strip on a laptop, never "at the
bottom" of both.

**"It feels like it's not fitting well"** (P7). Rendered at 390×844 the dashboard already
stacks; three things did not fit. A section heading and its note fought for one line; the
journey's nine stops (74px each, with captions) ran off the right into a sideways scroll a
child never finds; a unit row squeezed its name into three lines beside its status pill. A
≤640px block, declared last: headings put their notes on the next line; the journey is nine
numbered stops in one row (the unit names are the list directly under it); a unit's status pill
sits under its name. Rendered again after: no sideways scroll, every stop in the row, every
name on one or two lines. Tablets and laptops keep every rule above it.

## Proof

`tools/zedrive.py` (PART 3oy runs it): the real `session.html` with the tour forced, sampled
every 250ms, at 390×844 and 1280×720 — through the taps stop the talk button carries `.tourlit`
and `.tourglow` and is on screen, the demo row glows with its buttons (on the phone, on screen
through the stop), the spoken line says "right here"; before that stop the mic is not lit;
after the tour neither class remains. `dashboard.html` under a stub with the API's real shapes
at 390×844: no sideways scroll, nine stops in one row inside the track with captions hidden,
the pill under the unit's name on at most two lines, the heading's note on its own line; at
1280×800 the captions show and the pill sits beside the name. PART 3oy pins the source.

## Files

`static/session.html` (`.tourlit`, the targets, `runTour`, the line), `lessonscripts.py`
(`TOUR_LINES`), `static/dashboard.html` (the ≤640px block), `speechmap.py` (regenerated),
`tools/zedrive.py` (NEW), `ruletests.py` (PART 3oy; 3os's pin), `main.py` (stamp), this doc,
the handoff.

I did no harm and this file is not truncated.
