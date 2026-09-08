# CHANGELOG -- ruletests.py  (notes rolled out of the file's header)

Moved out of `ruletests.py` on 2026-09-08 (build ui): every CHANGE NOTE dated before 2026-09-01 -- 241 entries, VERBATIM, in the order they sat in the file (newest first). The 79 notes from 2026-09-01 on stay at the top of `ruletests.py` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
#   2026-08-31  BUILD rd -- PART 3he: the main road moves the star. The scripted lane
#               grades every tap in code and never emits [[mark]], so today_streak moved
#               neither up nor down there (measured, then watched live: a wrong tap fired
#               the intervention and the chips sat still). main._script_streak() bumps on
#               a correct answer (store.bump_today_streak, new -- today_of=(1,1), NO
#               counters) and resets on any wrong tap, graded at the ENGINE'S OWN LINE
#               (pending ans() vs the tapped value, before step() consumes it; redos where
#               code already grades them; unheard moves nothing). The fresh pair rides
#               every /api/script/answer response as "streak"; session.html feeds it to
#               the chips. Quiz lane deliberately EXCLUDED (assessment, qz's own ruling).
#               _RD_STREAK drives it end-to-end against real endpoints and a throwaway DB.
#   2026-08-31  BUILD rc -- PART 3hd: the star falls when the child slips. Jim's ruling: a
#               miss is ANY WRONG TAP -- watched live, a deliberate miss carried no tag,
#               nothing fired, and the streak climbed straight through. Three doors, each
#               pinned: the prompt's new [[miss]] tag (mirror of [[nice]], REQUIRED, all
#               copies); the pages post {miss:1} and /api/mark's new branch resets via
#               store.reset_today_streak (today-streak ONLY -- counters and accuracy
#               untouched, proven end-to-end in _RC_SLIP against real endpoints and a
#               throwaway DB); and the CODE FLOOR, tutor.answer_slip in the chat handler,
#               grading bare answers against computable pending asks (the qw/ra parsers,
#               one grammar) -- cautious in the cautious direction: sentences,
#               uncomputable asks and same-direction synonyms are never slips.
#   2026-08-31  BUILD rb -- PART 3hc: the chip says what it counts. Jim on the qz streak
#               chips, live: "there's nothing that says what those are." The classroom
#               pills explained themselves only in hover tooltips -- a child never hovers,
#               a tablet can't. Each pill now carries a visible 9px label under its number,
#               in the dashboard banner's OWN words ("days in a row" / "right in a row
#               today"), pinned in both files so the two surfaces never teach two names for
#               one number. Markup/CSS only; ids, render/bump wiring, tooltips and 3ha's
#               pins untouched (node dry run drove the unchanged JS against the new
#               structure first). Battery tile pins re-synced.
#   2026-08-31  BUILD ra -- PART 3hb: the leftover gets its buttons. Jim, live on
#               entry/basic the same evening qw deployed: "some of the times it's missing
#               bubbles." Measured first: referee 58 FIRED on every shape he saw and qw's
#               repair refused them all -- it only knew plain a-op-b arithmetic, so
#               comparison asks, either-or relation asks, one-more/one-less and
#               comes-after/before all shipped bubble-less as counted residue. tutor.py's
#               NEW _rb_counting_shapes() closes those four classes, still
#               computed-never-guessed (a comparison offers the question's OWN pair, so
#               the true answer is present by construction; N±1 is computed; X == Y,
#               below-zero and every word problem still refuse), FINAL SPOKEN ASK ONLY.
#               The PART proves each class repairs, each refusal refuses, the arithmetic
#               branch is untouched and consulted first (a boundary-split source pin, per
#               the qz law), the pt grid law holds over 0-20 for all four shapes, and
#               referee 58 + the choices-answer referee go silent on every repaired reply.
#               Battery tile pins re-synced.
#   2026-08-31  BUILD qz -- PART 3ha: a streak a child can see today. Jim wants a prominent
#               bar on BOTH the dashboard and the classroom page showing (1) the day streak
#               (already tracked) and (2) problems answered correctly IN A ROW TODAY, reset
#               to 0 the instant a problem is missed -- a live motivator, not a running
#               total. New store.py columns student_stats.today_streak/today_streak_day,
#               written atomically inside the SAME _bump_stats() upsert that already writes
#               the day streak, driven ONLY by record_practice() (per-problem [[mark]]
#               events) -- never by record_check() (a whole unit-check batch score is not an
#               "in a row" event). Read side gates on the stored day == today's stored day,
#               so a stale number from a past day reads back as 0 without needing a write.
#               _QZ_STREAK drives /api/mark/1234 and /api/session/1234 through a real
#               TestClient: builds a 3-in-a-row streak, proves a miss resets it to 0, proves
#               a new stored day restarts (not inherits) the count, proves a stale stored
#               day reads back as 0 with no write, and proves record_check leaves
#               today_streak untouched. Also checks main.py's /api/mark response now
#               carries the fresh today_streak/streak_days (COMPUTED, NEVER GUESSED -- the
#               same reasoning /api/check's best_pct already uses), /api/session's
#               progress.stats now carries stats for the classroom page, and both
#               dashboard.html and session.html ship the new markup/CSS/JS.
#   2026-08-31  BUILD qy -- PART 3ak extended: nightwatch.MAX_MINUTES's default moved
#               45 -> 90 (Jim: "Yes, raise it" -- the 2026-08-31 watch was cut off with
#               2 of the rotation's 12 slots unrun). One pin holds the new default
#               literal, not with a >=, so a revert is caught exactly; two more prove the
#               NIGHTWATCH_MAX_MINUTES Render override still works (set it, reload, read
#               it back; clear it, reload, confirm the new default returns) -- the point
#               of raising a number that is "overridable in Render without a deploy" is
#               that it stays that way. Also: the historical-night near_ceiling check
#               (38.5 min, pinned literal since build gp) was tied to the OLD 45-minute
#               default -- 38.5/45 = 85%, near it; 38.5/90 = 43%, not near it at all, and
#               the card is now correctly telling the truth about that. Rewired to assert
#               the honest new answer (False) plus a SEPARATE positive case computed off
#               nw.MAX_MINUTES itself (85% of whatever it currently is) so the "still
#               warns when truly near ceiling" property survives future budget changes
#               without another literal to go stale.
#   2026-08-31  BUILD qx -- PART 3gz: the verb is the operator. R7 (rule 15's command-ask
#               gate: "Simplify 8/12?" slipped in BOTH word and digit form; final-sentence
#               scoped after the canon sweep caught a mid-turn teaching question; net new
#               canon hits zero), R8 (rule 64's measurement-only probe,
#               probe · expressionswap, reordered vs replaced), and the qask PAIRING pin:
#               session.html calls no quiz endpoint today and handles no qask beat -- the
#               pin fails the day one arrives without the other, which is the trap the
#               measurement found.
#   2026-08-31  BUILD qw -- PART 3gy: the floor under the floor. Referee 58 could only
#               nudge; after three failed attempts a bubble-less question still shipped to
#               a child who cannot type (the watch's 84-replies-a-week number). CODE now
#               repairs it at the moment of shipping, on every exit of _create_verified
#               (one _shipped() door): compute the answer from the reply's own pending
#               problem, append the scripted lane's exact row. The build-pt law is the
#               whole design -- COMPUTED, NEVER GUESSED: word questions, uneven division
#               and negative take-aways ship as before and are COUNTED
#               (pass_through · elembuttons). 22 pins including a 507-case grid proving a
#               built row always holds the true answer.
#   2026-08-31  BUILD qv -- PART 3gx: referees 67 (a slash has no top -- fraction anatomy
#               in top/bottom words over a board that shows 1/4 with a slash and no
#               spoken bridge) and 68 (one board, one triangle -- a second DIFFERENT
#               [[triangle]] with no [[clear]] while the first stands; referee 56 only
#               knew NUMBERED questions), plus funcrule's NOT-NEW gate tightened to
#               NOT-YET-READ (the two-turn hole the watch shipped g(x)=3x-2 through),
#               pinned in funcrule's own PART beside its unchanged old silence.
#               ⚠️ 67's canon sweep caught basic/denominator and basic/numerator -- the
#               cards that TEACH the words -- fixed to the ps standard in foundations.py
#               (two spoken lines changed, two TTS clips re-render). PART 3fx's referee
#               count moves 66 -> 68.
#   2026-08-31  BUILD qu -- TWO FALSEHOOD ROWS FROM THE FIRST HEALTHY NIGHT WATCH, riding
#               PART 3ge exactly as its design demands (one row + a FIRES and a SILENT
#               line; no new referee): division-always-makes-smaller and
#               symbol-read-as-expression. Four FIRES lines (both watch sentences
#               verbatim, plus each shape's second form), four SILENT lines (each row's
#               escape, the authored remainder card whose word order must stay quiet, and
#               the one-sentence both-readings form). The table floor moves 11 -> 13. The
#               existing canon sweep covers the new rows with no new code.
#   2026-08-30  BUILD qt -- PART 3gw: the counting lessons actually count. qs built the
#               count-along and nothing in the canon asked for it, so a child who never
#               answered wrongly (and so never met the AI intervention) would never have seen
#               it. Thirteen authored drawings now count. ⭐ THE PIN THAT MATTERS: every
#               counted card must be one board.js will ACTUALLY count -- it refuses over
#               OBJ_COUNT_MAX things, over one row, or with take=, and falls through to the
#               ordinary drawing, so a card asking for a count-along it cannot have LOOKS
#               right on screen and is wrong in the source for ever. OBJ_COUNT_MAX is read
#               OUT OF board.js rather than restated. The cards left plain are pinned too,
#               with their reasons, because "finish the job" is the obvious next edit and it
#               would be wrong.
#   2026-08-30  BUILD qs -- PART 3gv: count out loud with me, and the 66th referee. The
#               model invented a promise the board could not keep ("point to each one and
#               count out loud with me" over a row of emoji drawn in one instant, as ONE
#               STRING). [[objects ... count="1"]] now lands the things one at a time with
#               a ✓ and a number each, paced to voice.js's new "mt:speaking" event. 28
#               pins, including the three belts that make it ALWAYS FINISH (a fallback, a
#               long stop, and a catch -- the stars are built VISIBLE and only hidden by
#               the script about to reveal them), the three refusals, and the referee that
#               fences the exception: a counted drawing may never sit under the question
#               it is meant to make the child answer. Canon swept 0 of 2,109 cards. The
#               referee count literal in PART 3fx moves 65 -> 66.
#   2026-08-30  BUILD qr -- PART 3gu: the authored question ships its buttons. The scripted
#               player in static/session.html never read step.choices or step.tap_only, so
#               every AUTHORED question in Entry-Level and Basic reached a child who cannot
#               type with no way to answer, while an `ai` intervention had buttons because
#               its tags ride inside step.board. 17 new pins, every one of them read through
#               code_only() -- this build's change notes quote every string it checks, so a
#               pin on the raw file would have passed on the documentation. The PART also
#               WALKS both youngest courses (432 asks) and proves the server ships a tag,
#               with the right answer among the options, for every one of them.
#               ⚠️ TWO OLDER PINS IN PART 3fh WERE INVERTED, NOT DELETED: the bare
#               `else showScrNext();` is now `else if (!boardTaps) showScrNext();`, and the
#               unlock/speak ADJACENCY the flooring pin relied on is now a direct test that
#               nothing is AWAITED in that gap -- a strictly stronger check than the string.
#               Both properties they protected are re-proved, and the beat each one now
#               excludes is pinned on its own line. Methodology tile 7,694 -> 7,724.
#               ⚠️ AND ONE UNRELATED DEFECT THE SECOND BATTERY EXPOSED, fixed in the same
#               sitting because it would otherwise have failed every run from here on:
#               PART 3dm's practice drill posted its rows under the LITERAL day
#               "2026-08-24" and asserted by_day carried it. store.drill_stats() reads a
#               ROLLING seven-day window, so that assertion had a FUSE: it passed for one
#               week after the build that wrote it and then failed for ever. It went red
#               for the first time when the clock crossed midnight UTC between this
#               build's second and third battery runs -- nothing about practice had
#               changed, the calendar had. The day is now taken relative to the run (two
#               days back: inside the window on any day, and never today), with a new chk
#               proving the row still carries the day it was TOLD rather than the day of
#               the run. A test whose result depends on how long ago it was written
#               measures the calendar, not the code.
#   2026-08-30  BUILD qm -- PART 3gp: the quiz says correct, every time (the 65th referee)
#               plus the progress panel Jim could not read. Both from one live Geometry
#               session. PART 3fx's literal referee count moves 64 -> 65.
#   2026-08-30  BUILD ql -- PART 3gk inverted: privacy.html names three processors again,
#               so the DEFAULT state is the gate REFUSING DeepSeek (for the brain seat AND
#               the critic seat), with the other direction proved by mutation. New pin:
#               the gate reads what a PARENT sees -- a change note naming a vendor must
#               never re-open it.
#   2026-08-30  BUILD qk -- PART 3go: working is not usable. DeepSeek answered a REAL
#               lesson prompt in 21.9s -- clearing the outage of every remaining suspect,
#               and nearly doubling Sonnet's 12.3s teaching call. seat-check now reports
#               tokens (so a second press shows the cache), warns when a real-size seat
#               is too slow to teach, and the card gains thinking-off and flash buttons.
#   2026-08-30  BUILD qj -- PART 3gn: a check the size of the thing it checks. qi's probe
#               reported "this seat works" on the morning after 120 real turns had
#               failed, because it sent fifteen tokens where a lesson sends ~46,000.
#               seat-check gains size=lesson (the real build_system_prompt, the real
#               3000-token ceiling); a passing small test now says it proves nothing.
#   2026-08-30  BUILD qi -- PART 3gm: reached, or refused. Jim's question ("somehow the
#               DeepSeek wasn't being called") is only answerable if the code keeps a
#               call that never got there apart from a vendor that answered and said
#               no. tutor.BrainUnreachable names the first; seat-check reports it, and
#               can test a seat that is not the live one.
#   2026-08-30  BUILD qh -- PART 3gl: the seat hands the class back. The first night on
#               the DeepSeek seat was 120 apologies; the pipeline failed OPEN instead of
#               OVER, and the report asked only for referee_crash reasons so the 120
#               failopen messages were never printed. Both fixed, both directions.
#   2026-08-29  BUILD qg -- PART 3gk: the DeepSeek seat. TUTOR_PROVIDER=deepseek on the
#               OpenAI-compatible adapter (url/extra/vendor), thinking effort from env
#               (default low), the privacy gate proved BOTH ways by mutating the page
#               it reads, the critic seat, and /health reporting the live seat.
#   2026-08-29  BUILD qf -- PART 3gj: one thought per line, in the boards. The 64th
#               referee (board_two_thoughts_conflict); its canon sweep found Jim's
#               screenshot line in the algebra1 like-terms FOUNDATION card and three
#               more -- all split. opRow shows the op once for an expression. PART 3fx's
#               literal referee count moves 63 -> 64.
#   2026-08-29  BUILD qe -- forSpeech says "Algebra One" / "Algebra Two" for the Roman
#               numerals in course names (Jim: "Algebra I is being pronounced Algebra
#               Eye"). Four SPEECH_CASES, the pronoun I guarded.
#   2026-08-29  BUILD qd -- PART 3gi: the intervention teaches the problem that was
#               asked. Jim's three screenshots: |6 − 9| became "count fifteen stars",
#               then the redo went to the live tutor with stale history. The note is
#               now engine-described (spoken_for/board_for/ans/praise); session.html
#               treats an "ai" step as an ask. PART 3fx's pv pin is superseded here.
#   2026-08-29  BUILD qc -- PART 3gh: the bars are on the board. Jim's screenshot of the
#               Algebra II opener: "there is no absolute value sign." Two [[step]] lines
#               added ahead of the number line in lessonscripts; spoken line untouched.
#               The screenshot's other two items (no 🚩; a page of white space) were
#               measured in a real browser and did not reproduce -- recorded in the PART.
#   2026-08-29  BUILD qb -- PART 3gg: the check that can be failed (rule 39(d)'s required
#               form replaces a bare "make sense?" ending) and the numeric either-or
#               ("Which is bigger, 3 or 5?", final sentence only). Both directions;
#               canon swept through the full stack, 0.
#   2026-08-29  BUILD qa -- PART 3gf: one entry per function letter (rule 48). The
#               notation referee's f/g/h entry was one character class, so f in the
#               history silenced g, and it needed a letter argument, so g(2) was never
#               seen. Both directions; lenient sweep 0, strict sweep ceiling 12 recorded.
#   2026-08-29  BUILD pz -- PART 3ge: the named list of falsehoods (the 63rd referee,
#               known_falsehood_conflict). Three false universals from the 2026-08-29
#               watch plus PART 3w's ten authored bans, now held LIVE from one table.
#               Both directions (true absolutes stay silent), canon sweep repeated in
#               the PART. PART 3fx's literal referee count moves 62 -> 63.
#   2026-08-29  BUILD py -- PART 3gd: the plain yes/no gets its buttons. Jim's standing
#               rule, restated: a binary question ships bubbles, everywhere. The six
#               shapes finite_answer_conflict knew were each one screenshot; the new
#               _PLAIN_YESNO_RE is the general one (final sentence opens with an
#               auxiliary, no "or", no wh-word). Both directions, and the canon sweep
#               is repeated INSIDE the PART so the 0 can never go stale.
#   2026-08-29  BUILD px -- PART 3gc: the reviewer reads the rule registry. _rule_titles
#               now delegates to tutor.rule_titles(); nightwatch renders its (B) index
#               from the same function. The "SHORTER than the set of rules" pin from
#               build pq is replaced by the new wording, because the list is no longer
#               short.
#   2026-08-29  BUILD px -- PART 3gb: ship the best draft, and read the critic's
#               verdict. The 2026-08-29 watch named the livecritic crash reason ("Extra
#               data" -- a verdict with chatter after it) and counted 66 replies shipped
#               with a known finding. The PART drives _create_verified end to end with
#               scripted referees: a clean draft ships byte-identical (do no harm); a
#               critic-only first draft ships over two prose drafts; three equal
#               findings still ship the last draft. _critic_verdict is tested on the
#               exact chatty shape from the watch.
#   2026-08-28  BUILD pw -- PART 3ga: a different problem is not a snapshot. Jim's
#               order-of-operations screenshot. supersedePrevious folded EVERY earlier
#               written block, not just re-statements of the current problem, because
#               the comparison the function is named for was never made -- one missing
#               `if`. The board hid a worked example behind a click while sitting 90%
#               empty. Build oz's fold is intact; the drive also caught a stale chip
#               count and that is fixed too. tools/pwdrive.py, both directions.
#   2026-08-28  BUILD pv -- PART 3fz: one character, three visible failures. From
#               Jim's Geometry screenshot. A hyphened stutter ("Si-61") parsed as
#               NEGATIVE 61 and graded a right answer wrong; the intervention it
#               triggered PRINTED ITS BOARD TAGS to the child as text; and that
#               intervention had been told, hardcoded, to teach "{a} + {b}" for every
#               problem including subtraction. None of the 62 referees could have seen
#               any of it -- two happen before a reply exists and one is a field they
#               never read. A person with a screenshot found it.
#   2026-08-28  BUILD pu -- PART 3fy: what he is saying is on the screen. Jim's board
#               complaint, MEASURED in a real browser (tools/puedrive.py) before a line
#               was written. The scripted lane came back CLEAN; the LIVE lane puts 90px
#               of a 406px turn above the fold on a 1280x600 window. ⚠️ My first run
#               said the scripted lane was broken too and my first run was WRONG -- it
#               tracked a stale copy of the figure that is SUPPOSED to scroll away.
#               ⚠️ And the fix Jim chose is necessary but NOT sufficient: text alone is
#               396px of that turn, so shrinking the picture cannot close it. The floor
#               was raised 190 -> 340 (at 190 the figure became unreadable) and turn
#               LENGTH is written into board.js as the next build.
#   2026-08-28  BUILD pt -- PART 3fx: the child cannot be right. Three referees from
#               Jim's flag queue (60/61/62), every one invisible to the other 59: tap
#               buttons that do not contain the answer, a question whose answer is
#               already on the board, and a question about a problem the reply never
#               drew. The first is the worst defect this session has found -- and a
#               PERSON found it, not the machine. A fourth flag was cut to a speaking
#               rule with its canon numbers. The both-directions test caught my own
#               bug first: mathcheck calls "2x + 1 = 5" wrong, not unverifiable.
#   2026-08-28  BUILD ps -- PART 3fw: the hole that always appears. Rule 61's SECOND
#               enforced slice (referee 59). The rule already named this exact case in
#               prompt words and the live lane broke it anyway -- promoted, not
#               re-worded. The canon sweep fired on our own calculus foundation card,
#               which is fixed in the same build (sweep 1 -> 0). The referee tile is
#               now PINNED to a count taken from the code, so 58 -> 59 can never drift
#               silently again. One shape CUT with its reason.
#   2026-08-28  BUILD pr -- PART 3fv: a fragment of an unspoken whole. All FIVE of the
#               night watch's remaining referee-backed findings were run through their
#               own referees first: unlike pq, ALL FIVE WERE SILENT -- holes, not
#               pass-throughs. Only the order-of-operations one is fixed, because it is
#               the only finding whose spoken prose the report reproduces in full; the
#               other four would be fixes built on my reconstruction and are recorded
#               as measured-but-unfixed. Two tempting repairs cut with their numbers
#               (169 and 29 authored cards). No new referee.
#   2026-08-28  BUILD pq -- PART 3fu: the eyes report what they saw. The night watch's
#               own report, worked. Rule 42 widened after MEASURING all three findings
#               (two misses, one pass_through -- assuming three misses would have been
#               three wrong fixes); "most people" and the whole everyone/everybody
#               family CUT by canon sweep. The watch now prints crash REASONS. And six
#               of its nine "refutations" turned out to be the reviewer's conduct list
#               being shorter than the referee set -- now surfaced as unjudged, never
#               counted as skepticism.
#   2026-08-28  BUILD pp -- PART 3ft: the last two courses, THE CURRICULUM IS READ.
#               Jim: "Finish the last twenty percent now." Prob & Stat and Diffeq,
#               72 lessons. With these, all ten courses / 360 lessons have been read
#               for sense. Neither course has a prose defect; 48 worked examples now
#               do their operation (22 + 26). Two findings pinned: DIFFEQ IS THE ONLY
#               COURSE WHERE THE FIRST EXAMPLE WAS ALSO BARE (six of them -- pi's
#               assumption did not hold to the end), and an operation-word DETECTOR
#               WAS CUT for 39 near-all-false hits, because counting aloud and a
#               doubling chain ARE the working.
#   2026-08-28  BUILD po -- PART 3fs: Calculus read for sense. Prose clean; 22 second
#               worked examples fixed. The part pins the COUNT ACROSS COURSES as the
#               real finding: 0, 12, 3, 3, 7, 9, 16, 22 -- the defect gets more common
#               as the mathematics gets harder, because an upper-course operation is a
#               one-liner and an author states the result instead of the method.
#   2026-08-28  BUILD pn -- PART 3fr: Pre-Calculus read for sense. The first course
#               with NO prose defects. Sixteen second worked examples fixed, and
#               THREE NEW PINS on a property no other read surfaced: the course keeps
#               promises made in OTHER courses ("Later is now"), and the battery now
#               guards those cross-course debts.
#   2026-08-28  BUILD pm -- PART 3fq: Algebra Two read for sense. The course that
#               started the thread now reads well. Ten changes, one of them a NEW
#               defect class -- internal shorthand spoken to a child ("pyth's") --
#               with a sweep proving it the only instance in 360 lessons.
#   2026-08-28  BUILD pl -- PART 3fp: Geometry read for sense. Seven second worked
#               examples stated the answer where the first stated the operation --
#               and FIVE of the seven were too long for pi's word-count sweep to see.
#               That is the case for reading a course instead of sweeping it.
#   2026-08-28  BUILD pk -- PART 3fo: Algebra One read for sense. Four changes in 36
#               lessons; one beat made the same contrast twice. Also closes the
#               radians fragment PART 3fn flagged and left open -- a flagged defect
#               that is not fixed is a debt. All four foundation courses now read.
#   2026-08-28  BUILD pj -- PART 3fn: Pre-Algebra read for sense. The strongest course
#               in the product; seven changes across five lessons. Rule 14 caught one
#               of the fixes deleting a sign the lesson had promised to name -- the
#               second time this session.
#   2026-08-28  BUILD pi -- PART 3fm: the second example teaches too. Basic read line
#               by line; the course is sound, but eleven "One more together" worked
#               examples had collapsed to the bare answer (a twelfth was found by
#               the part's own sweep, after my read missed it) -- one of them to a
#               FRAGMENT ("90 plus 3 — 93") that skipped the method it was teaching.
#   2026-08-28  BUILD ph -- PART 3fl: the last eight, the curriculum is whole. All ten
#               courses are nine units of four (360 lessons). Pins the two findings
#               only the validator could make: a fraction op whose whole pool was six
#               problems, and 50-percent-off, where the saving and the price you pay
#               are the same number so the lesson's own distractor collides with its
#               answer.
#   2026-08-28  BUILD pg -- PART 3fk: Entry fills its units. 20 -> 36 lessons, so no
#               five-year-old drops onto the live lane. The validator rejected the
#               first cut 18 times and the battery caught 4 more; both lists are in
#               the part's docstring because every one of them was right. The
#               giveaway allowlist grows 5+2 -> 7+4 for entry-u2-doubles, a ten-fact
#               recall domain that cannot fit a 7-problem bank, 2 asks and 3
#               demonstrations -- the quarter-turns argument, word for word.
#   2026-08-27  BUILD pf -- PART 3fj: the first course, read for sense. Jim: "Start at
#               the beginning." All 20 Entry lessons read; Entry turned out SOUND, and
#               only eight lines across six lessons changed. One was FALSE -- "17 take
#               away 9 equals 8 cubes longer" -- read to a five-year-old three times
#               in one lesson, and no validator here could ever have caught it.
#   2026-08-27  BUILD pe -- PART 3fi: the sentences make sense. Jim: "the text itself
#               is as if someone is teaching math in a non-native language" -- and
#               then, when I blamed the vocabulary canon: "Takeaway or minus, those
#               were just as well." The writing was the defect. Pins the rewritten
#               absolute-value lesson, the two authoring rules that survived a canon
#               sweep (stray space before punctuation; spoken sentence over 34 words),
#               the third that was CUT for 390 false positives, and rule 14's repair
#               after closing the spaces broke 70 lessons at once.
#   2026-08-27  BUILD pd -- PART 3fh: let the lesson breathe. Jim: "There was no pause
#               at any time. pictures showed up and disappeared." pb's scripted player
#               advanced on `else scrNext()` -- the instant speak() RESOLVED -- so a
#               missing clip dumped the whole lesson in one frame. Restores the three
#               protections pilot.html grew over builds ka/kd/ke and pb's hand-port
#               left behind (reading floor, 650ms breath, silence-waits-for-the-child),
#               using this page's OWN readMs rather than a second copy. The fix's first
#               cut served the floor on ask beats too and made the tap buttons inert
#               for 2.6s -- caught by the pb drive, pinned here. /tmp/pddrive.py, 14
#               assertions, silent AND voiced.
#   2026-08-27  BUILD pc -- PART 3fg: the figure fills the board. Jim: "Why is it so
#               hard to make a big number line". It was not hard -- .mfig was a
#               shrink-to-fit box, so an <svg> sized in PERCENT collapsed to the
#               300px replaced-element default and THREE builds' worth of raised
#               display caps (je 660, nw 1100, ox 1500) were dead letter. One CSS
#               line fixes it; the new part pins the line, pins that .mblock still
#               centers everything else, and pins the aspect-scaled cap floor that
#               math-figures.js / geo-figures.js now apply with Math.max so no
#               earlier build's chosen cap is ever undone. Measured, not reasoned:
#               /tmp/pcdrive.py, 14 assertions in a real browser.
#   2026-08-27  BUILD pb -- PART 3ff REWRITTEN: the classroom itself gets fast. pa
#               moved the child to a second page to make things quick; Jim wanted
#               the same room, quicker. The authored lessons play inside
#               session.html now, and the door pins from op/oq/pa are reconciled.
#   2026-08-27  BUILD pa -- PART 3ff: the gate is open (SUPERSEDED by pb). Every course's lessons door
#               is the authored lane; the live screen survives beside it as "Teach
#               me something else". Two pins OVERTURNED and recorded in place.
#   2026-08-27  BUILD oz -- PART 3fe: the board uses the room. MEASURED first (a
#               browser drive replayed Jim's own transcript and reported 560px of
#               work in a 1,732px board, 1,593px of scroll for one problem), then
#               fixed, then re-measured. Two self-inflicted defects recorded in
#               place: a stylesheet fix that reached only the page which loads
#               board.css, and a grid that listed the spanners instead of the
#               exceptions.
#   2026-08-27  BUILD oy -- PART 3fd: the day you can feel (partial goal fill on
#               both lanes, today stated in words, and the honesty rule that a
#               partial fill can never reach 100).
#   2026-08-27  BUILD ox -- PART 3fc: the seventh flag harvest (referees 56/57/58,
#               the [[segment]] figure, the bigger number line, and the server's
#               session-length note). Also THREE PIN REPAIRS this build earned:
#               two pins were matching their OWN explanatory text (the same lesson
#               build ov learned), and one depended on where a line happened to
#               wrap -- now whitespace-normalised.
#   2026-08-27  BUILD ow -- PART 3fb: use the whole board.
#   2026-08-27  BUILD ov -- PART 3fa: quizzes through the authored spine. Also
#               THREE FIXTURE REPAIRS this build exposed, each recorded in place:
#               the drill-ticket test compared against ONE lesson's closure while
#               the server uses the whole course's; the clip-outlier negative test
#               seeded every line with an identical clip and called that healthy;
#               and the per-lesson audio ceiling moved 20k -> 22k chars with its
#               ledger note (quizzes joined the closure; the dollar bar did not
#               move).
#   2026-08-27  BUILD ou -- PART 3ez: answer freely in the fast lane. The scripted
#               lane takes typed and spoken answers, read by a PURE PARSER
#               (lessonscripts.read_answer) and never by a model. Three real
#               mis-reads were caught here before shipping -- "1/2" as 2, "three
#               point five" as 5, "one half" as 1 -- plus str(obj)'s hex address
#               read as a number. numwords.py is the one shared number table.
#               PART 3cw's "no microphone is ever loaded" ruling is OVERTURNED by
#               Jim's flip order and recorded in place, not deleted.
#   2026-08-27  BUILDS or/os/ot -- PART 3ey: the walk-away list. or: session's
#               sidebar starts collapsed behind the #sbTab edge tab, the
#               controls reparent to the bottom strip (ordrive green). os: the
#               [[stepcard]] step grid (board.js machinery, three transcript
#               pages + scripted lane, rule 58e, registry; stepdrive green).
#               ot: six new figure tags (transversal/polygon/solid + venn/
#               tape/clock) and numberline hops=, documented per course
#               (figdrive green, 22 render assertions).
#   2026-08-27  BUILD oq -- PART 3ex: the raised hand. A child mid-script asks a
#               question and gets one bounded spoken answer (pending answers
#               fenced, no board tags, authored fallbacks on every failure
#               path); the script resumes un-re-spoken; the home tile widens to
#               the whole prealgebra course. 14-assertion drive + TestClient
#               bounds run green before the pins.
#   2026-08-27  BUILD op -- PART 3ew: the authored-spine pilot (Phase 3, Jim's
#               "go"). Pre-Algebra Unit 1 served from the authored lane beside
#               the live one: the home door, the pilot lens, the owner's 🚩 on
#               the scripted bubble, and the lane's own numbers on the admin
#               card. 10-assertion browser drive green before the pins.
#   2026-08-27  BUILD oo -- PART 3ev: the giveaway audits join the battery. The
#               41-hit hand tail from ms is closed (5 renumbered, 26 bank
#               removals across 18 lessons, one ask rotated, one story
#               renumbered with its sentence); what remains is a two-lesson
#               documented allowlist (quarter-turns' four-fact recall domain +
#               one false positive), pinned exactly -- any new giveaway
#               anywhere fails the build.
#   2026-08-27  BUILD on -- PART 3eu: the canon held to its own standard
#               (Phase 1 of the plan Jim approved). The full 54-referee sweep
#               now runs over all ~1,989 authored cards every battery run, with
#               two documented exemption classes (foundations may run long, rule
#               19a; demo beats may ask-and-answer, rule 19b) and the rest of
#               the stack still checked BEHIND each exemption. First run found
#               421; the night's fixes took it to 0, where this part pins it.
#   2026-08-27  BUILD om -- PART 3et: skip the introduction. Jim: "The
#               introduction to Abrabot should have a skip introduction button."
#               Server-marked intro steps (intro: True through _drill_clean),
#               drill.html's "⏭ Skip the intro" (silences the clip, drops only
#               marked steps, can never double-advance or eat teaching).
#               11-assertion browser drive green (skip + listen-through).
#   2026-08-26  BUILD ol -- PART 3es: the sixth flag harvest (six probstat
#               flags). Named-binary quiz questions ship buttons (two part3dx
#               assertions flip DELIBERATELY, dated); "or want another" + clause
#               forks; referee 53 an-opener-never-grades (server-gated); referee
#               54 the "Question 3: 20" clock-time collision; bars display cap
#               400 -> 720; store.py's 16-char verify_status truncation
#               normalized (the invisible shipped-critic replies).
#   2026-08-26  BUILD ok -- PART 3er: grade what they said, earn what you score
#               (Jim's probstat screenshot: "Spring" answered, "Pie chart --
#               correct! That's question 1 done" replied). tapped_answer's iy
#               digit gate opens for word taps whenever the reply GRADES; NEW
#               referee 52 (quiz_credit_conflict) rejects "question N done"
#               when the conversation never asked question N. 18(c) + 47(k).
#   2026-08-26  BUILD oj -- PART 3eq: side by side on purpose. Jim: "the
#               whiteboard is underutilized." Bubbles 80% -> 96% on the three
#               classroom pages, and the NEW [[beside]] tag places the next
#               board block NEXT TO the previous one (board.js mountBlock, the
#               one door; .mrow CSS with flex-wrap so phones stack; rule 58(d)
#               teaches the move once, in the shared rules). 19-assertion
#               browser drive ran green on all three pages before the pins.
#   2026-08-26  BUILD oi -- PART 3ep: the fifth flag harvest (five geometry
#               flags). Referee 42 learns the LEADING fork ("Want X, or Y?");
#               NEW referees 50 (the board does the drawing -- paper is never
#               the only picture) and 51 (a vertical-angles question gets its
#               X), both heard-gated; geo-figures.js [[angle]] grows cross="?"
#               (two full lines crossing, opposite angle labeled); the prompt's
#               own sketch-along clause was the paper flag's root cause and is
#               rewritten board-first; rule 37 grows the recap gloss.
#   2026-08-26  BUILD oh -- PART 3eo: the fourth flag harvest (an algebra2
#               absolute-value session). The leak referee learns the referees'
#               OWN nudge jargon ("has something to land on" spoken to a child);
#               referee 42 learns the bare final ready-check; the a2 unit-1
#               playbook gets the full absolute-value arc (distance picture,
#               cases BORN on the board, both answers checked, two examples).
#               The small-numberline flag was a stale browser cache -- the 1100px
#               file is verified LIVE; nx's no-cache ends that class.
#   2026-08-26  BUILD og -- PART 3en: the starting blocks (Jim's speculation,
#               V1). A computable pending line arms a full-pipeline right-answer
#               follow-up; a matching next answer ships it with ZERO model calls
#               on the clock; any mismatch or state drift falls through to the
#               untouched live path. Live TestClient drill with a counted fake
#               brain proves hit, miss, and the stale-history guard.
#   2026-08-26  BUILD of -- PART 3em: the seat survives a typo. LIVE_CRITIC_MODEL
#               ="claude-haiku-4.5" (dot) 404'd every critic read for four hours
#               (28 crashes = 28 turns with NO second opinion, fail-open each).
#               A model-not-found 404 now swaps the seat sticky to DEFAULT_MODEL
#               with ONE loud event. Proven with a stubbed client.
#   2026-08-26  BUILD oe -- PART 3el: one thought per line + the week-old
#               memory. Referee 49 (the check-cram), rule 40(i) (a mid-flight
#               problem is re-derived after a gap), the gap note's dynamic copy
#               of the same law. Headroom 616 -- the next shared clause
#               deliberates the eighth raise.
#   2026-08-26  BUILD od -- PART 3ek: the keyboard closes. A ⌨️✕ on the answer
#               bar of all three pages; reopen = the Type button where it exists
#               (session), a fixed ⌨️ pill where the link was retired with
#               !important CSS (practice/topic). The 8-assertion live drive
#               (close/reopen on all three pages, board room measured) ran green.
#   2026-08-26  BUILD oc -- PART 3ej: never fast-forward the board. Referee 48
#               (a result you speak is a result you drew, heard-gated both ways)
#               + 15(a)'s never-fast-forward clause, from Jim's live algebra
#               flag ("+3 to each side" -> "We got X equals 5" with two steps
#               invisible). The arithmetic was RIGHT; the teaching was wrong.
#   2026-08-26  BUILD nz -- PART 3ei: the third flag harvest. Referee 47 (count
#               your own drawing -- the objects tag is the truth), 29(c) scoped
#               to real boundaries (nu's same-day regression owned and fixed),
#               referee 45 learned "what number did you build?", the seventh
#               dated ceiling raise (193k -> 195k, deliberated since nw's 149).
#   2026-08-26  BUILD ny -- PART 3eh: where the seconds go (the latency deep
#               dive). PROMPT_CACHE_TTL=1h env support (unknown values fall back
#               to the plain 5m block, never crash a turn); /api/admin/stats
#               exposes critic_seat + prompt_cache_ttl; the admin tile names the
#               ACTUAL critic model. The big levers are proposals in the report
#               doc, not unattended builds.
#   2026-08-26  BUILD nx -- PART 3eg: the hard-refresh ritual dies. HTML/JS/CSS
#               responses carry Cache-Control: no-cache (revalidate -> 304s via
#               ETag); audio/images/JSON untouched by content-type scoping. Live
#               TestClient drill proves headers, 304 revalidation, and the audio
#               lane's exemption.
#   2026-08-26  BUILD nw -- PART 3ef: the second flag harvest + the placement
#               gap. Three doors end a drill run; the number line scales to the
#               board; one equation per line; "too" never hangs after a number;
#               techniques are named as tricks; rule 40(h) placement validates
#               skills not vocabulary, with the first-session word tour riding
#               the placement note. Headroom after: 149 chars -- the NEXT shared
#               clause must deliberate a raise (hr/il/ni/nu/nv discipline).
#   2026-08-26  BUILD nv -- PART 3ee: the night watch's thirteen. Referees 45
#               (never ask what the board already answers) + 46 (no record means
#               ask), three notation catalogue entries (slash/arrow/hug), "lots
#               of kids" in rule 42's shapes (and percentile exempted as probstat
#               curriculum), six prompt clauses, sixth ceiling raise (191k->193k).
#               Three canon catches during the dry run are pinned as cases.
#   2026-08-26  BUILD nu -- PART 3ed: the first flag harvest. Jim's in-app flag
#               queue produced four confirmed findings in one evening; referees 43
#               (unilateral sign-off, heard-gated) and 44 (board paren balance)
#               plus the offer-fork in referee 42, rules 29(c)/39(e)/47(e)/48(f),
#               and the fifth dated ceiling raise (188k -> 191k). Two 3dx pins
#               FLIPPED deliberately: Jim's flag ruled that two-way offers -- the
#               39(d) check-in shape included -- ship buttons now.
#   2026-08-25  BUILD ns -- PART 3ec: follow the pen. Jim, one lesson after nr:
#               "same problem." nr repaired the resize MOMENT and missed the
#               already-small STATE (keyboard open before the tall turn arrived).
#               scrollFeed's anchor now advances with the writing; the + key joins
#               the symbol strip ("a combo button for +- and a - button but no +").
#               3eb's two pins on nr's removed shrink-branch updated to the new
#               single invariant.
#   2026-08-25  BUILD nr -- PART 3eb: the board answers for its own size (the
#               symbol strip ate board room and the QUESTION slid below the fold;
#               ResizeObserver in board.js re-anchors, shrink-that-no-longer-fits
#               shows the END of the turn) + the pronounced amber pause button on
#               all three voice pages. Live drive ran green before these pins.
#   2026-08-25  BUILD nq -- PART 3ea: the owner's flag. Jim can flag a wrong
#               sentence from inside a live lesson; owner-only by admin key on BOTH
#               sides (no key -> no button in board.js, and 401 on all three routes).
#               Static pins + a LIVE TestClient drill (gate/write/caps/queue/resolve).
#   2026-08-25  BUILD np -- PART 3dz: the first production week's three root
#               fixes (pendcheck's check-in phantom, spokenlen's unsatisfiable
#               nudge, the critic nudge's first-sentence rule), both directions.
#   2026-08-25  BUILD no -- PART 3dy: the symbol strip (one keyboard, not two),
#               with the never-touch-the-mic history pin. Validated by an eight-
#               assertion browser drive across the three teaching pages first.
#   2026-08-25  BUILD nn -- PART 3dx: rule 39(e) + referee 42 (small answer spaces
#               ship buttons), with the 39(d) required-wording exclusion pinned.
#   2026-08-25  BUILD nm -- PART 3dw: the drill picker becomes a per-course
#               accordion and every complaint lands under the tapped button.
#               Validated first by a six-assertion headless drive with a stubbed
#               drill API; the pins are the cheap daily echo.
#   2026-08-25  BUILD nl -- PART 3dv: REFEREE 41 (an angle is called an angle),
#               course-gated, plus the template fix that removes the root cause.
#   2026-08-25  BUILD nk -- PART 3du: REFEREE 40 (no layout words for the board),
#               both directions, the canon, the wiring, and the prompt's wider ban.
#   2026-08-25  BUILD nj -- PART 3dt: REFEREES 38-39 PINNED, both directions plus
#               the standing canonical sweep and a \x08 tripwire (a backspace-eaten
#               \b parses fine and matches nothing -- the worst combination). The
#               domain-script pin reads the LOADED script, not the source: the
#               phrase spans a string-concat boundary, and that is the SIXTH pin
#               that would have failed on spelling rather than behaviour.
#   2026-08-25  BUILD ni -- PART 3ds: THE BOARD IS A CLAIM. The night watch's
#               machine-fixable findings pinned: the board-equation checker (both
#               directions + the STANDING 306-script sweep, in-battery, zero false
#               alarms), the notation referee's three new symbols and its
#               all-attribute-values fix, the 47/59/61 prompt clauses by verbatim
#               anchor, and rule 42 on nightwatch's reviewer list.
#   2026-08-25  BUILD nh -- 3dr: THE SEAMS JIM HEARD. Fixed timers under spoken
#               feedback (cut praise) are banned -- every advance chains on the line
#               finishing -- and Abrabot's 220px flying entrance is pinned. The
#               headless harness gained an INTERRUPTION LEDGER (utterances cancelled
#               before their own end) which proves no feedback line is cut; and a
#               harness lesson worth keeping: body.textContent.includes(...) MATCHES
#               THE PAGE'S OWN SCRIPT SOURCE, so the old "congratulations landed"
#               check had been vacuously true since it was written. Element-based
#               checks only (#answer .endbox). An assertion that cannot fail is not
#               an assertion.
#   2026-08-25  BUILD ng -- 3dr GROWS THE SIDEBAR PINS. Jim opened the nf demo and
#               said "in the sidebar of the demo i see no practice problems" -- right:
#               nf put practice at the END of the lesson and never touched the demo's
#               replica SIDEBAR, which was still the pre-mu classroom. Now pinned:
#               the 🤖 Extra practice button (same face and position as session.html),
#               the tour stop that introduces it, the tour line in both voice lists,
#               and the standalone door (a cold tap skips the "before we finish"
#               handoff -- no line plays that isn't true). Validated by four headless
#               journeys, fifteen assertions, before these pins were written.
#   2026-08-25  BUILD nf -- PART 3dr: THE DEMO PRACTICES TOO. The demo's new Abrabot
#               segment is pinned the way the product is built: the 20 bank answers
#               are RE-DERIVED here in Python against demo.html's abraAnswer()
#               (computed, never typed -- two implementations must agree), the bank
#               must cover every course in curriculum.COURSE_ORDER, the handoff line
#               must live in BOTH voice lists and be addressed by anchor, Abrabot's
#               voice must stay the free one, and the Skip door must exist. Validated
#               first by driving both journeys in a real headless browser.
#   2026-08-25  BUILD ne -- 3dq: THE MENU LINK IS PINNED. site-nav.js now injects
#               "How we teach" after "Our mission" on every marketing page; the pins
#               hold the injector, its double-link guard, and methodology.html's own
#               hardcoded here-link. Verified first by HEADLESS RENDER of all 13
#               pages (exactly one link each) -- the pin is the cheap daily echo of
#               that expensive proof.
#   2026-08-25  BUILD nd -- PART 3dq GROWS JIM'S REVIEW PINS. He approved the page
#               with three edits (the AI story plainly, the feedback story, retire
#               the word "scripted", drop the 90% tile) and each is now a pin, so a
#               future copy pass cannot quietly re-introduce what he removed. The
#               scripted pin reads code_only + whitespace-normalized text -- change
#               notes may still say the word; the page may not.
#   2026-08-25  BUILD nc -- PART 3dq: THE METHODOLOGY PAGE KEEPS ITS RECEIPTS. The
#               page now quotes teaching-rule names next to the research they came
#               from; this part fails the build if a quoted rule stops existing
#               (checked through RULES.md, which --rules regenerates from tutor.py),
#               if a citation vanishes, or if the not-proven confession is softened.
#               ⚠️ Search is WHITESPACE-NORMALIZED -- the first draft failed on a
#               title wrapped across two source lines. FOURTH pin to fail on spelling
#               rather than behaviour (3df, 3dk, 3dn's quote, now this). Normalize
#               before you match; the defect is never the line break.
#   2026-08-24  BUILD nb -- PART 3dp: NO BUTTON UNDER A TALKING TEACHER. And this one
#               is the answer to "why did a grep-shaped pin let build mx ship a bug
#               Jim could see in ten seconds?" -- because mx's guarantee was about
#               TIMING and every pin on it was about TEXT. 3dp lifts speak() and its
#               constants straight out of static/drill.html and RUNS them on a virtual
#               clock: real 3000ms, real 6000ms, real 85-per-character, four
#               scenarios, ~50ms total. It was validated by first running it against
#               the mx code, where scenario ① fails at 3.0s exactly as Jim reported.
#               ⚠️ IT LIFTS BY LANDMARK -- "var VOICE_WAIT_MS =" through the "score"
#               divider. If you move those, this part says so loudly rather than
#               quietly testing the wrong region; there is a pin for that too.
#   2026-08-24  BUILD na -- PART 3do: BUILDING THE COURSE IS NOT TEACHING A CHILD.
#               Third build running that the defect was a tile adding real numbers
#               into a false claim (mw, mz, now na), so this part does not check that
#               the build/serve split EXISTS -- it checks the two things that would
#               silently un-split it: ① a new kind="tts" render pass in main.py whose
#               mode is not in store.TTS_BUILD_MODES (it reads main.py's own call
#               sites and flags any mode containing "prewarm" that is unclassified),
#               and ② the headline dividing total_usd again instead of serve_usd.
#               ⭐ AND IT DOES THE ARITHMETIC ON A LIVE DATABASE, not just a grep:
#               logs a render pass and a child's line, then asserts build dollars are
#               not inside serve dollars AND that the two halves still re-account for
#               every character the old single total covered. Run the battery with
#               DATABASE_URL set or those five checks SKIP -- they are the half that
#               actually proves the money is right.
#   2026-08-24  BUILD mz -- PART 3dn GROWS TEETH. It used to check that every status
#               tutor.py can emit has a counter in store.py. That caught the missing
#               key; it could not catch static/admin.html ADDING THE KEYS UP WRONG,
#               which is what it was doing: mathcheck's pass-through (verify_unresolved
#               -- three drafts judged wrong, the third shipped) was being counted as
#               an error CAUGHT AND FIXED, and simultaneously left out of "shipped
#               unresolved". Three new pins read the page's own arithmetic:
#                 * verify_unresolved is inside shipped7, not inside the fixed count
#                 * "caught & actually fixed" resolves to verify_fixed alone
#                 * the first-try rate is its own tile and carries a colour class
#               ⚠️ THESE PINS READ static/admin.html AS TEXT. If you rename shipped7
#               or fixed7, fix them here in the same commit -- they are deliberately
#               specific, because the vague version of this pin is what let two builds
#               of wrong arithmetic through.
#   2026-08-24  BUILD mw/mx -- PART 3dn: EVERY REFEREE VERDICT IS COUNTED. It reads
#               the statuses out of tutor.py and fails if store.py has nowhere to put
#               one, because this bug has now happened TWICE in the same shape (gz
#               for prose, iv for the critic) and both times the fix was "add the key
#               we forgot" rather than "stop relying on remembering".
#               ALSO: PART 3df's silent-play pin matched the exact characters
#               "if (played) setTimeout(go" and failed when mx added braces -- while
#               the guarantee got stronger. It matches behaviour now. A pin that
#               fires on formatting teaches people to stop reading pins.
#   2026-08-24  BUILD mu -- THE TOUR PIN NOW SCANS THE LINES, NOT THE PROSE ABOUT
#               THEM. PART 3cb's layout-geometry check read the raw TOUR_STEPS block,
#               so the moment a comment EXPLAINED which phrases are banned -- which
#               the new Abrabot stop does, to stop the next author repeating the
#               mistake -- the pin fired on the warning instead of the defect. Same
#               trap code_only() was written for, five times over, and the tempting
#               repair is always to delete the documentation. It strips comments now.
#               NEW PINS in PART 3dm: the lesson sidebar has its own door to Abrabot,
#               the guided tour introduces it, and the two features that both wanted
#               the word "practice" are not both called practice.
#   2026-08-24  BUILD mt -- PART 3dm, PRACTICE IS COUNTED AND STILL IS NOT MASTERY.
#               The feature pulls against Jim's own ruling, so both halves are pinned
#               on a real database: the ledger fills AND unit_checks, topic_progress
#               and problems_practiced all stay untouched. Money tripwire included.
#               ALSO FIXED A BRITTLE PIN: PART 3bj asserted exactly 17 uses of
#               Depends(_code_dep), so adding any {code} route failed it -- and the
#               only way past a hardcoded count is to edit the number, which is the
#               very reflex that would let a route slip through WITHOUT the
#               dependency. It counts the {code} routes and compares now.
#   2026-08-24  BUILD mr -- PART 3dl, THE COURSE AGREES WITH ITSELF OUT LOUD. A pin
#               that no spoken line says "1 <plural>", swept over all 336 lessons.
#               It exists because 224 lines DID -- "1 pennies", "1 sixths", "1
#               stars" -- all in the two courses for the youngest children, all
#               already rendered in the real voice, and all passed by validate()
#               because grammar is not arithmetic. Nouns only: a pin that fires on
#               "1 equals" or "1 leaves" is a pin people learn to ignore.
#   2026-08-24  BUILD mq -- PART 3dk, THE COST EPOCH. Proves both halves on a real
#               database: the old spend is STILL in the 7-day figures, and the era
#               reads only what came after it. Plus the subtle one -- the epoch rides
#               system_events, which is purged at 90 days, so a pin holds the
#               exemption.
#               ⚠️ AND THAT PIN NEARLY SHIPPED VACUOUS. Its first draft called
#               purge_system_events(0.0000001), which int()s to 0 days and returns
#               immediately -- so "the purge does not eat the epoch" passed without
#               the purge ever running. The rows are really backdated 200 days now. A
#               test that proves nothing is worse than no test, because it is
#               believed.
#   2026-08-24  BUILD mp -- ⭐⭐ THE COVERAGE CLAIM IS NOW A TEST. PART 3cv's
#               Entry-Level pin moves to all nine units, and a new pin above it
#               walks curriculum.py and fails on ANY unit of ANY course with no
#               scripted lessons. That is the pin whose absence let Entry-Level U8
#               and U9 sit empty until a spreadsheet found them -- in the course
#               where the youngest children start. Three Unit 9 pins with it: the
#               unit covers all three things it is NAMED for, the group lessons
#               never say "times" (Basic Math U2 names multiplying), fair sharing
#               never leaves a remainder, and nothing demonstrated on a shape is
#               later asked -- checked BY SHAPE, because sides and corners are two
#               ops and workedaudit.py compares tuples.
#   2026-08-24  BUILD mo -- ENTRY-LEVEL UNIT 8, AND A DRILL-POOL BUG IT UNCOVERED.
#               PART 3cv: the Entry-Level span pin moves from units 1-7 to 1-8, and
#               NAMES Unit 9 as the one unit in the whole curriculum still
#               unscripted -- so the hole the spreadsheet found cannot be quietly
#               forgotten a second time. Three new pins with it: the unit covers all
#               three of the things it is NAMED for, the clock never wraps past 12
#               (that is modular arithmetic and this unit does not teach it), and
#               nothing the clock lesson DEMONSTRATES is later ASKED -- checked by
#               clock POSITION in both directions, which workedaudit.py structurally
#               cannot do because it compares problem tuples and "the hand points to
#               4" and "20 minutes past" are the same fact in two shapes.
#               PART 3de: two pins on the drill pool's ranking. drillpool kept its
#               own copy of the ramp measure and applied the LESSON'S op key to every
#               problem in a bank; both mixed-op lessons therefore had EMPTY pools
#               and nothing noticed. It now calls lessonscripts.difficulty_key, and
#               these pins hold it there.
#   2026-08-24  BUILD mn -- TWO PINS MOVED WITH JIM'S RULING, TWO PINS ADDED.
#               Jim tested the handoff with the rendered course and ruled that Mr.
#               Cadabra must wear HIS OWN FACE on the drill page ("when it goes back
#               to mister Cadabra, it needs to show his face"). So:
#               - PART 3dg's drill-page presence pin now requires presence BY
#                 IDENTITY (`presence: c.persona === "cadabra"`) instead of a blanket
#                 presence:false -- the guarantee it protects is unchanged and
#                 stronger: no persona but his can EVER mount a real person's video.
#               - PART 3dh's twin pin now also checks the fly transform rides the
#                 .faceslot WRAPPER, because the video host mounts on the canvas's
#                 parent and a canvas that flew alone would leave his face mid-air.
#               - PART 3di gains two pins: the handoff's hello/goodbye are standalone
#                 closure lines (Jim heard the browser-voice seam they used to
#                 cause), and main.py ALIASES lessonscripts' strings rather than
#                 keeping its own copies -- one owner, same argument as mk.
#   2026-08-21  BUILD kf -- PART 3cy, THE SCRIPTED LANE PICKS ITS OWN VOICE. Jim, with
#               the course fully prewarmed and ke's repair reporting zero damage:
#               "Still garbled when counting four stars" -- right words, bad audio, i.e.
#               a bad RENDER that ke's structural check cannot see. The course had been
#               rendered on eleven_flash_v2_5, the LOW-LATENCY model, in a lane that is
#               pre-rendered and does not care about latency. kf gives the scripted lane
#               its own model. The DANGEROUS part is key agreement, and that is what this
#               PART mostly tests: with the default unset every cache key must stay
#               BYTE-IDENTICAL to ke's (or the ~$43 already spent is orphaned on deploy),
#               and with the split on a clip must round-trip store->lookup as a HIT while
#               the live lane's keys do not move at all. Plus force/lesson semantics and
#               the audit's outlier maths, including the negative test that a healthy
#               course produces NO outliers.
#   2026-08-21  BUILD ke -- PART 3cx, THE VOICE CACHE IS WHOLE OR IT IS NOT CACHED.
#               Jim's kd playtest heard several lessons "slurring and speaking
#               nonsense" while the audio prewarm ran. Root cause: all three TTS
#               cache writers named their temp file after the TEXT, so the prewarm
#               and a child's playback collided on one path and cached two renders
#               spliced together. This PART proves the whole fix: 20 accept/reject
#               cases for mp3_is_intact() (real encoder output vs. splices,
#               truncation, zero fill, error bodies, lying Xing headers), 40 REAL
#               threaded races against _tts_cache_store() that must never leave a
#               corrupt entry, the refusal to cache damaged bytes, and eviction
#               spending the generated lane before the scripted course. Plus source
#               pins on the repair endpoint and on pilot.html's watchdog.
#               THREE EXISTING PINS WERE REPAIRED, not weakened: the TTS cap pin now
#               reads TTS_CACHE_MAX_MB's default (the cap moved behind an env var)
#               and additionally pins its floor; the SILENT-mode pin now names the
#               MECHANISM instead of the comment phrase "safety valve", because that
#               valve WAS the bug and its name went with it. And two new pins scan
#               code with comments stripped -- this battery documents the old broken
#               expressions on purpose, and a pin that forbids describing a bug
#               deletes the memory of it.
#   2026-08-19  BUILDS in + io -- in: PART 3cb gains the glow-is-the-pointer pin (no
#               tour line may point with layout geometry). io (the anecdote diet,
#               batch 1): rule 49(f)'s date pin replaced with a prescription anchor
#               -- the ONE deliberate pin change; every other pin survived the diet
#               untouched, which is the proof the diet cut only scaffolding.
#   2026-08-18  BUILD il -- PART 3cc, THE TODAY BAR MAKES REAL CALLS: pins the two
#               server calls and their wiring (match-tick in the quiz AND check
#               recording branches; time-tick on the minute beat; the injection net
#               on BOTH chat paths after recording), the page's two-kinds rendering
#               with the upgrade guard, the prompt's sizing + trust-the-server
#               words, and a full live drill (completion match, the 15-minute
#               worked tick, net idempotence, upgrade-not-downgrade, old-row
#               compatibility).
#   2026-08-18  BUILD ik -- PART 3cb, THE TOUR RUNS ONCE: pins the tours_seen store
#               fact (+ reset-cascade membership), the record-before-model-call
#               ordering on __tour_done__, the OR into /api/session's toured flag,
#               the skip button's same-path handoff, and a live store drill
#               (record/read/idempotence/isolation/reset hygiene on real sqlite).
#   2026-08-18  BUILDS ih/ii/ij -- PARTs 3by/3bz/3ca, the Tier-B remainder: rule 14
#               runtime (new board notation read aloud; first-time-only and
#               read-aloud exemptions), rule 22 (verbatim re-ask; six-word floor,
#               ladder re-phrases pass; prev_tutor plumbing pinned), rule 62 (the
#               audits' false-factoring shape; real work and generic tokens
#               exempt). Three-referee canonical sweep on empty history.
#               RULE_VERIFY 14/22/62 -> ENFORCED. Rule 19 stays deferred.
#   2026-08-18  BUILD ig -- PART 3bx, THE QUIZ VOCABULARY GATE (rule 37's
#               quiz-facing half, the Tier-B flagship): fire + every exemption
#               (delivered scripts, heard, teach-then-ask, teaching replies, one
#               term, missing facts), the names-only-the-missing-term pin, the
#               main->meta->sweep plumbing pins, and the 4-course canonical sweep
#               on empty history. RULE_VERIFY[37] -> ENFORCED (teaching half stays
#               covered + probed).
#   2026-08-18  BUILDS id/ie/if -- PARTs 3bu/3bv/3bw, the promotion batch (the
#               audit's Tier A): rule 42 comparisons (kindness form included; own-
#               work comparisons exempt), rule 60(c) one spotlight (tour stops
#               exempt), rule 16 substitution-rewrites (both 2026-08-07 catches
#               verbatim; quoted VALUES judged, never the attr syntax's '='), and
#               the Ground Rules' STAY IN ROLE leak shapes (math "rules" and the
#               math "not allowed" untouched). Four-referee canonical sweep;
#               RULE_VERIFY 16/42/60 -> ENFORCED. COVERED count 30 -> 27.
#   2026-08-18  BUILDS ia/ib/ic -- PARTs 3br/3bs/3bt, the quiz-honesty trio from one
#               live quiz run: 3br (rule 47e -- the untaught acute/right/obtuse
#               choice, verbatim, plus the taught / teach-in-reply / no-history
#               exemptions, the heard-from-ORIGINAL-messages plumbing pin, and the
#               sweep wiring); 3bs (rule 47g -- the vertex question that contains
#               its answer, the say-it-back exemption, and the ia+ib canonical
#               sweep with ia armed on empty history); 3bt (rule 47f words -- an
#               angle question draws its angle; complement = the split right angle).
#   2026-08-18  BUILD hz -- PART 3bq, THE PROMISED COMPARISON (rule 63e): fixtures
#               both directions (Jim's live catch verbatim; the honest deg="90"
#               split="50" fix; the question-alone and deferral exemptions), the
#               sweep wiring, the canonical sweep, and the prompt's words half
#               (rule 63e body + the [[angle]] compare move). RULE_VERIFY[63]
#               extended.
#   2026-08-18  BUILD hy -- PART 3bp, THE VOICE ASKS TWICE: pins voice.js's new
#               single retry of a failed speak-prep/clip (the mid-deploy mechanical-
#               voice blip Jim heard live), the immediate fallback on an
#               authoritative {voice:false}, the started/doneCalled guards, and the
#               unchanged 5s no-start watchdog.
#   2026-08-18  BUILD hx -- PART 3bo, THE BETA PAGE'S KEY LEAVES THE URL: pins the
#               sessionStorage + scrubbed-address-bar + header pattern on beta.html
#               (the credential-in-URL class's third sighting), the server-side
#               header acceptance on all three beta POSTs, the forget-on-wrong-key
#               behaviour, and the new "sign in at /login with your pass" line.
#   2026-08-18  BUILD hw -- PART 3bn, THE GOVERNOR'S EYES ON PRODUCTION: pins the
#               new nightly GitHub Actions screen audit (.github/workflows/
#               screenwatch.yml) -- cadence + dispatch, the live screencheck
#               invocation against mrcadabra.com, the secret-not-committed audit
#               code with a loud missing-secret failure, kept artifacts, a bounded
#               run, and CLI agreement between the workflow and screencheck.py.
#   2026-08-18  BUILD hv -- PART 3bm, ONE STORAGE BACKEND, LOUDLY: a real restore
#               drill proves token tables are withheld (a signed-in token dies with
#               the restore), a family deleted AFTER the snapshot stays forgotten
#               (deletions ledger re-applied), and post-reset work OLDER deletions
#               would wrongly erase survives; a dead configured DB gates the chat
#               lane with the warm maintenance message while ALLOW_FILE_FALLBACK
#               lifts the gate on dev boxes; source pins for the loud backup pass
#               and the automated off-site email copy.
#   2026-08-18  BUILD hu -- PART 3bl, THE SERVER RECORDS THE RESULTS (Class E's
#               flagship): live drill proves the tag records exactly once, the echo
#               deduplicates (checks_taken/quizzes_taken never double), a MINTED
#               result 409s with a "client_result_rejected" system_events row and
#               leaves no trace in mastery, a [[finalexam]] outside an exam turn
#               records nothing, and the misses ride the tag server-side. The
#               missed-pipeline drill and the hs POST family moved to the new truth
#               path; course_trial.py follows the honest flow end to end (and now
#               proves the minted-final 409 as part of the journey).
#   2026-08-18  BUILD ht -- PART 3bk, BOUNDED AND SPLIT: every Anthropic client
#               constructed with the 60s timeout (counted, all sites); the three
#               teaching pages carry the 90s abort + warm bubble; _require_admin's
#               tiers proved LIVE (unset graver key -> 503 fail-closed; right key
#               opens; the general key and a wrong key are refused at the graver
#               doors); admin.html's graverKey() flow pinned.
#   2026-08-18  BUILD hs -- PART 3bj, THE CREDENTIAL LEAVES THE URL (Phase 5 begins):
#               a live TestClient drill proves all 10 GET routes and the POST family
#               in BOTH forms (header+/me and legacy path), bare-'me' rejection, the
#               speak ticket lifecycle (mint -> stream -> bogus 410 -> legacy alive
#               -> 401 on a bad code), and library's header form; source ratchets
#               (concatenation-shaped, comment-proof) fail the build if any page
#               reverts to building an API URL with the code or the spoken line;
#               analytics.js's KID_PAGES guard is pinned (Jim's Plausible ruling).
#   2026-08-18  BUILD hr -- PART 3bi, THE STORY KEEPS ONE UNIT: 10 fixtures in both
#               directions (incl. the nightwatch catch verbatim and its suggested
#               fix, the resolving shopping story, the two-facts "and", money-only
#               and objects-only traps); canonical sweep; wiring checks (clause in
#               the prompt, referee in the sweep, RULE_VERIFY[32] -> ENFORCED for
#               the caught shape, honestly scoped). RULES.md regenerated.
#   2026-08-18  BUILD hq -- PART 3bh, THE TWO-PROMPT-SIZES EXPERIMENT IS RUNNABLE:
#               the --prompt-size lever exists and threads through; the large
#               student is all-heard + forced-verbatim and assembles the genuine
#               over-ceiling worst case (both sizes built in-process, free);
#               nightwatch survives run_scenario's new 4-member return; the report
#               states how to read the comparison. The live halves need keys and
#               run on Render -- what the battery can prove without keys, it now
#               proves on every push.
#   2026-08-18  BUILD hp -- PART 3bg, THE ORDER OF AUTHORITY: exactly one absolute
#               supremacy claim (GROUND_RULES); the five-level lattice present with
#               its tiebreakers and the audited cross-pulls named by number (65 over
#               fading, 64 over 23); the opener block re-scoped to level 3; the
#               lattice provably rides GROUND_RULES into all three lanes; and
#               RULES.md is regenerated to a temp file and byte-compared on EVERY
#               push -- it was two builds stale with nothing checking it, and now
#               a stale copy fails the build (run `python ruletests.py --rules`).
#   2026-08-18  BUILD ho -- PART 3bf, THE RECORD-CLAIM REFEREE (the count-claim
#               probe's promotion). RECORD_CLAIM_CASES: 19 transcript-shaped
#               fixtures in both directions, including the audit's own shapes (the
#               watch-count refusal, the phantom "Unit 9 in progress", the invented
#               "last score") and the traps that must stay silent (true scores, true
#               mastery, future conditionals, in-reply results, no-record lanes);
#               the canonical corpus swept with a full record; wiring checks pin
#               _claim_record -> meta["record"] -> the sweep, and the whole-reply
#               result-tag exemption.
#   2026-08-18  BUILD hn -- PART 3be, THE STREAK LIVES ON CALIFORNIA TIME (Jim's
#               THREE CLOCKS ruling): wiring checks (_bump_stats reads
#               _streak_today/_streak_now; default zone America/Los_Angeles; the
#               decision recorded in the CLOCKS note; tzdata in requirements) plus
#               a subprocess proof that STREAK_TZ genuinely steers the calendar
#               (UTC+14 vs UTC-12 never share a date) and that a bogus zone falls
#               back to the UTC day without crashing the import. PART 3bc's streak
#               proof now computes yesterday/gap on the STREAK'S clock -- computed
#               from UTC it was wrong for the ~7 hours a day the calendars disagree.
#   2026-08-18  BUILD hm -- PART 3bd, THE HONEST OPENER AND THE VALIDATED DECLARATION
#               (Phase 4 of the full-app review begins -- Class D). UNITPLAN_CASES
#               exercises the NINETEENTH referee (tutor.unitplan_conflict) in both
#               directions on transcript-shaped replies, incl. the phantom-Unit-5
#               shape; the canonical corpus (all foundation scripts, every course)
#               is swept for false fires; wiring checks pin the one grammar source
#               (tags.UNITPLAN_UNIT_PATTERN), the meta arming, the filing gate
#               (_accept_declared_unit + the "unitplan_rejected" telemetry), the
#               code-branched opener (no-record forbids a recap; returning states
#               facts from the server; the gap refresher reads the record), and rule
#               0's new precedence (THE NOTES WIN). _HM_PROOF drives the allowed-set
#               table, the filing gate, the rejection telemetry and the opener
#               has-record decision on a REAL temp SQLite database on every push.
#               ALSO: the nightwatch restart-safety block now pins the clock in BOTH
#               places it is read (write_report gained now=), because the hardcoded
#               2026-08-17 version went red the day the calendar rolled past it --
#               a test that pins the clock must pin it everywhere the code reads it.
#   2026-08-17  BUILD hl -- PART 3bc, THE SMALL CUTS OF PHASE 3: wiring checks (the
#               file-fallback history probe parses "::" like _ck builds it and both
#               login sites OR it into "returning"; record_topic_quiz claims an
#               existing row by (code, course, unit, topic_idx); the three practice
#               writers all bump stats through the one atomic _bump_stats and the
#               read-then-write streak trio is gone; THE THREE CLOCKS decision block
#               exists) plus _HL_PROOF, a behavioural subprocess on a temp SQLite
#               database every push: a rephrased topic quiz HEALS into one row
#               (best=max, taken summed, latest name kept); 80 threaded practice
#               marks land exactly with zero errors; the streak +1s on a
#               yesterday-active student and resets after a gap.
#   2026-08-17  BUILD hk -- PART 3bb, NO EXCHANGE CAN BE LOST: wiring checks (CAS
#               writer exists; both chat-path writes go through mutate_history; no
#               whole-blob save remains in the handler) plus the threaded hammer on a
#               real database every push -- 96 appends land exactly, pairs adjacent,
#               the two-first-turns insert race is safe, the 60-message cap holds.
#               The hammer EARNED its keep before it ever entered the battery: it
#               caught the row-lock version silently losing 200 of 240 appends on
#               SQLite (pysqlite begins transactions at the first WRITE, so the
#               locked read wasn't) -- zero errors, pure data loss. The CAS rewrite
#               exists because of that run.
#   2026-08-17  BUILD hj -- PART 3ba, ONE OWNER FOR "WHICH UNIT": wiring checks (the
#               resolver exists; prompt, referee, tracker and probe consume its
#               result; the placement note expires) plus the six-case priority table
#               proved against a real database on every push. The gs link checks
#               repointed: the focus guard is now the resolver's SOURCE, not a raw
#               number re-test. The priority test caught a real design error before
#               it shipped: the first progression walk started at unit 1 and sent a
#               placed-at-3 student backward the moment they mastered unit 3 -- the
#               placement is a FLOOR, and the walk now starts there.
#   2026-08-17  BUILD hi -- PART 3az, THE COUNTERS ARE ATOMIC: source checks that the
#               five converted store sites compute in the database, plus a REAL
#               behavioural proof on every push -- a subprocess brings up store.py on
#               a temp SQLite file, checks serial semantics (a bad retake never
#               lowers the best; a status never downgrades), then hammers it with 40
#               threaded writes and requires exact counts and a true max. A lesson
#               from writing it: the first hammer expected "practiced" as the deepest
#               status and FAILED -- because some hammer scores hit 95% and
#               record_check itself upgraded the unit to "mastered". The data was
#               right and the expectation was wrong; the assertion now says so.
#   2026-08-17  BUILD hh -- ONE TAG GRAMMAR: TAG_HANDLER, TAG_INLINE, CONTENT_ATTRS
#               and the live BOARD_TAG regex now DERIVE from tags.py -- the battery
#               validates the contract, it no longer declares it (declaring it here
#               meant the checker and the checked could drift in step and notice
#               nothing). New PART 3ay: registry internal consistency (with the
#               balance/machine/objects dedicated-renderer overlap PINNED, not
#               forbidden -- my first draft of that invariant was wrong and the data
#               was right), the derivations in tutor.py and this file, and every
#               page dispatcher's tag set checked against the registry
#               (mutation-verified with an unregistered [[sparkle]]).
#   2026-08-17  BUILD hg -- ONE REPLY PIPELINE: new PART 3ax (pipeline exists, exactly
#               one _create_verified call site, no lane-private Anthropic clients, all
#               three getters route through it, TODAY net stays lesson-only, prompts
#               stay CALLABLES so they build inside the try). PART 3at's failopen
#               needle and PART 3av's meta needles updated to the one-pipeline form.
#               A lesson from installing it: the last function in a file needs an
#               end-of-file boundary in body-extraction regexes, or its check reads an
#               empty body and fails on healthy code.
#   2026-08-17  BUILD hf -- ONE MICROPHONE: PART 3aw gains mic.js (functions + state,
#               including micTypeHint, the per-page wording knob); the gr spoken-letter
#               client checks (expectsALetter + expect=letter, the narrow gate) are
#               asserted once against mic.js, with each page checked for the include.
#               The mic was where build gz's two live defects were born -- the module
#               plus these guards is the blanket answer.
#   2026-08-17  BUILD he -- ONE BOARD: PART 3aw gains board.js (19 named functions +
#               its state/constants table); PAGE_PARITY's fitRow needles became "the
#               page loads /static/board.js" plus fitting checks asserted once against
#               the module; the board-tag CONTRACT (_board_contract) reads renderers
#               from board.js AND the page, so it survives functions living in either;
#               showColumn's byte-identical-on-three-pages check became "exists once,
#               with its guarantees" (the stronger property -- one copy CANNOT drift);
#               the spotlight checks split honestly: existence/keys once against the
#               module, CSS and the clearSpot CALLS still per page, because a glow
#               never outlives its moment only if THIS page's turn code clears it.
#   2026-08-17  BUILD hd -- ONE VOICE: the gn/gp3 head-of-clip guarantees (no flat 300ms
#               kick, wait for "running", never freeze past the ceiling, ctx0 in the
#               probe, [voicehead] carried) moved from three per-page assertions to ONE
#               assertion against static/voice.js -- plus a new guard that warmUpAudio
#               wakes the keep-alive (build cb, unified by hd: topic/practice had
#               silently lost it, the review's F9). PART 3aw gains voice.js AND a state
#               table: a page that re-DECLARES moved state (audioWarmed, ttsAudio, ...)
#               is a parse-time SyntaxError that kills its whole script, so the battery
#               fails it first. Mutation-verified: re-inlined speak() and a re-declared
#               audioWarmed both caught.
#   2026-08-17  BUILD hc -- ONE COPY: PART 3aw, and three existing parts repointed at
#               the single source. The spoken-text transforms and the board/variable
#               renderer moved out of the three teaching pages into
#               static/speech-text.js and static/board-text.js. Consequences here:
#               PART 3aw (new) fails the build if a page re-inlines a shared function,
#               drops an include, or loads it after its own script -- proved by
#               re-inlining styleVarsCore into topic.html and watching it fail.
#               PART 3 ran the forSpeech cases three times, once per copy, because
#               there were three copies; it now runs them ONCE against the module and
#               asserts each page LOADS it. The gn2/screencheck seam checks read
#               board-text.js instead of session.html -- one table to match, not three
#               that can drift. PAGE_PARITY guards the INCLUDES now, not the inline
#               text. PART 3au learned to read globals supplied by <script src> files,
#               so the sweep does not howl at the very refactor it exists to protect.
#   2026-08-17  BUILD hb -- THE NET: PART 3au (the undeclared-identifier sweep) and
#               PART 3av (the fourteenth referee, re-armed). Phase 2 of the full-app
#               review puts this net up BEFORE the shared-module extraction goes in.
#               PART 3au is the answer to build gz's two live defects -- a fix
#               hand-copied between pages without the state it reads, which no layer we
#               owned could see. Pure stdlib (no node, no npm, no pip: a check that
#               skips is a wish). It narrows the universe to identifiers that are
#               PAGE-LEVEL STATE on a sibling page, then does real brace-scope analysis
#               on just those -- a full JS scope analysis in regex produces noise, and a
#               checker that cries wolf gets ignored. Silent on all 13 shipped pages;
#               fires on both gz defects reintroduced verbatim, with the right diagnosis
#               for each half of the class; fires on 5 mutations injected into 4 pages.
#               It also SELF-TESTS on every run: an analyzer that has gone blind reports
#               exactly what a clean codebase reports.
#               PART 3at's beacon checks were REWRITTEN after they passed while build ha
#               had corrupted eight pages -- they read the raw source and found a
#               COMMENTED "<script". They now read comment-stripped source and assert no
#               bare prose before <head>, plus new screencheck page-coverage checks.
#   2026-08-17  BUILD ha -- PART 3at, EYES: THE APP MUST WATCH ITSELF. Pins every piece
#               of the telemetry build: the store layer answers safely with the DB off
#               (record_event/event_stats/recent_events/last_event_at/purge), every one
#               of tutor.py's ~19 crash handlers carries its _event call, the referee
#               sweep counts fires by name, the pass-throughs/probes/promptsize/catch-
#               alls are wired, /api/client-error + its flood guard exist, /health
#               reports subsystems + ops ages, the heartbeat/backup/nightwatch stamp
#               themselves, telemetry is purged, client-log.js is present AND the
#               FIRST script on every teaching page (a script that loads before the
#               beacon can crash unheard), the /admin card and the night watch's
#               morning section read the counts. PAGE_PARITY gains the beacon needle.
#   2026-08-17  BUILD gz -- PHASE 0 OF THE FULL-APP REVIEW. Four fixes, four sets of
#               checks, three parts touched:
#               PART 3h: the ceiling now has ONE definition (tutor.PROMPT_CEILING --
#               this file used to own a private CEILING while the serving path checked
#               nothing, which is how all-heard students shipped at 186,890-194,284
#               chars on every course, over the ceiling, silently). New worst-case
#               checks: the all-heard prompt must FIT (gz defers heard wording), every
#               heard script must still be OFFERED by name (rule 40), and a refresher
#               turn (foundations_force_verbatim) must restore the full wording.
#               PART 3e: two new parity needles -- lastTutorText declared AND assigned
#               on every teaching page (topic/practice used it undeclared: a
#               ReferenceError on every spoken answer, "I didn't quite catch that" on
#               two of three pages) -- plus keep-alive resume checks: topic/practice
#               read their own audioWarmed, never session.html's `started`.
#               PART 3as (new): the ops heartbeat is never gated by WEEKLY_EMAIL (the
#               old early-return silently disabled backups + the night watch); the
#               refresher wiring exists in main.py; store.usage_stats reports
#               verify_prose-unresolved / verify_empty; admin.html shows the
#               shipped-unresolved tile.
#   2026-08-17  BUILD gy -- PART 3ar, A RULE SPOKEN AS A LAW. The sixth and last cause
#               from the day's audit triage, and the one where the DISCRIMINATOR mattered
#               more than the detector. Rule 54's banned list gains the rest of the classic
#               bad mnemonic ("is means equals, of means times") plus of/per/each, without
#               touching vocabulary -- "sum means addition" NAMES an operation and rule 37
#               requires teaching it; "of means multiply" merely CORRELATES inside one
#               problem type, and a child applies it to "3 out of 4". Rule 61's fraction
#               case is born ENFORCED as the eighteenth referee, and it is only decidable
#               because the same lesson states the condition correctly three times -- so
#               the check is not "is this claim true?" but "is the condition in the
#               sentence?". 16 cases both directions plus the 1,015-string canonical sweep,
#               which is the test that matters here: the fraction library states this rule
#               many times over and 0 of those statements fire. Rule 54 COVERED -> ENFORCED.
#   2026-08-17  BUILD gx -- PART 3aq, A REQUEST TO BE SHOWN, REFUSED (rule 65, the
#               seventeenth referee). The referee needs all three conditions together --
#               they asked to be shown, nothing was worked out, and the job went straight
#               back to them -- so the cases prove each one alone is silent. Rule 65's own
#               remedy (working it, then handing over a NEW one) must pass, or the rule
#               would be unfollowable.
#   2026-08-17  BUILD gw -- PART 3ap, THE BARE ANSWER-DEMAND, THE DECIMAL, AND A REFEREE
#               THAT FOUGHT US. Two audit findings turned out to be ONE defect: a board
#               line with no "?" is invisible to rule 15's and rule 44's checks at once, so
#               "What do you get?" over "2.6 + 1.35" slipped past both. Under it sat gk's
#               fraction bug in decimal clothing -- the "1" of 1.35 found inside the word
#               "one". ⭐ And the canonical sweep, run only to prove those fixes harmless,
#               found a THIRD thing nobody had reported: gl's self-correction referee had
#               been REGENERATING TWO FOUNDATION SCRIPTS since it shipped, because they say
#               "hold on to this". No audit found that. The corpus did.
#   2026-08-17  BUILD gv -- PART 3ao, THE INVENTED HISTORY. Seven claims about what had
#               already happened that were untrue, split on whether a referee can check
#               them: gm's narrated-method referee gains a TOTALITY branch (a "start to
#               finish on your own" claim over a fragment) and is tested there both ways,
#               while the false COUNTS ("you've now watched this move twice", said twice
#               and false both times) get the [countclaim] PROBE instead -- a referee sees
#               one reply and cannot count a conversation. Measure when you cannot verify.
#   2026-08-17  BUILD gu -- COLD_QUIZ_CASES: RULE 47 STOPS BEING A WISH (the sixteenth
#               referee). ⭐ The most damning find in the day's triage and the clearest
#               argument this battery exists: the sentence "let's do it -- five questions,
#               all on finding the percent of a number" was caught on 2026-08-11, rule
#               47(d) was WRITTEN from it, and the tutor produced it again WORD FOR WORD on
#               2026-08-17 -- because rule 47 was COVERED and nothing watched it. The cases
#               include 47(d)'s own sanctioned remedy, which the first draft of the
#               detector rejected. Rule 47 COVERED -> ENFORCED.
#   2026-08-17  BUILD gt -- THREE MORE MALFORMED BOARD SHAPES (BOARD_NOTATION_CASES): an
#               arrow after an equals sign, a question stuffed inside an equation, and a
#               tautology. No judgement is required for any of the three, which is exactly
#               why missing them mattered. Scoped to eq= so a caption may still ask.
#   2026-08-17  BUILD gs -- PART 3an, THE UNIT FOLLOWS THE TEACHING. Jim reported the same
#               symptom twice ("it still says unit one when we are talking about unit
#               five") and BOTH earlier diagnoses were guesses. The chain is now asserted
#               link by link -- the tutor's [[unitplan]] declaration is the authority, an
#               explicit clicked focus still wins, _track_topic records the declaration and
#               not placement, /api/session serves it as progress.current_unit, and the
#               rail prefers it -- because breaking ANY one link brings the symptom back
#               looking like a display bug. The half that cannot be enforced (does the
#               declared unit match the content?) is left to the [unitdrift] probe.
#   2026-08-17  BUILD gr -- PART 3am, THE SPOKEN LETTER AND THE SIGNED ANSWER. Two ways to
#               ignore what a child actually said, both from one Geometry lesson of Jim's.
#               The transcription half is guarded at the seam: a language hint is sent, and
#               a 422 RETRIES WITHOUT IT, so a parameter can never silently break the
#               microphone; the spoken-letter map applies only when a letter was expected.
#               The signed half is rule 64 and the fifteenth referee -- it fires only when
#               the reply affirms a signed answer, then uses the unsigned magnitude, and
#               never mentions the sign, so the right answer ("both 5 and -5 square to 25,
#               but a length can't be negative") passes.
#   2026-08-17  BUILD gq -- PART 3al, THE OPENAI BOUNDARY: A PROMISE BECOMES A TEST. Sharing
#               is ON in the dedicated audit project, which is safe for exactly one reason
#               -- OpenAI is not in the teaching path, and every transcript it marks is
#               synthetic. static/privacy.html promises three processors and says "to
#               anyone, ever." So the build now FAILS if any teaching module so much as
#               references OpenAI, and the failure text names the privacy promise. Proved
#               by mutation: bolting a substitute-teacher fallback into tutor.py fails two
#               checks immediately.
#   2026-08-17  BUILD gp2 -- PART 3aj GAINS S7 (THE CONSOLE IS CLEAN) AND THE REAL POLICY.
#               A CSP violation on every silent-WAV data: URI sat under the console lines
#               we were reading. Nothing was broken -- the header ships report-only -- but
#               silentWavUri() is BOTH the audio warm-up and the keep-alive, so on the day
#               that header is enforced the voice regresses and nobody connects it to a
#               security header. The harness now reads the REAL policy out of main.py, so
#               the rig can reproduce the defect it was written to catch. Both ways: S7
#               fires twice with media-src removed, silent with it present.
#   2026-08-17  BUILD gp -- PART 3ak COVERS THE GOVERNOR'S FACE. go's first live night
#               exposed two holes: the report was served nowhere but a one-line log count,
#               and it COUNTED refutations without NAMING them -- so a reviewer quietly
#               killing real defects looked identical to a healthy one. The status/report
#               endpoints, the 30-night /admin card, the named dismissals and the
#               near-ceiling warning are all held here. Losing rotation coverage silently
#               is the one thing this must never do.
#   2026-08-16  BUILD go -- PART 3ak, THE NIGHT WATCH. Everything that does NOT need an API
#               key: the rotation, the ledger, the report, the email policy, restart-safety
#               and above all the FAILURE paths. A governor is judged by what it does when
#               the critic returns garbage, a lesson explodes, or the key is missing -- it
#               must never confirm a finding it could not verify, never end a night over
#               one bad lesson, and never let a silent cap read as "all clear".
#   2026-08-16  BUILD gn2 -- CASE IS MEANING, AT THE SEAM. The lesson that TEACHES
#               uppercase-vs-lowercase rendered its two lines identically. PART 3aj's seam
#               check follows the renderer from VAR_SKIP to the CASE-SENSITIVE
#               VAR_NEEDS_CONTEXT table, so the checker cannot go blind when that list
#               moves. ⭐ The four regressions in the draft renderer (the article in "A
#               **fact family** is", f and g through function-notation lessons, "(f o g)",
#               "the highest point a thrown ball reaches") were caught by the 1,015-string
#               canonical sweep and by NO hand-written fixture. Fixtures prove the logic;
#               only a real corpus proves the premise.
#   2026-08-16  BUILD gn -- PART 3aj (the screen auditor), LETTER_CASES (rule 63(d), the
#               thirteenth referee) and UNIT_CLAIM_CASES (rule 0's recap clause, the
#               fourteenth). All three come from ONE Geometry lesson Jim ran by hand.
#               The unit one is the one worth re-reading: it LOOKED like a broken progress
#               rail and was the opposite -- the rail was right and the tutor had invented
#               "two days ago we started Unit 5" for a student whose record says "New to
#               this course". A referee that judges a reply against a fact from OUTSIDE it
#               is new here, so it is tested three ways: fires on the wrong unit, silent on
#               the right one, and silent whenever the unit is unknown.
#   2026-08-16  BUILD gn -- PART 3aj, THE SCREEN IS CHECKED TOO. Jim ran one Geometry
#               lesson and found four defects by eye in the first turn -- a formula
#               rendered "a squared plus B squared equals C squared", a triangle lettered
#               on its CORNERS while the words named its LEGS, a rail saying Unit 1 under
#               prose saying Unit 5, and a clipped header. Nothing we owned could have
#               caught any of them: the referees read the reply, lessonaudit reads the
#               transcript, and all four defects are born in the RENDER. PART 3aj runs
#               screencheck.py's six screen checks -- 21 fixtures, both directions, all on
#               real turns -- with no browser and no key, so they run on every push rather
#               than when someone remembers. It also guards the two seams that would make
#               the checker go SILENTLY blind: geo-figures.js's font metrics (17/800 for a
#               vertex, 15/600 for a side -- the only way to tell a corner from a leg) and
#               session.html's VAR_SKIP list.
#   2026-08-16  BUILD gm -- RULE 43 GETS ITS ENFORCEMENT TESTED (18 new cases). Rule 43
#               forbids narrating a method onto a bare right answer, and it was written on
#               2026-08-13 from a live catch. On 2026-08-16 the audits caught the same
#               defect again: the student typed "1 1/2. Next." and was told "that
#               regrouping is exactly the move that trips people up". The new referee is
#               held to its job in both directions here -- the 2026-08-16 case verbatim,
#               rule 43's own two 2026-08-13 examples, and ten turns that MUST stay silent,
#               including praising the answer (the remedy rule 43 actually asks for) and
#               asking rule 59's "how did you get that?".
#   2026-08-16  BUILD gl -- COVERAGE FOR THE ELEVENTH REFEREE. The new ACCURACY sentence is
#               added to PART 1 so it must reach all ten courses, and fourteen checks hold
#               the self-correction referee to its job in both directions -- it catches the
#               audits' own HIGH verbatim, and it never fires on correcting the STUDENT.
#   2026-08-16  BUILD gj -- RULE 41 COVERAGE. Twelve checks holding the new caption referee
#               to its job in both directions (it catches the audits' own bare pie and
#               cookie pictures; it never fires on [[step]], [[write]], [[card]] or
#               [[mark]]), that it is actually wired into prose_board_conflict, and that
#               all 306 authored scripts already obey rule 41 so it can never fight them.
#   2026-08-14  BUILD gh -- A MISSING PACKAGE SKIPS, IT DOES NOT FAIL. Three checks failed
#               (one with a raw traceback) when sqlalchemy or httpx was simply not installed
#               on the machine running the battery. A battery that reports the ENVIRONMENT
#               as broken code teaches you to shrug at red -- and on the day this was
#               written, four genuine failures had been sitting unlooked-at, one of them a
#               prompt 5,595 characters over the ceiling. New dep_gate() skips with the
#               package name. Gated for THIRD-PARTY imports only: a missing module of our
#               own is a broken repo, not an unprovisioned laptop, and still fails.
#   2026-08-14  BUILD gg -- PART 3b AND 3d NOW GUARD THE CONTRACT BUILD gb CREATED. The old
#               promise was "every script reaches every prompt, verbatim, always", and it
#               was right until the library reached 306 scripts and the largest prompt hit
#               185,595 against a 180,000 ceiling. gb carries the LESSON'S UNIT in full and
#               NAMES the rest. These parts asserted the old promise and so failed on
#               correct code -- the worst kind of test. They are not deleted, they are
#               re-aimed, and they now guard three things instead of one: no term ever
#               vanishes (in EVERY unit each term is quoted or at least named -- a term the
#               tutor cannot see is one he will define from memory), every script is quoted
#               verbatim in at least one unit, and a HEARD script is never filtered by unit
#               (rule 40 must be able to restore its exact words, and "remind me" arrives in
#               any unit). The audio-cache check now asks whether a QUOTED script's wording
#               was altered, which is the thing the voice cache actually depends on.
#               Each rewritten check was verified by mutation: deferring a term without
#               naming it, giving a script a unit nobody teaches, filtering a heard script,
#               altering a quoted script's words, and dropping a heard script from the
#               refresher turn are all still caught.
#   2026-08-14  BUILD gf -- PART 3ac READS THE DEADLINE WRAPPER. Build ga wrapped runTutor's
#               three gates in withDeadline() so a gate that never settles cannot strand a
#               student; PART 3ac read those three lines literally and started failing on
#               correct code. It now normalises the wrapper away, asserts the SAME ordering
#               and awaiting rules on what is left, and adds a check that all three gates
#               still carry a deadline -- so neither rule can be dropped unnoticed.
#   2026-08-14  BUILD ge -- PART 3ai, THE DEPLOY STAMP. /health's APP_BUILD is how anyone
#               confirms Render actually took a deploy, and it had gone NINE builds stale,
#               so it was answering that question wrongly at the exact moment Jim needed it.
#               PART 3ai now fails the build when any shipped file carries a dated change
#               note newer than the stamp. Bumping it stops being a habit.
#   2026-08-13  BUILD fe -- THE 2026-08-13 LESSON-AUDIT FINDINGS, CLOSED (NEW PART 3ah;
#               PART 3w grows; PART 2 gains TRIANGLE_CASES). Five audit runs, 19
#               findings, each read against its quoted transcript first. Real: the
#               three HIGHs (the 4|4|4|2 sharing picture left standing; the triangle
#               hypotenuse mis-slotted three times in one lesson; the wrong picture
#               "fixed" in words only) plus thirteen more. New rule 63 (the words and
#               the picture are the same figure) ships with a new referee,
#               triangle_side_conflict -- born ENFORCED, swept in PART 2 against the
#               audit's real tags and every foundation script. Rule 61's corrected
#               list grows five -> nine and PART 3w bans the four new false forms
#               from authored content (the fraction one really lived there, in the
#               basic "fraction" foundation script -- same as el's function-notation
#               case). REJECTED, with reasons recorded in PART 3ah's header: the
#               rule-52 finding (52d decided this exact misread on 2026-08-11), the
#               rule-47 finding (the two-unaided-rights bar was met and 47d's speech
#               was delivered), and the rule-15 finding (a result-less [[column]] IS
#               the pending question). lessonaudit.py transport hardened (read 300s +
#               one transport retry) after two lessons died mid-audit; pinned here.
#   2026-08-13  BUILD fd -- THE PICTURES AND THE PROSE (NEW PART 3ag). Every screenshot
#               on the public site is a photograph of the DEMO -- that is why they can be
#               trusted, and it is also why the copy drifts: the demo changes and the
#               marketing pages have no idea. Re-capturing the shots for the beta push
#               found /homeschool claiming "3h 59m this week" in the paragraph, in the
#               alt text AND in the weekly-email preview, directly above a tile reading
#               2h 15m -- on the page whose whole promise is "a number you can put in an
#               instructional-hours log with a straight face". PART 3ag now reads the
#               numbers out of demo.html at test time and holds the copy to them: Maya's
#               week, the tile's ALT text (the version no sighted proofreader ever sees),
#               the heatmap's student count, and the Decimals scores in the email
#               preview. It also weighs every shot file -- a blank whiteboard is a 40 KB
#               PNG with a perfectly valid filename, which is exactly what the first
#               re-capture produced. Negative-tested: each mutation fails it.
#   2026-08-13  BUILD fc -- THE TRIAL ON THE DASHBOARD, GUARDED (PART 3af extended). The
#               safety-critical property is ISOLATION: the trial invents a parent, a
#               child, a teacher and a class, so it must run as a SEPARATE PROCESS with
#               its own DATABASE_URL and DATA_DIR. PART 3af now pins that, plus the admin
#               gate, the memory guard (a second interpreter costs ~120 MB; an OOM on a
#               512 MB instance would take the live site down), the timeout, the course
#               validation, --json/--validate, the JSON sentinel, and the panel wiring.
#               Negative-tested twice: pointing the trial at the live database, and
#               removing the memory guard, each fail the build. (The first attempt at the
#               memory negative test mutated the ASSIGNMENT and not the COMPARISON, so it
#               proved nothing -- worth remembering that a bad mutation reads exactly like
#               a passing guard.)
#   2026-08-13  BUILD fb -- THE FULL JOURNEY, END TO END (NEW PART 3af). Everything else
#               in this battery checks a PART. This runs one student's whole life through
#               the real app -- sign up, validate three units on the Course Assessment,
#               work the rest, hit the LOCKED Final Exam and read what it says, go back
#               and pass the owed quizzes, take the exam, Course Champion in the trophy
#               case, and the same picture on the parent AND teacher views -- by invoking
#               the new shipped tool course_trial.py. ⭐ It earned its place on its first
#               run by finding a live bug no single-endpoint test could see: a teacher
#               could not add a parent-created student to a class, because the classroom
#               path predated parent accounts and consulted students.json alone. PART 3af
#               also pins that specific regression (the three class lookups must route
#               through _lookup_student), and it is negative-tested by putting the
#               students.json-only check back.
#   2026-08-13  BUILD fa -- SECURITY F2 CLOSED, GUARDED (NEW PART 3ae). This part does NOT
#               trust the source to look right: it stands the real app up against a real
#               database and drives every class endpoint three ways -- anonymously, as the
#               WRONG teacher, and as the owner. That matters, because a source-reading
#               check would have passed on the OLD code too; those handlers looked
#               perfectly reasonable, and they were handing out children's login codes.
#               The drill asserts: every endpoint 401s anonymously · another teacher gets
#               404 on read, summary, reveal, add, remove and rename · no raw login code
#               appears in ANY class response (roster or summary) · reveal returns one
#               code to the owner and 404s a bogus ref · an unowned class can be claimed
#               once and an owned one never · signup inheritance moves only unowned
#               classes · logout really kills the token. Static checks alongside it pin
#               that _class_or_404 and the unauthenticated teacher-classes route stay
#               gone, that every /api/class handler calls _require_teacher AND _own_class
#               (naming any offender rather than counting), and that the page signs in
#               with a token instead of a URL parameter and renders masked codes.
#               NEGATIVE-TESTED three ways: dropping the ownership check, putting the raw
#               code back in the roster, and letting an owned class be re-claimed -- each
#               fails the build, and the middle one is invisible to every check that reads
#               source. The teacher page was also driven in a real browser end to end.
#   2026-08-13  BUILD ez -- A CLIP NEVER EATS SOMETHING BETTER (NEW PART 3ad). Three
#               regressions Jim found by USING the site, all one species: the video work
#               quietly took over something already doing a better job. (1) Build eu put
#               the site-welcome clip on the hero's "Hear him teach" button and returned
#               before the teaching sample -- so the button stopped teaching the day the
#               clip went live, and relabelled itself to a greeting. (2) Two welcomes
#               could stack once the home page started greeting visitors on the way into
#               the demo. (3) After the real demo problem, an audience-door visitor got
#               the WALKTHROUGH's ending -- re-speaking a line already heard and offering
#               the lesson just finished. PART 3ad pins each one where it actually broke:
#               no TutorMoments inside wireHear and the sample still reachable; every
#               worded label on that button is about TEACHING; the marker is set before
#               navigation, read BEFORE the demo's own welcome, and CLEARED; the
#               after-lesson panel passes its signal through, speaks nothing, keeps the
#               congratulations, and never re-offers the lesson. NEGATIVE-TESTED three
#               ways (re-add the hijack / stop clearing the marker / drop the
#               after-lesson argument -- each fails the build).
#               ⚠️ TWO DELIBERATE REVERSALS IN PART 3u2, recorded rather than deleted:
#               the checks that pinned build eu's hijack (the codec retire-and-retry on
#               the teach button, and the relabel-on-window-load) are RE-POINTED at where
#               the behaviour lives now -- the demo CTA -- because Jim reversed that
#               design decision, not because the guards were wrong.
#               Beyond the battery: driven in a real browser -- teach button fetched
#               /api/demo-audio/71 and played it as audio with NO video; the demo click
#               played the welcome then navigated; that arrival played no second welcome
#               and cleared its marker; a direct /demo visit still got the demo welcome.
#   2026-08-13  BUILD ey -- THE VOICE SEQUENCING, GUARDED (NEW PART 3ac). Mr. Cadabra's
#               talking clips now play at the seven moments of a lesson, and one rule
#               holds the design up: a canned clip and his LIVE voice never talk at once,
#               and a clip never REPLACES the personalised line (video cannot say a
#               child's name; the live voice can). That failure is a TIMING failure --
#               silent to every test that reads text, audible exactly once, in a real
#               lesson, as two voices over each other. So PART 3ac asserts the sequence
#               STRUCTURALLY: inside runTutor's own body the three statements must be
#               await runPendingMoment("before") / await speak(clean) /
#               await runPendingMoment("after"), in that order, all awaited, with speak()
#               at the same nesting level so it can never become conditional on the clip.
#               It also pins: every one of the seven moments reaches a REAL trigger and
#               every trigger sits in the function that owns its event (the thumbs-up cost
#               three builds to learn that a clip nothing can fire does not exist); the
#               cadence table (earned moments always play, repeatable ones capped at one a
#               day, so a clip stays a person and not a jingle); the goodbye plays AFTER
#               his words while celebrations play before; the page still works DARK; and
#               [[bye]] is taught in PROGRESS_TAGS_NOTE only, never the shared block.
#               "bye" joins LESSON_ONLY and TAG_INLINE (attribute-free, draws nothing).
#               NEGATIVE-TESTED four ways: dropping the await, making speak() conditional,
#               unwiring a moment, and retuning a cadence each fail the build.
#               BEYOND THE BATTERY, because these checks all read text: the real page was
#               driven in a real browser with a stand-in clip and the media timeline was
#               MEASURED -- clip ended 4867ms, voice started 4867ms (zero overlap); with
#               the await removed, voice started 1807ms against a clip running to 4938ms
#               (3.1s of overlap, caught). Dark path measured too: no moment video, voice
#               unchanged, zero page errors.
#   2026-08-13  BUILD ex -- THE SEVEN VERIFIED TEACHING DEFECTS, GUARDED (NEW PART
#               3ab). The last open items from the 2026-08-12 audit batch: rule 19(e)
#               a never-watched move is modelled before it is asked (the regrouping
#               catch) · 27(c) a story model holds ONE unit line to line (the
#               "3 dollars + 8 tickets" catch, pinned verbatim) · 49(g) the KIND of
#               error is spoken in words the student keeps (the 0.82 place-value
#               catch) · 50(g) the locked Final Exam's reply offers the retake path
#               unprompted · 51(f) a limit carries its approach and each side of an
#               asymptote is its own claim (both calculus catches, incl. the true
#               MINUS-infinity left side) · 52(e) the verdict opens the reply ("No --
#               it's 11") without overriding rule 22's ladder · NEW RULE 62 a
#               back-reference must point at work that actually happened. PART 3ab
#               pins each headline once-in-shared-block + once-in-a-built-prompt and
#               the load-bearing phrases INCLUDING the deliberate guard rails (52e
#               keeps the ladder; 62 keeps connecting-is-teaching; 51f names the true
#               behavior). COVERAGE gains seven needles so every course provably
#               receives all seven. RULE_VERIFY gains 62 (COVERED); RULES.md
#               regenerated -- 62 rules.
#   2026-08-13  BUILD ew -- PLACEMENT NEVER PASSES A UNIT; THE FINAL GATE IS DERIVED
#               (NEW PART 3aa). The 2026-08-13 status doc declared Jim's
#               no-credit-from-placement policy already in force. It was not:
#               challenge.html posted one /api/check per unit with the assessment
#               scores, record_check masters a unit at >= 90%, and _final_exam_state
#               reads that same table -- 5/5 on five placement questions silently
#               passed the unit. PART 3aa pins the policy on every path (no /api/check
#               in the assessment page, postJSON stays gone, post_placement and
#               save_placement inert toward mastery) and pins the keep-the-value half
#               (the placement POST carries strengths + units; PlacementIn round-trips
#               them; the result screen carries the honest sentence written AND
#               framed as quick wins). It also pins build ew's second fix: the
#               final-exam requirement is DERIVED from curriculum.units_for (no
#               "required": 9 literal in code -- comment lines stripped before the
#               ban, same as PART 3w; _units_required verified against every real
#               course's unit count in-process; the gate messages and session.html
#               speak the derived number; the shared FINAL notes in prompts.py are
#               count-neutral).
#   2026-08-12  BUILD eq -- TWO MECHANICAL GUARDS, GUARDED (PART 3z). From the
#               2026-08-12 audits: (1) a NEW malformed-tag referee -- eight referees and
#               none of them checked a tag was even parseable, so
#               [[choices options="yes... | show me one more]] reached a child as ONE
#               button reading '"yes,'; (2) the rule-44 referee's two blind spots, which
#               six findings in five lessons walked through: it needed TWO numeric
#               tokens (and a fraction counts as one, so a whole fraction quiz was
#               invisible) and ANY number in the prose exempted the reply. PART 3z pins
#               the real audit strings on both sides -- the offending lines must be
#               caught, the innocent lines from the SAME transcripts must not be -- so a
#               future tightening cannot quietly start regenerating good replies.
#   2026-08-12  BUILD en -- THE LAST TWO AUDIT ITEMS, GUARDED (PART 3y): rule 49 gains
#               (f) -- when the student NAMES their rule, that is evidence and it is the
#               one you answer (the audit caught a reply correcting a misconception the
#               student never had while their real one survived) -- and the two notation
#               registry gaps are closed: bare < and > (absent entirely, though comparing
#               fractions is core Basic Math) and the imaginary unit (absent though
#               algebra2 teaches complex numbers). PART 3y also pins the FALSE-POSITIVE
#               behaviour, because both patterns were the risky kind: arrows (->, =>) and
#               the or-equal pair must never read as inequalities, and the calculus
#               subscript scripts (x_i, "x · i") must never read as the imaginary unit.
#   2026-08-12  BUILD em -- THE FRACTION PIE, GUARDED (PART 3x). The 2026-08-12 audit's
#               one HIGH finding: a board captioned "one whole, cut into four equal
#               parts" drew TWO wedges, and a beginner was then asked to count three
#               shaded pieces that were never on screen. Verified in the renderer (one
#               wedge per data entry, plus a percentage legend that hands over the
#               answer) and traced to FIVE canonical foundation board lines. New
#               equal-parts mode [[pie parts="N" shaded="K"]]; PART 3x pins it: the
#               renderer must draw exactly N separated wedges with K filled, must print
#               NO text at all (rule 6 -- a percentage on a fractions board answers the
#               question the tutor is about to ask), must cap N so it stays countable,
#               must leave the proportional mode intact for unequal categories, and NO
#               authored pie board line may use the proportional form. Node renders the
#               real SVG in the check -- this is measured, not asserted.
#   2026-08-12  BUILD el -- RULE 61 (a generalization carries its condition), GUARDED,
#               plus the AUTHORED-CONTENT guard that is the real enforcement here. The
#               2026-08-12 audits caught five false universal claims across three
#               courses; mathcheck structurally cannot see them (no arithmetic in
#               "always"), so live replies are prompt-covered. But ONE of the five was
#               not a live slip at all -- it was the algebra1 function-notation
#               FOUNDATION SCRIPT, spoken verbatim to every student who meets f(x).
#               NEW PART 3w: the five known-false forms may never appear in ANY authored
#               content (prompts.py, foundations.py, notation.py), rule 61 must live in
#               the shared block exactly once with its five corrections and its
#               do-not-overcorrect clause, and the true absolutes it protects must still
#               be sayable. High-precision by design: it bans the five SENTENCES, never
#               the word "always" -- "the hypotenuse is always the longest side" is true
#               and must stay.
#   2026-08-12  BUILD ek -- ONE TRUE NAME PER COURSE, GUARDED. THIS FILE WAS PART OF
#               THE BUG. Its COURSES list used the phantom spellings "entrymath" and
#               "basicmath", so for two of the ten courses the whole battery has been
#               proving things about a course that does not exist -- and the two REAL
#               elementary courses ("entry", "basic") were never tested at all. That is
#               why nothing here caught that a real Basic Math lesson was running with
#               an EMPTY misconception catalogue, EMPTY foundation scripts and an EMPTY
#               notation table (0/0/0 bytes, measured). The tests and the content shared
#               the same wrong assumption, agreed with each other, and both disagreed
#               with production. COURSES is now the real keys, and NEW PART 3v is the
#               check that would have caught it on day one: every real course must get a
#               NON-EMPTY block from all three content modules; no module may key
#               content by a name that is not a real course; ruletests' own course list
#               must equal curriculum's keys; lessonaudit must audit real courses; and
#               canon() must resolve the legacy spellings (so no stored student record
#               is orphaned) while leaving unknown names alone (so a typo can never
#               silently become Algebra I again).
#   2026-08-12  BUILD ej -- THE VIDEO PRESENCE LAYER (phase 1), GUARDED. tutor-face.js
#               now carries Mr. Cadabra's video face over the canvas robot, robot as
#               the always-drawn fallback. NEW PART 3u: the robot draw path must
#               survive (any video failure lands on it), the presence must be
#               muted+playsinline+aria-hidden FOREVER (his voice lives in the pages,
#               never in the corner), every media error must tear down to the robot,
#               reduced-motion must get a still poster or the robot, the robot must
#               draw BEFORE the presence tick on every frame, all six coaching pages
#               must still include tutor-face.js and its export must keep draw +
#               moodFrom. FUTURE-PROOF: if/when static/videos/cadabra/presence.json
#               lands (Jim's HeyGen assets), the battery automatically validates it
#               -- parses, has an idle loop, and every referenced file exists.
#   2026-08-12  BUILD ei -- TEACHERS DEMO DOOR REWRITE, GUARDED. The /demo?view=
#               teachers walkthrough now names the replacement threat in its first
#               breath and frames everything as the teaching ASSISTANT. NEW ei
#               needles in PART 3j, same shape as eg/eh: both voice lists must
#               carry "I am not here to replace you", the thirty-hours-a-day
#               assistant line, "no class learns at one speed", "you make the
#               teaching decisions", and the outro's what-it-DOESN'T-do line; the
#               teachers intro/outro anchors must be the NEW ones. Everything else
#               rides the existing enforcement: lists identical + append-only
#               (238 -> 243), every anchor resolves to exactly one line, nine
#               teacher stops on the same panels.
#   2026-08-12  BUILD eh -- STUDENTS DEMO DOOR REWRITE, GUARDED. The /demo?view=
#               students walkthrough now charms the child AND reassures the parent
#               trying the door as if they were their child (Jim). NEW eh needles in
#               PART 3j, same shape as eg's: both voice lists must carry the
#               talks-and-LISTENS intro, the math-ONLY promise, the never-just-gives-
#               the-answer promise, and the nobody-can-give-you-a-trophy line; the
#               students intro/outro anchors must be the NEW ones. Everything else
#               rides the existing enforcement: lists identical + append-only
#               (234 -> 238), every anchor resolves to exactly one line, STU_STOPS
#               still overrides ten-for-ten by index.
#   2026-08-12  BUILD eg -- PARENTS DEMO DOOR REWRITE, GUARDED. The /demo?view=parents
#               walkthrough now answers the two questions a parent brings to a
#               conference table -- "is my child actually learning" and "will she
#               actually want to do this" -- with the tour structure untouched. NEW eg
#               needles in PART 3j: both voice lists must carry the two parent
#               questions, the teaches-never-hands-answers promise, the
#               missed-problem-comes-back line, and the voice-privacy outro; the
#               parents intro/outro anchors must be the NEW ones (the old lines stay
#               in the lists forever -- append-only -- but the parents door must not
#               speak them). Everything else PART 3j already enforced does the heavy
#               lifting: lists identical + append-only (227 -> 234), every anchor
#               resolves to exactly one line, every spoken literal is whitelisted,
#               HS_STOPS still covers every parent stop.
#   2026-08-12  BUILD ef -- HOMESCHOOL CONFERENCE-PITCH REWORK, GUARDED. Jim, pitching
#               at a homeschooling conference, asked /homeschool to LEAD with the
#               points that land at a real table: records/filing first, honest mastery
#               named (80/90, never rounds up), you're-still-the-teacher, and the four
#               trust questions answered plainly. New ef guards (in the eb marketing
#               block): the section ORDER is pinned (records -> hours -> window-in ->
#               ... -> teacher -> trust -> FAQ), the mastery bars and the four trust
#               answers must stay on the page, /privacy must be linked from the voice
#               answer, the method line must name the What Works Clearinghouse (the
#               blanket phrase stays banned), and NO dollar figure may appear (prices
#               live on /pricing alone). FAQ untouched: same 8 questions, still
#               pairwise disjoint; parent-code and walkbtn guards unchanged.
#   2026-08-12  BUILD ee -- THE FIVE TEACHING UPGRADES, GUARDED (rules 56-60 join the
#               shared block; claude/Teaching_Evidence_Base_2026-08-10.md is the
#               source). NEW PART 3t: each rule's headline + load-bearing phrases must
#               be present in GRAPH_TOOL_NOTE exactly ONCE (shared, never per-course);
#               rule 56 must keep its three safety anchors (the announced game, the
#               catalogued mistake, THE WRONG WORK NEVER STAYS); rule 60's two board
#               keys must be documented; and all THREE teaching pages (session,
#               practice, topic) must implement the board spotlight -- spotlightBoard()
#               with the line+board keys, the .stepglow CSS with its pulse, a
#               turn-start clear, and (session) the tour fallthrough so page-tour ids
#               still reach highlightEl. COVERAGE gains five needles so rules 56-60
#               are proven to reach all ten courses. THE CEILING: 150,000 -> 160,000.
#               That number was always a tripwire, not a measurement (see the PART 3h
#               essay); Jim's standing decision (2026-08-11, recorded in
#               Four_Lens_Review: "if you need to raise it, you raise it") authorizes
#               raising it when a teaching upgrade needs the space. This build spends
#               ~8.2k shared characters on five evidence-backed rules -- exactly the
#               trade the decision anticipated. Largest prompt measured 156,515 after.
#   2026-08-12  BUILD ed -- READ-BY-CODE THROTTLE (F1), GUARDED: every GET-by-code data
#               endpoint (session, records, misses, awards, time, topics, assessment,
#               placement, courses, sprints, sprint) must front its work with
#               _read_guard; the guard must cap DISTINCT codes per IP + the raw read
#               rate; _new_student_code must be widened to 4 digits. LIVE SEC2-DRILL:
#               enumeration from one IP 429s near the cap, a fresh IP starts clean,
#               same-code reloads never trip, and new codes match WORD+4digits.
#   2026-08-12  BUILD ec -- SECURITY HARDENING 1, GUARDED: F3 _client_ip must trust the
#               proxy-appended (rightmost) X-Forwarded-For end via TRUSTED_PROXY_HOPS,
#               never the spoofable leftmost (the old .split(",")[0] pattern is now
#               forbidden); F4 the security-headers middleware must stamp the full set
#               (nosniff, SAMEORIGIN, referrer, HSTS, permissions, CSP) with the CSP in
#               REPORT-ONLY mode only (an enforcing CSP would blank our inline scripts);
#               F5 /api/transcribe must cap the read at MAX_AUDIO_BYTES, 413 over it, and
#               re-raise HTTPException so the cap isn't swallowed. LIVE drill (SEC-DRILL):
#               headers ship on a page AND the API, and _client_ip picks the trusted end
#               even when the caller prepends fakes.
#   2026-08-11  BUILD eb -- CALM FEATURES PAGE + FOUR AUDIENCE FAQs, GUARDED: the
#               features page must stay icon-free (no emoji rows, no .ic spans), stay
#               six drop-down sections of >=41 plain bullets, and keep naming the
#               post-rewrite features (sprints, refresher, save/resume, retake,
#               tricky-ones, steer, phone, a11y). Each audience page (students,
#               parents, homeschool, teachers) must end with its OWN 8-question FAQ,
#               and the four question sets are swept PAIRWISE DISJOINT (Jim:
#               "different FAQs"). The dq "phantom parent code" guard now covers
#               homeschool.html too, where the same stale line was found and fixed.
#   2026-08-11  BUILD ea -- THE PACING STEER, GUARDED AND DRILLED: endpoint parent-
#               gated + ownership-checked; the child's explicit choice outranks the
#               plan (rule 50, source AND live-proven); the steered mastery note names
#               WHO asked and protects the student's agency; steers join the reset
#               family; family.html keeps its controls. Live: set -> overview carries
#               it -> _resolve_focus applies/yields/ignores correctly -> clear -> reset.
#   2026-08-11  BUILD dz -- ACCESSIBILITY + PHONES, GUARDED: all three teaching pages
#               must keep their polite live regions, the mic's spoken name, the
#               reduced-motion block, and the phone dock (board first, rail stuck to
#               the bottom); session's four overlays stay real dialogs with focus on
#               the welcome action.
#   2026-08-11  BUILD dy -- CHILD MANAGEMENT, GUARDED AND DRILLED: the four endpoints
#               stay parent-gated + ownership-checked (misses 404 so probes learn
#               nothing); remove keeps its server-verified typed-name consent; attach
#               keeps refusing other families' codes (409) and demo codes; a code
#               change must keep moving EVERY per-student table. LIVE drill: two
#               parents, rename, cross-parent 404s, history follows a new code, the
#               old code dies, orphan attaches, owned code refused, wrong typed name
#               400s, right one deletes account AND data.
#   2026-08-11  BUILD dx -- ASSESSMENT SAVE/RESUME, GUARDED: challenge.html must keep
#               saving after every answer, offering the resume on the start panel,
#               clearing on finish AND on deliberate fresh starts, and discarding a
#               save whose question bank changed (never resume into a different test).
#   2026-08-11  BUILD dw -- REFRESHER + THREE BARS, GUARDED: the opener must keep its
#               gap check (1+ days away -> a real 3-4 sentence refresher with a
#               memory-jog, "a friend catching you up, never a test"), the server's
#               empty-TODAY-bar order must survive (today_live -> per-turn [[today]]
#               demand), and session.html must keep the TODAY placeholder at load so
#               two bars is never the resting state. Both found live by Jim.
#   2026-08-11  BUILD dv -- THE BUZZER-BEATER SHIELD, GUARDED: sprint panels swapped
#               in by the TIMER (break, results) must stay shielded for 1.2s so a
#               click meant for the last answer can never dismiss the celebration.
#               Found live by Jim, on his own product, within hours of dp deploying.
#   2026-08-11  BUILD du -- RETAKE DOOR + PARENT'S TRICKY LIST, GUARDED: the
#               dashboard's 90% line keeps its Retake button (students only, gated on
#               a real quiz score existing); session.html opens the &quiz=1 door like
#               the final-exam door and sends "__unit_quiz__"; main.py interprets the
#               sentinel with the BEST-score reassurance (rule 50); the parent box
#               ("Recently tricky") and the Friday email ("Tricky this week") both
#               answer the most-asked parent question from rule 55's rows.
#   2026-08-11  BUILD dt -- MISSED-PROBLEM MEMORY, GUARDED END TO END (rule 55 joins
#               RULE_VERIFY as COVERED). Source checks: session.html parses missed=
#               and ships it on all three score POSTs; the dashboard's Tricky-ones
#               card exists, hides when empty, fails soft; _keep_misses clamps to
#               total-correct (a tutor can never report more misses than there were
#               questions); GET /api/misses is student-gated; the mastery note hands
#               misses back with rule 55(b)'s revisit-ONE orders; quiz_misses joins
#               the reset family; rule 55 lives in the SHARED block exactly once.
#               LIVE drill (TestClient + sqlite): post a 3/5 quiz reporting 4 misses
#               -> exactly 2 stored, newest first, unit names attached; the mastery
#               note carries them; a 5/5 with a phantom miss stores NOTHING; the
#               sweep holds the newest 200; reset_student_data leaves the list empty.
#   2026-08-11  BUILD ds -- HELP AND SPRINTS-ON-REQUEST, GUARDED (PART 3p block):
#               app-nav's help pill must stay /help and never regress to a mailto
#               (dead on school Chromebooks); help.html must exist whole with the
#               support address as SHOWABLE text; main.py must route /help; the
#               assessment page keeps its help door; session.html must honour
#               &sprint=1; the dashboard's Run-one-now stays student-only.
#   2026-08-11  BUILD dr -- ELEMENTARY VOICE, GUARDED. PART 3e's parity list now proves
#               all three teaching pages use the capability-only canRecord (the mic
#               excludes NO course), that "canRecord = !IS_ELEM" never returns (it
#               would silently mute the students least able to type), and that the
#               prompt's how-they-answer note tells the tutor elementary students may
#               talk, with EXTRA transcription charity for young readers.
#   2026-08-11  BUILD dq -- MARKETING MUST MATCH THE PRODUCT (PART 3p grows the
#               Four-Lens theme-B guards). Machine-caught from now on: parents.html
#               can never again promise the phantom "parent code" or call live
#               features "rolling out"; family.html must keep its per-child Records
#               link, How-are-they-doing narrative, and weekly-email toggle;
#               teachers.html must link the real /teacher tool; records.html's
#               bare-visit message points home, never at URL surgery; the two new
#               endpoints (/api/parent/overview, /api/parent/weekly-email) exist and
#               are parent-token gated. Plus the whole family flow LIVE (subprocess
#               + TestClient + sqlite): signup -> add child -> overview numbers ->
#               toggle the Friday email off -> flag lands where the digest pass
#               reads it -> tokenless requests refused.
#   2026-08-11  BUILD dp -- SPRINTS FOR ALL TEN COURSES, AND EVERY FACT RE-DERIVED.
#               PART 3n's coverage bar rises from 27 units/3 courses to 70/10 (a
#               ratchet -- shrinking it means someone's course lost its sprints).
#               The _verify oracle learned every upper-course question shape (one-
#               and two-step solves, slopes, systems, exponent laws, factor pairs,
#               roots/powers, means/medians, angle pairs, triangle sum, Pythagorean
#               triples, circle facts, midpoints, areas, logs, sequences, limits,
#               power/chain rules, antipowers, definite integrals, characteristic
#               roots, probabilities, compositions, zeros, reflections, distributes)
#               -- so the generated-answer sweep now arithmetic-proves the bulk of
#               all ~4,200 problems per seed. The FIXED FACT LISTS (trig values,
#               radians, i-powers, empirical rule, dice, derivative facts, trig
#               identities, ODE orders, Laplace) each get an INDEPENDENT oracle:
#               sympy, math.erf, complex arithmetic, enumeration -- a wrong "fact"
#               fails the build. The unknown-course fixture moved off "calculus"
#               (which HAS sprints now) onto a concept unit left out on purpose.
#               Also fixed (found by this build's probe): _num_choices starved
#               NEGATIVE answers down to one tap button (blanket no-negatives rule);
#               and answers now use the same unicode minus the questions use.
#   2026-08-11  BUILD do -- THE tutor.py SPLIT, GUARDED. tutor.py's prompt text (the
#               eleven templates, GROUND_RULES, GRAPH_TOOL_NOTE, the overlays, scopes,
#               and assessment voices) moved VERBATIM to the new prompts.py; the move
#               itself was proven byte-identical outside this battery (52 built
#               prompts hashed before/after, 52 equal). What THIS file now guards
#               forever: PART 3h proves prompts.py stays TEXT ONLY (AST: top-level
#               string/dict assignments -- no imports, defs, classes, or calls; the
#               boundary is the point), that tutor still re-exports every moved name
#               non-empty (every tutor.<NAME> reference keeps working), and that the
#               assembled lesson prompt kept its full size. The range=" sweep and the
#               auditor's never-writes list both learned the new file. No check was
#               weakened; every existing check runs against the split layout
#               unchanged -- the whole 2,7xx-check battery IS the do-no-harm proof.
#   2026-08-11  BUILD dn -- PART 3q's key-transport block closes dg's documented
#               residual: /community?mod= was the LAST key-in-a-URL. New checks prove
#               community.html reads the key from the SHARED sessionStorage stash
#               ("mt_admin_key" -- /admin unlocks both), honours a legacy ?mod= link
#               once then scrubs the address bar, sends the key in the X-Admin-Key
#               header and NEVER in the request body, and clears the stash on a 401;
#               admin.html builds no key-carrying URL of any kind; POST
#               /api/forum/moderate takes the header through the same _require_admin
#               constant-time gate as every other admin call. The whole door is also
#               proven LIVE (subprocess + TestClient + sqlite): wrong header 401s,
#               the right header gets PAST the gate (400 bad kind / 404 unknown id),
#               the legacy body key still authorizes (a cached pre-dn page must keep
#               working across the deploy), and no key at all is refused.
#   2026-08-11  BUILD dm -- PART 3n grows the DISPLAY half of the sprint guarantee:
#               the dashboard's sprint-record card starts hidden, never renders on an
#               empty history (sprints never gate, an empty card is a nag), compares
#               this student only with this student (rule 42), fails soft, and the
#               endpoint is student-gated -- plus the whole display drill run LIVE
#               against a real database (two sprints recorded through store.record_
#               sprint, read back oldest-first with the personal best).
#   2026-08-11  BUILD dl -- the two WWC-Strong teaching rules land: 53 (the number line
#               used on purpose -- magnitude and comparison, fractions between 0 and 1
#               first then past 1, benchmarks 0/half/1, equivalents at ONE position)
#               and 54 (word problems have TYPES -- Change, Equal Groups, Compare; the
#               type chooses the operation; key-word rules are BANNED). Rule 54(b) is
#               ENFORCED from day one: board_notation_conflict now also catches the
#               tutor TEACHING a story-cue shortcut ("altogether always means add"),
#               in prose or on a board, with the vocabulary distinction honoured (a
#               "sum means add" definition is rule 37, not a shortcut) -- five new
#               fixtures, both corpora swept clean.
#   2026-08-11  BUILD dk -- BATCH E of the audit re-run. BOARD_NOTATION_CASES: the two
#               notation abuses quoted from real re-run boards ("$50 + 10% = $55" and
#               "a^2 + 64 = 100 = ?") become permanent referee fixtures with the legal
#               shapes as FALSE cases (the "of" form, percent-with-percent, pending
#               percent lines, worked chains ending in a number). The foundation-corpus
#               sweep grows to FOUR draft-level referees. PART 3r gains the
#               point-on-a-hole fixtures (dropped at the hole, preserved elsewhere).
#               RULE_VERIFY: 27 moves COVERED -> ENFORCED for the percent-sum shape.
#   2026-08-11  BUILD dj -- PART 3s: BACKUPS. A backup system is only real if the
#               restore has been rehearsed, so the battery now performs the whole
#               drill on every run: seed a real SQLite database through the public
#               store API, snapshot it with export_all, prove the DRY LOOK changes
#               nothing, restore into a second blank database THROUGH THE ACTUAL
#               restore_backup.py tool (gzip file and all), and prove the two
#               databases row-for-row identical. Boundaries proven from source:
#               main.py never calls import_all (no restore endpoint can exist), the
#               download rides the X-Admin-Key header, the nightly pass is fenced and
#               atomic, rotation keeps BACKUP_KEEP, /admin has the download button
#               (cx: buttons, not instructions) and NO restore control, and
#               RECOVERY.md + restore_backup.py ship complete.
#   2026-08-11  BUILD di -- PART 3r: the figures the audit could not draw, proven
#               through the REAL renderer (node executes math-figures.js, the same
#               file the browser runs). Piecewise domains clip and mark their own
#               endpoints (open for strict, closed for inclusive -- the audit's jump
#               figure is the fixture); an unparseable domain fails OPEN; the shared
#               tool note reaches all ten prompts; and the three showColumn bodies are
#               compared byte-for-byte (build-bk drift class) with align="last" proven
#               unable to complete a wrong sum. ⭐ THE HARNESS'S FIRST RUN FOUND A LIVE
#               BUG: hole= had NEVER drawn on a genuine 0/0 removable point -- the
#               renderer evaluated the function AT the hole, got NaN, and bailed; the
#               feature only worked on functions DEFINED at the point, which is exactly
#               where holes do not belong, and the canonical scripts had quietly worked
#               around it with pre-simplified forms. Fixed with a numeric limit (both
#               sides sampled and required to agree), and the asymptote case -- where
#               painting a hole would be rule 51(e) broken in pixels -- is a permanent
#               NEGATIVE fixture.
#   2026-08-11  BUILD dh -- the audit's teaching findings, tested. ANSWERED_CASES (rule
#               17's new referee: the board must not answer the question -- the audit's
#               ticket card is the fixture, plus commuted and word-number variants, plus
#               the shapes good teaching uses as FALSE cases) and UNSPOKEN_CASES (rule
#               44's new referee: a numeric board problem with a numberless spoken ask --
#               the audit's "First question: ... What's the answer?" is the fixture).
#               The foundation-corpus sweep now runs ALL THREE draft-level referees
#               (self-answer, answered-q, unspoken) over every canonical script on every
#               run, so a future widening cannot quietly start flagging correct lessons
#               (the build-cy discipline, now paid for twice). RULE_VERIFY: 17 and 44
#               move COVERED -> ENFORCED; rule 52 declared (COVERED). Junk-input
#               never-raises covers the two new referees.
#   2026-08-11  BUILD dg -- PART 3q (reliability) + the audit-log misfires become
#               permanent referee cases. The first full audit's Render logs proved the
#               stumbles were OUR bugs, not rate limits: the rule-15 referee counted the
#               pronoun "one" as a number and had no concept of an OFFER (a dozen
#               misfires in forty minutes, each burning a paid draft -- and the geometry
#               lesson's worked example with them, S-1); claude-sonnet-5 intermittently
#               rejects assistant-prefill continuation (each rejection was a stumble);
#               five replies shipped as admitted partials at the 1600 ceiling. Every
#               quoted misfire is now a PENDING_CASES / SELF_ANSWER_CASES fixture (plus
#               guards proving the exclusions did not swallow the referee), and PART 3q
#               proves with a scripted client: the negotiated prefill fallback (the
#               named 400 switches shapes and is REMEMBERED; unrelated errors still
#               raise), the 3000 ceiling, the one silent retry on an empty reply, the
#               stand-alone wording in both regeneration nudges, and the admin key's
#               exit from query strings (X-Admin-Key header; sessionStorage; no
#               key-carrying URL built anywhere in admin.html).
#   2026-08-10  BUILD df -- PART 3o learns the SIXTH unit-name copy and PART 3p bans two
#               phrases from marketing copy. Jim asked for a sweep proving no blanket
#               "evidence based learning" claim exists anywhere. It doesn't -- but the
#               sweep caught courses.html (the PRINTABLE scope & sequence) still saying
#               "taught Socratically" (missed by build cc's site-wide removal) and still
#               listing the pre-restructure diffeq units, plus llms.txt claiming unit
#               mastery at 80%+ (it is 90%+ on a ten-question Unit Quiz) under the old
#               MyTutor brand name. All fixed in df. PART 3o now parses courses.html's
#               ten unit lists (order-based; the cards sit in curriculum order); PART 3p
#               strips HTML comments then fails the build if "Socratic" or
#               "evidence-based" appears in any static page, llms.txt, or README.md.
#   2026-08-10  BUILD de -- PART 3o: unit-name parity across all FIVE files. The diffeq
#               restructure (CUPM mainstream syllabus) edited the same nine unit names
#               in curriculum.py, pedagogy.py, session.html and topic.html, and nothing
#               proved they agreed -- each file works fine alone while the picker shows
#               one name and the tutor teaches another. curriculum.units_for() is now
#               the declared source of truth and the other four are compared to it byte
#               for byte for every course. Writing the check found the FIFTH copy:
#               challenge.html's *_UNIT_NAMES (the labels on assessment results), which
#               still carried the OLD diffeq units -- fixed in the same build, and its
#               banks are also shape-checked (9 units x 5 questions, answer index 0-3),
#               since the diffeq re-mapping is exactly the edit that could leave a unit
#               short a question. Any future rename that misses a file fails the
#               battery instead of shipping.
#   2026-08-11  BUILD dd -- PART 3n: fluency sprints. Priorities in order of what they
#               would cost a child: all 1,620 generated answers verified RIGHT (a drill
#               that reinforces a wrong fact is worse than none), sprints gate NOTHING
#               (checked at store, endpoint and page level), and half B must be a
#               sibling of half A, not a twin -- the first registry shipped B as a
#               byte-identical twin of A, which would have made "improvement" a memory
#               test, and the sibling check caught two more twin families (percents,
#               make-ten's shifted ramp pushing past nine) before ship.
#   2026-08-10  BUILD dc -- three guards: the auditor must count graceful-failure turns
#               itself (absence is invisible to a content marker), retry a stumbled turn
#               once, and carry the critic's three discipline checks earned from its
#               first-run false positives.
#   2026-08-10  BUILD db -- two guards for the reasoning budget: an "output limit
#               reached" probe result must be retried with room to think (it is proof of
#               access, not absence), and the quiet variant (200 + empty message +
#               finish_reason length) must not end a lesson looking like the student
#               left.
#   2026-08-10  BUILD da -- four guards for probe_models(): the tool must be able to ask a
#               key what it reaches, the pricing button must ask, a model gated behind
#               organisation verification must say so WITH the remedy, and the probe list
#               must be overridable without a code change.
#   2026-08-10  BUILD cz -- five guards from the auditor's first live failure: a preflight
#               before any lesson, a negotiated token parameter, the model list offered
#               only for a real model error, a summary that cannot make "nothing was
#               marked" look like "no findings", and the admin panel repeating the
#               server's summary instead of computing a second one.
#   2026-08-10  BUILD cy -- SELF_ANSWER_CASES and the corpus sweep. Rule 39(b) is ENFORCED
#               now, not merely COVERED. Two of the FALSE cases are real false positives
#               caught by sweeping our own content before shipping: a foundation script
#               ("What is a numerator? The numerator is...") and a demo line that restates
#               the question's own number as a hint. Both are now permanent fixtures, and
#               the suite sweeps every foundation script on every run so a future widening
#               of the referee cannot quietly start punishing good teaching.
#   2026-08-10  BUILD cx -- a check that an admin job the owner cannot reach is NOT
#               SHIPPED. Jim asked "tell me exactly how to run it" and the honest answer
#               was that he could not: both money-spending admin jobs were documented as
#               "POST /api/admin/..." and nothing in the product can POST JSON. The
#               foundation pre-render had therefore sat un-run for days while three
#               handoff documents told him to run it. Every spending endpoint must now
#               have a button on /admin and be priceable from there.
#   2026-08-10  BUILD cw -- PART 3l (the lesson auditor's boundaries) and THE CEILING
#               RAISED 135,000 -> 150,000 with the reason written down where it is
#               enforced. The old note said "consolidate, do not raise"; it was written
#               before anything had been measured. What we know now: 135,000 was a
#               judgement in an audit, the built prompt is ~17% of the model's real
#               window, and rule 51 spent the last 500 characters -- so the NEXT rule,
#               whatever it was, would have failed the build. Merging rules to satisfy an
#               invented number means editing the teaching, which fails invisibly. That
#               is the wrong risk to take on no evidence, and lessonaudit.py is now the
#               evidence: run it at two prompt sizes and set the number from what it finds.
#               PART 3l guards the auditor's BOUNDARIES rather than its findings (those
#               are opinions): the key value may appear in an Authorization header and
#               nowhere else, the job can always be priced before it is run, the price
#               says it is an estimate, and the auditor never writes to tutor.py or
#               foundations.py. A critic that edits the teaching is a second author nobody
#               reviewed.
#               A NOTE ON WRITING THAT KEY CHECK: the first version flagged the dry run's
#               own label line -- the words "OPENAI_API_KEY" printed beside
#               "present"/"MISSING", which is exactly what a diagnostic should say. A
#               check that cries wolf at correct code gets switched off, and then it
#               guards nothing. It now looks for the VALUE travelling, not the name.
#   2026-08-10  BUILD cv -- rule 51 joins the ten-course scan, and a new check that every
#               range= we write PARSES UNDER THE RENDERER'S OWN RULE. The regex is read
#               out of math-figures.js so it cannot drift. It exists because rendering one
#               new figure showed the [[graph]] documentation teaching range="-1,5" while
#               parseRange accepted only "a..b" -- the window was discarded, silently, and
#               the instruction had been unfollowable since the day it was written to fix
#               exactly that complaint.
#               ⚠️ THE OTHER LESSON FROM THIS BUILD is in _cv_welcome_check.py, not here:
#               Playwright matches routes in REVERSE registration order, so a catch-all
#               registered last swallowed the stubbed /api/session and the harness measured
#               the FIRST-TIMER card while reporting on the returning one. It now asserts
#               which screen it is looking at before it measures anything. A test must
#               prove it is looking at the right thing before it is allowed to pass.
#   2026-08-10  BUILD cu -- PART 3k: A BAR MUST BE REACHABLE BY THE INSTRUMENT THAT
#               MEASURES IT. Jim asked for a retake path for a unit passed but not
#               mastered. Checking it found something worse: mastery is 90% and the Unit
#               Quiz was four or five questions, so the only possible scores were 80% and
#               100% -- the bar could only be cleared with a perfect paper. Topic quizzes
#               likewise (four questions, 80% bar). It survived because the bar and the
#               question count live in DIFFERENT FILES and changed on DIFFERENT DAYS, and
#               no test ever multiplied them together. PART 3k does exactly that
#               multiplication, for every quiz, in every course: at least one NON-PERFECT
#               score must pass, or the bar does not mean what it says.
#               Also here: rule 50 joins the ten-course coverage scan, the quiz lengths
#               are scanned in all ten built prompts, and the locked Final Exam must name
#               the units holding it shut AND fall back rather than fail shut.
#   2026-08-10  BUILD ct -- THREE LAYOUT GUARDS, and the first real catch by cs's checks.
#               Jim hit a live one: the demo's answer buttons were a one-per-line grid,
#               the answer zone could take 47vh, and .feed is flex:1 -- so the whiteboard
#               lost every pixel the answers took. PART 3j now insists the buttons are a
#               wrapping ROW (the real classroom's own shape), the answer zone is capped
#               at 35vh or less, and the board carries a min-height FLOOR.
#               ⭐ AND cs's "every tour stop points at a real element" check paid for
#               itself immediately: rebuilding the teacher dashboard removed the
#               tdAttention CARD while its tour stop still pointed at it. glow() returns
#               quietly on a missing id, so that stop would have narrated a dashboard
#               that never moved -- no error, no log, just a paragraph about a panel the
#               visitor cannot see. The line moved onto the roster instead.
#   2026-08-10  BUILD cs -- THE WHITELIST CHECK THAT SHOULD HAVE EXISTED SINCE bx. The
#               demo design notes have said "every spoken string must be on the
#               whitelist" from the beginning and NOTHING enforced it. say() looks the
#               text up in VOICE_LINES and plays clip N by index; a line that is not
#               there does not raise -- that one stop drops to the browser's flat
#               mechanical voice in the middle of Mr. Cadabra speaking. All 24 literal
#               tour lines are now checked, on every tour on the page. Two more: every
#               tour stop must point at an element that EXISTS (glow() returns quietly on
#               a missing id, so a typo means the words play over a dashboard that never
#               moves), and the homeschool override must cover every parent stop (it is
#               read BY INDEX and falls through to the PARENT's words where it is short).
#               A LESSON FROM WRITING IT: the first version wrapped the parse in `except
#               Exception`, which swallowed a NameError -- ast was never imported -- so
#               every line looked off-list and the failure blamed the demo instead of the
#               test. The except is narrow now. A test's error handling must not be able
#               to hide the test's own bugs.
#   2026-08-10  BUILD cr -- PART 3j now proves ONE DOOR, ONE DASHBOARD. Jim: "I don't
#               want any links to any other dashboards from there." Three paths could
#               hand an audience visitor somebody else's screen and all three fail
#               silently, so each is checked against the SOURCE rather than against a
#               comment claiming it: showBalloons must return through the audience
#               ending BEFORE it builds the three balloons, the ending itself must
#               contain no dashboard opener at all, and the dashboard's back button must
#               not close a locked walkthrough (there is no page behind it).
#               Also checked: a locked door still leads somewhere. A test that only
#               proves an absence would happily pass on a dead end.
#               NOT IN THIS FILE, deliberately: the behaviour was also driven in a real
#               browser across all four doors and the open demo (59 checks). That harness
#               needs playwright, and this battery must stay runnable anywhere in a
#               second -- it lives in the sandbox, not the repo.
#   2026-08-10  BUILD cq -- PART 3j grew two checks and one of its own bugs was fixed.
#               New: the walkthrough must open the dashboard BEFORE it starts talking
#               (Jim watched a blank screen talk at him for thirty seconds), and every
#               audience line must be anchored by its opening WORDS, each anchor
#               resolving to exactly ONE whitelisted line.
#               THE BUG WORTH REMEMBERING: my first anchor regex used ["']([^"']{12,80})["']
#               to pull the anchor text out. Four of the nine anchors have an apostrophe
#               inside a double-quoted string -- "the parent's view", "That's the honest
#               read." -- and [^"'] stops dead at that apostrophe. The test found five
#               anchors, called it a pass at >=9 only by accident of failing loudly, and
#               would otherwise have checked less than half of what its name claimed.
#               A test that silently checks a subset is worse than no test. Capture the
#               opening quote, require the same character to close it.
#   2026-08-10  BUILD cp -- PART 3j, the audience walkthroughs. Guards the two things
#               that can break /demo?view=... silently: a marketing page pointing at a
#               view the demo does not implement, and the two voice lists falling out of
#               step. That second one deserves a warning to whoever reads this next:
#               clips are served BY INDEX, so a mismatch plays the WRONG AUDIO under the
#               RIGHT WORDS and nothing errors. While writing this I compared the lists
#               with a naive regex over quoted strings, which matched text inside
#               COMMENTS and made two identical 188-line lists look 117 lines apart. The
#               helper here parses main.py as Python and demo.html as JS-with-comments,
#               which is the only way to answer the question honestly.
#   2026-08-10  BUILD co -- PART 3i AND THE GENERATED RULES INDEX (audit #2 items 24
#               and 23). This file's header has said from day one: "ADDING A RULE? Add a
#               scenario here in the same commit. That is the whole point." We drifted
#               anyway -- rules 42 to 47 shipped with no check of their own -- because
#               nothing made the drift visible.
#               RULE_VERIFY now declares, for every rule, HOW it is verified, in four
#               honest tiers: ENFORCED (a machine catches it in a real reply),
#               EXERCISED (a --live scenario asserts the behaviour), COVERED (the text
#               provably reaches all ten prompts -- he was told, which is not the same as
#               he does it), UNVERIFIED (nothing at all).
#               It is a RATCHET, not a gate: existing debt prints but does not fail a
#               deploy, while a NEW rule with no declaration fails, and a rule that
#               quietly LOSES its scenario fails. Today: 13 enforced, 10 exercised,
#               25 covered, 1 unverified.
#               `python ruletests.py --rules` regenerates RULES.md from the prompt
#               itself, so the index can never drift from the classroom. That file is
#               also what you hand a curriculum advisor or a school district.
#   2026-08-10  BUILD cn -- PART 3h, "it must not degrade, and it must scale".
#               Nothing in this battery had ever asked whether anything GROWS, and two
#               things did: every chat turn loaded, parsed, appended to and rewrote the
#               student's ENTIRE conversation in order to read the last thirty messages
#               of it, and the usage log kept every row forever. PART 3h now checks the
#               transcript cap (and that it stays above what the model reads), the usage
#               retention pass, deliberate pool sizing, age-based rate-bucket eviction
#               and the TTS cache cap.
#               It also asserts the prompt does not FLIP SHAPE between turns -- build cl
#               made it do that to save characters, and the cache arithmetic showed the
#               flip costs about $0.24 an episode to save $0.0005 a turn.
#   2026-08-10  BUILD cm -- CACHE DISCIPLINE CHECKS. The system prompt is one cached
#               block; per-turn content inside it moves the cache prefix and re-bills
#               everything after it. PART 3g now asserts get_tutor_reply takes a
#               turn_note, that per-turn asides never appear in the system prompt, and
#               that two ordinary turns build a byte-identical prompt.
#   2026-08-10  BUILD cl -- DEFERRAL TESTS + THE PROMPT BUDGET.
#               The deferral tests care far more about RESTORING than about saving: a
#               brand-new student still gets every script verbatim, a returning student
#               keeps every UNHEARD script verbatim, heard scripts stay NAMED so he can
#               still offer them, asking restores the exact wording, the default is to
#               carry the words, and the refresher detector is checked on both the
#               explicit ask and the bare "yes" that follows rule 40(b)'s offer.
#               The prompt ceiling is now a BUDGET TABLE, not a single number. A total
#               tells you that you are over and nothing about what to do; the table
#               prices every block, so the next person adding one sees the cost before
#               paying it. Measured and recorded in the failure message: there is 0%
#               overlap between the course templates and the shared rules, so nothing can
#               be reclaimed for free -- the honest options are consolidating rules,
#               deferring another block the way cl defers heard scripts, or raising the
#               ceiling deliberately with the reason written down.
#   2026-08-10  BUILD ck -- PART 3g, the misconception catalogue, and a PROMPT-SIZE
#               tripwire (audit #2 item 22). PART 3g checks every entry has all nine
#               fields, unique ids, a speakable SAY that does NOT open by telling the
#               student they are wrong (rules 20/49c), and -- the important one -- that
#               no `detect` string is just a NUMBER in any spelling. The first end-to-end
#               run matched "I did three plus two first, so twenty" and returned two
#               confident WRONG theories, because "three" and "two" had survived a filter
#               that only required a letter. A numeric answer is evidence only in the
#               context of the problem it answers, and the matcher cannot see the
#               problem. That case is now a permanent fixture.
#               The prompt-size check prints every course's size and fails above 135,000
#               characters. It is a TRIPWIRE set above today's largest (130,022): when it
#               trips the answer is to consolidate overlapping rules -- the rules block
#               is ~45% of the prompt -- not to raise the number.
#   2026-08-09  BUILD cj -- PART 3f, NOTATION COVERAGE. Jim asked the right question
#               after the f(x) fix: "math is filled with these kinds of things. How can
#               we make sure every one of these is caught all of the time?" Fixing f(x)
#               by hand fixed one symbol and guaranteed nothing. PART 3f is the general
#               answer, held against notation.py:
#                 A  every notation on every board we ship is REGISTERED for that course
#                    (317 board strings scanned). Write a symbol the registry does not
#                    know and the build fails -- so a symbol cannot reach a child's
#                    screen without us having said, somewhere, how to read it.
#                 B  the DEEP families need a real script that says them aloud, not a
#                    table row. It caught three courses using subscripts silently.
#                 C  the registry must recognise its own examples, must reach all ten
#                    prompts, and no entry may collide with a narrower one -- that last
#                    invariant was added after the first run reported diffeq's mu as an
#                    unregistered population mean, because two entries matched one glyph.
#   2026-08-09  BUILD ci -- rule 48 and the NOTATION READABILITY check (PART 3b).
#               Jim found f(x) being used in Algebra I with nothing ever teaching it. The
#               check that would have caught it: for every course, if any script writes
#               function notation on the BOARD, some script in that course must read it
#               ALOUD in words and deny the wrong reading by name. It failed on four
#               courses the moment it was written, and on diffeq even after the first fix
#               -- because diffeq writes y(t), y prime and dy/dx rather than f(x), and my
#               first regex only knew about f, g and h. Both halves of the check now
#               share one letter set so they can never disagree again.
#   2026-08-09  BUILD ch -- SCORE_CASES, rules 45-47, and two arithmetic guards.
#               SCORE_CASES covers the new score referee. Its FALSE cases carry the
#               weight again: three false positives were caught here before shipping,
#               including one that revealed the percentage check was matching NOTHING
#               (a stray \b after "%"). Also asserts that tutor.py's pass marks never
#               drift from store.py's, and that no score in any total from 1 to 40 is
#               ever stored higher than the truth.
#   2026-08-09  BUILD cg -- PENDING_CASES and the today-bar guards.
#               PENDING_CASES covers the new rule-15 referee, and the FALSE cases carry
#               most of the weight: rule 39(d) now REQUIRES him to ask "does that click,
#               or should I show it another way?" constantly, and re-rolling those would
#               cost real money every turn. Two false positives were caught here before
#               shipping -- "which number is the denominator in three-fourths?" (the
#               hyphen read as minus) and "is 1/2 bigger than the piece we shaded?" (a
#               fraction counted as two numbers).
#               PART 3d/3e gained the today-bar guards: the store table is in the reset
#               cascade, session.html still rebuilds the bar from SRV_PROGRESS.today at
#               load, and ensure_today_tag() restores a bar a reload destroyed while
#               still never resetting one that is genuinely live.
#   2026-08-09  BUILD cf -- PART 3e, plus rules 41-44 and two new guards.
#               PART 3e "THE THREE TEACHING PAGES MUST MATCH" exists because auditing
#               audit #1 found that item 11 (board lines never wrap) shipped to
#               session.html and never reached practice.html or topic.html -- Jim's
#               broken-equation screenshot was still reproducible on two of three pages,
#               a day after we called it fixed. Same bug shape as build bk, where a rule
#               written into one of eleven per-course templates reached one course. PART 1
#               made that impossible for the prompt; PART 3e does it for the pages, and
#               also proves every board tag the SHARED prompt block teaches is drawable on
#               all three (the six lesson-only tags are named explicitly, and the test
#               fails if one of them ever leaks into the shared block).
#               PART 3c now enforces rule 41: a figure with no caption= is a failure.
#               PART 3d now proves all THREE teaching modes carry the canonical scripts
#               and honour the heard list.
#   2026-08-09  BUILD ce -- three new groups of checks, one per thing Jim asked for.
#               PART 1 gained rules 39 and 40 (coverage across all ten courses).
#               PART 2 gained VISUAL_CASES for the new visual referee -- including the
#               false-positive cases, which matter just as much: a re-roll is a real model
#               call, so ordinary prose about a number line, a promise to draw one next
#               time, and a look back at yesterday's picture must all stay clean.
#               PART 3c gained a drift check: tutor.FIGURE_TAGS (a constant, because
#               tutor.py must not read static files at request time) must still name
#               exactly the tags session.html's handleTags() routes to a figure renderer.
#               PART 3d is new -- foundation memory: the term key survives the model's own
#               capitalisation, a made-up term is rejected, the heard list actually reaches
#               the prompt and marks its scripts, every script stays byte-identical either
#               way (the audio cache depends on it), junk never raises, and the new table
#               is in store's per-student reset cascade.
#   2026-08-09  BUILD cd -- ADDED PART 3c, "board tags actually draw".
#               This is the machine for the failure Jim named on the demo page: "the
#               lesson referred to a diagram that didn't show up on the board... We got
#               one shot to do it right, and it failed." A board tag fails SILENTLY --
#               no exception, no log, the words are still spoken -- when its name is not
#               in handleTags(), when its attribute is not one the renderer reads, when
#               it carries no content, or when an attribute value contains a square
#               bracket (handleTags' own regex ends the tag there). PART 3c PARSES
#               static/math-figures.js, static/geo-figures.js and session.html's
#               handleTags() so the contract is read from the renderers themselves and
#               cannot go stale; a new tag with no entry in TAG_HANDLER/TAG_INLINE fails
#               the suite on purpose rather than being skipped. On its first run it
#               caught 11 already-shipped foundation scripts. It also checks the two
#               ways [[graph]] quietly draws the WRONG picture: lines= on a non-linear
#               expression (parseLinear flattens a parabola into a straight line) and a
#               comma where the grapher splits only on ";" or "|".
#   2026-08-09  CREATED (build bu, proactive audit #25). Every teaching rule we have
#               was born from Jim noticing a failure in a live lesson. That does not
#               scale to real students. This is the machine that notices instead.
```

I did no harm and this file is not truncated.
