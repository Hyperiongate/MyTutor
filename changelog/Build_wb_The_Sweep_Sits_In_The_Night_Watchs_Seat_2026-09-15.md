# Build wb — The sweep sits in the night watch's seat (2026-09-15)

The first course sweep (`wa`) read 36 Entry lessons and got an answer for one. The other 35:
*"reviewer did not return JSON: "* — an **empty** reply, 35 times. 809 seconds, so every
call went out and every call was billed.

Battery: **12,374 passed, 0 failed** (frozen copy, 2026-09-15).

## What happened

I had wired the sweep to the **Anthropic** judge transport. The model spent its whole
2,000-token output budget thinking and never wrote a word; the reply came back 200 with no
text block, and the transport handed `""` up as if it were an answer. The one lesson that
succeeded — `sharing-fairly` — is the shortest in the course, the only one the model finished
inside the budget.

The project already knew this failure. The **OpenAI** transport — the seat the night watch has
marked every night's transcripts with since build `iu` — has guarded exactly this since build
`fe`: *"a reasoning model can fail quietly: 200, finish_reason=length, an empty message,
because the whole budget went to thinking"* → one retry with a roomy budget. I chose the one
seat that did not have the guard.

## What changed

**The sweep sits in the night watch's seat.** `_sweep_judge` now routes through
`lessonaudit.JUDGE_PROVIDER` — OpenAI by default, the transport that is proven nightly — with
a 4,000-token budget (a whole lesson's findings are longer than a night's).
`COURSESWEEP_JUDGE=anthropic|openai` on Render overrides the seat for the sweep alone. The key
check follows the seat (an Anthropic key does not satisfy an OpenAI seat), the price line on
the card says which seat and model will read the course, and the report says who read it
(*"Read by: openai · gpt-4.1"*).

**The Anthropic seat gets the guard too.** `lessonaudit._anthropic_judge` now treats an empty
reply as what it is: one retry at four times the budget (at least +6,000), then an error that
names the model and the stop reason and says what to do. It can never again return `""` as a
success. The night watch's own seat is untouched.

## After the push

Refresh `/admin`, run the Entry sweep again from the same card. The price line will now read
*"read by openai (gpt-4.1)"*. It will cost about what the first one did.

I did no harm and this file is not truncated.
