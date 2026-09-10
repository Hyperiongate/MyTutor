# Build `uy` — The demo keeps time, 2026-09-10

Your five demo defects. **Not one of them was a timing tweak** — four were the same
mistake in different clothes: *something with no owner*. A spoken line had no owner, so
another line's events landed on it. An audio element had no owner, so an abandoned clip's
error was charged to the line that abandoned it. A board flip had no owner in the
sentence, so it ran when the sentence was over.

**Battery 11,619 → 11,646 · 0 failed · 3 skipped**, twice, md5-identical.
**Stamp:** `2026-09-10uy-the-demo-keeps-time`. On disk, unpushed, on top of `ux`.
**⚠️ PREWARM after this push** — 212 new voice lines across `ux` + `uy`, about **$3.64**.

Every number below was **measured in a real browser**, before and after, by a harness
that supplies what this container cannot: generated clips of a known length, and a
`speechSynthesis` that behaves like Chrome's — including the ~15-second cutoff that turns
out to be the engine of defect ③.

---

## ① "voice doesn't match mouth"

**It has never matched.** Build `sc` (2 September) declared `usingAnalyser`, `analyser`
and `timeData` on this page specifically so `cadabra.js` could read the real waveform.
It could not. Everything on `/demo` runs inside **one IIFE**, so those three were
*locals*, and `voiceLevel()`'s `typeof analyser !== "undefined"` was false on **every
frame of every line** from `sc` until today. The pencil has been running the synthetic
flap the whole time — moving while he talks, blind to syllables and pauses.

| | what cadabra.js could see |
|---|---|
| **before** | `undefined`, `undefined`, `undefined` — nothing on `window` |
| **after** | all three, and `usingAnalyser: true` while a clip plays |

`voice.js` gets away with the identical three lines because it is a classic script and
its top-level declarations land in the shared script scope. This page's do not.

**And the pin that should have caught it was requiring the defect** — it asserted the
literal `var audioCtx=null, analyser=null, timeData=null, usingAnalyser=false;`. A pin
that copies the code back to itself proves the code has not changed. It never proves it
works.

---

## ② "Mr Cadabra should start the demo right in the middle of the screen"

He was parked at his home corner until the *first tour stop* flew him to the Curriculum
button — so the host of the demo spent his own welcome off to one side.

| | where he stood, 1.2s after Start (1440px wide) |
|---|---|
| **before** | x = **1360** — 640px off centre, at the right edge |
| **after** | x = **730** — **10px off centre** |

And the **front-door path** gets a beat to see it. A visitor arriving from the home page
skips this page's welcome entirely, so without a pause the first tour stop flew him away
inside half a second — which is the path you were on.

---

## ③ "After abrabot talked, mr cadabra's voice was silent for the next item in the sidebar then started again later"

Here is the recorded before-timeline, from the harness:

```
 86.36s  Abrabot's cameo starts speaking (45 words)
101.36s  Chrome stops the utterance.  onend never comes.
112.51s  the tour's safety timer gives up and moves on
112.51s  clip starts: "Right under it, Explore a topic..."
112.93s  clip starts: "And the Final Exam..."      ← 0.42 SECONDS later
```

`lineDone` was **one global slot with no owner**. When the next line called
`speechSynthesis.cancel()`, Chrome released the stalled utterance by firing its `onend`
— straight into the *next* line's callback. The tour advanced twice, and the clip it
skipped was replaced on the shared `<audio>` element before a note of it played.

After: `112.65s` starts, `124.06s` ends. **It plays in full.**

The fix is one idea, and it fixes ⑤ too: **every spoken line is stamped with a number,
every handler carries the number it was started with, and anything arriving for an older
number is dropped.** An interruption detaches its handlers *before* silencing, so it
cannot raise an event at all. Chrome's 15-second cutoff is separately nudged.

---

## ⑤ "After a sample problem, fell back to browser's voice"

Two independent causes, both closed.

**(a) The one you heard.** `/demo/lesson` — the real-lesson page the level picker sends
you to — **ends** on a line written in the page:

> *"That is how every lesson in my classroom starts. Shall we look around, or try another level?"*

That lane is **cache-only on purpose** (a visitor must never be able to make the paid
renderer run). A line that belongs to no lesson is in no closure, was never rendered, and
so fell to the browser voice **every single time** — at the exact moment a visitor has
just decided the product is real. It is a `STANDALONE_LINE` now, like Abrabot's
introduction and the seam line, carried byte-for-byte by the page.

