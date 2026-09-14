# Build vz — Phase A: the scripted second explanation (2026-09-14)

Jim's design, in his own words (09-13): *"everything should be scripted the first time
around… somebody gives a wrong answer, explain what we just explained slightly differently…
only then if they miss the second time do we need to bring the AI in."* Plus the 09-13 ruling:
the redo is a **fresh** problem of the same shape, never the one they have just watched solved.

Battery: **12,333 passed, 0 failed** (frozen copy).

## What happens now on a wrong answer

The **first miss in a row** is answered by the engine itself. It speaks its own worked solution
of the very problem the student missed — the same spoken line and the same board the walk-back
has always drawn — and then asks a **fresh problem of the same shape** from the bank. No model
is woken. The child is never left holding an uncorrected error.

The **second miss in a row** opens the AI's door exactly as it always did: the same intervene
step, the same context, the same engine-chosen retest, the same `resume`. Nothing downstream of
that door changed — not main.py, not the session page, not the deferred re-teach lane.

A right answer puts the counter back to zero, so a later miss gets the engine's explanation
again rather than the model.

## What it costs, and what it saves

**Audio: six clips.** That is the whole bill. The worked lines the second explanation speaks
were already rendered — and the reason is a nice piece of luck that I measured rather than
assumed: the 48 lessons without `show_work_on_correct` are *exactly* the 48 whose ops have no
worked generator at all, so every worked line that can now be spoken was already in the closure.
The only new lines are the two frames (three openers, three hand-overs), and none of them
carries a number, so six clips serve all 360 lessons. Course lines 39,988 → 39,994; closure
40,242 → 40,248.

**Model turns: measured on an all-wrong walk, one where the old engine spent two.** For the far
more common case — a child who misses once and then gets it — the model is not called at all
where it used to be called every time. That is the cost lever you were after.

## The ladder now means what it is named for

`interventions` counts the times the **model** had to step in. The scripted explanation is not
one, so it sits above the ladder: a student who misses and recovers costs the ladder nothing. A
student who keeps missing still reaches the AI every second miss, still drops a level every
second AI turn, and still meets the warm close — and `MAX_PROBLEMS` is the hard floor under all
of it (at the cap there is no fresh problem, so the old path runs and `resume` ends the
practice, precisely as before).

## The opener moved — all 320 generators

Every worked line opened "Look what you did: ". That is written for a right answer, and the
same line now answers a wrong one, where it is simply false. It is now "Here it is, step by
step: ". The praise line above the walk-back still does the celebrating on a right answer, which
is where the credit always lived.

The engine had already made this exact judgment once, years of builds ago, and said so in
`_table_miss`'s own docstring: *"Never 'Look what you did' — the student did not."* The
generators now agree with it.

Same line count, same clips re-rendered — **the voice cache does not grow**, which is what
decided it: the alternative (a second opener for the re-teach) would have added about a
gigabyte and pushed the cache past its 8 GB cap.

## One tripwire raised, in writing

The two frames are spoken *inside* a lesson, so they belong to every lesson's closure the way
`LINE_WRONG` always has. That added ~290 characters to each, and the same three calculus
lessons that the `us` note names crossed the per-lesson ceiling again (24,577 / 24,562 / 24,560
against 24,500). The ceiling is 25,000 now, with its ledger entry. The dollar bar did not move
and did not need to: the worst lesson is $5.41 against the same $5.50. A lesson is never
trimmed to duck a tripwire.

## After the push

Run the prewarm once. It will list **six** lines (plus vy's one roots line and vw's 254 demo
lines if those have not been rendered yet). Everything else this build speaks was already
cached — but note that the 3,686 worked lines were **re-rendered under new text**, so the
prewarm will also list those: same count, replacing the old clips rather than adding to them.

## What Phase A does not do

Phase B (authored reteach beats per lesson, rather than the generated worked solution) and
Phase C (worked generators for the 48 lessons that have none) are still ahead. The 48 lessons
without a worked generator keep the old path on the very first miss, which is the honest
fallback until Phase C gives them one.

I did no harm and this file is not truncated.
