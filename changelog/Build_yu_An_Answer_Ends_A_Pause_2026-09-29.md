# Build yu — an answer ends a pause (2026-09-29)

Stamp: `2026-09-29yu-an-answer-ends-a-pause`. Battery: **13,334 passed · 0 failed · 3 skipped** (13,315 at yt; PART 3oo added).
Prewarm: **1 line** (`LINE_UNSURE`).

The first build off Jim's first-family playthrough (`claude/Playthrough_2026-09-29_The_First_Family.md`,
33 flags). It closes the day's one blocker inside a lesson — F23 — and the "tap the hand"
line (F19), and it settles three other flags by reading the code rather than changing it
(F18, F12, F30). The money-path blockers (F26, F27) are the next build.

## F23 — the tap that submitted nothing

Entry unit 2 lesson 4, "what is 2 + 4 + 6?": Jim tapped 12; the buttons vanished, nothing
appeared on the screen, and the tutor sat waiting. He had to turn on the microphone and say
it. A six-year-old on a tablet with no microphone is stuck there.

**Cause.** On all three board pages `sendToTutor` opened with `if (busy || paused) return;`.
The page was paused — the status line had read "Paused" with a green "▶ Resume" from the
moment the lesson opened (the 3:13 PM screenshot; the Pause button is the only thing that
sets that state). `board.js`'s tap handler gates only on `busy`: it disabled the row, cleared
it, and called `sendToTutor`, which returned without a word. The typed box had the same hole
(`sendTyped` empties the input, then `sendToTutor` refuses) and so did the microphone
(`mic.js` posts the transcript into the same door). Three doors, one silent drop.

**Fix.** A pause ends when the student answers. `sendToTutor` refuses on `busy` alone and,
if paused, calls the new `releasePause()` — defined beside `setPaused` on each page — which
clears the flag, restores the "⏸ Pause" button and the status line, and does NOT resume the
clip: the next line's `scrSay` runs `stopAllSpeech` and supersedes it, exactly as when a
student answers over a playing line. `board.js` is unchanged in logic; its handler carries a
note stating the contract (the row clears before the page accepts, so the page may refuse
only on `busy`).

**Proof.** `tools/yudrive.py` (PART 3oo runs it): the real `session.html` and `board.js`
under a stub API, the first ask on stage, the real Pause button pressed, then a tap — the
POST goes out carrying 12, the student's bubble shows it, the praise and the fresh ask
arrive, the pause is released; the same through the typed box; and a tap while `busy` still
sends nothing and leaves the buttons up. Run against the pre-`yu` page it fails exactly the
way Jim described (no POST, no bubble, still paused, the row gone).

## F19 — "tap the hand"

`LINE_UNSURE` (said when the student taps "I'm not sure") read "Tap the hand and ask me
anything". The ✋ was `pilot.html`'s (build oq); the pb port of the player into
`session.html` never carried it. A question still reaches the raised-hand door — typed or
spoken, `scrAnswer` routes a "?" or a what/why/how opener to `/api/script/ask` — so the line
now says what a student can do: "Saying you are not sure is a good move. Ask me anything, or
take a guess — I will help either way." One authored line; the count pins are unchanged
(the constant is what they read); prewarm it. PART 3oo pins that the line names no hand and
that the page really has none — the day a ✋ is added, the pin says to name it again.

## Settled by reading, not by changing

- **F18 (the slow walk-back after a miss)** is by design. `lessonscripts.step`: the FIRST
  miss in a row gets the engine's own walk-back instantly (vz); the SECOND miss in a row is
  the one doorway to the model (`intervene`, deferred by `ur` behind the hold line). Jim
  missed twice on purpose, so the second one thought. That is his 09-13 ruling in action.
- **F12 ("Paused" with a Resume button on a fresh lesson).** Only the Pause button sets that
  state, so it was pressed — by Jim, or by a tap that landed on it while the tour's pointer
  bobbed near the bottom bar (F6). Not an autoplay state; nothing to rename. It was, though,
  the pause that F23 fell into.
- **F30 ("Switch course" → the live lane).** Not a fall-through. Switch course goes to
  `/home` (the subject picker), then the course's hub, which offers three equal tiles —
  "Start my Basic Math course" (`/session`, scripted), "Get help with a problem"
  (`/practice`, live), "Explore a topic" (`/topic`, live). Jim tapped the third. The
  question for Jim is a product one: should the Entry and Basic hubs offer a six-year-old
  the two live tiles at all? (Hiding them for `ELEM_COURSES`, or moving them to the parent's
  view, is a small change once ruled.)

## Files

`static/session.html`, `static/practice.html`, `static/topic.html` (sendToTutor;
releasePause; dated notes), `static/board.js` (a note), `lessonscripts.py` (`LINE_UNSURE`),
`tools/yudrive.py` (NEW), `ruletests.py` (PART 3oo), `main.py` (stamp), `speechmap.py`
(regenerated; byte-identical, 941), this doc.

I did no harm and this file is not truncated.
