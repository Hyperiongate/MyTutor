# Build xx — The Child-Mode Skin, 2026-09-24

Project 7 of the 09-14 deep dive; the sixth gate build, after three sweep builds in a row
(`xu`, `xv`, `xw`). The deep dive's line: *Entry/Basic sessions get warmer board colour,
bigger tap targets, progress dots for "three in a row" visible during practice, and the
parent-facing helper text removed from the child's screen.* All four, for the two youngest
courses only; Pre-Algebra through Differential Equations are byte-for-byte what they were.

Stamp: **`2026-09-24xx-the-child-mode-skin`**. PART **3ns**. A gate build.

## What the child sees

The lesson page already sets `body.elem-mode` for Entry and Basic (since build `uc`), so every
part of the skin hangs off that one class, and none of it can reach another course.

**① The warm board.** `board-theme.css` has a third block after the white and the dark ones:
on the light board, `.elem-mode` paints the feed a warm cream (`#fff8e8`) with a matching
border. It is scoped with `:not([data-board="dark"])`, so a child who picked the dark board
keeps the navy exactly. No `--bd-<hex>` drawing token is re-pointed — every figure, card and
answer button paints as it does on the white board; only the board under them changes. (The
first cut also warmed the tutor bubble through `--tutor`; the board's bubble reads
`--bd-f2f4ff` since `rq`, so that line did nothing and came out.)

**② Bigger tap targets.** `board.js`'s `ensureChoicesCSS` adds three rules under
`.elem-mode`: the answer buttons are 72px tall at 26px type with a 14px gap (they were 52px
and 20px), and "I'm not sure" grows with them. The base `.choicebtn` rule is unchanged, and
PART 3ns pins it by its exact text.

**③ Three-in-a-row dots.** The engine's promise since `ri` — "three right answers in a row
and we're done" — is on the screen now: a pill in the chip row with three dots that fill
as the run grows, and a label ("1 of 3 in a row", then "3 in a row!"). The count is the
ENGINE's: `main.py`'s new `_script_practice(sess)` reads `state["streak"]`, `state["phase"]`,
`finished` and the lesson's `mastery` after the turn is graded, and `_with_practice` attaches
`{"practice": {"phase", "run", "need", "on"}}` to **every** `/api/script/start` and
`/api/script/answer` response. The two endpoints became thin wrappers (`script_start` →
`_script_start_lesson`, `script_answer` → `_script_answer_turn`) so the field rides all nine
of `script_answer`'s returns from one line — the drift `script_warm`'s own note warns about.
The page's `renderRunDots` draws the field only for `IS_ELEM` and only while `on`.

`on` is true in the practice phase, and — once the run is full — through the reason
question and the mastered end, so the three lit dots are on screen for the lesson's last
words. It is never true in the guided pairs, never in a times-table lesson (the pass is a
pass, not a streak — `sz`), and never on a still-learning end with a short run. A wrong
answer resets the dots to none, as the star resets. The field is fail-open: any error and the
page simply shows no dots.

**④ The helper text leaves.** The "🎙️ How to answer: …" line above the composer and the
`#hint` sentence ("Your turn — tap the microphone to talk, or tap "Type my answer" below")
are for the very first answer. `sendToTutor` — the one door every answer goes through — sets
`body.elem-settled` on the first message of the visit, and CSS hides both from then on, for
`elem-mode` only. The tour, the welcome tip, the talk button's own label ("Tap to talk" /
"Tap when you're done") and the status line are untouched, so the child still sees whose
turn it is.

## Proved

`tools/xxdrive.py` (in the repo, the `pwdrive.py` pattern) serves the real page with a stub
API and drives it twice in headless Chromium: **Entry** — cream feed (`rgb(255,248,232)`),
navy on the dark board, 72px/26px buttons, no dots before practice, one lit dot and "1 of 3
in a row" after the first graded answer, the helper text visible before and `display:none`
after; **Pre-Algebra** — white feed, navy dark board, 56px/20px buttons, no dots even with
the server saying `on = true`, no settling, the hint still there. PART 3ns runs it every
battery (a Playwright skip where the browser is absent), and drives the engine through the
TestClient: an Entry lesson to its end (pairs off → practice on, run 0 → 1 → a wrong answer
→ 0 → 1, 2, 3 with the end step), a reason lesson keeping the three lit dots through the
question and the end, a times-table lesson never on, and a still-learning end with a short
run staying dark.

## Counts

Course lines **40,495 — unchanged**; speechmap 941 (no spoken line changed).
`tools/pinscan.py`: 0 stale pins. The 3hp board-literal sweep passes: the warm block lives in
`board-theme.css`, not in the page's `<style>`, and the dots' CSS is a chip-row rule.

## After the push

`/health` = `2026-09-24xx-the-child-mode-skin`. **Nothing to prewarm** — no spoken line
changed. Open an Entry lesson and look: the cream board, the big buttons, and after the pair
questions a pill at the top right that fills star by star. Then the next sweep build (Basic
41, Geometry 36, Calculus 46, Entry 19, or Pre-Calc's fourth), then screencheck's two rules
(#6).

## Files

`main.py` (`_script_practice`, `_with_practice`, the two wrappers; stamp), `static/session.html`
(`#runDots`, `renderRunDots`, `elemSettle`, the CSS), `static/board.js` (the `.elem-mode`
choice rules), `static/board-theme.css` (the warm block), `tools/xxdrive.py` (NEW),
`ruletests.py` (PART 3ns), this doc, the refreshed `START_HERE_Handoff_2026-09-24.md`.

Battery on the frozen copy, 2026-09-24: **13,030 passed · 0 failed · 3 skipped** (13,008 at `xw`), second run clean — the first caught two of my own words: a JS comment saying "child" (the house word is student, PART 3ia) and a fallback line reordered past its pin (3fe); both fixed before the rerun.

I did no harm and this file is not truncated.