**And nothing was watching for that.** `voiceclosure.py` (new) reads every page in
`static/`, finds the string literals that reach a speech call — including through a
variable — and reports the ones the closure does not hold. **Zero** on the cache-only
pages now. Two remain on `challenge.html`; see *Still open*.

**(b) The one that was waiting to happen on the tour.** Replacing `src` on the shared
audio element makes the browser raise an error for the clip being abandoned — and
`onerror` by then points at the **new** line's failure handler. Three of those and the
page gives up on your voice and hands the rest of the demo to the flat browser one. A
superseded line can no longer fail.

---

## ④ "the actuall change lagged by about 5 seconds. Needs to happen with the voice."

The board peek ran from the stop's `after` hook — which **by definition cannot fire until
the line is over**, and *"Watch: white... and back to dark"* sits three-fifths of the way
through an 18-second line. The lag was the rest of the sentence.

| | when the board turned white |
|---|---|
| **before** | **18.48s** of an 18.48s clip — the very last moment, and it turned back to dark 1.6s into the silence |
| **after** | **9.36s** of 18.48s — half way through, under the words |

It is a **cue** now: armed on the phrase it belongs to, and timed from **the clip's own
clock** rather than from wall-clock — because a clip's real duration often arrives *after*
play has started, and the first cut re-armed from "now" each time it learned a better
number, which pushed the cue late by exactly however late the duration was.

If the cue never fires at all, the line's own end fires it — which is exactly where it
used to fire. **This can only ever be earlier, never later and never never.**

---

## Files

`static/demo.html` · `static/demo-lesson.html` · `lessonscripts.py` (the standalone
line) · **`voiceclosure.py` (NEW — `git add -A`)** · **`tools/demoprobe.py` and
`tools/cadcentre.py` (NEW — the harnesses, so the measurements can be repeated)** ·
`ruletests.py` (PART 3ku + seven pins repointed) · `main.py` (stamp).

The tour's **stops, lines and order are untouched**, and no voice line on `/demo` changed.

---

## How it was checked

- **Measured, not argued.** `demoprobe.py` drives the whole tour in Chromium with
  generated clips and a Chrome-shaped `speechSynthesis`; `cadcentre.py` measures where
  the pencil stands. Both were run against the page **as it shipped** and against the
  fixed page — every number in this document is one of those runs.
- **Battery 11,646 · 0 failed · 3 skipped, twice, md5-identical** — and the two runs
  straddle a change to the harness files, which is its own small proof that nothing in
  `tools/` reaches the build.
- **Five failability seams**, each restored after, each failing **by name**: the analyser
  trio put back inside the IIFE, the `stale()` guard removed from the clip's failure
  path, the board peek returned to an `after` hook, the closing line taken out of the
  closure, and the centring call removed.
- ⚠️ **The audit's own first cut reported the file it was written for as clean** — its
  regex spliced a shared string pattern in after a capture group, so the closing
  backreference matched the *variable name* instead of the quote. Fixed, and pinned with
  a control that proves the variable path is really read.

---

## Laws this build paid for

- **A pin that requires the code as written proves nothing.** `sc`'s pin asserted the
  exact declaration that made the mouth blind, and passed for eight days.
- **Timing bugs are usually ownership bugs.** One global callback slot and one shared
  audio element produced two of the five defects; neither needed a delay adjusted.
- **A hook named `after` runs after.** If the words describe something happening *now*,
  the thing must be tied to the words, not to the end of them.
- **Check what a check can see before trusting what it says** — again. This is the same
  law `uw`'s digit-blind giveaway audit paid for, in a different disguise.

---

## Still open

1. **`challenge.html` speaks two lines of its own** — *"Welcome back — picking up right
   where you left off. Question N."* and *"Alright — let's map out your whole course..."*
   That is the course assessment, where rule 18 gives the character no part at all, and
   the first line interpolates the question number so it could never be pre-rendered.
   Reported by the audit, deliberately not blocking. **Your call** whether the assessment
   should speak at all.
2. Everything still open from `ux` — the five ops with no walk-back picture, the 21
   `wordaudit` candidates, and the 78-word reading-level list.

I did no harm and this file is not truncated.
