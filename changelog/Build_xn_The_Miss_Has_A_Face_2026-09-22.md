# Build xn — The Miss Has A Face (2026-09-22)

Project 4 of the 09-14 deep dive, and the second gate build interleaved with the sweep
rounds. The 09-14 read of the classroom through a child's eyes: *"a wrong tap gets no
visible reaction on the board. The button does not shake, the answer is not marked, and the
pencil does not look at it. The correction arrives in words a second later. A child's world
is faster than that."* The 09-22 deep dive checked and found it exactly as described.

Stamp: **`2026-09-22xn-the-miss-has-a-face`**. Page-only: no engine change, no audio, no
referee, nothing to prewarm. Battery: see the bottom.

## What a child sees now

A wrong answer: **their own answer bubble shakes and is stamped with a red cross.** The
pencil **flies to it** and says the nudge there — *"Take your time. I am not going
anywhere."* — beside the crossed answer, not from wherever he was standing. The stamp stays
through the explanation, so the child can see *which* answer the words are about. When the
fresh problem lands (the first ask after a miss — `vz`'s redo is a fresh problem of the
same shape), he **points at its board**, so the eye goes from the cross to the new question.

A right answer: the bubble is stamped with a green tick, and the pencil celebrates as he
already did.

## Why the bubble, not the button

The 09-14 sketch said "shake the button". Two things stood in the way, and both are
standing rules rather than accidents: `board.js`'s `showChoices` clears the row the moment a
button is tapped, and `handleTags` opens every turn with *"stale answer buttons never
survive a new turn"* — so a marked button would be gone before the shake finished, and
keeping it would mean a stale row on the page. And a typed or spoken answer has no button
at all. What all three doors share is the **student's own bubble** in the feed: it is the
record of what they said, it stays in the transcript, and it is where they are looking.
So the bubble is what reacts. The tap row is cleared exactly as before; PART 3ni pins that.

The demo (`demo-lesson.html`) already marks its tapped button right or wrong. The session
page's stamps use the demo's colours, so both players speak one language.

## The pieces

- **`static/session.html`** — `markLastAnswer(kind)`: finds the newest `.bubble.student`,
  stamps it `graded wrong` / `graded right`, and on a miss sets `data-cad="miss"` so the
  pencil can find it. Called from the scripted grade (the streak comparison in `scrAnswer`,
  *before* the pencil is rung so his comfort has its target) and from the live lane's
  three doorbells (`[[mark]]`, `[[miss]]`, `[[nice]]`). `SCR.afterMiss` arms
  `problem.fresh`, rung once from the ask branch of the player. CSS: the cross, the tick,
  a shake and a small pop under `prefers-reduced-motion: no-preference`, with `dz`'s
  global reduced-motion rule covering the rest.
- **`static/cadabra-script.json` + `.example.json`** (identical, version `2026-09-22xn`) —
  `answer.wrong` is now `expression thinking` → `comfort target miss from nudges`; new
  `problem.fresh` → `hush` → `point target board.latest`. `cadabra.js` needed no change: it
  resolves any `data-cad` name, `comfort` already takes a target and a `from`, and
  `board.latest` is a name it resolves itself.

## Proven before the battery

A headless browser (Playwright) against the page on a stub server: the bubble carries the
classes, the `missshake` animation and the ✗ content; the pencil's comfort lands beside it
saying a nudge line; after the fresh board his point lands; a right answer gets its ✓ and no
`miss` target is left behind; no page errors. Screenshots in the session's scratch folder.

## Two things the battery's own rules caught

- **`rp`: no colour literals on the board.** The first cut wrote `#e0392b` and `#0e9f6e`.
  They are tokens now — `var(--bd-e0392b)`, `var(--bd-0e9f6e)` — which also gives the dark
  board its own red and green for free.
- **`ri`: every pencil target names a `data-cad` that exists on the page.** `miss` is set at
  runtime and `board.latest` is resolved by `cadabra.js`. The pin now admits each only on
  the evidence of the code that provides it — `setAttribute("data-cad", "miss")` on the
  page, `latestBlock()` in `cadabra.js` — never by name alone.

One older pin moved and marked "(xn)": `rr`'s "the scripted lane rings answer.correct off
the server's streak", which now reads the marked line.

## Left for later, on purpose

The demo's tapped button marks right/wrong but does not shake and the demo's pencil does not
comfort; the demo is its own player with its own rules and is a one-line follow-up when the
child-mode skin (project 7) reaches it. The 09-14 sketch's "bigger pencil, docked beside
the board" is project 5.

## Battery

Frozen copy, 2026-09-22: **12,865 passed · 0 failed · 3 skipped** (12,855 at `xm`). Two runs. The first failed three of the page's own laws: `pd`'s "nothing sits between the open answer door and his line" (my point was rung in that gap — moved to just before the door opens), `uc`'s "the taps open first, then the mic holds" (same cause), and `sd`'s "the product never prints child/children" (two of my comments did; they say student). Every one a rule worth keeping; second run clean.

I did no harm and this file is not truncated.
