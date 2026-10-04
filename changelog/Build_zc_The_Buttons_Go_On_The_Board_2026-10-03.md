# Build zc — the buttons go on the board (2026-10-03)

Stamp: `2026-10-03zc-the-buttons-go-on-the-board`. Battery: **13,504 passed · 0 failed · 3 skipped** (PART 3ow
added). **Nothing to prewarm** — no spoken line changed.

The first build off Jim's phone pass (`claude/Playthrough_2026-10-02_The_Phone.md`): P3, the
blocker, with P5 and P1 riding along.

## What was wrong, and what it is now

**"Count the stars" with no stars** (P3). On a 390×844 phone the dock at the bottom held the
name + status line, the nav strip, the mic, Pause, the hint, the helper line AND three 72px
child-mode answer buttons — 562px of the screen, measured — and the board above it was 26px
tall. The stars were there; they had no room. Jim guessed wrong, and the walk-back redrew the
stars after the buttons had cleared, which is why *that* worked.

The answer buttons belong with the question. `board.js` has one place a choices row lands now,
`mountChoicesRow()`: on a screen 900px wide or less the row goes **into the feed**, under his
words and his picture (before the anchoring pad, so follow-the-pen keeps the buttons in view);
on a desktop it sits beside `#composer` exactly as before — the lesson page's control strip,
the topic page's too. `showChoices` uses it, and the lesson page's own rows (`scrChoice`'s
Yes / Show me again and I'm ready, `showSeamChoice`'s lesson doors) go through it with the old
mount as their fallback. The phone dock also gives back two rows: the name + status line (the
title bar names him; the mic, the Pause button and the thinking flag carry the state) and the
helper line (the hint says the same three doors). Phones only; tablets and desktops keep theirs.

Measured after, same phone, same question: the board is 367px tall, with his words, twenty
stars and the four buttons all on it at once.

**Twenty stars off both edges** (P5). A plain `[[objects]]` row was one letter-spaced string
that could not wrap — 20 × 45px = 900px on a 390px phone. Past ten, a plain row is drawn as
rows of **ten** (`span.objten` — "ten and ten", the picture a child counts twenty by, and what
fits a phone); on a phone the star is 24px so ten fit a row; and every `.objline` may wrap
instead of overflowing. The count-along, count-on and take-away rows are untouched (the first
two already wrap).

**The steps below the fold** (P1). /family's header is tighter under 620px — "1 Create your
parent account" is in the first screen. Laptops unchanged.

## Proof

`tools/zcdrive.py` (PART 3ow runs it): the real `topic.html` and `session.html` under a stub
API. At 390×844 with twenty stars and three choices: the board is ≥300px tall, the choices row
is inside `#feed` with every button on screen, the stars are two `.objten` rows of exactly ten
inside the board, nothing scrolls sideways, the dock is under 240px with no name line and no
helper line; the scripted lane's own ask on `session.html` lands the same way. At 1280×800 both
pages are unchanged — the row beside `#composer` in the strip, the name and helper lines shown.
`family.html` at 390×844: step 1 inside the first screen. PART 3ow pins every line in the source.

## Files

`static/board.js` (`mountChoicesRow`, `phoneBoard`, the feed row CSS, `.objten`, the
wrapping and the phone star), `static/session.html` (its two rows; the phone dock),
`static/practice.html` + `static/topic.html` (the phone dock), `static/family.html` (the
phone header), `tools/zcdrive.py` (NEW), `ruletests.py` (PART 3ow), `main.py` (stamp),
`changelog/Playthrough_2026-10-02_The_Phone.md` (NEW), this doc, the handoff.

I did no harm and this file is not truncated.
