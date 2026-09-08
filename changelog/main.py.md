# CHANGELOG -- main.py  (notes rolled out of the file's header)

Moved out of `main.py` on 2026-09-08 (build ui): every CHANGE NOTE dated before 2026-09-01 -- 508 entries, VERBATIM, in the order they sat in the file (newest first). The 75 notes from 2026-09-01 on stay at the top of `main.py` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
#   2026-08-31  APP_BUILD -> "2026-08-31rd-the-main-road-moves-the-star". BUILD rd -- the
#               scripted lane (the main road) graded every tap in code and told the streak
#               NOTHING: today_streak moved neither up nor down there (measured in code,
#               then watched live -- a wrong tap on the counting card fired the
#               intervention and the chips sat still). NEW _script_streak() in
#               /api/script/answer: a correct answer bumps (store.bump_today_streak, new),
#               any wrong tap resets (rc's reset_today_streak) -- ordinary turns graded at
#               the engine's own line (pending problem's ans() vs the tapped value, before
#               step() consumes the pending state; unheard moves nothing; guided asks
#               count both ways), intervention redos graded where code already grades
#               them. The fresh pair rides the response as "streak" and session.html's
#               scrAnswer feeds it to the chips. NO counters move -- scripted problems
#               stay OUT of problems_practiced/accuracy (record_drill's standing
#               reasoning). THE QUIZ LANE IS DELIBERATELY EXCLUDED: a quiz is assessment,
#               and qz already ruled assessment events (record_check) out of the streak --
#               flag for Jim if he wants quizzes to count.
#   2026-08-31  APP_BUILD -> "2026-08-31rc-the-star-falls-when-the-child-slips". BUILD rc --
#               Jim's ruling: a miss is ANY WRONG TAP. Until now only a FINISHED problem
#               moved the today-streak, so a wrong tap inside a still-going problem left
#               the star standing (watched live on 2026-08-31: miss -> no tag -> streak
#               climbed straight through). THREE doors close it: ① the prompt's new
#               [[miss]] tag -> the page posts {miss:1} -> /api/mark's new miss branch ->
#               store.reset_today_streak (today-streak only; NO counters, NO finished
#               problem, accuracy untouched). ② the CODE FLOOR: the chat handler now
#               grades the child's bare answer against the previous turn's computable
#               pending ask (tutor.answer_slip -- the qw/ra parsers, one grammar) and
#               resets without waiting for the model; cautious by design, anything
#               uncertain is not a slip. ③ tags.py registers [[miss]] (attribute-free).
#               Scripted-lane per-answer streaks are a SEPARATE measured gap (build rd
#               candidate): /api/script/answer moves no streak at all, either direction.
#   2026-08-31  APP_BUILD -> "2026-08-31rb-the-chip-says-what-it-counts". BUILD rb -- Jim on
#               the qz streak chips: "there's nothing that says what those are." The
#               classroom pills' only explanation was a hover tooltip; each now carries a
#               visible label in the dashboard banner's own words ("days in a row" / "right
#               in a row today"). static/session.html markup/CSS only; PART 3hc pins the
#               labels in both files. NO CODE IN THIS FILE CHANGED.
#   2026-08-31  APP_BUILD -> "2026-08-31ra-the-leftover-gets-its-buttons". BUILD ra -- Jim,
#               live on entry/basic the same evening qw deployed: "some of the times it's
#               missing bubbles." qw's shipping-door repair only knew plain a-op-b
#               arithmetic, so the youngest courses' comparison / either-or / one-more /
#               comes-after asks shipped bubble-less as counted pass_through residue.
#               tutor.py's new _rb_counting_shapes() closes those four classes, still
#               computed-never-guessed, final spoken ask only; PART 3hb proves each class
#               failable and re-proves the build-pt grid law. NO CODE IN THIS FILE CHANGED.
#   2026-08-31  APP_BUILD -> "2026-08-31qz-a-streak-a-child-can-see-today". BUILD qz -- Jim
#               wants a prominent bar on both the dashboard AND the classroom page showing
#               the day streak (already tracked) and problems answered correctly IN A ROW
#               TODAY, reset the instant one is missed -- a same-day motivator, not a
#               running total. Two endpoints touched: POST /api/mark/{code} now returns the
#               fresh today_streak/streak_days read back from the write it just made
#               (COMPUTED, NEVER GUESSED -- the same reasoning /api/check's best_pct already
#               uses, so the client shows the server's authoritative number, never an
#               optimistic guess); GET /api/session/{code} (the classroom page's own load)
#               now carries progress["stats"] = mastery.get("stats", {}) from the SAME
#               get_mastery() call it already made for checks, so the classroom page's
#               streak chips have a number the instant the page loads, before any mark is
#               sent. All the actual streak math (schema, the atomic write, the day-gated
#               read) lives in store.py; see its own change note for the full design.
#   2026-08-31  APP_BUILD -> "2026-08-31qy-the-ceiling-was-too-low-for-the-room". BUILD qy
#               -- NO PYTHON IN THIS FILE CHANGED besides this stamp; the fix is entirely
#               in nightwatch.py. The 2026-08-31 night watch ran 8 of the rotation's 12
#               lesson slots and was then cut off by the default 45-minute time budget,
#               skipping 2 scenarios outright. Jim, asked whether to raise it: "Yes, raise
#               it." nightwatch.NIGHTWATCH_MAX_MINUTES's default moves 45 -> 90 (45min /
#               8 lessons measured ~5.6 min/lesson; all 12 slots need ~68 minutes at that
#               pace, so 90 leaves margin for a heavier finding night). LESSONS_PER_NIGHT
#               is unchanged at 12, so nightly spend does not move -- the time budget was
#               never the cost lever. Still overridable from Render with
#               NIGHTWATCH_MAX_MINUTES=<n> and no deploy; PART 3ak now proves the override
#               still works, not just the new default.
#   2026-08-31  APP_BUILD -> "2026-08-31qx-the-verb-is-the-operator". BUILD qx -- the
#               08-29 review's last two items, all in tutor.py: R7 (rule 15's referee
#               learns the COMMAND ASK -- "Simplify 8/12?" slipped in both word and
#               digit form because a command carries one number and no operator word;
#               the verb IS the operator; final-sentence scoped, net new canon hits
#               zero) and R8 (rule 64's measurement-only probe: the child's own
#               "3 + 2 x 4" silently worked as "2 + 3 x 4" now counts as
#               probe · expressionswap, "reordered" vs "replaced", so the next watch's
#               numbers decide whether a referee is worth its false-positive risk).
#               Plus PART 3gz's qask PAIRING pin: /api/script/quiz/* is pilot.html's
#               alone today and session.html's player has no qask beat -- the pin fails
#               the day one arrives without the other. NO CODE IN THIS FILE CHANGED.
#   2026-08-31  APP_BUILD -> "2026-08-31qw-the-floor-under-the-floor". BUILD qw -- the
#               buttons guarantee, in tutor.py: referee 58 could only nudge, so after
#               three failed attempts a bubble-less question still shipped to an
#               Entry-Level or Basic child who cannot type. CODE now repairs it at the
#               moment of shipping, on every exit of _create_verified: compute the
#               answer from the reply's own pending problem ("4 + 3 = ?", or "what is
#               four plus three?"), append the scripted lane's exact choices row.
#               COMPUTED, NEVER GUESSED -- what it cannot compute ships as before and
#               is COUNTED (pass_through · elembuttons; repairs are code_repair ·
#               elembuttons). NO CODE IN THIS FILE CHANGED.
#   2026-08-31  APP_BUILD -> "2026-08-31qv-the-words-point-at-the-picture-drawn". BUILD qv --
#               the night watch's three referee-shaped findings, measured first, closed
#               as REFEREE 67 (fraction anatomy in top/bottom words over a slash-written
#               fraction with no spoken bridge -- rule 63; notation.py's build-dk bridge
#               finally has teeth), REFEREE 68 (a second, different [[triangle]] with no
#               [[clear]] while the first stands -- rule 26; referee 56 only knew
#               numbered questions), and funcrule's NOT-NEW gate tightened to
#               NOT-YET-READ (the two-turn hole g(x)=3x-2 shipped through). All in
#               tutor.py. ⚠️ 67's canon sweep caught the basic/denominator and
#               basic/numerator cards themselves; both fixed in foundations.py to the
#               ps standard (two spoken lines changed -> two TTS clips re-render).
#               NO CODE IN THIS FILE CHANGED.
#   2026-08-31  APP_BUILD -> "2026-08-31qu-two-rows-from-the-night-watch". BUILD qu -- the
#               first healthy Anthropic-seat night watch (2026-08-31 08:46 UTC, run on
#               build qs -- which is also how we know qr and qs are LIVE) confirmed seven
#               findings; the two that are pure false WORDINGS land here as
#               KNOWN_FALSEHOODS rows in tutor.py: division described as splitting into
#               "smaller" groups with no condition, and the ÷ SIGN said to be read "two
#               divided by two" (the sign is read "divided by"; the EXPRESSION is read
#               with its numbers). No other file changed. The watch's remaining findings
#               are queued in the handoff: fractions top/bottom over an inline 1/4, the
#               unread g(x) rule, the missing [[clear]], answer-the-question-first, and
#               Jim's ruling that a unit-plan PREVIEW is exempt from first-use definitions.
#   2026-08-30  APP_BUILD -> "2026-08-30qt-the-counting-lessons-actually-count". BUILD qt --
#               the canon uses what qs built. NO PYTHON CHANGED ANYWHERE: thirteen authored
#               BOARD lines in foundations.py and lessonscripts.py gained count="1" -- the
#               cards where Mr. Cadabra counts the drawing himself, out loud, while he
#               models. Before this, only the AI intervention asked for the count-along, so
#               a child who never answered wrongly would never once have seen it, and the
#               COUNTING lessons of all lessons still drew every star in one instant.
#               ⚠️ Not one spoken line changed, so no TTS clip re-renders. PART 3gw pins the
#               thirteen, pins the ones deliberately left plain WITH their reasons, and --
#               the pin that matters -- re-checks board.js's three refusals against every
#               counted card, reading OBJ_COUNT_MAX out of board.js rather than restating
#               it: a card asking for a count-along the renderer refuses still LOOKS right
#               on screen, so that defect is invisible in a browser and permanent in source.
#   2026-08-30  APP_BUILD -> "2026-08-30qs-count-out-loud-with-me". BUILD qs -- the board
#               learns to count, and the 66th referee keeps the exception honest. NO PYTHON
#               IN THIS FILE CHANGED: the work is in static/board.js (the [[objects]] tag
#               takes count="1" and lands the things one at a time, each with its own ✓ and
#               number), static/voice.js (it announces "mt:speaking" so the shared board
#               layer can pace to his real voice without any page being touched), tutor.py
#               (referee 66 + the intervention's MODEL step) and prompts.py (the attribute,
#               its one ban, and the exception written into the law it excepts).
#   2026-08-30  APP_BUILD -> "2026-08-30qr-the-authored-question-ships-its-buttons". BUILD qr
#               -- Jim, on a live Entry-Level lesson: "these are all supposed to be bubble
#               answers, not tap to talk ... it's in a couple of these, but it's not on all
#               of them." NO PYTHON CHANGED. The server was never at fault, and the reading
#               that proves it is worth keeping:
#                 * lessonscripts.choices_for() builds a [[choices]] tag for EVERY scripted
#                   question, with no condition on it at all;
#                 * _script_clean() in THIS file sends it to the page as step.choices --
#                   a field of its OWN, beside step.board -- along with step.tap_only;
#                 * static/session.html's scrPlay() rendered step.board and nothing else.
#                   The string "step.choices" did not appear in that file.
#               So every AUTHORED question in Entry-Level and Basic reached the child with
#               no buttons, while an `ai` intervention had them (its tags ride INSIDE board,
#               split out of the model's reply by _split_ai_reply). That split is exactly
#               the "couple of these" Jim saw. static/pilot.html, the player this one was
#               ported from in build pb, has read step.choices since build ou; the port
#               dropped it, and dropped tap_only with it.
#               ⚠️ ONE SERVER BEHAVIOUR THE FIX NOW DEPENDS ON, so do not "tidy" it: the
#               unheard branch inside an intervention answers with a `say` beat whose BOARD
#               carries the redo's choices tag (LINE_TAP). The page renders that tag from
#               the board, must not draw a second row from step.choices, and must treat that
#               beat as pending -- its buttons ARE its question. All three handled in
#               session.html; ruletests PART 3gu pins every one of them and walks the entry
#               and basic lessons to prove the server ships a tag for every ask.
#   2026-08-30  APP_BUILD -> "2026-08-30qq-the-site-says-what-the-button-says". BUILD qq --
#               a sweep after qp, because renaming a button leaves fiction behind wherever
#               the site QUOTES that button. Three places, no Python touched:
#                 * static/family.html -- the parent's list of children had its own
#                   "💬 How are they doing?" link, ONE PER CHILD ROW, with the child's name
#                   already in data-name two inches to the left. Now "💬 How is Maya doing?".
#                   (Its assessment call was already right: it has resolved the child's
#                   most-worked course from the overview since it shipped, which is exactly
#                   the fix build qn had to make on the dashboard.)
#                 * static/landing.html -- the "Reports written for parents" card quoted the
#                   old wording to prospective customers.
#                 * static/llms.txt -- the machine-readable site summary quoted it too.
#               ALSO CHECKED AND ALREADY CORRECT, so deliberately untouched: static/demo.html
#               is a hand-written mirror of all three dashboards and was ALREADY in the voice
#               qn-qp introduced ("How is she doing, really?", "Her learning journey", "Her
#               nine Pre-Algebra units") and has no sprint card; static/teacher.html is the
#               CLASS ROSTER, not a per-child dashboard -- it links out to
#               /dashboard?...&view=teacher, so it inherited qn-qp with nothing to change.
#   2026-08-30  APP_BUILD -> "2026-08-30qp-one-page-one-child". BUILD qp -- Jim, on the live
#               parent view: "this should not say 'How are THEY doing, really?' -- it is just
#               for a single child ... Also, the paragraph says 'they' instead of 'your
#               child'." Three fixes, in the three places they actually live:
#                 * THE BUTTON (static/dashboard.html) asks about one child, and a TEACHER --
#                   who has many students and is not their parent -- gets its own words.
#                 * THE PARAGRAPH is written by the model, so prompts.py's parent voice now
#                   forbids the plural pronoun outright: the name, or "your child", never
#                   "they". The child's pronouns are not in the data and are never guessed.
#                 * ⚠️ AND A FALSE NUMBER WAS FOUND IN THAT PARAGRAPH while reading it. It
#                   claimed "206 real working minutes across 25 ACTIVE DAYS" over a 14-day
#                   window -- impossible on its face, on a page that tells parents every
#                   number is recorded and never estimated. _assessment_facts counted ROWS,
#                   and a row is (day, COURSE), so three courses in one afternoon read as
#                   three days; and store.get_time() has no date filter at all -- it returns
#                   the newest days*12 ROWS, so the sum could reach back months. Now uses
#                   store.get_time_between() (a real ISO window, the reader the printed
#                   records already use) and counts DISTINCT days. No other caller was
#                   affected: /api/time aggregates per day and slices, so the dashboard tile
#                   was always right.
#   2026-08-30  APP_BUILD -> "2026-08-30qo-every-course-he-is-actually-in". BUILD qo -- Jim,
#               still reading the demo student's page as a parent, on build qn: "I'm not sure
#               if we're talking geometry or algebra when I look at the strengthen next and
#               the learning journey. What course is that for? ... THE STUDENT IS WORKING ON
#               A COUPLE OF DIFFERENT COURSES. So we would have to have a couple of courses
#               here -- demo student's nine geometry units, here's where they are; demo
#               student's nine algebra units, this is where we are at. Not for all of them,
#               but just the ones he's been working on." And: "this sprint record takes up a
#               huge amount of space for just a little data point."
#               static/dashboard.html only (again NO endpoint changed):
#                 * THE JOURNEY IS ONE TITLED BLOCK PER COURSE the child has really worked
#                   in -- /api/courses/me names them, /api/topics is fetched per course, and
#                   each block carries its own track and unit cards under a heading that says
#                   whose and which. Courses never opened are not drawn.
#                 * "STRENGTHEN NEXT" SPANS THOSE COURSES with the course named on every row,
#                   taken round-robin so one course's untested units cannot fill the list and
#                   hide the others -- the very thing being complained about.
#                 * THE SPRINT CARD IS REMOVED from this page (Jim's ruling). Sprints still
#                   record, still print on the records page, and are still offered inside the
#                   lesson, which was always the main door; features.html and students.html
#                   no longer tell people to start one "from your dashboard".
#   2026-08-30  APP_BUILD -> "2026-08-30qn-the-parent-reads-the-right-course". BUILD qn --
#               Jim read the demo student's progress page AS A PARENT and could not
#               understand it: "how are they doing... only talks about the algebra course,
#               not the current course they're working on"; "it says my courses, and this is
#               the parents"; "if I did a little bit of geometry... it should have some way
#               of indicating that I'm there"; "the parents should be able to go to the site
#               and see everything and understand everything."
#               The whole fix is in static/dashboard.html -- NO ENDPOINT CHANGED, because
#               every number needed was already in the payloads and was being thrown away:
#                 * THE COURSE. The parent's door (/dashboard?code=..&view=parent) carries no
#                   &course=, so the page's `params.get("course") || "algebra1"` pinned every
#                   parent to Algebra I forever. /api/courses/me already returns last_active
#                   per course; when no course is named the page now lands on the one the
#                   child most recently worked in. An explicit ?course= still wins, so the
#                   "My courses" switcher is untouched.
#                 * THE VOICE. One owner()/subj() helper drives every heading, so "Your
#                   learning journey" reads "Emma's learning journey" for a grown-up and the
#                   two voices cannot drift apart again.
#                 * A TOE IN THE WATER SHOWS. The course strip's bar was units_mastered only;
#                   units_started (already in the payload) now draws a pale second segment so
#                   a started-but-not-mastered course stops looking untouched.
#                 * WHICH NUMBERS COUNT WHAT. store.get_mastery's own docstring calls its
#                   stats "whole-student": streak, accuracy, problems practiced and minutes
#                   span EVERY course while "Units mastered" spans one. Each tile now says
#                   so. No number moved -- they were always this; nothing said it.
#   2026-08-30  APP_BUILD -> "2026-08-30qm-a-verdict-every-time". BUILD qm -- one live
#               Geometry session, two flags. tutor.py: the 65th referee makes rule 47(i)
#               real -- no quiz question moves to the next without grading the last.
#               session.html: the Today progress bar is hidden (it was the only one that
#               depended on the tutor remembering to emit [[todaydone]], and it read as
#               broken), today leads in words, and the chip carries the unit's count.
#               No Python changed here except this stamp.
#   2026-08-30  APP_BUILD -> "2026-08-30ql-the-page-tells-the-truth". BUILD ql -- Jim ended
#               the DeepSeek trial. privacy.html goes back to naming THREE processors (it
#               named a fourth for one day, for a seat that never carried a single child's
#               turn), landing.html says Claude again, and render.yaml's blueprint seat is
#               anthropic. The seat machinery, the failover, seat-check and the watch's
#               failopen reasons all STAY -- they are vendor-neutral and they were the
#               real yield of the trial. No Python changed here except this stamp.
#   2026-08-30  APP_BUILD -> "2026-08-30qk-working-is-not-usable". BUILD qk -- qj's
#               real-size button answered in 21.9s: the DeepSeek seat WORKS on a full
#               teaching turn (which clears the outage of every remaining suspect), and
#               is nearly double Sonnet's 12.3s teaching call, which a refereed turn can
#               spend three times. seat-check now reports tokens (a second press shows
#               whether the 46k prefix cached), and says outright when a seat that
#               answers is still too slow to teach.
#   2026-08-30  APP_BUILD -> "2026-08-30qj-the-size-of-a-real-turn". BUILD qj -- qi's
#               seat probe told Jim "this seat works" on the morning after 120 real
#               turns had failed, because it sent a fifteen-token prompt where a lesson
#               sends ~46,000. seat-check gains ?size=lesson: the actual
#               build_system_prompt, the actual cached-block shape, the actual
#               3000-token ceiling. A passing SMALL test now says outright that it
#               proves nothing about a teaching turn. admin.html gets both buttons.
#   2026-08-30  APP_BUILD -> "2026-08-30qi-reached-or-refused". BUILD qi -- /api/admin/
#               seat-check grows ?provider=&model=&effort=, so DeepSeek can be tested
#               while production keeps teaching on Anthropic, and reports `reached` --
#               whether the request ever got to the vendor at all -- as its headline
#               fact. admin.html gains the Brain seat card with a button per seat.
#   2026-08-30  APP_BUILD -> "2026-08-30qh-hands-the-class-back". BUILD qh -- from the
#               first night on the DeepSeek seat (120 apologies). tutor.py fails OVER to
#               Anthropic instead of failing open; nightwatch.py finally prints the
#               failopen reasons it was counting. Here: NEW /api/admin/seat-check, one
#               cheap call to the configured seat that returns the vendor's own error
#               and a remedy -- so a seat can be tested before a child pays for it.
#   2026-08-29  APP_BUILD -> "2026-08-29qg-the-deepseek-brain". BUILD qg -- Jim's ruling:
#               DeepSeek replaces the Anthropic brain (TUTOR_PROVIDER=deepseek on Render).
#               tutor.py holds the seat and its privacy gate; static/privacy.html names
#               DeepSeek (and where its data goes); render.yaml documents the env. Here:
#               /health and /admin report tutor.active_brain() -- the seat actually
#               teaching -- instead of the CLAUDE_MODEL default.
#   2026-08-29  APP_BUILD -> "2026-08-29qf-one-thought-per-line". BUILD qf -- Jim's two
#               Algebra I screenshots: (tutor.py) the 64th referee rejects a board line
#               that finishes one equation and starts another; (foundations.py) four
#               authored cards that did exactly that are split, one thought per line;
#               (board.js) an operation on an expression is shown once, not under two
#               sides. No Python changed here except this stamp.
#   2026-08-29  APP_BUILD -> "2026-08-29qe-say-the-course-name". BUILD qe -- speech-text.js
#               only: forSpeech reads "Algebra I" as "Algebra One" and "Algebra II" as
#               "Algebra Two" (Jim: "Algebra I is being pronounced Algebra Eye"). No
#               Python changed except this stamp.
#   2026-08-29  APP_BUILD -> "2026-08-29qd-the-problem-that-was-asked". BUILD qd -- from
#               Jim's three screenshots: (tutor.py) the scripted-lane intervention
#               describes the missed problem with the engine's own words, board,
#               answer and explanation instead of reducing it to a + b, and stars are
#               scoped to plain adding/taking away; (session.html) an "ai" step counts
#               as an ask, so the redo is graded by code here instead of drifting to
#               the live tutor with stale history. No Python changed here except this
#               stamp.
#   2026-08-29  APP_BUILD -> "2026-08-29qc-the-bars-are-on-the-board". BUILD qc --
#               lessonscripts.py only: the Algebra II opener draws the absolute-value
#               bars it talks about. From Jim's screenshot. No Python changed here
#               except this stamp.
#   2026-08-29  APP_BUILD -> "2026-08-29qb-the-check-that-can-be-failed". BUILD qb --
#               tutor.py: a bare "make sense?" ending is rewritten to rule 39(d)'s
#               failable form with its buttons; numeric either-ors get their numbers as
#               buttons. Canon 0. No Python changed here except this stamp.
#   2026-08-29  APP_BUILD -> "2026-08-29qa-one-entry-per-function-letter". BUILD qa --
#               tutor.py: the notation referee (rule 14/48) treats f, g and h as
#               separate first uses and sees numeric arguments, so "g(2) = 8" after
#               f(x) is read aloud. No Python changed here except this stamp.
#   2026-08-29  APP_BUILD -> "2026-08-29pz-the-named-list-of-falsehoods". BUILD pz --
#               tutor.py: the 63rd referee, a table of named false general statements
#               (three from the 2026-08-29 watch, ten from PART 3w) with the true form
#               in every nudge. Canon swept 0. No Python changed here except this stamp.
#   2026-08-29  APP_BUILD -> "2026-08-29py-the-plain-yes-no-gets-its-buttons". BUILD py --
#               tutor.py + prompts.py: rule 39(e)'s referee learns the general yes/no
#               shape (final sentence opens with an auxiliary, no "or"), so "Does that
#               make sense?" ships Yes | Not yet and "Is 7 prime?" ships Yes | No.
#               Canon swept 0. No Python changed here except this stamp.
#   2026-08-29  APP_BUILD -> "2026-08-29px-ship-the-best-draft". BUILD px -- three
#               fixes from the 2026-08-29 night watch, none in this file. tutor.py: the
#               critic's verdict is read with raw_decode (the "Extra data" crashes the
#               watch finally named), and when the attempts run out the LEAST-BAD draft
#               ships instead of the last one. tutor.py + nightwatch.py: the
#               reviewer's conduct list is generated from the rule registry (five
#               findings went unjudged for citing rules 28/47/61/63). No Python changed
#               here except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pw-a-different-problem-is-not-a-snapshot". BUILD pw --
#               board.js only: supersedePrevious now COMPARES first lines, so a
#               different problem is no longer folded away as a stale snapshot of the
#               current one. From Jim's order-of-operations screenshot. No Python
#               changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pv-one-character-three-failures". BUILD pv --
#               Jim's Geometry screenshot, three bugs. NEW _split_ai_reply(): the AI
#               intervention step returned the model's WHOLE reply in `spoken` with an
#               empty `board`, so its [[step]] and [[choices]] tags were PRINTED TO THE
#               CHILD as literal text. Every other step kind in this lane splits prose
#               from tags; the AI step now does too, at BOTH return sites. The other
#               two fixes are in lessonscripts.py (the hyphen) and tutor.py (the
#               operator).
#   2026-08-28  APP_BUILD -> "2026-08-28pu-fit-the-turn-to-the-board". BUILD pu --
#               board.js grows fitTurnToBoard(): a turn whose figures make it taller
#               than the board is shrunk to fit before the anchor runs, so the picture
#               the words point at stays on screen. Measured, not reasoned. Partial by
#               its own admission -- see PART 3fy. No Python changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pt-the-child-cannot-be-right". BUILD pt --
#               three referees from Jim's flag queue (60/61/62). The worst: tap buttons
#               that do not contain the answer, so every tap is marked wrong. All 59
#               earlier referees were silent on it. No teaching content changed; one
#               HOW YOU SPEAK clause added in all eleven copies.
#   2026-08-28  APP_BUILD -> "2026-08-28ps-the-hole-that-always-appears". BUILD ps --
#               rule 61's second enforced slice (referee 59): a hole/cancelling law
#               spoken unconditionally. The canon sweep fired on our own calculus
#               foundation card, which is corrected in the same build. ONE authored
#               spoken line changed -- one TTS cache key needs rendering.
#   2026-08-28  APP_BUILD -> "2026-08-28pr-a-fragment-of-an-unspoken-whole". BUILD pr
#               -- rule 44 gains an eye for a pending question that is only a FRAGMENT
#               of a board problem nobody read aloud. Measured first: all five of the
#               night watch's referee-backed findings were HOLES, not pass-throughs.
#               Two repairs cut by canon sweep. No teaching content changed.
#   2026-08-28  APP_BUILD -> "2026-08-28pq-the-eyes-report-what-they-saw". BUILD pq --
#               the 2026-08-28 night watch, worked. Rule 42's referee widened (canon
#               swept; two additions CUT). The watch now reports crash REASONS, not
#               just counts, and separates findings the reviewer could not judge from
#               findings it refuted. No teaching content changed.
#   2026-08-28  APP_BUILD -> "2026-08-28pp-the-curriculum-is-read". BUILD pp -- the
#               last two courses. All 36 Prob & Stat and all 36 Diffeq lessons read;
#               both courses' prose clean, 48 worked examples now show their
#               operation. ⭐ ALL TEN COURSES, ALL 360 LESSONS, READ FOR SENSE.
#               No Python changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28po-calculus-read-for-sense". BUILD po -- all
#               36 Calculus lessons read; prose clean, 22 second worked examples now
#               show their operation. Eight courses read, 288 of 360 lessons. No
#               Python changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pn-precalc-read-for-sense". BUILD pn -- all 36
#               Pre-Calculus lessons read; the first course with NO prose defects at
#               all. Sixteen second worked examples now show their operation. No
#               Python changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pm-algebra-two-read-for-sense". BUILD pm --
#               all 36 Algebra II lessons read; the course that started this thread
#               now reads well. Ten changes, one of them internal shorthand spoken to
#               a child ("pyth's"), the only instance in 360 lessons. No Python
#               changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pl-geometry-read-for-sense". BUILD pl -- all
#               36 Geometry lessons read line by line; seven second worked examples
#               stated the answer where the first stated the operation. Five of the
#               seven were invisible to the word-count sweep. No Python changed
#               except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pk-algebra-one-read-for-sense". BUILD pk --
#               all 36 Algebra I lessons read line by line; four changes, plus the
#               Pre-Calc radians fragment pj flagged. The four foundation courses
#               (Entry, Basic, Pre-Algebra, Algebra I) have now all been read.
#               No Python changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pj-prealgebra-read-for-sense". BUILD pj --
#               all 35 Pre-Algebra lessons read line by line. It is the strongest
#               course in the product; seven changes across five lessons. No Python
#               changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pi-the-second-example-teaches-too". BUILD pi
#               -- Basic read line by line. The course is sound; eleven second worked
#               examples had collapsed to the bare answer and now show their working.
#               No Python changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28ph-the-curriculum-is-whole". BUILD ph -- the
#               last eight authored lessons. All ten courses are nine units of four,
#               360 lessons, and the authored lane covers every topic in the
#               curriculum. No Python changed except this stamp.
#   2026-08-28  APP_BUILD -> "2026-08-28pg-entry-fills-its-units". BUILD pg -- Jim:
#               "go and create the authored lessons as well." Entry goes 20 -> 36
#               lessons, nine units of four, so no five-year-old falls through to the
#               live lane any more. 352 authored lessons in the curriculum now. No
#               Python changed except this stamp; the work is in lessonscripts.py and
#               the regenerated quizsets.py.
#   2026-08-27  APP_BUILD -> "2026-08-27pf-the-first-course-read-for-sense". BUILD pf
#               -- Jim: "Start at the beginning." All 20 Entry lessons read line by
#               line. Entry turned out to be SOUND: eight lines across six lessons
#               changed, one of them a statement that was simply false ("17 take away
#               9 equals 8 cubes longer"). No Python changed except this stamp.
#   2026-08-27  APP_BUILD -> "2026-08-27pe-the-sentences-make-sense". BUILD pe -- the
#               third of Jim's three complaints, the one pd left open: "the text
#               itself is as if someone is teaching math in a non-native language."
#               I first blamed the VOCABULARY canon (it forces "take away" on all 336
#               lessons and bans "subtract", so a five-year-old's wording governs
#               Differential Equations) and proposed a 3,220-line swap. He overruled
#               it: "Takeaway or minus, those were just as well. It's just when you
#               put it in the whole context of those sentences, it just didn't make
#               sense." Measurable is not causal. No Python changed except this stamp;
#               the work is in lessonscripts.py. Proof: PART 3fi, plus validate()
#               running 35,526 checks across all 336 lessons with zero failures.
#   2026-08-27  APP_BUILD -> "2026-08-27pd-let-the-lesson-breathe". BUILD pd -- Jim:
#               "This is the worst lesson I have seen so far. There was no pause at
#               any time. pictures showed up and disappeared." One bug, two symptoms,
#               and it was mine: build pb's scripted player advanced on `else
#               scrNext();` -- the instant speak() RESOLVED. A missing or blocked clip
#               resolves in milliseconds, so the whole lesson landed in one frame and
#               oz's supersede chip ate the earlier pictures on the way past. pb had
#               hand-ported the player out of pilot.html and left behind all THREE
#               protections that page grew over builds ka/kd/ke: the reading floor,
#               the breath between beats, and "a silent beat waits for the child".
#               All three are restored, using session.html's OWN readMs (the tour has
#               used it since bj) rather than a second copy. The fix's first cut then
#               served the floor on ASK beats too and left the tap buttons live-looking
#               and inert for 2.6s -- the pb drive caught it inside the hour, and build
#               nb's law settles it: a child who can hear the question must never be
#               locked out of answering while it finishes. No Python changed except
#               this stamp. Proof: /tmp/pddrive.py (14 assertions, silent AND voiced)
#               plus all nine earlier drives re-run green.
#   2026-08-27  APP_BUILD -> "2026-08-27pc-the-figure-fills-the-board". BUILD pc --
#               Jim, on a live Algebra II absolute-value beat: "Why is it so hard to
#               make a big number line". It was not hard. It had been MEASURED WRONG
#               for three builds. session.html's .feed .mblock is a flex COLUMN with
#               align-items:center, so every child is sized by its own content -- and
#               a figure block's only content is an <svg> whose CSS width is a
#               PERCENTAGE. A percentage contributes nothing to intrinsic sizing, so
#               the browser used the CSS default width for a replaced element, 300px,
#               and then applied max-width to a box that was already 300px. EVERY
#               figure on the board rendered at exactly 300px on every screen. The
#               three builds that answered "make it bigger" by raising the display
#               cap (je 660 -> nw 1100 -> ox 1500) were raising a ceiling the floor
#               could never reach. One CSS line -- .feed .mfig { align-self: stretch }
#               -- opts the figure out of the centering and gives the percentage a
#               real box. Measured on a real render: the number line goes 300px ->
#               936px at a 1512px window, 1218px at 1920px. With the cap finally
#               real, math-figures.js and geo-figures.js got a matching FLOOR (the
#               width that puts a drawing about 420px tall at its own aspect ratio,
#               ceiling 1100, applied with Math.max so nothing shrinks): geometry
#               goes 300 -> ~520px, the [[segment]] line to ~940px. No Python
#               changed except this stamp. Proof: /tmp/pcdrive.py, plus all eight
#               earlier drives re-run green.
#   2026-08-27  APP_BUILD -> "2026-08-27pb-the-classroom-gets-fast". BUILD pb --
#               THE CORRECTION, and the mistake is worth recording. Build pa read
#               Jim's "open the gate so that every lesson at every course is fast"
#               as "send every course to the scripted PAGE". He put me straight at
#               once: "I want a student to have the original layout with the
#               whiteboard, with all of the stuff... I just want those answers to
#               be fast. I don't know why we have to do a whole new layout to make
#               that happen." He was right -- speed was never a reason to move a
#               child into a different room.
#               pa's home change is REVERTED: the course door is the classroom.
#               The authored lessons now play INSIDE session.html, through its own
#               addBubble, its own board, its own choices row, voice, sidebar and
#               bars. The room is untouched; a scripted beat simply costs ZERO
#               model calls, so the next thing he says is already written and
#               recorded before the child answers.
#               NOTHING IS LOST: a unit with no script opens the live way exactly
#               as before, an off-script question goes to the raised hand, a
#               network failure hands the turn to the live tutor, and when the
#               script runs out the live tutor takes the same session over with no
#               seam. Front-end only; this file carries the stamp. PART 3ff
#               rewritten; the op/oq/pa door pins reconciled.
#   2026-08-27  APP_BUILD -> "2026-08-27pa-the-gate-is-open". BUILD pa -- THE FLIP.
#               Jim, with the whole stack deployed and the course audio rendered:
#               "open the gate so that every lesson at every course is fast."
#               The authored lane stops being a pilot. EVERY course's lessons door
#               now opens on it -- all ten, 336 lessons, every word pre-written,
#               pre-checked and pre-voiced, so a beat starts the moment the child
#               taps instead of waiting on a model.
#               ⭐ THE LIVE LANE IS RE-AIMED, NOT RETIRED. It keeps every job the
#               script cannot do -- a problem the child brings in, a topic they
#               want to explore, a question the author never wrote -- and Entry and
#               Basic still have ladder topics with no script at all. It sits
#               beside the lessons tile as "Teach me something else". Retiring it
#               would strand a child on the first off-script question.
#               The lesson room also stops calling itself a pilot in front of
#               children, and its exit lands on the course hub it came from.
#               Front-end only; this file carries the stamp. PART 3ff, and TWO
#               EARLIER PINS OVERTURNED (prealgebra-only, and "never a replacement
#               until it earns it") -- recorded in place, not deleted.
#   2026-08-27  APP_BUILD -> "2026-08-27oz-the-board-uses-the-room". BUILD oz --
#               Jim, for the third time, with a screenshot: "it's still not using
#               the full screen ... answer something and move over to the side of
#               the whiteboard ... nothing has changed. We're just marching
#               straight down." THIS TIME I MEASURED IT instead of reasoning: his
#               board was 1,732px wide with the maths in a 560px column down the
#               middle (two thirds of the whiteboard empty) and 1,593px of scroll
#               for ONE problem. Four changes, all front-end:
#                 (1) THE FEED IS TWO COLUMNS -- his words left, the work they
#                     drew right, paired on one row by grid auto-placement. No
#                     wrapper element, so the fold/scroll/flag machinery walks the
#                     same DOM. Unlisted children default to FULL WIDTH (the first
#                     version squeezed [[stepcard]] rows into the 32% column).
#                 (2) THE WORKLIST FLOWS ACROSS -- rows fill a column then continue
#                     in the next one to the right; an op and its result never split.
#                 (3) THE RE-STATED SNAPSHOT SUPERSEDES THE OLD ONE. Rule 35 makes
#                     him re-state the whole equation every turn, so six turns
#                     stacked six near-identical boards. Earlier snapshots collapse
#                     behind ONE quiet chip. Figures never collapse.
#                 (4) THE CHECK LINE'S "|" IS GONE -- two sides, real space, a soft
#                     divider. Its spacing is INLINE because session.html does not
#                     load board.css at all (the first version fixed only the pilot
#                     page and rendered "= 115 + 6", worse than the bar).
#               Measured after: one problem now fits on ONE screen. This file
#               carries the stamp only. PART 3fe.
#   2026-08-27  APP_BUILD -> "2026-08-27oy-the-day-you-can-feel". BUILD oy -- Jim:
#               "the progress bar for the daily progress needs to be more specific
#               ... as we go lesson by lesson by lesson we should see progress
#               being attained, not just in big chunks ... so I feel like I'm
#               getting something done." Two different faults, two answers, both
#               lanes: (1) the bar never SAID what today was -- both lanes now name
#               the work in words (what is being worked on now, what is still to
#               come); (2) a goal was all-or-nothing -- segments now FILL as work
#               happens, driven by [[nice]] and [[mark]], the two signals the tutor
#               already sends. The fast lane gains a day strip: one segment per
#               lesson, the current one filling as answers land.
#               ⭐ THE HONESTY RULE: partial fill NEVER reaches 100. Only a real
#               [[todaydone]] tick, or the lesson's own end beat, completes a
#               segment -- the bar may encourage, it may never claim work that did
#               not happen. Front-end only; this file carries the stamp.
#               PART 3fd; the oy drive proves both lanes.
#   2026-08-27  APP_BUILD -> "2026-08-27ox-the-seventh-flag-harvest". BUILD ox --
#               seven live flags, three of them the SAME defect flagged three
#               times in three minutes. NEW REFEREES 56/57/58, each swept against
#               all 1,989 authored cards before enforcing: 56 a new numbered
#               question asked over the previous answer's board (rule 47l, the
#               triple flag -- "very misleading"); 57 a spoken colon pointing at a
#               stripped board tag (48d3, "that's:" is silence in the ear); 58 an
#               open question with no taps in a course answered by TAPPING (39f,
#               course-gated to entry/basic -- "this level of math is supposed to
#               be all bubbles"), which also CLOSED the "genuinely open-ended"
#               loophole that was doing the damage. NEW [[segment]] figure (five
#               midpoint questions were asked with nothing drawn). Number line cap
#               1100 -> 1500 with bigger marks. THIS FILE'S OWN CHANGE: the
#               SESSION LENGTH note -- Jim's "don't ask me every 2 minutes if I
#               want to stop" is a thing no prompt rule can fix, because the model
#               has no clock; the server now states the turn count and the ruling,
#               riding the turn note so the cached prefix never moves.
#               PROMPT_CEILING 203,000 -> 205,000, twelfth dated verse.
#   2026-08-27  APP_BUILD -> "2026-08-27ow-use-the-whole-board". BUILD ow -- THE
#               FIFTY-FIFTH REFEREE. Jim, live in geometry: "the screen is still
#               not using the full screen... it's not saying step one, step two,
#               step three." NOT A DEPLOY GAP -- /health reported
#               2026-08-27ot, so [[stepcard]] was live and the model simply did
#               not reach for it, which is what earns a referee here.
#               tutor.spoken_steps_conflict fires when the tutor SAYS two or more
#               numbered stages with no [[stepcard]] on the board; rule 58(e)
#               gains the matching HARD clause plus the [[beside]] width
#               reminder. A looser second arm was written, swept against all
#               1,989 authored cards, and CUT (eleven false positives -- "first
#               ones, then tens, then hundreds"). PROMPT_CEILING 201,000 ->
#               203,000, eleventh dated verse. This file carries the stamp only.
#   2026-08-27  APP_BUILD -> "2026-08-27ov-quizzes-through-the-spine". BUILD ov --
#               STEP 2 OF JIM'S FLIP. A child on the fast lane finished a topic
#               and hit a WALL: topic quizzes existed only in the live lane. Now
#               every one of the 336 authored lessons ends in a five-question
#               quiz. NEW /api/script/quiz/start + /answer; the questions are
#               PINNED DATA (quizsets.py, generated once) because the audio
#               closure has to enumerate every sentence a quiz can speak;
#               grading is code; recording goes through the SAME
#               store.record_topic_quiz the live lane uses, at the same 80% bar.
#               NOTHING IN A QUIZ THINKS -- there is no model call on either
#               route -- and the ✋ is hidden for the duration, because a score
#               earned with help is not a score. The score is DRAWN on the board,
#               never spoken, which keeps the closure at seven quiz lines.
#               Quizzes add ~1,337 lines to the audio closure (~$30 one-time
#               across all ten courses). PART 3fa; the ov drive proves the page.
#               ⚠️ TWO REAL BUGS THE DRIVE CAUGHT: the ✋ was still up during a
#               quiz's own say beats, and a PASS re-offered the same quiz while a
#               FAIL offered no retake -- exactly backwards.
#   2026-08-27  APP_BUILD -> "2026-08-27ou-answer-freely". BUILD ou -- STEP 1 OF
#               JIM'S FLIP ("go ahead and preload it... are you thinking of making
#               this a permanent option?"). The scripted lane was TAP-ONLY, which
#               cannot be the main road. /api/script/answer now also accepts
#               `said` -- what the child typed, or what mic.js transcribed -- and
#               lessonscripts.read_answer turns it into the same integer a tap
#               sends. ⭐ CODE READS IT, NEVER THE MODEL: the lane's whole speed
#               case is that nothing thinks between the child and the next
#               sentence. The parser REFUSES rather than guesses (a fraction, a
#               spoken decimal, or garbage gets an authored line and the existing
#               unheard re-ask), because reading "three point five" as 3 would
#               grade a wrong answer correct. A tap still sends a bare `value`, so
#               the old request is byte-for-byte unchanged. numwords.py is new:
#               one copy of the number-word table, shared with tutor.py's
#               referees. PART 3ez; the pilot drive proves the page.
#   2026-08-27  APP_BUILD -> "2026-08-27ot-the-figure-shelf". BUILDS or + os + ot
#               (Jim's walk-away list, all front-end -- no route or API changed
#               here; this note is the build stamp plus the map).
#               or -- THE PAGE GETS SIMPLE (session.html + ordrive): the sidebar
#               starts COLLAPSED behind an "Open the sidebar" edge tab; the face
#               and the mic/Pause/Type controls move to a compact strip at the
#               bottom of the board column (JS reparent, same ids -- phones keep
#               dz's dock). The top progress chips are UNTOUCHED (Jim retracted
#               that part himself: "let's leave that alone").
#               os -- THE BOARD READS ONE, TWO, THREE (board.js + the three
#               transcript pages + script-board.js + rule 58e + tags.py +
#               stepdrive): NEW [[stepcard n= title=]] tag -- labeled Step-N
#               cards side by side filling the board; blocks after a stepcard
#               land inside it until the next one or turn end.
#               ot -- THE FIGURE SHELF GROWS (geo-figures.js, math-figures.js,
#               tags.py, prompts.py per-course docs + figdrive): transversal
#               (the crossed parallel-lines picture), polygon, solid, venn,
#               tape, clock, and numberline hops=.
#   2026-08-27  APP_BUILD -> "2026-08-27oq-the-raised-hand". BUILD oq -- Jim's
#               expansion order ("I'm satisfied with unit one. Start expanding").
#               (1) NEW POST /api/script/ask: a child mid-script types a
#               question, gets ONE bounded spoken answer (tutor.script_question,
#               full referee pipeline, pending answers fenced, tags stripped);
#               five per lesson then an authored hold line; rate-limited; every
#               failure plays an authored fallback -- the door can never stall a
#               lesson. (2) home's prealgebra tile widens to the WHOLE course.
#               pilot.html gains the ✋ and the quiet resume.
#   2026-08-27  APP_BUILD -> "2026-08-27op-the-authored-spine-pilot". BUILD op --
#               Phase 3's pilot, on Jim's "go". Pre-Algebra Unit 1 is served from
#               the AUTHORED lane beside the live one: NEW /pilot route; home's
#               prealgebra hub grows the "Unit 1 -- the fast lessons" tile
#               (classic tile untouched -- the lanes sit side by side);
#               pilot.html gains the ?course=&unit= lens, the owner's 🚩, and a
#               way home; store.usage_stats counts the lane (script_turns /
#               ms_script_median / script_ai_turns) and the admin Cost card
#               shows it next to the live median. No serve-path change to the
#               live lane anywhere.
#   2026-08-27  APP_BUILD -> "2026-08-27oo-the-giveaways-are-closed". BUILD oo --
#               the ms hand-tail: 41 answer-giveaway hits closed (5 problems
#               renumbered, 26 bank removals across 18 lessons, one ask rotated,
#               one story renumbered with its sentence); teachaudit + workedaudit
#               now RUN IN THE BATTERY (PART 3ev) against an exact two-lesson
#               allowlist. lessonscripts.py/ruletests.py; only this stamp here.
#   2026-08-27  APP_BUILD -> "2026-08-27on-the-canon-held-to-its-own-standard".
#               BUILD on -- Phase 1 overnight: all 1,989 authored cards held to
#               the full 54-referee standard for the first time (421 findings ->
#               0): 132 arrow board lines split, 249 figures captioned, question
#               rows recaptioned, two promised pictures drawn, two piece->angle
#               spoken lines, two referee bugs fixed (percentile exemption,
#               chained equality), angle-piece narrowed. lessonscripts.py/
#               tutor.py/ruletests.py (PART 3eu pins zero); only this stamp here.
#   2026-08-27  APP_BUILD -> "2026-08-27om-skip-the-introduction". BUILD om --
#               Jim: "The introduction to Abrabot should have a skip introduction
#               button." _drill_intro_steps marks its steps intro: True and
#               _drill_clean lets the mark ride to the page; drill.html shows
#               "⏭ Skip the intro" on marked steps -- click silences the clip and
#               drops the remaining marked run. Only the server's own mark is
#               skippable, so the button can never eat teaching.
#   2026-08-26  APP_BUILD -> "2026-08-26ol-the-sixth-flag-harvest". BUILD ol --
#               six probstat flags: named-binary quiz questions ship buttons
#               (Jim's ruling); "or want another" + clause forks; "Question 3:
#               20" clock-time collision (referee 54 + 48(d2)); bar chart 400 ->
#               720; AND the sign-in fast-forward: this file's opener branch now
#               appends a DANGLING-ANSWER note when stored history ends on an
#               unanswered student turn, and sets student_context["opener"] so
#               referee 53 (an opener never grades) can see the door. Also
#               store.py: the 16-char verify_status truncation hid every
#               shipped-critic reply from the admin tiles ("0 live critic" while
#               14 sat uncounted) -- normalized on read.
#   2026-08-26  APP_BUILD -> "2026-08-26ok-grade-what-they-said". BUILD ok --
#               Jim's probstat screenshot: "Spring" answered, "Pie chart --
#               correct! That's question 1 done" replied. tapped_answer widened
#               to word taps when the reply grades; NEW referee 52 rejects
#               invented quiz credit; 18(c)/47(k) carry the law (tutor.py/
#               prompts.py/ruletests.py); only this stamp here.
#   2026-08-26  APP_BUILD -> "2026-08-26oj-side-by-side-on-purpose". BUILD oj --
#               Jim: "the whiteboard is underutilized." Bubbles 80% -> 96% and
#               the NEW [[beside]] board tag (next block lands NEXT TO the
#               previous one; phones stack). board.js/session/practice/topic +
#               prompts.py rule 58(d) + one leak-shape word in tutor.py; only
#               this stamp here.
#   2026-08-26  APP_BUILD -> "2026-08-26oi-the-fifth-flag-harvest". BUILD oi --
#               five geometry flags: referee 42 learns the LEADING fork ("Want X,
#               or Y?" ships buttons); NEW referees 50 (the board does the
#               drawing -- "grab your paper" with an empty board is rejected) and
#               51 (a vertical-angles question gets its X), both heard-gated;
#               geo-figures.js [[angle]] grows cross="?"; prompts.py rewrites the
#               sketch-along clause board-first, adds the rule-37 recap gloss and
#               names the leading fork in 39(e). tutor.py/prompts.py/
#               geo-figures.js; only this stamp here.
#   2026-08-26  APP_BUILD -> "2026-08-26oh-the-fourth-flag-harvest". BUILD oh --
#               five algebra2 flags: leak referee learns the referees' own nudge
#               jargon; referee 42 learns the bare final ready-check; the a2 u1
#               playbook gets the full absolute-value arc (pedagogy.py); the
#               small-numberline flag was a stale browser cache (1100px verified
#               live). tutor.py/pedagogy.py; only this stamp here.
#   2026-08-26  APP_BUILD -> "2026-08-26og-the-starting-blocks". BUILD og --
#               JIM'S SPECULATION, V1. A turn ending in a computable pending line
#               ("3 + 8 = ?") arms a background thread that generates the RIGHT-
#               answer follow-up through the FULL verified pipeline; a matching
#               next answer ships it instantly (zero model calls on the clock),
#               any mismatch falls through to the untouched live path. Right-
#               answer-only by Jim's ruling (the wrong branch cannot be pre-built
#               honestly, rule 49). Quiz/check/exam and result-recording turns
#               never speculate. Probes spec_armed/spec_hit/spec_miss surface the
#               hit rate on the telemetry panel.
#   2026-08-26  APP_BUILD -> "2026-08-26of-the-seat-survives-a-typo". BUILD of
#               -- LIVE_CRITIC_MODEL was set to "claude-haiku-4.5" (dot; real ID
#               claude-haiku-4-5) and the critic 404'd for four hours: 28
#               crashes, zero second opinions. tutor.py: a model-not-found 404
#               now swaps the seat STICKY to DEFAULT_MODEL with one loud event.
#               The env fix itself is on Render: LIVE_CRITIC_MODEL=claude-haiku-4-5.
#   2026-08-26  APP_BUILD -> "2026-08-26oe-one-thought-per-line". BUILD oe --
#               Jim's two flags from one resumed session: referee 49 (the check-
#               cram: label + value + substituted equation welded into one board
#               line) and rule 40(i) (after a gap a mid-flight problem is re-
#               derived, never resumed at its last step) -- the gap note HERE
#               carries the same law dynamically. Methodology 48 -> 49 referees.
#   2026-08-26  APP_BUILD -> "2026-08-26od-the-keyboard-closes". BUILD od --
#               Jim: "close the keyboard if I choose to do that." A ⌨️✕ on the
#               answer bar of session/practice/topic; the board takes its room
#               back (ns's ResizeObserver); reopen = the Type button (session)
#               or a fixed ⌨️ pill (practice/topic, whose link is retired).
#               Pages only; this stamp; referee count unchanged (48).
#   2026-08-26  APP_BUILD -> "2026-08-26oc-never-fast-forward". BUILD oc --
#               Jim's live algebra flag: "+3 to each side" -> "We got X equals 5"
#               with 3X = 15 and the divide never drawn or asked. Referee 48
#               (announced-unseen-result, heard-gated) + 15(a)'s never-fast-
#               forward clause. tutor.py/prompts.py only; this stamp; methodology
#               47 -> 48 referees, three places.
#   2026-08-26  APP_BUILD -> "2026-08-26nz-the-drawing-is-the-truth". BUILD nz
#               -- the third flag harvest: referee 47 (spoken counts must match
#               the [[objects]] drawing), 29(c) scoped to real boundaries (nu's
#               same-day stop-fork regression, owned + fixed), referee 45 learned
#               "what number did you build?", seventh ceiling raise 193k->195k.
#               All in tutor.py/prompts.py -- only this stamp changed here.
#               Methodology: 46 -> 47 referees, three places.
#   2026-08-26  APP_BUILD -> "2026-08-26ny-where-the-seconds-go". BUILD ny --
#               THE LATENCY DEEP DIVE (Jim: "ten seconds when somebody first
#               signs on and about five between problems... it's breaking up the
#               tempo"). Findings + full report in the project doc. Shipped here:
#               (1) PROMPT_CACHE_TTL=1h env support (tutor.py) -- a >5-minute
#               thinking pause no longer comes back to a cold 48k-token prompt;
#               (2) /api/admin/stats exposes critic_seat + prompt_cache_ttl, and
#               the admin tile now names the ACTUAL critic model instead of a
#               hardcoded "Opus" -- so the fast-critic A/B (the single biggest
#               env-only latency lever, ~1.5-3s/turn) can be run and read
#               honestly. NOT built unattended, proposed in the report: opener
#               prefetch at /home (kills the sign-on 10s), speculative next-turn
#               branches, sentence-streaming verification.
#   2026-08-26  APP_BUILD -> "2026-08-26nx-the-ritual-dies". BUILD nx -- CACHE-
#               BUSTING. Every HTML/JS/CSS response now carries Cache-Control:
#               no-cache (revalidate; ETag makes unchanged files 304s), so a
#               deploy reaches every browser on the next ordinary load -- no more
#               Ctrl+F5 ritual (it bit three times: demo sidebar, owner's flag,
#               admin queue). Audio/images/JSON untouched by content-type scoping
#               -- the voice cache must never pay a round-trip per sentence.
#   2026-08-26  APP_BUILD -> "2026-08-26nw-the-second-flag-harvest". BUILD nw --
#               Jim's four Entry-session flags + the placement gap he diagnosed
#               himself. HERE: the placed-student note now carries the vocabulary
#               law + first-session word tour (rule 40h holds the durable half).
#               Elsewhere: drill.html's three end doors, math-figures.js's
#               number line cap 660->1100, prompts.py's 15(a)/40(h)/48(h) and
#               the elementary trick-naming line. Ceiling untouched -- headroom
#               149 chars; the NEXT shared clause deliberates the seventh raise.
#   2026-08-26  APP_BUILD -> "2026-08-26nv-the-night-watchs-thirteen". BUILD nv
#               -- the 2026-08-26 night watch's 13 confirmed findings triaged:
#               referees 45 (answeredask) + 46 (norecordresume), slash/arrow/hug
#               notation entries, "lots of kids" in rule 42 (percentile exempt in
#               probstat), six prompt clauses, sixth ceiling raise (191k->193k).
#               All in tutor.py/prompts.py -- only this stamp changed here.
#               Methodology tile: 44 -> 46 referees, three places.
#   2026-08-26  APP_BUILD -> "2026-08-26nu-the-first-flag-harvest". BUILD nu --
#               Jim's flag queue paid for itself on day one: four confirmed
#               findings from one live evening. Referees 43 (unilateral sign-off,
#               heard-gated) + 44 (board paren balance), the offer-fork in referee
#               42, rules 29(c)/39(e)/47(e)/48(f), and the fifth dated
#               PROMPT_CEILING raise (188k -> 191k). All in tutor.py/prompts.py --
#               only this stamp changed here. Methodology tile: 42 -> 44 referees.
#   2026-08-25  APP_BUILD -> "2026-08-25nt-the-flag-shows-itself". BUILD nt --
#               one CSS constant in board.js: the owner's flag was drawn at 25%%
#               opacity and Jim could not find his own feature. 55%% now, and a
#               touch larger. Only this stamp changed here.
#   2026-08-25  APP_BUILD -> "2026-08-25ns-follow-the-pen". BUILD ns -- Jim:
#               "same problem with the sizing of the keyboard." nr repaired the
#               resize MOMENT; the failing case was the already-open keyboard with
#               a tall turn OUTGROWING the short board. scrollFeed's anchor now
#               follows the writing (see board.js's ns note); the symbol strip
#               gained its missing + key. All client-side; only this stamp here.
#   2026-08-25  APP_BUILD -> "2026-08-25nr-the-board-answers-for-its-size".
#               BUILD nr -- Jim, live in Pre-Algebra: the build-no symbol strip
#               opened and the tutor's "what do you get?" slid below the fold; he
#               had to scroll. Fix is ALL CLIENT-SIDE (board.js ResizeObserver on
#               the feed + the pronounced amber pause button on session/practice/
#               topic) -- nothing in this file changed but this stamp. See
#               static/board.js's nr note for the mechanism.
#   2026-08-25  APP_BUILD -> "2026-08-25nq-the-owners-flag". BUILD nq -- THE
#               OWNER'S FLAG. Jim, in a live geometry lesson, caught "piece" where
#               "angle" belonged and asked to be able to point at a sentence IN THE
#               APP and queue the fix. Ruling: "I only want it when I'm online. I
#               don't want the parents or teachers to see it." So the whole feature
#               rides the ADMIN KEY: board.js shows a tiny flag button on tutor
#               bubbles ONLY when the device holds the owner key (enabled from
#               /admin), and the three routes here -- POST /api/flag, GET
#               /api/admin/flags, POST /api/admin/flags/resolve -- all pass
#               _require_admin (same constant-time FORUM_MOD_KEY gate as every
#               admin call; header preferred, key never rides a URL we ship).
#               Students/parents/teachers have no key, so no button and 403 on the
#               routes. Data lands in store.flags (new table, additive); /admin
#               gained a Corrections queue panel. Nothing existing changed.
#   2026-08-25  APP_BUILD -> "2026-08-25np-the-phantom-and-the-nudges". BUILD np --
#               JIM'S FIRST TELEMETRY PANEL, ACTED ON. 274 fires across 560 turns
#               (49%% of turns paid a retry). The three roots: ① pendcheck (13%%,
#               #1) fired on rule 39(d)'s required check-ins whenever they mention
#               numbers -- exempted via _PQ_CHECKIN; expect its rate to drop by
#               half or more. ② spokenlen's nudge was unsatisfiable ("keep every
#               word" + fewer words) -- now first-beat-only, ~60 words. ③ the
#               critic nudge assigns the fix a place: the FIRST sentence grades
#               the ungraded answer / honors the skipped request. ALSO NOTED from
#               the same panel: the critic costs $0.92 against the brain's $5.85
#               -- my earlier "the critic is the top money lever" was WRONG in
#               production; retries and voice are the levers. ONLY tutor.py +
#               ruletests.py change; this is the stamp.
#   2026-08-25  APP_BUILD -> "2026-08-25no-one-keyboard-not-two". BUILD no -- JIM'S
#               UI ITEM 4, THE LAST OF THE REVIEW. math-keyboard.js reborn as a
#               SYMBOL STRIP living inside every answer bar (session's one box,
#               practice/topic's two): 17 math keys (÷ × − ± ² ³ ^ √ π θ ° parens
#               |x| ≤ ≥ ≠) inserting AT THE CARET of the same input the physical
#               keyboard types into; pointerdown+preventDefault keeps focus so a
#               phone's keyboard never closes mid-answer; |x| parks the caret
#               between the bars; every key's tooltip is its spoken name. ⚠️ NOT
#               the 2026-07-30 keypad returning: that sheet hid the microphone for
#               a week -- this file is now PINNED to never touch the mic. ONLY
#               static/math-keyboard.js + ruletests.py change; this is the stamp.
#   2026-08-25  APP_BUILD -> "2026-08-25nn-buttons-for-small-answers". BUILD nn --
#               JIM'S UI ITEMS 2+3 IN ONE BUILD. Yes/no check-ins and either-or
#               questions now ship [[choices]] taps in EVERY course (rule 39e); the
#               client has rendered them universally since 2026-08-03 -- only the
#               elementary prompts ever asked. The app's auto "I'm not sure" button
#               IS Jim's third button. Quizzes exempt: mastery is never a
#               one-in-three guess. Referee 42 holds the either-or shape; rule
#               39(d)'s required check-in wording is deliberately unmatched. Voice
#               and typing stay equally welcome -- taps are the fast lane, never
#               the only lane. Methodology count 41 -> 42. THIS FILE: stamp only.
#   2026-08-25  APP_BUILD -> "2026-08-25nm-ten-doors-not-a-wall". BUILD nm -- THE
#               DRILL PICKER, REBUILT FROM JIM'S UI REVIEW (item 1 of 4). One card
#               per course, tap to open its units, one open at a time, the arrival
#               course opens itself. And the "dead clicks" diagnosed: they always
#               worked -- every answer (enter-your-code, errors) went to the TOP of
#               a half-page wall. Messages now land in a note directly under the
#               tapped button, and the button itself says "starting…". ONLY
#               static/drill.html + ruletests.py change; this is the stamp.
#               STILL QUEUED from the same review: ② yes/no/confused quick buttons,
#               ③ finite-answer questions as tap bubbles, ④ the one-keyboard answer
#               layout. ② and ③ are one build (the choices machinery); ④ is its own.
#   2026-08-25  APP_BUILD -> "2026-08-25nl-an-angle-is-an-angle". BUILD nl -- THE
#               FORTY-FIRST REFEREE. Jim: the tutor said "piece" for "angle" in the
#               vocabulary lesson itself. Root cause: the geometry template's own
#               [[angle]] instructions modelled the word ("the 60° piece") -- the
#               tutor echoed its prompt. Template reworded, vocabulary rule added
#               (geometry-local), referee course-gated to geometry/precalc so
#               fractions keep their pieces and a pie chart's piece may be 90°.
#               Methodology count 40 -> 41. THIS FILE: stamp only.
#   2026-08-25  APP_BUILD -> "2026-08-25nk-no-up-there". BUILD nk -- THE FORTIETH
#               REFEREE. Jim's live catch: "looking at those three points up there"
#               while the points sat BELOW his words. board_layout_conflict rejects a
#               drawn-object noun + screen-direction phrase ("points up there",
#               "equation down there") -- narrow by necessity, because "down below"
#               and "down there" are legitimate MATH in two canonical scripts and
#               "up top" means numerator. The wider ban rides the prompt's board
#               block. Same law build `in` gave the tour, now for the tutor's own
#               prose. THIS FILE: stamp only. Methodology count 39 -> 40.
#   2026-08-25  APP_BUILD -> "2026-08-25nj-the-ones-that-got-away". BUILD nj -- THE
#               TWO REFEREES THAT EACH MISSED ONE, CLOSED. ① rule 16: "what would
#               f(4) be?" over a board showing only the worked f(3) -- the existing
#               referee needs a plug/substitute/check phrase, and a function ask
#               wears none. function_ask_rewrite_conflict (the 38th referee) demands
#               f(N) itself or the rule f(x)= on THIS reply's board. ② rule 44: a
#               NEW function DEFINITION written and questioned but never read --
#               the existing referee examines only board values carrying "?", and a
#               definition carries none. func_rule_spoken_conflict (the 39th),
#               heard-gated like the notation referee. ③ rule 15's column shape is
#               prompt-tier (a referee would have to guess which questions need a
#               written computation): COLUMN ARITHMETIC TOO clause added. The
#               canonical sweep caught ONE authored gap on the way in -- algebra1's
#               domain script wrote f(x)=1/x and never read it; fixed at source
#               (⚠️ one foundation clip re-renders on the next audio pass, pennies).
#               Methodology page: 37 -> 39 checks, three places. RULES.md
#               regenerated. THIS FILE: stamp only. STILL OPEN: prosecheck's 28
#               pass-throughs need the production "Referee fires by name" panel --
#               that is data only Jim's deploy can produce.
#   2026-08-25  APP_BUILD -> "2026-08-25ni-the-board-is-a-claim". BUILD ni -- THE
#               NIGHT WATCH'S 17 FINDINGS, THE MACHINE-FIXABLE HALF. ① mathcheck now
#               re-computes every ALL-CONSTANT equality chain drawn on the board (the
#               shipped 3/4-1/2=2/4-1/2 lie was invisible to a checker that read only
#               verify tags); a false board line now rides the same wrong->retry
#               machinery as a false spoken claim. ② The notation referee gains ÷,
#               the tight dot, and subscripts -- and finally reads EVERY quoted
#               attribute per tag, not just the first (the three-forms card had shown
#               it only its title). ③ Rules 47(h,i,j), 59(e) and two 61(c) entries
#               hold the quiz-conduct cluster. ④ Nightwatch's reviewer list gains
#               rule 42 -- it refuted two comparison findings for that exact
#               omission. NOTHING in main.py changes but this stamp; the work lives
#               in mathcheck.py, tutor.py, prompts.py, nightwatch.py. Swept clean:
#               0 false alarms across 306 canonical scripts; PART 3ds re-sweeps every
#               build. STILL OPEN from the same report: rules 44/16/15 referees each
#               missed one (build nj, next), and prosecheck's 28 pass-throughs are
#               the retry-prompt problem, not a referee problem.
#   2026-08-25  APP_BUILD -> "2026-08-25nh-let-them-finish-and-fly-in". BUILD nh --
#               JIM WATCHED THE FULL DEMO: "very good, just a couple of small things."
#               ① Feedback lines were cut off mid-word: four sites advanced on fixed
#               timers (1.9s under 5-second spoken lines). Every advance now chains
#               on the line FINISHING -- the same family as build nb's Next button,
#               one page over: a timer asking "done yet?" under a voice that is not.
#               ② Abrabot now FLIES onto the whiteboard at 220px and bounces while he
#               works; the sidebar orb stays Mr. Cadabra -- one character per face.
#               ONLY static/demo.html + ruletests.py change; this is the stamp.
#               No new voice lines. Verified by the upgraded headless harness: an
#               interruption ledger proves no feedback line is cancelled before its
#               own end, 18 assertions across four journeys, all green.
#   2026-08-25  APP_BUILD -> "2026-08-25ng-the-sidebar-catches-up". BUILD ng -- JIM
#               CAUGHT nf BEING HALF A FIX: "in the sidebar of the demo i see no
#               practice problems." The demo's replica sidebar was still the pre-mu
#               classroom. Now it carries the 🤖 Extra practice button (session.html's
#               twin), the walk-around tour introduces it, and the button WORKS --
#               a cold tap runs practice on the spot through a standalone door that
#               skips the end-of-lesson handoff line. THIS FILE: one tour line
#               appended to DEMO_VOICE_LINES (244 -> 245), byte-identical to
#               demo.html's, verified by ast.literal_eval on this side and a JS-string
#               parse on that side -- the nf comma lesson, applied.
#   2026-08-25  APP_BUILD -> "2026-08-25nf-the-demo-practices-too". BUILD nf -- EVERY
#               LEVEL DEMO NOW INCLUDES ABRABOT'S PRACTICE. Jim: "rewrite the demos so
#               that they include the practice problems with Abrabot." Flow per level:
#               teach -> problem -> two practice problems with the robot (his face,
#               his FREE browser voice, the drill's own personality and kindness, a
#               Skip door) -> congratulations. THIS FILE: ONE line appended to
#               DEMO_VOICE_LINES (243 -> 244) -- Mr. Cadabra's handoff, the only
#               rendered clip; everything Abrabot says is browser-voiced and costs
#               zero. ⚠️ The append initially LOST A COMMA and Python silently
#               concatenated two list strings: regex counted 244, ast.literal_eval
#               said 243. Caught before shipping because the count was verified BY
#               PARSING, not by pattern -- do the same next time. PART 3dr pins the
#               whole build, including re-deriving all 20 practice answers in Python
#               against demo.html's own abraAnswer().
#   2026-08-25  APP_BUILD -> "2026-08-25ne-on-the-menu". BUILD ne -- "HOW WE TEACH"
#               JOINS THE TOP NAV. Jim approved the reviewed page: "I like this
#               methodology page. Let's go ahead and add it to the menu." One
#               injector in site-nav.js covers all 13 marketing pages (the college-
#               dropdown pattern); methodology.html hardcodes its own link with
#               class="here". Placed after "Our mission" -- the two answer the same
#               visitor question. Only site-nav.js, methodology.html and ruletests.py
#               change; this is the stamp.
#   2026-08-25  APP_BUILD -> "2026-08-25nd-what-actually-happens". BUILD nd -- JIM
#               REVIEWED /methodology AND THIS IS HIS EDIT. New section 1 tells the
#               whole story plainly: an AI teaches and talks WITH the student, more
#               help when stuck, a math engine re-computes every claim, 37 checks
#               read every reply, and a second independent AI reviews the first --
#               "two AIs and a math engine, checking each other." Plus the feedback
#               section: spoken / board / site / parents / teachers, all positively
#               structured. The word "scripted" is RETIRED from visible copy at
#               Jim's direction (the blend is stated instead: "the curriculum is not
#               improvised, and the conversation is not canned"); the 90% tile and
#               rule card are gone from this page (the standard itself unchanged).
#               ONLY static/methodology.html + ruletests.py change; this is the
#               stamp. PART 3dq grew four (nd) pins holding Jim's review decisions.
#   2026-08-25  APP_BUILD -> "2026-08-25nc-the-receipts". BUILD nc -- THE MIDDLE
#               COURSES GET THEIR RECEIPTS. The deep dive found /methodology cited
#               real sources for the elementary courses and for Calc/DiffEq, while
#               the six courses between them got one uncited "standard progression"
#               paragraph. Jim: "I want people to know we've done all the research."
#               ⭐ THE RESEARCH WAS ALREADY IN THE RULES. Rules 53-58 have carried
#               WWC guide-and-recommendation tags since builds dl/ee. The page now
#               tells that story: three WWC practice guides mapped BY NAME to the
#               written rules implementing them, plus GAISE II for statistics (read
#               from the ASA's own PDF; our nine units follow its four-step arc).
#               ⚠️ NCTM's Principles to Actions deliberately NOT cited -- paid book,
#               unread, and the page's standard is read-before-named.
#               ONLY static/methodology.html + ruletests.py change; this is the stamp.
#               PART 3dq pins the citations, the quoted rule names (via RULES.md, the
#               generated bridge to tutor.py), the not-proven confession, and the
#               numbers strip (6,416). Page still NOT in the top nav -- Jim has not
#               reviewed the wording.
#   2026-08-24  APP_BUILD -> "2026-08-24nb-let-him-finish". BUILD nb -- NOTHING
#               APPEARS UNDER A TEACHER WHO IS STILL TALKING. Jim: "when Mr. Cadabra
#               is introducing Abrabot it still shows the Next button... it's very
#               distracting to have him talk and then have this next button show up,
#               because it feels like I'm supposed to push it."
#               ⚠️ BUILD mx BELIEVED IT HAD FIXED THIS, AND HALF-DID. mx hid the
#               button and revealed it on two paths -- speech finished silently, or
#               `onWaiting` fired -- but never asked what onWaiting MEANT. The timer
#               behind it asks "has this finished yet?" after THREE SECONDS, and his
#               introduction is four sentences, about twenty seconds of speech. So it
#               fired every single time, mid-sentence, and handed the button back the
#               key mx had just taken away. The hiding was real; the lock had a
#               second door.
#               ⭐ TWO FAILURES WERE SHARING ONE TIMER, and they are opposites:
#                 nothing audible after 3s -- it is not coming. Offer the button.
#                 audible and still going  -- he is TALKING. A button under a talking
#                                             teacher invites a child to interrupt him.
#               ⚠️ AND THE `ask` BEAT WANTS THE OPPOSITE OF THE FIX. It passes the same
#               callback to UNLOCK THE ANSWER BUTTONS, where being early is correct --
#               a child who can hear the question must never be locked out of
#               answering while it finishes. So patience is opt-in per call
#               (`patient`), not a new default. Changing the default would have been
#               the one-line version of this fix and would have broken answering.
#               ONLY static/drill.html CHANGES. main.py's change is this stamp.
#               PART 3dp pins it by LIFTING speak() and its constants out of
#               drill.html and driving them on a virtual clock -- the real 3000ms /
#               6000ms / 85-per-character values, four scenarios, about 50ms. Checked
#               against the mx code first: it fails ① at 3.0s, exactly as Jim saw.
#   2026-08-24  APP_BUILD -> "2026-08-24na-build-is-not-serve". BUILD na -- BUILDING
#               THE COURSE IS NOT TEACHING A CHILD, AND THE DASHBOARD NOW KNOWS IT.
#               Jim's /admin read "Cost / student-hour: $610.76". The arithmetic was
#               right and the statement was false: it divided roughly $1,000 of
#               ONE-TIME course construction -- rendering ~30,000 scripted lines to
#               audio, once, into a permanent disk cache -- by ONE WEEK of children's
#               engaged hours.
#               ⚠️ WHY THAT NUMBER WAS MEANINGLESS, not merely high: render the course
#               again next month and it DOUBLES while teaching gets no more expensive.
#               Teach ten times as many children and it COLLAPSES while nothing
#               improves. A number that moves for reasons unrelated to its own
#               question cannot be used to price anything.
#               TWO QUESTIONS, AND THEY MUST NEVER SHARE A TILE AGAIN:
#                 BUILD -- what did it cost to MAKE the course?   Paid once. Capital.
#                 SERVE -- what does an hour of teaching cost?    Paid every hour.
#               store.py owns the single definition (TTS_BUILD_MODES = script-prewarm,
#               prewarm) and splits the characters; this file only prices each half.
#               ⭐ usd_per_student_hour CHANGED MEANING IN THIS BUILD. It divides
#               serve_usd now, not total_usd. That is deliberate and it is the point
#               of the build -- see the ⚠️ block at the bottom of _usage_with_dollars.
#               The blended figure is NOT deleted: total_usd is untouched (the cost
#               alarm and the 30-day tiles read it), build_usd is reported beside it,
#               and usd_per_student_hour_blended keeps the old number inspectable.
#               A number that vanishes with no trace is how a dashboard loses an
#               argument with its own history.
#               ⚠️ NOTHING A CHILD SEES CHANGES. No lesson, no lane, no prompt.
#               ⭐ WHAT THE SPLIT IMMEDIATELY REVEALED, on a reconstruction of Jim's
#               own week: THE SECOND OPINION COSTS NEARLY TWICE THE TEACHING BRAIN
#               ($27.42 of critic against $14.77 of tutor). LIVE_CRITIC is the
#               majority of marginal cost, and build jp already measured it at ~21%
#               of turn time. It is now the single biggest lever on both the money
#               and the wait -- and that was invisible while ~$1,000 of course build
#               sat on top of it.
#               PART 3do of ruletests.py pins all of it, including the arithmetic on
#               a live database: a new render pass in this file whose mode is not in
#               TTS_BUILD_MODES fails the battery, because forgetting should be a red
#               battery today rather than a wrong dashboard in six weeks.
#   2026-08-24  APP_BUILD -> "2026-08-24mz-caught-and-actually-fixed". BUILD mz --
#               THE SECOND MEASUREMENT LIE, SAME FAMILY AS mw. Jim's /admin panel read
#               "Errors caught & fixed: 40" and "39.1% verified right first try", and
#               I went after the 39.1% -- which is when I found that the 40 was
#               counting replies that were caught and NOT fixed.
#               ⚠️ NOTHING IN THIS BUILD CHANGES WHAT A CHILD SEES. It is entirely
#               static/admin.html arithmetic plus the pins that hold it. main.py's
#               only change is this stamp. The numbers the server reports were always
#               right; the page was adding them up wrong.
#               THE ARITHMETIC, for whoever reads this next:
#                 verify_ok             -- the draft was right first try
#                 verify_fixed          -- a referee caught it AND a retry repaired it
#                 verify_unresolved     -- mathcheck judged three drafts wrong and we
#                                          SHIPPED the third one anyway
#                 verify_prose-unresolved / verify_critic-unresolved -- the same
#                                          surrender, from the prose referees and from
#                                          the live critic
#               The page used to fold verify_unresolved into "caught & fixed" while
#               LEAVING IT OUT of "shipped unresolved" -- exactly backwards, so the
#               one number that should have been alarming was decorating the good
#               column instead. From Jim's own screen (caught=40, prose-shipped=29),
#               at most 11 of the 40 were ever genuinely fixed.
#               Now: "Caught & actually fixed" counts ONLY verify_fixed, "Shipped
#               unresolved" counts all three surrenders and names the split, and the
#               first-try rate is its own tile with a colour (>=80 good, >=60 warn).
#               ⭐ THE RULE THIS KEEPS BREAKING: a dashboard that cannot be wrong is
#               worse than no dashboard, because you act on it. Twice now (mw, mz) a
#               tile has been quietly generous. PART 3dn in ruletests.py now pins the
#               arithmetic itself, not just the presence of the keys.
#               STILL OPEN and worth Jim's attention: WHY the first-try rate is 39%.
#               The tile is honest now; the underlying number has not moved. The
#               "Referee fires by name" panel on the same page is where that answer
#               lives, and it needs production data, not sandbox data.
#   2026-08-24  APP_BUILD -> "2026-08-24mx-abrabot-has-a-voice". BUILDS mw-my, from
#               ONE live session of Jim's. Six separate defects, and the two that
#               matter most were invisible until he hit them.
#               ⭐ mw -- A REFEREE VERDICT THAT NOBODY COUNTED. tutor.py has set
#               status="critic-unresolved" since build iv with the note "visible in
#               the usage log". It never was: store.py had no key for it, so every
#               reply that SHIPPED carrying an unresolved LIVE-CRITIC objection was
#               filed as verify_none -- "no check ran". The live critic is the one
#               whose first question is "does this draft grade the answer the student
#               just gave?", and Jim answered 13 and was never told. Identical to the
#               gz bug, one referee later. /admin now counts prose AND critic
#               findings, an unknown verdict is LOUD instead of silently "unchecked",
#               and PART 3dn reads tutor.py's statuses and fails if store.py has
#               nowhere to put one.
#               ⭐ my -- THE BOARD COULD SHOW ADDING AND NOT TAKING. [[objects]] has
#               had add="1" (drawing "⭐⭐⭐⭐⭐ + ⭐") since the elementary courses
#               shipped, and NOTHING for subtraction -- so 7 authored boards and every
#               generated one said "take two away" over a picture where nothing was
#               ever taken. Jim: "it could have shown four stars and crossed out one
#               of the stars, but instead he just laid out a problem and solved it
#               and did no teaching." New take="2" strikes the ones removed.
#               mx -- ABRABOT. His whole personality was eight clipped lines
#               ("Correct!" / "Not quite. Have one more try."); Jim: "no personality
#               to it... a strict teacher that's gonna spank me." Rewritten, FREE,
#               because he speaks in the browser voice and is not in the paid
#               closure. His name is respelled "Abra-bot" FOR SPEECH ONLY (the
#               browser read it "ah-brab-oh"), on his lines alone -- never Mr.
#               Cadabra's, whose audio is cache-keyed on verbatim text. And the Next
#               button now appears ONLY when the speech was silent.
#   2026-08-24  APP_BUILD -> "2026-08-24mv-what-it-is-built-on". BUILD mv -- THE
#               METHODOLOGY PAGE. Jim: "people want to know what we've based our
#               pedagogical approach to. What resources did we use? What research
#               backs up our methodology?"
#               NEW: /methodology -> static/methodology.html.
#               ⚠️ BOTH SOURCES WERE READ BEFORE THEY WERE NAMED, and their scope is
#               stated rather than stretched: the MAA Instructional Practices Guide
#               (© 2018 MAA, CC BY-NC 4.0) is about UNDERGRADUATE teaching, and
#               A Story of Units (© 2015 Great Minds) covers PRE-K THROUGH GRADE 5.
#               Neither organisation has endorsed anything and the page says so.
#               ⚠️ THE THIRD SECTION SAYS WE HAVE PROVEN NOTHING. There is no efficacy
#               study of this product. That paragraph is the reason the other two are
#               worth believing, and it is the one to defend if anyone asks to soften
#               it. NOT IN THE TOP NAV until Jim has read the wording.
#   2026-08-24  APP_BUILD -> "2026-08-24mu-the-practice-button". BUILD mu -- THE TOUR
#               TELLS THEM ABOUT IT, AND THE LESSON HAS A DOOR. Jim flagged the intro
#               himself: "we're gonna need to change the intros... here's your
#               practice button. If you wanna go practice, Abrabot will show up."
#               Nothing in this file changed but the stamp; the work is in
#               session.html (sidebar link + tour stop) and app-nav.js.
#               ⚠️ AND IT UNCOVERED A NAMING COLLISION. The lesson sidebar has
#               "✏️ Practice a problem" -- bring-me-YOUR-homework -- and mt had just
#               added a "✏️ Practice" pill for Abrabot's drill. Two different
#               features, one word, one pencil. Abrabot now wears his own robot face
#               (🤖) and the word EXTRA, and the tour stop states the difference in
#               one plain sentence instead of leaving a child to guess.
#   2026-08-24  APP_BUILD -> "2026-08-24mt-practice-counts". BUILD mt -- PRACTICE GETS
#               A DOOR AND A COUNTER.
#               ⚠️ THE BUG UNDERNEATH THE FEATURE: nothing in the app linked to
#               /drill. Not the nav, not the lesson, not the dashboard. 25,376
#               practice problems reachable only by typing the URL -- which is how
#               Jim found it on 2026-08-24 ("I can't see how to get to the practice
#               problems"). app-nav.js now carries a ✏️ Practice pill on every
#               student page, and drill.html finally loads the nav so a child can
#               get back out.
#               NEW: /api/drill/stats/{code}; every retired practice problem is
#               recorded via store.record_drill.
#               ⚠️ RECORDED WHERE THE PROBLEM RETIRES, not on every tap -- a second
#               chance is the same problem, and counting the re-ask would make a
#               child who eventually got it look like they got it wrong.
#               ⚠️ AND PRACTICE STILL SPENDS NOTHING. Jim, same day: "I don't want
#               practice to cost money." PART 3dm drives the lane with httpx.stream
#               replaced by a function that raises.
#   2026-08-24  APP_BUILD -> "2026-08-24ms-nothing-given-away". BUILD ms -- 71 of the
#               113 giveaways teachaudit found are closed. Nothing in this file
#               changed but the stamp; the fix is lessonscripts', and it swapped
#               WHICH PROBLEM IS ASKED rather than rewriting any teaching.
#               ⚠️ 462 NEW CACHE KEYS -- about $8.49 to render. Press ② after
#               deploying. The 462 old clips fall out of the closure and the evictor
#               collects them; nothing is billed twice for the same text.
#   2026-08-24  APP_BUILD -> "2026-08-24mr-one-pennies". BUILD mr -- 224 SPOKEN LINES
#               STOPPED SAYING "1 PENNIES". Nothing in this file changed but the
#               stamp; the fix is lessonscripts', and teachaudit.py is a new
#               standalone audit (not imported by anything, like workedaudit.py).
#               ⚠️ THE 224 CHANGED LINES ARE NEW CACHE KEYS -- about $2.70 to render.
#               Press ② after deploying. The old clips become orphans and the
#               evictor collects them; nothing is billed twice for the same text.
#   2026-08-24  APP_BUILD -> "2026-08-24mq-measure-from-here". BUILD mq -- THE COST
#               EPOCH, AND COST PER STUDENT-HOUR. Jim asked to "zero out our current
#               cost measurement so it is measuring cost based on how we do it now",
#               because the 7/30-day panels are dominated by ONE-TIME spend (~$806 to
#               render the course, ~$11 more for Entry-Level U8/U9) and would go on
#               being so for a month.
#               ⚠️ NOTHING IS DELETED. New POST /api/admin/cost-epoch writes a
#               timestamp; the payload gains cost_epoch + usage_epoch, and the cost
#               tiles gain a SECOND reading measured from it. usage7/usage30 are
#               byte-for-byte what they were. Until Jim starts an era, usage_epoch is
#               None and /admin looks exactly as it does today.
#               ⭐ COST PER STUDENT-HOUR is the number he actually asked for. Cost per
#               STUDENT flatters a quiet week and punishes a busy one; an hour of
#               teaching is the unit the product is sold in. NULL, never 0, when no
#               hours have been measured -- "$0.00 per hour" reads as "teaching is
#               free", the exact opposite of unmeasured.
#   2026-08-24  APP_BUILD -> "2026-08-24mp-curriculum-complete". BUILD mp -- ⭐⭐
#               ENTRY-LEVEL UNIT 9, AND WITH IT EVERY UNIT OF EVERY COURSE HAS
#               SCRIPTED LESSONS. No change in this file beyond the stamp: the four
#               lessons and five ops are lessonscripts'. Recorded here because the
#               closure GREW -- 29,734 -> 30,101, +367 -- and Unit 9's audio costs
#               about $4.98 to render once. Press ② in /admin until it reads `done`.
#   2026-08-24  APP_BUILD -> "2026-08-24mo-unit-eight". BUILD mo -- ENTRY-LEVEL UNIT 8.
#               No change in this file beyond the stamp: the four new lessons and the
#               five new ops are lessonscripts', and the drill-pool ranking fix is
#               drillpool's. Recorded here because the closure GREW -- 29,332 lines
#               -> 29,734, +402 -- and Unit 8's audio costs about $5.75 to render
#               once. Press ② in /admin until it reads plain `done`.
#   2026-08-24  APP_BUILD -> "2026-08-24mn-the-seam". BUILD mn -- MR. CADABRA KEEPS
#               HIS VOICE THROUGH THE WHOLE HANDOFF. Jim tested the drill with the
#               fully rendered course and heard the seam mj built: the fly-in's hello
#               ("Let's look at this one together.") and the goodbye played in the
#               BROWSER voice while the re-teach between them played in his REAL
#               voice. mj had left those two lines out of the closure on purpose;
#               build mn moves them INTO it. The strings now live in lessonscripts
#               (CADABRA_HANDOFF_HELLO / CADABRA_HANDOFF_BYE, beside ABRABOT_INTRO)
#               and _CAD_HELLO/_CAD_BYE below are aliases of them -- one owner, so
#               the prewarm renders them, the evictor protects them and the drill
#               gate admits them without a second list anywhere. NO route changed;
#               _drill_speakable() starts answering true for these two lines the
#               moment they are in the closure, and the page already asks for the
#               natural voice wherever that is true.
#               ⚠️ ONE PRESS OF ② AFTER DEPLOY renders the two new lines (~$0.02).
#               Until then the cache-only gate 204s them to the browser voice --
#               the old behavior, never a charge.
#   2026-08-24  APP_BUILD -> "2026-08-24mm-deploy-safe". BUILD mm -- ONE FILE MUST
#               NOT BE ABLE TO TAKE THE SITE DOWN. Found while preparing the handoff
#               for the morning deploy, not by a test.
#               ⚠️ THE RISK. drillpool.py is a NEW file (mg) and main.py imported it
#               bare. `git commit -am` does NOT stage a new untracked file, and Jim
#               deploys GitHub -> Render. So the realistic first-deploy failure was:
#               drillpool.py never reaches the repo, main.py raises ImportError at
#               module load, and the WHOLE SITE is down -- for a feature nobody had
#               used yet. static/drill.html and static/script-board.js are new too,
#               but a missing static file is a 404 on one page, not a dead app.
#               THE FIX IS THE HOUSE PATTERN, not a special case: misconceptions,
#               foundations, sprints and nightwatch are ALL imported try/except into
#               None and reported in /health's `subsystems`. Drill now joins them.
#               A deploy that lost the file gets: the site up, "drillpool": false on
#               /health, an empty picker, and a 503 with words on /api/drill/start --
#               instead of a blank page and no clue.
#               PART 3dj pins that the import is guarded, that /health reports it,
#               and that every route which touches drillpool checks it first.
#   2026-08-23  APP_BUILD -> "2026-08-23mk-the-introduction". BUILD mk -- PHASE 5
#               OF ABRABOT, AND THE LAST ONE: MR. CADABRA INTRODUCES HIM, in four
#               authored lines, in his real voice, the first time a child opens the
#               drill room. 525 characters. About TWELVE CENTS, once, ever -- I told
#               Jim one to two dollars when I scoped it; the real number is $0.12.
#               ⚠️ THE LINES WERE THE EASY HALF. They are the first speech in the
#               product that belongs to the COURSE rather than to a lesson, and
#               main.py built "the closure" in SIX separate places -- the prewarm, the
#               dry-run, the clip audit, the model split, the eviction guard and the
#               byte estimator -- each as its own comprehension over audio_lines().
#               Adding a line to five of six is not a small bug: a line the evictor
#               does not know about is DELETED after the course paid to render it,
#               and a line the prewarm does not know about is SILENCE in production.
#               So lessonscripts.course_audio_lines() is now the one answer and all
#               six ask it. It also declines to include course-level speech when the
#               caller narrowed to a single lesson, so re-rendering one lesson cannot
#               quietly re-price the introduction.
#               ⚠️ AND THESE LINES ARE OUTSIDE validate()'s REACH, because validate()
#               takes a lesson. PART 3di holds them to the same rules instead -- the
#               VOCABULARY canon, the beat word cap, no notation -- and earned its
#               keep on this very build: the first draft of line four said a problem
#               "gives you trouble", and "gives you" is a banned synonym for
#               "equals". Speech nothing checks is speech that quietly acquires
#               "subtract" eighteen months from now, in his real voice, to a child.
#               ONCE PER CHILD, PER PROCESS. No store write in this lane, so a
#               redeploy re-introduces them. That is the right way round: hearing it
#               twice is a small cost, skipping it for a child who never heard it is
#               the feature not existing.
#               ⚠️ FOR JIM'S RENDER: the closure is now 29,330 lines, up 4. Those four
#               are new and unrendered, so they want to be in the SAME render pass as
#               the rest -- not a separate trip.
#   2026-08-23  APP_BUILD -> "2026-08-23mj-the-handoff". BUILD mj -- PHASE 4 OF
#               ABRABOT: HE FETCHES MR. CADABRA, AND IT COSTS NOTHING.
#               Jim: "if it detects a child is struggling, it needs to call in Mr
#               Cadabra to do some more teaching" and "can we have it fly in and
#               replace mr cadabra when it enters the game." Both now happen.
#               ⭐ THE CHANGE THAT MATTERS IS A PIN THAT MOVED. mh and mi enforced
#               "drill.html must not contain the string /api/speak". That was the
#               right REASON written as the wrong RULE. The reason: a GENERATED
#               problem's sentence was never pre-rendered, so sending it to a paid
#               renderer is a guaranteed cache miss -- a live call per problem, per
#               child. The rule held only while the lane never legitimately needed
#               the route. Mr. Cadabra's re-teach is the exact opposite: it is the
#               lesson's OWN authored teach beat, enumerated by audio_lines(),
#               rendered once by the prewarm, a cache hit forever.
#               So the guarantee moved to where a page cannot get it wrong. voice.js
#               sends lane:"drill"; /api/speak-prep then (a) REFUSES a ticket for any
#               text outside the scripted closure and (b) mints a CACHE-ONLY ticket,
#               so even an authored line that has not been rendered yet costs nothing
#               and 204s to the browser voice. Half the course is still unrendered
#               while Jim's quota refills, and a drill request must never be the
#               thing that renders it. When the render finishes, his real voice
#               appears in the drill lane by itself.
#               ⭐ AND IT IS PROVED, NOT ARGUED. PART 3dh's live drive replaces
#               httpx.stream with a function that RAISES, so if anything in this lane
#               ever reaches ElevenLabs the battery fails instead of Jim's card.
#               THE LADDER: first fetch = ONE worked example (a stuck child usually
#               needs to watch one done, not to hear the lesson from the top); second
#               fetch = the full teach sequence, then the worked example.
#               ⚠️ AND THE COUNTERS RESET WHEN HE ARRIVES, or a child having a bad
#               afternoon is re-taught on every single miss -- which is how a helpful
#               feature turns into a punishment.
#               ⚠️ WHAT TRIPS IT, HONESTLY. The scope said "the same misconception
#               twice". misconceptions.py cannot deliver that here: match() reads the
#               WORDS of an answer for detect-strings, and a drill answer is a TAPPED
#               NUMBER with no words in it -- many entries carry no detect strings at
#               all. So the trigger is what the lane can actually measure and has
#               measured since mh: three wrong in a row, or two problems missed even
#               on the second try. Claiming misconception detection off a tap would
#               be a measurement that does not exist.
#   2026-08-23  APP_BUILD -> "2026-08-23mi-abrabot-the-character". BUILD mi --
#               PHASE 3 OF ABRABOT: HE BECOMES A CHARACTER. NOTHING IN THIS FILE
#               CHANGED but this note and the stamp. The work is in three static
#               files, and all three changes are ADDITIVE with the old behaviour as
#               the default:
#               (1) static/tutor-face.js -- the robot's eight colour constants became
#               TutorFace.PALETTES: .cadabra unchanged to the byte, plus .abrabot
#               (cyan shell, amber eyes). draw() resolves opts.palette into the SAME
#               eight local names the drawing code always used, so not one drawing
#               line moved.
#               ⭐ AND opts.presence:false DRAWS THE ROBOT ALONE. The presence layer
#               is VIDEO OF A REAL PERSON. Without that flag the drill page would
#               have laid Mr. Cadabra's actual face over Abrabot's body the moment
#               the video manifest deployed -- and it would have looked like a
#               rendering glitch rather than the impersonation it is. PART 3dg pins
#               that the drill page passes it.
#               (2) static/voice.js -- a `voiceProfile` hook, null by default, so a
#               page can give its speaker its own voice, rate and pitch. Abrabot
#               lives on the browserSpeak path by design (a generated problem has no
#               clip), and that path had exactly ONE voice: Mr. Cadabra's fallback.
#               ⚠️ THE PITCH IS THE GUARANTEE, NOT THE VOICE. A machine may have one
#               English voice installed, and then no preference list can separate two
#               characters -- so a profile always shifts rate and pitch too. The
#               battery pins the DEFAULTS (1.0 / 0.9) as literals, because "additive"
#               is a claim until something holds it.
#               (3) static/drill.html -- his face on the picker and beside his words,
#               his name under both, and a brief smile when an answer is right.
#               Deliberately NOT TutorFace.celebrate(): that gold burst marks a
#               problem finished in a LESSON, and drill is practice.
#               ⚠️ WHY THE ROBOT IS THE RIGHT FACE FOR HIM AND ALWAYS WAS. Jim, in
#               tutor-face.js's build-ej note: "I don't like the robot... I think
#               it's fine to have Mr. Cadabra in every instance." The robot's job has
#               been to be the fallback face nobody wants to see. Here it becomes a
#               face somebody DOES want: a helper who is visibly a machine, standing
#               next to a teacher who is visibly a person.
#   2026-08-23  APP_BUILD -> "2026-08-23mh-abrabot-drill-loop". BUILD mh --
#               PHASE 2 OF ABRABOT: THE DRILL LOOP. Phase 1 built the problems
#               (drillpool.py, 24,880 of them, validator-vetted) and wired them to
#               nothing. This build gives them a door: three routes here, one new
#               page (static/drill.html), one extracted shared file
#               (static/script-board.js), and GET /drill.
#               ⭐ THE RULE THAT SHAPES THE WHOLE LANE: A GENERATED PROBLEM HAS NO
#               CLIP. Mr. Cadabra's voice is pre-rendered per line and the cache is
#               keyed on the verbatim text, which is what makes every scripted line
#               free forever -- and what makes a generated sentence a guaranteed
#               MISS: a live ElevenLabs call per problem, per child, at full price
#               and full latency. So Abrabot speaks in the BROWSER's own voice.
#               That is not a compromise dressed as a feature; it is why he is a
#               different character. drill.html never sets elevenEnabled and never
#               calls /api/voice-status, so voice.js takes its browserSpeak path,
#               and PART 3df pins that the page names no paid audio route at all.
#               ⚠️ THE SHARED BOARD LAYER, and why it is a file and not a copy.
#               pilot.html had carried board.js's ambient contract and the scripted
#               tag dispatcher inline since kj. The drill page needs exactly the
#               same twenty-nine tags. voice.js's own header records what happened
#               the last time this lane duplicated a layer: FOUR hand-ports of the
#               audio code in a row, each missing a different one of the four
#               head-of-clip protections, until the copy was deleted and the real
#               file loaded. So the dispatcher moved to script-board.js VERBATIM
#               and pilot.html now loads it. Both pages are browser-driven in the
#               battery, because "nothing changed" is a claim, not a proof.
#               THE POOLS ARE MEMOISED, NOT PRELOADED. One lesson costs ~0.07s to
#               pool (21.7s for all 328), so the first child to drill a lesson pays
#               milliseconds. /api/drill/lessons kicks a background warm walk and
#               reports `ready` honestly -- a null count means NOT MEASURED YET,
#               never "no problems". Boot is untouched: a cold Render instance has
#               a redeploy's worth of work to do already.
#               MASTERY IS UNTOUCHED, still, by Jim's ruling: "Drill is practice,
#               quizzes are for mastery." The lane writes exactly one thing: a
#               usage row, kind="drill", so /admin can see it working. No topic
#               row, no unit, no mastery, ever.
#               HONEST GAPS, recorded so they are not mistaken for bugs: (a) the
#               pool is walked from its easiest end on every NEW session, because
#               nothing is persisted -- position is a store write and this lane
#               does not write; (b) 53 of 328 lessons have no pool at all, and the
#               picker says so up front rather than failing at the tap; (c) the
#               server already reports `struggling` and the page shows it only
#               under ?dev=1 -- Abrabot must NOT promise to fetch Mr. Cadabra in a
#               build where he cannot. That is phase 4.
#   2026-08-23  APP_BUILD -> "2026-08-23mg-abrabot-phase-one". BUILD mg --
#               PHASE 1 OF ABRABOT, the practice assistant. NOTHING IN THIS FILE
#               CHANGED but this note and the stamp: phase 1 is a new module
#               (drillpool.py) and a battery pin, wired to no route and no page.
#               WHAT IT IS. Every op already carries a check() saying which
#               {a,b,c} are legal -- the auto-picker has used them to choose banks
#               for thirteen builds. So the ops ARE generators. drillpool turns
#               that surface into 24,880 EXTRA practice problems against the 3,947
#               authored, 6.3x the practice depth with no new authoring.
#               ⭐ THE DESIGN DECISION WORTH KEEPING: the admission filter is the
#               COURSE'S OWN validate(), not new rules in the new file. Every
#               candidate is put in a bank with nine of its lesson's human-vetted
#               problems and must survive all forty-odd rules. An envelope of tap
#               ratios and bounds -- the first design -- could never have caught
#               what that did on the first run: problems that do not CARRY in a
#               carrying lesson, do not REGROUP in a regrouping one, DO carry in
#               the lesson promising none, and sums overflowing the tens in a
#               two-digit lesson. Those promises live in validate(); a second copy
#               would have drifted.
#               ⚠️ AND THE PIN EARNED ITS KEEP IMMEDIATELY, on the build that wrote
#               it: pool_for()'s early return (the cap and scan-limit exit) handed
#               back an UNSORTED list, so the 61 biggest pools -- the ones a child
#               is likeliest to reach -- lurched between hard and easy while every
#               small pool ramped properly. Pin an invariant; do not trust the
#               function that holds it.
#               MASTERY IS UNTOUCHED, by Jim's ruling: "Drill is practice, quizzes
#               are for mastery." PART 3de pins that drillpool cannot reach store.
#   2026-08-23  APP_BUILD -> "2026-08-23mf-two-honest-numbers". BUILD mf --
#               ⚠️ SUPERSEDES mf's SIBLING: if you took a main.py stamped "me"
#               earlier today, DISCARD IT and deploy this one instead. Same
#               evictor fix, plus the second bug below. render.yaml is
#               unchanged from the me delivery.
#               THE PROJECTION WAS ~35% LIGHT, and Jim was about to plan a
#               $418 render around it. _tts_cache_bytes_per_char() divided the
#               average size of CACHED clips by the average line length of the
#               WHOLE closure -- including the 10,324 lines not rendered yet.
#               Two different populations: his cached clips averaged 92.7
#               characters against a closure average of 124.9, so the rate came
#               back as 923 B/char while those very clips sat on disk at 1,244.
#               The admin panel therefore promised a finished cache of 3,762 MB
#               when the honest figure is ~4,345 -- a 582 MB error against a
#               4,500 MB cap, i.e. the difference between comfortable and
#               nearly full. Each sampled clip is now weighed against ITS OWN
#               text via the new _script_closure_chars() memo; generated-lane
#               clips are skipped rather than guessed at. Reproduced against a
#               simulated cache built to Jim's exact position: old estimator
#               31.6% low, new estimator 0.0%.
#               ⚠️ NOTE FOR JIM, unrelated to any code here: ELEVENLABS_VOICE_ID,
#               ELEVENLABS_MODEL and SCRIPT_TTS_MODEL are all INSIDE the cache
#               key. Changing any one of them invalidates all 19,002 clips he
#               has paid for and the whole course counts as missing again.
#               TTS_CACHE_MAX_MB is not in the key and never was -- raising it
#               from 2500 to 4500 could not, and did not, affect the voice.
#   2026-08-23  APP_BUILD -> "2026-08-23me-the-evictor-can-see-the-course".
#               BUILD me -- ⚠️ A REAL BUG, FOUND WHILE CHECKING WHETHER THE
#               FINISHED COURSE FITS ON THE DISK. _evict_tts_cache() culled
#               down to a flat 80% of the cap. With Jim's cap at 4,500 MB
#               that target is 3,600 MB -- but the completed course's audio
#               closure is 3,738 MB. So the first time anything tipped the
#               cache over the cap, eviction would have thrown away every
#               generated clip, found itself STILL above target, and then
#               deleted ~138 MB of COURSE audio that had been paid for --
#               putting those lessons back on the streaming path, which is
#               exactly where build ke's slurring lived. The protection added
#               in ke (evict the generated lane first) was real but could not
#               save the course from the TARGET itself.
#               The target now never falls below what the protected closure
#               actually occupies, plus a 64 MB margin so a cull does not
#               re-enter on the next clip. A cap genuinely too small still
#               warns and still culls -- that decision stays Jim's.
#               render.yaml updated in the same build: it still documented a
#               1 GB disk, and it is the file a rebuild-after-disaster starts
#               from. Now 5 GB with TTS_CACHE_MAX_MB recorded beside it.
#   2026-08-23  APP_BUILD -> "2026-08-23md-the-curriculum-is-complete".
#               BUILD md -- ⭐⭐ THE CURRICULUM IS COMPLETE. DIFFEQ UNIT 9
#               (Nonlinear Systems & Stability). 324 lessons -> 328, 313
#               ops -> 317. THIRTEEN COURSES DONE. NOTHING IN THIS FILE
#               CHANGED but this note and the stamp.
#   2026-08-23  APP_BUILD -> "2026-08-23mc-algebra-and-the-plane". BUILD
#               mc -- DIFFEQ UNITS 7 AND 8 (Laplace Transforms; Linear
#               Systems & the Phase Plane). 316 lessons -> 324, 305 ops
#               -> 313. NOTHING IN THIS FILE CHANGED but this note and
#               the stamp. ONE UNIT LEFT IN THE ENTIRE CURRICULUM.
#   2026-08-23  APP_BUILD -> "2026-08-23mb-one-number-decides". BUILD mb
#               -- DIFFEQ UNITS 5 AND 6 (Second-Order Linear:
#               Homogeneous; Nonhomogeneous, Vibrations & Resonance).
#               308 lessons -> 316, 297 ops -> 305. NOTHING IN THIS FILE
#               CHANGED but this note and the stamp.
#   2026-08-23  APP_BUILD -> "2026-08-23ma-the-shape-and-the-walk". BUILD
#               ma -- DIFFEQ UNITS 3 AND 4 (Qualitative Analysis:
#               Equilibria & Stability; Numerical Methods: Euler &
#               Runge-Kutta). 300 lessons -> 308, 289 ops -> 297.
#               NOTHING IN THIS FILE CHANGED but this note and the
#               stamp.
#   2026-08-23  APP_BUILD -> "2026-08-23lz-the-equation-as-a-picture".
#               BUILD lz -- ⭐ DIFFERENTIAL EQUATIONS OPENS, the
#               thirteenth and last course (U1 Introduction,
#               Classification & Slope Fields; U2 First-Order:
#               Separable & Linear). 292 lessons -> 300, 281 ops -> 289.
#               NOTHING IN THIS FILE CHANGED but this note and the
#               stamp.
#   2026-08-23  APP_BUILD -> "2026-08-23ly-calculus-complete". BUILD ly --
#               ⭐ CALCULUS COMPLETE (U8 Applications of Integration; U9
#               Introduction to Differential Equations). 284 lessons ->
#               292, 273 ops -> 281. TWELVE courses done; only
#               Differential Equations remains. NOTHING IN THIS FILE
#               CHANGED but this note and the stamp.
#   2026-08-23  APP_BUILD -> "2026-08-23lx-backwards-and-the-area". BUILD
#               lx -- CALCULUS UNITS 6 AND 7 (Antiderivatives &
#               Indefinite Integrals; The Definite Integral & the FTC).
#               276 lessons -> 284, 265 ops -> 273. NOTHING IN THIS FILE
#               CHANGED but this note and the stamp.
#   2026-08-23  APP_BUILD -> "2026-08-23lw-the-tool-and-the-best". BUILD lw
#               -- CALCULUS UNITS 4 AND 5 (Applications of Derivatives; Curve
#               Sketching & Optimization). 268 lessons -> 276, 257 ops -> 265.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp.
#   2026-08-23  APP_BUILD -> "2026-08-23lv-the-slope-at-a-point". BUILD lv --
#               CALCULUS UNITS 2 AND 3 (The Derivative; Product, Quotient &
#               Chain Rules). 260 lessons -> 268, 249 ops -> 257. NOTHING IN
#               THIS FILE CHANGED but this note and the stamp.
#   2026-08-23  APP_BUILD -> "2026-08-23lu-inference-and-calculus". BUILD lu
#               -- ⭐ PROBABILITY & STATISTICS COMPLETE (U9 Sampling &
#               Inference) and ⭐ CALCULUS OPENS (U1 Limits & Continuity).
#               252 lessons -> 260, 241 ops -> 249. NOTHING IN THIS FILE
#               CHANGED but this note and the stamp. Jim raised
#               TTS_CACHE_MAX_MB to 4000 on 2026-08-23, which covers the
#               finished course (~3,800 MB projected). ELEVEN courses done;
#               only Calculus (U2-U9) and Differential Equations remain.
#   2026-08-23  APP_BUILD -> "2026-08-23lt-the-curve-that-fits". BUILD lt --
#               PROB & STATS UNITS 7 AND 8 (Random Variables & Expected
#               Value; The Normal Distribution). 244 lessons -> 252, 233 ops
#               -> 241. NOTHING IN THIS FILE CHANGED but this note and the
#               stamp -- the course grew in lessonscripts.py (ops pdis/evwa/
#               fair/hedg and n68/zsco/zval/ntal). U7: a distribution adds to
#               one whole, expected value as a weighted average, what prize
#               would be fair, and the long-run cost of a play. U8: the 68
#               percent rule as a headcount, counting standard deviations,
#               reading the curve backwards, and how few people live in the
#               tails. ⭐ [[normal]] used for the first time -- the LAST
#               unused renderer in the app, and teach-only, since it labels
#               the axis at every standard deviation.
#   2026-08-23  APP_BUILD -> "2026-08-23ls-a-number-on-a-chance". BUILD ls --
#               PROB & STATS UNITS 5 AND 6 (Probability Basics; Conditional
#               Probability & Independence). 236 lessons -> 244, 225 ops ->
#               233. NOTHING IN THIS FILE CHANGED but this note and the stamp
#               -- the course grew in lessonscripts.py (ops ppct/por/pand/
#               ptre and cbse/ccnt/indp/wout). U5: chance as a percent, the
#               OR rule, the AND rule, and counting winning paths. U6: what
#               conditioning does to the denominator, the conditional rate,
#               what independence claims, and drawing without replacement.
#               [[tree]] used for the first time (teach beats only -- it
#               prints every leaf's product).
#   2026-08-23  APP_BUILD -> "2026-08-23lr-two-numbers-at-once". BUILD lr --
#               PROB & STATS UNITS 3 AND 4 (Scatterplots & Correlation;
#               Collecting Data). 228 lessons -> 236, 217 ops -> 225. NOTHING
#               IN THIS FILE CHANGED but this note and the stamp -- the course
#               grew in lessonscripts.py (ops spnt/sslp/resd/sblw and strf/
#               resp/bias/merr, plus three scatter helpers). U3: read one dot,
#               the slope as a rate, residuals, and the line through the
#               cloud. U4: stratified samples, response rate, undercoverage,
#               and four times the people for half the margin. [[scatter]]
#               used for the first time (with fit="true" in teach only -- it
#               prints the line's equation).
#   2026-08-23  APP_BUILD -> "2026-08-23lq-statistics-opens". BUILD lq --
#               ⭐ PROBABILITY & STATISTICS OPENS, THE TENTH COURSE (U1
#               Exploring Data; U2 Describing Distributions). 220 lessons ->
#               228, 209 ops -> 217. NOTHING IN THIS FILE CHANGED but this
#               note and the stamp -- the course grew in lessonscripts.py
#               (ops dotm/dcnt/htot/farv and medv/iqrw/madv/pctl, plus six
#               list helpers). U1 reads the PICTURE: the mode under the
#               tallest stack, a counted slice with a dot on the line, a
#               histogram's bars added, an outlier spotted. U2 puts numbers
#               on the shape: the even-length median, the box plot's middle
#               half, the average distance from the mean, and percentiles.
#               [[histogram]] and [[boxplot]] used for the first time.
#   2026-08-22  APP_BUILD -> "2026-08-22lp-precalc-complete". BUILD lp --
#               ⭐ PRE-CALC COMPLETE (U8 Sequences, Series & the Binomial
#               Theorem; U9 Introduction to Limits). 212 lessons -> 220, 201
#               ops -> 209. NOTHING IN THIS FILE CHANGED but this note and
#               the stamp -- the course grew in lessonscripts.py (ops gsum/
#               sigm/pasc/gser and lsub/lhol/lsid/avgr, plus the _fact/_npr/
#               _ncr helpers). U8: geometric sums, sigma as an instruction,
#               choosing when order does not matter, and an infinite halving
#               series that settles. U9: limits by substitution, the hole,
#               one-sided disagreement, and the average rate of change over a
#               shrinking window -- the derivative, handed to Calculus.
#               NINE COURSES DONE; only Probability & Statistics, Calculus
#               and Differential Equations remain unopened.
#   2026-08-22  APP_BUILD -> "2026-08-22lo-the-work-clothes-and-the-equation".
#               BUILD lo -- PRE-CALC UNITS 6 AND 7 (Applications of
#               Trigonometry; Conic Sections & Parametric Equations). 204
#               lessons -> 212, 193 ops -> 201. NOTHING IN THIS FILE CHANGED
#               but this note and the stamp -- the course grew in
#               lessonscripts.py (ops arsn/ramp/brng/vmag and crad/cctr/elax/
#               parm). U6: area from two sides and the angle, the 30-degree
#               ramp, bearings wrapped past 360, an arrow's length from its
#               steps. U7: un-square the radius, read the center (the sign
#               points opposite), un-square and double for an ellipse's
#               width, and position by time. Two shelved renderers finally
#               used -- [[vector]] and [[conic]] -- both TEACH-ONLY, since
#               each would print or let a child measure the answer.
#   2026-08-22  APP_BUILD -> "2026-08-22ln-the-language-and-the-mirror". BUILD
#               ln -- PRE-CALC UNITS 4 AND 5 (Trigonometric Functions;
#               Analytic Trigonometry). 196 lessons -> 204, 185 ops -> 193.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp --
#               the course grew in lessonscripts.py (ops rad1/nspn/refq/wper
#               and pyid/cofn/negf/sols; period is "wper" because "peri" was
#               already Basic Math's perimeter). U4 deepens alg2-u8: radians
#               in half turns, negative angles named forwards, reference
#               angles hugging the flat line, the period of sin(ax). U5, the
#               identities: one whole split into hundredths, partners across
#               90, the mirror that flips height and never across, and
#               crossings counted per sweep.
#   2026-08-22  APP_BUILD -> "2026-08-22lm-the-shortcut-and-the-layers". BUILD
#               lm -- PRE-CALC UNITS 2 AND 3 (Polynomial & Rational Functions;
#               Exponential & Logarithmic Functions). 188 lessons -> 196, 177
#               ops -> 185. NOTHING IN THIS FILE CHANGED but this note and the
#               stamp -- the course grew in lessonscripts.py (ops negp/remt/
#               vprd/vasy and logp/lsol/hcnt/cmpd). U2: the minus parade, the
#               Remainder Theorem as the plug-in shortcut (named on the board;
#               the speech says "left over" -- "remainder" contains the banned
#               "remain"), Vieta's product (lh's planted promise, paid), and
#               forbidden x's counted from factored bottoms. U3: the power
#               rule brings the exponent down front, log equations solved by
#               stacking the base, halvings counted backwards (hlfl's mirror),
#               and money that doubles beating steady adding.
#   2026-08-22  APP_BUILD -> "2026-08-22ll-algebra-two-complete". BUILD ll -- ⭐
#               ALGEBRA II COMPLETE (U9 Statistics & Probability: weighted means,
#               three slots, expected value, sampling) and ⭐ PRE-CALC OPENS (U1
#               Functions & Their Graphs: composition, the graph-slides rule,
#               domain, piecewise). 180 lessons -> 188, 169 ops -> 177. NOTHING
#               IN THIS FILE CHANGED but this note and the stamp -- the course
#               grew in lessonscripts.py (ops wavg/cnt3/expv/samp and
#               fcmp/fshf/fdom/fpie). Eight courses done, Pre-Calc the ninth
#               underway; only Probability & Statistics, Calculus and
#               Differential Equations remain unopened.
#   2026-08-22  APP_BUILD -> "2026-08-22lk-the-ride-and-the-circle". BUILD lk --
#               ALGEBRA II UNITS 7 AND 8 (Sequences & Series; Trigonometric
#               Functions). 172 lessons -> 180, 161 ops -> 169. NOTHING IN THIS
#               FILE CHANGED but this note and the stamp -- the course grew in
#               lessonscripts.py (ops anth/gnth/gaus/reca and sinp/cosp/spin/
#               ampl). U7: ride the pattern (the off-by-one), times again,
#               Gauss's pairing (the child gets to BE Gauss at n=100), walk the
#               rule. U8: the circle of size one -- sine as height, cosine as
#               across, coterminal spins, amplitude. [[unitcircle]] drawn by
#               scripted lessons for the first time (teach boards only -- it
#               prints the answers); the non-stats renderer shelf is now fully
#               walked. One unit left in Algebra II: U9.
#   2026-08-22  APP_BUILD -> "2026-08-22lj-the-root-and-the-hidden-exponent".
#               BUILD lj -- ALGEBRA II UNITS 5 AND 6 (Radicals & Rational
#               Exponents; Exponential & Logarithmic Functions). 164 lessons ->
#               172, 153 ops -> 161. NOTHING IN THIS FILE CHANGED but this note
#               and the stamp -- the course grew in lessonscripts.py (ops
#               rmul/rpow/rsq/rbet and hlfl/logb/logm/lbet). U5: a root, never a
#               halving. U6: decay's linear faller, the logarithm as the hidden
#               exponent, logs add, and estimation between the powers.
#   2026-08-22  APP_BUILD -> "2026-08-22li-the-degree-and-the-divide". BUILD li --
#               ALGEBRA II UNITS 3 AND 4 (Polynomial Functions; Rational
#               Expressions & Functions). 156 lessons -> 164, 145 ops -> 153.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp -- the
#               course grew in lessonscripts.py (ops pdeg/turnc/rsum3/pval and
#               rdiv/rsol/excl/rasy). U3: what the degree promises -- adds under
#               times, caps the wiggles, three crossings together, and x³ is not
#               3x. U4: division becomes a function -- a/x both directions, the
#               forbidden x, and the survivor at the far horizon.
#   2026-08-22  APP_BUILD -> "2026-08-22lh-algebra-two-opens". BUILD lh -- ⭐
#               ALGEBRA II OPENS (U1 Foundations & Systems; U2 Quadratic Functions
#               & Complex Numbers). 148 lessons -> 156, 137 ops -> 145. NOTHING IN
#               THIS FILE CHANGED but this note and the stamp -- the course grew
#               in lessonscripts.py (ops absv/absc/el2/sys3 and
#               vtx2/rsum/disc/imag). U1: absolute value as distance, elimination
#               that leaves a pair, three unknowns two at a time. U2: the
#               quadratic's secrets unsolved -- where it turns, both roots
#               together, the discriminant's sign (the first 0/1/2 judgment ask),
#               and i arrives.
#   2026-08-22  APP_BUILD -> "2026-08-22lg-geometry-complete". BUILD lg -- GEOMETRY
#               UNITS 8 AND 9 (Area, Surface Area & Volume; Probability). ⭐
#               GEOMETRY IS COMPLETE: nine units, 36 lessons, the sixth finished
#               course. 140 lessons -> 148, 129 ops -> 137. NOTHING IN THIS FILE
#               CHANGED but this note and the stamp -- the course grew in
#               lessonscripts.py (ops para/lshp/surf/svol and poft/notp/outc/twop).
#               U8 ends on the k³ volume capstone of U4's scaling story; U9 is
#               chance in child numbers, closing on the two-way table ([[twoway]]
#               drawn by a scripted lesson for the first time; [[tree]] stays on
#               the shelf -- it prints its leaf products, unusable on asks).
#               Next: Algebra II.
#   2026-08-22  APP_BUILD -> "2026-08-22lf-the-rim-and-the-grid". BUILD lf --
#               GEOMETRY UNITS 6 AND 7 (Circles; Coordinate Geometry). 132 lessons
#               -> 140, 121 ops -> 129. NOTHING IN THIS FILE CHANGED but this note
#               and the stamp -- the course grew in lessonscripts.py (ops
#               cent/insc/iarc/alen and vseg/dist/mid2/corn). U6: the whole is 360
#               against the straight-line habit, the inscribed angle both
#               directions ([[circle inscribed=]] drawn by scripted lessons for the
#               first time, on the angle-to-arc side only -- its auto-label is the
#               given there and the answer the other way), arc length on the
#               shaded pie. U7: the grid -- fencepost, taxicab-vs-straight,
#               2D midpoint, the fourth corner.
#   2026-08-22  APP_BUILD -> "2026-08-22le-the-scale-and-the-climb". BUILD le --
#               GEOMETRY UNITS 4 AND 5 (Similarity & Dilations; Right Triangles &
#               Trigonometry). 124 lessons -> 132, 113 ops -> 121. NOTHING IN THIS
#               FILE CHANGED but this note and the stamp -- the course grew in
#               lessonscripts.py (ops scal/sfac/mside/sare and pyth/leg/tang/topp).
#               U4 is the times-never-add thread closed by the k² area surprise;
#               U5 is Pythagoras both directions on whole triples, then the tangent
#               as the climb inside a triangle. [[righttriangle]] draws its first
#               scripted lessons (teach/worked + tangent asks only -- it always
#               labels the hypotenuse, so it never carries a Pythagorean ask).
#               New audio if rendered now: 720 unique lines / ~75k chars (~20 MB);
#               course total after le ≈ 930k chars ≈ 949 MB projected -- the 2500
#               cap holds it with room.
#   2026-08-22  APP_BUILD -> "2026-08-22ld-the-shape-moves". BUILD ld -- GEOMETRY
#               UNITS 2 AND 3 (Transformations & Symmetry; Congruence & Triangle
#               Proofs). 116 lessons -> 124, 105 ops -> 113. NOTHING IN THIS FILE
#               CHANGED but this note and the stamp -- the course grew in
#               lessonscripts.py (ops tran/refl/htrn/rota and cong/isos/extr/chas).
#               U2 is the three moves with one coordinate rule each (slide adds,
#               flip changes one sign, half turn changes both) closed by turn
#               symmetry; U3 is matching-by-letters congruence, the isosceles pair
#               read both directions, and the exterior angle as the course's first
#               proof. New audio if rendered now: 695 unique lines / ~82k chars
#               (~22 MB) -- the 2500 cache cap holds it with room (course total
#               after ld ≈ 856k chars ≈ 873 MB projected).
#   2026-08-22  APP_BUILD -> "2026-08-22lc-geometry-opens". BUILD lc -- ⭐ ALGEBRA I
#               COMPLETE (U9 Data & Statistics) and ⭐ GEOMETRY OPENS (U1 Foundations
#               & Constructions). 108 lessons -> 116, 97 ops -> 105. NOTHING IN THIS
#               FILE CHANGED but this note and the stamp.
#               U9 finishes the renderer shelf -- [[dotplot]] and [[bars]] draw for a
#               scripted lesson for the first time -- and builds to the one idea that
#               matters: one unusual number drags the mean and leaves the median
#               standing. Geometry U1 lays its vocabulary with figures rather than
#               definitions. Four courses done: Entry, Basic, Prealgebra, Algebra I.
#   2026-08-22  APP_BUILD -> "2026-08-22lb-the-cache-can-keep-it". BUILD lb -- Jim:
#               "check the scripted course audio ... it keeps running and running, and
#               I'm not sure it's caching what it's processing."
#               IT WAS CACHING. THEN THE EVICTOR WAS DELETING IT. The voice cache caps
#               at TTS_CACHE_MAX_MB (default 300 MB) and the scripted course had grown
#               to 9,829 lines / 696,327 characters -- about 711 MB of audio, 2.4x the
#               cap. Every render pushed the cache over, the evictor culled it back to
#               80% of cap (240 MB) taking course audio with it, and the next check
#               reported thousands of lines missing again. Paid for, deleted, re-billed.
#               Reproduced locally before any claim was made: with a cap below the
#               course, three rounds each paid for 810 lines and kept 335.
#               THE COURSE CROSSED THE CAP AT BUILD ko (pre-u5-times-by-ten). Every
#               render since then has been partly burning money.
#               WHAT WAS ALREADY THERE AND USELESS: build ke computed the projection
#               (used/cap/projected/fits) and returned it on every dry run. Build kl
#               labelled every button FREE or SPENDS. Build kq made the render a
#               watchable job. NONE OF THEM EVER REFUSED, and admin.html never printed
#               the disk block -- one unread field, and the symptom stayed invisible
#               through six builds while the course quietly outgrew its shelf.
#               THE FIX: the render is REFUSED with a 409 when the projection does not
#               fit, and the refusal names the env var AND the number to set. A
#               deliberate over_cap_ok overrides it (the admin page re-arms the button
#               for one second click, the same two-click money pattern kl gave the
#               per-lesson re-render, lapsing after 20s). The FREE check now always
#               prints the cache line. dry_run, and any render that fits, are
#               untouched. Battery part 3dd, 12 pins.
#               FOR JIM: set TTS_CACHE_MAX_MB=900 in Render -> Environment, and raise
#               the mounted disk (render.yaml documents 1 GB at /var/data, shared with
#               the nightly DB snapshots) to 2 GB before rendering the whole course.
#   2026-08-22  APP_BUILD -> "2026-08-22la-rooms-and-curves". BUILD la -- Algebra I
#               Units 7 AND 8 in one build, per Jim's pacing ruling. 100 lessons ->
#               108, 89 ops -> 97. NOTHING IN THIS FILE CHANGED but this note and
#               the stamp.
#               U7 Polynomials & Factoring: the area model runs backwards -- four
#               rooms, middles add, corner times; factoring as a two-clue detective
#               game; the whole common factor or none; the vanishing middle.
#               U8 Quadratic Functions: the first curve; zero times anything;
#               a square is never negative so the curve has a floor; and the ball
#               comes down, where the square root is an answer before it is a symbol.
#   2026-08-22  APP_BUILD -> "2026-08-22kz-one-hundred-lessons". BUILD kz -- Algebra I
#               Unit 6, Exponents & Exponential Functions. ⭐ 96 lessons -> 100 -- THE
#               COURSE REACHES ONE HUNDRED SCRIPTED LESSONS. 85 ops -> 89. NOTHING IN
#               THIS FILE CHANGED but this note and the stamp.
#               Powers behave: joining piles ADDS the counts, copying a pile TIMES
#               them (taught as a deliberate pair, each the other's wrong tap);
#               b × 10^a carries a digit; and the doubling pond is the first
#               exponential growth, with the linear thinker's answer as the wrong tap.
#   2026-08-22  APP_BUILD -> "2026-08-22ky-two-lines-cross". BUILD ky -- Algebra I
#               Unit 5, Systems of Equations. 92 lessons -> 96, 81 ops -> 85.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp.
#               Two rules true at once: the grapher draws two lines crossing;
#               substitution is "swap y for what it equals"; the sum-and-difference
#               puzzle; elimination as two shopping trips where the eraser vanishes.
#               The unit-wide distractor is the OTHER unknown's value -- a system
#               holds two answers, and only one of them is yours.
#   2026-08-22  APP_BUILD -> "2026-08-22kx-the-first-line". BUILD kx -- Algebra I
#               Unit 4, Linear Functions & Graphs. 88 lessons -> 92, 77 ops -> 81.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp.
#               ⭐ [[graph]] draws its first scripted line. A line is the machine's
#               whole table of answers at once; slope is taught from two points as
#               "the climb per step" before any formula; y = ax + b is a sentence
#               ("start at b, climb a per step") before it is a formula.
#   2026-08-22  APP_BUILD -> "2026-08-22kw-the-number-machine". BUILD kw -- Algebra I
#               Unit 3, Functions & Notation. 84 lessons -> 88, 73 ops -> 77.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp.
#               ⭐ [[machine]]'s first scripted use -- the last of July's renderers to
#               be picked up. A function is a machine; f(3) is the machine's name and
#               its meal, and the f-times-3 misreading (reasonable, after the
#               distributive lesson taught parentheses as times) is named out loud
#               and offered as the wrong tap.
#   2026-08-22  APP_BUILD -> "2026-08-22kv-the-balance-tips". BUILD kv -- Algebra I
#               Unit 2, Linear Equations & Inequalities. 80 lessons -> 84, 69 ops ->
#               73. NOTHING IN THIS FILE CHANGED but this note and the stamp.
#               Solving begins, drawn on ⭐ [[balance]] -- the balance-scale renderer's
#               first scripted use (same shelf as [[areamodel]] and [[angle split=]]).
#               Undo a plus; undo a times; two steps back in reverse order; and "less
#               than" answered with the biggest allowed whole number, whose wrong tap
#               is the boundary itself.
#   2026-08-22  APP_BUILD -> "2026-08-22ku-algebra-one-opens". BUILD ku -- Algebra I
#               Unit 1, Foundations & Expressions. 76 lessons -> 80, 65 ops -> 69.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp. The ninth
#               course in COURSE_ORDER begins: course key "algebra1", unit names from
#               curriculum.COURSES. Prealgebra U9's four seeds now work together --
#               two-step evaluation, a second letter, collecting past a y, and the
#               minus carried through the parentheses in an [[areamodel]] with a
#               negative room.
#   2026-08-21  APP_BUILD -> "2026-08-21kt-prealgebra-complete". BUILD kt --
#               Prealgebra Unit 9, Variables & Expressions -- THE LAST UNIT.
#               72 lessons -> 76, 61 ops -> 65. PREALGEBRA IS COMPLETE: nine units,
#               35 lessons (Unit 2 has three). NOTHING IN THIS FILE CHANGED but this
#               note and the stamp.
#               ⭐ The distributive property is DRAWN as an area model ([[areamodel]],
#               in the registry since July, first scripted use) -- a rectangle 4 tall
#               and (x + 3) wide cut into a 4x room and a 12 room. The child is shown
#               the two rooms, not handed the rule.
#   2026-08-21  APP_BUILD -> "2026-08-21ks-the-first-figures". BUILD ks -- Prealgebra
#               Unit 8, Measurement & Geometry Basics. 68 lessons -> 72, 57 ops -> 61.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp.
#               ⭐ The first scripted lessons that draw a real FIGURE. Basic's geometry
#               unit draws none -- every board in it is a [[step]] line -- while
#               geo-figures.js has carried [[triangle]] and [[angle]] since July. The
#               straight-line lesson finally uses [[angle deg="180" split="130"]], the
#               tag added on 2026-08-01 for exactly that sentence and never used by a
#               scripted lesson until now.
#   2026-08-21  APP_BUILD -> "2026-08-21kr-percents". BUILD kr -- Prealgebra Unit 7,
#               Percents. 64 lessons -> 68, 53 ops -> 57. NOTHING IN THIS FILE CHANGED
#               but this note and the stamp; the work is in lessonscripts.py.
#               Basic's percent lesson only does 10/25/50 through a fraction shortcut
#               that says nothing about 30 or 70 percent. U7 replaces it with one
#               method that never runs out -- find ten percent, count the tens -- and
#               runs it forwards, as a reading of one number against another,
#               backwards from a part to the whole, and up and down on a price.
#   2026-08-21  APP_BUILD -> "2026-08-21kq-the-render-is-a-job". BUILD kq -- Jim:
#               "I keep getting failure notice on the script rendering." The notice
#               read "Request failed.", which is admin.html's fallback for a non-2xx
#               with no JSON detail -- and the cause was never in the rendering.
#               script-prewarm rendered every missing line SERIALLY INSIDE THE HTTP
#               REQUEST. A whole course is hundreds of ElevenLabs calls, so the browser
#               had to hold one connection open for minutes; Render's proxy cuts a
#               request that long, and a redeploy kills it outright ("Waiting for
#               connections to close" appears three times in the log Jim pasted, each
#               one landing on an in-flight render). The page then reported failure
#               over work that was very possibly half done, and threw away the HTTP
#               status code -- the one number that would have said which it was.
#               THE FIX, three parts:
#                 (1) the render moved to a background thread. The POST returns in
#                     MILLISECONDS (measured: 8ms for a 62-line job) with a job id.
#                     The render loop itself is unchanged, line for line.
#                 (2) ONE LOCK, process-wide, in _prewarm_start -- the only door.
#                     A second render while one is running is refused with a 409 that
#                     says why. TWO OVERLAPPING JOBS PAYING TWICE FOR THE SAME LINES IS
#                     WHAT EMPTIED THE ELEVENLABS CREDITS; nothing prevented it before.
#                 (3) the job's progress is written to disk as it goes, and a record
#                     still marked "running" at boot is recovered as INTERRUPTED. A job
#                     killed by a deploy can finally say so, and say how far it got.
#               dry_run is untouched: free, synchronous, same request -- every existing
#               battery pin on this endpoint exercises that path and still passes.
#               NEW POST /api/admin/script-prewarm-status. admin.html now starts and
#               POLLS both SPENDS buttons, keeps the HTTP status in its error text, and
#               reports an interrupted job on load. Battery part 3dc, 18 new pins.
#               NOTE FOR NEXT TIME: tempfile had to be hoisted to the top import block.
#               _prewarm_recover_record() runs at import time, which is EARLIER than
#               the old `import tempfile` 3,000 lines down -- the recovery path, the
#               one that must never fail quietly, would have raised NameError.
#   2026-08-21  APP_BUILD -> "2026-08-21kp-ratios-and-rates". BUILD kp -- Prealgebra
#               Unit 6, Ratios, Rates & Proportions. 60 lessons -> 64. NOTHING IN THIS
#               FILE CHANGED but this note and the stamp; the work is in
#               lessonscripts.py.
#               Basic Math's "one costs" already finds a unit PRICE. These four are the
#               family around it, in dependency order: keep a ratio's shape when both
#               sides grow, scale a rate over time, write that move as an equation with
#               a hole in it, and split an amount in a ratio -- the genuinely different
#               one, because there the TOTAL is given and the parts must be counted
#               first. The whole unit is aimed at one error: adding instead of timesing
#               (2 to 3 grown to 4 becoming "4 to 5"), and three of the four lessons
#               offer exactly that as their wrong tap.
#               The validator co-authored again: it rejected "makes" (banned speech,
#               canon is "equals") so the machine now FILLS bottles; it caught "gives
#               you" and "is the same as"; it demanded "per hour" and "proportion" be
#               said out loud (rule 14); and it found a share of ONE part colliding with
#               the size of one part, which tightened shr's check to require three
#               different tap options and moved 1-to-3 out of the bank.
#   2026-08-21  APP_BUILD -> "2026-08-21ko-decimals-by-place". BUILD ko -- Prealgebra
#               Unit 5, Decimals. 56 lessons -> 60. NOTHING IN THIS FILE CHANGED but
#               this note and the stamp; the work is in lessonscripts.py.
#               Basic NAMES tenths and hundredths; U5 goes to the thing that actually
#               goes wrong -- PLACE. Comparing two decimals is really converting both to
#               a common unit, so lesson 1 counts hundredths and the "more digits means
#               bigger" misconception dies where it lives: 0.5 is FIFTY hundredths and
#               0.45 is forty-five, drawn on one number line.
#   2026-08-21  APP_BUILD -> "2026-08-21kn-fractions-go-further". BUILD kn -- Prealgebra
#               Unit 4, Fractions. 52 lessons -> 56. NOTHING IN THIS FILE CHANGED but
#               this note and the stamp; the work is in lessonscripts.py.
#               Basic Math takes fractions as far as adding and taking them away, and
#               its "fraction of a group" only ever asks a UNIT fraction ("one half of
#               4"). U4 goes past that: a NON-unit fraction of a number, how many parts
#               fit inside a whole, dividing BY a fraction, and reading a fraction
#               bigger than one. Every answer is a whole number because a tap answer has
#               to be -- a real constraint that was allowed to shape the questions
#               rather than be worked around.
#   2026-08-21  APP_BUILD -> "2026-08-21km-integers-arrive". BUILD km -- Prealgebra
#               Units 2 and 3. 45 lessons -> 52. NOTHING IN THIS FILE CHANGED but this
#               note and the stamp; the work is in lessonscripts.py.
#               U2 (factors, the smallest factor, breaking into primes) goes UNDERNEATH
#               Basic's GCF/LCM. U3 (counting back past zero, adding a negative, taking
#               away a negative, times with a negative) is THE FIRST UNIT WHOSE ANSWERS
#               GO BELOW ZERO, and it needed the validator extended three times --
#               every one an assumption that was TRUE through Basic Math and false the
#               moment integers arrive: answers were required to be >= 1; the tap-option
#               parser was r"\d+", which cannot see a minus sign; and options were
#               required to be >= 1 too. A lesson now declares min_value and the guards
#               stay on for the other 45.
#               Also recorded: an upper bound on tap options was tried and REVERTED --
#               six shipped lessons said at once that a neighbour distractor one step
#               past max_value is normal (Counting to 10 offers 9 | 10 | 11), and they
#               were right.
#   2026-08-21  APP_BUILD -> "2026-08-21kl-the-money-buttons". BUILD kl -- Jim, before
#               pressing anything: "I re render the audio. It doesn't charge me for ones
#               that it's already done. Is that correct?" The answer was "it depends
#               which button", and NOTHING ON SCREEN SAID SO. script-prewarm without
#               force skips cached lines free; with force it re-renders and bills for
#               every line including good ones (which is the whole point -- a cache hit
#               otherwise never re-renders). Two buttons, opposite money behaviour,
#               near-identical labels. NOTHING IN THIS FILE CHANGED but this note and
#               the stamp; the work is in static/admin.html. Every button now says FREE
#               or SPENDS, the paying ones are tinted amber, and the forced re-render
#               is CONFIRMED: with "Whole course" picked it could bill ~4,200 lines
#               (~$90) on one click, so it now prices the job for free first and
#               rewrites itself to name the real number before it can spend.
#   2026-08-21  APP_BUILD -> "2026-08-21kk-prealgebra-unit-one". BUILD kk -- the first
#               new COURSE of the content push: Prealgebra Unit 1, Number Sense & Order
#               of Operations. Four lessons (times before add; parentheses first;
#               exponents are repeated times; power, then times, then add) and four new
#               ops in lessonscripts. 41 lessons -> 45.
#               THIS FILE: /api/script/lessons no longer hand-types the course titles.
#               The map held exactly TWO entries, so the moment a third course existed
#               the picker would have shown the raw id "prealgebra" as a heading. It now
#               derives from curriculum.COURSES, which already has all ten.
#   2026-08-21  APP_BUILD -> "2026-08-21kj-the-real-board". BUILD kj -- the content push
#               begins. Jim: "I wanna get the script done. I wanna get the problem bases
#               done. I wanna get the teaching methodology done ... I wanna go through
#               all the courses."
#               THE MEASUREMENT THAT SET THE ORDER: lessonscripts declares
#               LEVELS = (abstract, pictorial, concrete), the pedagogy from the
#               2026-08-20 research ruling. What ships is 35 lessons ABSTRACT, 1
#               CONCRETE, ZERO PICTORIAL -- 35 of 41 draw no picture at all, because
#               pilot.html could render exactly four tags. Perimeter, area, volume,
#               fractions on a number line and quarter turns are taught with sentences
#               and equations. The methodology was not being delivered.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp; the work is in
#               static/ (new board.css, pilot.html now loads board.js + the figure
#               libraries and dispatches ~24 tags instead of 4). Recorded here because
#               /health is how a deploy is confirmed.
#               The remaining eight courses are ~200 lessons; authoring them against a
#               four-tag renderer would have meant writing algebra and calculus with no
#               graphs and re-authoring later. tags.py already held the 35-tag registry
#               and validate() already accepted board_tag_names -- the grammar and the
#               renderers both existed; only the wiring was missing.
#   2026-08-21  APP_BUILD -> "2026-08-21ki-one-voice-layer". BUILD ki -- kh MEASURED
#               the renders and cleared them: fitting voice length against text length
#               over Counting to 10 gave an intercept of +16ms (a chopped head would be
#               about -500ms), zero clips starting under 20ms, and a slope implying the
#               voice runs 216 wpm against the 156 wpm the yardstick assumed -- which is
#               the whole of the "75%". THE RENDERS ARE COMPLETE. The first word is lost
#               in PLAYBACK. Jim also placed the regression: it was fine early on, and
#               broke around the time the course was prewarmed -- consistent, because
#               streamed clips took seconds to arrive and gave the output device time to
#               wake, while a cached clip starts in ~50ms.
#               NOTHING IN THIS FILE CHANGED but this note and the stamp. The fix is in
#               static/pilot.html: it no longer HAS a voice layer, it loads voice.js.
#               kg hand-ported three of voice.js's four protections and still missed the
#               live AudioContext; that was the fourth hand-port in a row to be wrong,
#               which is the real finding -- hand-porting a voice layer does not
#               converge. voice.js documents an AMBIENT CONTRACT (CODE, forSpeech,
#               setState) and the pilot page now satisfies it, with forSpeech kept as
#               the IDENTITY on purpose: this file's TTS cache is keyed on VERBATIM
#               text, so a transform would miss all 3,879 cached lines and re-render the
#               course at full price.
#   2026-08-21  APP_BUILD -> "2026-08-21kh-measure-the-clip". BUILD kh -- Jim after kg:
#               the four-star GARBLE is gone (the quality model fixed it, so kf was
#               right about the model), but "it's still missing the first couple of
#               words in each" -- with kg deployed, confirmed on /health.
#               STOP. voice.js's build jb comment says this was chased FOUR times on
#               the main app -- "bl: lead silence; cb: the keep-alive loop; gn: the
#               resume race" -- and records that jb finally PROVED THE DELIVERY PATH
#               INNOCENT by measurement: the leading silence really is ~1,254ms decoded
#               in Chrome, the silence-to-voice seam is lossless, the head probe reports
#               currentTime=0.000 every clip. Its conclusion: "That leaves exactly one
#               unmeasured link: what ElevenLabs actually renders." kg was the FIFTH
#               reasoned fix. This build stops reasoning and measures.
#               ALSO A BLIND SPOT IN kf's AUDIT, admitted here: it flags clips that
#               deviate from the COURSE'S OWN MEDIAN seconds-per-character. That is the
#               right yardstick for one odd clip and the WRONG one for a uniform
#               defect -- if every render is short at the head, the median moves with
#               them and nothing looks like an outlier. A self-calibrating detector is
#               blind to exactly the failure Jim is describing.
#               THIS FILE: NEW POST /api/admin/clip-bytes returns ONE cached clip
#               (base64) plus its text, by lesson and index. That lets the admin page
#               decode the REAL audio in the browser -- the only place with an mp3
#               decoder we can reach -- and measure where sound actually starts and how
#               much VOICE a clip contains, against an ABSOLUTE expectation from its
#               word count rather than against its neighbours. Reads only; serves
#               nothing that is not already in the cache; admin-gated because it is
#               lesson audio, and capped so it can never become a bulk exfiltration
#               route.
#   2026-08-21  APP_BUILD -> "2026-08-21kg-the-route-stays-awake". BUILD kg -- Jim,
#               playtesting kf: "the first one or two words of every single spoken
#               word or paragraph was cut off." NOTHING IN THIS FILE CHANGED but this
#               note and the build stamp; the whole fix is in static/pilot.html, and
#               it is recorded here because /health is how a deploy is confirmed.
#               THE FINDING: pilot.html carried NONE of the head-of-clip protections
#               voice.js has had since builds bl/cb/gn, whose own comment describes
#               Jim's report exactly -- audio codecs power down after a few seconds of
#               silence and swallow the first ~200-400ms of the next sound waking up.
#               The pilot page built a NEW Audio() per beat (handing the route back to
#               the OS between clips), had no keep-alive, never warmed the pipeline on
#               the tap gesture build ka already gave it, and asked /api/speak for
#               lead=0 -- the MINIMUM, less leading silence than the main app gives any
#               clip. All four are ported, kept identical to voice.js so they cannot
#               drift. "Self-contained ON PURPOSE" had quietly come to mean re-deriving
#               the voice layer without the fixes already paid for in debugging.
#               NOTE the lead ladder uses THIS file's existing /api/speak `lead`
#               parameter (0-4 blocks of ~280ms), which was already built and which
#               only session.html was using.
#   2026-08-21  APP_BUILD -> "2026-08-21kf-the-right-voice". BUILD kf -- Jim, after
#               the whole course was prewarmed and the ke repair found ZERO damaged
#               clips: "Still garbled when counting four stars." Asked what he hears,
#               he reported the RIGHT WORDS with BAD AUDIO. That rules out the cache
#               (0 damaged of 4,306, 93.7% detector coverage), rules out the ke valve
#               (every line is cached now, and cached clips always took the sound
#               Content-Length path), and points at the RENDER ITSELF.
#               THE DESIGN MISTAKE UNDERNEATH IT: the whole scripted course was
#               rendered with ELEVEN_MODEL = "eleven_flash_v2_5" -- the LOW-LATENCY
#               model, chosen when audio was generated live mid-conversation and
#               ~75ms mattered more than fidelity. Since the 2026-08-20 pivot the
#               scripted lane is PRE-RENDERED: latency is irrelevant, the clip is
#               made once and replayed from cache forever. ElevenLabs sells Flash at
#               half price precisely because it trades quality for speed, and names
#               Multilingual v2 as the narration model. We were paying a permanent
#               quality tax for a speed benefit this lane no longer uses.
#               THIS FILE:
#                 (1) SCRIPT_TTS_MODEL -- the scripted lane's own model. DEFAULT IS
#                     EMPTY, meaning "same as ELEVEN_MODEL", so this build changes
#                     NOTHING until Jim sets it in Render. When set, any line in the
#                     scripted closure renders AND KEYS on that model while the live
#                     conversational lane stays on Flash, where latency is real.
#                 (2) _tts_model_for(text) is the ONE place that decides. The cache
#                     path, the streaming render and the prewarm all call it, so a
#                     clip can never be written under one model's key and looked up
#                     under another's -- which would silently re-render (and re-bill)
#                     the entire course on every play.
#                 (3) script-prewarm gains `lesson` and `force`: re-render ONE
#                     lesson, over the top of cached clips. That is what makes the
#                     model switch testable for pennies (Counting to 10 is 62 lines)
#                     instead of ~$86 for the whole course, sight unheard.
#                 (4) NEW POST /api/admin/course-audio-audit -- walks the CLOSURE, so
#                     it knows the TEXT behind every clip and can report offending
#                     LINES rather than hashes. Flags clips whose MPEG format is not
#                     the canonical 44100/mono/128k (those glitch when the leading
#                     silence is concatenated) and clips whose duration is a wild
#                     outlier against the MEDIAN seconds-per-character of the course
#                     itself -- self-calibrating, no guessed speaking rate. Free,
#                     non-destructive, and it answers "one bad clip or five hundred?"
#                     without anyone listening to 3,879 lines.
#               Reviews/quizzes/exams stay DEFERRED by Jim's ruling.
#   2026-08-21  APP_BUILD -> "2026-08-21ke-the-voice-repair". BUILD ke -- Jim's kd
#               playtest: "several of the lessons have the voice slurring and
#               speaking nonsense", heard while the audio prewarm was running.
#               ROOT CAUSE, and it was not missing audio (a missing clip is SILENT
#               here -- pilot.html has no browser-voice fallback): all THREE cache
#               writers built their temp file from the text itself --
#               `tmp = path.with_suffix(".part")` -- so the temp name was a pure
#               function of the line. Render the same line from two places at once
#               (the prewarm loop AND a child's playback, which is exactly what Jim
#               was doing) and both writers open that ONE path with mode "wb". One
#               truncates what the other is writing; one renames a half-written file
#               into place as a valid cache entry; the loser keeps writing into the
#               renamed inode -- which IS the served cache file. The result is two
#               different renders spliced together, cached, and replayed forever.
#               That is what "melted / underwater" sounds like. THIS FILE:
#                 (1) _tts_cache_store() is now the ONE way a clip enters the cache.
#                     Every writer gets its OWN temp file (tempfile.mkstemp in the
#                     cache dir), so two writers can never share a path; the rename
#                     is atomic, last-writer-wins, and BOTH files are complete.
#                 (2) Nothing is cached until it VALIDATES -- mp3_is_intact() walks
#                     the MPEG frame chain end to end AND cross-checks the Xing/Info
#                     header's declared byte count. The walk alone is not enough:
#                     ElevenLabs renders constant-bitrate mp3_44100_128, so spliced
#                     clips stay frame-aligned and walk clean. The byte count is what
#                     catches them. Error bodies (JSON/HTML), truncation, zero fill
#                     and appended junk are all caught too.
#                 (3) NEW POST /api/admin/tts-cache-repair -- scans the cache, deletes
#                     every clip that fails validation plus any stray .part files, and
#                     reports honestly how many clips carry an Xing header (the
#                     detector's real coverage). dry_run lists without deleting.
#                     Deleted clips simply re-render on next play, at normal cost.
#                 (4) _evict_tts_cache() no longer culls the scripted course. It
#                     evicted OLDEST-FIRST by mtime, and after a whole-course prewarm
#                     the oldest clips ARE the course -- lesson one first. It now
#                     spends the generated-lane clips before ever touching a line the
#                     scripted closure needs, and says so in the log when it must.
#                 (5) script-prewarm calls the evictor when it finishes (it never did,
#                     so it could silently overrun the 300 MB cap) and its dry_run now
#                     reports projected bytes against the cap, so the render is priced
#                     in DISK as well as dollars before Jim spends either.
#               Reviews/quizzes/exams stay DEFERRED by Jim's ruling.
#   2026-08-21  APP_BUILD -> "2026-08-21kd-the-content-sweep". BUILD kd -- ten new
#               lessons close the audit's remaining named gaps (Entry counting,
#               before/after, story problems, coins; Basic story problems, LCM,
#               different-bottom fractions, hundredths, quarter turns, volume) --
#               41 lessons across the two courses. THIS FILE: /api/script/start now
#               returns the lesson's id alongside its topic, so the pilot page can
#               offer "Next lesson" from the course order when a lesson ends.
#               Reviews/quizzes/exams stay DEFERRED by Jim's ruling ("my priority
#               right now is to get the app up and running").
#   2026-08-21  APP_BUILD -> "2026-08-21kc-the-recut". BUILD kc -- Jim approved the
#               Eureka audit's re-cut: the first eight scripted lessons move to
#               ENTRY-LEVEL MATH (units 2-6) where his own curriculum places them;
#               Basic Math gets its real Unit 1 (place value to 1,000, rounding to
#               tens and hundreds, interleaved multi-digit review) plus the audit's
#               two biggest holes -- multiplying/dividing two-digit numbers (Eureka
#               G4-M3, 43 days, previously zero lessons) and fractions ON the number
#               line (Eureka G3-M5's core idea). 31 lessons across TWO courses now;
#               /api/script/lessons carries course + course_title so the picker can
#               group honestly. lessonscripts.py + static/pilot.html + ruletests.py.
#   2026-08-21  APP_BUILD -> "2026-08-21jz-all-nine-units". BUILD jz -- THE COURSE
#               CROSSES ALL NINE UNITS (lessonscripts.py + ruletests.py; this file for
#               the stamp). Seventeen new lessons on a data-driven op registry:
#               regrouping (jr's "too small"/"regroup" canon, "borrow" banned),
#               multiplication, division, left-overs, missing factors, GCF, fractions
#               of a group, equivalent fractions, same-bottom fraction add/take-away,
#               tenths, dimes-and-pennies, percent, unit price, perimeter, area.
#               24 lessons, 3,054 authoring checks, ~$28 of audio for the whole
#               course. COURSE_ORDER now owns the sequence (fixes jy's carrying-
#               before-no-carry ordering) and the module refuses to import if it
#               disagrees with the lesson list. The validator caught EIGHT of my own
#               authoring errors on first run (bad ramps, duplicate problems, symbols
#               never taught) -- the factory working exactly as designed.
#   2026-08-21  APP_BUILD -> "2026-08-21jy-carrying-comes-home". BUILD jy -- lesson 7,
#               "Adding with carrying" (lessonscripts.py + tutor.py + ruletests.py;
#               this file for the stamp). The lesson jr's fight was about: "over nine"
#               is now canon vocabulary, "ten or more" is BANNED from every lesson's
#               closure at build time, the validator requires every bank problem to
#               actually carry, and the intervention prompt teaches with the same
#               words. Seven lessons; whole-course audio ~$11.
#   2026-08-21  APP_BUILD -> "2026-08-21jx-single-digit-said-plainly". BUILD jx --
#               lessonscripts.py + ruletests.py; this file for the stamp. Jim's second
#               wording ruling ("we're adding SINGLE-DIGIT numbers -- one through
#               nine -- that's how I would say it"): the four lessons are renamed by
#               their INPUTS and the validator's new a_max/b_max caps make every bank
#               provably match its name (it caught L2's 10−6 and L4's 20−10 on the
#               spot). NEW lessons 5 (Tens and ones) and 6 (Adding two-digit numbers,
#               no carrying -- validator-enforced, abstract-only levels). The course
#               is now SIX lessons, ~$10 of audio total.
#   2026-08-21  APP_BUILD -> "2026-08-21jw-the-first-four-lessons". BUILD jw -- THE
#               COURSE TAKES SHAPE. lessonscripts.py grows to FOUR verified lessons
#               (adding up to 10 -- reworded to Jim's plain-language ruling: the goal
#               chip says "Adding numbers up to 10" and the script SAYS "every answer
#               will be ten or smaller" -- taking away up to 10, adding up to 20,
#               taking away up to 20). This file: /api/script/start takes a lesson id,
#               NEW GET /api/script/lessons lists the course, and script-prewarm
#               renders the whole course's deduped closure (~$7). tutor.py's
#               intervention prompt learns taking away. pilot.html gains the picker.
#   2026-08-21  APP_BUILD -> "2026-08-21jt-the-script-serves". BUILD jt -- THE SCRIPTED
#               LESSON LANE (Jim's scripted-first ruling, phase 2 server half).
#               NEW: POST /api/script/start + /api/script/answer drive the pure,
#               battery-verified engine in lessonscripts.py; POST /api/admin/
#               script-prewarm renders the pilot's whole audio closure (~$1.66).
#               THREE INVARIANTS, pinned by PART 3cw: no answer ever reaches the
#               client (grading is code, always); the model never steers (bounded
#               Model-Lead-Test turns, code-graded redo, engine-owned return, full
#               fallback to the scripted retest when the model fails); and a script
#               turn costs nothing (kind="script" usage rows carry the wall time, so
#               jm's instrument can prove the pilot's latency claim). tutor.py gains
#               script_intervention (a ~1,600-char prompt vs the lesson lane's
#               ~183,000 -- the latency dividend on the one turn that still thinks).
#   2026-08-20  APP_BUILD -> "2026-08-20jr-one-rule-one-wording". BUILD jr --
#               CONSISTENCY MEMORY (store.py + tutor.py; this file wires the note and
#               carries the stamp). Jim caught it live: "over nine, carry" and, four
#               turns later in the same lesson, "ten or more, carry". The words a
#               student was first taught for a rule now ride THIS TURN'S user message
#               (never the system prompt -- the 71k cached prefix must not move), and a
#               contradiction is a probe rather than a retry, because today's numbers
#               say a turn is 16 seconds and 30% of them already retry.
#   2026-08-20  APP_BUILD -> "2026-08-20jq-what-a-turn-writes". BUILD jq --
#               store.py + tutor.py + static/admin.html + ruletests.py; this file for
#               the stamp. jm and jp took the 16-second turn apart and found 12.3s of it
#               is the teaching model writing ~875 output tokens at a perfectly normal
#               ~71 tokens/second -- so the wait is LENGTH, not the prompt, not the
#               referees (those are ~1s of the whole thing). Rule 19c caps what the
#               child HEARS and that cap is holding, so the rest is board tags and
#               structure -- a ratio nobody had ever measured. jq measures it.
#   2026-08-20  APP_BUILD -> "2026-08-20jp-the-second-opinion-is-visible". BUILD jp --
#               store.py + tutor.py + static/admin.html + ruletests.py; this file for
#               the stamp AND for critic pricing. LIVE_CRITIC=anthropic with
#               LIVE_CRITIC_MODEL=claude-opus-5 is LIVE, so an entire extra model reads
#               every accepted draft -- and it was invisible twice over: its seconds sat
#               in jm's "referees and our own work" bucket, and its tokens were in no
#               figure on the cost card at all (every one filters kind == "brain"; a
#               critic row is kind == "critic"). Now timed (ms_critic) and counted, with
#               its OWN price vars -- CRITIC_IN_USD_PER_MTOK / CRITIC_OUT_USD_PER_MTOK --
#               because Opus is not priced like the teaching model and borrowing those
#               numbers would understate it several times over. Nothing about the
#               critic's behaviour changed: this build only makes it possible to DECIDE.
#   2026-08-20  APP_BUILD -> "2026-08-20jo-the-referee-can-hear-words". BUILD jo --
#               tutor.py + ruletests.py; this file for the stamp. Rule 44's referee
#               could only hear numbers 0-20 and the round tens, so every board problem
#               with a bigger number burned all three attempts and shipped anyway --
#               4.3% of turns, and the largest single cause of the 21 replies that went
#               out WITH a known finding. Found by MEASURING (/admin, build jj's
#               by-name table + build jm's clock), not by reasoning.
#   2026-08-20  APP_BUILD -> "2026-08-20jn-write-it-say-it". BUILD jn -- foundations.py
#               + ruletests.py; this file for the stamp. Jim, from one live precalc
#               lesson: "We write f of x, which is read as f of x." An AUTHORED script,
#               spoken verbatim -- not the model. Writing "f(x)" would NOT have fixed it,
#               because forSpeech() converts f(x) -> "f of x" for the TTS engine, so the
#               naive fix is still a tautology in the ear. The wording now names the
#               notation in words that survive that transform; the board still shows the
#               real f(x). NEW PART 3cq scans every authored script for the shape AS
#               HEARD and fails the naive fix as loudly as the original defect.
#   2026-08-20  APP_BUILD -> "2026-08-20jm-the-turn-clock". BUILD jm -- HOW LONG A
#               TURN TAKES, MEASURED. store.py (usage_log +ms_total/ms_model/ms_retry,
#               additive migration, usage_stats reports median/p90/max plus the model
#               and retry averages), tutor.py (_timed_create_full + _turn_ms, riding the
#               `tokens` dict that already reaches the usage log), static/admin.html
#               (three tiles on the Cost & verifier card). This file changes for the
#               stamp only -- /api/admin/stats returns whatever usage_stats reports, so
#               the new keys need no endpoint change. Step 2 of the 2026-08-20
#               responsiveness proposal, and the prerequisite for every latency claim
#               after it: the extended-thinking test and the pre-hoc corrections work
#               both need a BEFORE number, and until now the only one that existed was
#               Jim counting seconds.
#   2026-08-20  APP_BUILD -> "2026-08-20jl-rule-61-goes-live". BUILD jl -- the
#               THIRTY-SEVENTH referee: an order-of-operations rule spoken as an
#               unconditional law is regenerated (rule 61), from the night watch's only
#               confirmed finding of 2026-08-20. tutor.py + ruletests.py; this file for
#               the stamp. Sequence of the morning, for the record: jj (admin.html,
#               referee fires by name -- static, no stamp) and jk (nightwatch.py, the
#               reviewer's second test) were each committed and pushed on their own
#               before this one; jl supersedes jk on /health.
#   2026-08-20  APP_BUILD -> "2026-08-20jk-the-reviewer-gets-a-second-test". BUILD jk --
#               nightwatch.py only (this file changes for the STAMP, so /health can prove
#               the new governor is live). The night watch's reviewer had ONE way to
#               confirm a finding -- "would a child learn something false?" -- which no
#               rule of CONDUCT can pass, so rules 17, 43, 62, 44, 15 and 40 were
#               structurally unconfirmable and the 2026-08-20 report refuted 19 of 20.
#               VERIFY_SYSTEM now judges TRUTH *and* CONDUCT. Full reasoning in
#               nightwatch.py's own note. ⚠️ nightwatch.py is NOT in ruletests' _STAMP_PY
#               list, so this bump is deliberate, not enforced -- adding it there is a
#               one-line follow-up worth doing.
#   2026-08-19  APP_BUILD -> "2026-08-19ji-cluster-b-merged". BUILD ji --
#               CONSOLIDATION BATCH 2, CLUSTER B. Rules 16 and 17 fold into rule 15
#               as clauses (d) and (e): 16 was literally 15(a) applied to
#               substitution/check questions (its own text said so), 17 is its mirror
#               (the asking reply must not carry the answer). Numbering FROZEN per the
#               rails -- 16 and 17 keep their numbers as one-line pointers, so every
#               referee message and pin citing them stays true. PART 3co pins all six
#               absorbed prescriptions.
#               ⚠️ MEASURED HONESTLY: the merge saved only ~350 chars, NOT the ~3.0K
#               the proposal projected -- that figure was the CLUSTER SIZE (15+16+17 =
#               5,914), not the overlap. The rules are almost all prescription, so
#               merging buys structure, not bytes. Cluster C measures even smaller
#               (22+24 = 1,887 total, ~200 of real overlap) and is NOT worth the churn.
#               If prompt size must come down for latency, the lever is the four
#               biggest rules (63: 5,108 · 61: 4,335 · 19: 4,099 · 49: 3,419), not
#               more merges. Proposal doc updated with the measured numbers.
#   2026-08-19  APP_BUILD -> "2026-08-19jh-the-board-says-where". BUILD jh -- three
#               catches from one resumed lesson on 24368 + 8175. (1) REFEREE 36: the
#               board carried "43" under the line (ones and tens done, HUNDREDS next)
#               and the tutor announced "ten-thousands: 2 + 1 = ?", skipping two
#               columns -- partial= makes the next place OBJECTIVE, so it is now
#               refereed. (2) JIM'S RULING: a half-finished problem is RESTARTED on
#               resume, never resumed mid-column -- the new session's board is EMPTY
#               of that work, and the tutor's memory of which step was next is exactly
#               what goes wrong. (3) The Today's Goal chip vanished on restart while
#               the progress chip restored beside it: showGoal only ever ran from a
#               live [[goal]] tag, so it is now restored from the stored items (which
#               ARE the goal). ALL CODE IS IN tutor.py / prompts.py / session.html;
#               this file only carries the stamp. PART 3cn.
#   2026-08-19  APP_BUILD -> "2026-08-19jg-draw-the-move-whole". BUILD jg -- REFEREE
#               35. Jim, solving 3(x-2)=2x+5: "it put a bubble between those, and the
#               original equation was out of sight up high... it feels like it doesn't
#               understand what is on the screen." THE PROMPT CAUSED IT -- five places
#               said "because the board STACKS, you never re-state the whole solution",
#               which was TRUE when the worklist was one permanent visible column and
#               became FALSE once turns scroll (build ir anchors each new bubble at the
#               TOP, pushing earlier lines off screen). All five rewritten; rule 15(a)
#               -- which reaches ALL TEN courses -- now says the referents must be in
#               THIS VERY REPLY, not "earlier", names the live catch, points at
#               [[solve]] for redrawing a whole chain, and requires a CHECK to be ONE
#               line. orphan_step_conflict rejects an op drawn over a line the reply
#               never wrote. Prompt headroom is now TIGHT (algebra2 184,552/186,000):
#               consolidation Batch 2 is the next thing that buys room. PART 3cm.
#   2026-08-19  APP_BUILD -> "2026-08-19jf-resume-or-not". BUILD jf -- the ONE clip
#               in this whole voice investigation that ever started mid-audio logged
#               currentTime=18.207 after an 8-minute gap, and setPaused() resuming a
#               half-played clip produces exactly that line -- as does a spontaneous
#               restart, which would drop a child's sentence. Opposite diagnoses,
#               identical log. Jim could not recall pressing Pause, so the probe now
#               reports viaResume=true/false: each page stamps lastResumeAt the
#               instant a RESUME asks for playback. Measurement, not memory -- the
#               standing lesson of this whole hunt. ALL CODE IS IN static/voice.js +
#               the three pages' setPaused; this file only carries the stamp. 3ci.
#   2026-08-19  APP_BUILD -> "2026-08-19je-readable-axes". BUILD je -- Jim, on a live
#               statistics lesson: "the number line in this diagram is ridiculous.
#               There is no way that you can read it, and there's plenty of room on
#               the whiteboard to have a bigger number line." A dot plot of homework
#               minutes 20..90 printed a LABEL FOR EVERY INTEGER -- 71 numbers in
#               420px -- an unbroken smear of digits. [[dotplot]] AND [[numberline]]
#               both looped `t++` and labelled every step, so any wide range was
#               unreadable (a 0..100 number line drew 101 labels). Now fitStep picks a
#               human tick (1, 2, 2.5, 5, 10, 20 ...) and WIDENS it until neighbouring
#               labels measurably cannot touch; whole-number data never gets 3.25-style
#               ticks; both figures grew (680 / 660px) and the dot plot's HEIGHT now
#               follows its tallest stack instead of a fixed 200px of mostly blank
#               board. Verified by rendering 8 ranges in Chromium: ZERO overlapping
#               label pairs, and -10..10 still keeps every whole number. ALL CODE IS IN
#               static/math-figures.js; this file only carries the stamp. PART 3cl.
#   2026-08-19  APP_BUILD -> "2026-08-19jd-one-beat-per-turn". BUILD jd -- REFEREE
#               34, measured straight off Jim's [voiceclip] probe: a live turn came
#               back at 126 spoken words = FORTY-SIX SECONDS of unbroken speech at a
#               child ("Mr. Cadabra is very slow today"), and it was a WELCOME-BACK
#               opener that taught nothing new. That is build ja's bill -- ja lifted
#               the 1-3 sentence cap so a new idea could be taught properly, Jim ruled
#               "long, but IN BEATS", and nothing bounded a turn. Now rule 19(c) gives
#               a number (about 80 spoken words a beat, never past 110, one beat per
#               turn ending on a continue-check) and scopes the exemption to TEACHING
#               SOMETHING NEW -- greetings, recaps and reactions stay at 1-3 sentences.
#               spoken_length_conflict enforces it on the SPOKEN prose only, so a
#               tag-heavy turn is never punished for what it draws. RULE_VERIFY[19]
#               COVERED -> ENFORCED. ALSO SETTLED TONIGHT: the [voiceclip] numbers
#               (silence 1263ms as designed, voice at 168-184 wpm) prove the clips are
#               COMPLETE -- the missing-first-words hunt is not a truncation. ALL CODE
#               IS IN tutor.py / prompts.py / ruletests.py (PART 3ck); this file only
#               carries the stamp.
#   2026-08-19  APP_BUILD -> "2026-08-19jc-the-column-redraws". BUILD jc -- Jim,
#               watching a five-digit carrying lesson: "as you complete steps, what
#               you just did disappears off the top of the screen... it would be
#               better if they restated what it looked like -- the three underneath
#               the eight and five in red, and the one carried above the tens column
#               in red." [[column]] gains carries="1_" and partial="43" (both
#               RIGHT-ALIGNED to the ones column, "_" = empty), so the tutor re-emits
#               the same problem after each place and the board REDRAWS IT WHOLE. The
#               page diffs against the last render of that problem and reds only what
#               changed -- the model states where the work stands and cannot get the
#               highlighting wrong. Verified by rendering the real sequence in
#               Chromium: carries land 0px off their columns. Also rule 13(c), his
#               second catch the same lesson: ONE TEST KEEPS ONE WORDING ("greater
#               than nine" and "ten or bigger" are one rule to us and two to a child
#               learning to carry). ALL CODE IS IN static/board.js + the three pages'
#               CSS + prompts.py; this file only carries the stamp. Pinned PART 3cj.
#   2026-08-19  APP_BUILD -> "2026-08-19jb-measure-the-clip". BUILD jb -- Jim's
#               FOURTH report of missing first words. This session ruled the whole
#               delivery path innocent BY MEASUREMENT: the lead silence decodes to
#               ~1,254ms in Chrome's own decoder, the silence-to-voice seam is
#               lossless (a 2,000ms tone came back 2,012ms), his [voicehead] lines
#               show currentTime=0.000 into a running graph on every clip, forSpeech
#               preserves the opening words, stopAllSpeech has ONE call site, and he
#               confirms the missing words ARE in the chat bubble -- and bubble text
#               and spoken text are the same string. ONE link was never measured:
#               what ElevenLabs renders. probeClip (?voiceprobe=1, cache-hit fetch,
#               non-blocking, fails silent) decodes the served bytes and reports the
#               real leading silence, the real voice duration, and what that many
#               words SHOULD take -- so a short render is unmistakable. NO behaviour
#               change: this build only ends the guessing, exactly as gn's probe was
#               meant to. Pinned in ruletests PART 3ci. ALL CODE IS IN
#               static/voice.js; this file only carries the stamp.
#   2026-08-19  APP_BUILD -> "2026-08-19ja-teach-before-you-ask". BUILD ja -- Jim,
#               watching a live entry-level lesson: "it's starting off by asking a
#               question right away... somehow there needs to be more teaching
#               involved... there shouldn't be a limit on how much he teaches."
#               ROOT CAUSE: "Keep almost every reply to 1-3 short sentences. No
#               monologues out loud." lived in all ten courses, and rule 19 -- the
#               teach-first rule -- CONCEDED to it ("your replies stay short"). Told
#               both to demonstrate and to stay to three sentences, the model dropped
#               the demonstration and kept the question. Now: rule 19 is rewritten as
#               TEACH IT BEFORE YOU ASK IT with four beats (say what it is -> work a
#               complete example yourself on the board -> take the length teaching
#               needs, in beats with a continue-check that is NEVER a computation ->
#               hand over with the model still on the board), and all NINETEEN copies
#               of the cap across the ten courses now name the exception. Jim's
#               ruling on pacing: long, but in BEATS -- a forty-second monologue at a
#               six-year-old is not teaching either. Worst normal prompt after this:
#               algebra2 182,187 of 186,000. NEXT (Jim's ruling, not yet built): the
#               saved demo library -- a worked demonstration generated once per
#               topic, refereed, saved, delivered verbatim thereafter. Pinned in
#               ruletests PART 3ch; RULES.md regenerated. ALL CODE IS IN prompts.py /
#               ruletests.py; this file only carries the stamp.
#   2026-08-19  APP_BUILD -> "2026-08-19iz-pipes-are-not-bars". BUILD iz -- the
#               absolute-value phantom is DEAD: iy's line-naming showed the
#               rule-14 referee firing on the pipe separators of option lists
#               ("3/4 | 2/4 | 4/8"), not on real bars -- the unresolvable nudge
#               that haunted every audit since ih, and it skewed the model
#               comparison against arms that used more answer buttons. Pattern
#               now demands non-space inside both bars. Also: the Anthropic
#               live critic is held to JSON by brace prefill (4 wasted checks
#               in one arm). The three-arm test MUST be re-run on this build --
#               all prior arm scores are contaminated. ALL CODE IS IN tutor.py /
#               ruletests.py; this file only carries the stamp.
#   2026-08-19  APP_BUILD -> "2026-08-19iy-request-is-not-an-answer". BUILD iy --
#               two catches from the arm-1 rerun log: referee 33 now enforces
#               only QUANTITATIVE taps (a "Quiz me!" button is a request, not an
#               answer to parrot), and the rule-14 nudge NAMES the exact board
#               line that carries the unread symbol (3-for-3 unresolved even
#               with the ready sentence = the model cannot find the accused
#               line; now it is quoted, and the server log shows it too). ALL
#               CODE IS IN tutor.py / ruletests.py; this file only carries the
#               stamp. NOTE: pushed AFTER the three-arm test completed, so the
#               arms stayed comparable.
#   2026-08-19  APP_BUILD -> "2026-08-19ix-nightwatch-five-closed". BUILD ix --
#               the night watch's first run on the iv build confirmed FIVE
#               findings (2 definition-precision, the pocket-money story, the
#               overgeneralized hole rule, and the undefined-y board line that
#               our OWN rule 14 wording was teaching). All five closed at the
#               rulebook: rule 13 gains (b) FULL-GENERAL-FORM DEFINITIONS,
#               rule 14's function-notation example now defines y FIRST,
#               rule 32 gains (c) MONEY YOU HAVE IS NOT A COST, rule 61's
#               caught-in-real-lessons list grows to TEN with the qualified
#               hole rule. Words first, per the promotion discipline -- the
#               watch re-checks nightly and a repeat earns a referee. Pinned in
#               ruletests PART 3cg; RULES.md regenerated. ALL CODE IS IN
#               prompts.py / ruletests.py; this file only carries the stamp.
#   2026-08-19  APP_BUILD -> "2026-08-19iw-spoken-fraction-counts". BUILD iw --
#               two catches from Jim's FIRST Opus audit run: (1) referee 33
#               false-fired on a tapped "3/4" answered back as "three fourths"
#               (fraction options now match their spoken forms); (2) the audit's
#               report filename ignored CLAUDE_MODEL, so the opus arm overwrote
#               the sonnet arm's report (lineup + filename now carry resolved
#               models). ALL CODE IS IN tutor.py / lessonaudit.py /
#               ruletests.py; this file only carries the stamp.
#   2026-08-19  APP_BUILD -> "2026-08-19iv-second-pair-of-eyes". BUILDS iu + iv --
#               Jim's A/B ruling (challenger: gpt-5.6). iu: the tutor brain is
#               pluggable (TUTOR_PROVIDER env; _OpenAIBrain adapter; default
#               anthropic = byte-identical) and lessonaudit grows the lineup flags
#               --brain / --live-critic / --judge with an Anthropic judge seat, so
#               the A/B runs as four measured arms with per-arm report files.
#               iv: the LIVE CRITIC seat (LIVE_CRITIC env, off by default) -- a
#               second model reads every accepted draft and a confident objection
#               retries through the existing loop; the judgment-mole class caught
#               without a build per mole. NOTHING is switched on by default;
#               production is byte-identical until the env vars are set. ALL CODE
#               IS IN tutor.py / lessonaudit.py / ruletests.py (PART 3cf); this
#               file only carries the stamp.
#   2026-08-19  APP_BUILD -> "2026-08-19it-nudge-says-how". BUILDS is + it -- from
#               Jim's "wtf" screenshot + Render log, same night. is: REFEREE 33,
#               tapped_answer_conflict (rule 18a) -- he tapped "32" answering his
#               own question and the reply graded the lesson's OTHER thread
#               ("Eleven is the answer..."); now a reply to a tapped [[choices]]
#               answer that engages neither their answer nor any option of that
#               question is regenerated. it: the rule-14 notation nudge is
#               PRESCRIPTIVE (5-for-5 unresolved retries, abs-value bars every
#               time -- the fifth in Jim's own log tonight): the referee message
#               now QUOTES the ready sentence to add. ALL CODE IS IN tutor.py /
#               prompts.py / ruletests.py (PART 3ce); this file only carries the
#               stamp.
#   2026-08-19  APP_BUILD -> "2026-08-19ir-turn-starts-at-the-top". BUILDS iq + ir --
#               Jim's board-room pair, same sitting as ip. iq: the TODAY'S GOAL banner
#               and the three progress bars collapse into two small clickable chips
#               ("Today's Goal" / "Today's Progress") that pop open on click -- the
#               panels are the same elements, every render path untouched, the tour
#               still opens the real bars and tucks them back after. ir: every new
#               tutor bubble is placed at the TOP of the visible board (build ax did
#               this only for window-tall turns); history is above, board work fills
#               in below, via a self-shrinking spacer so short turns can reach the
#               top. ALL CODE IS IN static/session.html (iq) and static/board.js
#               (ir, shared by session/topic/practice); this file only carries the
#               stamp. Pinned in ruletests PART 3cd.
#   2026-08-19  APP_BUILD -> "2026-08-19ip-speak-the-primes". BUILD ip -- derivatives
#               are SAID, not improvised (Jim in Differential Equations: y″ spoken as
#               "yuh", y′ sometimes "y" -- inconsistently wrong, because forSpeech had
#               NO rule for prime marks and the TTS engine guessed differently every
#               time). forSpeech now converts ′ ″ ‴ ⁗ and the ASCII/smart-quote forms
#               (y', y'', y") to "prime / double prime / triple prime / quadruple
#               prime" on any standalone letter, with guards so "y'all", "that's",
#               possessives and quoted words are never touched; f′(x) chains to
#               "f prime of x". Twelve new pins in ruletests PART 3. ALL CODE IS IN
#               static/speech-text.js; this file only carries the stamp.
#   2026-08-19  APP_BUILD -> "2026-08-19io-anecdote-diet". BUILD io -- the approved
#               consolidation's Batch 1: every dated citation stripped from the
#               rulebook's prose (stories live in change notes and build records;
#               principles, prescriptions and teaching examples intact).
#               GRAPH_TOOL_NOTE 105,253 -> 101,407. Battery 4,776 green with ONE
#               deliberate anchor update (49f). ALL CODE IS IN prompts.py /
#               ruletests.py; this file only carries the stamp. Next: the merge
#               clusters (Batches 2-3), per the proposal doc.
#   2026-08-19  APP_BUILD -> "2026-08-19in-glow-not-geometry". BUILD in -- the
#               session tour stops pointing with layout words (Jim on a phone: the
#               sidebar stacks below the chat, so "over on the left" pointed at
#               nothing). Glow-anchored wording throughout; welcome card fixed;
#               pinned in PART 3cb. ALL CODE IS IN static/session.html; this file
#               only carries the stamp. (demo.html's identical phrases are
#               pre-rendered clips -- queued, needs a re-render pass.)
#   2026-08-18  APP_BUILD -> "2026-08-18im-stray-word-refuses". BUILD im -- the
#               lessonaudit CLI refuses stray words loudly instead of silently
#               running the default (Jim's 13-minute loss: `prompt-size large`
#               without the dashes ran the DEFAULT size and reported it as the
#               experiment; the two same-config runs it accidentally produced did
#               measure run-to-run noise: 7 vs 6 findings on identical settings).
#               ALL CODE IS IN lessonaudit.py; this file only carries the stamp.
#   2026-08-18  APP_BUILD -> "2026-08-18il-today-earns-its-bar". BUILD il -- THE
#               TODAY BAR MAKES REAL CALLS (Jim's design ruling, same night as his
#               catch: quiz + whole unit completed, Today bar never moved). "Today
#               = how much time did they spend working AND how much progress did
#               they make; the app needs to make some type of call." The bar's
#               advance was model-judgment (wish-tier); the SERVER now makes both
#               calls from facts it holds: _today_match_tick (a recorded quiz/check
#               whose name matches an unfinished item -> COMPLETED tick, called from
#               build hu's writer) and _today_time_tick (every ~15 engaged minutes
#               on the time clock -> a WORKED tick on the first unfinished item,
#               called from the minute beat -- the struggling-hour principle).
#               _ensure_today_ticks appends [[todaydone n kind]] for any server tick
#               the page hasn't seen (net pattern, both chat paths, and the
#               augmented reply is what history remembers). store.today_goals grows
#               the worked notion ("3w" entries, back-compatible); /api/session's
#               today payload carries it; session.html renders worked segments
#               distinctly; prompts teach 10-15-minute item sizing and
#               trust-the-server. Completed outranks worked; nothing un-ticks.
#               PART 3cc.
#   2026-08-18  APP_BUILD -> "2026-08-18ik-tour-once". BUILD ik -- THE TOUR RUNS
#               ONCE, AND IT CAN BE SKIPPED. Jim's live catch as a brand-new
#               student: tour -> placement test -> "start you in unit two, ready?"
#               -> yes -> THE WHOLE INTRODUCTION PLAYED AGAIN. Cause: "toured" was
#               INFERRED (_has_any_history over the classroom group) and the tour
#               writes no history, so his exact path re-armed it. Now the tour is a
#               RECORDED FACT: when __tour_done__/__tour_done_declined__ arrives,
#               store.record_tour_seen(code, _tour_group_key(course)) writes the
#               new tours_seen row BEFORE any model call (a slow opener can never
#               cost a second sit-through), and /api/session's "toured" ORs the
#               recorded fact with the old history inference (pre-ik students never
#               re-tour; a store outage degrades to the old behavior, never worse).
#               tours_seen joins _STUDENT_CODE_TABLES (a reset student is a new
#               student). session.html adds the "Skip the intro" button -- skipping
#               hands off through the SAME __tour_done__ path, so a skipped tour is
#               a seen tour. PART 3cb. (Jim's second catch tonight -- the Today bar
#               showing no progress while a unit completed -- is DIAGNOSED, design
#               conversation queued: the bar's advance is model-judgment, wish-tier;
#               see Session_Summary / the ix-design queue item.)
#   2026-08-18  APP_BUILD -> "2026-08-18ij-work-that-happened". BUILDS ih + ii + ij,
#               THE TIER-B REMAINDER -- referees 30-32 close out the promotion
#               audit's practical list: new board notation is read aloud (rule 14) ·
#               a question is never re-asked word for word (rule 22, fed the
#               previous tutor turn) · a back-reference points only at work this
#               conversation actually held (rule 62, the 2026-08-12 audits' own
#               false-factoring shape). Rule 19 stays deferred by the audit's
#               judgment. Ledger: 14/22/62 -> ENFORCED; the sweep is THIRTY-TWO;
#               ENFORCED rules 31 of 65. ALL CODE IS IN tutor.py / prompts.py; this
#               file only carries the stamp. PARTs 3by/3bz/3ca.
#   2026-08-18  APP_BUILD -> "2026-08-18ig-quiz-vocab-gate". BUILD ig, THE QUIZ
#               VOCABULARY GATE (rule 37's quiz-facing half; the promotion audit's
#               Tier-B flagship). ia generalized to the whole course glossary: a
#               numbered quiz question offering a choice between glossary terms
#               the student was never taught is rejected by tutor's TWENTY-NINTH
#               referee. This file's part: student_context["terms_known"] =
#               _foundations_heard(code, course) -- the [[learned]]-tracked
#               delivered-scripts list, durable across sessions and history caps
#               -- handed to the sweep via meta. Built conservatively (zero
#               [termgap] calibration data; Jim checked the Render log: none yet
#               -- the probe keeps counting either way, and the events table holds
#               90 days). PART 3bx.
#   2026-08-18  APP_BUILD -> "2026-08-18if-stay-in-role". BUILDS id + ie + if, THE
#               PROMOTION BATCH -- the answer to Jim's "we're still in whack-a-mole
#               mode": the promotion audit showed every recent live miss came from
#               the thirty rules held by prompt words alone, so its Tier A (the four
#               promotable with nothing but the reply in hand) stops being wishes
#               tonight. Referees 25-28 in tutor.py: comparisons to other students
#               (rule 42 -- "most kids find this hard" included), a second board
#               spotlight (rule 60c), a substitution/check ask that writes no real
#               equation (rule 16, both 2026-08-07 live catches), and instruction
#               leaks ("my instructions", "rule 47 says", "step tag", "I'm not
#               allowed" -- the Ground Rules' STAY IN ROLE). Ledger: 16/42/60 ->
#               ENFORCED; the sweep is TWENTY-EIGHT. ALL CODE IS IN tutor.py /
#               prompts.py; this file only carries the stamp. PARTs 3bu-3bw.
#   2026-08-18  APP_BUILD -> "2026-08-18ic-quiz-honesty". BUILDS ia + ib + ic, the
#               QUIZ-HONESTY TRIO -- four catches from ONE live quiz run of Jim's,
#               closed the same evening. ia (rule 47e, the TWENTY-THIRD referee):
#               tutor.quiz_term_conflict rejects an acute/right/obtuse quiz choice
#               this conversation never taught; the first referee fed the
#               conversation's own text (tutor._create_verified computes `heard`
#               from the ORIGINAL messages -- never the retry list -- so a rejected
#               draft cannot teach the checker its own vocabulary). ib (rule 47g,
#               the TWENTY-FOURTH): tutor.question_self_contained_conflict rejects a
#               numbered quiz question that states "the vertex ... at Y" and then
#               asks "what is the vertex". ic (rule 47f, words): an angle question
#               draws its angle -- a complement question's picture IS the split
#               right angle ([[angle deg="90" split="62"]]). The fourth catch (the
#               new question's figure appearing while the previous answer is still
#               being narrated) is the KNOWN narration/board timing limitation --
#               tags render on arrival, the voice reads linearly; 47(e)'s
#               teach-in-its-own-turn discipline is the mitigation, and a true
#               narration-synced board reveal stays on the queue as its own build.
#               ALL CODE IS IN tutor.py / prompts.py; this file only carries the
#               stamp. PARTs 3br/3bs/3bt; RULES.md regenerated.
#   2026-08-18  APP_BUILD -> "2026-08-18hz-promised-comparison". THE TWENTY-SECOND
#               REFEREE. Jim's live catch: "here's our angle again, fifty degrees,
#               next to a right angle for comparison" -- over a board holding ONLY
#               the fifty-degree angle. A figure WAS drawn, so the promised-picture
#               referee stayed quiet; the content referees only read triangles.
#               NEW tutor.angle_compare_conflict (rule 63e): a spoken right-angle
#               comparison must have deg="90" in an [[angle]] tag of the same reply
#               (the honest move is split -- the piece drawn INSIDE the right
#               angle); the comparison QUESTION alone never fires. Rule 63 gains
#               (d) and (e) in prompts.py; PART 3bq; RULES.md regenerated. ALL CODE
#               IS IN tutor.py / prompts.py; this file only carries the stamp.
#   2026-08-18  APP_BUILD -> "2026-08-18hy-voice-asks-twice". THE VOICE ASKS TWICE.
#               Jim heard the seam live: he pushed hx while touring the dashboard and
#               one line came out in the mechanical browser voice before the warm
#               voice returned. Cause: speak tickets are server memory (_SPEAK_TICKETS),
#               so a deploy's instance switchover wipes them and can kill one in-flight
#               prep/clip; voice.js then fell back to the browser voice immediately
#               (sound over silence -- right, but audible). voice.js now re-asks for a
#               fresh prep ONCE (~700ms) before falling back; {voice:false} is still
#               believed immediately and the 5s watchdog stays the outer guarantee.
#               ALL CODE IS IN static/voice.js; this file only carries the stamp.
#               PART 3bp pins the shape; proved in a real Chromium drive (first prep
#               killed -> second prep -> the warm clip plays; voice:false -> exactly
#               one ask).
#   2026-08-18  APP_BUILD -> "2026-08-18hx-beta-key-leaves-url". THE WEAKEST PAGE,
#               DIAGNOSED AND FIXED (Phase 5's last named page). /beta's pass
#               generator opened via ?admin=<FORUM_MOD_KEY> -- the GENERAL ADMIN KEY
#               in a URL, the credential-in-URL class's third sighting. beta.html now
#               uses /admin's exact pattern (legacy link honoured once, sessionStorage,
#               address bar scrubbed, X-Admin-Key header everywhere, wrong key
#               forgotten); the three beta POSTs here accept the header (body.key
#               stays for stale pages, now optional so header-only calls validate).
#               Plus one content fix: the page now tells a tester WHERE to enter
#               their pass (sign in at /login). PART 3bo pins all of it.
#   2026-08-18  APP_BUILD -> "2026-08-18hw-screen-watch". THE GOVERNOR'S EYES ON
#               PRODUCTION (the last queued piece of Phase 1's "give the governor
#               eyes"). NEW .github/workflows/screenwatch.yml: GitHub's runners have
#               the browser Render lacks, so every night at 09:30 UTC one drives a
#               real three-turn lesson on mrcadabra.com with a dedicated audit
#               student and judges the rendered screens with screencheck's six
#               checks; findings FAIL the run (GitHub notifies Jim), report +
#               screenshots kept as artifacts. ⚠️ JIM'S ONE-TIME SETUP: create a
#               dedicated audit student and add its code as the SCREENWATCH_CODE
#               repo secret. PART 3bn pins the workflow. This file only carries the
#               stamp.
#   2026-08-18  (decision record, no code change -- APP_BUILD stays hv) JIM'S RULING:
#               BOOKMARK LOGIN STAYS. Page-nav links keep carrying ?code= on purpose;
#               the hs note's "parked product decision" is decided. See _code_dep's
#               docstring for the ruling and the compensating controls. Jim also
#               confirmed DATA_EXPORT_KEY and FAMILY_RESET_KEY are set in Render env.
#   2026-08-18  APP_BUILD -> "2026-08-18hv-one-backend-loudly" (Phase 5, Classes E+F).
#               (1) LOUD DEGRADED MODE: a CONFIGURED-but-unreachable database no
#               longer silently forks persistence onto stranded local files. NEW
#               _degraded_reply() gates the three teaching lanes with a warm
#               maintenance message + throttled ops email; ALLOW_FILE_FALLBACK=1
#               marks a dev box and lifts the gate; /health storage gains
#               "degraded". (2) THE BACKUP CANNOT DIE SILENTLY: the pass is fenced
#               with ops_fail telemetry + an alert email, and a skip refreshes the
#               ops_pass marker so /health's backup age means "age of the newest
#               snapshot" (the backup-age-null mystery had two innocent readings;
#               now it has one, and a real failure reaches Jim's inbox). (3) THE
#               OFF-SITE COPY IS AUTOMATED: every OFFSITE_BACKUP_DAYS (default 7)
#               the freshest snapshot is EMAILED to ALERT_EMAIL as an attachment
#               (_send_email grew attachment support), size-capped with a loud
#               alert, restart-safe via ops_pass rows, visible in /health ops.
#               (4) store.py: the DELETIONS LEDGER + token-free restores -- see its
#               own hv note.
#   2026-08-18  APP_BUILD -> "2026-08-18hu-server-records-results" (Phase 5, Class E's
#               flagship). MASTERY IS NO LONGER CLIENT-WRITTEN. NEW
#               _record_result_tags(): the server parses [[check]]/[[quiz]]/
#               [[finalexam]] out of the reply it JUST generated (all three lanes +
#               the opener) and records the scores itself -- record_check /
#               record_topic_quiz / record_final_exam (final still gate-checked, and
#               a final tag outside an exam turn writes telemetry instead). The
#               client POST endpoints became ECHO GATES: a POST matching what the
#               server recorded (in-memory TTL ledger, keyed code/course/kind/unit/
#               topic/pct) deduplicates to {recorded:"server"}; a POST the server
#               never saw the model emit gets 409 + a "client_result_rejected"
#               system_events row -- minted mastery becomes telemetry, not truth.
#               Stale cached pages keep working across the deploy (their echoes
#               match). No page changes needed. Sprints remain client-counted (they
#               never gate anything, by design) -- named here, not silently skipped.
#   2026-08-18  APP_BUILD -> "2026-08-18ht-bounded-and-split" (Phase 5, two cuts):
#               (1) THE GOD-KEY IS SPLIT. _require_admin gained tiers: FORUM_MOD_KEY
#               stays the general panel/moderation/beta key; the FULL DB snapshot
#               download demands DATA_EXPORT_KEY; destructive student/family resets
#               demand FAMILY_RESET_KEY. Graver tiers never fall back to the general
#               key and FAIL CLOSED (503 naming the env var) until Jim sets the two
#               new keys in Render. admin.html prompts for the graver keys and
#               forgets a wrong one on 401.
#               (2) THE TURN CANNOT HANG. tutor.py bounds every Anthropic call
#               (ANTHROPIC_TIMEOUT_S, default 60s, max_retries=1); session/topic/
#               practice add a 90s fetch abort with a warm try-again bubble.
#               ⚠️ JIM'S DEPLOY STEP: add DATA_EXPORT_KEY and FAMILY_RESET_KEY (two
#               long random values) in Render env, or backup download and resets
#               stay disabled (on purpose).
#   2026-08-18  APP_BUILD -> "2026-08-18hs-credential-leaves-url". PHASE 5 (THE BETA
#               GATE) BEGINS -- review Class F. The student CODE is the login, and it
#               travelled in request lines that plaintext HTTP logs record (Render's
#               edge, uvicorn's access log); /api/speak's query also carried the
#               SPOKEN LINE -- a child's lesson, usually with their first name.
#               (1) NEW _code_dep: all 17 /api/xxx/{code} routes resolve their code
#               through one dependency -- X-Student-Code header preferred, path form
#               kept for stale cached pages; every shipped page now sends the header
#               with 'me' in the path (the dg admin-key precedent, applied to the
#               student credential).
#               (2) NEW POST /api/speak-prep -> GET /api/speak?t=<opaque ticket>:
#               an <audio src> cannot send headers, so the voice path mints an
#               in-memory TTL ticket carrying {code, text, lead}; the clip still
#               STREAMS with the same cache and leading silence. Tickets are not
#               single-use (<audio> legitimately re-requests); a restart invalidates
#               them and pages fall back to the browser voice via existing paths.
#               Legacy ?text=&code= stays for stale pages. /api/transcribe and
#               /api/library gained the header form (mic.js/library.js send it).
#               (3) The [billing] log line masks the parent's email.
#               (4) analytics.js: JIM'S RULING 2026-08-18 -- no fourth party on
#               children's pages; the tracker refuses to load on student surfaces.
#               ⚠️ PARKED PRODUCT DECISION (not code): page-NAVIGATION links
#               (/session?code=...) still carry the code -- they are how young
#               students log in from a family bookmark. Moving login to a
#               cookie/session is Jim's call, recorded in the Phase 5 notes.
#   2026-08-18  APP_BUILD -> "2026-08-18hr-one-unit-stories". THE NIGHTWATCH'S FIRST
#               CATCH, CLOSED THE STANDING WAY: rule 32(b) (prompts.py -- a story
#               that models an expression keeps ONE unit) + the twenty-first
#               referee (tutor.story_units_conflict, the caught money-plus-objects
#               shape) + PART 3bi. The governor found it at 1:44am; the fix ships
#               with its check the same morning. This file only carries the stamp.
#   2026-08-18  APP_BUILD -> "2026-08-18hq-two-prompt-sizes". THE DEGRADATION
#               EXPERIMENT IS RUNNABLE (lessonaudit.py --prompt-size small|large;
#               see its hq note). nightwatch unpacks run_scenario's new 4th return
#               member; this file only carries the build stamp.
#   2026-08-18  APP_BUILD -> "2026-08-18hp-order-of-authority". THE PRECEDENCE
#               LATTICE (Phase 4). The words changed in prompts.py (WHEN INSTRUCTIONS
#               COLLIDE -- five levels, one supremacy claim, the audited cross-pulls
#               named); RULES.md regenerated and now battery-guarded against
#               staleness; this file only carries the build stamp.
#   2026-08-18  APP_BUILD -> "2026-08-18ho-record-referee". THE RECORD-CLAIM REFEREE
#               (the count-claim probe's promotion; Phase 4, Class D). NEW
#               _claim_record(code, course): the compact past-facts record (unit-check
#               best/last, topic-quiz bests, mastered, touched) built from the store
#               each lesson turn and handed to tutor's TWENTIETH referee via
#               student_context["claim_record"] -> meta["record"]. False score
#               claims, false mastery/in-progress claims and invented watch-counts
#               (the audit's "you've now watched this move twice" refusal) are now
#               regenerated before a student sees them. The referee's engine and
#               patterns live in tutor.py (see its ho note).
#   2026-08-18  APP_BUILD -> "2026-08-18hn-streak-clock". THE STREAK LIVES ON
#               CALIFORNIA TIME -- Jim's ruling on THE THREE CLOCKS ("use California
#               Pacific Time"). The change itself is in store.py (_streak_now/
#               _streak_today feeding _bump_stats' unchanged SQL CASE; STREAK_TZ env,
#               default America/Los_Angeles; loud UTC fallback) with tzdata added to
#               requirements.txt; this file only carries the build stamp.
#   2026-08-18  APP_BUILD -> "2026-08-18hm-honest-opener". PHASE 4 OF THE FULL-APP
#               REVIEW BEGINS (Class D: the model's word becoming truth, unvalidated).
#               THREE CUTS IN THIS FILE:
#               (1) THE OPENER IS BRANCHED IN CODE. The old opener note told the model
#               "if you have met before... give a SHORT recap" and let IT decide from
#               history -- so an empty record made compliance require invention, the
#               invented recap was stored in history, and every later opener replayed
#               it as memory (the review's likeliest phantom-Unit-5 origin). NEW
#               _opener_record_note(): the SERVER decides has-record from the store
#               (assistant history / touched / mastered -- placement alone is not a
#               record of lessons), the no-record opener now FORBIDS a recap, and a
#               returning student's recap FACTS are stated by the server from the
#               record (resolved unit + name, mastered units, last-active). History
#               is thereby demoted to STYLE: the note says outright that when the
#               conversation and the record disagree, the record wins. The gap-days
#               refresher now names the record's unit (the old text pointed the model
#               at its own stored prose), and only fires when a record exists.
#               (2) [[unitplan]] IS VALIDATED BEFORE IT FILES. NEW _unit_allowed_set
#               (resolved + focus + touched + mastered + next-in-progression + the
#               unit the student's own message just asked for) rides student_context
#               into tutor's meta, arming the NINETEENTH referee (unitplan_conflict:
#               a declaration outside the set is regenerated before the student sees
#               it); NEW _accept_declared_unit re-checks at filing time (referees
#               fail open), so a surviving hallucinated declaration writes a
#               system_events row ("unitplan_rejected") instead of a topic_progress
#               row. Jim's gs ruling (THE UNIT FOLLOWS THE TEACHING) still holds --
#               for any teaching the record can justify.
#               (3) The [[unitplan]] unit pattern now compiles from
#               tags.UNITPLAN_UNIT_PATTERN (one grammar source, two consumers).
#   2026-08-17  APP_BUILD -> "2026-08-17hl-small-cuts". THE SMALL CUTS OF PHASE 3
#               (this file: one of the three -- the returning-student check).
#               _has_any_history's FILE-fallback branch parsed session keys with
#               "-" while every writer builds them with "::" -- so with the DB off,
#               EVERY returning student was greeted as brand new (and codes
#               containing "-" mis-split). The branch now parses "::" exactly like
#               _ck builds it. Both login sites (student + beta) now compute
#               "returning" as bool(session history) OR _has_any_history(code), so
#               a student whose current-course session is empty but who has history
#               in another course is still greeted as returning. store.py carries
#               the other two cuts (atomic streak, quiz identity) -- see its hl note.
#   2026-08-17  APP_BUILD -> "2026-08-17hk-no-lost-turns". THE HISTORY RACE IS CLOSED.
#               NEW mutate_history(code, course, fn) is the only way the chat path
#               writes conversation history: both the main turn and the opener now
#               APPEND/TRANSFORM atomically via store.update_history (CAS -- see
#               store.py's hk note for why not a row lock: the lock version was
#               silently wrong on SQLite and the hammer caught it losing 200 of 240
#               appends with zero errors). The opener's junk-strip is re-applied to
#               the FRESH history inside the transform (idempotent), so an opener
#               racing a typed first message can no longer erase it. The file
#               fallback does its read-transform-write under _sessions_lock.
#               save_session remains for WHOLE-session writes (resets, imports) only.
#   2026-08-17  APP_BUILD -> "2026-08-17hj-one-unit-owner". THE DEEPEST CUT OF PHASE 3.
#               "Which unit is this student in" had FIVE competing answers reconciled
#               ad hoc by four consumers -- the unit-rail bug's whole family. NEW
#               main._resolve_unit(code, course, placement, focus) is the ONE
#               derivation, with a named priority: focus > tracked (the most recently
#               touched UNMASTERED unit -- so build gs's [[unitplan]] authority now
#               PERSISTS across sessions instead of evaporating at the next opener) >
#               progression-from-the-placement-FLOOR (a placed-at-3 student advances
#               to 4 on mastering 3, never "back" to units the Challenge cleared --
#               the first draft walked from 1 and the priority-table test caught it
#               before it ever ran) > placement (brand-new students only) > 1.
#               CONSUMERS: student_context["current_unit"] feeds build_system_prompt's
#               playbook + foundation filter AND _lesson_unit (the fourteenth referee)
#               -- same field, so they still cannot disagree; the tracker files under
#               the resolved value (killing review F4c: placement outranked
#               progression on every tagless turn, forever); the drift probe logs
#               resolved+source as its fourth signal.
#               THE PLACEMENT NOTE EXPIRES (review F4a): the "should start around
#               Unit N" sentence -- which tutor.py regex-read back OUT of the prose to
#               pick the playbook -- now rides only while placement is genuinely the
#               best answer. After that, the field carries the truth as data.
#               gs PRESERVED: an explicit [[unitplan]] declaration still outranks
#               everything except the student's own focus for the tracking write.
#               PROVED on a real database (ruletests PART 3ba, every push): the
#               six-case priority table, including the two cases that were actually
#               broken -- mastered-placement-advances and tracked-persists.
#   2026-08-17  APP_BUILD -> "2026-08-17hi-atomic-counters". PHASE 3 BEGINS: counter
#               arithmetic moved INTO the database (see store.py's hi note) -- best
#               scores can no longer regress, a unit can no longer be silently
#               un-mastered by overlapping submissions, minutes and attempt counts
#               are exact under any concurrency. No main.py logic changed.
#   2026-08-17  APP_BUILD -> "2026-08-17hh-one-grammar". PHASE 2 COMPLETE. NEW FILE
#               tags.py is the single source of the [[tag]] grammar -- it had SEVEN
#               independent declarations across tutor.py, ruletests.py and the page
#               dispatchers, and one had already drifted (the live BOARD_TAG regex
#               was missing numberline and areamodel, so teaching with either counted
#               as "no board" in --live checks; fixed by derivation). tutor.py and
#               ruletests.py derive their sets; the page dispatchers stay
#               page-specific BY DESIGN and the battery cross-checks them against the
#               registry (mutation-verified: an unregistered [[sparkle]] pasted into
#               topic.html fails the build). No main.py logic changed.
#   2026-08-17  APP_BUILD -> "2026-08-17hg-one-pipeline". PHASE 2, BACKEND HALF: the
#               three reply getters in tutor.py became thin configurations of ONE
#               _reply_pipeline (see tutor.py's hg note). No main.py logic changed --
#               this bump exists so /health can answer "did Render take it?".
#   2026-08-17  APP_BUILD -> "2026-08-17hf-one-microphone". PHASE 2, PART FIVE -- the
#               LAST triplicated frontend cluster, and the one where build gz's two
#               live voice-answer defects were born. Unlike voice.js/board.js this was
#               NOT a verbatim move: the three mic copies had genuinely DIVERGED.
#               Named, and reconciled in static/mic.js:
#               (1) hint wording -- session says 'tap "Type my answer"' (it has that
#               button), topic/practice say "just type your answer below" (always-on
#               type bar). A page-config variable (micTypeHint) carries each page's
#               phrase; every string each page could show before is byte-identical
#               after (asserted statically, page by page).
#               (2) structure -- topic/practice had transcribe() split out (gr),
#               session inlined it. The split wins, everywhere.
#               (3) THE F10 CONFLATION, fixed -- the one deliberate change. On topic/
#               practice a TRANSPORT failure and an empty transcript both returned ""
#               and both read to a child as "I didn't quite catch that -- tap and try
#               again": our outage, their blame, on every retry. transcribe() now
#               returns {ok, text}; a failed request says honestly "I couldn't reach
#               the classroom just now -- give it a second and tap again."
#               PROVED with a real fake-device microphone (Chromium fake audio +
#               granted permission): record -> stop -> transcribe -> the text arrives
#               in the page's tutor sender, on ALL THREE pages, zero page errors; the
#               silence path and the server-500 path each show their own message.
#               This end-to-end mic test had never existed for this app.
#               PART 3aw gains mic.js (6 functions + 5 state names, micTypeHint
#               included); the gr spoken-letter client checks read the single copy.
#   2026-08-17  APP_BUILD -> "2026-08-17he-one-board". PHASE 2, PART FOUR: THE
#               WHITEBOARD BECOMES ONE COPY -- static/board.js. The 34 top-level
#               display functions (every [[step]]/[[write]]/[[solve]] row, the graph,
#               figures, balance, machine, objects, choices, the bubble feed, the
#               spotlight; choiceBtn rides nested inside showChoices as it always did)
#               plus their pure state (lastTurnEl, spotTimer, choicesRow, autoScroll,
#               stickBottom) and constants (GRAPH_COLORS, SPOT_MS) moved out of the
#               three teaching pages. Measured before the move: byte-identical after
#               comment normalisation on all three -- zero divergence, which after
#               build gz is luck, not safety.
#               DELIBERATELY NOT MOVED: DOM refs (feed, composer -- board.js loads in
#               <head>, before the DOM exists) and the page-specific dispatchers
#               (handleTags, wipeBoard, feedBlock, getWorklist, clearStage): which
#               tags a page supports is configuration, not copy-paste.
#               PROVED, not assumed: a ten-tag corpus (step, write, solve, column,
#               graph, triangle, balance, machine, objects, choices, card) rendered
#               in a REAL BROWSER before and after, on all three pages -- 30 turns,
#               every board drawn, bubble AND board HTML byte-identical, ZERO
#               differences. Battery: PART 3aw gains board.js (functions + state);
#               the board-tag contract, the showColumn guarantees, the fitting checks
#               and the spotlight checks now read the SINGLE copy, while per-page
#               checks keep what pages still own (CSS, the clearSpot CALLS).
#   2026-08-17  APP_BUILD -> "2026-08-17hd-one-voice". PHASE 2, PART THREE: THE VOICE
#               PIPELINE BECOMES ONE COPY -- static/voice.js. Harder than hc because
#               this cluster OWNS STATE: 13 page-level variables (ttsAudio, audioCtx/
#               analyser/timeData/usingAnalyser, keepAlive, audioWarmed, lastAudioAt,
#               paused, elevenEnabled, maleVoice, firstClipOfSession, firstSpeakLead)
#               moved WITH the 11 functions (speak, browserSpeak, pickVoice,
#               ensureAudioGraph, silentWavUri, start/stopKeepAlive, warmUpAudio,
#               stopAllSpeech, withDeadline, speechDeadline). Pages' declarations were
#               REMOVED -- a duplicate top-level let is a SyntaxError, so a relapse dies
#               at parse time, and PART 3aw now checks for re-declaration too.
#               ONE DELIBERATE BEHAVIOUR CHANGE (review finding F9): the three
#               warmUpAudio copies had diverged -- session started the keep-alive at the
#               opening tap (build cb's "wake the output device early") and topic/
#               practice did NOT, so their first words could still hit a powered-down
#               device after all three voice fixes (bl, cb, gn). voice.js carries
#               session's variant: the cb cure now applies on every page. Everything
#               else moved VERBATIM, comments included (the gn resume race, the gp3
#               ctx0 probe -- each was a real child's cut-off first word).
#               AMBIENT CONTRACT, verified before the move: voice.js reaches for exactly
#               three names it does not define -- CODE, forSpeech (speech-text.js loads
#               first), setState (each page's UI hook) -- all present on all three pages.
#               PROVED: all three pages parse; booted in a real browser with ZERO page
#               errors; functions defined, warmUpAudio contains the keep-alive wake on
#               every page, and cross-script state is readable AND writable from page
#               code; nine speaking turns driven through screencheck (S1-S7 + console):
#               0 findings. Battery: the gn/gp3 voice guarantees are asserted once
#               against the module; pages are checked for the include, for re-inlining,
#               and for state re-declaration (mutation-verified: all three fire).
#   2026-08-17  APP_BUILD -> "2026-08-17hc-one-copy". PHASE 2 OF THE FULL-APP REVIEW,
#               PART TWO: THE EXTRACTION. The review's Class B -- "one renderer, five
#               hand-synced copies" -- is the whack-a-mole GENERATOR: ~2,400 duplicated
#               lines across session/topic/practice, where build gz's two live defects
#               existed only because a fix reached one copy and not its siblings, and
#               build gn2's "case is meaning" fix had to be hand-copied three times.
#               TWO NEW SHARED FILES, extracted VERBATIM (not one character of logic
#               changed in the move):
#                 static/speech-text.js -- FRAC_WORDS, fracWords, mixedWords, moneyWords,
#                   forSpeech: what a string should SOUND like.
#                 static/board-text.js  -- VAR_NEEDS_CONTEXT, the MV_* tables,
#                   varInMathContext, escapeHTML, styleVars, styleVarsCore, machineSub:
#                   what the student SEES, including the gn2 case rules.
#               Both are CLASSIC scripts on purpose, so the functions stay globals and
#               EVERY EXISTING CALL SITE WORKS UNCHANGED -- the pages lost code, not
#               behaviour. Loaded in <head> before any inline script.
#               SCOPE WAS CHOSEN BY EVIDENCE, NOT AMBITION. Only functions that are
#               byte-identical across all three pages AND depend on nothing but the
#               browser were moved. The voice CONTROL functions sitting right beside
#               forSpeech (speechDeadline, stopAllSpeech, withDeadline) were left in the
#               pages: they read page state (`paused`, `ttsAudio`), and extracting them
#               would have thrown a ReferenceError on the first pause. They belong to a
#               later voice.js that moves that state with them.
#               PROVED EQUIVALENT, NOT ASSUMED: the 974-string corpus (949 authored
#               foundation strings + 25 adversarial cases aimed at case, signs, money,
#               fractions and function names) pushed through forSpeech, styleVars and
#               machineSub in a REAL BROWSER, before and after, on all three pages --
#               2,922 outputs each, ZERO differences, zero page errors. Then screencheck
#               drove all three pages: S1-S7, 0 findings.
#               GUARDED: ruletests PART 3aw fails the build if any page re-inlines a
#               shared function, drops an include, or loads it after its own script
#               (verified by re-inlining styleVarsCore into topic.html: caught). PART 3
#               now runs the forSpeech cases ONCE against the module and asserts each
#               page LOADS it; the gn2 seam checks read the single source instead of
#               three copies; PART 3au learned to read <script src> globals so the
#               sweep does not howl at the refactor it exists to protect.
#   2026-08-17  APP_BUILD -> "2026-08-17hb-the-net". PHASE 2 OF THE FULL-APP REVIEW,
#               PART ONE: THE NET GOES UP BEFORE THE EXTRACTION GOES IN. Phase 2's real
#               move is collapsing ~2,400 duplicated frontend lines into shared modules;
#               this build first makes the class of defect that refactor risks MECHANICAL
#               to catch, and fixes a defect build ha introduced.
#               ⚠️ (1) BUILD ha CORRUPTED EIGHT OF THE TEN APP PAGES, AND hb FIXES IT.
#               ha inserted the client-log.js include after the first literal "<head>" in
#               each file -- which on eight pages is a "<head>" MENTIONED INSIDE the
#               change-note comment at the top. The include landed inside that comment,
#               and the comment note shipped with it ("-->") CLOSED the comment early,
#               spilling the rest of the change-note prose into the live document.
#               session.html rendered ONE body child instead of nineteen. ha's own check
#               passed the whole time, because it searched the RAW source for "<script"
#               and found the commented one. Caught by DRIVING the pages in a real
#               browser. ha was never pushed, so this never reached a student -- but it
#               would have. The include now goes after the first <head> OUTSIDE any
#               comment, on all ten pages, verified in a browser (body children 3-19, no
#               stray prose, beacon live and first).
#               (2) ruletests PART 3au -- THE UNDECLARED-IDENTIFIER SWEEP. Pure stdlib,
#               no node/npm/pip, so it runs for everyone on every push. Catches build
#               gz's exact class (a fix hand-copied between pages without the state it
#               reads) including the hard half: declared in an inner scope, read at page
#               level. Silent on all 13 shipped pages; fires on both gz defects
#               reintroduced verbatim; fires on 5 injected mutations across 4 pages; and
#               it SELF-TESTS every run, so an analyzer that goes blind cannot look like
#               a clean codebase.
#               (3) PART 3at's beacon checks now read COMMENT-STRIPPED source and assert
#               no bare prose before <head> -- the check that actually catches (1). The
#               two obvious checks (balanced delimiters, comment-stripping) both pass on
#               the broken file; this one fails it with 18,681 characters of evidence.
#               (4) THE UNIT REFEREE IS RE-ARMED ON PRACTICE AND TOPIC (see tutor.py) --
#               ruletests PART 3av, both directions + the canonical sweep.
#               (5) screencheck now drives all THREE teaching pages, not one (see its
#               own note); demo/challenge are NAMED as uncovered rather than skipped.
#   2026-08-17  APP_BUILD -> "2026-08-17ha-eyes". PHASE 1 OF THE FULL-APP REVIEW: THE
#               APP WATCHES ITSELF. The review's meta-finding: fail-open everywhere,
#               observed nowhere -- ~19 print-only crash handlers, probes printing to
#               logs nobody aggregates, a browser with zero error reporting, and a
#               teaching path whose failures can never reach store.record_error. Now:
#               (1) store.system_events + record_event/event_stats/recent_events/
#               last_event_at/purge_system_events (see store.py ha note);
#               (2) tutor.py counts every referee FIRE and CRASH by name, every
#               pass-through, every probe hit, both promptsize alarms, and the three
#               teaching-path catch-alls (see tutor.py ha note);
#               (3) NEW POST /api/client-error -- static/client-log.js (loaded FIRST on
#               the ten app pages) beacons window.onerror/unhandledrejection here;
#               rate-limited per IP, hard caps, silently drops floods;
#               (4) /health now reports SUBSYSTEMS (which defensive imports loaded --
#               a broken mathcheck.py is a visible False instead of a silent
#               unverified tutor) and OPS AGES (seconds since the last heartbeat /
#               backup / night-watch pass -- a dead ops thread is a growing number);
#               (5) the heartbeat, backup, nightwatch and purge passes stamp
#               system_events; the purge pass also ages out telemetry (EVENTS_DAYS,
#               default 90);
#               (6) NEW GET /api/admin/events feeds the /admin Telemetry card;
#               nightwatch's morning report gains "The week's telemetry" with named
#               offenders. Probes ([unitdrift], [termgap], [rule37]) count themselves.
#   2026-08-17  APP_BUILD -> "2026-08-17gz-stop-the-bleeding". PHASE 0 OF THE FULL-APP
#               REVIEW (six independent review passes over every file; findings and the
#               six-classes attack plan live in the project doc Full_App_Review_2026-08-17).
#               Four surgical fixes, each with its battery check:
#               (1) VOICE ANSWERS WERE DEAD ON topic.html AND practice.html. Both pages
#               used lastTutorText (the build-gr expect=letter hint) without ever
#               declaring or assigning it -- a ReferenceError inside transcribe() on
#               EVERY spoken answer, swallowed by its catch, so both pages told the
#               student "I didn't quite catch that" and blamed their audio. The fix that
#               was hand-copied between pages left its state behind: the exact
#               copy-divergence class the review names. Both pages also read the
#               undeclared `started` in their visibilitychange handlers (ReferenceError
#               on every return to the tab; keep-alive never restarted -- the bl/cb
#               "first word swallowed" symptom, still alive on two pages). They now use
#               the page-level audioWarmed they already maintain.
#               (2) THE PROMPT CEILING IS ENFORCED AT RUNTIME (see tutor.py gz note):
#               all-heard students overflowed 180K on every course, silently. On
#               refresher turns this file sets foundations_force_verbatim (from
#               foundations.wants_refresher) so rule 40's exact-words promise holds.
#               (3) THE HEARTBEAT ALWAYS BEATS: WEEKLY_EMAIL=off used to return early
#               from _start_digest_thread -- one misnamed flag silently disabling the
#               nightly BACKUP, the cost watchdog, the usage purge and the night watch.
#               The flag now gates only the email, inside _weekly_digest_pass.
#               (4) store.py's /admin verifier breakdown no longer buckets
#               "prose-unresolved" (a reply that SHIPPED with a known unresolved referee
#               finding) and "empty" into verify_none -- they are their own counts, and
#               admin.html displays the caught-by-referee number honestly.
#   2026-08-17  APP_BUILD -> "2026-08-17gy-audit-closed". ALL SIX CAUSES FROM THE DAY'S
#               AUDIT ARE CLOSED. Five lesson-audit runs, ten lessons, 27 findings, triaged
#               against their own transcripts (24 held, 1 rejected with its reason, 2 weak)
#               and collapsed into six causes -- FIVE of which were places a referee we
#               already owned failed to fire. Builds gt (board shapes), gu (rule 47's cold
#               quiz, whose founding sentence had reappeared VERBATIM six days after the
#               rule was written from it), gv (invented history), gw (the bare answer-demand
#               and the decimal), gx (rule 65, show them when asked) and gy (a rule spoken
#               as a law) close them. FOUR new referees (15-18), two new rules (64, 65),
#               three rules moved COVERED -> ENFORCED (47, 54, and rule 61's fraction case),
#               and one referee that had been REGENERATING TWO FOUNDATION SCRIPTS since it
#               shipped -- found not by any audit but by the canonical sweep.
#   2026-08-17  APP_BUILD -> "2026-08-17gx-show-them". NEW RULE 65 + the SEVENTEENTH
#               referee, closing the fifth cause from the day's triage and the worst single
#               thing in it: a child asked to be shown the square root of 169 and was told
#               "you've now watched this move twice -- let's flip it", then handed a new
#               triangle. It happened again two turns later. Both counts were false. Nothing
#               in the rulebook had ever said "when a student asks to be shown, show them" --
#               it does now, in all ten courses, and the referee needs all three conditions:
#               they asked, nothing was worked out, and the job went straight back to them.
#   2026-08-17  APP_BUILD -> "2026-08-17gw-bare-demand". The fourth cause from the day's
#               triage, and it came apart into three. The rule-15 and rule-44 findings on
#               the decimal lesson were ONE defect: a board line with no "?" is invisible to
#               BOTH referees at once, so "What do you get?" over "2.6 + 1.35" slipped
#               through twice. Under it sat gk's fraction bug in decimal clothing -- the
#               "1" of 1.35 found inside the word "one". And the canonical sweep, run to
#               prove the fixes harmless, turned up a THIRD thing nobody had reported: gl's
#               self-correction referee has been regenerating two foundation scripts every
#               time the tutor tried to deliver them, because they say "hold on to this".
#   2026-08-17  APP_BUILD -> "2026-08-17gv-invented-history". The third cause from the
#               day's audit triage, and the biggest: seven claims about what had already
#               happened that were untrue. Split on whether a referee can check them --
#               gm's referee is widened to catch a TOTALITY claim ("start to finish on your
#               own") over a fragment, and the false counts ("you've now watched this move
#               twice", said twice and false both times) are PROBED rather than enforced,
#               because a referee sees one reply and cannot count a conversation. The false
#               count matters beyond its own untruth: it is what the tutor used to REFUSE a
#               child who asked to be shown the square root of 169.
#   2026-08-17  APP_BUILD -> "2026-08-17gu-cold-quiz". RULE 47 STOPS BEING A WISH. The
#               second cause from the day's audit triage, and the most damning single find
#               in it: the sentence "let's do it -- five questions, all on finding the
#               percent of a number" was caught on 2026-08-11, rule 47(d) was WRITTEN from
#               it, and the tutor produced it again WORD FOR WORD on 2026-08-17 -- because
#               rule 47 was COVERED and nothing watched it. A child was told that two
#               warm-up problems qualified them for a unit quiz on a unit never taught, and
#               a five-question instrument wore the Unit Quiz's name into their record.
#               cold_quiz_conflict (the sixteenth referee) enforces 47(d)'s own bar; rule 47
#               moves COVERED -> ENFORCED.
#   2026-08-17  APP_BUILD -> "2026-08-17gt-board-shapes". THE FIRST AUDIT FINDINGS CLOSED.
#               Five lesson-audit runs (ten lessons, 27 findings, 6 HIGH) were triaged
#               against their own transcripts -- 24 hold, 1 rejected with its reason, 2 weak
#               -- and they collapse into SIX causes, FIVE of which are places a referee we
#               already owned failed to fire (see Audit_Triage_2026-08-17.md). This build
#               closes the cheapest and most complete of them: board_notation_conflict now
#               knows an arrow after an equals sign, a question stuffed into an equation, and
#               a tautology. No judgement is needed for any of the three, which is exactly
#               why missing them mattered.
#   2026-08-17  APP_BUILD -> "2026-08-17gs-unit-follows-teaching". THE UNIT FOLLOWS WHAT IS
#               BEING TAUGHT. Jim reported the same symptom twice -- "it still says unit one
#               on the top when we are talking about unit five" -- and BOTH earlier diagnoses
#               were guesses, including one of mine that blamed the tutor and cleared the
#               rail. The real defect: the rail was seeded from placement.start_unit, where
#               the student was PLACED, a number that never moves; the tutor chose its own
#               topic; and NOTHING RECONCILED THEM. Worse, _track_topic filed activity under
#               that same placement unit, so the store agreed with the stale rail and the
#               whole system was confidently wrong together -- which is exactly why no check
#               ever caught it. Jim's ruling: the unit follows the teaching. So the tutor's
#               own [[unitplan unit="N"]] is now the authority (an explicit focus the student
#               clicked still wins), it is what _track_topic records, /api/session serves it
#               back as progress.current_unit, and session.html's rail prefers it over
#               placement. PART 3an asserts every link of that chain, because breaking any
#               one of them brings the symptom back looking like a display bug.
#               ⚠️ The half that CANNOT be enforced yet -- whether the declared unit matches
#               the content -- is measured by the new [unitdrift] probe, which logs when the
#               declaration, curriculum.classify_unit and the tracked unit disagree. Two
#               diagnoses of this symptom have been guesses; the third gets data first.
#   2026-08-17  APP_BUILD -> "2026-08-17gr-heard-and-honoured". TWO WAYS TO IGNORE WHAT A
#               CHILD ACTUALLY SAID, both from one Geometry lesson of Jim's.
#               (1) THE SPOKEN LETTER. Asked which side was the hypotenuse, he said the
#               letter "c"; ElevenLabs returned the Spanish "si"/"CSI"; the tutor told him
#               he was WRONG and demanded a letter. We were sending no language hint at all.
#               Now: language_code (STT_LANGUAGE, default "eng") with a retry WITHOUT the
#               hint on a 422, so a parameter can never silently break the microphone; plus
#               a server-side spoken-letter map applied only when the page says a letter was
#               the expected answer. That corrects OUR transcription, which is a different
#               act from changing the student's answer.
#               (2) THE SIGNED ANSWER -- NEW RULE 64 + the FIFTEENTH referee. He answered
#               "minus five" to "what times itself gives twenty five?" and was told "That is
#               correct", after which the reply taught on using 5. Both halves are wrong:
#               (-5)(-5) really is 25 but a LENGTH IS NEVER NEGATIVE, so "correct" was
#               untrue; and swapping his number for a different one without saying so
#               teaches a child that the minus sign is decoration -- the exact misconception
#               a squaring lesson exists to prevent. answer_sign_conflict fires only when the
#               reply affirms a signed answer, uses the unsigned magnitude, and never
#               mentions the sign; the right response ("both 5 and -5 square to 25, but a
#               length can't be negative") passes.
#   2026-08-17  APP_BUILD -> "2026-08-17gq-openai-boundary". A PROMISE BECOMES A TEST.
#               Jim turned on OpenAI's "share inputs and outputs" for a DEDICATED AUDIT
#               PROJECT, which makes the night watch essentially free and lifts the budget
#               ceiling off its coverage. That bargain is safe for exactly one reason:
#               OpenAI is not in the teaching path. Every transcript it marks is a
#               synthetic lesson between an AI student persona and the tutor; no child's
#               words have ever been sent to it. The day that stops being true, a minor's
#               conversation lands in a project where sharing is ON -- and static/
#               privacy.html promises exactly three processors (Anthropic, ElevenLabs,
#               Render) and says "we do not send student data to anyone else... to anyone,
#               ever." So the boundary now has a guard: PART 3al fails the build if any
#               teaching module so much as references OpenAI, and names the privacy promise
#               in its failure text. Proved by mutation -- bolting a substitute-teacher
#               fallback into tutor.py fails two checks immediately.
#               ⚠️ THE SUBSTITUTE TEACHER CANNOT SHIP WITHOUT A PRIVACY-POLICY CHANGE AND A
#               SEPARATE NON-SHARING PROJECT. That was underweighted when it was first
#               discussed; it is a policy question before it is an engineering one.
#   2026-08-17  APP_BUILD -> "2026-08-17gp3-voice-closed". THE FIRST WORD IS FIXED, and the
#               probe that proved it needed fixing too. Jim, on the gn build: "Better -- I
#               hear the whole greeting now." Three builds tried this (bl and cb padded the
#               front of the clip; gn removed the flat 300ms race that let a clip start into
#               a still-suspended audio graph) and the third one was right. But his console
#               showed "ctx=running" on every clip and that was reported back to him as
#               "the race never fired" -- WRONG, and it would have sent the next fix chasing
#               the MP3 decoder. The probe samples the graph when audio STARTS, and forcing
#               that state to "running" is exactly what the fix does. A probe that reads
#               state only AFTER a fix has acted cannot say whether the fix was needed. It
#               now logs ctx0 (what we found) beside ctx (what we started into), so the next
#               report of a clipped word arrives with the evidence already in it.
#   2026-08-17  APP_BUILD -> "2026-08-17gp2-console-watch". A LANDMINE, FOUND IN A CONSOLE
#               PASTE. Jim sent the [voicehead] output from a live Geometry lesson, and
#               under the lines we were reading sat a Content-Security-Policy violation on
#               every silent-WAV data: URI the voice uses. Nothing was broken -- that header
#               ships report-only -- but it is documented as something we intend to ENFORCE,
#               and on that day silentWavUri() stops loading. That one function is BOTH the
#               audio warm-up and the keep-alive loop: the two mechanisms protecting the
#               first syllable of every sentence the tutor speaks. The voice would regress
#               and nobody would connect it to a security header. Fixed with one CSP
#               directive (media-src 'self' data:), and then made un-miss-able: screencheck
#               gained S7 (the console is clean) and its harness now serves the REAL policy
#               read out of this file, so the rig can finally reproduce the defect it was
#               written to catch. Proved both ways -- S7 fires twice with media-src removed
#               and is silent with it present.
#   2026-08-17  APP_BUILD -> "2026-08-17gp-nightwatch-card". THE GOVERNOR GETS A FACE, and
#               its reviewer becomes auditable. Build go ran for the first time overnight --
#               12 lessons, 6 new confirmed, 16 refuted, 38.5 minutes -- and exposed two
#               holes in itself within twelve hours. (1) The findings were written to a
#               markdown file on the persistent disk and served NOWHERE: the only readable
#               output was a one-line count in the Render log. A governor whose reports are
#               hard to reach is a governor that gets ignored, which go's own header warns
#               about. New: GET /api/admin/nightwatch/status + /report, and a Night watch
#               card on /admin that reads the last 30 nights. (2) The report COUNTED what
#               the reviewer refuted without NAMING it -- so a 73% refute rate could not be
#               told apart from a reviewer quietly killing real defects. The report now
#               lists every dismissal with the reviewer's reason, and says how to judge
#               them. The card also warns when a run is near its time ceiling, because
#               losing rotation coverage silently is the one thing this must never do.
#   2026-08-16  APP_BUILD -> "2026-08-16go-night-watch". THE GOVERNOR. Jim: "only AI is
#               gonna be capable of governing AI... depending on me to fix it or notice
#               problems is only going to address some of those problems and probably just
#               the big ones. I need you to set up a system but you are able to catch the
#               things that I cannot catch." Everything we owned was a RATCHET -- fourteen
#               referees and ~4,000 checks, every one of them a thing a human found first.
#               nightwatch.py goes LOOKING: ~12 lessons a night on a rotation, marked by
#               the OpenAI critic, every finding then handed to an independent reviewer
#               whose job is to REFUTE it, only NEW survivors reported, and an email only
#               when there is something to say. It rides the existing heartbeat (no new
#               Render service, nothing for Jim to configure) and is fenced so it can
#               never touch a lesson. Switch: NIGHTWATCH=off.
#   2026-08-16  APP_BUILD -> "2026-08-16gn2-case-is-meaning". CASE IS MEANING. Jim's next
#               Geometry lesson read "A, B, C = corners (vertices)" over "a, b, c = sides
#               (lengths)" and both lines rendered IDENTICALLY, because styleVarsCore
#               forced every styled variable to a capital -- the one line whose job was to
#               separate the two cases destroyed the distinction it taught. A styled letter
#               now renders exactly as written, and the table that decides which letters
#               need context is case-sensitive. session.html / practice.html / topic.html,
#               plus lessonaudit's discipline check 4, which had told the critic that case
#               mixing was invisible to the student. It no longer is.
#   2026-08-16  APP_BUILD -> "2026-08-16gn-screen-auditor". Carries gn on top of gm: the
#               THIRTEENTH referee (triangle_letter_conflict, rule 63(d)) and the new
#               offline screen auditor (screencheck.py + ruletests PART 3aj). Jim ran one
#               Geometry lesson and found four defects by eye in the first turn; nothing we
#               owned could have caught any of them, because every checker read the REPLY
#               or the TRANSCRIPT and all four are born in the RENDER. gn points a checker
#               at the SCREEN, and closes the one of the four that is pure teaching: a
#               triangle whose words named sides a, b, c while the picture lettered only
#               its corners. Rule text: prompts.py GEOMETRY [[triangle]] doc.
#   2026-08-16  APP_BUILD -> "2026-08-16gm-audit-findings". Carries gm on top of gj/gk/gl:
#               the TWELFTH referee, narrated_method_conflict. Rule 43 already forbade
#               narrating a method onto a bare right answer -- it was written 2026-08-13
#               from a live catch -- and the 2026-08-16 audits caught it again three days
#               later: the student typed "1 1/2. Next." and the tutor answered "that
#               regrouping is exactly the move that trips people up, and you nailed it
#               clean." Crediting an unperformed step teaches a child that the step is a
#               word rather than an act, and tells their parent something untrue. The
#               referee fires only when the student showed NO working AND the reply credits
#               a NAMED procedure; praising the answer, and asking rule 59's "how did you
#               get that?", are both untouched.
#   2026-08-16  APP_BUILD -> "2026-08-16gl-audit-findings". Adds gl to gj/gk: the ACCURACY
#               block in every course now also says "fix it SILENTLY -- never let the
#               student watch you change your mind", and tutor.py's eleventh referee
#               enforces it. From the audits' one HIGH: "3/4 is smaller than 3/4... wait,
#               let's just confirm...", shipped to a nine-year-old.
#   2026-08-16  APP_BUILD -> "2026-08-16gk-audit-findings". BUILD gk joins gj: rule 44's
#               coverage test now requires a fraction's two halves to be SAID TOGETHER, so
#               "three plus one really is four" no longer counts as having read "three
#               fourths plus one fourth" aloud.
#   2026-08-16  APP_BUILD -> "2026-08-16gj-audit-findings". BUILD gj -- RULE 41 BECOMES A
#               REFEREE, RULE 37 BECOMES A MEASUREMENT, from the 2026-08-16 lesson audits.
#               (1) tutor.py gains the tenth referee: a figure drawn with NO caption is
#               regenerated. Four were, in the two lessons aimed at the youngest students.
#               (2) _record_unintroduced logs [rule37] when a term that HAS a canonical
#               script is said for the first time without it -- "denominator" to a confused
#               nine-year-old, the same defect as "right angle" in Geometry. It only logs:
#               the visible half of rule 37 is already patched by _bold_first_terms, and
#               whether a term was truly DEFINED cannot be checked mechanically, so a
#               referee there would loop. Measure, then decide.
#   2026-08-14  APP_BUILD -> "2026-08-14gi-termgap-probe". Carries gh (a missing package
#               SKIPS instead of failing the battery) and gi (the term-gap probe: when a
#               student has to ask what a word means and the tutor had just used it, one
#               line is logged saying whether we HAVE a script that went undelivered or
#               have none at all). Both are measurement; neither changes a lesson.
#               _record_term_gap runs BEFORE the turn is appended to history, so the
#               tutor's previous words -- the ones the student is reacting to -- are still
#               the last thing in it. No reply changes, no model call, no student text.
#   2026-08-14  APP_BUILD -> "2026-08-14ge-foundation-coverage". The stamp had gone NINE builds
#               stale (still reading fe from 2026-08-13) while fx, fy, fz, ga, gb, gc, gd
#               and ge shipped, so /health -- whose only job is to answer "did Render take
#               my change?" -- was answering wrongly. Jim hit this live: a board line he had
#               just fixed still looked wrong, and the one instrument that should have told
#               him whether the deploy had landed said "fe". Bumped, the comment widened
#               from "the backend" to anything shipped, and ruletests PART 3ai now FAILS THE
#               BUILD if any shipped file carries a change note dated later than the stamp.
#               The work in this stamp: gb (the foundation block is filtered to the lesson's
#               unit), fz + gc (120 new foundation scripts, 186 -> 306), fx + fy + ge (a
#               finished problem and the opener fold away on the board), ga (the voice stops
#               garbling parentheses; no gate can strand a student), gd (the missing-mark
#               probe), and ge (the "point" script draws points instead of saying it does).
#   2026-08-13  APP_BUILD -> "2026-08-13fe-audit-findings-closed". BUILD STAMP ONLY here
#               -- the work lives in prompts.py (new rule 63, THE WORDS AND THE PICTURE
#               ARE THE SAME FIGURE, plus amendments to rules 4/13/14/17/26/41/43 and
#               four more corrected forms under rule 61), tutor.py (new
#               triangle_side_conflict referee, rule 63c born ENFORCED),
#               foundations.py (the basic "fraction" script loses its false "always";
#               its voice clip re-renders once -- run the /admin pre-render),
#               lessonaudit.py (patient read timeout + one transport retry after two
#               lessons died mid-audit), and ruletests.py (PART 3ah + PART 3w growth +
#               TRIANGLE_CASES). From the five 2026-08-13 lesson-audit runs: 19
#               findings triaged, 16 closed, 3 rejected with reasons recorded in
#               PART 3ah's header.
#   2026-08-13  APP_BUILD -> "2026-08-13fd-showcase-ready". THE PUBLIC PAGES AND THE
#               DEMO, MADE CURRENT FOR BETA TESTERS. Jim: "I'm gonna make a push for
#               seeing if I can get some beta testers... take a look at the pages
#               itself. Take a look at the demos and update the demos that need to be
#               updated. I want everything to be current, ready to go, showcase."
#               No Python changed in this build except this line -- the work is in
#               static/ -- but the build string is what tells Render, and Jim, that the
#               site he is about to show strangers is the one he just looked at.
#               WHAT CHANGED: all six product screenshots re-captured from the CURRENT
#               demo (they dated from 2026-08-04, before Mr. Cadabra's real face and
#               before all four demo doors were rewritten), and the marketing copy that
#               had quietly drifted away from them corrected -- /homeschool said "3h 59m"
#               in three places above a tile reading 2h 15m, /parents' weekly-email
#               preview described a different child's quiz scores than the dashboard
#               beside it, /teachers' alt text counted five students in a picture of six,
#               and /students' alt text described four cards that were not in the frame.
#               NEW ruletests PART 3ag reads those numbers OUT OF demo.html at test time,
#               so the next time the demo's sample student changes, the battery fails the
#               same day instead of leaving a visitor to spot the contradiction.
#               Also driven, not read: every one of the ten demo levels, all four
#               audience doors, and the whole Algebra I lesson to its ending. Clean.
#   2026-08-13  APP_BUILD -> "2026-08-13fc-trial-on-admin". THE FULL-JOURNEY TRIAL MOVES
#               TO THE DASHBOARD. Jim: "is it possible to build that into the admin
#               dashboard? And maybe it could even ask a couple of questions like, what do
#               you want to trial? Or maybe it just runs a trial like you just did, and it
#               reports back to me." Yes: NEW POST /api/admin/course-trial (admin-key
#               gated) + a panel on /admin with two questions -- which course, and how
#               many opening units the student VALIDATES on the assessment -- one button,
#               and a step-by-step report including the exact words the student is told at
#               the locked Final Exam.
#               ⚠️ ISOLATION IS THE WHOLE POINT AND IT IS NOT A DETAIL. The trial invents a
#               parent, a child, a teacher and a class; run against the live database it
#               would litter real data with fakes. So it runs as a SEPARATE PROCESS with
#               DATABASE_URL and DATA_DIR pointed at a throwaway temp directory -- the
#               store is a module-level singleton and there is no safe way to swap its
#               engine underneath a live server. VERIFIED, not asserted: a browser drill
#               counts rows in the "live" database before and after a dashboard run and
#               they are identical.
#               ⚠️ AND IT DECLINES WHEN MEMORY IS TIGHT. A second interpreter importing
#               this app costs ~120 MB (measured); on Render's free 512 MB instance that
#               is affordable but not free, so under 200 MB available it returns a plain
#               explanation rather than risking the OOM killer taking the live site down
#               mid-lesson. Also a 3-minute timeout: a wedged trial reports itself.
#               Caught while building, by driving it rather than reading it: main.py never
#               imported `sys`, so the first version 500'd on every call.
#   2026-08-13  APP_BUILD -> "2026-08-13fb-full-journey". ⭐ A LIVE BUG FOUND BY WALKING
#               A WHOLE COURSE. Jim asked for an end-to-end trial -- one student who
#               validates the first three units on the Course Assessment, works the rest,
#               meets the locked Final Exam, goes back and passes the owed quizzes, takes
#               the exam, and lands a Course Champion medal that shows on the parent AND
#               teacher views. The new tool is course_trial.py, and ON ITS FIRST RUN it
#               failed at the last step: A TEACHER COULD NOT ADD A PARENT-CREATED STUDENT
#               TO A CLASS. "No student with the code 'OTTER5911'" -- for a code that was
#               perfectly valid and whose dashboard, awards and progress all worked.
#               CAUSE: the classroom endpoints predate parent accounts (2026-07-28 vs
#               2026-07-31) and consulted the in-memory STUDENTS dict -- students.json,
#               the four pilot personas -- while _lookup_student has known about BOTH
#               sources since the day parent accounts shipped. So every real customer's
#               child was invisible to the class path: unaddable, and if somehow added,
#               shown with no name and no progress. It would have blocked any school
#               pilot on day one.
#               FIXED in the three places that did it: post_class_student's existence
#               check, _class_public's roster names, and _class_student_row's name
#               lookup -- all now route through _lookup_student. Nothing else in the app
#               had the bug; only the class path was written before parent accounts.
#               Guarded by ruletests PART 3af, which also RUNS course_trial.py on every
#               push, and negative-tested by re-introducing the students.json-only check.
#   2026-08-13  APP_BUILD -> "2026-08-13fa-classroom-locked". ⭐ SECURITY FINDING F2 IS
#               CLOSED -- the last open item from the 2026-08-12 review, and reading the
#               code to fix it showed it was worse than the note said.
#               WHAT WAS WRONG: every class endpoint was UNAUTHENTICATED, and
#               GET /api/class/{code} returned the whole roster INCLUDING every child's
#               login code -- and a student code IS the login (students have no password).
#               One guessed class code handed over every child in that class: their codes,
#               their progress, their transcripts. Those routes never got F1's _read_guard
#               either, so they were enumerable AND unthrottled. The old "teacher code"
#               was documented in this very file as "a door, not a lock", and it was.
#               THE FIX: real teacher accounts mirroring the parent stack -- same PBKDF2
#               hashing, same 30-day token, same single-use emailed reset -- in their own
#               tables, so the live parent/billing path is untouched. A class now has an
#               OWNER (classes.teacher_id) and EVERY read and write goes through
#               _require_teacher + _own_class. A class that exists but is not yours
#               answers 404, never 403: "it exists, it just isn't yours" is a membership
#               oracle on an endpoint family that was an enumeration target already.
#               NEW: /api/teacher/signup · login · logout · me · claim · forgot · reset,
#               and /api/class/{code}/reveal/{ref}.
#               REMOVED: GET /api/teacher/{teacher_code}/classes (a roster of children
#               behind a short guessable key), and the helper _class_or_404, which looked
#               a class up with no ownership check and was what every leaking endpoint
#               reached for -- leaving it would invite the next handler to use it.
#               EXISTING CLASSES (Jim's call): nothing is deleted or orphaned. They start
#               UNOWNED and are taken over either by entering the old teacher code at
#               signup or by claiming a class by code while signed in. Unowned classes
#               can be claimed exactly ONCE; an owned class can never be re-claimed by
#               either path -- both guarantees are enforced inside one transaction in
#               store.claim_class.
#               ROSTER CODES (Jim's call): no class response ships a raw login code any
#               more. Rows carry a masked code plus an opaque ref, and the owning teacher
#               reveals ONE code at a time through its own throttled endpoint. A
#               projected or screenshotted roster no longer leaks thirty logins at once.
#               Guarded by ruletests PART 3ae, which stands the real app up against a real
#               database and drives every endpoint anonymously, as the WRONG teacher, and
#               as the owner -- a source-reading check would have passed on the old code.
#               Negative-tested three ways; the teacher page driven in a real browser.
#   2026-08-13  APP_BUILD -> "2026-08-13ez-hear-him-teach". BUILD STAMP ONLY here -- the
#               work is in static/landing.html, static/demo.html and ruletests.py (NEW
#               PART 3ad). Three regressions Jim found by using the site: the hero's
#               "Hear him teach" button had been hijacked by build eu to play the welcome
#               CLIP instead of the teaching sample (and relabelled itself, so it no
#               longer said what it did); the site welcome now plays on the way INTO the
#               demo instead, with a one-shot marker so nobody ever hears two welcomes;
#               and the after-lesson panel no longer replays the walkthrough dialogue a
#               visitor has already heard.
#   2026-08-13  APP_BUILD -> "2026-08-13ey-he-sequences". BUILD STAMP ONLY here -- the work
#               is in static/session.html (the moment sequencer + the seven in-lesson
#               moments), prompts.py (the NEW [[bye]] tag, lesson-only) and ruletests.py
#               (NEW PART 3ac + "bye" in LESSON_ONLY/TAG_INLINE). PHASE 2 OF THE VIDEO
#               PROJECT IS NOW CODE-COMPLETE: a clip and his live voice can never talk at
#               once, and a clip never replaces the personalised line. Ships DARK -- six of
#               the seven clips are not recorded yet, so today this changes nothing a
#               student can see; the day Jim's recordings land the same code lights up.
#   2026-08-13  APP_BUILD -> "2026-08-13ex-seven-defects-closed". BUILD STAMP ONLY here --
#               the work is in prompts.py (rules 19e/27c/49g/50g/51f/52e + NEW RULE 62,
#               closing all seven verified teaching defects from the 2026-08-12 audits)
#               and ruletests.py (NEW PART 3ab + seven COVERAGE needles). RULES.md
#               regenerated: 62 rules. Ships together with build ew below in one push.
#   2026-08-13  APP_BUILD -> "2026-08-13ew-placement-is-honest". PLACEMENT NEVER PASSES A
#               UNIT, AND THE FINAL EXAM GATE IS DERIVED, NOT HARD-CODED. Jim's policy:
#               "a student who places into the middle of a course should NOT get a pass on
#               the earlier units just for answering a few placement questions right."
#               The 2026-08-13 status doc claimed that policy was already in force. IT WAS
#               NOT: challenge.html's finish() posted one /api/check per unit with the
#               placement per-unit scores, record_check marks a unit mastered at >= 90%,
#               and _final_exam_state reads that same unit_checks table -- so 5/5 on a
#               unit's five placement questions silently mastered the unit, and a student
#               who aced the whole assessment could unlock the Final Exam without ever
#               taking a Unit Quiz. The earlier investigation read the placement TABLE
#               (which is indeed inert) and missed the side-channel in the page. FIXED at
#               the source: challenge.html no longer posts /api/check at all; the per-unit
#               results now ride INSIDE the placement payload (PlacementIn gains
#               `strengths` + `units`, stored in the placements JSON blob -- no schema
#               change), which also lights up two dormant consumers that always read
#               placement.strengths and always got nothing: the dashboard's strengths
#               chips and the tutor prompt's "Strengths:" line. NOTE ON OLD DATA: checks
#               already seeded by past placements cannot be told apart from real quiz
#               scores retroactively; dev-phase data, accepted and recorded here.
#               SECOND FIX, same build: _final_exam_state returned "required": 9 and
#               unlocked at nine mastered units REGARDLESS of course -- correct today only
#               because all ten courses happen to have nine units. Now derived from
#               curriculum.units_for(course) (fallback 9 if that ever errors), and the
#               gate messages (FINAL_GATE_MESSAGE + _final_gate_message) carry the derived
#               count instead of a literal "of 9" / "all nine". session_state's pre-DB
#               fallback dict derives the same way. prompts.py's FINAL notes reworded
#               count-neutral ("every unit of the course"). ruletests PART 3aa pins ALL of
#               it: no /api/check in challenge.html, placement payload carries its units,
#               the honest sentence on the result screen, no "required": 9 literal, the
#               derivation present, and record_check unreachable from any placement path.
#   2026-08-13  APP_BUILD -> "2026-08-13ev-he-speaks". THE FIRST TWO TALKING CLIPS ARE LIVE
#               (build stamp only here; the assets are static/videos/cadabra/ and the work
#               is in tutor-moments.js, tutor-face.js and landing.html). Jim recorded
#               site_welcome and demo_welcome in ElevenLabs and generated them in HeyGen,
#               portrait, same avatar. Post-produced to 540x960 H.264/AAC (1.35MB + 1.15MB)
#               with a poster frame and moments.json carrying each clip's words as caption
#               text. mp4 ONLY, deliberately: VP9/webm encoded LARGER than the mp4 here
#               (1.53MB vs 1.15MB) and H.264 plays in every consumer browser; the player
#               takes <source> lists so another encoding is a manifest edit, never a code
#               change. ⚠️ A REAL BUG CAUGHT IN TESTING, and it was latent since build ep:
#               a <video> whose every <source> fails does NOT fire an error event on the
#               ELEMENT -- the spec routes those errors to the <source> tags and the element
#               settles into networkState 3 in silence. Proven in this container's Chromium,
#               which has no H.264: the demo card opened and the tour never started. Fixed
#               in BOTH files (_sourcesFailed / sourcesFailed) -- which also repairs the
#               presence layer, where an undecodable clip would have sat on a dead poster
#               instead of tearing down to the robot. The landing button now also retires an
#               unplayable clip and gives the visitor the audio sample on the same click.
#               Guarded in PART 3u and 3u2.
#   2026-08-12  APP_BUILD -> "2026-08-12eu-he-steps-out". PHASE 2 OF THE VIDEO PROJECT, THE
#               CODE HALF (build stamp only here; the work is in the NEW
#               static/tutor-moments.js plus landing.html and demo.html). Phase 1 is the
#               silent corner presence and does not change. This is the other half: a few
#               one-time clips in which Mr. Cadabra really speaks, in his real voice. It is
#               a SEPARATE file from tutor-face.js deliberately -- these clips have sound,
#               and the presence layer's "the corner never makes a sound" guarantee is
#               enforced by a test that reads that file, so keeping them apart keeps the
#               guarantee absolute. THE VOICE RULE: a clip and his live voice never talk at
#               once -- play() returns a promise and every caller waits for it. Ships DARK:
#               with no moments.json (today) every page behaves exactly as it does now; the
#               day the recordings land the same callers light up. Wired at the two moments
#               where NO live voice competes: the landing hero button ("Meet Mr. Cadabra")
#               and the demo opener, where the clip replaces the synthesised WELCOME_LINE.
#               The seven in-lesson moments wait for the voice-sequencing work. Guarded in
#               PART 3u2.
#   2026-08-12  APP_BUILD -> "2026-08-12et-two-intensities". THE RING HAD ALMOST NOTHING TO
#               FIRE ON (build stamp only here; the work is in prompts.py,
#               static/tutor-face.js and the three teaching pages). es shipped and Jim
#               still saw nothing, so I fired celebrate() by hand on the live site: the
#               ring drew perfectly. The fault was upstream, in the prompt text every
#               course carries -- "Silently, during normal practice, when the student
#               COMPLETES a problem you MAY record whether they got it right... not for
#               every small sub-step." Optional, and sub-steps excluded, so during a
#               teaching lesson the doorbell was almost never pressed. Two consequences,
#               both fixed: the celebration never fired, AND problems-practiced/accuracy
#               have been under-counting for every student since those numbers existed.
#               [[mark]] is now REQUIRED on a finished problem (one canonical paragraph
#               replacing nine slightly different ones), and NEW [[nice]] marks a correct
#               answer along the way -- at most one per reply, never alongside [[mark]],
#               never while correcting, no tally, no server call. The pages draw a quieter
#               single ring for it. Guarded in PART 3u, including a check that reads
#               prompts.py and fails if "you may record" ever comes back.
#   2026-08-12  APP_BUILD -> "2026-08-12es-celebration-is-ours". THE THUMBS-UP CLIP HAS NO
#               THUMBS IN IT (build stamp only here; the work is in static/tutor-face.js).
#               Jim, after er deployed: "I'm answering questions correctly and I'm not
#               getting a thumbs up... maybe he's giving a thumbs up outside the range of
#               the circle." Frames pulled from the raw HeyGen source and from the shipped
#               crop settle it: the avatar never raises a hand at ANY crop -- it is a
#               chest-up photoreal presenter that does not gesture, so the "thumbs_up"
#               clip is a slightly warmer smile, invisible at 70px beside the idle loop.
#               The trigger built in er works; there was simply nothing to see. So the
#               celebration no longer depends on the avatar: a gold ring pulse, flash and
#               sparkles are drawn in the same circular slot over the video, the poster or
#               the bare robot, on EVERY correct answer, with an opacity-only variant under
#               prefers-reduced-motion. The happy one-shot still plays underneath when the
#               presence is live. Guarded in PART 3u.
#   2026-08-12  APP_BUILD -> "2026-08-12er-thumbs-up-works". THE THUMBS-UP HAD NO
#               TRIGGER (build stamp only here; the work is in static/tutor-face.js and
#               the three teaching pages). Jim, looking at the deployed site: "all I'm
#               seeing is a little circle ahead of Mister instead of the robot. Nothing
#               else." He was right, and the reason was concrete: the pages' setState
#               only ever holds speaking / listening / thinking / idle, so mood "happy"
#               was never once passed to the presence layer and the thumbs-up clip --
#               generated, shipped, listed in the manifest -- could not play in a real
#               lesson. A clip nothing can trigger is a clip that does not exist. NEW
#               TutorFace.celebrate() fires that one-shot directly WITHOUT touching
#               `state`, so the busy glow, the thinking flag and the level meter (which
#               all read it) are undisturbed; session/practice/topic ring it the moment
#               the tutor MARKS a correct answer. Verified live: idle -> thumbs-up ->
#               back to idle, no page errors. Guarded in PART 3u so the doorbell cannot
#               be removed without failing the build.
#   2026-08-12  APP_BUILD -> "2026-08-12eq-reply-integrity". TWO MECHANICAL GUARDS from
#               the 2026-08-12 audits (build stamp only here; the work is in tutor.py
#               and ruletests.py PART 3z). (1) NEW malformed_tag_conflict, running
#               FIRST in the referee sweep: eight referees existed and not one checked
#               that a board tag could be PARSED, so a missing closing quote reached a
#               Basic Math student as one answer button reading '"yes,' with the second
#               choice absent. (2) The rule-44 referee had two blind spots that six
#               findings in five lessons walked straight through -- it required TWO
#               numeric tokens (a fraction counts as one, so an entire fraction quiz
#               was invisible while the tutor said only "this fraction"), and any
#               number anywhere in the prose exempted the whole reply. Now one stated
#               quantity qualifies and the test is whether the words carry THIS
#               problem's numbers. Both verified against the real audit strings, on
#               both sides: the offending lines caught, the innocent lines from the
#               same transcripts untouched.
#   2026-08-12  APP_BUILD -> "2026-08-12ep-cadabra-is-here". THE ROBOT IS RETIRED --
#               Mr. Cadabra's real face is live in the corner of every teaching page
#               (build stamp only here; the work is in static/tutor-face.js, the new
#               static/videos/cadabra/ assets, and ruletests PART 3u). Jim generated
#               the four presence loops in HeyGen from the near-silent audio kit; they
#               came back 1080x1920 portrait and were cropped to the circular slot,
#               loop-sealed with a 1-second crossfade, and encoded twice: 105 MB of raw
#               footage became 368 KB of web assets. ONE MACHINERY CHANGE: a manifest
#               clip is now a LIST of encodings (webm/VP9 then mp4/H.264) rendered as
#               <source> children so the BROWSER picks what it can decode -- which is
#               how this was caught, the mp4s tearing down to the robot in a headless
#               test with no proprietary codecs. Verified live against the real app:
#               presence mounts and PLAYS, all five moods map correctly (speaking still
#               deliberately shows the idle loop -- his voice talks, the face never
#               fakes a mouth), reduced-motion gets the still poster, and any media
#               failure still lands on the robot underneath.
#   2026-08-12  APP_BUILD -> "2026-08-12en-diagnosis-and-symbols". THE LAST TWO AUDIT
#               ITEMS (build stamp only here; the work is in prompts.py, notation.py
#               and ruletests.py). (1) RULE 49 GAINS (f): when a student NAMES their
#               own rule out loud, that is evidence, not a hypothesis, and it is the
#               rule you answer -- the audit caught a reply explaining that 3x2 is not
#               3+2 to a student who had just said "we do 5 plus 3 first because it's
#               on the left", so their real rule survived until they objected. (2) TWO
#               NOTATION REGISTRY GAPS CLOSED: bare < and > were absent entirely (only
#               the or-equal pair, and not for elementary) though comparing fractions
#               is core Basic Math and the audit caught "1/4 > 1/8" written and never
#               read aloud; and the imaginary unit was absent though algebra2 teaches
#               complex numbers. Both patterns dry-run against every authored board
#               string before shipping, and PART 3y pins the false-positive behaviour
#               (arrows are not inequalities; x_i is not the imaginary unit).
#               THE 2026-08-12 AUDIT LIST IS NOW CLOSED except the two items
#               deliberately declined (see WHEN_YOU_ARE_BACK).
#   2026-08-12  APP_BUILD -> "2026-08-12em-countable-fractions". THE FRACTION PIE (the
#               2026-08-12 audit's one HIGH finding; build stamp only in this file --
#               the work is in static/math-figures.js, foundations.py, prompts.py and
#               ruletests.py). A board captioned "one whole, cut into four equal parts"
#               drew TWO wedges (a quarter and a three-quarter lump) and printed "the
#               rest 75%" beside a picture teaching one fourth -- then the lesson asked
#               a beginner "how many pieces are shaded?" over ONE shaded wedge and the
#               student answered "3", which they cannot have counted. Traced to FIVE
#               canonical foundation board lines, not a live slip. NEW equal-parts mode
#               [[pie parts="4" shaded="3"]]: N separated countable wedges, K filled,
#               capped at 12, and printing NO text at all -- because a percentage on a
#               fractions board answers the question the tutor is about to ask (rule 6).
#               The proportional data= form is untouched and still correct for unequal
#               categories (spinners, surveys). Guarded by PART 3x, which renders the
#               real SVG with node and counts the wedges rather than trusting the
#               source, and which fails if any authored board line ever goes back.
#   2026-08-12  APP_BUILD -> "2026-08-12el-generalizations". NEW RULE 61: A
#               GENERALIZATION CARRIES ITS CONDITION (build stamp only in this file;
#               the work is in prompts.py, foundations.py and ruletests.py). From the
#               2026-08-12 lesson audits, which caught FIVE false universal claims
#               across calculus, algebra1 and algebra2 -- all the same failure, a
#               helpful heuristic spoken as a law, and all invisible to mathcheck
#               because there is no arithmetic in the word "always". Rule 61 carries
#               the five real catches with their true forms and forbids the obvious
#               overcorrection (true absolutes stay crisp). ALSO: one of the five was
#               not a live slip -- it was the algebra1 function-notation FOUNDATION
#               SCRIPT, spoken verbatim; corrected in foundations.py, so its cached
#               audio re-renders once (run the /admin foundation pre-render after
#               deploying to pay that once, up front). Guarded by new PART 3w, which
#               bans the five SENTENCES from all authored content -- never the word
#               "always" -- and was negative-tested both ways.
#   2026-08-12  APP_BUILD -> "2026-08-12ek-course-identity". ONE TRUE NAME PER COURSE --
#               a live teaching defect in the two YOUNGEST courses (build stamp only in
#               this file; the work is in curriculum.py, notation.py, misconceptions.py,
#               foundations.py, lessonaudit.py and ruletests.py). THE DEFECT: this file
#               validates an incoming course against curriculum.COURSES, whose keys are
#               "entry" and "basic" -- but the three CONTENT modules filed the same two
#               courses under "entrymath" and "basicmath". So every real Entry-Level and
#               Basic Math lesson asked those modules for their content and got NOTHING:
#               misconception catalogue 0 bytes (rule 49 had no rules to look up),
#               foundation scripts 0 bytes (rules 36-38 had no canonical wording),
#               notation table 0 bytes (rule 48 had no registry). Measured, then fixed.
#               It hid because ruletests.py and lessonaudit.py used the phantom
#               spellings too -- the tests and the content agreed with each other and
#               both disagreed with production. NOTHING IS RENAMED IN THE STORE: the
#               new curriculum.canon() resolves the legacy spellings forward, so any
#               student row, mastery record or bookmark written under the old name still
#               lands on the right course instead of silently falling back to Algebra I.
#               Guarded by new ruletests PART 3v (20 checks), which was negative-tested:
#               re-introducing the bug fails the build.
#   2026-08-12  APP_BUILD -> "2026-08-12ej-video-presence". THE VIDEO PRESENCE LAYER,
#               PHASE 1 (build stamp only in this file; the work lives in
#               static/tutor-face.js + new PART 3u in ruletests.py; the full design
#               is claude/Video_Presence_Project_Plan_2026-08-12.md). Jim is retiring
#               the canvas robot in favor of Mr. Cadabra's real face: a one-time
#               HeyGen video library (scripts + audio kit delivered 2026-08-12) --
#               muted presence loops in the corner (idle/listening/thinking + a
#               thumbs-up one-shot on "happy"), robot kept as the always-drawn
#               fallback under any failure, reduced-motion gets a still poster.
#               SHIPS DARK: until static/videos/cadabra/presence.json + clips land,
#               every page behaves exactly as before. No page edits -- the layer
#               hangs off the TutorFace.draw call all six coaching pages already make.
#   2026-08-12  APP_BUILD -> "2026-08-12ei-teachers-demo". THE TEACHERS DEMO DOOR:
#               ASSISTANT, NOT REPLACEMENT (Jim: teachers see three wins -- helps
#               me, helps my students, individualized pace -- and one threat: "am I
#               really going to let an AI run my class and replace me?"). THIS
#               FILE: five lines APPENDED to DEMO_VOICE_LINES (238 -> 243),
#               identical to demo.html's VOICE_LINES -- a new intro that opens
#               "I am not here to replace you" and closes "your class stays yours",
#               new words for teacher stops 1/5/9 (the assistant who does what no
#               teacher has thirty hours a day for · needs-attention as triage that
#               frees them from one-pace-fits-all, "no class learns at one speed" ·
#               "I gather the picture, you make the teaching decisions"), and a new
#               outro naming what it DOESN'T do (plan lessons, grade judgment, run
#               the room). Tour untouched: nine stops, same panels, same order.
#   2026-08-12  APP_BUILD -> "2026-08-12eh-students-demo". THE STUDENTS DEMO DOOR
#               CHARMS THE CHILD AND REASSURES THE PARENT (Jim: parents try the
#               student door as if they were their child). THIS FILE: four lines
#               APPENDED to DEMO_VOICE_LINES (234 -> 238), identical to demo.html's
#               VOICE_LINES -- new students intro ("I really talk, and I really
#               listen" -- say it out loud, he hears you, you work it out together),
#               a new ask-me-out-loud honest-read stop (no mystery numbers, no
#               report-card code), a trophy-case stop that makes EARNING the point
#               ("nobody can give you these -- not me, not anyone"), and a new outro
#               carrying the two safety promises a listening parent needs: math ONLY
#               (anything else gets a smile and a steer straight back) and never
#               just handing over the answer. Tour untouched: same ten stops, same
#               panels, same order. Clips render on first play or via pre-render.
#   2026-08-12  APP_BUILD -> "2026-08-12eg-parents-demo". THE PARENTS DEMO DOOR
#               SPEAKS TO WHAT A PARENT ACTUALLY ASKS (Jim, from a parent-teacher
#               conference: a teacher shows the app -- what does the parent want to
#               know? "Is my child actually learning" and "will she actually want to
#               do this"). THIS FILE: seven lines APPENDED to DEMO_VOICE_LINES
#               (227 -> 234), identical to demo.html's VOICE_LINES -- new parents
#               intro, new words for parent stops 1/2/4/5/8 (conference question ·
#               teaches-never-hands-answers · one-record + the streak nobody can
#               assign · kitchen-table + missed-problems-come-back · trophy case as
#               the will-she-use-it answer), and a new outro carrying the
#               voice-privacy answer. The tour structure is untouched: same ten
#               stops, same panels, same order; HS_STOPS unchanged. Clips render on
#               first play or via the admin pre-render.
#   2026-08-12  APP_BUILD -> "2026-08-12ef-homeschool-pitch". THE CONFERENCE PITCH
#               REWORK of /homeschool (build stamp only in this file; the work lives
#               in static/homeschool.html + new ef guards in ruletests.py). Jim,
#               pitching at a homeschooling conference: same content, new spine --
#               records/filing day FIRST, honest hours as its evidence, the mastery
#               bars named (80/90, never rounds up), a new "You're still the teacher"
#               section (steer + placement + works-with-your-curriculum), a new "The
#               trust questions" section (four calm answers: never a bare answer, the
#               separate math-engine check, voice audio deleted immediately -> links
#               /privacy, something-bigger-than-math -> a trusted adult), and a
#               method line naming the WWC guides. No dollar figure on the page --
#               prices live on /pricing alone. FAQ byte-identical (eb guards).
#   2026-08-12  APP_BUILD -> "2026-08-12ee-teaching-upgrades". THE FIVE TEACHING
#               UPGRADES (prompt lane; claude/Teaching_Evidence_Base_2026-08-10.md).
#               No route or logic changes in THIS file -- the build stamp only. The
#               work lives in: prompts.py (rules 56-60: find-the-error,
#               self-monitoring, two-ways-one-board, right-answer-wrong-method, the
#               board spotlight), the three teaching pages session/practice/topic
#               (the [[highlight]] tag gains id="line" and id="board" -- board work
#               glows while teaching; self-clears; reduced-motion safe), and
#               ruletests.py (new PART 3t; coverage needles; the 150k prompt ceiling
#               raised to 160k per Jim's standing 2026-08-11 decision).
#   2026-08-12  APP_BUILD -> "2026-08-12ed-read-throttle". SECURITY PASS 2 -- finding F1
#               (claude/Security_Review_2026-08-12.md). The GET-by-code reads that return a
#               child's data (session, records, misses, awards, time, topics, assessment,
#               placement, courses, sprints, sprint) were enumerable and UNTHROTTLED -- a
#               short code was the only key. Two-part fix:
#               (A) _read_guard(request, code) now fronts every one of those endpoints. It
#                   applies a generous per-IP raw read cap (READ_IP_LIMIT=600/5min) AND the
#                   real anti-enumeration guard: a per-IP DISTINCT-CODE ceiling
#                   (CODE_PROBE_MAX=50 distinct codes / CODE_PROBE_WINDOW=900s). A family
#                   re-reads its own 1-2 codes forever (never trips); a scraper walking
#                   thousands of DIFFERENT codes is refused after ~50. Self-pruning,
#                   in-process, env-tunable. Pairs with the ec F3 fix (an IP can't be
#                   spoofed, so the cap can't be dodged by rotating addresses).
#               (B) _new_student_code widened 2 -> 4 digits: 50 x 9000 = 450,000 (was
#                   4,500), a ~100x space. Existing 2-digit codes keep working (nothing
#                   validates digit count); only NEW codes are longer. Still one friendly
#                   word + a number for a child to type.
#               Guards: ruletests "BUILD ed" block (every read endpoint calls _read_guard;
#               the generator is 4-digit) + a live SEC2-DRILL (enumeration from one IP
#               hits 429; a fresh IP is unaffected; same-code re-reads never trip; new
#               codes match WORD+4digits). F2 (class lock) remains for the teacher-auth build.
#   2026-08-12  APP_BUILD -> "2026-08-12ec-security-hardening-1". SECURITY PASS 1 of the
#               review in claude/Security_Review_2026-08-12.md (Jim: "make sure our security
#               is robust"). Three low-risk, universal fixes:
#               F3 -- _client_ip no longer trusts the SPOOFABLE leftmost X-Forwarded-For
#                     entry (a visitor could prepend a fake and slip the per-IP brute-force
#                     limits on sign-in / signup / password-reset). It now trusts only the
#                     rightmost TRUSTED_PROXY_HOPS entries (default 1 = the address Render
#                     appended) -- un-spoofable behind our own proxy.
#               F4 -- a new @app.middleware stamps the standard browser-hardening headers on
#                     EVERY response: nosniff, X-Frame-Options SAMEORIGIN, Referrer-Policy,
#                     HSTS, a mic-only Permissions-Policy, and a Content-Security-Policy in
#                     REPORT-ONLY mode (our inline styles/scripts + Plausible mean an
#                     enforcing CSP could blank the site; report-only describes it safely
#                     and can be flipped on later with a nonce refactor).
#               F5 -- /api/transcribe caps the audio it reads at MAX_AUDIO_BYTES (12 MB,
#                     env-tunable) and returns a clean 413 over it, instead of pulling an
#                     unbounded upload into memory. The catch-all except now re-raises
#                     HTTPException so the 413 actually reaches the caller.
#               Nothing else changed. Guards: ruletests PART 3 "BUILD ec" block (source
#               checks + a live TestClient drill proving headers ship and XFF is read from
#               the trusted end). F1 (read-by-code throttle) and F2 (class lock) are the
#               next two builds, per the review's proposed order.
#   2026-08-11  APP_BUILD -> "2026-08-11eb-features-faq". CALM FEATURES PAGE + FOUR
#               AUDIENCE FAQs (Jim: "the features page has too much information... I don't
#               like the icons... just bullet points... consolidate... drop-downs" + "a FAQ
#               section on the bottom of the homeschool, parent, teacher and student pages
#               ... DIFFERENT FAQs"). Static-only build -- nothing in this file changed but
#               the stamp. features.html: one calm column of six <details> drop-downs,
#               features as plain bullets (bold name + one line), NO emoji icons, 30 -> 41
#               features (the eleven shipped since the last rewrite: sprints, refresher,
#               save/resume, retake, tricky-ones x2, steer, child management, phone dock,
#               a11y, /help). students/parents/homeschool/teachers .html each end with an
#               8-question FAQ in that audience's own voice; no question repeats across
#               pages; every answer states only what the product does today. homeschool
#               also lost its phantom "parent code" line (same dq honesty fix as parents).
#               Checks: ruletests PART 3p eb block (icon-free features page, new features
#               present, four disjoint FAQs, parent-code guard extended to homeschool).
#   2026-08-11  APP_BUILD -> "2026-08-11ea-pacing-steer". THE PACING CONTROL (Four-Lens
#               homeschool item 3; the parent-as-teacher design Jim approved 07-28).
#               A parent can now set ONE standing plan per child on /family: "center
#               sessions on Unit N for now." NEW POST /api/parent/student-steer
#               (parent-gated + ownership-checked; unit=0 clears; course defaults to
#               where the child actually works, resolved server-side so no page grows
#               a seventh course list). Applied by _resolve_focus in the chat handler:
#               the child's OWN explicit focus always outranks the plan (rule 50), and
#               the mastery note words it honestly -- "their parent asked", introduced
#               as today's plan, never as the student's request, never a punishment,
#               and the student's agency wins if they ask for something else. The
#               steer shows on /family (overview carries it) until changed or cleared;
#               it survives a dy code regeneration and dies with a reset.
#   2026-08-11  APP_BUILD -> "2026-08-11dz-a11y-and-phones". ACCESSIBILITY + PHONE
#               PASS (Four-Lens student items 5 and 8). Nothing in this file changed
#               but the stamp: on all three teaching pages the transcription readout
#               and your-turn hint are polite aria-live regions, the mic button has a
#               spoken name, the orb is decorative, session's four overlays are real
#               dialogs (welcome focuses its action), and prefers-reduced-motion
#               stills every pulse. PHONES: the board comes FIRST and the left rail
#               becomes a compact bottom DOCK (orb+status row, horizontal nav chips,
#               mic and answer box always in reach). Desktop untouched; all inside
#               the existing 900px media query.
#   2026-08-11  APP_BUILD -> "2026-08-11dy-child-management". FOUR SUPPORT EMAILS
#               BECOME FOUR BUTTONS (Four-Lens parent item 2). New parent-token-gated,
#               ownership-checked endpoints: /api/parent/student-rename ·
#               student-newcode (a leaked login code is a leaked key: fresh code
#               minted, EVERY per-student row moves with it in one transaction via
#               store.change_student_code, old code dies instantly) · student-remove
#               (permanent; the parent must TYPE the child's name back, and the
#               server verifies it -- then the same cascade Start Fresh uses) ·
#               student-attach (claim an UNOWNED code; another family's code returns
#               409 with a support hand-off; shared demo codes refused). Ownership
#               misses return 404, not 403 -- an outsider probing codes learns
#               nothing. family.html grows the ⚙ Manage panel per child + the
#               attach link under Add-a-child.
#   2026-08-11  APP_BUILD -> "2026-08-11dx-assessment-save-resume". THE 45-QUESTION
#               ASSESSMENT SURVIVES A CLOSED TAB (Four-Lens student item 4). Nothing
#               in this file changed but the stamp: challenge.html now saves the run
#               state on the student's device after EVERY answer (the question order
#               is deterministic, so the whole state is four numbers and nine
#               per-unit counts), offers "Pick up where you left off -- question N of
#               45" on the start panel for 48 hours, clears on finish and on a
#               deliberate fresh start, and discards the save if the question bank
#               itself changed between visits. Same-device only, by design.
#   2026-08-11  APP_BUILD -> "2026-08-11dw-refresher-and-three-bars". TWO MORE OF JIM'S
#               LIVE CATCHES. (1) THE GAP-AWARE OPENER: "welcome back, we were looking
#               at this chart, ready to keep going?" is fine after lunch and useless
#               after four days. The opener branch now computes the days since the
#               last session in THIS course (store.get_course_activity, fail-open)
#               and, at 1+ days, orders a REAL refresher: name the unit and topic,
#               say plainly what you were working on and what they'd already nailed,
#               board the key thing, one gentle memory-jog question -- "a friend
#               catching you up, never a test." (2) THREE BARS, ALWAYS: the TODAY bar
#               was routinely missing on resumed sessions -- the tutor announced no
#               goals, ensure_today_tag can only mirror announced goals, and
#               yesterday's stored goals rightly don't rebuild today. Now the server
#               KNOWS when the bar is empty (today_live) and hands the opener a
#               per-turn ORDER to state the 2-3 item plan and emit [[today items]];
#               session.html additionally shows the labeled TODAY placeholder from
#               the first second, so the wall never has fewer than three maps. Both
#               notes are per-turn dynamic text -- zero static prompt cost.
#   2026-08-11  APP_BUILD -> "2026-08-11dv-sprint-buzzer-shield". JIM'S OWN LIVE CATCH:
#               he answered a sprint's last question exactly as the 60 seconds ended;
#               the timer swapped the panel under his click, the click landed on
#               "Start my lesson ▶" (same screen spot as the answer buttons), and the
#               whole A/B celebration vanished before he saw it. Nothing in this file
#               changed but the stamp: session.html's sprShow() gained a shield --
#               any sprint panel swapped in BY THE TIMER (stretch break, results)
#               keeps its buttons inert and dimmed for 1.2 seconds, so a
#               buzzer-beater click can never dismiss the results. Deliberate-tap
#               panels are unshielded. His sprint DATA was never at risk (the POST
#               fires before the panel can be dismissed) -- what vanished was the
#               celebration, which is half the point of the feature.
#   2026-08-11  APP_BUILD -> "2026-08-11du-retake-and-parent-view". TWO DOORS ON TOP OF
#               dt's FOUNDATION. (1) THE RETAKE BUTTON (Four-Lens student item 2): the
#               dashboard's "Unit Quiz best 62% -- let's get it to 90%" line finally
#               has a button. "📝 Retake the Unit Quiz →" opens /session?...&quiz=1;
#               session.html treats it like the Final-Exam door (no tour, no side
#               offers, welcome button says what it does) and sends the NEW
#               "__unit_quiz__" sentinel; this file turns it into marching orders --
#               administer the focus unit's quiz NOW, remind them the record keeps
#               their BEST (rule 50), never make them ask again; warm-up offered only
#               if the notes show unmet topics. (2) THE PARENT'S ANSWER (parent item
#               6, unlocked by dt): the parent box and the Friday email's per-child
#               section both gain the actual missed problems ("Recently tricky" /
#               "Tricky this week"), max 3, with the child's own answers -- absent
#               entirely when there were none.
#   2026-08-11  APP_BUILD -> "2026-08-11dt-missed-problems". THE DATA FOUNDATION
#               (Four-Lens student item 1, NEW RULE 55): until today a 62% Unit Quiz
#               stored ONLY "62%" -- nobody, including the tutor next session, could
#               see WHICH problems were missed. Now: the tutor reports each miss in
#               the tag (missed="question => their answer | ...", rule 55a -- the
#               tutor is the only one who knows what was asked); /api/quiz,
#               /api/check, and /api/final accept the list via _keep_misses (HONESTLY
#               CLAMPED: never more entries than total-correct, <= 25, fail-open so a
#               malformed list never costs the score); store.quiz_misses keeps the
#               newest 200 per student and joins the reset family day one. Surfaced
#               three ways: NEW GET /api/misses/{code} feeds the dashboard's
#               "Tricky ones" card; _mastery_note hands the last 5 back to the tutor
#               with rule 55(b)'s marching orders (revisit exactly ONE, early, as a
#               fresh similar problem -- spaced retrieval, never a re-test); and the
#               parent's "what did she struggle with?" becomes buildable later from
#               the same rows.
#   2026-08-11  APP_BUILD -> "2026-08-11ds-sprints-anytime-help". TWO STUDENT-LENS FIXES
#               (Four-Lens Review items 3 and 6). (1) HELP THAT WORKS FOR A KID: new
#               /help route + static/help.html, a student-first FAQ (sign-in, mic,
#               sound, "I'm confused" is a power move, nothing is lost on refresh) with
#               a grown-ups section (family page, teacher tool, support address as
#               TEXT a kid can show a parent). app-nav.js's Contact pill -- a mailto:
#               dead on school Chromebooks -- is now ❓ Help -> /help on every app
#               page, and challenge.html (the highest-stakes page, which had NO help
#               affordance at all) gains the same link. (2) SPRINTS ON REQUEST: the
#               dashboard sprint card gains "⚡ Run one now" -> /session?...&sprint=1,
#               which starts the sprint directly; before, sprints were startable ONLY
#               from the lesson-open offer, so a student who skipped it had no way
#               back. Card still hidden until a first sprint exists; parent/teacher
#               view never shows the button; no sprint for the unit fails soft.
#   2026-08-11  APP_BUILD -> "2026-08-11dr-elementary-voice". THE YOUNGEST STUDENTS GET
#               A VOICE (Jim: "I think it's okay for the youngest to have a way to talk
#               as well"). Nothing in this file changed but the stamp: session/practice/
#               topic drop canRecord's !IS_ELEM exclusion (entry/basic students -- the
#               ones least able to type -- get the same tap-to-talk mic as everyone
#               else, with the tap answer buttons unchanged beside it), and prompts.py's
#               how-they-answer note tells the tutor they may speak, with EXTRA
#               transcription charity for young readers. The transcribe/speak pipeline
#               is untouched -- it never cared what course the audio came from.
#   2026-08-11  APP_BUILD -> "2026-08-11dq-family-mission-control". THE LINKS-AND-COPY
#               BATCH (Four-Lens Review, order-of-attack item 1 -- Jim: "fix all the
#               things you found that you think you can fix"). /family becomes
#               MISSION CONTROL: NEW GET /api/parent/overview (parent-token gated,
#               one call) gives each child's real minutes this week, active days,
#               units mastered, last-active, and most-worked course; NEW POST
#               /api/parent/weekly-email is the in-product Friday-report toggle
#               (before: the only switch was the tokenized link inside the email).
#               family.html gains per-child stat lines, a Records link (the
#               homeschool page's "one click from your parent view" is finally
#               TRUE), an inline "How are they doing?" narrative per child, and the
#               email toggle. parents.html drops two promises the product doesn't
#               make (there IS no separate read-only parent code -- the parent door
#               takes the child's code; parent accounts are LIVE, not "rolling out")
#               and points at /family. teachers.html finally links to the real
#               /teacher tool. records.html's bare-visit message points at /family.
#               Marketing-copy discipline going forward: copy ships in the same
#               build as the feature it describes.
#   2026-08-11  APP_BUILD -> "2026-08-11dp-sprints-all-courses". FLUENCY SPRINTS REACH
#               EVERY COURSE. The registry (sprints.py) grows from the 3 elementary
#               courses to ALL TEN -- 70 units with a genuine 60-second recall skill
#               (one-step solves, slopes, factor pairs, special angles, the power
#               rule, Laplace facts...); concept units get no sprint ON PURPOSE.
#               Nothing in this file changed but the stamp: the offer, endpoints,
#               store, and dashboard card were built course-agnostic in dd/dm and
#               light up for the new courses on their own. Every computed answer is
#               formula-derived and the battery's oracle now arithmetic-proves the
#               question shapes; every fixed FACT list (trig values, i-powers, the
#               68-95-99.7 rule, derivatives, identities...) is re-derived from
#               mathematics (sympy/erf/complex) on every battery run. Also fixed in
#               sprints.py, found by this build's probe: negative answers had been
#               starved to a SINGLE tap choice by a no-negatives distractor rule
#               meant for the counting courses (live since dd in prealgebra unit 3).
#               Anxiety rules unchanged: never gates, personal-best only.
#   2026-08-11  APP_BUILD -> "2026-08-11do-prompt-split". THE WORDS AND THE MACHINERY
#               NOW LIVE APART. tutor.py (539 KB) was two-thirds prompt TEXT; all of
#               it moved VERBATIM into the NEW prompts.py (353 KB of pure text, no
#               logic -- the battery now enforces that boundary by AST), leaving
#               tutor.py a 190 KB engine. Proven byte-identical: 52 built prompts
#               (every course x lesson/first-meeting/practice/topic + final modes +
#               standalone constants) hashed before and after -- 52 of 52 equal, so
#               NOTHING the model reads changed and no cached audio or behavior can
#               shift. Nothing in this file changed but the stamp; tutor.py re-exports
#               every moved name, so main.py's imports work untouched. From here on:
#               edit the WORDS in prompts.py, the MACHINERY in tutor.py. NEW FILE
#               prompts.py rides this push.
#   2026-08-11  APP_BUILD -> "2026-08-11dn-modkey-header". THE LAST KEY-IN-A-URL
#               RESIDUAL IS CLOSED. Build dg moved the admin key out of query strings
#               (Render logs them in plaintext) but left one documented residual: the
#               forum-moderation unlock was /community?mod=<key>, and the moderate
#               call carried the key in its JSON body from a URL-sourced variable.
#               Now: POST /api/forum/moderate accepts the key in the X-Admin-Key
#               HEADER (preferred) via the same _require_admin() constant-time gate
#               as every other admin call -- the body key stays ACCEPTED (optional,
#               default "") so nothing breaks mid-deploy, but no page we ship sends
#               it any more. community.html reads the key from sessionStorage
#               ("mt_admin_key", the same stash admin.html fills, so mod mode follows
#               Jim from /admin in the same tab); a legacy ?mod= link is honoured
#               ONCE, stashed, and scrubbed from the address bar. admin.html's
#               moderation quick-link is now plain /community. A wrong/rotated key
#               401s -> the page clears the stash and returns to the public view.
#               Zero prompt characters (the dn lane continues while the prompt-size
#               measurement stays postponed).
#   2026-08-11  APP_BUILD -> "2026-08-11dm-sprint-graph". THE DISPLAY HALF OF WWC g26
#               rec 6 ("track AND SHOW progress") -- the sprints table has recorded
#               every one-minute round since build dd and nothing displayed the
#               growth. NEW GET /api/sprints/{code}?course= (student-gated, whole
#               course history oldest-first, personal best; empty when the DB is off
#               -- the card is a bonus, never a 500) feeding dashboard.html's new
#               hidden-until-data "⚡ Your sprint record" card: two bars per sprint
#               (round A pale, round B solid), a green +n over every self-beat.
#               Rule 42 throughout: the only comparison is this student with this
#               student. Chosen over the prompt-budget work ON PURPOSE: Jim postponed
#               the two-size auditor measurement, so today's builds spend ZERO prompt
#               characters (this one) until that measurement runs.
#   2026-08-11  APP_BUILD -> "2026-08-11dl-wwc-rules". The two strongest remaining
#               evidence gaps close as NEW RULES 53 (number-line doctrine) and 54
#               (word-problem types; key-word shortcuts BANNED and machine-enforced).
#               Nothing in this file changed but the stamp -- the work lives in
#               tutor.py and ruletests.py; RULES.md regenerated (54 rules).
#   2026-08-11  APP_BUILD -> "2026-08-11dk-audit-polish". BATCH E -- the audit
#               re-run's six small accuracy fixes. NOTHING in this file changed but
#               the stamp: rule 48(e) say-it-back + rule 52(d) compute-is-not-this-rule
#               + the new board_notation_conflict referee live in tutor.py; the
#               point-on-a-hole guard in static/math-figures.js; the fraction-slash
#               bridge in notation.py; the fixtures in ruletests.py; RULES.md
#               regenerated (rule 27 -> ENFORCED for the percent-sum shape).
#   2026-08-11  APP_BUILD -> "2026-08-11dj-backups". Jim: "if Render falters or
#               something falters, do we have sufficient backup so that we could
#               recreate everything right away?" The honest audit: code = safe on
#               GitHub; voice cache = recreatable for ~$20 (and since 08-11 it
#               survives deploys on the persistent disk); the DATABASE = no way back
#               at all. Now it has three: (1) NIGHTLY SNAPSHOT -- _backup_pass rides
#               the existing 30-minute heartbeat, writes one gzipped JSON snapshot of
#               every table per day to DATA_DIR/backups (the persistent disk),
#               atomically (.tmp then rename), restart-safe (gates on the newest
#               file's mtime, not process memory), rotated (BACKUP_KEEP, default 14);
#               (2) RENDER'S OWN database backups (paid DB plans -- Jim confirms the
#               plan); (3) THE OFFSITE COPY -- GET /api/admin/backup streams a FRESH
#               snapshot as a download (admin key in the X-Admin-Key header, build-dg
#               discipline), wired to a button on /admin's new 🛟 Backups card, plus
#               GET /api/admin/backup/status for the card's nightly report. THERE IS
#               DELIBERATELY NO RESTORE ENDPOINT -- a remote wipe-and-replace is a
#               foot-gun; restores run offline via the new restore_backup.py with an
#               explicit --yes-i-mean-it flag, inside one transaction. The full drill
#               (bad deploy / lost database / Render gone entirely) is RECOVERY.md;
#               render.yaml was refreshed into a truthful recreation recipe (disk,
#               DATA_DIR, all env names). Export/restore themselves live in store.py.
#   2026-08-11  APP_BUILD -> "2026-08-11di-piecewise". BATCH D of the first full audit
#               (Audit_Findings_2026-08-11.md): the board tools the audit proved
#               missing. NOTHING in this file changed but the stamp -- the work lives in
#               static/math-figures.js (piecewise domains via "for", automatic
#               open/closed endpoint circles, and ⭐ a live bug the new harness caught:
#               hole= had NEVER drawn on a genuine 0/0 removable point, fixed with a
#               numeric limit that also refuses to paint a hole on an asymptote), the
#               three teaching pages ([[column align="last"]] -- the deliberately-wrong
#               last-digit lineup for contrast teaching, byte-identical on all three),
#               tutor.py (the shared tool note), and ruletests.py (PART 3r renders the
#               new figures through the real math-figures.js on every run).
#   2026-08-11  APP_BUILD -> "2026-08-11dh-audit-rules". BATCHES B + C of the first full
#               audit (Audit_Findings_2026-08-11.md). NOTHING in this file changed but
#               the stamp -- the work lives in tutor.py (nine rule additions incl. NEW
#               rule 52; two new referees: rules 17 and 44 move COVERED -> ENFORCED),
#               ruletests.py (their fixtures, quoted from the audit; the three-referee
#               foundation sweep), misconceptions.py (denominator-zero-means-hole; the
#               discriminating-counterexample warning on decimal alignment),
#               notation.py (f(a+1) read as "f of the quantity a plus one"), and
#               lessonaudit.py (the final-exam scenario seeds a real mastery picture;
#               critic discipline checks 4 and 5: the board's capital-letter convention,
#               and decided designs are not findings). RULES.md regenerated -- 52 rules,
#               16 enforced.
#   2026-08-11  APP_BUILD -> "2026-08-11dg-reliability". BATCH A: the first full audit's
#               stumbles were OUR bugs, not rate limits (Audit_Findings_2026-08-11.md,
#               PART 5). The teaching-side fixes live in tutor.py (referee false
#               positives, negotiated continuation, ceiling 1600 -> 3000, empty-reply
#               retry, stand-alone regeneration nudges). THIS file's share is SECURITY:
#               the admin key was riding in QUERY STRINGS ("GET /api/admin/stats?key=..."),
#               and query strings are written into Render's request logs in plaintext.
#               The OpenAI key was protected from exactly this in build cw (PART 3l:
#               Authorization header and nowhere else); the admin key now gets the same
#               discipline. The four admin GET endpoints (/api/beta/list,
#               /api/admin/stats, /api/admin/email-test, /api/admin/digest-test) accept
#               the key in an X-Admin-Key HEADER; admin.html sends it that way and never
#               puts the key in a URL again (unlock stores it in sessionStorage; a legacy
#               ?key= bookmark is honoured once, stashed, and scrubbed from the address
#               bar). The query parameter is still ACCEPTED server-side so nothing Jim
#               has saved breaks, but no page we ship generates it any more.
#               ⚠️ AFTER THIS DEPLOYS, JIM ROTATES FORUM_MOD_KEY IN RENDER -- the old
#               value has been logged and must be treated as burned.
#               KNOWN RESIDUAL, queued: /community?mod=<key> (forum moderation) still
#               carries the key in a URL because community.html has no other unlock;
#               admin.html's moderation quick-link keeps working that way until that
#               page's auth is reworked (its own small build). The /beta quick-link is
#               now PLAIN /beta -- the generator lives on /admin itself since 08-04.
#   2026-08-10  APP_BUILD -> "2026-08-10df-honest-copy". HONEST-COPY SWEEP. Jim: "make
#               sure we don't have anything in here that says evidence based learning as
#               a blanket statement." The sweep proved NO such claim exists anywhere on
#               the site -- the only "evidence" wording is "mastery evidence" in the
#               records/portfolio sense, which is honest and stays. But it caught three
#               stale facts, all fixed in df: (1) courses.html (the PRINTABLE scope &
#               sequence) still said the questioning-method word build cc retired, and
#               (2) still listed the pre-restructure diffeq units; (3) llms.txt (the
#               public AI-crawler summary) claimed unit mastery at "80%+" where the real
#               bar is 90%+ on a ten-question Unit Quiz, and still carried the old
#               MyTutor brand name from before the 08-03 rebrand. NO changes in this
#               file beyond the stamp -- the work lives in courses.html, llms.txt and
#               ruletests.py (PART 3o learns courses.html's ten unit lists; NEW PART 3p
#               bans the retired method word and blanket "evidence-based" from every
#               visible page, llms.txt and README, forever).
#   2026-08-10  APP_BUILD -> "2026-08-10de-diffeq-cupm". DIFFEQ RESTRUCTURED TO THE
#               CUPM MAINSTREAM SYLLABUS. Jim: "go with the one that you feel will be
#               most acceptable to most schools." The MAA/CUPM ODE course study (in
#               D:\MyTutor) describes where mainstream college ODE courses have
#               converged: qualitative analysis (equilibria, phase line, stability) and
#               numerical methods (Euler, Runge-Kutta) are core units now; series
#               solutions have largely moved out; systems get real time including the
#               phase plane and a taste of nonlinear dynamics. Our old syllabus was the
#               older formula-methods sequence. New nine: 1 intro/classification/slope
#               fields, 2 separable+linear (exact = one brief topic), 3 qualitative,
#               4 numerical, 5 homogeneous 2nd-order, 6 nonhomogeneous+vibrations+
#               resonance, 7 Laplace, 8 linear systems/phase plane, 9 nonlinear/
#               linearization. No changes in THIS file beyond the stamp -- the work
#               lives in curriculum.py, tutor.py, pedagogy.py, foundations.py (four new
#               scripts: slope field, equilibrium, Euler's method, eigenvalue),
#               session.html, topic.html. NOTE: unit numbers changed meaning. No live
#               students exist; any old diffeq mastery rows describe the OLD units and
#               would mislead -- acceptable only because we are pre-launch.
#   2026-08-11  APP_BUILD -> "2026-08-11dd-fluency-sprints". THE LARGEST EVIDENCE GAP
#               CLOSED: WWC guide 26 recommendation 6 ("regularly include timed
#               activities", STRONG -- named independently by four sources) -- we had
#               nothing. Format studied from the real Eureka G1M1 Teacher Edition and
#               rebuilt with OUR items (their curriculum is (c) Great Minds, not open):
#               two sibling 60-second rounds, pattern-family sequencing, and the only
#               celebrated number is B minus A -- the student against the student
#               (rule 42, which Eureka's design independently arrived at).
#               Jim's calls: offered at lesson start (one optional link on the welcome
#               card), TAP answers (a timed minute must not measure our transcription
#               latency), full A/B with a stretch break.
#               THIS FILE: GET/POST /api/sprint/{code}. Seeded per student-per-day (a
#               mid-sprint reload rebuilds the SAME sprint; tomorrow's is fresh), history
#               and personal best from the new store table, counts re-clamped server-side.
#               ⚠️ SPRINTS NEVER GATE ANYTHING -- ruletests PART 3n proves it at all
#               three layers, and verifies every one of the 1,620 generated answers.
#               NEW FILE sprints.py (27 units across entry/basic/prealgebra); store.py
#               gains the sprints table (JOINS _STUDENT_CODE_TABLES day one);
#               session.html gains the overlay. The teaching prompt is UNTOUCHED -- the
#               offer is deterministic UI, so the prompt budget paid nothing.
#   2026-08-10  APP_BUILD -> "2026-08-10dc-count-the-stumbles". Jim ran the FULL first
#               audit: ten lessons, nine critic findings. Adjudication is in the project
#               (Audit_Findings_2026-08-10.md): most findings were rejected on the quoted
#               evidence -- including the critic calling our removable-discontinuity
#               graph WRONG (the line y=x+2 with the point removed IS the standard graph
#               of (x^2-4)/(x-2); the transcript derived it two lines earlier) and
#               flagging a missing [[step eq="b = sqrt(64) = ?"]] that is plainly there.
#               ⭐ THE REAL FINDING WAS ONE THE CRITIC CANNOT MAKE: the tutor STUMBLED
#               four times in ten lessons -- graceful-failure turns ("Sorry, I lost my
#               train of thought") a real student would have watched. A content marker
#               reads straight past absence, so counting stumbles is now CODE's job:
#               detected, retried once (a student would repeat themselves), counted, and
#               injected into the report as a reliability finding at fixed severity.
#               "Lost my train of thought" = the model returned EMPTY after retries;
#               "having trouble thinking" = the API call itself failed. Jim: the Render
#               logs from 21:45-22:09 UTC name the underlying errors.
#               The critic's system prompt also gained the three discipline checks its
#               first marking run earned: re-read surrounding turns before flagging,
#               search the reply for your own suggested fix, and correct-under-standard-
#               conventions mathematics is never a finding.
#   2026-08-10  APP_BUILD -> "2026-08-10db-room-to-think". Jim's second key probe came
#               back: gpt-5.5 ✓ (the answer he wanted), and gpt-5.1 marked unusable with
#               "max_tokens or model output limit was reached". THAT LINE WAS MY BUG, and
#               it is a false NEGATIVE worth understanding: a reasoning-family model
#               spends tokens THINKING before it writes a word, and that spending counts
#               against max_completion_tokens -- so my 5-token probe left it no room to
#               think, and an error that PROVES access (the request was accepted, billed
#               and answered) read as no-access.
#               Fix, same philosophy as the parameter swap: the API names the limit that
#               was hit, so take it at its word -- retry once with room to think (4x or
#               +3000 tokens), never guessed from the model name. Also handles the QUIET
#               variant: a 200 with an empty message and finish_reason "length", which
#               would otherwise end a lesson looking like the student walked out.
#               This matters beyond the probe: with OPENAI_AUDIT_MODEL=gpt-5.5, the
#               student turns (120-token budget) would have died the same way.
#   2026-08-10  APP_BUILD -> "2026-08-10da-which-models". Jim, holding a new OpenAI key:
#               "how can I tell if it's for chat five point five?"
#               You cannot tell by looking. A key carries no model list; access belongs to
#               the ORGANISATION, and for a project-scoped key to that project's model
#               permissions. The only honest answer is to ASK THE KEY -- so the tool does.
#               NEW probe_models(): one tiny call per candidate model, reporting which this
#               key can actually reach. Folded into the /admin "① Check my key & price it"
#               button, so one click answers the question for a fraction of a cent without
#               teaching a lesson. A model that needs ORGANISATION VERIFICATION now says
#               so AND gives the remedy (Settings > General > Verify Organisation, photo
#               ID and a live selfie, access about 15 minutes after approval) instead of
#               handing back a 403 for somebody to paste into a search engine.
#               The button no longer claims to be "free": it costs a fraction of a cent
#               and says so. A price for a job that cannot run is worse than no price.
#   2026-08-10  APP_BUILD -> "2026-08-10cz-audit-preflight". Jim ran the lesson auditor
#               for the first time and it failed. Four fixes, three of them mine:
#               (1) OpenAI's newer models reject "max_tokens" and want
#               "max_completion_tokens". The parameter is now NEGOTIATED -- try one, and
#               if the API names the other, switch and remember. Not guessed from the
#               model name: names change, and guessing is how you ship a break.
#               (2) ⭐ A PREFLIGHT. His run spent 89.9 SECONDS AND TWO LIVE TUTOR CALLS
#               before discovering a parameter name. One tiny call now proves the key,
#               the model and the parameter first, for a fraction of a cent.
#               (3) The default model was "gpt-5.5", chosen from a press release rather
#               than from his account. His key reaches gpt-4.1 and gpt-4o; the default is
#               now gpt-4.1, still overridden by OPENAI_AUDIT_MODEL.
#               (4) ⚠️ AN HONESTY BUG IN MY OWN REPORT. It headlined "2 scenarios · 0
#               findings" for a run in which BOTH lessons died before a word was marked.
#               Zero findings and zero lessons marked are OPPOSITE RESULTS and must never
#               read the same. The report and the /admin panel now say "NOTHING WAS
#               MARKED", and the panel repeats the server's summary instead of composing
#               its own.
#               One thing that worked exactly as designed: the error named every model his
#               account can reach, so the diagnosis took seconds. It named them for the
#               wrong reason though -- the check fired on any error containing the word
#               "model" -- so that now fires only on a genuine model error.
#   2026-08-10  APP_BUILD -> "2026-08-10cy-wait-time". No code change in this file -- the
#               stamp moves for the FIFTH REFEREE in tutor.py.
#               From the MAA Instructional Practices Guide Jim added to the tutor folder:
#               teachers wait LESS THAN 1.5 SECONDS before answering their own question;
#               the research says wait SEVEN; and the first thing that improves when you
#               wait is HOW OFTEN A STUDENT SAYS "I DON'T KNOW" (Fuller 1985, Tobin 1987).
#               The guide's vignette is an instructor asking eight questions and answering
#               every one himself a second later. We cannot rush our students -- they
#               answer whenever they like -- but we can rush OURSELVES exactly that way.
#               ⭐ NOT A NEW RULE. Rule 39(b) already says one question per turn and it
#               comes LAST; it has been COVERED since build ce -- written into all ten
#               prompts and never checked. Moving a rule UP A TIER is worth more than
#               writing a new one, and it costs no prompt budget. 39 is now ENFORCED.
#               Also: .gitignore now excludes *.pdf. The evidence base in D:\MyTutor is
#               ~104 MB and growing; it belongs beside the code on Jim's machine, not in
#               the GitHub repo or the image Render builds on every deploy.
#   2026-08-10  APP_BUILD -> "2026-08-10cx-buttons-not-instructions". Jim asked "tell me
#               exactly how to run it", and the honest answer was that he could not.
#               BOTH admin jobs -- the new lesson auditor and the foundation pre-render --
#               were documented as "POST /api/admin/... with {key, dry_run:true}", and
#               nothing in the product can POST JSON. That is why the pre-render had sat
#               UN-RUN FOR DAYS while three handoff documents kept telling him to run it.
#               A control panel whose controls are instructions to use a tool the owner
#               does not have is not a control panel.
#               /admin now has both as buttons: price it (free), then run it. The audit
#               walks its cast two lessons at a time and remembers where it got to, so a
#               long job never becomes one long request, and it has a Copy-the-report
#               button because the report's whole purpose is to be handed to someone.
#               THE GENERAL LESSON, worth more than the buttons: a feature is not shipped
#               when the endpoint answers. It is shipped when the person it was built for
#               can reach it. This file's own change notes have been quietly failing that
#               test since build cf.
#   2026-08-10  APP_BUILD -> "2026-08-10cw-lesson-auditor". Jim: "I need to build some
#               sort of effectiveness/reality check so we don't keep having these
#               problems." NEW FILE lessonaudit.py + POST /api/admin/lesson-audit.
#               Two things check quality today and there is a gap between them:
#               ruletests.py checks the CODE and the WORDS OF THE PROMPT and cannot judge
#               teaching, and Jim reads lessons one at a time, which does not scale past
#               Jim. The auditor closes it: student PERSONAS played by OpenAI take real
#               lessons from the real prompt, then OpenAI marks each transcript against
#               the generated rule index as a picky maths teacher. Ten scenarios, each
#               built around a failure class we have actually been bitten by.
#               ⭐ WE CHOSE THIS OVER LIVE PER-TURN REVIEW, and the reason is the point:
#               every defect found this week was a MISSING SPECIFICATION, not a bad day.
#               A live reviewer catches those sometimes and lets them through next
#               Tuesday; a rule plus a test closes them forever, for free -- and live
#               review would roughly double per-turn cost and put a pause in front of a
#               voice tutor, which is the product.
#               NOTHING IN IT CHANGES THE TEACHING. It returns a report a human reads; a
#               wrong critic quietly sanding down good teaching is the exact failure this
#               is meant to prevent. Admin-key gated because it spends on two APIs, runs
#               on Render because that is where the keys are, dry_run prices it for free,
#               limit/offset walk the cast in batches so no request runs long.
#               NEW ENV VARS: OPENAI_API_KEY (required for a real run) and optional
#               OPENAI_AUDIT_MODEL / AUDIT_TURNS. The key is read, never printed, never
#               returned, never logged -- ruletests PART 3l holds that line.
#   2026-08-10  APP_BUILD -> "2026-08-10cv-holes-windows-and-the-fold". No logic change in
#               this file -- the stamp moves for the four fixes below (tutor.py,
#               foundations.py, math-figures.js, session.html, ruletests.py).
#               (1) Jim, reading a live limits lesson: "it doesn't say WHY there is no
#               value at x = 2, and it completely ignores the graph that continues to the
#               right after x = 2." He is right: y = x^2 has no hole at 2, and the lesson
#               painted one on and asserted it. NEW RULE 51 -- a feature on the board must
#               BELONG to the function, and the student must see where it came from -- plus
#               a canonical calculus script for the removable discontinuity built on
#               f(x) = (x^2-4)/(x-2), where the hole is something they watch appear.
#               (2) ⭐ RENDERING THAT SCRIPT FOUND A SILENT ONE: the [[graph]] docs told
#               the tutor to write range="-1,5" while the renderer's parseRange accepted
#               ONLY "a..b" -- so every comma-framed window was discarded and the graph
#               fell back to -10..10. That instruction exists BECAUSE of Jim's earlier
#               catch that a window "barely showed the parabola", so the fix for that bug
#               had never once worked. parseRange now takes "a..b", "a,b" and "a to b",
#               and ruletests reads its regex out of the renderer and checks every range=
#               we write against it.
#               (3) Jim: "the Welcome back page should never require scrolling. I had to
#               scroll down to see what was my option." The returning card was still
#               carrying the first-timer's three how-it-works bullets; the new-student
#               card overflowed too, at every common laptop size.
#   2026-08-10  APP_BUILD -> "2026-08-10cu-mastery-is-reachable". Jim: "if I pass an exam
#               with an eighty-five, I can go onto the next unit. I can do all the units
#               and still be carrying an eighty-five with me, which is gonna keep me from
#               mastering the final exam... there should be the ability to review and
#               retake that quiz so we can get it up to the mastery level."
#               ⭐ WHAT WE FOUND WAS WORSE THAN THE THING HE DESCRIBED. Mastery is 90% and
#               the Unit Quiz was FOUR OR FIVE questions -- so the only scores it could
#               produce were 80% and 100%. There was no 85, and "mastery = 90%" silently
#               meant a PERFECT PAPER. The topic quizzes had the same defect one floor
#               down: three or four questions against an 80% bar, i.e. four out of four.
#               The bar and the question count lived in different files and moved on
#               different days (the bar went 80 -> 90 on 2026-08-04); no test ever
#               multiplied them together. ruletests PART 3k does that now.
#               HIS DECISIONS: Unit Quiz -> TEN questions (90% = miss one and still
#               master), topic quiz -> FIVE (80% = miss one and still pass); a student may
#               still move on with a unit unmastered, but the tutor now CHASES it (new
#               rule 50); and the locked Final Exam names the units holding it shut.
#               THIS FILE: _final_gate_message() replaces the flat "you've mastered 3 of
#               9" -- it names each unit still open, its best Unit Quiz score, offers the
#               review-and-retake, and says plainly that the record keeps their BEST score
#               so a retake can only ever help. Falls back to the old wording if the
#               record cannot be read: a locked door must never also be a silent one.
#               No stored data changes. store.record_check has always kept the best score,
#               so every retake was already safe -- nobody had been told.
#   2026-08-10  APP_BUILD -> "2026-08-10ct-board-and-all-four-views". Two things from Jim,
#               one of them a live defect he hit in a Basic Math demo lesson:
#               (1) "when the answers popped up, they shortened the whiteboard to the
#               point where I could only see a fraction of what was actually being
#               displayed... maybe instead of four answers stacked on top of each other,
#               one row of four, or two rows of two." The answer buttons were a
#               one-per-line grid and the answer zone could take 47vh; the board is flex,
#               so whatever the answers took, the whiteboard lost. THE REAL CLASSROOM
#               ALREADY SOLVED THIS -- session.html lays its tap-to-answer buttons out as
#               a centred wrapping ROW. The demo now matches it. Measured at 1280x800:
#               board 351px -> 435px, answers 193px -> 109px, four buttons on one row.
#               (2) "I'd like to do that same idea for the homeschool, the teacher, and
#               the student." The teacher and student dashboards got the cs treatment.
#               Homeschool needed nothing: it rides the parent dashboard, so it was
#               finished in cs.
#               THIS FILE: sixteen lines APPENDED to DEMO_VOICE_LINES (211 -> 227) --
#               five teacher stops, four student stops, five for the student DOOR (which
#               was describing the visitor in the third person right after greeting them
#               with "this is your dashboard"), and two for the habit charts. Appended,
#               never inserted: clips are served BY INDEX. About 4,000 characters of new
#               audio, roughly a dollar, once.
#   2026-08-10  APP_BUILD -> "2026-08-10cs-full-parent-dashboard". Jim: "the demo is what
#               is selling this product, and the parent is our number one customer... we
#               have this great dashboard for parents. What we've done with this demo is
#               we created a shortened dashboard that doesn't show much at all with a
#               whole lot of words. I want a fully fleshed out parent dashboard, and I
#               want you to give me a tour of that dashboard."
#               He is right, and the demo's OWN design notes already said so: they
#               specify seven sections for the parent view and it shipped with four.
#               /demo's parent dashboard is now a section-for-section mirror of the real
#               /dashboard?view=parent -- honest read, the read-only parent box with the
#               records link, five tiles with the mastery ring, focus areas, nine units
#               with dates AND scores, the learning journey, the status meter, the trophy
#               case, the courses strip, the placement strengths, the honesty footer.
#               The tour went from 5 stops to 10, and homeschool overrides all 10.
#               THIS FILE: ten lines APPENDED to DEMO_VOICE_LINES (201 -> 211), five
#               parent and five homeschool, byte-identical to demo.html's VOICE_LINES.
#               Appended, never inserted -- clips are served BY INDEX. New audio is about
#               2,500 characters, roughly sixty cents, once.
#   2026-08-10  APP_BUILD -> "2026-08-10cr-one-door-one-dashboard". Jim: "when we go to
#               the homeschool page, the teacher page, the student page, I want that demo
#               to only show the dashboard that's interesting to that particular person.
#               I don't want any links to any other dashboards from there."
#               The three-view chooser belongs to the OPEN demo at /demo, where the
#               visitor asked to see all three. A visitor who came through one door is now
#               locked to it: the ending panel, the "Done" button and the dashboard's own
#               back button all lead to that door's own ending, never to another
#               audience's screen. Not a dead end -- the ending offers the walkthrough
#               again, a real lesson, and the pricing page.
#               THIS FILE: four closing lines APPENDED to DEMO_VOICE_LINES (197 -> 201),
#               one per door, byte-identical to demo.html's VOICE_LINES. Appended, never
#               inserted: clips are served BY INDEX. New audio is about 1,300 characters,
#               roughly thirty cents, once.
#   2026-08-10  APP_BUILD -> "2026-08-10cq-homeschool-walkthrough". Jim walked the
#               homeschool door and hit a bug I put there in cp: "it talks for a long
#               time and says this is the page that your child works from. It's just a
#               blank screen. It stays blank, blank, blank, blank until it gets to the
#               parents' view." Two faults, both mine.
#               (1) ORDER. startAudienceWalkthrough blanked the page and THEN spoke a
#               thirty-second intro before opening the dashboard. Nobody should ever be
#               talked at by an empty screen. The screen goes up FIRST now, the first
#               stop glows, and the words come over the top of something to look at.
#               (2) TAILORING. Homeschool borrowed the parent tour verbatim, so a
#               homeschool visitor heard a parent's script. It now has five stop lines of
#               its own -- Monday morning, one adult teaching several grades, no
#               teacher's aide behind you.
#               THIS FILE: five lines APPENDED to DEMO_VOICE_LINES (192 -> 197). Appended,
#               never inserted: clips are addressed BY INDEX, so anything inserted above
#               them would play the wrong audio under the right words, silently. They are
#               byte-identical to demo.html's VOICE_LINES and PART 3j proves it every run.
#   2026-08-10  APP_BUILD -> "2026-08-10cp-audience-walkthroughs". Jim: the demo "is
#               almost like a video... I would like one of those available, a very
#               obvious button that says view the demo on the parent page, the teacher
#               page, the homeschooling page, and the student page."
#               Four doors into ONE demo: /demo?view=parents|teachers|homeschool|students
#               speaks an intro written for that visitor -- naming the features they came
#               for -- and then runs the matching dashboard's existing narrated tour.
#               Deep-linked rather than rebuilt four times, because copying a tour into
#               four marketing pages is the copy-paste-drift that gave us the build-bk
#               rule bug and the board-wrap bug.
#               THIS FILE: four lines APPENDED to DEMO_VOICE_LINES (188 -> 192). They are
#               addressed BY INDEX, so they go on the END and nothing above them moves;
#               they must stay byte-identical to demo.html's VOICE_LINES, and PART 3j now
#               proves it on every run.
#   2026-08-10  APP_BUILD -> "2026-08-10co-rule-index". No code change in this file.
#               Audit #2 items 23 and 24 shipped: every rule now DECLARES how it is
#               verified (ruletests.py PART 3i, a ratchet -- new drift fails, old debt
#               prints), and `python ruletests.py --rules` generates RULES.md from the
#               prompt itself. Generating it exposed that rules 2, 5 and 8 were checked
#               by nothing at all; 2 and 8 are now enforced by the visual referee.
#               ⚠️ RULES.md is a NEW FILE in the repo (generated, but committed so it can
#               be read on GitHub without running anything).
#   2026-08-10  APP_BUILD -> "2026-08-10cn-scale-and-stability". Jim's brief: quality,
#               low latency, no degradation over time, headroom to keep adding teaching
#               code, ten thousand simultaneous students, build under $1,000.
#               ★ THE DEGRADATION HE DESCRIBED WAS REAL AND IT WAS HERE. Every chat turn
#               loaded the student's ENTIRE conversation, parsed it, appended two
#               messages, re-serialised it and wrote it all back -- to use the last 30.
#               A student a year in was moving several megabytes of JSON per turn, and it
#               got worse every week they came back. MAX_STORED_MESSAGES caps it at 60
#               (double what the tutor reads) via _bounded_history on the one path every
#               save goes through. Nothing the tutor uses is lost; progress, mastery,
#               quizzes, hours and awards live in their own tables. It is also the right
#               privacy posture for a child's conversation.
#               ★ USAGE LOG now purged daily off the existing heartbeat (USAGE_LOG_DAYS,
#                 default 180). ★ RATE BUCKETS now expire by AGE -- the old sweep only
#                 dropped already-empty buckets, so with every bucket busy the table grew
#                 past its cap and never came down. ★ DB POOL sized in store.py.
#               ★ REVERSED BUILD cl. Deferring the wording of heard scripts saved ~6,500
#                 characters a turn and cost a cache rebuild on every flip: about $0.24
#                 an episode to save $0.0005 a turn, plus a slower turn each time. The
#                 prompt is now byte-identical for a whole session. A STABLE prompt beats
#                 a smaller one, and at ~34k tokens we are using 17% of the window.
#   2026-08-10  APP_BUILD -> "2026-08-10cm-cache-discipline". Jim asked whether "cost"
#               meant money or performance. Checking the money side found a real defect
#               I had shipped the build before: the misconception hint was appended into
#               the SYSTEM PROMPT, which is one cached block -- so every turn it fired
#               moved the cache prefix and re-billed ~15,000 tokens (plus a cache write)
#               to deliver a ~195-token note. It now travels as turn_note= on the
#               student's own message, where nothing is cached. Same information to the
#               model, better placed, and the system prompt is byte-identical turn to
#               turn again.
#   2026-08-10  APP_BUILD -> "2026-08-10cl-prompt-budget". Jim on the character ceiling:
#               "we broke the files into sub-files... I don't know if that creates
#               problems or an increased chance of errors. I don't want to have that."
#               MEASURED FIRST. Splitting files does not reduce the prompt at all -- a
#               prompt carries ONE course template, so cross-template duplication costs
#               disk (471 KB) and not prompt (130 KB). And the templates overlap the
#               shared rules by 0%, so there is no duplication left to reclaim anywhere.
#               Every reduction from here removes or defers real teaching content, so
#               exactly one was taken, the one rule 40 already made safe: a script the
#               student has HEARD is offered, not replayed, so its wording only belongs
#               in the prompt on the turn they accept the offer. THIS FILE decides that,
#               reading the student's words and -- because the offer is usually answered
#               with a bare "yes" -- the tutor's previous turn as well. Fails OPEN.
#               6,000-8,000 chars off an ordinary returning-student turn, growing as the
#               student learns more. ruletests now prints a per-block PROMPT BUDGET so
#               the next block's cost is visible before it is paid.
#   2026-08-10  APP_BUILD -> "2026-08-10ck-misconceptions". NEW FILE misconceptions.py
#               (148 catalogued wrong RULES; audit #2 item 2 -- the highest-leverage
#               teaching item left). THIS FILE adds the just-in-time half: before the
#               turn, match what the student JUST said against this course's catalogue
#               and, on a hit, hand the tutor the diagnosis AND the remedy in the same
#               note. Always framed as a possibility he may discard -- a matcher that
#               overrode his own reading of a child would be worse than no matcher
#               (rule 49d/e). Conservative by construction: numbers are never evidence
#               in any spelling, matches are on word boundaries, at most two theories.
#               ⚠️ misconceptions.py MUST be committed with this batch.
#   2026-08-09  APP_BUILD -> "2026-08-09cj-notation-registry". No code change in this
#               file. NEW FILE notation.py -- the single source of truth for every
#               symbol the courses use: how it is written, how it is SAID, and the wrong
#               reading to deny. tutor.py feeds it into every prompt; ruletests.py PART
#               3f fails the build if any board line writes a symbol the registry does
#               not know. ⚠️ notation.py MUST be committed with this batch.
#               ⚠️ Re-run POST /api/admin/prewarm-foundations: three new scripts.
#   2026-08-09  APP_BUILD -> "2026-08-09ci-function-notation". No code change in this
#               file. Jim, live in Algebra I: "it's never been clearly stated to me what
#               f of x is, how to say f of x... and then it flipped over to g of x."
#               It was not the student and not a stale deploy -- the teaching was never
#               written. See foundations.py (five new scripts), tutor.py (rule 48) and
#               ruletests.py (the check that would have caught it).
#               ⚠️ AFTER DEPLOYING, RE-RUN POST /api/admin/prewarm-foundations so the five
#               new scripts are rendered before a student meets them (about 63 cents).
#   2026-08-09  APP_BUILD -> "2026-08-09ch-assessment-honesty" (proactive audit #2, the
#               assessment group: items 9, 10 and 11). No endpoint changed shape; the
#               work is in store.py (the arithmetic), tutor.py (rules 45-47 and a fourth
#               referee) and ruletests.py. These three protect the progress bars, which
#               are the product's central promise: every count here becomes a green bar,
#               a parent dashboard line, and a row in a printable homeschool record.
#   2026-08-09  APP_BUILD -> "2026-08-09cg-todaybar-pendingcheck". Jim's live Pre-Algebra
#               resume, two problems, both of which we had "fixed" before.
#               (1) "There's only two of the three tracking bars across the top. I don't
#               know where the third one is, and I don't know why it keeps disappearing."
#               ROOT CAUSE: the UNIT and COURSE bars survive a page load because the
#               SERVER can rebuild them from mastery data (build br did that for UNIT).
#               The TODAY bar never had a server side at all -- it lived only as a
#               [[today items]] tag the model emitted once, held in browser memory. Any
#               reload or resume wiped it, and it could only return if the model happened
#               to emit the tag again, which on a resumed opener it did not. Worse, the
#               ensure_today_tag() net stood DOWN in exactly that case, because it read
#               "a [[today]] exists earlier in history, so a bar is already up" -- true
#               within one sitting, false the moment the page reloads.
#               FIX, same shape as the other two bars: NEW store table `today_goals`
#               (code, course, day) written by _record_today_bar() from the tutor's own
#               [[today items]] / [[todaydone n]] tags, returned by /api/session as
#               progress.today, and rendered by session.html at load. Ticks MERGE, so a
#               later turn can never un-tick an earned win; a new plan resets them; it is
#               scoped per day so yesterday's goals never show as today's. main.py also
#               now tells tutor.py whether a bar genuinely exists (student["today_live"])
#               instead of letting it guess from history.
#               (2) "It gave me a problem without putting it on the board, and this is the
#               exact example that we've already used once before that was supposedly
#               fixed. And I don't understand why it's not fixed." He is right, and the
#               reason matters: rule 15 does not merely forbid this, it names this exact
#               column-addition scenario and prints the exact fix
#               ([[step eq="dollars: 2 + 1 + 1 = ?"]]), and has since build bm. A rule in
#               a prompt is guidance, not a guarantee. So it became a referee --
#               tutor.prose_pending_question_conflict(), the third check in
#               prose_board_conflict(): ask the student to COMPUTE something and emit no
#               pending "?" line, and the draft is thrown away and rewritten. See tutor.py.
#   2026-08-09  APP_BUILD -> "2026-08-09cf-audit1-closure-audit2-start". TWO JOBS.
#               JOB 1 -- Jim: "take a look at Audit One and make sure we've accomplished
#               all of those." Checked all 25 items of the 2026-08-08 audit against the
#               REAL built prompt for all ten courses and the real source, not memory.
#               24 had shipped. ONE HAD NOT, and it was a live bug: item 11, the fix that
#               stops a long board line WRAPPING mid-equation, went into session.html in
#               build bu and NEVER reached practice.html or topic.html. Jim's original
#               screenshot ("dimes: 7 + 8 + = 16" with "1(carried)" on the next line -- a
#               literally different equation on screen) was still reproducible on two of
#               the three teaching pages. Both pages now have the nowrap CSS and fitRow(),
#               and on ALL THREE pages [[write]] lines are fitted too (they never were).
#               A second gap found the same way: practice and topic were built from
#               GROUND_RULES + GRAPH_TOOL_NOTE only, so rules 36-40 reached them while the
#               canonical scripts those rules refer to did not -- a student could hear one
#               definition of "denominator" in the lesson and a different one on the topic
#               page, which is rule 28 broken at platform scale. Both modes now get the
#               foundation block AND the heard-list (this file wires it at both endpoints
#               and records [[learned]] there too).
#               ruletests.py PART 3e now makes the whole class of bug impossible: the
#               three teaching pages are three copies of one classroom and must match.
#               JOB 2 -- audit #2 "do first". NEW: POST /api/admin/prewarm-foundations
#               (item 21). The TTS cache is keyed by TEXT and starts empty, so the FIRST
#               student to reach each of the 173 scripts pays a live render -- seconds of
#               silence on the exact turn that introduces a new idea. We know all 173
#               strings in advance, so that first student should not be a real child.
#               Admin-key gated, idempotent (an already-cached script is skipped free),
#               dry_run prices it without spending, limit renders in batches, atomic
#               writes so a partial clip is never left behind, and one failure never
#               stops the batch. Dry run today: 173 scripts, 82,856 characters.
#               Rules 41-44 are in tutor.py.
#   2026-08-09  APP_BUILD -> "2026-08-09ce-checkin-memory-visualref". Jim, on the three
#               items from proactive audit #2: "we need to have a cap on how long we talk
#               to an eight year old… I think you need to check in with them every now and
#               then" · "nothing tells him which scripts that student has heard, so a loyal
#               student can re-hear it… we should just query him and say, do you think you
#               got it, or do you want me to refresh your memory?" · "you can't say one
#               thing and then have the numbers say something different."
#               THIS FILE carries half of the second item -- FOUNDATION MEMORY:
#                 _foundations_heard(code, course) reads the student's already-heard
#                   canonical terms out of store and puts them on student_context BEFORE
#                   the turn, which is the only way the tutor can ever know: a new
#                   session's history is empty, so the prompt was previously telling him
#                   to skip an introduction he had no way to identify.
#                 _record_learned(code, course, reply) reads the [[learned term="..."]]
#                   tags rule 40(f) asks him to emit and writes them down AFTER the turn.
#                   Parsing and validation live in foundations.learned_terms_in(), so a
#                   tag naming a script we do not have is DROPPED -- a typo must never
#                   retire an introduction a student still needs -- and ruletests.py can
#                   test that filter without booting the app.
#                 The tag is invisible: every page's stripTags() already removes any
#                   [[...]], so no client change was needed and none was made.
#                 foundations is imported DEFENSIVELY here, exactly as in tutor.py.
#               Both chat call sites (the __open__ opener and the normal turn) record.
#               Rules 39 and 40 and the visual referee are in tutor.py; the table and its
#               reset-cascade entry are in store.py.
#   2026-08-09  APP_BUILD -> "2026-08-09cd-foundation-library". No code change in this
#               file -- the build string moves so /health proves the deploy landed.
#               TWO THINGS SHIPPED, both in files main.py only reads through tutor.py:
#               (1) foundations.py grew from 24 canonical foundation scripts to 173 --
#                   every course now has 17 or 18 verbatim introductions instead of 2.
#                   Jim: "I want you to expand that library of saved script... I'd spend
#                   a hundred dollars on it to make it complete." One-time ElevenLabs
#                   render of all 173 is 82,856 characters -- roughly $12 to $25 at
#                   current per-character rates, then free forever, because _tts_cache_path()
#                   in this file keys the audio cache by the TEXT of the line. Verbatim
#                   scripts are the whole reason that cache can ever hit.
#               (2) ruletests.py PART 3c -- "board tags actually draw". Jim's demo
#                   failure ("the lesson referred to a diagram that didn't show up on
#                   the board... we got one shot to do it right, and it failed") has a
#                   root cause that no exception ever reports: a board tag whose NAME or
#                   ATTRIBUTE the renderer does not read draws nothing (or draws the
#                   wrong picture) in total silence. PART 3c parses math-figures.js,
#                   geo-figures.js and session.html's handleTags() and holds every board
#                   line to what those renderers actually read. On its first run it
#                   caught 11 already-shipped scripts: [[graph expr=...]] (the grapher
#                   reads func=, never expr= -- empty axes), [[numberline from/to/mark]]
#                   (it reads min/max/points), [[triangle a/b/c]] and [[righttriangle
#                   a/b/c]] (they read sides/v and adj/opp/hyp), [[vector x/y]] (reads
#                   v="4,3"), lines="y=x^2" (lines= flattens a parabola to a straight
#                   line), a comma used where the grapher needs a semicolon, and two
#                   [[write]] tags whose square brackets ended the tag early in
#                   handleTags' own regex. All fixed; all 57 figures now re-rendered
#                   through the real renderers and confirmed non-empty.
#   2026-08-09  APP_BUILD -> "2026-08-09cc-foundation-first". ★ PEDAGOGY CHANGE (Jim).
#               We described this classroom as SOCRATIC. That was wrong, and Jim caught
#               it from the inside: "there's no foundation built -- when I'm looking at
#               fractions, I'm not getting what is a fraction, what's a denominator,
#               what's a numerator." The evidence agrees: for NOVICES -- nearly every
#               student on a new topic -- fully guided explicit instruction beats
#               discovery, and a student who "discovers" something wrong remembers the
#               wrong version over the correction (Clark/Kirschner/Sweller); a 2026
#               systematic review of Socratic method in mathematics finds it demands
#               heavy teacher expertise, more time, and depends on prior knowledge the
#               student may not have. So:
#               (1) NEW SHARED RULES 36-38 (all ten courses, verified): 36 teach the
#                   thing before you ask about the thing -- name it, name every part,
#                   define it, worked example, check understanding, THEN questions;
#                   37 vocabulary is taught, never assumed; 38 concrete -> picture ->
#                   symbols, with I-do/we-do/you-do and guidance that FADES as the
#                   student gains competence (never before).
#               (2) The per-course templates no longer say "Socratic" -- they say
#                   foundation-first, and rules 36-38 override any older wording.
#               (3) NEW foundations.py -- CANONICAL FOUNDATION SCRIPTS, 24 of them, the
#                   exact words for each course's foundational terms (what a fraction
#                   IS, what a denominator IS, what a variable IS...). Spoken VERBATIM.
#                   This also answers Jim's cost point directly: the TTS cache is keyed
#                   by the TEXT, so a verbatim script is rendered ONCE for the whole
#                   platform and is free for every student after -- teaching MORE now
#                   costs less, not more. Re-wording it is what costs money.
#               (4) EVERY public page swept: no page claims the Socratic method any
#                   more (landing incl. its JSON-LD twin, mission, homeschool, features,
#                   parents, practice, llms.txt, README).
#               ruletests.py grows to 140 checks incl. a new PART 3b that proves each
#               script reaches its course prompt, is speakable, marks its key term, and
#               that no page has crept back to the old claim.
#   2026-08-09  APP_BUILD -> "2026-08-09cb-firstword-quizretry" (Jim's three questions).
#               (1) THE CLIPPED FIRST WORD, PROPERLY. Leading silence only helps if the
#               OUTPUT DEVICE is awake -- Bluetooth speakers, headphones and many laptop
#               codecs power down after a few seconds of quiet and swallow the first
#               200-400ms while they wake, which is exactly "a word or two", and worst
#               "when he comes back from doing something". Two fixes on all three
#               teaching pages: a truly silent WAV now LOOPS in its own element for as
#               long as the lesson is open (paused when the tab is hidden), so the audio
#               route never sleeps; and the lead is now DYNAMIC -- a clip after >2.5s of
#               silence (or the session's first) gets the full ~840ms pad, >0.9s gets
#               ~560ms, back-to-back clips get ~280ms.
#               (2) FAILED QUIZZES: NEW SHARED RULE 35 (all ten courses). A failed quiz
#               is never re-given on the spot. Name the win, diagnose the ONE or TWO
#               skills underneath the misses, re-teach each with a worked example, and
#               require TWO unaided correct problems on that skill BEFORE offering a
#               retake -- with fresh questions, never the same items. A second failure
#               steps BACK to the prerequisite instead of looping. The word "failed" is
#               never used about the student. ruletests.py gains the coverage check and
#               a live scenario.
#               (3) The parent records report was verified working end to end: /records
#               serves the printable page and /api/records/{code} returns the real hours
#               log, per-course unit progress and awards. No change needed.
#   2026-08-09  APP_BUILD -> "2026-08-09ca-demo-voice-recovery" (Jim's live walk-through,
#               two real bugs -- demo.html only; no server logic changed).
#               (1) ⭐ HIS VOICE WAS LOST MID-DEMO. "I got the mechanical voice from the
#               browser rather than our guy's voice." Cause: `serverVoiceOK` was a
#               ONE-WAY LATCH -- the first clip that failed to load switched the ENTIRE
#               rest of the session to the flat browser voice. That is precisely what
#               the first visitor hits after we append lines: a brand-new clip isn't
#               cached, the server has to generate it, and one slow fetch poisoned
#               everything after it. Now every line tries his real voice, a failure is
#               retried once, only THAT line falls back, a stalled clip gives up after
#               6s, and the server voice is re-tried every fifth line even after
#               repeated failures. Verified: one bad clip, then the next lines are back
#               in his voice.
#               (2) ⭐ STRANDED ON THE TEACHER DASHBOARD. "When I finished the teacher's
#               dashboard, it stopped -- it didn't put the three bubbles up again."
#               The bubbles depended on the audio chain completing, so a stalled clip
#               (bug 1) left the visitor with no way forward but the browser's back
#               button. Now THREE independent things bring the bubbles back and any one
#               is enough: the tour finishing, a hard watchdog armed when the dashboard
#               opens (every stop's estimate + 30s), and a "✓ Done — show the three
#               views" button that is visible the whole time a dashboard is open.
#   2026-08-09  APP_BUILD -> "2026-08-09bz-demo-figures-typed-realdash" (Jim, three things
#               from a live walk-through).
#               (1) THE NUMBER LINE WAS INVISIBLE. The figure SVGs carried a viewBox but
#               no WIDTH, and inside the whiteboard's centred flex column an auto-width
#               SVG collapses to a smudge. Figures now take a real width (max 660px) and
#               a 150px minimum height, with a larger caption.
#               (2) THE DEMO NO LONGER SPEAKS. Jim: "let's just drop the speaking part
#               for the demo." A one-shot sales page should not hang on a microphone
#               permission prompt. All 20 lesson lines re-worded for typing (appended
#               154-173; the mic wording at 115-134 is now unused), the mic UI is gone,
#               and POST /api/demo-transcribe is REMOVED (nothing called it, and an
#               unused endpoint that spends ElevenLabs money is a surface we don't need).
#               Typed answers still accept spoken forms ("two", "negative two").
#               (3) THE DASHBOARDS NOW MATCH THE REAL PRODUCT. Asked directly whether
#               they did, the honest answer was no: the teacher view invented a 9x6
#               mastery grid, per-student coaching reasons, a class-level honest read and
#               time charts, and the parent view invented week/September trend sections.
#               None of that exists. Rebuilt from the real screens: the student view is
#               dashboard.html's real tiles (units mastered · accuracy · problems
#               practiced · time this week · day streak) + where-you-are + quiz results +
#               strengthen next + trophy case + my courses; the teacher view is
#               teacher.html's real class manager (open by class code, per-student units
#               mastered/started with a star, needs-attention flags, open a student
#               read-only, add by student code); the parent view is the same dashboard in
#               parent view (How X is doing + the honest read + the same five numbers +
#               strengthen next + the printable record). Tours rewritten to match
#               (appended 174-187; 135-152 now unused).
#   2026-08-09  APP_BUILD -> "2026-08-09by-demo-button-center-bubbles" (Jim, three small
#               things). (1) A highlighted ORANGE "🎬 Try the demo" pill is now the last
#               item in the marketing nav on every page with a .nav-links row, injected
#               by the shared static/site-nav.js (styled in place if a page already had
#               its own /demo link, and suppressed on /demo itself). features.html had a
#               nav row but never loaded the shared script -- fixed. (2) The three
#               dashboard bubbles now appear CENTERED on the screen in an overlay
#               instead of at the bottom of the page. (3) They are offered again at the
#               END OF EVERY DASHBOARD TOUR, not just after the lesson -- with "let me
#               look around on my own" to dismiss them (the dashboard stays open behind)
#               and a floating "👀 Show the three views" button to bring them back.
#               No voice lines added; no server logic changed (stamp bump only).
#   2026-08-09  APP_BUILD -> "2026-08-09bx-demo-nofailure-dashboards". Jim, on the demo:
#               "we got one shot to do it right, and it failed" -- a lesson referred to a
#               diagram that never appeared (precalc said "welcome to the unit circle"
#               with no circle drawn), and most lessons still told the visitor to TYPE
#               after we moved to voice. ALL TEN LESSONS REBUILT deliberately:
#               every visual a line mentions is DRAWN in that same step (new unit-circle
#               and bar-chart figures; the geometry triangle now carries the ASKED
#               angles, 90/35/?, not the taught ones), every ask is voice-worded, and
#               each course teaches a worked example before asking. A new audit
#               (/tmp-style checks, mirrored in the build) walks all 22 steps and fails
#               the build on any unmatched visual reference or any "type it" language;
#               a second walk plays a plausible SPOKEN answer through every course.
#               THE THREE DASHBOARDS ARE NOW FULL (Jim: "extravagant and very, very
#               thorough"): one invented student, Maya Rivera, 7th grade, with a real
#               record -- 4 units mastered with dates and quiz scores, 312 problems,
#               an 11-day streak, 12 awards, the unit-5 topic ladder, an accuracy trend
#               and a minutes-per-day chart, and her next three sessions. The teacher
#               view gains a 6-student roster, a 9x6 mastery grid, per-student
#               "strengthen next" with reasons, a long honest read, and a time-on-task
#               chart. The parent view gains a plain-English read, the week, the arc
#               since September, everything mastered with dates and scores, what's hard
#               right now WITH the plan, awards, and the printable record. Each is
#               toured in SIX spoken stops (was three).
#               DEMO_VOICE_LINES: 39 APPENDED (115-153); 0-114 untouched.
#   2026-08-09  APP_BUILD -> "2026-08-09bw-demo-voice-dashboards" (Jim's three asks).
#               (1) THE DEMO IS ANSWERED BY TALKING. New POST /api/demo-transcribe --
#               same ElevenLabs engine and the same TRANSCRIBE-AND-DELETE guarantee as
#               /api/transcribe (audio lives only in the request, never disk, never
#               stored), but rate limited BY IP (12 per 5 min) because a demo has no
#               student code. demo.html now shows a real microphone button; spoken
#               answers are normalised client-side ("negative two" -> -2, "one half" ->
#               1/2, "fifty-five degrees" -> 55) before matching. Typing remains one tap
#               away and becomes automatic when a browser can't record or the visitor
#               declines the mic. Elementary courses still TAP (that IS their classroom).
#               (2) TEACH FIRST (rule 19 in the demo): every course opens with a taught
#               example -- a drawn NUMBER LINE for negative numbers, a shaded fraction
#               bar, a labelled triangle, a worked equation -- before any question.
#               (3) THREE DASHBOARDS: after the problem, three big balloons offer the
#               STUDENT, TEACHER and PARENT views; each opens full-screen with sample
#               data and Mr. Cadabra tours it in three spoken stops, then the balloons
#               return so every view stays available.
#               DEMO_VOICE_LINES: 20 APPENDED (95-114); 0-94 untouched so cached audio
#               stays valid; both lists verified identical (115 lines).
#   2026-08-09  APP_BUILD -> "2026-08-09bv-fullpage-demo". Jim: "when they click start
#               the demo, I want them to go to a full page view, and go through the
#               complete tour of the page just like we do with a new student."
#               demo.html: the welcome card stays as the front door, but Start now swaps
#               the window to the REAL classroom layout (left rail with Mr. Cadabra +
#               Curriculum / Course assessment / Progress dashboard / Practice a problem
#               / Explore a topic / Final Exam / Look it up, top bar, goal banner, the
#               three bars, the big whiteboard, the answer zone) and he walks ALL TEN
#               STOPS in the real student-tour order (build bf), each spoken with the
#               matching element glowing + a "look here" tag; the Curriculum list opens
#               for its stop and closes again (build bi). Skippable. After the tour it is
#               unchanged from bt (picker -> scripted intro -> one interactive problem ->
#               spoken congratulations). DEMO_VOICE_LINES: 7 APPENDED (88-94, the sidebar
#               stops); 0-87 untouched so cached audio stays valid; lists verified
#               identical (95 lines) and every spoken string is on the whitelist.
#   2026-08-09  APP_BUILD -> "2026-08-09bu-proactive-rules". Jim: "implement the
#               proactive rules as you see fit" (claude/Proactive_Rules_Audit_2026-08-
#               08.md). No main.py logic changes -- stamp bump only. Shipped:
#               (1) tutor.py shared rules 20-34 (answer handling, board-over-time,
#                   session endings, off-topic + a ⚠️ counsel-queued distress rule,
#                   problem quality, spaced review) -- verified in ALL TEN courses;
#               (2) number-speech rules in all eleven "HOW YOU SPEAK" blocks;
#               (3) forSpeech() on session/practice/topic: negative VALUES, percents,
#                   ratios, common + mixed fractions, thousands separators -- and the
#                   board's Unicode minus now reads as "minus" (a pre-existing gap the
#                   new test battery surfaced);
#               (4) board lines never wrap mid-equation: nowrap cells + fitRow() shrinks
#                   an oversized line to fit (the "7 + 8 + = 16 / 1(carried)" break);
#               (5) ⭐ THE PROSE REFEREE in tutor.py -- catches a reply whose SPOKEN
#                   words contradict its own board (the live 2026-08-08 "fifteen dimes"
#                   bug); narrow by design, fails open, silently regenerates;
#               (6) NEW ruletests.py -- the rule regression battery (51 offline checks
#                   + scripted live student scenarios). Not imported by the app.
#   2026-08-09  APP_BUILD -> "2026-08-09bt-classroom-demo". THE DEMO IS THE CLASSROOM
#               (Jim's redesign): /demo now opens as the real learning board (goal
#               banner + the three progress bars in the real palette + whiteboard +
#               Mr. Cadabra), speaks a welcome, gives a GUIDED TOUR of the screen
#               (board -> bars -> Mr. Cadabra, each stop spoken + glowing, skippable),
#               then the ten-course picker; picking a course plays a scripted INTRO
#               line and runs ONE real problem INTERACTIVELY (type or tap, escalating
#               help on misses -- the regular process, not a movie), ending with a
#               spoken "Congratulations" as the TODAY bar lights its first segment.
#               THE MATH KEYPAD GRID IS GONE from the demo (simple answer bar instead).
#               DEMO_VOICE_LINES: 16 lines APPENDED (indices 72-87: welcome, 3 tour
#               stops, picker invite, 10 course intros, congratulations) -- identical
#               append in demo.html; indices 0-71 untouched so cached audio stays valid.
#   2026-08-08  APP_BUILD -> "2026-08-08bs-worked-example-first". tutor.py only: new
#               shared rule 19 -- every NEW topic opens with a complete worked example
#               (tutor works every step + answer on the board, narrating why), THEN the
#               student tries a similar one ("?"-line), with the example left up until
#               their first success. "I do, then you do" (Jim's rule).
#   2026-08-08  APP_BUILD -> "2026-08-08br-resumebars-pendingline". (1) session.html
#               renders the UNIT bar at page load (curriculum + placement + quiz
#               history) -- no longer waits for [[unitplan]]; a resumed session had
#               shown only the course bar. (2) tutor.py: [[today]] required in the
#               first message of EVERY session (resumes included); rule 15 gains the
#               pending-"?"-line device ([[step eq="dollars: 2 + 1 + 1 = ?"]]) so an
#               asked step is ALWAYS on the board without running ahead.
#   2026-08-08  APP_BUILD -> "2026-08-08bq-check-student-answer". tutor.py only: new
#               rule 18 in the shared precision block -- compute the student's numeric
#               answer before accepting it (wrong answer = coaching, never adopted),
#               and spoken numbers must match the board's numbers in the same reply
#               (Jim's screenshot: "fifteen" accepted for 7+8+1 while the board wrote 16).
#   2026-08-08  APP_BUILD -> "2026-08-08bp-money-speech". "$1.85" was voiced "one dot
#               eight five". forSpeech() on all three teaching pages now reads money as
#               dollars-and-cents and plain decimals as "point" spoken digit by digit;
#               tutor.py HOW YOU SPEAK gains the matching rule. Stamp bump only here.
#   2026-08-08  APP_BUILD -> "2026-08-08bo-todaybar-stepline". tutor.py only (stamp bump):
#               (1) TODAY-bar safety net -- ensure_today_tag() mirrors the opener's own
#               goal items into [[today]] when the model skips the tag (deterministic,
#               lesson-only, never resets a live bar); rule 0(c) requires the tag.
#               (2) Rule 4 sharpened: every answered sub-step gets its own board line
#               before any combined line (the "dollars: 2 + 1 = 3" jump-to-answer catch).
#   2026-08-08  APP_BUILD -> "2026-08-08bn-no-truncated-turns". Jim's live freeze (Basic
#               Math first teaching turn showed only "Let", empty board, lesson stalled):
#               the reply hit tutor.py's 1200-token ceiling mid-tag and nothing checked
#               stop_reason. tutor.py's new _create_full() continues a capped reply via
#               assistant prefill and stitches the pieces (up to 2 continuations);
#               ceiling raised to 1600. Covers lesson + practice + topic. No main.py
#               logic changes (build stamp only).
#   2026-08-08  APP_BUILD -> "2026-08-08bm-yourturn-greenbars". (1) Rule 15 sharpened in
#               tutor.py (live catch: "your turn -- what's ten minus two times three?"
#               was asked with the new problem existing only in the spoken words): the
#               problem handed to the student must be WRITTEN on the board ([[step]]/
#               [[write]]) in the same reply it is asked; only its ANSWER stays off.
#               (2) session.html bars in Jim's palette: light-green card, white unfilled
#               segments, black text (replaces bj's dark-gray card).
#   2026-08-08  APP_BUILD -> "2026-08-08bl-firstwords-thinkflag". Static-only build (all
#               changes in session/practice/topic; bump so /health confirms the deploy).
#               (1) FIRST WORDS CLIPPED (Jim, ongoing): every TTS clip now requests
#               lead=1 (~560ms leading silence via the existing /api/speak lead param;
#               the first clip keeps lead=3) AND a suspended Web-Audio context is
#               resumed before playback starts. (2) THINKING FLAG: a red pulsing
#               "Mr. Cadabra is thinking…" badge mid-whiteboard while he thinks; hidden
#               the moment his voice starts.
#   2026-08-07  APP_BUILD -> "2026-08-07bk-times-sign". Jim's screenshot: "3 + 2 X 4"
#               showed the multiplication x styled as a red variable. Fixed both ways:
#               (1) tutor.py board rules now say WRITE × (or ·) for multiplication,
#               never the letter x; (2) styleVarsCore on session/practice/topic renders a
#               lone x between two numbers as a true × sign, unstyled (coefficients like
#               2x and real variables like "3 + x" untouched). No backend logic changes.
#   2026-08-07  APP_BUILD -> "2026-08-07bj-bars-alltour-contrast". Static-only build (all
#               changes in static/session.html; this bump exists so /health confirms the
#               deploy): (1) the today/unit preview bars now show for the WHOLE welcome
#               tour, from the first word (bi showed them only during the "bars" stop --
#               Jim: "they should all show up right at the beginning"); previews are
#               replaced by the real bars when [[today]]/[[unitplan]] render. (2) Bars
#               contrast rework (Jim: "dark gray, not super dark; the spaces in between
#               should be light"): dark-gray card, light unfilled segments, colored fills.
#   2026-08-07  APP_BUILD -> "2026-08-07bi-tour-smallfixes". THREE TOUR TOUCHES (Jim):
#               (1) the curriculum list the tour opens closes again when the tour moves on
#               (it pushed Mr. Cadabra below the fold); (2) the bars tour stop previews the
#               today/unit bars with labeled placeholders (only the course bar exists
#               before the first lesson turn); (3) the three bars sit on a dark card so
#               they stop washing out on the light page. session.html only; bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07bh-original-restated". RULE 16 SHARPENED (Jim's
#               second live catch: the check question wrote the substituted line but spoke
#               of "the original equation on the board" that had scrolled away). The rule
#               now requires re-writing the ORIGINAL equation itself, labeled, above the
#               check line, and bans the phrase "the original equation" unless this reply
#               shows it. tutor.py only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07bg-tour-polish". TOUR POLISH, FINAL ROUND (Jim):
#               (1) the talk button's emoji mic rendered as a gray "dead fly" on Windows --
#               replaced with a drawn SVG microphone on all three teaching pages;
#               (2) "Type instead" link -> a full-size "Type my answer" button (as big as
#               mic/pause), all student-facing strings updated; (3) NEW tour stop explains
#               the three progress bars (today's goals / unit topics + quiz markers + Unit
#               Quiz flag / nine units marching to the Final Exam), glowing #pbars.
#               Static only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07bf-nav-order". SIDEBAR ORDER + ONE-STOP TOUR (Jim):
#               lesson nav now reads Curriculum → Course assessment → Progress dashboard →
#               Practice a problem → Explore a topic (NEW — the lesson page never had the
#               topic link) → Final Exam → 📖 Look it up. The welcome tour covers each item
#               individually in that exact order (practice + assessment are no longer
#               explained in one breath). session.html only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07be-code-entry". CODE BOX FITS EVERY PASS (Jim pasted
#               a pass verbatim -> "not recognized"; separately his TRY-MESA44 test turned
#               out to be MY sandbox test pass, never on live). index.html's #code/#pcode
#               inputs had maxlength=12 -- but 5 of the 50 beta words make 13-char passes
#               (TRY-JUNIPER42 et al), so a verbatim PASTE silently lost the final digit ->
#               "not recognized" ~10%% of the time. maxlength now 20; inputmode=numeric
#               dropped (beta passes have letters; phones showed a digits-only keyboard).
#               Ships together with bd's forgiving login normalizations.
#   2026-08-07  APP_BUILD -> "2026-08-07bd-forgiving-codes". FORGIVING BETA-CODE LOGIN (Jim:
#               generated a pass, typed it in, "not recognized" -- the lookup demanded the
#               exact TRY-XXXX form). /api/login now retries honest normalizations of the
#               typed code (squash spaces, uppercase, add the TRY- prefix, fix a missing
#               dash) and signs in with the first that IS a real pass. "tiger42",
#               "TRY TIGER42", "try-tiger42" all work now. Pilot and parent-student codes
#               are looked up exactly as typed, unchanged. main.py only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07bc-student-reset". WIPE A PILOT/DEMO STUDENT + BETA-
#               DELETE SAFETY (Jim: "I'll be able to wipe 0000, right?" -- he couldn't:
#               0000 is a pilot persona, not a beta pass and not parent-owned, so neither
#               delete path reached it). (1) NEW POST /api/admin/student-reset (admin key,
#               student code): wipes every per-student row for that ONE code via
#               store.reset_student_data; the code keeps working as brand new (account row
#               re-created on login). 404 for unknown codes so typos never silently
#               "succeed". admin.html's Start Fresh card gained a second row for it (same
#               two-click confirm). (2) SAFETY FIX caught in review: /api/beta/delete's
#               cascade now verifies the pass EXISTS before wiping -- previously a
#               mistyped or pilot code would have its student data erased and THEN get a
#               "no pass with that code" error. Nobody hit it; now nobody can.
#   2026-08-07  APP_BUILD -> "2026-08-07bb-beta-delete". DELETE A BETA ACCOUNT (Jim: "I see
#               how to delete a parent's account by email, but I can't delete a beta
#               account" -- true: revoke only DISABLED the code and left every scrap of its
#               student data). NEW POST /api/beta/delete (admin key): removes the pass row
#               AND all data under that code via store.delete_beta_cascade (one
#               transaction). admin.html + beta.html pass tables gained a "delete" button
#               (two-click confirm) next to revoke; revoked rows can now be deleted too, so
#               the list can finally be cleaned. BONUS FIX: final_exams joined the student
#               wipe list, so parent resets also remove exam rows (table was born today).
#   2026-08-07  APP_BUILD -> "2026-08-07ba-start-at-one". UNPLACED STUDENTS START AT UNIT 1
#               (Jim's dashboard catch, confirming a parked question: a brand-new unplaced
#               Demo student was steered to Unit 2 "Addition to 20" with Unit 1 "Counting &
#               Number Sense" never touched). Root cause: chat()'s tracking fallback was a
#               flat "default Unit 2 if unplaced" -- the first turn logged "learning Unit
#               2", the mastery note then told the tutor to FOCUS there, snowball. Now:
#               unplaced activity counts toward the student's FIRST UNMASTERED unit (fresh
#               student = Unit 1); placed students unchanged; focus_unit still overrides.
#               tutor.py rule 1 companion line: no placement + no mastery data = the course
#               path starts at UNIT 1, never assume a fresh student skips ahead.
#               NOTE (same conversation): most of the other dashboard oddities Jim saw were
#               NOT bugs -- the shared demo/test code is a persistent student that remembers
#               every prior test run (AI batteries included). Use admin Start Fresh before
#               serious walk-throughs.
#   2026-08-07  APP_BUILD -> "2026-08-07az-no-self-answer". RULE 17 (Jim's live catch:
#               "five yummy cookies: how many cookies do you see?"). tutor.py's shared
#               rules block gained rule 17 -- a reply that asks a question must never state
#               or hint at its own answer (counting questions never name the count; recaps
#               name the topic, not the pending answer). tutor.py only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07ay-follow-fix2". FOLLOW FIX ROUND 2 (Jim, on the ax
#               build: Basic-Math cookies still hid below the fold). Root cause: the pages'
#               OWN anchor-scroll fired a scroll event the listener mistook for the student
#               scrolling away -> following disabled -> when the tap-to-answer row shrank
#               the transcript, the re-anchor was skipped. New autoScroll flag: only a REAL
#               student scroll releases following. Verified against the exact event
#               sequence in a node simulation. Static only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07ax-follow-turn". TRANSCRIPT FOLLOWS THE TURN (Jim,
#               first Entry-Level lesson: "the whiteboard disappears below and I have to
#               scroll constantly"). All three teaching pages: every new bubble re-engages
#               auto-follow; a tutor turn TALLER than the window anchors the view to the
#               START of the turn (words + board in view) instead of pinning to the bottom
#               (which shoved the bubble off the top); short turns still pin to the bottom.
#               Static only; build bumped for deploy verification.
#   2026-08-07  APP_BUILD -> "2026-08-07aw-pause-chips". PAUSE RESTORED + LIBRARY CHIPS
#               (Jim). (1) The ⏸ Pause button is BACK on all three teaching pages
#               (reverses this morning's removal -- with the tutor talking so much, the
#               student needs a way to stop him mid-sentence): pauses the voice, holds the
#               turn (mic + sends disabled while paused), Resume continues the sentence.
#               (2) 📖 Look it up now opens with CONTEXT CHIPS -- choices drawn from what's
#               being taught right now (the tutor's bolded key terms newest-first, the unit
#               bar's topic ladder, today's goal, the practice problem / explored topic) --
#               plus "✏️ Something else…" which reveals the type-your-own box. Students who
#               don't know what to call a thing can just tap it. Static only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07av-graph-holes". GRAPH HOLES + "SQUARED" (Jim's live
#               catches in Calculus): (1) [[graph]] gained hole="a" (math-figures.js draws
#               an open red-ringed circle on the first curve; tutor.py docs + BOARD HONESTY
#               rule extended: a spoken hole/asymptote/feature must be DRAWN, and the window
#               framed so it's visible with room on both sides). (2) forSpeech() on all
#               three teaching pages converts ² ³ π θ ± ≥ ≤ ≠ ° to spoken words -- the voice
#               was reading "x²" as "x two". Static + prompt only; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07au-course-path". RESUME CHOICE + LIBRARY IN THE TOUR
#               (Jim's live catch: he explored a MID-COURSE geometry topic, came back, and
#               "Continue my lesson" resumed the side-trip -- "I don't have a way to get
#               back to the beginning where I want to be").
#               (1) The welcome-back overlay now offers TWO buttons: "▶️ Continue where I
#                   left off" (unchanged) and NEW "🧭 Take me to my course path — Unit N",
#                   where N = the first unmastered unit from the server's mastery data
#                   (falls back to Unit 1 for a fresh course, Unit 9 if all mastered). The
#                   choice sets the focus unit and sends the NEW "__open_fresh__" sentinel:
#                   the opener is told NOT to recap/resume the side work -- welcome briefly,
#                   then the full opening sequence for that unit.
#               (2) The introductory tour gained a stop for the 📖 Look it up button
#                   (library.js injects it before the tour runs), so new students learn the
#                   reference library exists. session.html only + this note; build bumped.
#   2026-08-07  APP_BUILD -> "2026-08-07at-quiet-invite". TWO LIVE CATCHES (Jim's screenshot):
#               (1) QUIET ASSESSMENT INVITATION, PROPERLY THIS TIME. The 08-06 "card shows
#                   alone, silent, opaque" design lived only in session.html and was LOST
#                   when the runaway 08-06 chat rebuilt that file from a stale copy.
#                   Restored + hardened: offerAssessment() no longer speaks/bubbles/status;
#                   #assessInvite backdrop is OPAQUE; and NEW decline sentinels
#                   ("__open_declined__" / "__tour_done_declined__") tell the opener the
#                   card was answered "not right now" -- the tutor is instructed the
#                   question is ASKED AND ANSWERED and must not re-offer it (the old bug:
#                   student clicked no, the spoken welcome asked again).
#               (2) RULE 16 (tutor.py): a substitution/"check it" question must re-write
#                   its full equation on the board in the SAME reply -- Jim's screenshot
#                   showed "plug 4 back into two x plus five equals thirteen" spoken with
#                   only "x = 4" on the board.
#   2026-08-07  APP_BUILD -> "2026-08-07as-lookitup". THE LOOK-IT-UP LIBRARY (Jim: "a
#               searchable database covering all the topics of all the courses" -- a stuck
#               student types e.g. "binomial theorem" or "adding dollars and cents" and a
#               readable bubble opens; the tutor's voice and the chat are never involved).
#               NEW module library.py: 15 curated seed articles (aliases + fuzzy matching,
#               4 reading-level bands from the course id) + a GENERATE-ONCE fallback (one
#               strict-prompted model call for an unmatched topic, scrubbed to a safe HTML
#               subset, saved forever to the NEW store table `library_articles` -- the
#               library fills itself with what students actually ask; off-topic searches
#               refuse cleanly). NEW endpoint GET /api/library?q&course&code (students
#               only; 30 lookups / 6 generations per 5 min). NEW static/library.js: the
#               shared 📖 Look it up button (left nav) + search overlay + article bubble,
#               included on session + practice + topic. DB off -> seeds still work,
#               generated articles serve but don't persist.
#   2026-08-07  APP_BUILD -> "2026-08-07ar-champion". COURSE CHAMPION MEDAL, DIPLOMA REMOVED
#               (Jim: "a diploma implies a California-recognized school, and we are not one").
#               (1) REMOVED the GET /diploma route (the printable Certificate of Completion)
#                   and every diploma link/mention in session.html + tutor.py's final-exam
#                   prompts. Never reintroduce credential-style documents (diploma /
#                   certificate / transcript) without counsel -- they read as accreditation.
#                   (The honest homeschool RECORDS report is unaffected -- it's a log, not a
#                   credential.)
#               (2) ADDED the reward in its place: AWARD_DEFS "champion" (🏅 Course Champion,
#                   "Passed a course Final Exam") -- computed in awards_state from
#                   store.get_final_exam(course).passed per active course, persists like
#                   every award, appears in the dashboard trophy case + the NEW! celebration
#                   + the tutor's 48-hour congratulation note automatically (all generic
#                   AWARD_DEFS plumbing). students.html award catalog updated to match.
#               store.final_exams and its passed_at stamp are unchanged (now simply the date
#               the course was conquered). Exam flow, gate, and bars unchanged.
#   2026-08-07  APP_BUILD -> "2026-08-07aq-progress-finals". PROGRESS BARS + FINAL EXAM (Jim:
#               a nervous student should always SEE where they are; and a real course final).
#               (1) PROGRESS BARS (lesson page): three thin bars under the goal banner --
#                   TODAY (the opener's 2-3 goals; the tutor lights segments with the new
#                   [[today]]/[[todaydone]] tags as the student demonstrates each), UNIT (the
#                   unit's topic ladder from the new [[unitplan]] tag, with a 📝 quiz marker
#                   per topic + the 🏁 Unit Quiz at the end; passed quizzes light from the
#                   existing [[quiz]] tags + server history), COURSE (nine unit segments, gold
#                   when mastered, ending at the 🎓 Final Exam). /api/session now returns a
#                   `progress` object (mastered units, unit-quiz bests, topic quizzes, final
#                   state) so the bars are honest on load, not just live.
#               (2) FINAL EXAM, HARD-GATED (Jim's rule: prep AND exam only for students who
#                   mastered ALL 9 units at 90%). New: _final_exam_state() +
#                   FINAL_GATE_MESSAGE; ChatRequest.final ("prep"|"exam") re-verified
#                   SERVER-SIDE every turn (ineligible -> gate message, no paid call);
#                   tutor.py appends the prep/exam prompt note only after that check.
#                   POST /api/final/{code} records the [[finalexam]] score (gate-checked
#                   again; store.record_final_exam stamps passed_at once at >= 90%).
#                   GET /diploma?code&course -- printable Course Diploma, served only after
#                   a passed final. Prep = optional overview; exam = 18 questions, no hints.
#               New store table final_exams (see store.py). Nothing existing removed.
#   2026-08-07  APP_BUILD -> "2026-08-07ap-opening-order". OPENING SEQUENCE FIXED ORDER (Jim's
#               live check on Pre-Algebra: greeting, warm-up question, and THEN the goals card
#               and numbers -- backwards). tutor.py's SESSION_OPENER_RULES gained rule 0: every
#               course's first message is greeting (course welcome on a first visit) -> today's
#               topic -> today's goal + goals card -> "Ready to get started?" and STOP; the
#               first problem comes next turn, board-first. The 08-03 version of this fix was
#               elementary-only -- now universal. tutor.py only; build bumped for deploy verify.
#   2026-08-07  APP_BUILD -> "2026-08-07ao-voice-everywhere". VOICE-FIRST CLASSROOM (Jim: "back
#               to the conversational back-and-forth between the teacher and the student
#               everywhere"). Mostly a STATIC build (server changes: this note, the build id,
#               a /api/transcribe docstring update, and the Stripe product description):
#               (1) practice.html + topic.html: voice input restored (canRecord is a real
#                   capability check again, matching session.html's 2026-08-06 restore).
#               (2) MIC-HIDING BUG FIXED: math-keyboard.js still force-hid #talkBtn at
#                   DOMContentLoaded (its 2026-07-30 "type-in tier" lines), silently undoing
#                   the 2026-08-06 restore on session.html -- the mic button never actually
#                   appeared. Those lines are removed.
#               (3) 🧮 Math Keyboard RETIRED app-wide (math-keyboard.js now only provides the
#                   Enter ⏎ button + answer-bar layout; keeps its filename so includes don't
#                   404). ⏸ Pause and the Yes/No/I'm confused/Hint quick buttons REMOVED on
#                   all three teaching pages -- the student just SAYS it. KEPT: typing
#                   fallback everywhere, elementary tap-to-answer, 📈 graph tool, Enter ⏎.
#               (4) tutor.py: GRAPH_TOOL_NOTE rewritten (student talks now; transcription
#                   read charitably; no math-keyboard mentions). help-tips.js tips updated.
#               (5) "No microphone, ever" marketing/privacy claims SWEPT site-wide (landing,
#                   features, homeschool, parents, teachers, pricing, mission, privacy,
#                   llms.txt, README): new story = student talks with the tutor; voice is
#                   transcribed to text and the audio is deleted immediately, never stored.
#                   Stripe product description updated (also fixed stale "8 courses" -> ten).
#               NOTE: demo.html + DEMO_VOICE_LINES deliberately UNTOUCHED (the scripted demo
#               still types on its scripted keypad; the voice-line list is append-only).
#               ⚖️ Attorney follow-up: confirm transcribe-and-delete meets the COPPA audio
#               exemption; add voice-in (ElevenLabs Scribe) to the privacy policy + DPA set.
#   2026-08-06  APP_BUILD -> "2026-08-06an-voicein". VOICE INPUT RESTORED (Jim). The tap-to-talk
#               flow (dormant since 2026-08-01's "no microphone" master switch) is back on:
#               session.html's canRecord is a real capability check again (ON for typing courses
#               on browsers that can record; OFF for elementary tap-to-answer + unsupported
#               browsers, which type). The student taps 🎙️ → speaks → the audio posts to the
#               EXISTING /api/transcribe (ElevenLabs Scribe; unchanged, still code-gated + rate-
#               limited + hallucination-scrubbed). "Type instead" stays available everywhere.
#               No server code change beyond a docstring accuracy fix. FOLLOW-UP (Jim): the
#               "no microphone, ever" claims across marketing + privacy pages must be reworked
#               to match — separate task, flagged in the handoff.
#   2026-08-06  APP_BUILD -> "2026-08-06am-homeschoolvideo". Jim's new 77-second homeschool page
#               video embedded under the hero on /homeschool (static/videos/homeschool.mp4 +
#               homeschool-poster.jpg; controls + poster; "Homeschool Video Played" Plausible
#               event on first play — mirrors the teachers video). Frame-checked brand-correct.
#               Static assets + one page; build bumped for deploy verification.
#   2026-08-06  APP_BUILD -> "2026-08-06al-navhome". NAV: "How it works" -> "Home" on all 12
#               marketing pages (Jim: the old first nav item scrolled cold visitors straight
#               past the new hero to the four-steps section; it now opens the TOP of the
#               landing page; marked "here" on the landing page itself). The hero's "See how
#               it works" button still scrolls to #how. Static-only; build bumped for deploy
#               verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ak-tencourses-pulse". LANDING (Jim): (1) the "Hear him
#               teach" button now PULSES (radiating ring, CSS-only, stops on click, off under
#               prefers-reduced-motion) -- "it needs to catch my eye". (2) The courses section
#               was still living in the eight-course era: heading said "middle school through
#               calculus" and Entry-Level Math + Basic Math were missing from the chips. Now
#               "first grade through calculus and beyond" with all TEN courses -- and the same
#               fix in the meta/og/twitter descriptions and JSON-LD blurb. landing.html only.
#   2026-08-05  APP_BUILD -> "2026-08-05aj-hearhim-breathe". TWO LANDING ITEMS (Jim green-lit the
#               remaining design-review quick wins):
#               (1) "🔊 HEAR HIM TEACH" -- a button on the hero whiteboard plays ONE fixed line
#               of Mr. Cadabra's real voice on click (browsers allow audio after a click). The
#               line is APPENDED to DEMO_VOICE_LINES (index 71; identical append in demo.html's
#               VOICE_LINES -- the lists stay in sync, append-only) and served by the existing
#               /api/demo-audio/{i} whitelist + cache; the robot's mouth animates while it
#               plays. Fallbacks: no ElevenLabs key (204) or any error -> the button becomes an
#               honest "Hear him in the demo →" link. No new endpoint; no server change beyond
#               the appended line.
#               (2) BREATHING-ROOM PASS (landing.html): hero lede split into two short
#               paragraphs (same words); the product-screenshots section (#see) moved UP to
#               sit right after "Why families choose" (show, then tell); section padding,
#               heading margins, and line-heights opened up. Copy unchanged throughout.
#   2026-08-05  APP_BUILD -> "2026-08-05ai-heroalign". HERO LESSON RIGOR (Jim: the hero skipped
#               the both-sides step the real classroom shows). static/landing.html only: the
#               hero board now writes the operation row under BOTH sides (   − 1  − 1) before
#               the result line, equals signs column-aligned (white-space:pre), bubbles use the
#               both-sides teaching language. Static no-JS board updated to match. No server
#               change; build bumped for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ah-herolive". LIVE HERO LESSON (outside design review:
#               "the site tells more than it shows"). static/landing.html only: the hero
#               whiteboard mock now teaches a ~14s scripted mini-lesson on a loop — bubble asks,
#               student reply pill answers, board draws each step, robot face talks/smiles in
#               sync. No video, no new requests; static board preserved for no-JS and
#               prefers-reduced-motion. No server change; build bumped for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ag-featuresaccordion". FEATURES PAGE: ACCORDION REDESIGN
#               (Jim: "more visible without scrolling so far -- make everything a drop-down and
#               fit it at the top of the page"). static/features.html only: all 30 features are
#               now compact click-to-expand rows (native <details>/<summary>, no JS) in TWO
#               balanced columns (15 rows each side); page height dropped from ~4 screens to
#               under 2, with The Teaching and Proof fully visible on the first screen. All
#               titles + descriptions unchanged from build af. No server change; build bumped
#               for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05af-featuresplus". FEATURES PAGE: SIX MORE CARDS (Jim).
#               static/features.html only -- The Teaching 6->9 (Practice mode / Explore a topic /
#               a tutor who remembers you), Proof 6->9 ("How am I doing?" one click / progress
#               persists across devices / streaks build the habit), and two cards strengthened
#               (assessment card now promises the tailored PLAN; weekly-email card names TIME
#               SPENT). Sections stay multiples of three. No route or server change; build
#               bumped for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ae-featurespage". FEATURES PAGE LIVE (Jim approved the
#               draft): new static/features.html (six sections x three cards, everything real,
#               DRAFT ribbon removed) served at NEW route GET /features. NAV REORDER on every
#               marketing page (Jim: "homeschool, students, parents, teachers are the four
#               demographics we sell to -- get Courses out from between them, and put Features
#               right after Our mission"): the top-nav link order is now How it works · Our
#               mission · Features · Courses · Homeschool · Students · Parents · Teachers ·
#               Community · Pricing · Contact (page extras like Privacy/FAQ keep their spots at
#               the end; the college-math dropdown still follows Courses -- site-nav.js finds it
#               by href, not position). Routes otherwise unchanged.
#   2026-08-05  APP_BUILD -> "2026-08-05ad-assessinvite". ASSESSMENT INVITATION (Jim: when a
#               student joins a course for the FIRST time, welcome + tour as before, then warmly
#               ENCOURAGE the Course Assessment -- "find your strengths, see where to focus, and
#               I'll build a plan just for you" -- never forced; the 2026-07-28 removal of the
#               forced redirect stands). Static-only change in session.html: a spoken invitation
#               + choice card (take the assessment / start at Unit 1) shown right after the tour
#               for brand-new students, and before the opener for toured students entering a new
#               course; only when the course has no history AND no placement. Declining continues
#               the exact old flow. No server route changed; build bumped for deploy verification.
#   2026-08-05  APP_BUILD -> "2026-08-05ac-opsalerts". OPS ALERTING (pre-launch readiness review:
#               "you should learn about a broken API key from an alert, not from a parent" --
#               the one Tier-2 audit item never built). THREE pieces, all additive:
#               (1) GLOBAL ERROR HANDLER: any unhandled exception on any route now (a) prints to
#               the Render log as before, (b) is recorded to the new store.error_log table, and
#               (c) EMAILS JIM -- throttled to at most one email per error-kind per hour so a
#               crash loop can't flood the inbox. The caller gets a warm JSON 500 instead of a
#               bare stack trace. HTTPExceptions (normal 4xx "please sign in" answers) are NOT
#               errors and don't trip any of this.
#               (2) COST WATCHDOG: the existing 30-min scheduler loop now also checks estimated
#               spend over the trailing 24h (same math as /admin's cost panel) and emails Jim
#               when it crosses COST_ALERT_USD (env, dollars; unset = watchdog off). Throttled
#               to one alert per ~20h. Never guesses: silent unless the price env vars are set.
#               (3) /api/admin/stats now returns errors24 (count) + errors_recent (newest 20),
#               and /admin shows an Errors tile + a recent-errors table when there are any.
#               New env (all optional): ALERT_EMAIL (where alerts go; defaults to SMTP_USER),
#               COST_ALERT_USD (daily-spend alarm threshold), ALERT_THROTTLE_MIN (default 60).
#               Alert emails ride the existing WORKING smtp pipe (_send_email) on a background
#               thread -- an alert can never slow or crash a student's lesson.
#   2026-08-05  APP_BUILD -> "2026-08-05ab-freshreset". ADMIN "START FRESH" (Jim: a button to fully
#               reset ONE parent account by email so he can walk the brand-new-parent signup with
#               his own address, without the site recognizing him). NEW admin-only endpoint
#               POST /api/admin/parent-reset {key, email}: same FORUM_MOD_KEY gate as every other
#               admin tool; looks up the parent by that exact email and, via new
#               store.delete_parent_cascade(), atomically deletes THAT one parent + their children
#               + all per-student/per-parent rows. Touches no other account; never touches the
#               admin key or any env var. 404s (harmlessly) if no account exists for the email.
#               The /admin page gained a gated "Start fresh" card (two-click confirm) that calls
#               this and then clears THIS browser's mt_parent_token so /family opens as a stranger.
#               No existing route/behavior changed -- purely additive.
#   2026-08-04  APP_BUILD -> "2026-08-04aa-demohelp". DEMO ESCALATING HELP (Jim deliberately
#               failed a demo problem repeatedly and only ever got the same "try again" hint —
#               the scripted demo was failing the exact test skeptical parents run: does the
#               tutor ADAPT?). demo.html now escalates: miss 1 = the hint · miss 2 = "let's
#               look at it a different way" + the worked solution revealed on the board ·
#               miss 3 = show the answer warmly, note the real classroom keeps trying new
#               ways until it clicks, and move on. THREE new fixed lines APPENDED to
#               DEMO_VOICE_LINES (kept IDENTICAL to demo.html's VOICE_LINES; appended so
#               existing demo-audio cache indices stay valid).
#   2026-08-04  APP_BUILD -> "2026-08-04z-records". HOMESCHOOL RECORDS PAGE (Jim: the
#               homeschool page promises records -- "do they have a page where they can
#               download the required records?"). Now they do: /records?code=X is a printable
#               report (browser print -> paper or PDF): summary tiles, the honest hours log
#               day-by-day with per-course breakdown over a chosen range (30/90/180/365 days),
#               progress by course (placement, unit statuses, topic quizzes passed, Unit Quiz
#               best, mastered at 90%), and awards with dates. Data: NEW GET
#               /api/records/{code}?days=N (store.get_time_between + the same per-course unit
#               logic as /api/topics). Linked from the dashboard's parent/teacher box and the
#               homeschool page's records section. Honest by design: engaged minutes only,
#               real scores only, and the report itself notes that state rules differ.
#   2026-08-04  APP_BUILD -> "2026-08-04y-quizzes". QUIZZES (Jim): (1) TOPIC QUIZZES -- each
#               unit's topics are now a ladder with a short quiz (3-4 Qs) as the rung between
#               topics; PASSING (80%+, store.QUIZ_PASS_PCT) is how the student earns the next
#               topic. The tutor runs them conversationally and emits a new hidden tag
#               [[quiz unit topic name correct total]]; the pages show a "Quiz" result card and
#               POST the score to the new /api/quiz/{code} (-> store.record_topic_quiz).
#               Gating persists across sessions because _mastery_note now tells the tutor which
#               topic quizzes are passed per unit ("resume at the first unpassed topic; don't
#               re-quiz passed ones"). (2) The end-of-unit check is now called the "UNIT QUIZ"
#               everywhere students and parents see it (tag/API unchanged: [[check]] ->
#               /api/check). Mastery still = 90% (store.PASS_PCT). (3) /api/topics now returns
#               each unit's quiz rows ({name, best_pct, passed}) + quizzes_passed so the
#               dashboard (student AND the parent/teacher read-only views) shows quiz results.
#               (4) STRAY-80 FIXES from the build-w sweep: the in-lesson result card said "Unit
#               mastered!" at 80% on session/practice/topic pages, and teacher.html's heatmap
#               starred at 80 -- all four now use the honest 90. Also fixed practice.html's
#               check POST which omitted `course` (practice checks mis-filed under Algebra I).
#   2026-08-04  APP_BUILD -> "2026-08-04x-weeklymail". THE WEEKLY PARENT EMAIL -- the one
#               feature the site promised ("A weekly report in your inbox... every Friday")
#               that was still unbuilt. Assembled from parts that already existed: the SMTP
#               pipe (_send_email, proven by password resets), the windowed week numbers
#               (NEW store.week_activity), and the SAME parent-voice writing engine as the
#               dashboard's "How are they doing, really?" (tutor.get_assessment, audience
#               "parent" -- exactly what the landing page promised: "the same analytical
#               summary"). HOW IT WORKS: a daemon thread wakes every 30 minutes; in the
#               Friday send window (20:00-23:59 UTC = Friday afternoon/evening US) it sends
#               each due parent (has children, not opted out, nothing sent in the last 3
#               days) one plain-text email: per child, the week's real minutes/days, checks
#               taken (with the honest 90% mastery bar), new awards, streak -- plus the AI
#               summary for the child's most-worked course (skipped gracefully if the AI
#               errors; the numbers still go out). Zero-activity children get a gentle
#               nudge line, never guilt. CAN-SPAM hygiene: every email carries a one-click
#               unsubscribe link (random token, grants ONLY unsubscribe -- new GET
#               /api/parent/weekly-email/unsubscribe, with resubscribe), a reason line, and
#               the support address. Admin: GET /api/admin/digest-test?key=&email= builds a
#               real parent's digest and returns it as JSON WITHOUT sending (add &to= to
#               send one copy for eyeballing). Env: WEEKLY_EMAIL=off disables the scheduler;
#               sends require SMTP_* set (already live). PAGES: parents/homeschool/landing
#               weekly-email copy un-futured ("coming with launch" -> it exists now), and the
#               preview mock's "Mastered ... 84%" corrected to 92% (below the new 90% bar).
#   2026-08-04  APP_BUILD -> "2026-08-04w-mastery90". THREE OF JIM'S CHANGES: (1) MASTERY = 90%
#               now, everywhere -- store.PASS_PCT is the single source (all six hardcoded ">= 80"
#               mastery checks here now read store.PASS_PCT); tutor prompts, dashboard/teacher/
#               admin/students/teachers page texts updated; all screenshots re-shot since the old
#               captions ("80%+") were baked into the pixels. (2) NEW "GRADUATE" honor: finishing
#               a WHOLE course now renders as a 🎓 "Graduate — <Course>" trophy (was the generic
#               🏆 "Course completed" tile) -- computed live from all-9-units-mastered, so it
#               upgrades/downgrades honestly with the new bar. (3) lesson.png re-shot: it still
#               showed the old purple-sphere Mr. Cadabra in the header and speaker spots; the new
#               shot has the official logo header + robot speaker (it is also the og:image
#               everywhere, incl. the parents/teachers pages Jim saw it on).
#   2026-08-04  APP_BUILD -> "2026-08-04v-teachervideo". FIRST PAGE VIDEO (static-only; bump for
#               deploy verification). Jim's teachers video ("Rev A 8.3.26", 69s, 3MB, brand-
#               correct, built from the current screenshots) embedded on /teachers under the
#               hero: poster frame, controls, preload=metadata, playsinline, no autoplay;
#               fires a "Teacher Video Played" Plausible event once on first play. Files:
#               static/videos/teachers.mp4 + teachers-poster.jpg (new static/videos/ folder).
#   2026-08-04  APP_BUILD -> "2026-08-04u-brand". OFFICIAL LOGO (static-only; bump for deploy
#               verification). Jim delivered the brand deck ("Teachers_Video_Deck Rev 2 by SE"):
#               its gradient endpoints are #6C5AE5->#1FB5B0 -- within one shade of the site's
#               existing --purple/--teal, so NO recolor was needed (the deck was built FROM the
#               site palette). Incorporated the genuinely new piece: the logo -- a navy grid of
#               rounded squares with one golden starred tile -- rebuilt as a clean vector
#               (static/brand-mark.svg; colors #15357C/#FFC511 sampled from the deck's pixels),
#               swapped in for the purple orb dot in every nav/footer brand spot (14 pages) and
#               as the favicon. The robot face still represents Mr. Cadabra HIMSELF wherever he
#               speaks (demo speaker, hero mock, classrooms) -- logo = company, robot = him.
#   2026-08-04  APP_BUILD -> "2026-08-04t-mailfunnel". TWO ITEMS (Jim): (1) EMAIL DIAGNOSTICS --
#               his reset email never arrived. Likeliest cause: the account email is
#               jim+test@shift-work.com and forgot-password (by anti-probing design) silently
#               sends nothing for addresses without accounts. To make the pipe debuggable either
#               way: _send_email() now RETURNS the exact failure text instead of just false; a
#               new admin-only GET /api/admin/email-test?key=&to= sends a real test email and
#               reports the precise SMTP error (config shown WITHOUT the password); the forgot
#               endpoint now logs no-account / send-failure outcomes to the server log (never to
#               the caller). (2) PLAUSIBLE FUNNEL GOALS (Measurement plan #2) -- frontend fires
#               five named events (Demo Level Picked / Demo Completed / Parent Signup / Checkout
#               Started / Subscribed) via a tiny mtTrack helper in analytics.js; demo.html +
#               family.html instrumented. Cookieless, no personal data, COPPA-clean. Jim adds
#               the five goals in the Plausible dashboard to see funnel conversion.
#   2026-08-04  APP_BUILD -> "2026-08-04s-heroface". LANDING HERO ROBOT (static-only; bump for
#               deploy verification). The hero whiteboard mock still showed the old purple sphere
#               as Mr. Cadabra; it now draws his real robot face (shared tutor-face.js, gently
#               animated, sphere fallback if the script fails). Hero paragraph also now mentions
#               elementary tap-to-answer alongside typing.
#   2026-08-04  APP_BUILD -> "2026-08-04r-faq". FAQ OVERHAUL on the landing page (static-only;
#               bump for deploy verification). Jim's review caught three stale answers (no
#               Anthropic/Claude mention, "answers by typing" ignoring elementary tap-to-answer,
#               eight courses instead of ten); rewrote those and added four new questions (math
#               verified by a real engine, math-only guardrails, cost incl. family plan, devices).
#               Both the visible FAQ and the JSON-LD FAQPage schema regenerated from one list.
#   2026-08-04  APP_BUILD -> "2026-08-04q-pwreset". PASSWORD RESET + SIGN-IN FIXES (Jim tried
#               to create an account with an email that already had one and the form silently
#               flipped tabs). Backend half: (1) _send_email() -- the app's FIRST outbound
#               email, via the existing Titan mailbox over SMTP; needs env vars in Render:
#               SMTP_HOST=smtp.titan.email, SMTP_PORT=465, SMTP_USER=support@mrcadabra.com,
#               SMTP_PASS=<the mailbox password> (optional SMTP_FROM; APP_BASE_URL defaults to
#               https://mrcadabra.com). Until they are set, forgot-password answers honestly
#               that email isn't wired up and points at support@. This same pipe will later
#               carry the weekly parent email. (2) POST /api/parent/forgot -- ALWAYS answers
#               "sent" whether or not the email has an account (no probing which emails exist);
#               rate-limited per IP and per address; emails a 45-minute single-use link built
#               from a token whose HASH alone is stored. (3) POST /api/parent/reset -- redeems
#               the token, sets the new PBKDF2 hash, and signs the parent out of every device.
#               Frontend half in family.html (409 message no longer swallowed, eyeball,
#               forgot/reset forms).
#   2026-08-04  APP_BUILD -> "2026-08-04p-demoface". DEMO POLISH x3 (Jim; static-only, bump for
#               deploy verification): (1) the demo now shows Mr. Cadabra's ROBOT FACE (same
#               tutor-face.js as every classroom page) instead of a plain sphere -- mouth moves
#               while speaking, teal glow highlights him, happy face on right answers, sphere
#               kept as fallback; (2) the demo math keyboard states it is NOT a calculator;
#               (3) after a wrong check, the next key tapped REPLACES the stale answer
#               (backspace still edits it one character at a time).
#   2026-08-04  APP_BUILD -> "2026-08-04o-familyclarity". FAMILY PAGE CLARITY (static-only; bump
#               for deploy verification). Jim, seeing /family as a new parent: "HARBOR60 -- what
#               IS that? I think it's a password but I don't know for sure." The code chip is now
#               labeled LOGIN CODE - TAP TO COPY; add-a-child says a NICKNAME is fine (real name
#               not needed -- data minimization); the empty state walks the 3 steps in order.
#   2026-08-04  APP_BUILD -> "2026-08-04n-tencourses". PRICING TRUTH PASS (static-only; bump for
#               deploy verification). Jim's screenshot caught the landing pricing section stale:
#               "All 8 courses" (there are TEN since 2026-08-03), the old "ask about multi-student
#               pricing" family card (the real plan: one seat covers 2 kids, 2nd free), and the
#               Free card's "Start free" button sending people to /demo instead of the real free
#               signup at /family. Fixed on landing + the stray "eight"s on pricing (incl.
#               JSON-LD), homeschool, beta, community.
#   2026-08-04  APP_BUILD -> "2026-08-04m-costlog". MEASUREMENT #1 (Jim: "let's get started on
#               the measurement"). Every paid event is now RECORDED (counts only, never text):
#               tutor turns log their real token consumption + verifier verdict (tutor.py does
#               the logging; the four call sites here now pass the student code through), and
#               _tts_stream_response() logs every voice request's character count + whether the
#               audio cache served it free (speak + demo). /api/admin/stats now also returns
#               usage7/usage30 aggregates with estimated DOLLARS -- computed ONLY when the price
#               env vars are set (ANTHROPIC_IN_USD_PER_MTOK, ANTHROPIC_OUT_USD_PER_MTOK,
#               ELEVEN_USD_PER_1K_CHARS in Render); with no prices set it reports raw counts and
#               null dollars -- honest metrics, nothing invented. /admin renders the new section.
#   2026-08-03  APP_BUILD -> "2026-08-03l-shots". PRODUCT-SCREENSHOT REFRESH + two dashboard CSS
#               fixes (all static; bump is for deploy verification). Jim spotted the teachers-page
#               heatmap image cut off at the bottom; an audit of ALL six product screenshots found:
#               lesson.png still said "MyTutor" (it is the og:image for every page AND on the
#               landing/students pages), and dashboard/dashboard-full/parent.png were each clipped
#               mid-content. All five re-captured from the live pages (teacher.png was fixed
#               earlier today). dashboard.html also gained two real fixes the shots exposed: the
#               KPI ring no longer covers the "UNITS MASTERED" label, and the page title no longer
#               breaks mid-word next to the nav pills. landing.html alt text updated to match.
#   2026-08-03  APP_BUILD -> "2026-08-03k-ipad". iPAD/TABLET READINESS PASS -- all changes are in
#               the static pages (no backend code changed; this bump exists so the deploy can be
#               verified at /health). challenge.html + demo.html: audio was silent on iPads (audio
#               must first play INSIDE a tap; challenge awaited a fetch first, demo made a new
#               Audio element per line) -- both now unlock one shared element inside the first tap.
#               practice/topic/session: type-box 16px (stops iPad zoom-on-focus), 100dvh layout
#               (composer can't hide behind Safari's toolbar), 44px quick buttons.
#   2026-08-03  APP_BUILD -> "2026-08-03j-mathverify". THE MATH VERIFIER (Jim's pick): every
#               tutor reply is now re-checked by a real math engine (SymPy) before the student
#               sees it. The work lives in tutor.py (_create_verified + prompt rules 10-12) and
#               the NEW mathcheck.py; sympy was added to requirements.txt. main.py itself needed
#               NO code changes (the three /api/chat|practice|topic endpoints already call
#               tutor.get_*_reply, which now verify internally) -- this is the build bump only.
#   2026-08-03  APP_BUILD -> "2026-08-03i-demolevels". TEN-LEVEL DEMO (Jim): /demo now opens with
#               a level picker (all ten courses, Entry-Level Math -> Differential Equations); each
#               level runs a short scripted sample -- the elementary two answer by TAPPING (like
#               the real elementary classroom), the rest keep the math keyboard. DEMO_VOICE_LINES
#               regenerated FROM THE SAME SOURCE as demo.html's VOICE_LINES (build-verified
#               identical); the original 13 lines are unchanged so their cached audio is reused,
#               and each new line costs ElevenLabs once ever.
#   2026-08-03  APP_BUILD -> "2026-08-03h-boardprimary". BOARD IS THE LESSON (Jim: "words are the
#               backup; overutilize the whiteboard, not underutilize -- at ALL levels"). tutor.py's
#               shared GRAPH_TOOL_NOTE (prepended to EVERY course x lesson/practice/topic) gained
#               rules 7-9: never ask a student to imagine what the toolkit can draw; show CHANGE
#               (before + the change) instead of describing it; and the sound-off check -- every
#               reply must be followable with the audio muted. [[objects]] gained add="n"
#               (⭐⭐⭐⭐⭐ + ⭐) on session/practice/topic. No route changes.
#   2026-08-03  APP_BUILD -> "2026-08-03g-firstwords". THREE playtest fixes (Jim): (1) FIRST-WORDS
#               CLIP: /api/speak gained `lead` (0-4 extra ~280ms silence blocks); pages send lead=3
#               on the FIRST clip of a session, because audio outputs (esp. Bluetooth) close during
#               the thinking wait and eat the head of the first clip -- now they eat silence.
#               (2) OPENING PACING (tutor.py): the elementary opener now does welcome + goal + plan
#               card + a ready-check ONLY -- the first problem waits for the child's reply, board
#               first. (3) NEW [[objects]] board tag (session/practice/topic.html) draws countable
#               emoji rows so the tutor SHOWS five stars instead of asking a child to imagine them.
#   2026-08-03  APP_BUILD -> "2026-08-03f-elemguard". ELEMENTARY GUARDRAILS + ANSWER-BAR ELEM MODE.
#               No logic change in this file: tutor.py gained the "stay inside this course" wall and
#               the board-first-buttons-second rule (playtest: persona notes about algebra made
#               Entry-Level Math teach equations); students.json personas are now COURSE-NEUTRAL so
#               any persona can demo any course; session/practice/topic.html hide the typing gear
#               (Math Keyboard/Graph/"Two ways to answer" + their ? bubbles) for entry/basic and show
#               a tap-friendly hint + placeholder instead. Stamp bump so /health proves the deploy.
#   2026-08-03  APP_BUILD -> "2026-08-03e-elemtour". TOUR PER CLASSROOM TYPE (Jim's playtest: an
#               already-toured demo code got NO welcome/tour in Entry-Level Math and went straight
#               into a problem). The `toured` flag from /api/session is now computed per classroom
#               GROUP: the elementary tap-to-answer courses (entry/basic) count separately from the
#               typing courses, via _tour_group() + a `courses` filter on _has_any_history (DB and
#               JSON paths). So a student's FIRST elementary lesson always gets the full intro --
#               Mr. Cadabra's welcome, the "what math is" opener, the screen tour with the
#               tap-to-answer stop -- even if they toured a typing course before, and vice versa.
#               session.html also gained &tour=1 to force-replay the tour for demos/testing.
#   2026-08-03  APP_BUILD -> "2026-08-03d-cadabra". REBRAND (Jim): the product is now
#               "Mr. Cadabra's Classroom" everywhere a user can see -- all static pages (titles,
#               meta/OG, nav brands, body copy, footers), the beta-pass message, the demo line,
#               the forum fallback author (now just "A parent"), and the Stripe product display
#               name ("Mr. Cadabra's Classroom — Full access"; the finder matches the old
#               "MyTutor Full access" name too and renames it, so no duplicate product is created;
#               the internal price lookup_keys mytutor_monthly/annual are UNCHANGED on purpose --
#               they are invisible IDs and changing them would orphan existing prices).
#               "Hyperion Shift LLC" remains ONLY on /privacy and /terms (legal entity must be
#               named there) and as the invisible legalName in the landing page's structured data.
#               Same deploy: elementary welcome/tour now describe TAP-TO-ANSWER buttons instead of
#               the keyboard (session.html), and the chat pages re-pin the transcript when the
#               choice buttons appear so the tutor's words never slip out of view.
#   2026-08-03  APP_BUILD -> "2026-08-03c-tapanswers". TAP-TO-ANSWER for the elementary courses
#               (Jim: little kids can't type -- give them multiple-choice answers to click). New
#               [[choices]] whiteboard tag rendered by session/practice/topic.html as big tappable
#               answer buttons (+ an automatic "I'm not sure" button); tutor.py's elementary brain
#               and the entry/basic practice/topic scopes now emit it for every question with a
#               specific expected answer. Typing stays as a backup. No changes in this file beyond
#               the stamp -- the tag flows through the existing /api/chat reply path untouched.
#   2026-08-03  APP_BUILD -> "2026-08-03b-elemcourses". ELEMENTARY RESTRUCTURE (Jim): TWO new
#               courses BELOW Pre-Algebra -- ENTRY-LEVEL MATH (grades 1-3) and BASIC MATH (grades
#               4-6) -- each a full peer (9 units, 45-Q assessment, lesson/practice/topic). All the
#               work is in curriculum.py, pedagogy.py, tutor.py and the front-end course maps
#               (challenge/topic/session/home/dashboard/teacher + /courses catalog); main.py itself
#               only bumps the stamp, because course selection is data-driven off curriculum.COURSES
#               (which now includes "entry"/"basic"), so every /session /practice /topic /challenge
#               /dashboard route already accepts them via ?course=. ALSO: a shared static/site-nav.js
#               adds a "College level math" dropdown (Calculus, Differential Equations) to the
#               marketing top nav. No route changes; nothing removed.
#   2026-08-03  APP_BUILD -> "2026-08-03a-adminfamily". TWO features for Jim:
#               (1) FAMILY PLAN -- one paid plan now covers UP TO TWO children. New
#               KIDS_PER_SEAT=2 constant + _seats_for()/_covered_count() helpers; coverage in
#               _student_tier + _parent_payload now uses seats*2 (oldest kids covered first);
#               billing_checkout/billing_cover buy ceil(kids/2) seats so a 2nd child is free
#               and a 3rd child adds a plan (Stripe prorates). Pricing/family copy reworded to
#               "covers up to 2 children" (static/pricing.html, static/family.html). No harm to
#               Stripe checkout/portal/webhook, the free gate, or add-a-child.
#               (2) ADMIN DASHBOARD -- new /admin page (static/admin.html) + GET /api/admin/stats,
#               protected by the existing FORUM_MOD_KEY. One place for live signup/subscription/
#               engagement/beta/forum/health numbers (store.admin_stats(), aggregate counts only --
#               no names/emails/codes), the beta pass generator built in, and quick links.
#   2026-08-02  APP_BUILD -> "2026-08-02a-discovery". AI SEARCH + GOOGLE DISCOVERY (Jim):
#               new routes /robots.txt (welcomes Google + AI crawlers, hides app pages),
#               /sitemap.xml (all 13 public pages), /llms.txt (plain-text product summary
#               for AI assistants) -- files live in static/. Companion change: every public
#               page gained canonical + Open Graph/Twitter tags and schema.org JSON-LD
#               (org/product/FAQ on landing, course list on /courses, offers on /pricing).
#   2026-08-01  APP_BUILD -> "2026-08-01h-boardleads". BOARD LEADS, WORDS FOLLOW (Jim): the
#               tutor was speaking equations and arithmetic checks entirely in words while
#               the whiteboard sat empty. tutor.py's GRAPH_TOOL_NOTE gained rules 4-6: all
#               spoken math must be written on the board in symbols in the same reply, and
#               spoken text points at the board instead of narrating symbols. Prompt-only
#               change; this bump exists so /health proves the new prompt is deployed.
#   2026-08-01  APP_BUILD -> "2026-08-01g-keyterms". DETERMINISTIC first-use key-term bolding
#               (_bold_first_terms + KEY_TERMS, ~60 curated terms): the live audit showed the
#               prompt rule alone misses passing first mentions, so the server now guarantees
#               it on every chat/practice/topic reply -- skipping [[tags]], prior-turn terms,
#               and anything already bolded. Board-honesty rules added to GRAPH_TOOL_NOTE.
#   2026-08-01  APP_BUILD -> "2026-08-01f-terms180". KEY TERMS + STRAIGHT LINES (Jim's beta
#               run, round 2): GROUND_RULES tells the tutor to wrap first-use key terms in
#               **asterisks**; session/practice/topic render them bold red (.kterm). The
#               [[angle]] figure now allows deg=180 (the 175 cap was silently bending the
#               straight lines supplementary-angle lessons describe).
#   2026-08-01  APP_BUILD -> "2026-08-01e-voicefit" (Jim's beta-route test). (1) FIRST-WORD
#               CLIPPING: every TTS clip is now served with ~280ms of leading MP3 silence
#               (matching ElevenLabs' format) so slow audio outputs swallow silence, not the
#               first word. (2) POST-TOUR OPENER: new __tour_done__ sentinel -- after the
#               screen tour, the opener explicitly must NOT re-introduce Mr. Cadabra by name
#               (the tour just did); it bridges straight into the course big idea + goals.
#               (3) tutor.py opener rules: when asking the student to pick from a shown card,
#               SAY WHERE THE LIST IS and repeat 1-2 examples aloud -- no vague 'those'.
#   2026-08-01  APP_BUILD -> "2026-08-01d-howami". NARRATIVE ASSESSMENTS (Jim's long-term
#               vision: tailored, human, honest). GET /api/assessment/{code}?course&audience:
#               gathers ONLY real recorded facts (_assessment_facts: placement, per-unit
#               mastery with real check scores, practice, accuracy, streak, engaged minutes
#               over 14 days, awards, other-course activity) and has tutor.get_assessment()
#               write ONE warm honest paragraph -- student voice or parent voice. 30-min
#               in-memory cache per (code, course, audience) + 8/hr/code rate limit keeps
#               cost tiny. Dashboard gained the "How am I doing?" button (parent view asks
#               "How are they doing, really?"). The same engine will write the weekly
#               emails when those ship.
#   2026-08-01  APP_BUILD -> "2026-08-01c-onetour". (1) ONE SCREEN TOUR PER STUDENT: /api/
#               session returns `toured` = store.has_any_history(code) (any course; JSON
#               fallback scans the sessions file) -- switching courses no longer replays the
#               tour. (2) Math Keyboard sheet gained a 'this isn't a calculator -- it TYPES
#               into your answer' caption + the answer-bar reminder now names the TWO ways
#               to answer (static/math-keyboard.js). (3) Lesson sidebar hint now truthfully
#               says the answer box is at the BOTTOM of the screen.
#   2026-08-01  APP_BUILD -> "2026-08-01b-demofix". DEMO MADE REPRESENTATIVE (Jim's playtest:
#               the demo showed multiple-choice taps, but the real product has NO multiple
#               choice anywhere -- students type with the math keyboard). DEMO_VOICE_LINES
#               updated in lockstep with demo.html's VOICE_LINES: intro + first question are
#               now ONE line (the redundant "Okay, let's go" click is gone) and both concept
#               questions say "type your move". List shrank 14 -> 13 entries; audio for new
#               lines is generated+cached on first play, same as before.
#   2026-08-01  APP_BUILD -> "2026-08-01a-betastamp" (Jim: the live site looked like it takes
#               payment, but Stripe is in test mode -- "we are not taking payment at this
#               time"). NEW _payments_open(): payments count as OPEN only when the Stripe key
#               is a LIVE key (sk_live_...); test/no key = beta mode automatically, no sticker
#               to forget. billing_ready in /api/parent/me now reflects it (the /family page
#               swaps subscribe buttons for an honest beta notice), and checkout/portal/cover
#               all refuse politely with a beta message. Env override PAYMENTS_OPEN=open|closed
#               for deliberate demos. Pricing page gained a visible amber beta stamp.
#   2026-07-31  APP_BUILD -> "2026-07-31q-beta". BETA-TESTER PROGRAM (Jim: "five free logins
#               for approved beta testers... works five times... only stays open an hour or
#               two"). NEW route /beta (public pitch + mailto application; ?admin=<key> shows
#               Jim's pass generator). A beta pass (TRY-XXXX, store.beta_codes) grants FULL
#               access: each /api/login consumes one of its uses (default 5) and opens a timed
#               window (default 2h); sign-ins during an open window ride free (race-guarded);
#               progress is keyed to the pass so testers continue across days. _lookup_student
#               honors a pass only while its window is open; _student_or_404 explains expiry
#               kindly ("sign in again -- N of 5 left" / "pass used up, thanks!") instead of a
#               bare 404, and /api/login returns beta flags so the login page can greet
#               testers with their remaining count. Admin: /api/beta/create|list|revoke,
#               keyed on FORUM_MOD_KEY (constant-time compare). Marketing pages gained a slim
#               gradient BETA RIBBON under the header -> /beta.
#   2026-07-31  APP_BUILD -> "2026-07-31p-community". MISSION PAGE + COMMUNITY FORUM + HEADER v2.
#               (1) NEW route /mission (static mission.html: fun / accessible / complete / taught
#                   right -- every claim on it is something the product really does).
#               (2) NEW route /community + forum API: GET /api/forum/{section} and
#                   /api/forum/post/{id} are PUBLIC reads; POST /api/forum/post|reply require a
#                   signed-in parent token (parents post, students never; author = parent's first
#                   name or "A MyTutor parent"; title<=140, body<=4000; rate-limited 6/10min per
#                   parent + 12/10min per IP). POST /api/forum/moderate (FORUM_MOD_KEY env,
#                   constant-time compare) soft-deletes a post/reply -- hides, never destroys.
#                   Four sections: working / ideas / resources / courses.
#               (3) HEADER v2 on every marketing page + /family: spacious two-row bar (brand +
#                   buttons up top, centered links below) after Jim found the one-row fix still
#                   cramped; nav + footers gained "Our mission" and "Community" links.
#   2026-07-31  APP_BUILD -> "2026-07-31o-taxcode". FIX found in Jim's live sandbox test: new
#               Stripe accounts enable "Managed Payments" by default, which REQUIRES a tax code
#               on every product -- checkout returned "the product tax code is missing". The
#               product is now created with PRODUCT_TAX_CODE (txcd_10000000, "General --
#               Electronically Supplied Services"; override via STRIPE_TAX_CODE env var), and
#               _ensure_product_tax_code() heals the product that was already created without
#               one. An accountant can refine the classification later without a code change.
#   2026-07-31  APP_BUILD -> "2026-07-31n-accounts". REAL PARENT ACCOUNTS + STRIPE BILLING +
#               FREE-PLAN GATE (the payments foundation, built with Jim step by step).
#               (1) ACCOUNTS: POST /api/parent/signup|login|logout, GET /api/parent/me,
#                   POST /api/parent/students. Email + password (PBKDF2-SHA256, 390k iters,
#                   per-account salt, constant-time compare, timing-decoy on unknown emails;
#                   the password itself is NEVER stored or logged). Sign-in issues a 30-day
#                   random token (X-Parent-Token header). Children are FIRST NAMES ONLY and
#                   get friendly codes (MAPLE42-style, collision-checked vs students.json +
#                   accounts). Signup 5/hr/IP, login 20/5min/IP. All parent/billing endpoints
#                   require the database (503 with a clear message otherwise -- accounts must
#                   not live in throwaway JSON). NEW route /family serves the portal page.
#               (2) STUDENT LOOKUP: _lookup_student() -- students.json personas first (pilot,
#                   unchanged forever), then DB accounts with a parent_id. Every existing
#                   endpoint (chat/dashboard/awards/heartbeat/voice) works for family students
#                   with no other change.
#               (3) BILLING (cards NEVER touch this server): POST /api/billing/checkout ->
#                   Stripe-hosted Checkout (monthly $29 / annual $288 per student, quantity =
#                   number of children; prices found-or-created in Stripe by lookup_key so no
#                   dashboard clicking); /api/billing/portal -> Stripe's hosted manage/cancel
#                   page; /api/billing/cover -> prorated quantity bump after adding a child.
#                   POST /api/stripe/webhook (signature-verified via STRIPE_WEBHOOK_SECRET;
#                   payload re-parsed as plain JSON because SDK wrapper shapes drift between
#                   versions) is the ONLY writer of subscription state. Env: STRIPE_SECRET_KEY,
#                   STRIPE_WEBHOOK_SECRET, optional SITE_URL. Without keys: friendly 503s and
#                   the portal shows "payments launching soon" instead of dead buttons.
#               (4) FREE-PLAN GATE (_student_tier/_free_gate in /api/chat, BEFORE the paid
#                   Claude call): free = placement + FIRST mastered unit + unlimited practice/
#                   topic help; after their first mastered unit a free student gets a warm
#                   upgrade note, never an error. Oldest children are covered first, so adding
#                   a child never bumps a paying one to free. Pilot codes are never gated.
#   2026-07-30  APP_BUILD -> "2026-07-30m-parents". NEW route /parents serving the parent trust
#               page (what the child experiences / what the parent sees / privacy promises /
#               3-step start). "For parents" tab added to nav + footer across the marketing site.
#   2026-07-30  APP_BUILD -> "2026-07-30l-rewards". STUDENT REWARD SYSTEM + FOR-STUDENTS PAGE.
#               (1) NEW GET /api/awards/{code}: merit badges (one per mastered unit, per course),
#                   course trophies (all 9 units mastered), and effort awards (AWARD_DEFS: streaks,
#                   engaged-minute milestones, practice volume, Brave Start, Perfect Check, Bounce
#                   Back, Explorer, Pathfinder) -- all computed from data the app already records
#                   honestly. Effort awards PERSIST once earned (new store.awards table), with a
#                   48h "NEW!" window and a "next up" nudge. Design rule: every award names what
#                   the student DID -- process praise, never person praise.
#               (2) TUTOR AWARENESS: /api/chat appends a note when an award was earned in the last
#                   48h so Mr. Cadabra congratulates the effort once, then keeps teaching.
#               (3) Dashboard gained the 🏆 TROPHY CASE (dashboard.html); NEW route /students
#                   serves the student how-to page (lesson flow, tools, the earnable-awards list --
#                   keep its list in sync with AWARD_DEFS).
#   2026-07-30  APP_BUILD -> "2026-07-30k-homeschool". NEW route /homeschool serving the dedicated
#               homeschool marketing page (Jim: "this should scream homeschooling"): parent-view +
#               student-dashboard screenshots, honest engaged-time story, weekly email report
#               (labeled "coming with launch" -- not built yet), records/requirements section.
#               Homeschool tab added to nav + footer across the marketing site; landing hero pill
#               now leads with "Built for homeschool families". New shots: parent.png, timetile.png.
#   2026-07-30  APP_BUILD -> "2026-07-30j-demofix". DEMO SCRIPT FIXES (Jim's playtest): the demo's
#               board no longer reveals "x = 4" before asking the student to type it (the student
#               now computes 8÷2 and the board confirms AFTER, with a check line), and the power-key
#               instructions now give the correct order (2, then xⁿ, then 3 -- the old wording
#               produced "^23"). DEMO_VOICE_LINES updated to the six new/changed lines; MUST stay
#               identical to demo.html's VOICE_LINES.
#   2026-07-30  APP_BUILD -> "2026-07-30i-website". MULTI-PAGE MARKETING SITE + WARM DEMO VOICE
#               (Jim's feedback: one-page anchor nav felt like a one-person company; no product
#               screenshots; demo voice was robotic).
#               (1) NEW routes /courses, /teachers, /pricing serving real pages (courses generated
#                   from curriculum.py; teachers page carries a real product screenshot).
#               (2) NEW GET /api/demo-audio/{idx}: serves ONLY the demo's fixed whitelisted lines
#                   (DEMO_VOICE_LINES -- keep identical to demo.html's VOICE_LINES) in the real
#                   ElevenLabs voice via the shared TTS cache; per-IP rate limited; no arbitrary
#                   text possible, and each line is paid for at most once ever. The speak pipeline
#                   was refactored into _tts_stream_response() (shared; behavior unchanged).
#               (3) static/shots/*.png: real product screenshots (sample data, labeled) used by the
#                   marketing pages.
#   2026-07-30  APP_BUILD -> "2026-07-30h-frontdoor". THE LANDING PAGE IS NOW THE FRONT DOOR
#               (go-live prep for mrcadabra.com): GET / serves landing.html (was the bare code-entry
#               screen), NEW GET /login serves index.html, NEW GET /demo serves demo.html. All 11
#               in-app "kick back to login" redirects across the static pages were retargeted from
#               "/" to "/login" in the same change, and the landing/nav gained a Sign in link -- so
#               a parent hitting the domain sees the marketing site, and students still land on the
#               login form whenever a code is missing/invalid.
#   2026-07-30  APP_BUILD -> "2026-07-30g-timetrack". ENGAGED-TIME TRACKING (parents' "how long did
#               my kid actually work?"). NEW: POST /api/heartbeat (adds one verified minute; requires
#               a valid code; rate limited; server-side MIN_BEAT_GAP_SECONDS stops a tampered client
#               inflating the clock) + GET /api/time/{code} (per-day totals with per-course split;
#               the client computes today/this-week against the student's local calendar). Data in
#               store.py's new time_daily table. Frontend: static/time-tracker.js beats once a minute
#               ONLY while the tab is visible AND the student was active in the last 4 minutes -- an
#               open-but-idle tab counts NOTHING. Dashboard gained a "Time this week" tile. This is
#               also the data spine for the upcoming weekly parent email.
#   2026-07-30  APP_BUILD -> "2026-07-30f-lockdown". MARKET-PREP SECURITY PASS (Tier 1 of the
#               Market_Readiness_Review):
#               (1) /api/speak and /api/transcribe now REQUIRE a valid student code (they spend real
#                   ElevenLabs money and previously took none), spoken text is capped at MAX_SPEAK_CHARS,
#                   and both are rate limited. Pages pass &code= on their speak/transcribe calls now.
#               (2) NEW in-process sliding-window RATE LIMITER (_rate_limit): /api/chat, /api/practice,
#                   /api/topic capped at 40 messages / 5 min per code (far above human pace; stops
#                   runaway scripts spending the Anthropic budget); /api/login capped at 20 attempts /
#                   5 min per IP (the 4-digit code space can't be brute-forced quickly).
#               (3) TTS cache now has a 300 MB cap with oldest-first eviction (_evict_tts_cache) --
#                   it previously grew without bound.
#               (4) REMOVED the public /avatar-lab route (internal experiment; exposed internal notes
#                   and an unauthenticated paid-TTS call) -- static/avatar-lab.html is now a stub.
#               (5) REMOVED GET /api/progress/{code} + `import progress`: it served FABRICATED sample
#                   stats; verified nothing calls it (dashboard uses real /api/courses + /api/topics).
#                   progress.py is now unused and can be deleted from the repo.
#               (6) NEW routes /privacy and /terms serving the new static trust pages.
#   2026-07-30  APP_BUILD -> "2026-07-30e-opener". No logic change in this file; the bump pairs with a
#               tutor.py SESSION-opener fix (no fake "placement challenge" claim; goals card shown once).
#               Verify /health shows this stamp after deploy.
#   2026-07-30  APP_BUILD -> "2026-07-30d-topicfix". No logic change in this file; the bump pairs with a
#               tutor.py TOPIC-MODE prompt fix (goals card shows once; every turn hands the ball back so
#               the tutor never stops on a bare statement). Verify /health shows this stamp after deploy.
#   2026-07-30  APP_BUILD -> "2026-07-30c-caching". COST CONTROL: (1) TTS AUDIO CACHE on /api/speak --
#               identical text is served from an on-disk cache instead of re-calling ElevenLabs (the
#               cached bytes are the same render, so no quality change); (2) pairs with tutor.py PROMPT
#               CACHING on the model calls. Both are billing/latency only. Verify /health shows this stamp.
#   2026-07-30  APP_BUILD -> "2026-07-30b-toolhelp". No logic change here; pairs with a tutor.py change
#               so Mr. Cadabra can explain HOW to use the 🧮 math keyboard and 📈 graph paper on request.
#   2026-07-30  APP_BUILD -> "2026-07-30a-graphtool". No logic change in this file; the bump pairs with
#               a tutor.py change that teaches the tutor about the new 📈 Graph tool (coordinate graph
#               paper; plotted points arrive as text coordinates). Also new static static/graph-input.js
#               + graph script includes on session/practice/topic. Verify /health shows this stamp.
#   2026-07-29  APP_BUILD -> "2026-07-29b-scopeguard". No logic change in this file; the bump pairs
#               with a tutor.py change that adds a firm GROUND_RULES scope/jailbreak block to every
#               mode's system prompt (math-only, refuses off-topic/other-student/override attempts;
#               cross-course math still allowed). Verify /health shows this stamp after Render rebuilds.
#   2026-07-29  APP_BUILD -> "2026-07-29a-untruncate". No logic change in this file; the bump pairs
#               with a tutor.py fix that raised the student-facing reply cap max_tokens 700 -> 1200 so
#               long lesson openers (a [[goal]] plus a big [[card]]) stop getting truncated mid-tag.
#               Verify /health shows this stamp after Render rebuilds; if it's stale, do Manual Deploy
#               -> "Clear build cache & deploy latest commit". Do no harm.
#   2026-07-28  THREE FRONT DOORS -- STUDENT / PARENT / TEACHER. Stamp -> "2026-07-28s-threedoors".
#               The home page now has three clearly separated sign-in sections instead of one student
#               box with a combined "parent or teacher?" link, so each person lands on exactly the
#               view meant for them: a STUDENT on their own hub, a PARENT on their child's read-only
#               progress (/dashboard?..&view=parent), a TEACHER on every class they run
#               (/teacher?teacher=CODE). Backend change is small and additive: ClassIn gained an
#               optional teacher_code, POST /api/class passes it through, and the NEW endpoint
#               GET /api/teacher/{teacher_code}/classes lists that teacher's classes (with student
#               counts) on top of store.list_classes_for_teacher(). store.py adds ONE nullable column
#               (classes.teacher_code) via a self-healing additive migration, so classes made before
#               today still open by class code.
#               HONEST LIMIT, stated plainly: with no accounts yet these are DOORS, NOT LOCKS --
#               anyone holding a code can open that door. Separating the roles makes the app clear
#               and safe to USE; real access control is the accounts work still deferred, and a pilot
#               school must be told so. No existing endpoint, model, table or route changed.
#               Do no harm.
#   2026-07-28  "MY COURSES" -- THE DASHBOARD NO LONGER SHOWS ONLY ONE COURSE. Stamp ->
#               "2026-07-28r-mycourses". A student could only ever see the course they happened to
#               enter with, which broke the app's own core case: a student in Algebra I who is also
#               shoring up fractions in Pre-Algebra saw HALF their progress and needed four clicks to
#               reach the rest. New GET /api/courses/{code} returns every course with REAL activity
#               (units started/mastered/checked, avg best, last active) in ladder order, built on the
#               new store.get_course_activity(code) which gathers it in ONE pass over topic_progress
#               + unit_checks rather than a query per course. Courses never opened are omitted
#               (nothing invented); when tracking is off it reports that. dashboard.html renders the
#               strip and hides it entirely for a single-course student, so nothing changes for them.
#               Read-only and additive -- no existing endpoint, table, or signature touched.
#   2026-07-28  PHASE 4 -- DIFFERENTIAL EQUATIONS COURSE COMPLETE (eighth full peer, and the top of
#               the ladder). Stamp -> "2026-07-28q-diffeq". No route/logic change here (only the
#               stamp) -- `course` flows generically. Landed in curriculum.py (COURSES["diffeq"]) +
#               pedagogy.py (COURSE_PEDAGOGY["diffeq"]) + tutor.py (DIFFEQ lesson brain, CLASSIFY-
#               FIRST + scope/subject) + the 5 static files (home picker, dashboard title, topic
#               UNITS, session CURRICULUM/opener, challenge DIFFEQ 45-Q bank). Assumes Calculus and
#               does not re-teach it. Source: DiffEq_Curriculum_KB.md. Do no harm.
#   2026-07-28  PHASE 4 -- CALCULUS COURSE COMPLETE (seventh full peer). Stamp -> "2026-07-28p-calculus".
#               No route/logic change here (only the stamp) -- `course` flows generically. Landed in
#               curriculum.py (COURSES["calculus"]) + pedagogy.py (COURSE_PEDAGOGY["calculus"]) +
#               tutor.py (CALCULUS lesson brain, idea-before-machinery, heavy grapher use + scope/
#               subject) + the 5 static files (home picker, dashboard title, topic UNITS, session
#               CURRICULUM/opener, challenge CALCULUS 45-Q bank). Source: Calculus_Curriculum_KB.md.
#               Do no harm -- the six existing courses untouched.
#   2026-07-28  MR. CADABRA GETS A FACE. Stamp -> "2026-07-28o-robotface". New shared
#               static/tutor-face.js draws a small friendly ROBOT HEAD into the existing
#               <canvas id="orb"> on session/practice/topic/challenge, driven by the SAME 0..1
#               amplitude those pages already computed from the ElevenLabs audio analyser -- so his
#               mouth opens in time with his real speech. Eyes blink and drift, the antenna glows
#               with his voice, and the mood follows the page state (speaking / listening /
#               thinking / happy / idle). No new dependency, no avatar service, no extra network
#               call; if the script ever fails to load the pages fall back to a simple orb. This is
#               a deliberately stylized head, NOT the realistic 3D avatar that was tried and
#               rejected earlier. Static-only change (+ this stamp). Do no harm.
#   2026-07-28  TEACHER / PARENT CLASSROOM VIEW. Stamp -> "2026-07-28n-classroom". New: a lightweight
#               CLASS concept so a teacher or parent can follow SEVERAL students at once. Added
#               ClassIn/ClassStudentIn models, the helpers _class_or_404 + _class_student_row, the
#               endpoints POST /api/class, GET /api/class/{code}, POST+DELETE
#               /api/class/{code}/students[...], and GET /api/class/{code}/summary?course= (the
#               classroom payload: every student's per-unit best scores + class-wide per-unit
#               averages and a needs-help ranking), plus the GET /teacher page route. Roster lives in
#               store.py's new `classes`/`class_members` tables. Deliberately NOT an accounts system:
#               no password, no new personal data -- a class code just groups student codes that
#               ALREADY exist in students.json (unknown codes are rejected with a clear message).
#               Every endpoint reports tracking:false when the DB is off. Existing single-student
#               /dashboard?view=teacher is untouched. Do no harm.
#   2026-07-28  PHASE 4 -- PROBABILITY & STATISTICS COURSE COMPLETE (sixth full peer). Stamp ->
#               "2026-07-28m-probstat". No route/logic change here (only the stamp) -- `course` flows
#               generically. Landed in curriculum.py (COURSES["probstat"]) + pedagogy.py
#               (COURSE_PEDAGOGY["probstat"]) + tutor.py (PROBSTAT lesson brain built on the stats
#               visuals + scope/subject) + the 5 static files (home picker, dashboard title, topic
#               UNITS, session CURRICULUM/opener, challenge PROBSTAT 45-Q bank). Source:
#               ProbStat_Curriculum_KB.md. Do no harm -- the five existing courses untouched.
#   2026-07-28  GRAPHICS STAGE 3 -- TRIG / CONICS / NUMBER LINE / TILES / VECTORS. Stamp ->
#               "2026-07-28l-figures". Six new figures in static/math-figures.js ([[unitcircle]],
#               [[righttriangle]], [[conic]], [[numberline]], [[areamodel]], [[vector]]) routed by the
#               3 pages to showFig(). tutor.py practice/topic + the Pre-Calc lesson prompt document them.
#               No route/logic change here (only the stamp). Do no harm.
#   2026-07-28  GRAPHICS STAGE 2 -- STATISTICS & PROBABILITY VISUALS. Stamp -> "2026-07-28k-statsviz".
#               Nine new figures in static/math-figures.js ([[bars]]/[[histogram]]/[[dotplot]]/
#               [[boxplot]]/[[scatter]] with least-squares fit/[[normal]]/[[twoway]]/[[tree]]/[[pie]]),
#               routed by session/practice/topic.html to showFig(). tutor.py practice/topic prompts now
#               document them. No route/logic change here (only the stamp). Do no harm.
#   2026-07-28  GRAPHICS STAGE 1 -- REAL FUNCTION GRAPHER. Stamp -> "2026-07-28j-grapher". No route/logic
#               change here (only the stamp). New shared static/math-figures.js exposes
#               window.MathFigures.svg('graph', attrs): [[graph]] now plots ANY function of x
#               (sin/cos/tan, exp, logs, higher-degree polynomials, rationals WITH asymptotes, sqrt,
#               abs) via func=, on top of the old lines=/parabola=/points=. Wired into session/practice/
#               topic.html (a showFig() helper + [[graph]] -> showFig; math-figures.js include). tutor.py
#               graph docs now teach func=. Backend stamp so /health confirms the tutor.py deploy landed.
#               Do no harm -- purely additive.
#   2026-07-28  PHASE 4 -- TRIG / PRE-CALC COURSE COMPLETE (fifth full peer). Stamp -> "2026-07-28i-precalc".
#               No route/logic change here -- `course` already flows generically. The work landed in
#               curriculum.py (COURSES["precalc"]) + pedagogy.py (COURSE_PEDAGOGY["precalc"]) + tutor.py
#               (PRECALC lesson template + practice/topic scope + subject) + the 5 static files (home
#               picker card, dashboard title, topic UNITS, session CURRICULUM/opener, challenge PRECALC
#               45-question assessment bank). Source: PreCalc_Curriculum_KB.md. This stamp lets /health
#               confirm the backend (tutor.py) deploy landed. Do no harm -- the four existing courses
#               untouched.
#   2026-07-28  COMPREHENSIVE COURSE ASSESSMENT + COURSE-SCOPED CHECKS. Stamp -> "2026-07-28h-assessment".
#               The quick adaptive placement became a voluntary, comprehensive Course Assessment
#               (challenge.html: all 9 units x 5 Qs, per-unit 0..10 scoring, recommended-path /
#               choose-your-own results). The forced first-entry redirect was removed (home.html +
#               session.html), and a "Course assessment" link now lives in the sidebar. Backend change
#               HERE: CheckIn gained `course`, and /api/check now files the check under the RIGHT
#               course (curriculum.unit_name(course, unit) + store.record_check(..., course)) instead of
#               always Algebra I -- so the assessment's per-unit scores (and the tutor's own end-of-unit
#               checks in Geometry/Pre-Algebra/Algebra II) land on the correct per-course dashboard.
#               Backward-compatible: course defaults to 'algebra1'. Do no harm.
#   2026-07-28  PHASE 4 -- ALGEBRA II COURSE COMPLETE (fourth full peer). Stamp -> "2026-07-28g-algebra2".
#               No route/logic change in this file -- `course` already flows generically through every
#               endpoint (chat/practice/topic/placement/session/topics) to curriculum/pedagogy/tutor/
#               store, all of which now know "algebra2". The work landed in: curriculum.py (COURSES
#               ["algebra2"] + rules) + pedagogy.py (COURSE_PEDAGOGY["algebra2"]) + tutor.py
#               (ALGEBRA2 lesson template + practice/topic scope + subject) + the 5 static files
#               (home picker card, dashboard title, topic UNITS, session CURRICULUM/opener, challenge
#               ALG2 placement bank). This stamp lets /health confirm the backend (tutor.py) deploy
#               landed. Source: AlgebraII_Curriculum_KB.md. Do no harm -- other courses untouched.
#   2026-07-28  INTRO/EXPECTATIONS + COLUMN-MATH VISUAL. Stamp -> "2026-07-28f-introcolumn".
#               Backend change is in tutor.py only: (1) Topic mini-lessons now open with a topic intro +
#               a "by the end you'll be able to..." goals card; (2) all three lesson openers show a short
#               expectations goals card after the goal banner; (3) documented the new [[column]] tag for
#               stacked, decimal-point-aligned add/subtract. The [[column]] renderer itself is static
#               (session/practice/topic.html). This stamp lets /health confirm the tutor.py deploy landed.
#   2026-07-28  PHASE 4 -- PRE-ALGEBRA COURSE COMPLETE (full peer). Stamp -> "2026-07-28e-prealgebra".
#               tutor.py gained the Pre-Algebra lesson prompt + scope/subject; challenge.html a 9-tier
#               Pre-Algebra placement bank (course selection now handles 3 courses); topic.html +
#               session.html the Pre-Algebra concept/curriculum menus; home.html a Pre-Algebra picker
#               card (first) + title; dashboard.html the title label. Pre-Algebra is now pickable and a
#               full peer of Algebra/Geometry. Backend change = tutor prompt only (+ this stamp); rest
#               is static. Algebra I + Geometry unchanged.
#   2026-07-28  PHASE 4 -- PRE-ALGEBRA COURSE (catalog + teaching brain). Stamp -> "2026-07-28d-prealgcat".
#               curriculum.py + pedagogy.py gained a third course, "prealgebra" (9 foundations units:
#               number sense/order-of-ops, factors, integers, fractions, decimals, ratios, percents,
#               measurement, variables). Additive; Algebra I + Geometry unchanged (verified). NOT
#               student-reachable yet -- the Pre-Algebra lesson prompt, placement bank, unit lists,
#               and picker card come next. This stamp just confirms the new backend modules deployed.
#   2026-07-28  PHASE 4 (geometry) -- GEOMETRY WHITEBOARD FIGURES. Stamp -> "2026-07-28c-geofigures".
#               New shared static/geo-figures.js draws labeled triangles, angles, and circles; the
#               three whiteboard pages load it and dispatch [[triangle]]/[[angle]]/[[circle]] tags,
#               and the Geometry lesson prompt (tutor.py) documents them. Backend change is only the
#               tutor prompt + this stamp; everything else is static. Algebra unaffected.
#   2026-07-28  MULTI-COURSE (Phase 3.4c) -- PER-COURSE DASHBOARD. Stamp -> "2026-07-28b-coursedash".
#               /api/topics/{code} now takes ?course= and returns THAT course's units + mastery
#               (store.get_topics/get_mastery(code, course) + curriculum.units_for(course) +
#               read_placement(code, course)). dashboard.html reads the course and carries it in its
#               links. Default algebra1, so single-course behavior is unchanged. This completes the
#               per-course front door: Geometry is now a full peer of Algebra end to end.
#   2026-07-28  MULTI-COURSE (Phase 3.4b) -- PER-COURSE PLACEMENT + SESSION ENDPOINTS. Stamp ->
#               "2026-07-28a-placement". Threaded `course` through the session/placement wrappers
#               (get_session/save_session/read_placement/save_placement + a file-key helper _ck) and
#               the endpoints /api/session, /api/placement (POST + GET), plus /api/chat's session
#               get/save and placement read. So a student's lesson session AND placement are now
#               read/written PER COURSE end-to-end, and the hub gates first-entry placement per
#               course (challenge.html now serves a Geometry question bank). Algebra I is the default
#               everywhere, so single-course behavior is unchanged.
#   2026-07-27  MULTI-COURSE (Phase 3.3) -- PER-COURSE SESSION MEMORY + PLACEMENT (storage). Stamp ->
#               "2026-07-27e-coursemem". store.py's `sessions` and `placements` tables are now keyed by
#               (code, course) with the same self-healing migration (existing rows stamped 'algebra1'),
#               so a student can hold a separate lesson session AND placement per course. store's
#               session/placement functions default course to 'algebra1', so THIS file's calls are
#               UNCHANGED and behavior is identical until the picker threads a course (3.4). Verified on
#               SQLite: fresh, old-schema migration across all four course tables, separation, idempotent.
#   2026-07-27  MULTI-COURSE (Phase 3, step 2) -- COURSE-MODE LESSON PER COURSE. Stamp -> "2026-07-27d-geomlesson".
#               ChatRequest gains `course` (default 'algebra1'); /api/chat passes it to
#               tutor.get_tutor_reply (which now selects the course's lesson template), to
#               _mastery_note (course-scoped mastery steering via store), and to the course-activity
#               _track_topic (records "learning" under the right course). Nothing changes for Algebra I
#               (the default); the Algebra lesson prompt is byte-identical (verified). Geometry course
#               mode becomes reachable once the picker sends course='geometry' (Phase 3.4).
#   2026-07-27  MULTI-COURSE (Phase 3, step 1) -- COURSE-AWARE PRACTICE + TOPIC. Stamp -> "2026-07-27c-ptcourse".
#               PracticeRequest/TopicRequest gain an optional `course` (default 'algebra1'); the
#               /api/practice + /api/topic handlers pass it to tutor.get_practice_reply /
#               get_topic_reply, to curriculum.classify_unit (classify within the course), and to
#               _track_topic (which now records progress under the right course via store). Nothing
#               changes for Algebra I (the default); once the course picker sends course='geometry',
#               those two modes teach + track Geometry. Verified: Algebra prompts byte-identical,
#               Geometry assembles with its own scope + pedagogy. See Multi_Course_Expansion_Plan.md.
#   2026-07-27  MULTI-COURSE (Phase 2) -- COURSE-AWARE PROGRESS DB. Stamp -> "2026-07-27b-coursedb".
#               store.py's per-unit tables (topic_progress, unit_checks) are now keyed by
#               (code, course, unit) with a self-healing migration that stamps all EXISTING rows
#               'algebra1' (nothing lost). Every store function defaults course to 'algebra1', so
#               main.py's calls here are UNCHANGED and student-facing behavior is identical until
#               the course picker (Phase 3) supplies a course. Verified on SQLite: fresh-create,
#               old-schema migration, course separation, idempotent restart. See the project doc
#               Multi_Course_Expansion_Plan.md.
#   2026-07-27  MULTI-COURSE CATALOG (Phase 1). Stamp -> "2026-07-27a-catalog". curriculum.py and
#               pedagogy.py became a two-level course CATALOG (Course -> units) with a second course,
#               Geometry, added; both stay BACKWARD-COMPATIBLE so main.py / tutor.py are unchanged and
#               Algebra I behaves byte-for-byte as before (verified: 20 classify inputs + all playbook
#               states identical to the originals). This stamp bump only CONFIRMS Render redeployed the
#               new modules -- no route or student-facing behavior change yet (the course picker is a
#               later phase). See the project doc Multi_Course_Expansion_Plan.md.
#   2026-07-25  STT NON-SPEECH SCRUB. Stamp -> "2026-07-25b-navtype-stt". Added _clean_transcript()
#               and applied it to /api/transcribe: speech-to-text hallucinations on silence/noise
#               ("[outro jingle]", "[music]", "(applause)", musical notes) are stripped, and if
#               nothing real remains the endpoint returns "" so the UI says "didn't catch that"
#               instead of feeding garbage to the tutor. (A hallucinated "[outro jingle]" had made
#               Mr. Cadabra end a whole topic after one question.) tutor.py adds a matching topic
#               no-self-wrapup guard. Also this build ships the topic/practice nav + type-box UI.
#   2026-07-24  PHASE E -- VISUAL POLISH. Stamp -> "2026-07-24l-polish". Restyled index.html
#               (login) onto the app's design system (warm gradient bg, purple/teal brand
#               gradient, app card/shadow, gradient primary button, Mr. Cadabra orb) so the front
#               door matches the hub/dashboard/lesson pages. Front-end only (index.html); other
#               pages already share the system. (challenge.html not yet reviewed for polish.)
#   2026-07-24  PHASE D -- CONTENT-ENGINE GUARDRAILS. Stamp -> "2026-07-24k-guardrails". The
#               "verify every problem you make up" rule now lives in pedagogy.py METHODOLOGY, so
#               it reaches all three tutor modes (lesson/practice/topic) via the injected
#               playbook: the tutor solves+checks every invented problem, keeps it on-standard,
#               calibrates difficulty, and discards bad ones. Backend prompt change only.
#   2026-07-24  PHASE C -- PARENT/TEACHER PORTAL. Stamp -> "2026-07-24j-teacher". Front-end only:
#               index.html gains a "Parent or teacher? View a student's progress" entry (enter the
#               student's code -> /dashboard?code=..&view=teacher); dashboard.html adds a read-only
#               review mode (Parent/Teacher badge, a plain-language "how to help" summary, weak
#               units shown as "Focus area" instead of a lesson-launch button). Reuses /api/login
#               + /api/topics; no backend change (stamp bump only, to confirm the deploy).
#   2026-07-24  PHASE B -- STRENGTHEN-WEAK-POINTS LOOP. Stamp -> "2026-07-24i-steering".
#               ChatRequest gains optional `unit` (focus). New _mastery_note() summarizes what
#               the student has mastered vs. still needs; /api/chat injects it (+ focus_unit)
#               into the tutor context so Mr. Cadabra STEERS to weak units and does spaced
#               review. Dashboard "Work on it" -> /session?code=..&unit=N; session.html forwards
#               the unit; a focused session tracks toward THAT unit. (tutor.py: {mastery} section.)
#   2026-07-24  PHASE A3 -- MASTERY DASHBOARD. Stamp -> "2026-07-24h-dashboard". dashboard.html
#               rebuilt on the real mastery data (units mastered ring, day streak, accuracy,
#               problems practiced) + a "Strengthen next" section naming started-but-not-mastered
#               units (weakest first) with a Work-on-it link. No backend change (uses the
#               /api/topics fields A1 added). Completes Phase A (measurement spine).
#   2026-07-24  PHASE A2 -- CHECK FLOW LIVE. Stamp -> "2026-07-24g-checks". The tutor now runs
#               end-of-unit checks and marks practice problems (tutor.py prompt); the frontends
#               POST to the A1 endpoints (/api/check, /api/mark) and show a result card. Backend
#               endpoints unchanged from A1. Next: A3 dashboard shows the accumulated mastery.
#   2026-07-24  PHASE A1 -- MASTERY BACKEND. New endpoints POST /api/check/{code} (record an
#               end-of-unit check score) and POST /api/mark/{code} (count a practiced problem);
#               /api/topics now also returns per-unit best_pct/checks_taken/mastered + a summary
#               with units_mastered and stats (problems_practiced, accuracy_pct, streak_days).
#               Backed by new store.py tables (unit_checks, student_stats). Additive + guarded
#               (tracking:false when DB off) -> do no harm. Stamp -> "2026-07-24f-mastery".
#               (A2 = the tutor-run check flow that CALLS these; A3 = the dashboard that SHOWS
#               them. This A1 step is invisible plumbing until A2/A3 land.)
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24e-superscript". Reason: the board now renders
#               POWERS as real superscripts (x^2 -> x squared shown as x², 10^3 -> 10³, plus
#               pre-formed ²/³) in styleVars across session/practice/topic -- fixes "I don't see
#               the square" (it was showing a literal caret "x^2"). Front-end only.
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24d-alltranscript". Reason: practice.html and
#               topic.html were rebuilt to the SAME transcript + left-sidebar layout as the
#               lesson (scrollable feed of tutor chat + student chat + math blocks, auto-scroll,
#               controls on the left). Fixes the Topic bug where a graph overlapped the tutor's
#               text (each figure is now its own block in the flow). Front-end only; stamp
#               confirms the deploy.
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24c-autoscroll". Reason: session.html transcript
#               feed now AUTO-SCROLLS to the newest content (rAF + a MutationObserver, and it
#               stays put if the student scrolled up to read history). Front-end only; stamp
#               just confirms the deploy.
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24b-introfirst". Reason: tutor.py + pedagogy.py
#               now enforce "define the concept before any exercise" for a beginner (Topic mode
#               was drilling polynomials before defining them). Backend-only; stamp confirms the
#               redeploy.
#   2026-07-24  BUILD STAMP BUMP -> "2026-07-24a-transcript". Reason: session.html lesson
#               page was rebuilt as a single scrollable TRANSCRIPT (tutor chat + student chat
#               + worked math in one retained, scrollable feed); the right sidebar was removed
#               and the avatar + Curriculum/Practice/Dashboard nav + all controls (Pause, Tap-
#               to-talk, Yes/No/confused) moved to the LEFT; the always-on 9-unit course list
#               was removed. Front-end only (session.html); this stamp just confirms the deploy
#               landed. (practice.html/topic.html not yet converted -- pending Jim's OK.)
#   2026-07-23  BUILD STAMP BUMP -> "2026-07-23h-boardstage". Reason: Stage 3 -- the tutor's
#               spoken words now render ON the whiteboard (words + math in one place), the side
#               chat was removed, a Pause button was added (all front-end in session/practice/
#               topic.html), and tutor.py gained a "write the problem on the board when you pose
#               it" rule. This stamp confirms the tutor.py backend redeployed.
#   2026-07-23  BUILD STAMP BUMP -> "2026-07-23g-stepboard". Reason: Stage 2 -- the
#               whiteboard is now a persistent STACKING worklist driven by the new [[step]]
#               tag, and the server-side board-guessing net (ensure_board) was retired (see
#               tutor.py notes). Front-end changes are in session/practice/topic.html; this
#               stamp bump lets /health confirm the tutor.py backend redeployed too.
#   2026-07-23  BUILD STAMP BUMP -> "2026-07-23f-strongbrain". Backend reason: the tutor
#               now runs on the stronger claude-sonnet-5 brain AND injects real per-unit
#               pedagogy from the new pedagogy.py KB (see tutor.py notes). No route change
#               here -- the bump exists so /health confirms Render redeployed. REMINDER:
#               the live model is set by the Render env var CLAUDE_MODEL, which OVERRIDES
#               the code default -- set CLAUDE_MODEL=claude-sonnet-5 in Render (or delete
#               it) or the tutor stays on whatever that var says (currently Haiku).
#   2026-07-23  BUILD STAMP BUMP -> "2026-07-23e-boardsync". Backend-only reason: the
#               tutor.py whiteboard logic changed (the board no longer runs ahead of the
#               student / answers the question it just asked). No route or handler change
#               here -- the stamp bump exists so /health confirms Render redeployed the new
#               tutor.py. If /health still shows an OLDER build, the new pacing fix is NOT
#               live yet (static files push instantly, but the Python backend only updates
#               on a Render rebuild).
#   2026-07-22  AVATAR LAB (experiment). Added GET /avatar-lab -> serves
#               static/avatar-lab.html, a Ready Player Me 3D-avatar sandbox for
#               Mr. Cadabra (design an avatar, watch it talk via /api/speak). It does
#               NOT touch the live /session tutor; brain stays Claude. New route only.
#   2026-07-21  PHASE 2 -- REAL PER-TOPIC TRACKING. Course chats record Unit 2
#               (linear equations) as "learning"; Practice classifies the problem's
#               unit and records "practiced"; Topic records the chosen unit as
#               "explored" (via curriculum.classify_unit). All guarded by
#               store.enabled() and wrapped so tracking never breaks a turn. New
#               GET /api/topics/{code} returns all 9 units + honest summary for the
#               real dashboard.
#   2026-07-21  DURABLE STORAGE FOUNDATION (opt-in). Added store.py (SQLAlchemy) and
#               routed session + placement persistence through it: when DATABASE_URL
#               is set (e.g. a Render PostgreSQL instance) memory lives in the DB and
#               survives deploys/sleeps; when it's NOT set the app uses the SAME JSON
#               files as before, so nothing changes for the current deploy. /health
#               now reports storage status. This is the base for real per-topic
#               tracking, accounts, and subscriptions.
#   2026-07-21  HOME HUB + TOPIC MODE. Added GET /home (the "what would you like to
#               do today?" hub: course / practice / topic), GET /topic (topic page),
#               and POST /api/topic (mini-lesson on a chosen topic via
#               tutor.get_topic_reply; client-held history, not persisted). Login and
#               the Challenge now land placed students on /home instead of /session.
#   2026-07-21  PRACTICE MODE. Added GET /practice (serves practice.html) and
#               POST /api/practice: the student brings a specific problem from school
#               and Mr. Cadabra coaches them through it (tutor.get_practice_reply).
#               Practice history is CLIENT-held and passed in each request (sanitized
#               here), so nothing is persisted -- a homework problem is a one-off.
#   2026-07-21  ENTRY-FLOW + DURABLE-MEMORY GROUNDWORK.
#               • /api/login now also returns `placed` (has the student done the
#                 placement Challenge?) so the login screen can force first-timers
#                 to "find their level" before any lesson.
#               • /api/session/{code} now also returns `placement` + `placed` so the
#                 lesson page can enforce the flow and pick first-tour vs welcome-back.
#               • DATA_DIR is now overridable via the DATA_DIR env var so memory can
#                 live on a Render PERSISTENT DISK (e.g. /var/data) and survive
#                 redeploys/sleeps. Default unchanged (BASE_DIR/data).
#   2026-07-20  Added POST /api/transcribe: server-side speech-to-text via
#               ElevenLabs Scribe (reuses ELEVENLABS_API_KEY). The browser records
#               the student's audio and posts it here; we return the text. This
#               replaces the flaky browser SpeechRecognition. Model via
#               ELEVENLABS_STT_MODEL (default scribe_v1).
#   2026-07-19  Added Mr. Cadabra's Challenge (placement quiz): GET /challenge,
#               POST/GET /api/placement/{code} (persisted to data/placements.json).
#               Placement now feeds BOTH the dashboard (via progress.py) and the
#               tutor (the placement is injected into the tutor's progress context
#               in /api/chat, so he starts each student at the right level).
#   2026-07-19  Firmed up ElevenLabs voice_settings (stability 0.55 + speaker
#               boost) to reduce garbled words.
#   2026-07-19  Added the progress DASHBOARD: GET /dashboard (serves
#               dashboard.html) and GET /api/progress/{code} (data from
#               progress.py -- currently representative sample data, real shape).
#   2026-07-19  LOW-LATENCY VOICE. /api/speak is now a STREAMING GET that proxies
#               ElevenLabs' stream endpoint (audio starts playing before it's fully
#               generated), and the default model is now eleven_flash_v2_5 (fast).
#               Added /api/voice-status so the frontend knows whether the natural
#               voice is available before requesting it. Removed the old POST speak.
#   2026-07-19  Set the default ELEVENLABS_VOICE_ID to Jim's chosen voice
#               (sB7vwSCyX0tQmU24cW2C) so a fresh deploy uses it even without the
#               env var. Still overridable via the ELEVENLABS_VOICE_ID env var.
#   2026-07-19  Added POST /api/speak: proxies ElevenLabs text-to-speech so the
#               tutor can talk in a natural voice. The API key stays server-side
#               (env ELEVENLABS_API_KEY). If the key is missing or the call fails,
#               it returns 204 and the browser falls back to its built-in voice.
#               Voice/model configurable via ELEVENLABS_VOICE_ID / ELEVENLABS_MODEL.
#   2026-07-19  Initial Day 1 backbone. FastAPI backend that:
#                 - serves the minimal code-entry screen and the session screen
#                 - validates a student login code against students.json
#                 - runs a text chat with the tutor (tutor.py / Claude API)
#                 - remembers each student's conversation across logins by
#                   saving it to data/sessions.json
#               Voice (Day 3) and the animated orb options (Day 5) are not here
#               yet; this is the backbone they will plug into.
```

I did no harm and this file is not truncated.
