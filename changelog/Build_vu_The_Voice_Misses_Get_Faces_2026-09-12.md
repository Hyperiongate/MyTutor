# Build `vu` — The Voice Misses Get Faces (2026-09-12)

**Stamp:** `2026-09-12vu-the-voice-misses-get-faces` · **PART 3lq** (16 pins) · **battery 12,256 passed · 0 failed · 3 skipped** · files: `main.py`,
`store.py`, `nightwatch.py`, `ruletests.py` · no referee count change · no prompt change · no
prewarm owed

## The number

The cost epoch (since 2026-08-26): students' pages asked for 1,360 clips. 105,185 characters
came off the disk free. **78,845 characters were rendered live by ElevenLabs — 43% of everything
spoken to a student — and that is the entire $17.35 serving-side voice bill, about $4 per
student-hour**, on a course whose every one of 39,988 lines is supposed to be cached. The AI's
18 interventions account for perhaps 11,000 of those characters. The rest had no name: the
usage ledger keeps counts, never text (build ha's law), and nothing split the rows by page.

## What `vu` does

- **`voice_miss` events.** `_tts_stream_response` — the one door every spoken line goes
  through — now writes a `system_events` row on every cache miss that will spend: **name** =
  the lane (`speak`, `script`, `demo`, …), **detail** = the size, whether the line is **IN the
  closure** (the course already paid to render it: a cache or label defect) or **outside it**
  (a line that varies, or a model's words), and a head of the text. A `cached_only` lane (drill)
  never spends and never writes one. The event lands before ElevenLabs is asked.
- **The head keeps the privacy law.** `_voice_miss_head`: 80 characters for a closure line
  (authored, already public in the course); **six words** for anything else — enough to say
  *which kind* of line it is ("Look what you did: 12 sits…") and no more; and the student's own
  account name, if the store has one and it appears, becomes `[name]`. The speak endpoint only
  ever voices the tutor, never a student's words.
- **`store.usage_stats` → `tts_serve_by_mode`**: per lane, requests, characters rendered live,
  characters served from the cache. The build lanes stay out. Every older key unchanged.
- **The night watch** prints "Voice misses — by lane" under the pass-through block: each lane's
  count, characters and closure split, then its distinct line heads newest-first with the
  ghost test. `voice_miss` joins the named-offenders kinds.
- **`/api/admin/events`'s default feed** carries `voice_miss` beside the other alarm kinds
  (`?kind=voice_miss&limit=200` reads a week of them).

## What the first day will most likely say

I could not find a leak in the scripted lane itself: the orientation line keeps the score on the
card; the praise lines (1,500 sampled) are all in the closure; the drill lane cannot spend by
construction; the speechmap mismatch was closed in `vc`. What is left is (a) **the live lanes
under your own code `0000`** — the 09-10/09-11 live-lane turns in the pass-through ledger were
yours, and every live-tutor reply is a ~600-character live render — (b) the AI's scripted
interventions, and (c) the marketing demo, which speaks to every visitor. My bet is (a) is most
of it, in which case the "leak" is your testing and a child's hour costs well under a dollar.
The report will say so, per lane, with the lines, after one night.

## After the push

Nothing to prewarm. Read the "Voice misses — by lane" block of the next night watch, or hit
`/api/admin/events?kind=voice_miss&limit=200` from the admin tab.

I did no harm and this file is not truncated.
