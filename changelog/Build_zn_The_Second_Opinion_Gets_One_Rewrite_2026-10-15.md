# Build zn — the second opinion gets one rewrite (2026-10-15)

Stamp: `2026-10-15zn-the-second-opinion-gets-one-rewrite`. Battery: **13,645 passed · 0 failed · 3 skipped** (PART 3ph, 13 checks; two older pins re-pinned). **Nothing to prewarm.**
Builds on zm, which is on disk and not yet pushed. One push carries both.

PM-21 on the PM board (re-scoped 10-14 to make the live turn faster safely).

## What the numbers said

The **💵 Cost & verifier** card, 7 days to 10-14 (all 48 tutor turns were the model trial):

- The median turn was 11.4 s, the slowest 10% took 31.7 s, and the slowest turn took 82 s.
- **Retries were 37.2% of all turn time**, an average of 6.4 s per turn. Every retry is a whole
  new reply from the model.
- The second opinion's read itself is cheap: 1.3 s on Claude Haiku 4.5, 7.7% of turn time.
- **12 replies shipped with a known finding, and 10 of them were the second opinion's.** In
  each, it objected, the tutor rewrote, it objected again, the tutor rewrote again, and the
  last draft shipped with the objection still standing.

Those 10 turns paid for three replies and two extra reads, and gained nothing over sending
the second draft. They are the 30–82 s turns.

## What changed

**A second-opinion objection now buys one rewrite per turn, not two.** If the rewrite draws
another objection, the turn ends there. It ends exactly the way an out-of-attempts turn
always has:

- the least-bad draft ships;
- the `pass_through · livecritic` event names it;
- the floor still withholds any draft that would teach something false.

**What did not change:**

- The second opinion still reads every draft the other checks pass. Its objections are still
  recorded, still help choose which draft ships, and still show on Telemetry.
- **The math checks and the wording checks keep all three attempts.** A reply whose math is
  wrong never reaches a child.
- A clean first draft ships exactly as before, after one call.

**The setting:** `LIVE_CRITIC_RETRIES` in Render.

- Unset means **1**, the new default.
- **2** is the old behaviour, exactly.
- **0** makes the second opinion a recorder only, with no rewrites.

The **Second opinion** tile on /admin now ends with "· 1 rewrite per objection", so the
setting in force is visible.

**One honest number fixed on the way.** A turn that ran out of tries logged "3 attempts"
on its usage row whatever happened. It now logs the attempts actually made: 2 for a turn the
new limit settled early, and still 3 when all three were used.

## What to expect

On the 10-14 numbers, about 1 turn in 5 drops one whole reply, and those are the slowest
turns. The median turn barely moves, because most turns were never touching this. The slowest
10% should fall the most. Read the same card after a few days of real lessons.

**The Render setting, separately (Jim):** `LIVE_CRITIC_MODEL=claude-haiku-5-5`, the newer Haiku
the safety net already uses. If you change it, also set the two critic price settings so the
dollar figure on the tile stays right: `CRITIC_IN_USD_PER_MTOK=0.10` and
`CRITIC_OUT_USD_PER_MTOK=0.50`. If the model name is ever refused, the code already falls back
to the main model on its own.

## Proof

PART 3ph runs the real reply pipeline with stand-ins for the model and the checks:

- The limit: unset is 1, then 0, 1 and 2 as set; out-of-range values are clamped; nonsense
  falls back to the default.
- A clean draft: one call, no event.
- One objection and then a clean rewrite: the rewrite ships.
- **Two objections: settles after two drafts, the newer ships, logged as 2 attempts.**
- `=2` reproduces the old three drafts exactly.
- `=0` makes one draft that ships with the objection recorded.
- After the second opinion's rewrite, a math error still gets its own retry.
- A wrong-math draft never ships.
- The wording checks keep all three attempts.
- The floor is untouched.
- The tile shows the limit, and the dated notes are in.

**Two older tests re-pinned on purpose:** px's and sj's "three critic objections, the newest
ships" now run with `LIVE_CRITIC_RETRIES=2`, the old behaviour, which the setting must still
reproduce.

## Files

`tutor.py` (`critic_retry_budget`, the loop, `_settle` logs the attempts made), `main.py`
(stamp, `critic_seat.retries`), `static/admin.html` (the tile), `ruletests.py` (PART 3ph and
the two re-pins), this doc.

I did no harm and this file is not truncated.
