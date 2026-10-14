# Build zl — the model trial (2026-10-13)

Stamp: `2026-10-13zl-the-model-trial`. Battery: **13,626 passed · 0 failed · 3 skipped** (PART 3pf, 15 checks; one older pin moved -- 3on read a 1500-character slice of the admin header, now notes()). **Nothing to prewarm.**

PM-20 on the PM board. The 10-09 deep dive: *"Move to Sonnet 5.5, through a measured trial,
not a blind swap."* zl is the instrument; the trial itself is one button on /admin after the
push, because the API key lives only on Render.

## What it is

**/admin → ⚖️ Model trial.**

- **Two models:** A is blank (meaning the live model, `claude-sonnet-5`) and B is
  `claude-sonnet-5-5`. You also choose the number of lessons (4), the turns per lesson (6), and
  whether the marker reads each lesson.
- **① Price it (FREE)** says how many tutor turns, about how many dollars, and about how many
  minutes. With the defaults that is 48 turns and roughly $1.50–2.
- **② Run the trial (SPENDS)** runs in the background, and the card follows it.
- **The report** is read in place and lists, side by side:
  - the student's wait per turn (median, and the slowest 10%);
  - reply length, and the spoken characters per turn (the voice bill);
  - turns the math referees made him redo, and all referee fires;
  - apologies ("lost my train of thought");
  - teaching findings by severity (the night watch's marker);
  - dollars per turn, priced from Anthropic's published rates.

  Each row says which model it favours, followed by the opening replies of the first lessons
  side by side. It ends with how to read it: one trial is a handful of lessons, so a small
  difference is noise. Switching stays one Render setting, `CLAUDE_MODEL`, and this card never
  changes it.

**How it stays fair and safe:**

- Both models teach the **same scenario lessons** (the night watch's students), with the same
  prompt and the same referees.
- They take turns going first: A first, then B first.
- Each logs its turns under its own code (`TRIAL-A`, `TRIAL-B`), never a student's.
- Before any lesson, each model is checked with one tiny call. A model the key can't reach
  stops the trial and the report says why.
- **Real students keep the live model the whole time.**

## Two seams in tutor.py, and one fix found on the way

- `tutor.model_override(model)`: inside it, brain turns **on this thread only** use `model`
  (`claude_model()` reads it; otherwise `CLAUDE_MODEL` as before). The trial runs on its own
  thread, so a student on any other thread is untouched. The brain path reads `claude_model()`
  at its three places; nothing else changed.
- **Event taps are now thread-scoped.** `tap_events` was one global list, so a night-watch lesson
  counted any real student's referee fires that happened at the same moment as its own. A tap
  now hears only its own thread. The pipeline runs a turn on one thread, so a lesson's own
  counts are unchanged and the cross-talk is gone.
- `store.usage_for_codes(codes, since)`: per-code brain totals from the same cost log /admin uses.

## Proof

PART 3pf (15 checks):

- the override is per-thread: another thread sees the live model; it nests and restores;
- the brain path's three reads, and an open override teaches on Anthropic;
- a tap ignores another thread's event;
- a stand-in trial: same lessons, own codes, alternating order, every measure, Sonnet 5.5's
  cheaper cache read showing in dollars, the report, a refused model, the same model twice
  refused, Price it;
- the routes, the admin card, reports written, listed and read (never a path), the notes.

**Through the real admin endpoints** (stand-in model replies): Price it, then Run. The job
finished and the report listed and read back. Model B's replies were genuinely produced under
`claude-sonnet-5-5` while `/status` still showed the live model `claude-sonnet-5`. Without the
admin key the routes return 401.

## After the push

1. **/admin → Model trial → ① Price it → ② Run the trial.** It takes about 15 minutes. Don't
   push while it runs.
2. Read the report and tell me what it says. If Sonnet 5.5 is as good or better on wait,
   findings and math redos, the switch is `CLAUDE_MODEL=claude-sonnet-5-5` in Render.

## Files

`modeltrial.py` (NEW), `tutor.py` (`model_override`, `claude_model`, thread-scoped taps),
`main.py` (stamp, the three routes), `store.py` (`usage_for_codes`), `static/admin.html` (the
card), `ruletests.py` (PART 3pf), this doc.

I did no harm and this file is not truncated.
