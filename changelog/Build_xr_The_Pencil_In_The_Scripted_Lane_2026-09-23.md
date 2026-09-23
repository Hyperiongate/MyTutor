# Build xr — The Pencil In The Scripted Lane, 2026-09-23

Stamp: **`2026-09-23xr-the-pencil-in-the-scripted-lane`**. PART **3nm**. Project 5 of the
09-14 deep dive, the fourth gate build of the alternating schedule (watch policy `xl` → the
miss has a face `xn` → Phase C `xo` → **this**). Built on Jim's "go ahead and start the next
build" while he was away.

## What was wrong

The 09-14 project list: "He points at the board line being spoken, underlines the number he
just said, goes to write mode when a board draws, waves at the lesson intro, parties at the
streak. Driven by the engine's own steps — no authoring per lesson. Bigger, docked beside
the board rather than drifting." The 09-22 deep dive checked: the pencil's moves still had
zero callers in any of the 360 lessons. The scripted lane rang him only for answers, misses
and the lesson's ends; every teach, picture, worked example and walk-back played with him
floating at the window's edge, 55% of the way down, wandering.

## The build

**The engine names its beats** (`lessonscripts.py`). The authored kinds were already named for
the page by `beat_of` (why, picture, teach, worked, practice_intro, explain, recap). The
engine's own steps now carry a name too: `intro` on the lesson's introduction, `praise` and
`walk-back` in `_correct_beats`, `second-look`, `walk-back` and `fresh-one` on the first miss.
`main._script_clean` already keeps a `beat` a step carries. Additive: no spoken line, board or
count changed — course lines are still 40,495.

**The page rings them** (`static/session.html`). `cadBeat(step, isAsk)` runs for every
scripted beat, before the ask's door opens (the pd rule) and before `problem.fresh`: it
rings `beat.<name>` — the server's name, `ask` for a question, `say` for anything else. The
praise beat carries the right answer as data (numbers only, from `SCR.lastRight`, set where
the streak grades the tap) and rings 1,400 ms late so the answer.correct bounce is not cut
short; a beat that has moved on by then rings nothing. An intro that plays more than eight
seconds after the last `lesson.start` — the seam's next lesson — rings `lesson.start` again,
so he waves hello at every lesson, not only the first. `board.written` (the glance) is no
longer rung while the scripted lane runs; the glance is the live lane's.

**The pencil learns four things** (`static/cadabra.js`, version `2026-09-23xr`):

- **`present`** — a new behaviour. He comes to the newest board block with his tip on its
  lower corner in the write pose (the lean `draw()` uses), as if he had just drawn it, and
  holds there while the line is spoken. Measured 340 ms after the ring, because the feed
  scrolls every new tutor turn to the top of the board a frame after it lands (Jim's `ir`
  ruling); while he holds, the tip follows a block that scrolls. A block whose corner sits
  higher than his own body — which, under `ir`, is most of them — is **pointed at from
  below** instead, by `point`, for the same held length; and a block that scrolls up under
  him while he writes hands over to `point` the same way. Rule 19 stands: a corner over a
  control tries the other corner, then gives up.
- **`hold: "voice"`** on `present` and `point`: the pose lasts until the voice has been
  silent for a beat (`S.speaking`, fed by `mt:speaking`/`mt:silent` and the rt watchdogs),
  never shorter than `ms`, never longer than `maxMs`. The old fixed-`ms` form is untouched.
- **`fire(moment, data)` fills `"$name"`** in a step's strings from `data.name` — `"text":
  "= $answer"` underlines the answer the student just gave. A step naming a value the page
  did not give is left out, never drawn blank.
- **The dock.** Menu `dock: "board"`: on a desktop his home is the board's top-right
  corner, inside its own margin, and the roaming drift is off (the rj float stays —
  breathing, not wandering). No dock in the menu = the old home and drift, byte for byte;
  the phone's corner home (ug) is untouched. Pointing up at a high block he now stands
  at `1.0 ×` his height below it (was 0.85): at 200 px his hat brushed the bubble.

**The menu** (`static/cadabra-script.json` and `.example.json`, identical): `beat.picture`,
`beat.teach`, `beat.worked`, `beat.practice_intro`, `beat.recap` and `beat.walk-back` →
present the newest block, held for the voice; `beat.praise` → pleased, then underline
`"= $answer"` on the board; `beat.why` → the teaching face at home (the why is told over
the goal card); `beat.second-look` → the listening face (he is beside the miss already);
`beat.ask` → release, out of the way while the student works. `height` 146 → **200**,
`handSize` 26 → 36; the phone size stays 92. Every older moment is unchanged: `lesson.start`
enters and waves, `answer.wrong` comforts at the miss, `problem.fresh` points, `milestone`
parties, `answer.correct` celebrates (its tier-2 party at every third right answer is the
"party at the streak" the project asked for — it was already there, with the lesson party at
the mastered end).

## Proven

Headless (Playwright, `prove_xr.py`, screenshots in the session's scratch folder): version
xr, size 200, the dock at the board's corner (x = board.right − 44, y = board.top + 216); a
teach beat on a top-of-board block → the point pose from below, held through
`mt:speaking` and released to home on `mt:silent`; a worked beat → the same; a right
answer then the praise beat → one ink stroke under `= 10`; the ask → home; a praise with
no answer → the underline step skipped, no error; a seam intro → `lesson.start` rung once;
no page errors. The first cut stood him over the top bar's Switch-course button (the write
pose on a top-of-board block) — that is where the "too high → point from below" rule and
the 340 ms settle came from.

PART 3nm pins all of it: the beat names reaching the page on a real lesson (begin, a right
answer, a miss), the page's ring and its order, the praise's answer and wait, the seam's
lesson.start, the live lane's glance kept, `present` / `holdFor` / `fillSteps` / the dock in
cadabra.js, the menu's moments (both copies), and that no scheduled beat is a dead moment.
Four pins moved with the text: the size in 3hk, the graded line in 3hd and 3ni, the menu's
version in 3ni. `pinscan` 0 misses.

Battery on the frozen copy: **12,935 passed · 0 failed · 3 skipped** (12,920 at xq; two runs -- the first moved three older pins: 3kc's phone home and drift lines, 3ko's "the engine names no beat").

## After the push

`/health` = `2026-09-23xr-the-pencil-in-the-scripted-lane`. **Nothing to prewarm.** Then
open any lesson and watch: he sits at the board's top-right corner, bigger; on each teach
beat he comes down beside the bubble and points at the board line while it is spoken, and
goes home when the voice stops; on a right answer he bounces, then underlines the answer on
the worked board; on the question he steps back. The one thing to judge by eye is the
size — 200 was chosen from the project's "0.30 → ~0.45" (×1.5 would be 219); the number
is the menu's `height` and takes no code to change.

## Left for later, on purpose

The write pose (tip on the block's corner) shows only for a block low enough on the board
to leave room for his body — a tall figure, or a second block under a long turn. Under
`ir` most blocks sit at the top, so most beats are the point-from-below. If Jim wants the
write pose more often, the honest change is in the page's scroll ruling, not here. The demo
page drives him itself and is untouched. The child-mode skin (project 7) and the
voice-cache reclaim card (project 9) are the next gate builds.

## Files

`lessonscripts.py`, `static/session.html`, `static/cadabra.js`, `static/cadabra-script.json`,
`static/cadabra-script.example.json`, `ruletests.py` (PART 3nm), `main.py` (stamp), this
doc, the refreshed `START_HERE_Handoff_2026-09-23.md`.

I did no harm and this file is not truncated.
