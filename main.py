# =============================================================================
# main.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-08  OLDER NOTES (before 2026-09-01) live in changelog/main.py.md
#               -- moved out on 2026-09-08 (build ui) VERBATIM, 508 entries; 75 stay here.
#               Keep adding new notes HERE, newest at top; roll them out again
#               (notes_rollout.py) when this header passes ~100 KB.
#   2026-09-10  APP_BUILD -> "2026-09-10vc-one-label-for-every-clip".
#               BUILD vc -- THE LABEL ON THE SHELF AND THE LABEL ON THE REQUEST.
#               Jim's ruling on build vb's open finding, in his words: "Go with
#               recommendation two" -- have the RECORDER tidy the sentence the same
#               way the page does, and generate the server's copy from the page's.
#               A clip is filed under a label and the label IS the sentence. The
#               prewarm filed it as authored; the page asked for it after forSpeech
#               tidied it ("Algebra II" -> "Algebra Two", "3:2" -> "3 to 2",
#               "**Area**" -> "Area"). Where those differ the clip was never found:
#               rendered once for nobody, then rendered LIVE again on every play, by
#               every student, forever. 1,943 of 39,969 course lines (11% of
#               geometry) and 306 of 306 foundations scripts -- every one of those,
#               since build cf, because each opens with a **bold** term.
#               forSpeech stays in JavaScript (the browser voice needs it too), so
#               the server's copy is a BUILD ARTEFACT: tools/genspeechmap.py runs the
#               real function in node over every authored line and writes the
#               differences to speechmap.py. Changes here:
#                 * `import speechmap` -- HARD, because the failure mode is silence.
#                 * _spoken(text) -- the ONE reader; anything absent is its own
#                   answer, so a gap degrades to pre-vc behaviour, never worse.
#                 * _closure_lines() -- mk's one owner of what the closure IS now
#                   also owns what it is CALLED. All six sites go through it.
#                 * _drill_speakable and the foundations prewarm tidy at the top.
#               ⚠️ RUN BOTH PREWARMS AFTER THIS PUSH. The correct labels have never
#               been rendered: ~403,600 characters, about $89 once. That is not new
#               spend -- it is the spend that has been repeating on every play.
#               ⚠️ REGENERATE speechmap.py after ANY edit to static/speech-text.js or
#               to an authored line. ruletests PART 3ky rebuilds it in memory and
#               fails the build when the committed file is stale.
#   2026-09-10  APP_BUILD -> "2026-09-10vb-the-next-line-is-already-loaded".
#               BUILD vb -- THE LOOK-AHEAD. Jim: "10 second latency is too long when
#               we know this is next after a correct answer we need to load that so
#               it is ready to go." Two additions here, both fail-open:
#                 * _script_warm(lesson, state) -- the spoken lines that follow a
#                   CORRECT answer to the question now pending, computed by the pure
#                   engine on a DEEP COPY (step() mutates the state it is handed, so
#                   a guess about the child must never be allowed to move the
#                   lesson). Text only, capped at SCRIPT_WARM_LINES = 3, [] on any
#                   error at all.
#                 * POST /api/script/warm -- one door for it, deliberately NOT a
#                   field on script_answer's five different returns (that is the
#                   drift this file keeps paying for), and the better moment anyway:
#                   the page asks while the QUESTION is on screen and the child is
#                   thinking, which is dead air we were paying for already.
#               `import copy` is new, with the rest of the standard library.
#               ⚠️ THE VOICE-TICKET CEILING MOVED WITH IT: speak-prep's per-code
#               limit is 60 -> 150 per five minutes, because the shelf mints its
#               ticket early and a lesson can now reach ~90 in a window. A ticket
#               is not a render (the money is spent by /api/speak, on authored
#               lines that cache forever), and a 429 here would have dropped a
#               child to the mechanical browser voice mid-lesson.
#               ⚠️ ONE OPEN LEAK THIS BUILD MEASURED AND DID NOT FIX -- Jim's call,
#               and pinned in ruletests PART 3kx so it cannot grow while he rules:
#               1,943 of the 39,969 closure lines are prewarmed under the RAW
#               authored text but REQUESTED as forSpeech(text), so the course pays
#               to render a clip no page ever asks for and then pays AGAIN, live, on
#               every play. Worst in geometry (11%) and algebra2 (8.7%). Either the
#               wire stops transforming or the prewarm starts to -- both change
#               something real, which is why it is a ruling and not a patch.
#               ⭐ THE SECOND LEAK IS FIXED HERE: session.html's whole TOUR -- ten
#               course openers, the stops, the closings, the first words every new
#               student hears -- was in no closure, so the prewarm never rendered
#               one of them. lessonscripts.TOUR_LINES puts all 29 in it (~$1.47,
#               once), and voiceclosure.py, whose hand-written list of speech
#               function names is why nobody saw it, now discovers those names.
#   2026-09-10  APP_BUILD -> "2026-09-10va-the-youngest-course-draws-every-problem".
#               BUILD va -- NO CODE IN THIS FILE CHANGED, the stamp only. Thirteen
#               Entry-Level ops that drew nothing now draw the picture that teaches
#               their skill, on the ask and on the walk-back, and the walk-back is
#               switched on in the seventeen lessons that use them.
#               ⚠️ 198 NEW VOICE LINES (about $7) -- a walk-back is spoken, one line per
#               problem. Run the script-prewarm from /admin after this push.
#   2026-09-10  APP_BUILD -> "2026-09-10uz-a-picture-counts-one-kind-of-thing". BUILD uz
#               -- NO CODE IN THIS FILE CHANGED, the stamp only. Jim's four rulings on
#               the 09-10 night watch: referee 87 (a priced story is not drawn with
#               objects), rule 15(f) (invite their method, draw their method -- rules,
#               not a referee, by his ruling), the Course Assessment loses its voice
#               (rule 18), and the 21 giveaway candidates triaged to 2 real fixes, both
#               closed by moving a bank problem.
#               ⚠️ 15 NEW VOICE LINES (about $0.29). Not one SPOKEN line was rewritten
#               -- but a bank problem IS spoken, so swapping two of them retires 16 ask,
#               re-ask, praise and walk-back lines and renders 15 new ones. "No spoken
#               line changed" is not the same as "no voice line changed"; the closure is
#               the only thing that knows the difference, and it was asked.
#   2026-09-10  APP_BUILD -> "2026-09-10uy-the-demo-keeps-time". BUILD uy -- NO CODE IN
#               THIS FILE CHANGED, the stamp only. The five demo defects Jim reported:
#               the mouth reads the real audio at last, he starts in the middle of the
#               screen, every spoken line owns its own events (so a stale utterance can
#               no longer silence the next one, and an abandoned clip can no longer be
#               counted as a server failure), the board peek runs under the words that
#               describe it, and the demo lesson's closing line is in the voice closure.
#               voiceclosure.py joined the repo.
#               ⚠️ ONE MORE NEW VOICE LINE on top of ux's 211: run the script-prewarm
#               from /admin after this push.
#   2026-09-10  APP_BUILD -> "2026-09-10ux-the-expression-comes-first". BUILD ux --
#               NO CODE IN THIS FILE CHANGED, the stamp only. Jim's four Algebra I
#               flags fixed in the OPS rather than in the flagged beats (the
#               expression before the value, x = N on every walk-back board, the bar
#               redrawn on the trap beat, the figure given the whole feed width);
#               "Got it?" retired for "With me so far?"; referee 86 reads the youngest
#               courses' reading level; deixis.py joined the repo.
#               ⚠️ 211 NEW VOICE LINES: run the script-prewarm from /admin after this
#               push.
#   2026-09-09  APP_BUILD -> "2026-09-09uw-entry-units-two-to-four-to-the-shape".
#               BUILD uw -- NO CODE IN THIS FILE CHANGED, the stamp only. Twelve
#               Entry-Level lessons (Units 2, 3 and 4) went to the shape, Jim's
#               ruling (c) landed on the reason question, referee 52 stopped reading
#               a missing addend as a completed line, and wordaudit.py joined the
#               repo. ⚠️ 181 NEW VOICE LINES: run the script-prewarm from /admin
#               after this push.
#   2026-09-09  APP_BUILD -> "2026-09-09uv-the-board-keeps-up-with-the-voice". BUILD uv --
#               WHAT HAPPENED LAST TIME, FROM THE RECORD. Jim, 2026-09-09: "They are not
#               an AI. They don't remember instantly what they did before yesterday. So we
#               have to familiarize them. This is where we are. Then we have to say, this
#               is what we're gonna do." us gave every lesson an orientation beat, but it
#               could only say THAT the previous lesson was finished -- a boolean.
#               Everything else a returning child needs was already in the store (ue's
#               script_answers, one row per graded answer; script_done.last_at) and nothing
#               read it. NEW: _days_ago_phrase ("yesterday", "3 days ago", "last week", ""
#               when nothing honest can be said) and _orientation_last (the score of their
#               last sitting at that lesson). script_start hands the prepared dict to
#               lessonscripts.lesson_orientation, which puts it on the CARD and leaves the
#               spoken line alone -- a pre-rendered clip, so uv adds NO voice lines and
#               needs no prewarm. Fail-open at every step: no store, no rows, a bad date or
#               an impossible score simply drops that part of the line (rule 0: a recap is
#               a memory, not a guess), and the score is only ever asked for a lesson the
#               record says was FINISHED. FIRST-TRY answers to REAL questions only -- the
#               guided pairs are the tutor's own work and would inflate a child's score.
#   2026-09-09  APP_BUILD -> "2026-09-09uu-the-front-door-quieted". BUILD uu. NO CODE IN
#               THIS FILE CHANGED -- the stamp only. static/landing.html (served at "/")
#               is now the quiet front door Jim asked for on 28 Aug and approved as the
#               1 Sep mockup: one row of nav, one sentence, the pencil, three honest doors
#               (/demo/lesson, /demo?tour=1, /login), every old nav link in the footer.
#               No route changed; /demo/lesson and /demo?tour=1 are uh's and rk's doors.
#               PART 3kq pins it, live at two sizes.
#   2026-09-09  APP_BUILD -> "2026-09-09ut-the-first-watch-on-the-new-stack". BUILD ut. NO
#               CODE IN THIS FILE CHANGED -- the stamp only. The 09-09 night watch (the
#               first on the us stack: 0 errors, every closure line rendered) gave tutor.py
#               one falsehood row, the times sign in the notation registry, and three narrow
#               referees (arrowpointer, pictured, problemnumbers); ruletests PART 3kp pins
#               them. /health reads the new stamp after the push.
#   2026-09-09  APP_BUILD -> "2026-09-09us-orient-then-one-idea-per-beat". BUILD us -- THE
#               SHAPE JIM CHOSE: ORIENT, THEN ONE IDEA PER BEAT WITH A CHECK. Jim, after a
#               live lesson: "if you just sat down for the first time, what do you need?
#               You need to get oriented. A little review. What we're gonna do today. Then
#               step by step." IN THIS FILE: script_start inserts the ORIENTATION as the
#               second step, after the intro -- lessonscripts.lesson_orientation(lesson,
#               prev_done), where prev_done is the RECORD's word (store.get_script_done)
#               that the previous lesson in the order was finished; no record, no store,
#               any error -> the "Today" form, never a lost lesson. _script_clean attaches
#               `beat` to every say step (lessonscripts.beat_of) so the page can pause on
#               it: the check after a picture, teach or worked beat and the ready gate
#               after the practice intro live in session.html. The engine's walk is
#               unchanged. PART 3ko pins it, live end to end.
#   2026-09-09  APP_BUILD -> "2026-09-09ur-the-wrong-answer-is-answered-at-once". BUILD ur --
#               Jim's flag 21:41 (algebra2): "more than 30 second wait after a wrong answer".
#               The answer endpoint resolved the model's re-teach (verified up to three
#               times, ~10 s each) BEFORE responding, so the engine's own "Not quite --
#               let's look at it together" reached the student only after the whole wait.
#               NEW: ScriptAnswerIn.defer_ai -- the answer turn returns at once (the
#               verdict, the star, the hold line, an {"kind": "ai_pending"} marker) and
#               stores the deferred turn on the session; NEW POST /api/script/intervene
#               (_script_deferred_run) runs it: the same model turn, bookkeeping (mode,
#               history, redo), askboard floor and fail-open (no reply -> the engine's own
#               retest) that lived in the answer turn, at both sites (the first
#               intervention and the wrong-again redo). FAIL-SAFE: an answer that arrives
#               while a re-teach is still deferred resolves it first, silently; a page
#               that does not send defer_ai (pilot.html) gets exactly the old shape.
#               session.html sends defer_ai and speaks the wait (LINE_THINKING). PART 3kn
#               pins it through the TestClient, statically, and live in a browser with the
#               re-teach delayed twelve seconds.
#   2026-09-08  APP_BUILD -> "2026-09-08uq-the-problem-is-always-on-the-board". BUILD uq --
#               Jim's corrections queue (13 flags from a live precalc/algebra2 session; the
#               triage is claude/Triage_Corrections_Queue_2026-09-08_...). IN THIS FILE:
#               _ai_board_floor(board_tags, ask_board) -- an `ai` intervention step whose
#               reply carries no drawing or writing tag gets the ask's own board (the one
#               the engine put on the intervene step) prepended, at BOTH ai-step sites
#               (the first intervention and the wrong-again redo). Jim's flags 22:03/22:05:
#               the live tutor re-asked "what is f of g of 2?" with no board, and he "had
#               to guess since there was audio of the problem but no text and no visual".
#               Event code_repair "askboard". Elsewhere in uq: the practice-intro card and
#               the absc/fcmp boards (lessonscripts.py), the rewritten graph-slides and
#               inside-the-distance lessons (lessons/), speech-text.js's quotation rule,
#               the eighty-first referee's "back to our first machine" phrase (tutor.py).
#   2026-09-08  APP_BUILD -> "2026-09-08up-a-new-machine-still-called-f". BUILD up. NO
#               CODE IN THIS FILE CHANGED but the stamp. uo's honest gap closed on Jim's
#               word: the authored function practice retires the name out loud in every
#               problem ("A new machine, still called f"), and the eighty-first referee
#               reads [[machine]] cards as definitions. PART 3kl pins it.
#   2026-09-08  APP_BUILD -> "2026-09-08uo-one-name-per-function". BUILD uo. NO CODE IN
#               THIS FILE CHANGED but the stamp. Jim's three rulings on the 09-08 watch:
#               the eighty-first referee, tutor.function_redefined_conflict (rule 28: one
#               letter names one function, all conversation -- fed heard_tutor); the
#               prompt's rule-28 clause; RULED_ALLOWED row seven (rule 48: a board equation
#               built from introduced symbols is not new notation); mathcheck's
#               expressions_equal. PART 3kk pins it.
#   2026-09-08  APP_BUILD -> "2026-09-08un-the-figure-that-never-came". BUILD un. NO CODE
#               IN THIS FILE CHANGED but the stamp. The 2026-09-08 night watch's truth items
#               and proven holes, all in tutor.py: the rule-61 referees read the prose with
#               markdown emphasis stripped (the **division** dodge); two new falsehood rows
#               (the hundredths place; parentheses never multiply); the story-units grammar
#               reads "two bags of candy with four pieces each"; postponed_show's branch
#               three (a figure asked for, only text tags landed); the eightieth referee,
#               triangle_letters_unspoken_conflict (rule 14). PART 3kj pins it.
#   2026-09-08  APP_BUILD -> "2026-09-08um-the-tap-unlocks-the-sound". BUILD um. NO CODE IN
#               THIS FILE CHANGED but the stamp. Jim, on his phone after the push: the demo
#               lesson had no sound. static/demo-lesson.html never primed the audio inside
#               a tap and its ?course= door autostarted with no tap at all -- phones play
#               both silently. The page unlocks the sound inside every tap that starts
#               speech and ?course= shows a Start door instead. PART 3ki pins it.
#   2026-09-08  APP_BUILD -> "2026-09-08ul-the-landscape-phone". BUILD ul -- THE LANDSCAPE
#               PHONE. NO CODE IN THIS FILE CHANGED but the stamp. A release rehearsal of the
#               whole unpushed stack (tt..uk) on a real Postgres -- every route, a fresh
#               database and the upgrade path, a family and a teacher, 44 page renders --
#               found one defect: a phone turned sideways (844x390) showed a 38px board.
#               session/practice/topic gain a last-declared block for short screens;
#               cadabra.js rule 33 treats a short window as a phone (the menu's
#               phone.maxHeight). PART 3kh pins and measures it.
#   2026-09-08  APP_BUILD -> "2026-09-08uk-the-mark-floor". BUILD uk -- THE MARK FLOOR
#               (F4 of the 09-06 night watch; Jim ruled 09-07: build it, no retry). NO CODE
#               IN THIS FILE CHANGED but the stamp. tutor.py: repair_missing_mark at the
#               shipping door -- a spoken, unambiguous verdict on a numbered quiz answer
#               that forgot its [[mark]] gets the mark from code (the page posts it to
#               /api/mark/me exactly as a model-written mark). PART 3kg pins it.
#   2026-09-08  APP_BUILD -> "2026-09-08uj-one-file-per-course". BUILD uj -- ONE FILE PER
#               COURSE (housekeeping, second half). NO CODE IN THIS FILE CHANGED but the
#               stamp. lessonscripts.py's 360 lessons now live in lessons/<course>.py (ten
#               pure-data files joined by lessons/__init__.py); lessonscripts.py imports
#               them and keeps every name this file reads (LESSONS, LESSON_BY_ID,
#               COURSE_ORDER, PILOT_LESSON, start, step, ans ...). The data was proved
#               deep-equal before and after; PART 3kf pins it.
#   2026-09-08  APP_BUILD -> "2026-09-08ui-the-notes-move-out". BUILD ui -- THE NOTES MOVE
#               OUT (housekeeping). NO CODE IN THIS FILE CHANGED but the stamp. This header
#               was 552 KB -- 48% of the file, 583 dated notes back to 2026-07-19. Every note
#               dated before 2026-09-01 now lives in changelog/main.py.md, verbatim and in
#               order (notes_rollout.py, new at the repo root, did the move and proved it
#               lost nothing); the pointer above says so. Same for tutor.py, store.py,
#               ruletests.py, lessonscripts.py, prompts.py, session/practice/topic/demo.html.
#               The battery's dated-note pins now read notes(<file>) -- the header PLUS the
#               changelog -- instead of a fixed slice that slid as notes were added above
#               it (PART 3ke). Nothing a student sees changed.
#   2026-09-08  APP_BUILD -> "2026-09-08uh-the-demo-teaches". BUILD uh -- P3 OF THE DEEP
#               LOOK. The demo was a tour of the furniture with an empty board; it never
#               showed a lesson. Now the front door leads to /demo/lesson (NEW route,
#               static/demo-lesson.html): pick a level, and Mr. Cadabra teaches the
#               opening of that course's FIRST authored lesson exactly as a student
#               hears it -- the why, the picture, the rule read off it, the worked
#               example, one question answered by tap or typed words, the walk-back --
#               then offers the classroom tour (/demo?tour=1) and the three views
#               (/demo?views=1). THE DEMO LESSON LANE (/api/demo/lesson/levels, /start,
#               /answer): the real engine, a fixed seed, _script_clean (never an answer
#               key), the classroom's three grading doors, NO student, NO store write,
#               NO model (intervene -> the engine's resume), opaque short-lived tokens,
#               eight graded answers per token, per-visitor rate limits. THE VOICE: a
#               "demo" lane on /api/speak-prep -- the drill lane's twin (closure-only,
#               cache-only: a visitor can never make the paid renderer run), no student
#               code, rate-limited per visitor. speak_prep gains `request` for that.
#               session.html: the youngest students get a THREE-stop tour (its own doc).
#   2026-09-08  APP_BUILD -> "2026-09-08ug-the-phone-classroom". BUILD ug -- P1 OF THE
#               DEEP LOOK. NO CODE IN THIS FILE CHANGED; this is the stamp. The work is in
#               static/session.html, practice.html, topic.html, demo.html (a bounded board
#               and a three-row dock on every screen <=900px; a one-line top row, the icon
#               nav on its own row, bubbles clear of the pencil and the lesson title
#               wrapping on phones <=640px; the mic reads "Listen…" while it is dark),
#               static/cadabra.js (rule 33: small, in the board's corner, no wander on a
#               phone) and the menu's new `phone` block. ALSO FIXED THERE: on every screen
#               <=900px the board had no bound on its height, so board.js's top-anchoring
#               pad grew it without limit (853,422px measured after forty seconds) -- the
#               app is the viewport now and the board scrolls, as on a desktop.
#   2026-09-08  APP_BUILD -> "2026-09-08uf-the-per-student-view". BUILD uf -- P2 OF THE
#               DEEP LOOK, SECOND HALF. The admin console could see totals and 37 tables
#               but could not answer "how is Sam doing". NEW GET /api/admin/student?code=
#               (general admin tier, X-Admin-Key header only, rate-limited, 404 for an
#               unknown code): one student, everything, read-only -- the courses they
#               touched with every unit's status in the ue words, the lessons done with
#               dates and the three-in-a-row flag, every graded answer in the authored
#               lane (script_answers, newest first, the question and the expected
#               beside the answer), topic quizzes, Unit Quizzes, engaged minutes by day,
#               awards, the whole-student stats. BY CODE, TYPED: there is deliberately
#               NO route that lists student codes (F2 closed enumeration). admin.html
#               gains the "One student" card under the board. store.student_courses is
#               the one new reader. No teaching, no lane, no store write changed.
#   2026-09-07  APP_BUILD -> "2026-09-07ue-the-authored-lane-writes-it-down".
#               BUILD ue -- P2 OF THE DEEP LOOK, FIRST HALF (Jim's order: P0, P2, P1).
#               The review drove five whole authored lessons and the admin console
#               read "0 problems practiced": the scripted lane kept one row per
#               finished lesson (script_done) and the streak, and nothing per answer.
#               (1) EVERY GRADED ANSWER IS WRITTEN DOWN. _script_note_ask remembers the
#                   question on screen (a new pending problem resets the try count and
#                   starts the clock; a re-ask after "unheard" keeps both -- unheard is
#                   not a try); _script_record_answer writes one script_answers row
#                   (store.py, new) at each of the lane's THREE grading points -- the
#                   ordinary ask at the engine's own line, the reason question by its
#                   label, the intervention redo -- with the verdict the star already
#                   uses. Fail-open everywhere: a lost row never costs a turn. The
#                   streak, the engine and the payload are untouched.
#               (2) "LESSON DONE" IS NOT "MASTERED". Jim's ruling (2026-09-07): "Mastered"
#                   is the 90% Unit Quiz and nothing else. _script_finish writes "taught"
#                   for a mastered end (was "mastered"); the passed topic quiz writes
#                   "taught" (was "mastered"); store.record_check stays the one writer of
#                   "mastered", and store's one-time migration un-says the historical
#                   rows. _goal_suggest counts a taught unit as a practice pick.
#               (3) /api/topics and /api/records units carry lessons_done / lessons_total
#                   (_lessons_by_unit, from script_done and the course's lessons); the
#                   dashboard's stats carry lesson_answers / lesson_first_try_pct /
#                   lessons_done beside the live lane's counters (store.get_mastery),
#                   never blended -- Jim's apart-from-the-course ruling (mt) stands and
#                   the pages ADD the lanes and say so.
#               ENGAGED MINUTES WERE NEVER MISSING: /api/heartbeat counts them from
#               time-tracker.js on every learning page, scripted lane included; the
#               review's zero came from driving the lane by API with no page open. No
#               second clock is added -- it would double-count.
#   2026-09-07  APP_BUILD -> "2026-09-07ud-the-small-fixes-of-the-deep-look".
#               BUILD ud -- P0 OF THE DEEP LOOK (claude/Review_Deep_Look_2026-09-07.md;
#               Jim chose P0, then P2 data, then P1 phone). THIS FILE:
#               (1) THE OWNER'S TOOLS ARE THE OWNER'S. static/pilot.html (and the /pilot
#                   route), cadabra-lab.html (the bench), demolab.html (the layout
#                   concept), avatar-lab.html (the retired stub) and static/mockup/ were
#                   served to anyone who typed the address. StaticFiles is now
#                   _OwnerGatedStatic: those paths answer 404 to the public -- the same
#                   answer a missing file gives -- and open for the X-Admin-Key header or
#                   the HttpOnly mt_owner cookie that POST /api/owner/unlock sets (admin
#                   .html calls it as the dashboard unlocks; /api/owner/lock drops it).
#                   The cookie is HMAC(FORUM_MOD_KEY, label): rotate the key and every
#                   browser is out; an unset key closes the tools to everyone. shots/
#                   stays public (the marketing pages show those screenshots).
#               (2) THE PUBLIC SIGN-IN PAGE STOPS TALKING LIKE A DEV BOX. SHOW_TEST_CODES
#                   (unset: follows ALLOW_FILE_FALLBACK, so a dev box shows them and
#                   Render does not) reaches index.html through GET /api/site-flags,
#                   booleans only; the "not yet security" note is rewritten to what is
#                   true. health() reports both flags.
#               ELSEWHERE (no main.py change): the public copy that still sent the
#               youngest students to the buttons INSTEAD of the microphone (landing,
#               features, teachers, students, homeschool) reads the uc order; the
#               methodology prose's "58 separate checks" (the tile said 79) now sits in
#               <span data-referees> pinned to the count in tutor.py; practice/topic's
#               "How to answer" line is short and light in their narrow sidebar.
#               NOT DONE, ON PURPOSE: the drill room keeps its "Abrabot" name -- builds
#               mh/mt made him a deliberate second character (the browser's voice, no
#               cost, no mastery) and the tour introduces him as "my helper"; that is a
#               design choice for Jim, not a defect. PART 3jz pins all of the above.
#   2026-09-07  APP_BUILD -> "2026-09-07uc-the-youngest-speak-and-the-mic-waits".
#               BUILD uc -- TWO OF JIM'S CHANGES, both about how the student answers.
#               (1) Entry-Level and Basic answer the way the other eight courses answer:
#               say it, type it if you'd rather, tap a button if you like. Jim: "we sent
#               one out and said nobody has to write the answer, everybody can just speak
#               the answer ... we should have gone back to the first two courses." Every
#               instruction that sent them to the buttons FIRST now reads what the other
#               courses read (session/practice/topic: the answer-bar line, the ready hint,
#               the tour's last stop, the welcome tip, the composer placeholder), and
#               prompts.py tells the tutor the same thing. THE BUTTONS ARE UNTOUCHED --
#               every course ships them, referee 58 and build qw's guarantee still put a
#               row under every elementary question; what is gone is the instruction to
#               use them INSTEAD of talking. The two symbol pads stay hidden there.
#               (2) The microphone waits for the speaker (session.html): a scripted ask
#               beat opens the taps and the typing box the moment the question lands --
#               builds nb/pd, unchanged -- and now holds the MIC dim until the spoken line
#               ends. Jim: "let the speaker do the speaking. And as soon as they're done
#               ... they light up." No route, engine or lesson change: this build is the
#               three teaching pages, prompts.py, and their battery.
#   2026-09-07  APP_BUILD -> "2026-09-07ub-calculus-units-seven-to-nine-to-the-shape".
#               BUILD ub -- Calculus Units 7-9 (the integral, its uses, differential
#               equations) rewritten to the shape: twelve lessons, each with a why, a
#               picture drawn before the rule, the rule read off the picture, two worked
#               examples drawn on it, every right answer walked back on the picture, a
#               reason question after the streak, and a recap. ⭐ CALCULUS 36/36. The
#               area under the graph is SHADED on every integral ask with "?" written in
#               it and the area written on the walk-back -- static/math-figures.js learns
#               [[graph shade="lo..hi" label="?"]] and between="1"; every canon graph
#               draws byte-for-byte as before (1,455 of them). No route change.
#   2026-09-07  APP_BUILD -> "2026-09-07ua-calculus-units-four-to-six-to-the-shape".
#               BUILD ua -- Calculus Units 4-6 (derivatives at work, optimisation,
#               antiderivatives) rewritten to the shape: twelve lessons, each with a why,
#               a picture drawn before the rule, the rule read off the picture, two worked
#               examples drawn on it, every right answer walked back on the picture, a
#               reason question after the streak, and a recap. CALCULUS 24/36. The speed
#               line, the valley, the hump and the cubic are drawn with the answer
#               withheld; the fence is a tape and the square a metre grid; the reverse
#               power rule is a machine. One ask wrote a chain of equals ending in "= ?"
#               on all twelve of its problems (rule 15) and writes two statements now.
#               static/math-figures.js: a [[graph]] keeps a five-digit y label whole by
#               growing its canvas leftward; every canon graph draws byte-for-byte as
#               before. No route change.
#   2026-09-07  APP_BUILD -> "2026-09-07tz-calculus-units-one-to-three-to-the-shape".
#               BUILD tz -- Calculus Units 1-3 (limits, the derivative, the rules)
#               rewritten to the shape: twelve lessons, each with a why, a picture drawn
#               before the rule, the rule read off the picture, two worked examples drawn
#               on it, every right answer walked back on the picture, a reason question
#               after the streak, and a recap. CALCULUS 12/36. The limit lessons draw the
#               curves themselves (the hole, the two shelves, the fraction flattening);
#               the derivative lessons draw the point on the ask and the tangent on the
#               walk-back; the rule lessons run the power and chain rules as machines.
#               Every single-curve graph names its legend (the raw "(36*x^2)/..." no
#               longer prints). No engine or route change: this build is lessonscripts.py
#               and its battery.
#   2026-09-07  APP_BUILD -> "2026-09-07ty-probstat-units-seven-to-nine-to-the-shape".
#               BUILD ty -- Probstat Units 7-9 (expected value, the normal curve,
#               confidence) rewritten to the shape: twelve lessons, each with a why, a
#               picture drawn before the rule, the rule read off the picture, two worked
#               examples drawn on it, every right answer walked back on the picture, a
#               reason question after the streak, and a recap. ⭐ PROBSTAT 36/36. Two asks
#               that said "how many students" ask about the whole group now (rule 42);
#               three that wrote a question inside a step write statements. No engine or
#               route change: this build is lessonscripts.py and its battery.
#   2026-09-07  APP_BUILD -> "2026-09-07tx-the-words-and-the-picture-are-the-same-thing".
#               BUILD tx -- the last two proven holes from the 09-06 watch. THE 79TH
#               REFEREE, shares_picture_conflict: a story about a chocolate bar drawn as
#               a [[pie]] (or a pizza drawn as a bar). RULES.md itself recorded that half
#               of rule 63 as prompt-covered and a scenario candidate; the scenario found
#               it. And board_count_conflict learns the STORY nouns (bags, candies,
#               marbles...) and the "plus N loose" claim it had no pattern for at all --
#               so a drawing that omits the four loose candies the voice just promised is
#               caught against the tag's own add= attribute. Plus Jim's 2026-09-07 ruling
#               on N10 as RULED_ALLOWED row six: the money model for decimals is teaching,
#               not a units defect. Referees 78 -> 79; truth class unchanged at 11.
#   2026-09-07  APP_BUILD -> "2026-09-07tw-the-say-it-then-write-it-family".
#               BUILD tw -- three proven holes from the 09-06 and 09-07 watches, all of
#               them a student looking at something the voice never gave them. (1) The
#               ask-lists (_VIS_ASKED, _RD_ASKS) learn "give me an example", "an
#               example?", "like what?" and "show me one" -- they knew only "show me an
#               example", so the same request in the words a student actually uses went
#               unrefereed. (2) THE 78TH REFEREE, op_unspoken_conflict: an operation
#               drawn over both sides ([[step op="- 5"]]) while the voice says only the
#               goal. Rule 4 was COVERED by prompt words and enforced by nothing.
#               (3) The credited-method list learns the ARITHMETIC verbs -- it held the
#               procedure verbs only, so "you carried the 1" fired and "You multiplied 3
#               times 2 first" did not. Referees 77 -> 78, all three conduct-class; truth
#               class unchanged at 11. No engine or route change.
#   2026-09-07  APP_BUILD -> "2026-09-07tv-the-gate-learns-who-wrote-the-symbol".
#               BUILD tv -- referee 31 (the first-use gate) stops counting the STUDENT'S
#               own words as evidence that a notation has been met. The 09-06 watch's F2
#               and the 09-07 watch's N6 are one hole: `heard` joins every message of the
#               turn, so the function-notation student's opening -- "my book has f(x) in
#               it and I don't know what that means" -- silenced the referee on the reply
#               that introduced f(x), on a [[write]] tag and inside a [[machine]] caption
#               alike. _create_verified now computes heard_tutor from the assistant
#               messages only and prose_board_conflict carries it to that referee and no
#               other. A reading the tutor gave in an earlier turn also buys silence now,
#               which nothing ever tested. No new referee (still 77), no engine or route
#               change, truth class unchanged at 11.
#   2026-09-07  APP_BUILD -> "2026-09-07tu-the-truth-trio-and-the-reviewers-list".
#               BUILD tu -- the 2026-09-07 night watch's three TRUTH-class findings,
#               and the reviewer's rulings list grown from one row to five. Jim's
#               ruling, 2026-09-07: truth items first. The 76th referee compares a
#               pie's caption with the fraction the pie actually shades (the watch's
#               HIGH: parts="6" shaded="2" captioned "one sixth"); the 77th catches a
#               listed sequence said to move TOWARD a value its own numbers move away
#               from; KNOWN_FALSEHOODS row 17 catches factoring DEFINED as pieces that
#               multiply to zero. Both new referees are truth-class, so a draft
#               carrying one is withheld rather than shipped least-bad. No engine or
#               route changed: this build is referees, a falsehood row, four reviewer
#               rulings and one critic discipline line.
#   2026-09-06  APP_BUILD -> "2026-09-06tt-probstat-units-four-to-six-to-the-shape".
#               BUILD tt -- Probstat Units 4-6 (sampling, probability, conditional)
#               rewritten to the shape on the bars, the tape, the hundred square, the
#               machine, the pie, the array, the tree and the two-way table. The
#               undercoverage ask no longer asks "how many students" (rule 42). Stamp
#               only.
#   2026-09-06  APP_BUILD -> "2026-09-06ts-the-lesson-introduces-itself".
#               BUILD ts -- Jim, back after a day: "Welcome back" and then a why beat
#               with no unit, no lesson, no name. Every scripted lesson now opens with
#               lessonscripts.lesson_intro(): course, unit and its name, lesson i of
#               n, topic -- spoken and on a board card -- before the why. Stamp only;
#               the prewarm has 360 new closure lines to render.
#   2026-09-06  APP_BUILD -> "2026-09-06tr-probstat-units-one-to-three-to-the-shape".
#               BUILD tr -- Probstat Units 1-3 (exploring data, describing
#               distributions, scatterplots) rewritten to the shape on the dot plot,
#               the histogram, the box plot, the number line, the bars, the hundred
#               square, the scatter cloud, the machine and the tape. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06tq-precalc-units-seven-to-nine-to-the-shape".
#               BUILD tq -- Precalc Units 7-9 (conics, series, limits) rewritten to the
#               shape on the circle, the conic grid, the tape, the path and the vector,
#               the machine, the bars, the array, the number line and the grapher's
#               holes and steps. Precalc is 36/36. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06tp-precalc-units-four-to-six-to-the-shape".
#               BUILD tp -- Precalc Units 4-6 (trig functions, identities, applications)
#               rewritten to the shape on the bars, the unit circle, the split flat
#               line, the wave in degrees, the hundred square, the right triangle, the
#               honest SAS triangle, the compass and the vector. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06to-precalc-units-one-to-three-to-the-shape".
#               BUILD to -- Precalc Units 1-3 (functions, polynomials, logs and
#               exponentials) rewritten to the shape on the machine, the grid, the
#               number line, the array, the area model and the bars. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06tn-algebra-two-units-seven-to-nine-to-the-shape".
#               BUILD tn -- Algebra 2 Units 7-9 (patterns, the unit circle, statistics)
#               rewritten to the shape on the bars, the number line, the staircase
#               rectangle, the machine, the unit circle, the wave, the array and the
#               pie. Algebra 2 is 36/36. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06tm-algebra-two-units-four-to-six-to-the-shape".
#               BUILD tm -- Algebra 2 Units 4-6 (division moves in, roots, decay and
#               logs) rewritten to the shape on the grid, the machine, the number line,
#               the array and the bars. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06tl-algebra-two-units-one-to-three-to-the-shape".
#               BUILD tl -- Algebra 2 Units 1-3 (absolute value and clues, the vertex,
#               roots, the test number and i, polynomials) rewritten to the shape on the
#               number line, the bars, the tape, the grid, the array and the machine.
#               Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06tk-geometry-units-seven-to-nine-to-the-shape".
#               BUILD tk -- Geometry Units 7-9 (the grid, area and volume, chance and
#               counting) rewritten to the shape on the grid, the right triangle, the
#               parallelogram with its true height, the rectangle, the cube and the box,
#               the bars, the pie, the array and the two-way table. Geometry is 36/36.
#               Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06tj-geometry-units-four-to-six-to-the-shape".
#               BUILD tj -- Geometry Units 4-6 (similar shapes, the right triangle,
#               circles) rewritten to the shape on the two triangles, the bars, the
#               rectangle of squares, the right triangle and the pie of arcs. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06ti-geometry-units-one-to-three-to-the-shape".
#               BUILD ti -- Geometry Units 1-3 (angles and the circle, the three moves,
#               triangles) rewritten to the shape on the angle, the circle, the number
#               line, the grid, the pie and the triangle. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06th-algebra-one-units-seven-to-nine-to-the-shape".
#               BUILD th -- Algebra 1 Units 7-9 (the four rooms, curves, the three
#               middles) rewritten to the shape on the area model, the grid, the tape,
#               the dotplot and the number line. Algebra 1 is 36/36. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06tg-algebra-one-units-four-to-six-to-the-shape".
#               BUILD tg -- Algebra 1 Units 4-6 (lines, two rules, powers) rewritten to
#               the shape on the grid, two lines, bars, the place-value chart and the
#               doubling bars. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06tf-algebra-one-units-one-to-three-to-the-shape".
#               BUILD tf -- Algebra 1 Units 1-3 (expressions, equations, functions)
#               rewritten to the shape on the bar, the area model, the balance, the
#               number line and the machine. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06te-prealgebra-units-seven-to-nine-to-the-shape".
#               BUILD te -- Prealgebra Units 7-9 (percent, measurement and geometry,
#               the first letters) rewritten to the shape on the tape, the hundred
#               grid, the rectangle round the triangle, the split line, the triangle
#               and the area model. Stamp only.
#   2026-09-06  APP_BUILD -> "2026-09-06td-prealgebra-units-four-to-six-to-the-shape".
#               BUILD td -- Prealgebra Units 4-6 (fractions, decimals, ratio) rewritten
#               to the shape on the tape, the fraction line, the hundred grid, the
#               place-value chart (new tenths column) and two pies. Stamp only.
#   2026-09-05  APP_BUILD -> "2026-09-05tc-prealgebra-units-one-to-three-to-the-shape".
#               BUILD tc -- Prealgebra Units 1-3 (order of operations, factors,
#               integers) rewritten to the shape on the ladder, the rectangle and
#               the number line with hops. Stamp only.
#   2026-09-05  APP_BUILD -> "2026-09-05tb-entry-unit-one-to-the-shape".
#               BUILD tb -- Entry Unit 1 rewritten to the shape (stars counted one at a
#               time; the number line for before/after and bigger). Stamp only.
#   2026-09-05  APP_BUILD -> "2026-09-05ta-the-tutor-sees-the-board".
#               BUILD ta -- Jim's flag 22:31 ("acted like there was a number line when
#               there wasn't"): the engine's intervene step now carries the ask's board
#               and tutor.script_intervention reads it (context["board"]); the rule-7
#               referee holds the reply to the picture it names. THIS FILE: stamp only
#               -- script_answer already hands the whole intervene step to
#               _script_intervene as `context`, so the board rides along unchanged.
#   2026-09-05  APP_BUILD -> "2026-09-05sz-the-times-table-is-a-pass".
#               BUILD sz -- Jim's flag 22:40 and rulings ⑥ ⑦: the times-table lesson is
#               mastered by ONE clean pass of all 81 facts, not three in a row. THIS
#               FILE: script_start draws the pass's shuffle seed (secrets) and hands it
#               to lessonscripts.start -- the one place chance enters the scripted lane;
#               the engine does the rest and no path here changed. The slip inside a
#               pass never reaches _script_intervene (the engine emits no intervene
#               step for it), so the AI-turn accounting is untouched.
#   2026-09-05  APP_BUILD -> "2026-09-05sy-basic-unit-nine-to-the-shape".
#               BUILD sy -- Basic Unit 9 (measuring) rewritten to the shape on the new
#               rectangle figure, the circle and the box. The whole Basic course -- 36
#               lessons -- is on the shape. Stamp only.
#   2026-09-05  APP_BUILD -> "2026-09-05sx-basic-unit-eight-to-the-shape".
#               BUILD sx -- Basic Unit 8 (percent) rewritten to the shape on the
#               hundredths square, the sharing picture and the tape. Stamp only.
#   2026-09-05  APP_BUILD -> "2026-09-05sw-basic-unit-seven-to-the-shape".
#               BUILD sw -- Basic Unit 7 (decimals and money) rewritten to the shape on
#               the tenths line, the new hundredths square and the place-value chart.
#   2026-09-05  APP_BUILD -> "2026-09-05sv-basic-unit-six-to-the-shape".
#               BUILD sv -- Basic Unit 6 (adding and taking away fractions) rewritten to
#               the shape on the fraction line. Stamp only.
#   2026-09-05  APP_BUILD -> "2026-09-05su-basic-unit-five-to-the-shape".
#               BUILD su -- Basic Unit 5 (fractions) rewritten to the shape on the
#               fraction line, the shared array and two pies. Stamp only.
#   2026-09-05  APP_BUILD -> "2026-09-05st-basic-unit-four-to-the-shape".
#               BUILD st -- Basic Unit 4 (factors and multiples) rewritten to the shape on
#               the array, the rectangle, the Venn and two number lines. Stamp only.
#   2026-09-05  APP_BUILD -> "2026-09-05ss-basic-unit-three-to-the-shape".
#               BUILD ss -- Basic Unit 3 (dividing) rewritten to the shape on the array
#               read the other way (sharing, left-overs) and the area model backwards.
#               Stamp only in this file.
#   2026-09-05  APP_BUILD -> "2026-09-05sr-basic-unit-two-to-the-shape".
#               BUILD sr -- Basic Unit 2 (multiplying) rewritten to the shape on the
#               new [[array]] figure, the area model and the place-value chart. Stamp
#               only in this file.
#   2026-09-05  APP_BUILD -> "2026-09-05sq-basic-unit-one-to-the-shape".
#               BUILD sq -- Basic Unit 1 rewritten to the seven-beat shape (Jim's ruling
#               after running sp: every lesson, taught this way, with a graphic). Stamp
#               only in this file; the work is in lessonscripts.py, board.js (borrows=),
#               math-figures.js ([[placevalue]]), tags.py, tutor.py's draw regex, the
#               three pages' figure lists and script-board.js.
#   2026-09-05  APP_BUILD -> "2026-09-05sp-the-lesson-learns-to-teach".
#               BUILD sp -- THE LESSON LEARNS TO TEACH (Jim: "are we really in the
#               business here of teaching, or are we just trying to create a teaching
#               app?"). lessonscripts grows the seven-beat shape as optional lesson
#               fields and a REASON question (beat six, "Say it"): an ask with
#               reason=True and TEXT options. THIS FILE: _script_clean ships `reason`
#               on every ask, and /api/script/answer grades a reason tap BY ITS LABEL
#               in code before read_answer can scan it for a digit -- exact option
#               match answers, "not sure" gets LINE_UNSURE, anything else is unheard.
#               No model on that path. The rounding-to-tens lesson is the prototype.
#   2026-09-04  APP_BUILD -> "2026-09-04so-the-mark-goes-away-and-the-voice-is-counted".
#               BUILD so -- Jim's live flags, the page-and-eyes cluster. Pages: the
#               pencil's [[ink]] marks clear at the start of every turn (his "black
#               line ... still there"); the scripted answer door shows the thinking
#               state (a wrong answer's model intervention "looked frozen"). Eyes:
#               voice.js files a voice_fallback event through client-log.js's new
#               MyTutorReport, and /api/client-error files whitelisted named kinds;
#               new _closure_render_status() counts closure lines not yet in the TTS
#               cache and lends the number to the night watch, which prints it beside
#               "run the prewarm" -- the prewarm is manual, and Jim heard the browser
#               voice on two closure lines that were simply not rendered yet.
#   2026-09-04  APP_BUILD -> "2026-09-04sn-the-warm-choice". BUILD sn -- Jim's ruling ③:
#               a still-learning lesson end offers the student a CHOICE -- go on to the
#               next lesson, or review this one -- instead of handing the seam to the
#               live tutor. This supersedes sl's "still learning does not advance",
#               which Jim softened the same day. Server half here: _script_clean now
#               puts next_id on EVERY end step that has a next lesson, and `choice`:
#               True on a still-learning one. lessonscripts owns the spoken line;
#               session.html renders the two buttons and starts the chosen lesson
#               inside the scripted lane (review = the same lesson from the start --
#               ruling #4, resume at a lesson boundary). No model call either way.
#               A course boundary still falls through to the live tutor until ④.
#   2026-09-04  APP_BUILD -> "2026-09-04sm-the-board-answers-the-question-asked". BUILD
#               sm is tutor.py ONLY; this file changes for the STAMP. Jim's ruling ①:
#               board/words disagreement is truth-class -- boardcount joins the floor's
#               truth list and the SEVENTY-FIFTH referee (exprswap, qx's probe promoted)
#               catches the 09-04 HIGH: a board working 2 + 3 x 4 = 14 while the voice
#               works 3 + 2 x 4 = 11. Referees 74 -> 75. No behaviour here changes.
#   2026-09-04  BUILD sl -- THE SEAM READS THE COURSE ORDER. Jim's ruling: a MASTERED
#               lesson advances on its own (no student choice); a "still learning" end
#               does NOT advance. New _next_lesson_id() reads lessonscripts.COURSE_ORDER --
#               the authored 360-lesson sequence nothing at this seam had ever read -- and
#               _script_clean now puts next_id/next_topic on a MASTERED `end` step. That is
#               the half the page needs to advance INSIDE the scripted lane instead of
#               asking the live tutor to guess what comes next (the 09-01 "one-less reads
#               as subtraction" bug: rj made the model announce its guess, this removes the
#               guess). SERVER ONLY and purely additive -- next_id is "" on a non-mastered
#               end and at a course boundary, and until session.html reads it NOTHING
#               changes for a child. The page change is Jim's to approve.
#               (later, 2026-09-04) APPROVED AND WRITTEN: session.html's seam now
#               starts next_id inside the scripted lane. APP_BUILD ->
#               "2026-09-04sl-the-seam-reads-the-course-order" (the sk default-10
#               change in nightwatch.py rides under this stamp too; it carried none).
#               Jim's same-day rulings for what this build deliberately leaves to
#               the live tutor: a STILL-LEARNING end gets a warm choice (go on /
#               review) and a COURSE END gets a celebration and a certificate --
#               both their own builds. PART 3ih pins the server half both ways and
#               the page half's two edits.
#   2026-09-03  APP_BUILD -> "2026-09-03sj-the-floor". BUILD sj is tutor.py +
#               nightwatch.py; this file changes for the STAMP. THE FLOOR: a draft
#               every attempt of which carried a TRUTH-class finding (false board
#               math, a false law, a named falsehood, a choice list with no right
#               answer) no longer ships -- the child gets the fallback line, a `floor`
#               event names the referee, the lesson continues next turn. Conduct
#               findings ship least-bad exactly as px designed. The 09-03 watch's 148
#               pass-throughs/week can now only fall. Referees stay 74. PART 3ig.
#   2026-09-03  APP_BUILD -> "2026-09-03si-the-law-wore-a-different-costume". BUILD
#               si is tutor.py ONLY -- this file changes for the STAMP. Both rule-61
#               findings from the 09-03 night watch, neither needing a new referee:
#               the order-of-operations law found TWICE fourteen days apart in the
#               same lesson (the 37th referee was NOT dead -- measured -- it was one
#               missing alternation, "no matter WHICH order"), and the HIGH, "two
#               solutions because it's a squared equation", as KNOWN_FALSEHOODS row
#               16. Referees stay 74; falsehoods 15 -> 16. No behaviour in this file
#               changes. PART 3if.
#   2026-09-03  APP_BUILD -> "2026-09-03sh-the-watch-says-what-it-was-told-to-do".
#               BUILD sh is nightwatch.py ONLY -- this file changes for the STAMP, so
#               /health can prove the report improvements are the ones running. Four
#               holes in the morning report, each named by a triage that then had to
#               give up on it: the 10-vs-12 question (three watches running; the report
#               printed only what HAPPENED, never what it was TOLD to do, so a shrunken
#               rotation, skipped slots and a changed constant were indistinguishable);
#               507 referee fires with no names; crash reasons with no clock, so a ghost
#               and a live regression read alike; and a reviewer never told about Jim's
#               09-01 rule-42 ruling, which had it re-confirming a settled shape. No
#               behaviour in this file changes. PART 3ie.
#   2026-09-02  APP_BUILD -> "2026-09-02sg-the-sweep-stays-out-of-the-code". BUILD
#               sg: the sd child->student sweep had rewritten CODE identifiers --
#               feed.children -> feed.students froze Jim's probstat session at the
#               opener (crash in wipeBoard, swallowed as an unhandled rejection).
#               13 identifiers restored across 10 static pages; scrNext gains a
#               crash net (a broken beat skips forward instead of freezing); PART
#               3id pins it all. No main.py logic change -- the bump is the stamp.
#   2026-09-02  APP_BUILD -> "2026-09-02sf-spoken-math-is-written-math". BUILD sf:
#               THE SEVENTY-FOURTH REFEREE (tutor.py's spoken_math_unwritten_
#               conflict) -- Jim's live rule, verbatim: "if we can write our a
#               problem... we do." A spoken chain of computations over an empty
#               board is sent back demanding [[step]] lines AND a continue-check
#               (his "froze" screenshot was a dead-end turn -- "Nothing to do,
#               page alive"). No main.py logic change: the bump is the build
#               stamp, tile 73 -> 74 lives in methodology.html, the PART is 3ic.
#   2026-09-02  APP_BUILD -> "2026-09-02se-five-flags-from-jims-queue". BUILD se,
#               Jim's five live flags, one build: ① the entry count-on line drops
#               its "trap" sentence (lessonscripts); ② rounding is taught
#               LINE-FIRST (pedagogy -- his flagged reply, canonized); ③ rule 19(d)
#               forbids handing over past an un-narrated example (prompts);
#               ④ "8,516" is spoken in WORDS (speech-text.js -- comma numbers only,
#               so hundreds of fine cached clips keep their keys) and rule 19(f)
#               keeps the voice from reading a read-it-yourself number at all;
#               ⑤ THE SEVENTY-THIRD REFEREE, board_flood_conflict (tutor.py):
#               seven+ drawing tags in one reply = several beats wearing one
#               turn's clothes -- split, never shrink the font. NO CODE IN THIS
#               FILE CHANGED -- stamp only. PART 3ib.
#   2026-09-02  APP_BUILD -> "2026-09-02sd-the-student-is-a-student". BUILD sd,
#               Jim's wording ruling: the student is "the student / your student",
#               never "the child" -- 344 visible occurrences across 22 pages +
#               llms.txt + THIS file's demo voice lines (byte-identical twin) and
#               its parent-visible email/API strings. Scope his call: ALL BUT LEGAL
#               (privacy/terms keep the word the law is written in); historical
#               header notes stay verbatim. PART 3ia holds the whole boundary.
#   2026-09-02  APP_BUILD -> "2026-09-02sc-the-demo-holds-still-and-shows-its-boards".
#               BUILD sc, four demo rulings from Jim, this day: ① no page scrolling
#               in the classroom (a scrolled page moves the target out from under the
#               pencil); ② he says "board", never "whiteboard" (two DEMO_VOICE_LINES
#               reworded IDENTICALLY in both lists -- clips regenerate from text on
#               first play); ③ a new tour stop points at the board-choice chip and
#               flips white -> back to dark (one line APPENDED to both lists, 253 ->
#               254); ④ the Abrabot end-stops are gone from all four dashboard tours
#               (he is introduced once on the main tour and never brought back; his
#               standalone button stays). Plus the demo's mouth now reads the REAL
#               audio (the page declares the analyser globals cadabra.js has read
#               since rt -- it never had them, so the mouth ran on the synthetic
#               flap). Voice-list edits in THIS file are the byte-identical twin of
#               demo.html's, per the standing pin. PART 3hz holds it.
#   2026-09-02  APP_BUILD -> "2026-09-02sb-the-practice-goal". BUILD sb, Jim's
#               2026-09-02 design: a parent (/family) or teacher (/teacher) may set
#               a DAILY practice goal -- minutes in the adult's hands, a problem
#               ring in the child's, only ever skills the record has earned. NEW:
#               POST /api/parent/student-goal (parent door, _own_student gate) ·
#               POST /api/class/{code}/goal (teacher door, _own_class +
#               _resolve_member, same validation via ONE _set_goal_checked) · GET
#               /api/goal/{code} (the child's read: target/done/kind + a
#               newest-mastered suggestion for kind=latest; the child never sees
#               who set it -- Jim: never adversarial). /api/mark responses carry
#               {goal:{target,done}} when a goal is set so the ring moves on the
#               answer that earned it; /api/parent/overview and the class roster/
#               summary rows carry the goal for the adult's view. PART 3hy.
#   2026-09-02  APP_BUILD -> "2026-09-02sa-the-question-mark-is-a-blank-said-so".
#               BUILD sa, the 09-02 watch's finding G (rule 14) and its LAST
#               buildable item: a ? hugging a fraction slash (?/10) is first-use
#               notation and must be read aloud; the bare "= ?" the canon uses
#               never matches. A registry row on referee 31 -- count stays 72.
#               PART 3hx pins it. NO CODE IN THIS FILE CHANGED -- stamp only.
#   2026-09-02  APP_BUILD -> "2026-09-02rz-a-variables-letter-keeps-its-case". BUILD
#               rz, the 09-02 watch's finding E (rule 28): the seventy-second referee
#               -- a variable written X on the board while the words say x is two
#               names for one thing; clean case splits fire, a/e/i/o never judged.
#               prompts.py rule 28 carries the case clause; methodology's tiles moved
#               (72 reply checks, battery count). PART 3hw pins it. NO CODE IN THIS
#               FILE CHANGED -- stamp only, per the stamp law below.
#   2026-09-02  APP_BUILD -> "2026-09-02ry-the-accepted-offer-is-honored-and-the-
#               verdict-is-proven". BUILDS rx + ry, the 09-02 watch's T3 findings
#               C and D, delivered together: referee 70 gains the acceptance-turn
#               branch (offer to show + "yes!" + nothing drawn -> fire), the
#               quiz-verdict referee reads board numbering too, and -- Jim's
#               ruling, "Retry + code floor" -- repair_missing_verdict at the
#               shipping door speaks a PROVEN "Correct." + [[mark]] when the
#               model skipped the verdict (never "Not quite", never unproven).
#               PARTs 3hu + 3hv pin it. NO CODE IN THIS FILE CHANGED -- stamp
#               only, per the stamp law below.
#   2026-09-02  APP_BUILD -> "2026-09-02rw-the-hole-is-drawn-open-and-the-op-tells-
#               the-truth". BUILDS rv + rw, the 09-02 watch's two HIGHs, delivered
#               together: mathcheck gains check_graph_claims (a filled point where
#               the curve provably has no value -> "wrong", nudging hole=) and
#               check_step_ops (a numeric both-sides op label is APPLIED to the
#               previous step and compared per side -- the lying "+ 9 to both
#               sides" fires), and tutor.py gains KNOWN_FALSEHOODS row 15 ("turn
#               ANY quadratic into a perfect square"). PARTs 3hs + 3ht pin all of
#               it. NO CODE IN THIS FILE CHANGED -- stamp only, per the stamp law
#               below.
#   2026-09-02  APP_BUILD -> "2026-09-02ru-a-comma-makes-a-tuple-not-an-expression".
#               BUILD ru -- the 09-02 watch's newest crash: mathcheck died on any
#               comma-bearing board text (parse_expr returns a plain tuple; see
#               mathcheck.py's ru note) and failed open, unjudging the reply. Fixed
#               at mathcheck._parse, PART 3hr pins it. NO CODE IN THIS FILE CHANGED.
#               ⚠️ STAMP NOTE: build rt (cadabra.js lip-sync, 2026-09-02) shipped
#               WITHOUT bumping this stamp -- /health said "rs" while rt was live.
#               This bump moves the stamp past rt; the law stands: EVERY build that
#               touches ANY shipped file bumps APP_BUILD, one-file pencil builds
#               included -- the stamp exists so Jim never has to wonder.
#   2026-09-02  APP_BUILD -> "2026-09-02rs-the-demo-three-things-jim-saw". BUILD rs --
#               ONE line APPENDED to DEMO_VOICE_LINES (252 -> 253), byte-identical to
#               demo.html's VOICE_LINES: the miniature-dashboard tour line. The old
#               "here is a corner of it" line stays (append-only). Nothing else.
#   2026-09-02  APP_BUILD -> "2026-09-02rr-the-pencil-has-feelings-about-your-work".
#               BUILD rr -- Jim's behaviour list for the pencil, all front-end plus
#               the tag grammar: [[ink circle=|underline=|bang=]] registered in
#               tags.py and taught in prompts.py (one paragraph x9); cadabra.js
#               finds the word by text and marks it, glances at new board work,
#               comforts a stuck child, throws a party at milestones, waves, and
#               stops talking when the voice does (voice.js announces mt:silent);
#               the pages ring the new doorbells; the demo loses the orb circle.
#               NOTHING in this file changed but the stamp.
#   2026-09-01  APP_BUILD -> "2026-09-01rn-two-holes-closed-one-ruling-taken". BUILD
#               rn -- the watch's cluster E one-liners: rule 39's "See how that
#               works?" and rule 15's spoken-only function rule CLOSED (two
#               widenings in tutor.py, referees stay 71). Rule 42's "trips a lot of
#               people up": put to Jim against pq's pinned people/folks cut -- his
#               ruling: people-forms stay legal; dispositioned allowed-by-ruling.
#               Rule 44's ordering half + cluster B's rule-4 cousin deferred with
#               paper trails. NO CODE IN THIS FILE CHANGED.
#   2026-09-01  APP_BUILD -> "2026-09-01rm-credit-only-what-you-saw". BUILD rm -- the
#               09-01 watch's cluster C (rules 43/47/62): invented praise ("lined
#               those up perfectly", no work shown) and unverifiable skill-mastery
#               claims ("we've already got solid <skill>"). Referee 32's gate widened
#               in tutor.py (count stays 71); the "two in a row unaided" finding
#               deferred with reasons (needs turn-structured history).
#               NO CODE IN THIS FILE CHANGED.
#   2026-09-01  APP_BUILD -> "2026-09-01rl-the-first-use-list-learns-lim-and-squared".
#               BUILD rl -- the 09-01 watch's cluster B (rule 48 x2): lim written
#               before "the limit as x approaches" was said, and a²+b²=c² before
#               "a squared" was said. Referee 31's gate WIDENED (exponent pattern
#               gains real superscripts; new limit entry) and notation.py gains the
#               limit registry row -- see tutor.py/notation.py rl notes.
#               NO CODE IN THIS FILE CHANGED.
#   2026-09-01  APP_BUILD -> "2026-09-01rk-the-course-remembers-which-lessons-are-done".
#               BUILD rk -- Jim: "I keep logging in as student zero zero zero zero, and
#               it keeps starting over from the beginning." Root cause: no per-LESSON
#               record existed (topic_progress is per UNIT; topic quizzes only fire on
#               pilot.html) and scriptPick read payload fields that do not exist
#               (best_pct/topic_name vs the real passed/name), so its done-set was
#               always empty and pool[0] repeated forever. THIS FILE: _script_finish
#               now writes store.record_script_done(code, course, lesson id, mastered)
#               beside the unit record, and /api/session's progress ships
#               "script_done" (the mastered lesson ids) for the picker to resume from.
#               The picker fix itself is session.html's.
#   2026-09-01  APP_BUILD -> "2026-09-01rj-the-orb-retires-and-the-seam-is-announced".
#               BUILD rj -- Jim watched ri live and ruled three things: (1) THE SEAM IS
#               ANNOUNCED ("acted as if we had been working on subtraction. This is
#               strange"): _SCRIPT_DONE_NOTES remembers the finished lesson at
#               _script_finish, and the chat route turns __script_done__ /
#               __script_done_mastered__ into a turn note making the live tutor NAME
#               the new topic first (the page speaks lessonscripts.LINE_NEW_TOPIC
#               before handing off). (2) The pencil is 30% larger with a slight float
#               (menu + cadabra.js). (3) The ORB RETIRES from session/topic/practice
#               ("he is to be gone everywhere"; demos later) -- the pencil layer is now
#               wired on all three student pages.
#   2026-09-01  APP_BUILD -> "2026-09-01ri-three-in-a-row-means-move-on". BUILD ri --
#               Jim's live catch: "I gave three correct answers and it gave me a 4th
#               question." His ruling: the promised three-in-a-row IS the advance gate.
#               lessonscripts.py: gate is streak >= ADVANCE_STREAK alone, MIN_PROBLEMS
#               removed. Also the pencil now ENTERS ONLY at lesson.start (the menu ran
#               a joke + tour over the real recorded opening) and every menu target
#               resolves to a real data-cad name. NO CODE IN THIS FILE CHANGED.
#   2026-09-01  APP_BUILD -> "2026-09-01rh-the-pencil-wakes-up". BUILD rh -- Jim: "activate
#               the pencil icon as Mr Cadabra." session.html wired to the Cadabra companion
#               layer (twelve additive edits, re-applied onto the current page) and the
#               switch created: static/cadabra-script.json (delete it to turn him off).
#               NO CODE IN THIS FILE CHANGED.
#   2026-09-01  APP_BUILD -> "2026-09-01rg-the-words-point-where-the-column-put-it".
#               BUILD rg -- the watch's rule-63 finding: "the 6 under the 5" over a
#               column that draws it above. REFEREE 71, column_words_conflict
#               (tutor.py), computed from the tag's own term order. NO CODE IN THIS
#               FILE CHANGED.
#   2026-09-01  APP_BUILD -> "2026-09-01rf-the-asked-for-picture-is-drawn-now". BUILD rf
#               -- the watch's other HIGH (geometry, rule 65): the requested drawing
#               postponed into an offer. REFEREE 70, postponed_show_conflict (tutor.py):
#               asked-to-see + the final ask offers to show/draw; offers of MORE stay
#               silent. NO CODE IN THIS FILE CHANGED.
#   2026-09-01  APP_BUILD -> "2026-09-01re-the-factors-are-checked-by-expanding-them".
#               BUILD re -- the watch's HIGH: a spoken factor pair contradicting the
#               board's quadratic. KNOWN_FALSEHOODS row 14 + REFEREE 69 (tutor.py,
#               factor_claim_conflict -- expand the pair, compare to the reply's one
#               quadratic, computed never guessed). NO CODE IN THIS FILE CHANGED.
#
# HOW IT RUNS:
#   Locally:  uvicorn main:app --reload
#   Render:   uvicorn main:app --host 0.0.0.0 --port $PORT   (see render.yaml)
#
# IMPORTANT NOTE ABOUT MEMORY ON RENDER:
#   sessions.json + placements.json (under DATA_DIR) let the tutor remember each
#   student and their placement. On Render's FREE web service the disk is EPHEMERAL
#   -- it resets on every redeploy AND whenever the service sleeps (~15 min idle) --
#   so students look brand new each time. To make memory DURABLE, attach a Render
#   PERSISTENT DISK (needs a paid Starter instance), mount it at e.g. /var/data, and
#   set env var DATA_DIR=/var/data. The code already reads DATA_DIR, so no code
#   change is needed once the disk is attached.
# =============================================================================

# (vb) copy.deepcopy is used by _script_warm's speculative engine step -- the
# look-ahead must never advance the real lesson state. Imported HERE with the
# rest of the standard library, not beside its one caller (build kq's law).
import copy
import gzip
import hashlib
import hmac
import json
import os
import re
import secrets
# build kq: tempfile is imported HERE, not 3,000 lines down. _prewarm_recover_record()
# runs at import time -- it is what turns a job killed by a redeploy into a visible
# "interrupted" -- and it writes the record back. A late import would have made that
# one path raise NameError, which is the one path that must never fail quietly.
import tempfile
import threading

# build go (2026-08-16) -- THE GOVERNOR. Imported defensively: nightwatch is offline
# tooling, and a deploy where it is missing or broken must still teach children.
try:
    import nightwatch
except Exception as _nw_exc:  # noqa: BLE001
    nightwatch = None
    print(f"[nightwatch] module unavailable, the night watch is off: {_nw_exc}")
import time
import uuid
from collections import defaultdict, deque
from pathlib import Path

import httpx
from fastapi import Depends, FastAPI, File, Header, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import time as _time
import tutor
import lessonscripts   # build jt: the scripted-first pilot engine (pure; see its header)
import store   # durable DB storage; dormant unless DATABASE_URL is set (see store.py)
import curriculum   # 9 units + classify_unit() for real per-topic tracking
import tags     # build hm: the tag grammar's one source (hard import, loud at boot)
import speechmap  # (vc) GENERATED from static/speech-text.js -- see _spoken() below.
                  # A hard import on purpose: without it every clip goes back to
                  # being filed under a label no page ever asks for, silently.
import library  # 2026-08-07: the "Look it up" reference library (seeds + generate-once)
try:
    # 2026-08-10 (build ck): the misconception catalogue, used to recognise a known
    # error pattern in what the student JUST said and hand the tutor the fix for it.
    import misconceptions
except Exception as _exc:  # noqa: BLE001
    misconceptions = None
    print(f"[main] misconceptions.py unavailable ({_exc}) -- diagnosis note disabled")
try:
    # 2026-08-09 (build ce): used ONLY to validate a [[learned term="..."]] tag against
    # the real script names before we write it down. Defensive, exactly like tutor.py's
    # import: a missing or broken foundations.py must never keep the classroom down.
    import foundations
except Exception as _exc:  # noqa: BLE001
    foundations = None
    print(f"[main] foundations.py unavailable ({_exc}) -- foundation memory disabled")

try:
    import sprints
except Exception as _exc:  # noqa: BLE001
    sprints = None
    print(f"[main] sprints.py unavailable ({_exc}) -- fluency sprints disabled")

# Bring up the database backend if DATABASE_URL is configured. If it isn't (or the
# DB can't be reached), store.enabled() stays False and we use the JSON-file storage
# below, exactly as before -- so the current app is unaffected until a DB is added.
store.init()
# BUILD hv (2026-08-18, Phase 5 -- review Class E): a CONFIGURED database that
# cannot be reached is a LOUD event now, not a silent fork onto un-backed-up
# files. The teaching lanes refuse to write stranded state (see _degraded_reply)
# unless ALLOW_FILE_FALLBACK says this is a dev box, and Jim's inbox hears about
# it (throttled) the moment the app boots degraded.
ALLOW_FILE_FALLBACK = (os.environ.get("ALLOW_FILE_FALLBACK", "").strip().lower()
                       in ("1", "true", "yes", "on"))

# ---- (ud) THE PUBLIC SIGN-IN PAGE STOPS TALKING LIKE A DEV BOX -----------------
# The persona codes (1234 Alex ... 0000 Demo) were printed on /login for every
# visitor. They are a dev-box line now: SHOW_TEST_CODES=1 shows them; unset, a dev
# box (ALLOW_FILE_FALLBACK) shows them and Render does not. /api/site-flags is the
# one public door the page reads it through -- booleans only, never a secret.
SHOW_TEST_CODES = ((os.environ.get("SHOW_TEST_CODES", "").strip().lower()
                    in ("1", "true", "yes", "on"))
                   if os.environ.get("SHOW_TEST_CODES", "").strip() else ALLOW_FILE_FALLBACK)

# ---- (ud) THE OWNER'S TOOLS ARE THE OWNER'S -------------------------------------
# Four pages and a folder under static/ are Jim's workbenches, not the app: the
# scripted picker (pilot.html, also routed at /pilot), Mr. Cadabra's bench
# (cadabra-lab.html), the demo layout concept (demolab.html), the retired avatar
# stub (avatar-lab.html) and static/mockup/. StaticFiles served every one of them to
# anyone who typed the address. Now they answer 404 to the public -- exactly what a
# missing file answers, so their existence is not advertised -- and open only for
# the owner: an X-Admin-Key header (scripts), or the HttpOnly mt_owner cookie that
# POST /api/owner/unlock sets once the general admin key verifies (admin.html calls
# it as the dashboard unlocks). The cookie is an HMAC of the admin key, so rotating
# FORUM_MOD_KEY in Render logs every browser out of the tools at once, and an UNSET
# key is fail-closed: nothing is the owner. static/shots/ stays public on purpose --
# the marketing pages show those screenshots.
_OWNER_STATIC_FILES = frozenset({"pilot.html", "demolab.html", "cadabra-lab.html",
                                 "avatar-lab.html"})
_OWNER_STATIC_PREFIXES = ("mockup/",)
_OWNER_COOKIE = "mt_owner"
_OWNER_TOOLS = ("/pilot", "/static/cadabra-lab.html", "/static/demolab.html")


def _owner_token() -> str:
    """The cookie value that proves the owner: HMAC(admin key, a fixed label). Empty
    when the admin key is unset, and an empty token never matches anything."""
    admin = os.environ.get("FORUM_MOD_KEY", "").strip()
    if not admin:
        return ""
    return hmac.new(admin.encode("utf-8"), b"mr-cadabra-owner-tools",
                    hashlib.sha256).hexdigest()


def _is_owner(request: Request) -> bool:
    """True for the admin key in the X-Admin-Key header or the owner cookie; constant-
    time compares; False whenever FORUM_MOD_KEY is unset (fail-closed)."""
    admin = os.environ.get("FORUM_MOD_KEY", "").strip()
    token = _owner_token()
    if not admin or not token:
        return False
    header = (request.headers.get("x-admin-key") or "").strip()
    if header and hmac.compare_digest(header, admin):
        return True
    cookie = (request.cookies.get(_OWNER_COOKIE) or "").strip()
    return bool(cookie) and hmac.compare_digest(cookie, token)


def _owner_static_path(path: str) -> bool:
    """Is this static path one of the owner's tools? `path` is the part after /static/."""
    p = (path or "").replace("\\", "/").lstrip("/")
    return p in _OWNER_STATIC_FILES or p.startswith(_OWNER_STATIC_PREFIXES)


class _OwnerGatedStatic(StaticFiles):
    """StaticFiles that answers 404 for the owner's tools unless the request is the
    owner's. Everything else is served exactly as before."""

    async def get_response(self, path: str, scope):
        if _owner_static_path(path) and not _is_owner(Request(scope)):
            raise HTTPException(status_code=404, detail="Not Found")
        return await super().get_response(path, scope)
if store.degraded():
    print("[store] ⚠️  DEGRADED: DATABASE_URL is set but the database is unreachable. "
          + ("ALLOW_FILE_FALLBACK is on (dev): file mode allowed." if ALLOW_FILE_FALLBACK
             else "Teaching lanes will answer with the maintenance message until the "
                  "DB returns (set ALLOW_FILE_FALLBACK=1 only on a dev box)."))

# ---- ElevenLabs voice config (all optional; empty key -> browser voice) -----
# Set these in Render (NOT in code). If ELEVENLABS_API_KEY is missing, the app
# still talks using the browser's built-in voice.
ELEVEN_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
# Default voice = Jim's chosen ElevenLabs voice. Override with any other voice_id
# from your ElevenLabs Voice Library via the ELEVENLABS_VOICE_ID env var.
ELEVEN_VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", "sB7vwSCyX0tQmU24cW2C")
# eleven_flash_v2_5 = low latency (best for live conversation); override with
# ELEVENLABS_MODEL="eleven_multilingual_v2" for higher quality at more latency.
ELEVEN_MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_flash_v2_5")
# BUILD kf: THE SCRIPTED LANE'S OWN MODEL. Flash exists to keep a LIVE conversation
# responsive. Scripted lesson audio is pre-rendered once and replayed from cache, so
# latency there is worth nothing and fidelity is worth everything -- ElevenLabs prices
# Flash at half precisely because it trades one for the other, and names Multilingual
# v2 as the narration model. DEFAULT EMPTY = "same as ELEVEN_MODEL", so this changes
# nothing until it is set in Render -> Environment.
# ⚠️ SETTING THIS CHANGES THE CACHE KEY of every scripted line: they all become misses
# and re-render at the new model's price. Run script-prewarm after changing it, and
# test on ONE lesson first (script-prewarm with lesson=... force=true).
SCRIPT_TTS_MODEL = os.environ.get("SCRIPT_TTS_MODEL", "").strip()
# Speech-to-text model (ElevenLabs "Scribe"). Used by /api/transcribe.
ELEVEN_STT_MODEL = os.environ.get("ELEVENLABS_STT_MODEL", "scribe_v1")

# ---- Paths -----------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
# DATA_DIR holds the tutor's MEMORY (each student's conversation + placement).
# It defaults to a "data" folder next to the code, but can be pointed at a Render
# PERSISTENT DISK by setting the DATA_DIR env var (e.g. DATA_DIR=/var/data) so that
# memory SURVIVES redeploys and restarts. On an ephemeral (free-plan) disk this
# folder is wiped on every deploy and whenever the service sleeps -- which is why,
# without a persistent disk, students appear brand new each time.
DATA_DIR = Path(os.environ.get("DATA_DIR", str(BASE_DIR / "data")))
STUDENTS_FILE = BASE_DIR / "students.json"
SESSIONS_FILE = DATA_DIR / "sessions.json"
PLACEMENTS_FILE = DATA_DIR / "placements.json"  # results of Mr. Cadabra's Challenge

DATA_DIR.mkdir(exist_ok=True)  # make sure the memory folder exists

# A simple lock so two overlapping requests never corrupt the sessions file.
_sessions_lock = threading.Lock()


# ---- Loading the hardcoded students ----------------------------------------
def load_students() -> dict:
    """Read students.json and return the {code: student} mapping."""
    with open(STUDENTS_FILE, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("students", {})


STUDENTS = load_students()


# ---- Session memory (per student code) -------------------------------------
def _read_all_sessions() -> dict:
    if not SESSIONS_FILE.exists():
        return {}
    try:
        with open(SESSIONS_FILE, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        # If the file is missing or somehow corrupted, start fresh rather than
        # crash. We do no harm to a running session over a bad memory file.
        return {}


def _write_all_sessions(all_sessions: dict) -> None:
    tmp = SESSIONS_FILE.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(all_sessions, fh, ensure_ascii=False, indent=2)
    tmp.replace(SESSIONS_FILE)  # atomic swap so the file is never half-written


def _ck(code: str, course: str = "algebra1") -> str:
    """File-storage key (only used when the DB is off). Algebra I stays under the bare code
    so existing JSON files keep working; other courses are namespaced as 'code::course'."""
    return code if (course or "algebra1") == "algebra1" else f"{code}::{course}"


def get_session(code: str, course: str = "algebra1") -> dict:
    """Return this student's saved session for a course, creating an empty one if needed."""
    if store.enabled():
        return store.get_session(code, course)
    all_sessions = _read_all_sessions()
    return all_sessions.get(_ck(code, course), {"history": []})


# THE STORED TRANSCRIPT IS BOUNDED (2026-08-10, build cn).
# Jim: "I don't want to build in something that's going to degrade over time where the
# errors are gonna start to add up... because we're not discarding things that we should
# discard." This was that, and it was the biggest one in the app.
# Every chat turn LOADED the entire conversation, parsed it, appended two messages,
# re-serialised it and wrote the whole thing back. The tutor never sees more than the
# last MAX_HISTORY_MESSAGES (30) -- _trim_history throws the rest away immediately -- so
# a student one year in was moving several megabytes of JSON per turn to use 30 messages
# of it. At 10,000 students that is roughly 48 GB of transcript and a turn that gets
# slower every single week.
# We keep a generous margin over what the model reads (60 stored vs 30 sent) so nothing
# the tutor could want is ever missing, and we keep the OLDEST messages when trimming
# is impossible -- no. We keep the NEWEST, which is what a conversation needs.
# It also happens to be the right privacy posture: this is a child's conversation, we
# already delete their audio on the spot, and retaining a transcript forever is a
# liability rather than an asset. Progress, mastery, quizzes, hours and awards all live
# in their own tables and are untouched by this.
MAX_STORED_MESSAGES = 60

# SECURITY (build ec, 2026-08-12 -- finding F5): the largest audio upload /api/transcribe
# will pull into memory. A few seconds of student speech is well under 1 MB; 12 MB is a
# roomy ceiling for a long answer while closing the unbounded-read memory/cost hole.
# Env-tunable (MAX_AUDIO_BYTES) without a code change.
try:
    MAX_AUDIO_BYTES = int(os.environ.get("MAX_AUDIO_BYTES", str(12 * 1024 * 1024)) or (12 * 1024 * 1024))
except (TypeError, ValueError):
    MAX_AUDIO_BYTES = 12 * 1024 * 1024


def _bounded_history(session: dict) -> dict:
    """Return `session` with its transcript capped. Never raises."""
    try:
        h = session.get("history")
        if isinstance(h, list) and len(h) > MAX_STORED_MESSAGES:
            session = dict(session)
            session["history"] = h[-MAX_STORED_MESSAGES:]
    except Exception as exc:  # noqa: BLE001
        print(f"[session] history trim skipped: {exc}")
    return session


def mutate_history(code: str, course: str, fn) -> None:
    """build hk: THE ONLY WAY THE CHAT PATH WRITES HISTORY. `fn(history) -> history`
    is applied atomically (store.update_history: one transaction, row-locked on
    Postgres) so two overlapping turns can no longer erase each other -- the
    lost-update race whose window was the model's multi-second latency. The file
    fallback does its read-transform-write under _sessions_lock, which makes it
    equally race-free in the single-process deploy that fallback exists for.
    save_session below remains for WHOLE-session writes (resets, imports); new
    chat-path code must use this instead."""
    if store.enabled():
        store.update_history(code, course, fn, cap=MAX_STORED_MESSAGES)
        return
    with _sessions_lock:
        all_sessions = _read_all_sessions()
        sess = all_sessions.get(_ck(code, course), {"history": []})
        sess = dict(sess)
        sess["history"] = list(fn(list(sess.get("history") or [])) or [])
        all_sessions[_ck(code, course)] = _bounded_history(sess)
        _write_all_sessions(all_sessions)


def save_session(code: str, session: dict, course: str = "algebra1") -> None:
    session = _bounded_history(session)
    if store.enabled():
        store.save_session(code, session, course)
        return
    with _sessions_lock:
        all_sessions = _read_all_sessions()
        all_sessions[_ck(code, course)] = session
        _write_all_sessions(all_sessions)


# ---- Placement results (from Mr. Cadabra's Challenge) ----------------------
def read_placement(code: str, course: str = "algebra1") -> dict:
    """Return this student's saved placement result for a course, or {} if none."""
    if store.enabled():
        return store.read_placement(code, course)
    if not PLACEMENTS_FILE.exists():
        return {}
    try:
        with open(PLACEMENTS_FILE, "r", encoding="utf-8") as fh:
            return json.load(fh).get(_ck(code, course), {})
    except (json.JSONDecodeError, OSError):
        return {}


def _lessons_by_unit(code: str, course: str) -> dict:
    """(ue) {unit: {"done": n, "total": m}} for a course: `total` counts the authored
    lessons in each unit, `done` the ones this student has finished (script_done,
    a lesson finished twice counts once). Never raises; an unreadable store gives
    every unit done=0 so the page shows honest zeros, not a missing card."""
    out = {}
    try:
        for les in lessonscripts.LESSONS:
            if les.get("course") != course:
                continue
            u = out.setdefault(int(les.get("unit") or 0), {"done": 0, "total": 0})
            u["total"] += 1
    except Exception as exc:  # noqa: BLE001
        print(f"[lessons] course walk failed: {exc}")
    if not store.enabled():
        return out
    try:
        for r in store.get_script_done(code, course) or []:
            les = lessonscripts.LESSON_BY_ID.get(r.get("lesson_id") or "") or {}
            u = out.get(int(les.get("unit") or 0))
            if u is not None:
                u["done"] += 1
    except Exception as exc:  # noqa: BLE001
        print(f"[lessons] get_script_done failed: {exc}")
    return out


def _track_topic(code: str, unit, name: str, status: str, course: str = "algebra1") -> None:
    """Record real per-topic engagement (Phase 2), but only when the database is on,
    and never let a tracking hiccup break a student's turn. `course` files the progress
    under the right course (multi-course, Phase 3); defaults to Algebra I."""
    if not (store.enabled() and unit):
        return
    try:
        store.record_topic(code, unit, name, status, course=course)
    except Exception as exc:  # noqa: BLE001
        print(f"[track] record_topic failed (ignored): {exc}")


def _resolve_unit(code: str, course: str, placement: dict, focus_unit: int):
    """ONE OWNER for "which unit is this student in" (2026-08-17, build hj -- full-app
    review Phase 3, and the completion of build gs).

    The review counted FIVE competing answers to this question, reconciled ad hoc by
    four consumers -- and the unit-rail bug (Jim, twice: "it still says unit one when
    we are talking about unit five") was this fact expressed through one of them. gs
    fixed the tracker for one turn; the NEXT session still re-derived from placement,
    because nothing carried the truth forward. This function is now the derivation,
    and everything downstream -- the prompt's playbook, the fourteenth referee, the
    tracker, the placement note -- consumes its RESULT as a field.

    Priority, most intentional first, each one named so the drift probe can say which
    source answered:
      focus       -- the student clicked "Work on it" (or the parent's standing steer,
                     resolved upstream): their explicit intent, always wins.
      tracked     -- the most recently touched UNMASTERED unit. This is what the
                     lesson is actually in: gs made the tutor's own [[unitplan]] the
                     tracking authority, so the declaration persists here across
                     sessions instead of evaporating at the next opener. A mastered
                     unit deliberately does NOT pin (progression must advance past a
                     finished unit even if its celebration was the last touch).
      progression -- the first unit whose best check score is below the bar: where
                     the course itself says they are.
      placement   -- where the Challenge placed them: meaningful ONLY while nothing
                     deeper exists (a brand-new student). The old code let this
                     outrank progression forever -- a number that never moves steering
                     lessons that do.
      default     -- Unit 1.
    Returns (unit, source). Never raises: any storage surprise degrades toward
    placement/default, never toward an exception in a child's turn."""
    if 1 <= int(focus_unit or 0) <= 9:
        return int(focus_unit), "focus"
    # THE PLACEMENT IS A FLOOR, not a pin. A student placed at Unit 3 was placed PAST
    # units 1-2 -- progression walks upward FROM the floor, so mastering unit 3 moves
    # them to 4, never "back" to units the Challenge already cleared. (The first
    # version of this function walked from 1 and sent a placed-at-3 student to Unit 1
    # the moment they mastered their placement unit -- caught by the priority-table
    # test before it ever ran.)
    try:
        floor = int((placement or {}).get("start_unit") or 1)
    except (TypeError, ValueError):
        floor = 1
    floor = floor if 1 <= floor <= 9 else 1
    mastered = set()
    try:
        if store.enabled():
            checks = (store.get_mastery(code, course) or {}).get("checks", {})
            mastered = {u for u in range(1, 10)
                        if int((checks.get(u) or {}).get("best_pct") or 0) >= store.PASS_PCT}
            rows = sorted((r for r in (store.get_topics(code, course) or [])
                           if r.get("last_touched") and 1 <= int(r.get("unit") or 0) <= 9),
                          key=lambda r: str(r.get("last_touched")), reverse=True)
            for r in rows:
                u = int(r["unit"])
                if u not in mastered:
                    return u, "tracked"
            for u in range(floor, 10):
                if u not in mastered:
                    if rows or mastered:          # the course has real history
                        return u, "progression"
                    break
    except Exception as exc:  # noqa: BLE001 -- resolution must never break a turn
        print(f"[resolve_unit] degraded to placement: {exc}")
    try:
        su = int((placement or {}).get("start_unit") or 0)
        if 1 <= su <= 9:
            return su, "placement"
    except (TypeError, ValueError):
        pass
    return 1, "default"


def _message_names_unit(message: str, course: str, unit: int) -> bool:
    """Did the student's OWN message just ask for this unit? True on an explicit
    "unit N" or when the message classifies to that unit's content ("can we do the
    pythagorean theorem?"). Conservative: classify_unit returns (None, None) on no
    match, and a failure here is simply False -- never an exception in a turn."""
    try:
        text = str(message or "")
        if not text or text.startswith("__"):
            return False
        if re.search(r"\bunit\s+0*{}\b".format(int(unit)), text, re.I):
            return True
        u, _name = curriculum.classify_unit(text, course)
        return u == int(unit)
    except Exception:  # noqa: BLE001
        return False


def _unit_allowed_set(code: str, course: str, resolved_unit: int, focus_unit: int = 0,
                      message: str = "") -> tuple:
    """BUILD hm (2026-08-18, Phase 4 -- Class D): every unit this turn's [[unitplan]]
    declaration could HONESTLY name, from facts the server actually holds:

      resolved     -- the unit _resolve_unit put them in (always allowed);
      focus        -- their explicit click / the parent's steer;
      touched      -- any unit with a topic_progress row (revisits are legitimate);
      mastered     -- any unit already mastered (reviewing it is legitimate);
      progression  -- the next unmastered unit after the resolved one (a legitimate
                      mid-session advance when a unit is finished);
      asked-for    -- a unit the student's OWN message just requested.

    The nineteenth referee (tutor.unitplan_conflict) regenerates a draft declaring
    anything else, and _accept_declared_unit refuses to file it. Never raises; a
    storage surprise degrades toward the smaller honest set, never an exception."""
    allowed = set()
    for u in (resolved_unit, focus_unit):
        try:
            u = int(u or 0)
        except (TypeError, ValueError):
            continue
        if 1 <= u <= 9:
            allowed.add(u)
    try:
        if store.enabled():
            checks = (store.get_mastery(code, course) or {}).get("checks", {})
            mastered = {u for u in range(1, 10)
                        if int((checks.get(u) or {}).get("best_pct") or 0) >= store.PASS_PCT}
            allowed |= mastered
            for r in (store.get_topics(code, course) or []):
                try:
                    u = int(r.get("unit") or 0)
                except (TypeError, ValueError):
                    continue
                if 1 <= u <= 9:
                    allowed.add(u)
            for q in (store.get_topic_quizzes(code, course) or []):
                try:
                    u = int(q.get("unit") or 0)
                except (TypeError, ValueError):
                    continue
                if 1 <= u <= 9:
                    allowed.add(u)
            try:
                start = int(resolved_unit or 0)
            except (TypeError, ValueError):
                start = 0
            if 1 <= start <= 9:
                for u in range(start + 1, 10):
                    if u not in mastered:
                        allowed.add(u)      # the next step, if this one finishes today
                        break
    except Exception as exc:  # noqa: BLE001 -- the referee degrades, the turn never breaks
        print(f"[unitplan] allowed-set degraded to resolved/focus: {exc}")
    for u in range(1, 10):
        if u not in allowed and _message_names_unit(message, course, u):
            allowed.add(u)
    if not allowed:
        allowed.add(1)
    return tuple(sorted(allowed))


def _accept_declared_unit(declared, resolved_unit: int, unit_source: str,
                          allowed, code: str = "", course: str = ""):
    """BUILD hm: the FILING gate for the tutor's [[unitplan]] declaration -- Jim's
    gs ruling (THE UNIT FOLLOWS THE TEACHING) now holds only when the record could
    justify the teaching. Returns (course_unit, verdict):

      verdict "none"       -- no declaration; track the resolved unit.
      verdict "focus-wins" -- an explicit focus outranks the declaration (unchanged
                              since gs: the student's click is the deeper intent).
      verdict "accepted"   -- the declaration is in the allowed set; it files, and
                              (via topic_progress) persists into the next resolution.
      verdict "rejected"   -- the record cannot justify it. The resolved unit files
                              instead and the rejection writes a system_events row --
                              a surviving hallucination becomes a chart, never a fact.

    Belt AND suspenders with the nineteenth referee: the referee regenerates these
    drafts in the pipeline, but every referee fails open, so the filing gate re-checks
    what actually shipped. Never raises."""
    try:
        if not declared:
            return resolved_unit, "none"
        if unit_source == "focus":
            return resolved_unit, "focus-wins"
        if int(declared) in set(int(u) for u in (allowed or ())):
            return int(declared), "accepted"
        print(f"[unitplan] REJECTED declaration: code={str(code)[:3]}*** course={course} "
              f"declared={declared} resolved={resolved_unit} allowed={list(allowed or ())}")
        try:
            store.record_event("unitplan_rejected", "filing",
                               f"declared={declared} resolved={resolved_unit} "
                               f"allowed={list(allowed or ())}", code, course)
        except Exception:  # noqa: BLE001
            pass
        return resolved_unit, "rejected"
    except Exception as exc:  # noqa: BLE001 -- filing must never break a turn
        print(f"[unitplan] accept check crashed (filing resolved): {exc}")
        return resolved_unit, "error"


def _resolve_focus(code: str, course: str, req_unit: int):
    """(focus_unit, steered) for this turn (build ea). Order of authority:
    1. the student's own explicit focus (a dashboard link) -- always wins;
    2. the parent's standing steer for THIS course (set on /family);
    3. none. Fail-open: a store hiccup never costs a turn."""
    if 1 <= int(req_unit or 0) <= 9:
        return int(req_unit), False
    try:
        if store.enabled():
            s = store.get_steer(code)
            if s and s.get("course") == course and 1 <= int(s.get("unit") or 0) <= 9:
                return int(s["unit"]), True
    except Exception as exc:  # noqa: BLE001
        print(f"[steer] resolve failed (ignored): {exc}")
    return 0, False


def _mastery_note(code: str, focus_unit: int = 0, course: str = "algebra1",
                  steered: bool = False) -> str:
    """PHASE B: a short, human-readable summary of what this student has MASTERED vs. still
    needs IN THIS COURSE, for the tutor to STEER by (spend effort on weak units + spaced
    review). Empty string when the DB is off or anything errors -- never breaks a turn."""
    if not store.enabled():
        return ""
    try:
        topics = {r["unit"]: r for r in store.get_topics(code, course)}
        checks = (store.get_mastery(code, course) or {}).get("checks", {})
    except Exception as exc:  # noqa: BLE001
        print(f"[mastery-note] failed (ignored): {exc}")
        return ""
    mastered, working, notstarted = [], [], []
    for n, name in curriculum.units_for(course):
        best = int((checks.get(n) or {}).get("best_pct") or 0)
        t = topics.get(n)
        if best >= store.PASS_PCT:
            mastered.append(f"Unit {n} ({name})")
        elif t and t.get("status") not in (None, "not-started"):
            tag = ("best " + str(best) + "%") if best else "no check yet"
            working.append(f"Unit {n} ({name}, {tag})")
        else:
            notstarted.append(str(n))
    parts = []
    if mastered:
        parts.append("MASTERED: " + "; ".join(mastered) + ".")
    if working:
        parts.append("STILL TO MASTER (focus here): " + "; ".join(working) + ".")
    if notstarted:
        parts.append("Not started: units " + ", ".join(notstarted) + ".")
    note = " ".join(parts) if parts else "Just getting started -- no mastery data yet."
    # TOPIC QUIZZES (2026-08-04): tell the tutor exactly which mid-unit quizzes are already
    # passed, so gating survives across sessions -- resume each unit's ladder at the first
    # unpassed topic and never re-quiz a passed one.
    try:
        qrows = store.get_topic_quizzes(code, course)
    except Exception as exc:  # noqa: BLE001
        print(f"[mastery-note] get_topic_quizzes failed (ignored): {exc}")
        qrows = []
    if qrows:
        by_unit = {}
        for q in qrows:
            by_unit.setdefault(q["unit"], []).append(q)
        qparts = []
        for n in sorted(by_unit):
            items = []
            for q in by_unit[n]:
                if q["best_pct"] >= store.QUIZ_PASS_PCT:
                    items.append(f"'{q['topic_name']}' PASSED ({q['best_pct']}%)")
                else:
                    items.append(f"'{q['topic_name']}' NOT passed yet (best {q['best_pct']}%)")
            qparts.append(f"Unit {n}: " + "; ".join(items))
        note += (" TOPIC QUIZZES so far -- " + " | ".join(qparts) +
                 ". Resume each unit at its first unpassed topic; do not re-quiz passed topics.")
    # RECENT MISSES (2026-08-11, build dt -- rule 55's spaced-review half). The tutor
    # reported these in quiz tags; now they come back as steering. Capped tight: the
    # note is per-turn prompt weight, and ONE revisited problem is the whole ask.
    try:
        misses = store.get_misses(code, course, limit=5)
    except Exception as exc:  # noqa: BLE001
        print(f"[mastery-note] get_misses failed (ignored): {exc}")
        misses = []
    if misses:
        mm = "; ".join(
            f"\"{m['question'][:80]}\" (they answered \"{m['answer'][:40]}\""
            + (f", Unit {m['unit']}" if m.get("unit") else "") + f", {m['when']})"
            for m in misses)
        note += (" RECENT MISSED PROBLEMS (rule 55): " + mm +
                 ". Early in this session -- after the opener, never as a cold open -- "
                 "revisit exactly ONE of these as a FRESH, slightly different problem "
                 "of the same kind, warmly. One is enough; never re-run a failed quiz.")
    fu = int(focus_unit or 0)
    if 1 <= fu <= 9:
        if steered:
            # build ea: the PARENT set this plan on /family -- the student did not ask.
            note += (f" THE FAMILY PLAN: their parent asked that sessions center on "
                     f"Unit {fu} ({curriculum.unit_name(course, fu)}) for now. Steer "
                     f"there warmly and introduce it as today's plan -- never as "
                     f"something the student requested, and never as a punishment. If "
                     f"the student asks to work on something else, honor rule 50: "
                     f"their agency wins for this session.")
        else:
            note += (f" TODAY the student chose to work on Unit {fu} "
                     f"({curriculum.unit_name(course, fu)}) -- center this session there.")
    return note


def _claim_record(code: str, course: str):
    """BUILD ho (2026-08-18, Phase 4 -- Class D): the compact record the twentieth
    referee (tutor.record_claim_conflict) judges past-claims against. Everything in
    it is a fact the server holds:
        best / last  -- unit-check percentages, keyed by unit
        quiz_pcts    -- topic-quiz best percentages (sorted, de-duplicated)
        mastered     -- units at/over the bar
        touched      -- units with any topic_progress row
    Returns None when the DB is off or anything surprises -- the referee then stays
    silent rather than guessing (the gn property). Never raises."""
    if not store.enabled():
        return None
    try:
        checks = (store.get_mastery(code, course) or {}).get("checks", {})
        best, last, mastered = {}, {}, []
        for u in range(1, 10):
            c = checks.get(u) or {}
            if int(c.get("checks_taken") or 0) or int(c.get("best_pct") or 0):
                best[u] = int(c.get("best_pct") or 0)
                last[u] = int(c.get("last_pct") or 0)
            if int(c.get("best_pct") or 0) >= store.PASS_PCT:
                mastered.append(u)
        touched = sorted({int(r.get("unit")) for r in (store.get_topics(code, course) or [])
                          if str(r.get("unit") or "").isdigit()
                          and 1 <= int(r.get("unit")) <= 9})
        quiz_pcts = sorted({int(q.get("best_pct") or 0)
                            for q in (store.get_topic_quizzes(code, course) or [])})
        return {"best": best, "last": last, "quiz_pcts": quiz_pcts,
                "mastered": mastered, "touched": touched}
    except Exception as exc:  # noqa: BLE001 -- a silent referee beats a broken turn
        print(f"[claimrecord] degraded to None: {exc}")
        return None


def _opener_record_note(code: str, course: str, resolved_unit: int, history) -> tuple:
    """BUILD hm (2026-08-18, Phase 4 -- Class D's opener half): (has_record, note).

    The opener used to hand the model an UNCONDITIONAL demand for a recap ("give a
    SHORT recap of where you two are") and let the model decide from history whether
    you had met -- so when the record was empty, compliance REQUIRED invention, the
    invented recap was stored verbatim in history, and every later opener replayed it
    as memory (the review's most plausible phantom-Unit-5 origin). The server holds
    the record; the server now decides.

    has_record -- True only if something REAL exists: a stored assistant turn in this
    course's history, a touched unit, or a mastered unit. Placement alone is NOT a
    record of lessons together (rule 0's placement-honesty clause already governs it).

    note -- when has_record, the recap FACTS stated by the server from the store:
    the resolved unit (the same value the prompt's playbook and the referees were
    given), mastered units, last-active date. History is thereby demoted to STYLE:
    the note says in so many words that when the conversation and the record
    disagree, the record wins. Never raises; a store surprise degrades toward
    "less claimed", never toward an exception in a child's opener."""
    hist_real = False
    try:
        hist_real = any((m or {}).get("role") == "assistant" for m in (history or []))
    except Exception:  # noqa: BLE001
        hist_real = False
    touched, mastered, last_active = [], [], ""
    try:
        if store.enabled():
            rows = store.get_topics(code, course) or []
            touched = sorted({int(r.get("unit")) for r in rows
                              if str(r.get("unit") or "").isdigit()
                              and 1 <= int(r.get("unit")) <= 9})
            checks = (store.get_mastery(code, course) or {}).get("checks", {})
            mastered = sorted(u for u in range(1, 10)
                              if int((checks.get(u) or {}).get("best_pct") or 0)
                              >= store.PASS_PCT)
            la = (store.get_course_activity(code).get(course) or {}).get("last_active")
            last_active = str(la or "")[:10]
    except Exception as exc:  # noqa: BLE001 -- claim less, never break the opener
        print(f"[opener] record note degraded: {exc}")
    has_record = bool(hist_real or touched or mastered)
    if not has_record:
        return False, ""
    try:
        uname = curriculum.unit_name(course, resolved_unit) or ""
    except Exception:  # noqa: BLE001
        uname = ""
    bits = ["you two are working in Unit {}{}".format(
        resolved_unit, " ({})".format(uname) if uname else "")]
    if mastered:
        bits.append("already mastered: Unit " + ", Unit ".join(str(u) for u in mastered))
    if last_active:
        bits.append("last session in this course: " + last_active)
    note = (" SERVER RECORD FOR YOUR RECAP -- progress FACTS come from HERE and from "
            "the mastery notes above; the conversation below refreshes tone and recent "
            "wording only, and if it seems to remember a unit or topic this record does "
            "not show, THE RECORD WINS: " + "; ".join(bits) + ". When you name a unit, "
            "name THAT one. If you are unsure exactly what you were doing last time, "
            "say less, never more: welcome them back and start from what the record "
            "shows.")
    return True, note


def save_placement(code: str, result: dict, course: str = "algebra1") -> None:
    if store.enabled():
        store.save_placement(code, result, course)
        return
    with _sessions_lock:
        all_p = {}
        if PLACEMENTS_FILE.exists():
            try:
                with open(PLACEMENTS_FILE, "r", encoding="utf-8") as fh:
                    all_p = json.load(fh)
            except (json.JSONDecodeError, OSError):
                all_p = {}
        all_p[_ck(code, course)] = result
        tmp = PLACEMENTS_FILE.with_suffix(".json.tmp")
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(all_p, fh, ensure_ascii=False, indent=2)
        tmp.replace(PLACEMENTS_FILE)


# ---- Request models --------------------------------------------------------
class LoginRequest(BaseModel):
    code: str


class ChatRequest(BaseModel):
    code: str
    message: str
    unit: int = 0              # optional focus unit (from the dashboard "Work on it" link)
    course: str = "algebra1"   # which course this lesson session belongs to (multi-course)
    # 2026-08-07 FINAL EXAM: "" (normal lesson) | "prep" | "exam". The server RE-VERIFIES
    # eligibility (every unit of the course mastered -- derived, build ew) on every
    # turn -- the client is never trusted.
    final: str = ""


class SprintResultIn(BaseModel):
    course: str = "prealgebra"
    unit: int = 1
    skill: str = ""
    a_correct: int = 0
    a_attempted: int = 0
    b_correct: int = 0
    b_attempted: int = 0


class FinalIn(BaseModel):
    correct: int
    total: int
    course: str = "algebra1"
    missed: list = []          # build dt: rule 55's missed problems ride the same POST


class PracticeRequest(BaseModel):
    code: str
    problem: str = ""          # the specific problem the student is stuck on
    message: str               # what the student just said (or the problem, first turn)
    history: list = []         # prior practice turns, held by the browser (not persisted)
    course: str = "algebra1"   # which course this practice session belongs to (multi-course)


class TopicRequest(BaseModel):
    code: str
    topic: str = ""            # the topic the student chose to explore
    message: str               # what the student just said (or the topic, first turn)
    history: list = []         # prior topic turns, held by the browser (not persisted)
    course: str = "algebra1"   # which course this topic exploration belongs to (multi-course)


class HeartbeatRequest(BaseModel):
    code: str
    course: str = "algebra1"   # which course the student is working in right now
    day: str = ""              # the STUDENT'S local calendar day 'YYYY-MM-DD' (validated server-side)


class PlacementIn(BaseModel):
    level: int = 1
    level_title: str = ""
    start_unit: int = 1
    start_unit_name: str = ""
    points: int = 0
    # 2026-08-13 (build ew): the assessment's per-unit picture rides INSIDE the placement
    # payload now, instead of masquerading as unit CHECKS (which fed mastery and could
    # silently pass a unit -- the exact thing Jim's policy forbids). `strengths` is the
    # competent units' names (the dashboard chips + the tutor prompt's "Strengths:" line
    # both already read placement.strengths -- dormant until today); `units` is the full
    # per-unit result list ({u, name, correct, total, pct, rating, competent}). Stored in
    # the placements JSON blob -- no schema change, and nothing here touches mastery.
    strengths: list = []
    units: list = []


class _CheckMissedMixin(BaseModel):
    missed: list = []          # build dt: rule 55's missed problems ride the same POST


class CheckIn(_CheckMissedMixin):
    unit: int                  # which of the 9 units this end-of-unit check covered
    correct: int = 0           # questions the student got right
    total: int = 1             # questions on the check
    course: str = "algebra1"   # which course this check belongs to (so it's filed per-course)


class QuizIn(BaseModel):
    """A mid-unit TOPIC QUIZ result (2026-08-04). Passing (80%+) unlocks the next topic."""
    unit: int                  # which of the 9 units the topic belongs to
    topic: int = 0             # the topic's position in the unit's topic list (1-based; 0 = unknown)
    name: str = ""             # the topic's name as the tutor stated it
    correct: int = 0
    total: int = 1
    course: str = "algebra1"
    missed: list = []          # build dt: [{"q": question, "a": their answer}, ...] from rule 55


def _keep_misses(code: str, course: str, unit: int, topic: int, kind: str,
                 missed, correct: int, total: int) -> None:
    """Store the tag's missed problems (build dt), HONESTLY CLAMPED: never more
    entries than were actually missed (total - correct), never more than 25, and
    always fail-open -- a malformed missed list must never cost the score above it."""
    try:
        if not (store.enabled() and missed):
            return
        room = max(0, min(25, int(total) - int(correct)))
        if not room:
            return
        items = []
        for it in list(missed)[:room]:
            if isinstance(it, dict):
                items.append({"q": it.get("q"), "a": it.get("a")})
        if items:
            store.record_misses(code, course, int(unit or 0), int(topic or 0),
                                kind, items)
    except Exception as exc:  # noqa: BLE001
        print(f"[misses] store failed (ignored): {exc}")


# TEACHER / PARENT CLASSROOM (2026-07-28) -- see the classroom endpoints below.
class ClassIn(BaseModel):
    class_code: str            # short, case-insensitive key the teacher picks (e.g. "MRSB-P3")
    name: str = ""             # friendly label, e.g. "Period 3 Algebra"
    owner_name: str = ""       # teacher/parent display name (optional)
    teacher_code: str = ""     # LEGACY convenience key, kept only for inheritance (build fa)
    token: str = ""            # build fa: the signed-in teacher's token -- now REQUIRED


class ClassStudentIn(BaseModel):
    code: str                  # an EXISTING student code to add to the class
    token: str = ""            # build fa: the signed-in teacher's token


# TEACHER ACCOUNTS (2026-08-13, build fa -- closing security finding F2).
class TeacherSignupIn(BaseModel):
    email: str
    password: str
    name: str = ""             # display name (optional)
    school: str = ""           # optional, display only
    teacher_code: str = ""     # OPTIONAL: inherit the classes run under this legacy code


class TeacherLoginIn(BaseModel):
    email: str
    password: str


class TeacherForgotIn(BaseModel):
    email: str


class TeacherResetIn(BaseModel):
    token: str
    password: str


class TeacherTokenIn(BaseModel):
    token: str = ""


class TeacherClaimIn(BaseModel):
    token: str = ""
    class_code: str


class ParentSignupIn(BaseModel):
    email: str
    password: str
    name: str = ""             # parent's display name (optional)


class ParentLoginIn(BaseModel):
    email: str
    password: str


class ParentTokenIn(BaseModel):
    token: str


class ParentForgotIn(BaseModel):
    email: str


class ParentResetIn(BaseModel):
    token: str
    password: str


class ParentStudentIn(BaseModel):
    token: str
    name: str                  # child's FIRST name only (we ask for nothing more)


class MarkIn(BaseModel):
    correct: int = 1           # was the practice problem right (1) or wrong (0)
    attempted: int = 1         # how many problems this represents (usually 1)
    highest_tier: int = 0
    strengths: list = []
    # (rc, 2026-08-31) 1 = a wrong tap on the CURRENT, still-going problem (the
    # [[miss]] tag). Resets the today-streak only -- no counters, no finished problem.
    miss: int = 0


# ---- App -------------------------------------------------------------------
app = FastAPI(title="Math Tutor MVP", version="0.1.0")


# =============================================================================
# SECURITY HEADERS (build ec, 2026-08-12 -- finding F4)
# -----------------------------------------------------------------------------
# One small middleware stamps the standard browser-hardening headers on EVERY
# response (pages, API, static). These are defense-in-depth: alone they ruin
# nothing, but together they stop a whole class of tricks -- clickjacking (our
# site framed inside a fake page), MIME-sniffing, protocol downgrade, and
# referrer leakage.
#
#   X-Content-Type-Options   nosniff -- browser must honor our declared types
#   X-Frame-Options          SAMEORIGIN -- only WE may frame our own pages
#   Referrer-Policy          strict-origin-when-cross-origin -- no path leak off-site
#   Strict-Transport-Security force HTTPS for a year (Render is HTTPS-only already)
#   Permissions-Policy       deny camera/geolocation/payment; MIC stays allowed
#                            (the tutor is voice-first)
#   Content-Security-Policy-Report-Only  -- the ONE header shipped in REPORT-ONLY
#                            mode on purpose. Our pages use inline <style>/<script>
#                            and load Plausible; an enforcing CSP could blank the
#                            site, so we start by DESCRIBING the policy without
#                            blocking, and can flip it to enforcing (and add a
#                            nonce refactor to drop 'unsafe-inline') once proven.
# setdefault() everywhere so a route that sets its own header always wins.
# =============================================================================
_CSP_REPORT_ONLY = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' https://plausible.io; "
    "style-src 'self' 'unsafe-inline'; "
    "img-src 'self' data:; "
    "font-src 'self' data:; "
    # 2026-08-17 (build gp2, found in Jim's console during a live Geometry lesson): every
    # silent-WAV data: URI was logging a CSP violation, because media-src was never set and
    # so fell back to default-src 'self'. Report-only today, which is why nothing broke --
    # but this header is documented as something we intend to FLIP TO ENFORCING, and on
    # that day silentWavUri() would stop loading. That single function is BOTH the audio
    # warm-up and the keep-alive loop: the two mechanisms that protect the first syllable
    # of every sentence the tutor speaks. The voice would regress and nobody would connect
    # it to a security header. A landmine defused for the cost of one line.
    "media-src 'self' data:; "
    "connect-src 'self' https://plausible.io; "
    "frame-ancestors 'self'; "
    "base-uri 'self'; "
    "form-action 'self'; "
    "object-src 'none'"
)
_SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "SAMEORIGIN",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Permissions-Policy": "camera=(), geolocation=(), payment=(), microphone=(self)",
    "Content-Security-Policy-Report-Only": _CSP_REPORT_ONLY,
}


@app.middleware("http")
async def _security_headers(request: Request, call_next):
    response = await call_next(request)
    for _h, _v in _SECURITY_HEADERS.items():
        response.headers.setdefault(_h, _v)
    # build nx (2026-08-26): THE HARD-REFRESH RITUAL DIES. Three separate times a
    # shipped fix "wasn't there" until Jim pressed Ctrl+F5 (the demo sidebar, the
    # owner's flag, the admin queue): StaticFiles sends no Cache-Control, so
    # browsers cached pages and scripts on heuristics and served them STALE after
    # a deploy. Now every HTML/JS/CSS response says "no-cache" -- which means
    # REVALIDATE, not "don't store": the ETag/Last-Modified that FileResponse
    # already sends makes an unchanged file a tiny 304, and a changed file
    # arrives the moment Render restarts. ⚠️ SCOPED BY CONTENT TYPE on purpose:
    # audio (/api/speak's clips), images and JSON are untouched -- re-validating
    # every cached voice clip would add a round-trip to every sentence Mr.
    # Cadabra speaks (the same landmine the CSP note above defused).
    _ct = response.headers.get("content-type", "")
    if ("text/html" in _ct or "javascript" in _ct or "text/css" in _ct):
        response.headers.setdefault("Cache-Control", "no-cache")
    return response


def _lookup_student(code: str):
    """Find a student by code, wherever they live (2026-07-31).

    Pilot/persona students come from students.json exactly as before. Students
    created by a signed-up parent live in the database (accounts.parent_id set);
    they are returned in the same shape the rest of the app expects, so every
    endpoint (chat, dashboard, awards, heartbeat, voice) works for them unchanged.
    Returns None when the code is unknown."""
    code = (code or "").strip()
    if not code:
        return None
    student = STUDENTS.get(code)
    if student:
        return student
    if store.enabled():
        acct = store.get_account(code)
        if acct and acct.get("parent_id"):
            return {
                "name": acct.get("name") or "Student",
                "grade": "",
                "progress": "",                      # real progress lives in the DB tables
                "family": True,                       # marks a parent-managed student
                "parent_id": acct["parent_id"],
            }
        # BETA PASS (2026-07-31): valid ONLY while a sign-in window is open. Full
        # access during the window (it's a trial of the real product); when the
        # window lapses, _student_or_404 explains kindly instead of a bare 404.
        bc = store.get_beta_code(code)
        if bc and not bc.get("revoked") and store.beta_window_active(bc):
            return {"name": bc.get("label") or "Beta tester", "grade": "",
                    "progress": "", "beta": True}
    return None


def _beta_404_detail(code: str):
    """A kind, specific message when a KNOWN beta pass can't be used right now."""
    if not store.enabled():
        return None
    bc = store.get_beta_code(code)
    if not bc:
        return None
    if bc.get("revoked"):
        return "This beta pass has been closed. Email support@mrcadabra.com if that seems wrong."
    left = int(bc["uses_allowed"]) - int(bc["uses_used"])
    if left <= 0:
        return ("This beta pass has been used up — thank you for test-driving Mr. Cadabra's Classroom! "
                "We'd love your feedback at support@mrcadabra.com.")
    return (f"Your beta session window has ended. Sign in again with this pass to keep "
            f"going — {left} of {bc['uses_allowed']} sign-ins left.")


def _student_or_404(code: str) -> dict:
    student = _lookup_student(code)
    if not student:
        beta_note = _beta_404_detail((code or "").strip())
        raise HTTPException(status_code=404,
                            detail=beta_note or "That code was not recognized.")
    return student


# -----------------------------------------------------------------------------
# COST & ABUSE GUARDS (added 2026-07-30, market-prep lockdown)
# -----------------------------------------------------------------------------
# Every /api/chat, /api/practice, /api/topic call spends Anthropic money, and every
# /api/speak / /api/transcribe call spends ElevenLabs money. Before this change,
# /api/speak and /api/transcribe required NO login code at all -- a stranger who
# found the URL could run up the bill directly -- and nothing anywhere was rate
# limited. Now: (a) both voice endpoints require a valid student code; (b) the
# spoken text has a hard length cap; (c) a small in-process sliding-window rate
# limiter throttles every paid endpoint per code (and /api/login per IP, so the
# 4-digit code space can't be brute-forced quickly). The limits are set WELL above
# any real student's pace, so a legitimate user never sees a 429.
_RL_LOCK = threading.Lock()
_RL_BUCKETS: dict = defaultdict(deque)
MAX_SPEAK_CHARS = 5000          # tutor replies spoken aloud run ~200-2500 chars; 5000 is generous
# BUILD ke: configurable, because the scripted course is now a real, measurable
# claim on this disk and the honest answer to "it does not fit" is a bigger cap,
# not a quieter evictor. Default unchanged at 300 MB. Set TTS_CACHE_MAX_MB in
# Render -> Environment to raise it; script-prewarm's dry_run reports the fit.
try:
    _TTS_CACHE_MAX_MB = max(50, int(os.environ.get("TTS_CACHE_MAX_MB", "300")))
except Exception:  # noqa: BLE001 -- a bad env value must not stop the app booting
    _TTS_CACHE_MAX_MB = 300
_TTS_CACHE_MAX_BYTES = _TTS_CACHE_MAX_MB * 1024 * 1024   # cap the audio cache (evicts generated lane first)
# BUILD me: how much room an eviction leaves ABOVE the protected course, so that a
# cull does not put us straight back over the cap on the very next generated clip.
_TTS_EVICT_MARGIN_BYTES = 64 * 1024 * 1024        # 64 MB


def _rate_limit(key: str, limit: int, window_seconds: int, what: str = "requests") -> None:
    """Sliding-window limiter. Raises 429 if `key` exceeds `limit` per `window_seconds`."""
    now = time.monotonic()
    with _RL_LOCK:
        # Keep the bucket table itself from growing without bound.
        # build cn: the old sweep only dropped buckets that were ALREADY empty, so with
        # ten thousand active students -- every bucket non-empty -- the table could grow
        # past the cap and never come back down. Expire by age instead: a bucket whose
        # newest hit is older than its window is spent, whatever it still holds.
        if len(_RL_BUCKETS) > 5000:
            stale = [k for k, q in _RL_BUCKETS.items()
                     if not q or q[-1] <= now - max(window_seconds, 3600)]
            for k in stale:
                _RL_BUCKETS.pop(k, None)
            if len(_RL_BUCKETS) > 50000:      # pathological: shed the oldest wholesale
                for k in sorted(_RL_BUCKETS, key=lambda k: _RL_BUCKETS[k][-1]
                                if _RL_BUCKETS[k] else 0)[:20000]:
                    _RL_BUCKETS.pop(k, None)
                print("[rate] bucket table shed to 30k keys")
        q = _RL_BUCKETS[key]
        while q and q[0] <= now - window_seconds:
            q.popleft()
        if len(q) >= limit:
            raise HTTPException(status_code=429,
                                detail=f"Too many {what} in a short time — please wait a minute and try again.")
        q.append(now)


# =============================================================================
# READ-BY-CODE ENUMERATION GUARD (build ed, 2026-08-12 -- finding F1)
# -----------------------------------------------------------------------------
# A student's login code is the only key to their data, and the GET-by-code reads
# (session, records, misses, awards, time, topics, assessment, placement, courses,
# sprints, sprint) had NO speed limit -- someone could script guesses across the
# short code space and harvest children's names and progress.
#
# The precise defense: ENUMERATION IS, BY DEFINITION, "many DIFFERENT codes from
# one source." A real family reads its own 1-2 codes over and over; a scraper walks
# thousands. So on top of a generous raw per-IP read cap (blunts hammering/cost), we
# track how many DISTINCT codes each IP has touched in a rolling window and refuse
# once it crosses a ceiling set far above any honest use (a whole co-op reviewed
# from one address is ~30 kids; the ceiling is higher still). Repeatedly reading the
# SAME code -- a real dashboard reloading -- never trips it. Paired with the widened
# code format (_new_student_code) and the F3 IP-spoofing fix, a sweep is infeasible:
# an IP is capped to CODE_PROBE_MAX guesses per window and can't rotate its address.
# All in-process, self-pruning; env-tunable without a code change.
# =============================================================================
try:
    _READ_IP_LIMIT = int(os.environ.get("READ_IP_LIMIT", "600") or 600)
except (TypeError, ValueError):
    _READ_IP_LIMIT = 600
try:
    _CODE_PROBE_MAX = int(os.environ.get("CODE_PROBE_MAX", "50") or 50)
except (TypeError, ValueError):
    _CODE_PROBE_MAX = 50
try:
    _CODE_PROBE_WINDOW = int(os.environ.get("CODE_PROBE_WINDOW", "900") or 900)
except (TypeError, ValueError):
    _CODE_PROBE_WINDOW = 900
_CODE_PROBE_LOCK = threading.Lock()
_CODE_PROBE: dict = defaultdict(dict)      # ip -> {code: last_seen_monotonic}


def _read_guard(request: Request, code: str) -> None:
    """Throttle a read-by-code endpoint against enumeration. Raises 429 when an IP
    exceeds the raw read rate OR touches too many DISTINCT codes in the window."""
    ip = _client_ip(request)
    # (1) raw per-IP read cap -- generous for a browsing family, a wall for a firehose.
    _rate_limit("read:" + ip, limit=_READ_IP_LIMIT, window_seconds=300, what="lookups")
    # (2) distinct-code ceiling -- the actual anti-enumeration guard.
    key = (code or "").strip()
    now = time.monotonic()
    with _CODE_PROBE_LOCK:
        seen = _CODE_PROBE[ip]
        for c in [c for c, t in seen.items() if t <= now - _CODE_PROBE_WINDOW]:
            del seen[c]
        seen[key] = now
        distinct = len(seen)
        if not seen:                                    # never keep an empty inner dict
            _CODE_PROBE.pop(ip, None)
        if len(_CODE_PROBE) > 20000:                    # keep the outer table bounded
            for k in [k for k, d in _CODE_PROBE.items()
                      if not d or max(d.values()) <= now - _CODE_PROBE_WINDOW]:
                _CODE_PROBE.pop(k, None)
    if distinct > _CODE_PROBE_MAX:
        raise HTTPException(status_code=429, detail=(
            "Too many different codes tried from this connection — if you're a "
            "teacher reviewing a class, please wait a minute between students."))


def _client_ip(request: Request) -> str:
    """Caller IP for the per-IP rate limiter, read from the position we actually trust.

    SECURITY (build ec, 2026-08-12 -- finding F3): X-Forwarded-For is built LEFT-to-right
    (client, proxy1, proxy2, ...). A visitor can PREPEND any value they like on the left,
    so the old `.split(",")[0]` (leftmost) was attacker-controlled -- rotating a fake header
    let someone slip the sign-in / signup / password-reset brute-force limits. Our own
    proxy (Render) APPENDS the real peer on the RIGHT, and the client cannot control what we
    append. So we trust only the rightmost `TRUSTED_PROXY_HOPS` entries and take the one just
    inside them. Default 1 hop = "the last entry" = the address Render saw the connection
    from. If ever fronted by an extra trusted proxy (e.g. Cloudflare -> Render), set
    TRUSTED_PROXY_HOPS=2 in the environment; never lower it below the real hop count.
    """
    try:
        hops = int(os.environ.get("TRUSTED_PROXY_HOPS", "1") or 1)
    except (TypeError, ValueError):
        hops = 1
    if hops < 1:
        hops = 1
    fwd = [p.strip() for p in (request.headers.get("x-forwarded-for") or "").split(",") if p.strip()]
    if fwd:
        idx = len(fwd) - hops                 # the entry just inside our trusted proxy hops
        return fwd[idx] if idx >= 0 else fwd[0]
    return request.client.host if request.client else "unknown"


def _degraded_reply():
    """BUILD hv: the answer a teaching lane gives while the database is CONFIGURED
    but unreachable (store.degraded()). The old behaviour silently forked every
    write onto local files that no backup covers and no reconnect reclaims -- a
    student practiced into a void and the record called them absent. Honest beats
    silent: a warm pause message, a system print, and Jim's inbox (throttled).
    Returns None when healthy (or when ALLOW_FILE_FALLBACK marks a dev box)."""
    if not store.degraded() or ALLOW_FILE_FALLBACK:
        return None
    print("[store] degraded: teaching turn answered with the maintenance message")
    _ops_alert("db-degraded", "Database unreachable — teaching paused",
               "DATABASE_URL is set but the database cannot be reached; students are "
               "seeing the maintenance message. Check the Render database, then "
               "/health storage.degraded.")
    return {"reply": ("(One moment — my classroom notebook is being looked after, "
                      "and I never teach without it, so nothing you do gets lost. "
                      "Please try again in a few minutes!)"),
            "degraded": True}


def _require_student(code: str) -> dict:
    """Like _student_or_404 but returns 401 (auth), for the paid voice endpoints."""
    student = _lookup_student(code)
    if not student:
        raise HTTPException(status_code=401, detail="A valid login code is required.")
    return student


def _code_dep(code: str, request: Request) -> str:
    """BUILD hs (2026-08-18, Phase 5 -- THE CREDENTIAL LEAVES THE URL, review Class F).
    The student CODE is the login; a code in a URL is a password in a request line,
    and request lines are written to plaintext HTTP logs we do not control (Render's
    edge, uvicorn's access log). Every student-gated {code} route now resolves its
    code through THIS dependency: the X-Student-Code HEADER is preferred (the pages
    send the placeholder 'me' in the path), and the old path form still works so a
    stale cached page keeps functioning across the deploy -- it is the PAGES that
    stopped putting the credential in the URL, the server merely stopped requiring
    them to. (The dg precedent: the admin key made this exact move to X-Admin-Key.)
    Page-NAVIGATION links (/session?code=...) still carry the code BY JIM'S RULING
    (2026-08-18, same day: "Do not kill the bookmark login") -- a family bookmark
    is how a young student signs in, and that convenience is the product. The
    compensating controls are real: API calls never carry the code (this
    dependency), the read-guard throttles code enumeration, and a parent can mint
    a new code in one tap if one leaks (build dy). Do not "fix" this without a
    NEW ruling from Jim."""
    try:
        h = (request.headers.get("X-Student-Code") or "").strip()
    except Exception:  # noqa: BLE001
        h = ""
    if h:
        return h
    c = (code or "").strip()
    return "" if c.lower() in ("me", "-") else c


@app.get("/")
def home():
    """FRONT DOOR (changed 2026-07-30): the marketing/landing page. A parent visiting
    mrcadabra.com now sees what MyTutor IS, with a Sign in link -- the bare code-entry
    screen used to live here and moved to /login. Every in-app 'kick back to login'
    redirect was retargeted from '/' to '/login' in the same change."""
    return FileResponse(STATIC_DIR / "landing.html")


@app.get("/login")
def login_page():
    """The code-entry screen (was served at '/' until 2026-07-30)."""
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/demo")
def demo_page():
    """The self-contained interactive demo lesson (pretty route for marketing links).
    (uh) The front door now leads to /demo/lesson first -- a REAL authored lesson --
    and comes back here for the classroom tour (?tour=1) and the three views
    (?views=1); see static/demo.html's note."""
    return FileResponse(STATIC_DIR / "demo.html")


@app.get("/demo/lesson")
def demo_lesson_page():
    """(uh, 2026-09-08) THE DEMO TEACHES -- P3 of the deep look. A visitor picks a
    level and Mr. Cadabra teaches the opening of that course's first authored lesson
    exactly as a student hears it: the why, the picture, the rule read off it, the
    worked example, then ONE question the visitor answers by tap or by typing, then
    the walk-back on the picture. The real engine (lessonscripts), the real boards
    (script-board.js), the real voice (the pre-rendered closure, cache-only), no
    student record, no model. The page: static/demo-lesson.html."""
    return FileResponse(STATIC_DIR / "demo-lesson.html")


@app.get("/homeschool")
def homeschool_page():
    """Marketing: the dedicated homeschool page (parent view, honest hours, records)."""
    return FileResponse(STATIC_DIR / "homeschool.html")


@app.get("/records")
def records_page():
    """The printable homeschool records report (2026-08-04): hours log, mastery, awards."""
    return FileResponse(STATIC_DIR / "records.html")


@app.get("/help")
def help_page():
    """In-app help (2026-08-11, build ds): the student-first FAQ. Every app page's
    ❓ Help button lands here -- the old mailto: link was dead on school Chromebooks."""
    return FileResponse(STATIC_DIR / "help.html")


@app.get("/students")
def students_page():
    """Marketing/help: the student how-to page (lesson flow, tools, earnable awards)."""
    return FileResponse(STATIC_DIR / "students.html")


@app.get("/parents")
def parents_page():
    """Marketing: the parent trust page (child experience, parent view, privacy promises)."""
    return FileResponse(STATIC_DIR / "parents.html")


@app.get("/courses")
def courses_page():
    """Marketing: all eight courses with every unit listed (printable scope & sequence)."""
    return FileResponse(STATIC_DIR / "courses.html")


@app.get("/features")
def features_page():
    """Marketing (2026-08-05): every product feature on one page, grouped in six
    sections of three cards. Everything listed is live in the product today."""
    return FileResponse(STATIC_DIR / "features.html")


@app.get("/teachers")
def teachers_page():
    """Marketing: the classroom/co-op page (heatmap screenshot, features, pilot CTA)."""
    return FileResponse(STATIC_DIR / "teachers.html")


@app.get("/family")
def family_page():
    """The family portal (2026-07-31): parent signup/sign-in, children + their codes,
    plan & billing. The page's own JS talks to /api/parent/* and /api/billing/*."""
    return FileResponse(BASE_DIR / "static" / "family.html")


@app.get("/beta")
def beta_page():
    """Beta-tester program (2026-07-31): public pitch + Jim's ?admin= generator."""
    return FileResponse(BASE_DIR / "static" / "beta.html")


@app.get("/admin")
def admin_page():
    """Jim's central admin dashboard (2026-08-03). A visitor without the key sees
    only a locked 'enter your key' prompt; the real numbers, the beta generator,
    and the quick links appear only after /api/admin/stats verifies the key
    server-side. The admin key never lives in this file."""
    return FileResponse(BASE_DIR / "static" / "admin.html")


@app.get("/mission")
def mission_page():
    """Our mission (2026-07-31): fun, accessible, complete, taught right."""
    return FileResponse(BASE_DIR / "static" / "mission.html")


@app.get("/methodology")
def methodology_page():
    """(mv) How we teach, and what it is built on. Jim, 2026-08-24: "people want to
    know what we've based our pedagogical approach to. What resources did we use?"

    ⚠️ THE THIRD SECTION OF THAT PAGE SAYS WE HAVE PROVEN NOTHING, and it stays. A
    page that implied a proven outcome would be the first thing a careful parent
    caught us on, and the admission is what makes the two sections above it worth
    believing. Not in the top nav until Jim has read the wording."""
    return FileResponse(BASE_DIR / "static" / "methodology.html")


@app.get("/community")
def community_page():
    """The community forum (2026-07-31): parents post, everyone reads."""
    return FileResponse(BASE_DIR / "static" / "community.html")


@app.get("/pricing")
def pricing_page():
    """Marketing: standalone pricing page."""
    return FileResponse(STATIC_DIR / "pricing.html")


@app.get("/session")
def session_page():
    """The screen where the student talks with the tutor."""
    return FileResponse(STATIC_DIR / "session.html")


@app.get("/dashboard")
def dashboard_page():
    """The full-screen progress dashboard."""
    return FileResponse(STATIC_DIR / "dashboard.html")


@app.get("/teacher")
def teacher_page():
    """The CLASSROOM view: a teacher or parent following several students at once."""
    return FileResponse(STATIC_DIR / "teacher.html")


@app.get("/challenge")
def challenge_page():
    """Mr. Cadabra's Challenge -- the fun adaptive placement quiz."""
    return FileResponse(STATIC_DIR / "challenge.html")


@app.get("/practice")
def practice_page():
    """Practice mode -- bring a specific problem from school and get coached on it."""
    return FileResponse(STATIC_DIR / "practice.html")


@app.get("/drill")
def drill_page():
    """ABRABOT'S PRACTICE ROOM (build mh) -- extra problems from drillpool.py, fed by
    a helper who speaks in the BROWSER's voice. Separate from /practice, which is the
    AI homework-help lane: this one costs nothing per problem and touches no mastery.
    """
    return FileResponse(STATIC_DIR / "drill.html")


@app.get("/home")
def home_page():
    """The 'what would you like to do today?' hub (course / practice / topic)."""
    return FileResponse(STATIC_DIR / "home.html")


@app.get("/pilot")
def pilot_page(request: Request):
    """THE AUTHORED-SPINE LANE (build op -- Phase 3's pilot, Jim's "go").
    Scripted lessons served instantly from the authored course, the model held to
    bounded interventions. The home hub linked Pre-Algebra students here with
    ?course=prealgebra&unit=1 during the pilot; unfiltered it is the full scripted
    picker. (ud) AN OWNER TOOL NOW: session.html carries the authored lane for every
    student, nothing links here any more, and the public gets the same 404 a missing
    page gets. Unlock from /admin (the dashboard sets the owner cookie) or send the
    admin key in X-Admin-Key."""
    if not _is_owner(request):
        raise HTTPException(status_code=404, detail="Not Found")
    return FileResponse(STATIC_DIR / "pilot.html")


@app.get("/api/site-flags")
def site_flags():
    """(ud) Public, boolean-only page flags. `test_codes`: /login may print the
    persona test codes (SHOW_TEST_CODES, or a dev box). Nothing here is a secret."""
    return {"test_codes": bool(SHOW_TEST_CODES), "build": APP_BUILD}


@app.post("/api/owner/unlock")
def owner_unlock(request: Request, response: Response,
                 x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """(ud) Set the HttpOnly owner cookie that opens the owner's tools (/pilot, the
    bench, the demo concept page, static/mockup/). Header only -- the key never rides
    in a URL (build dg). Constant-time, general tier, 30 days, Secure on https."""
    _require_admin(x_admin_key)
    secure = (request.url.scheme == "https"
              or (request.headers.get("x-forwarded-proto") or "").lower() == "https")
    response.set_cookie(_OWNER_COOKIE, _owner_token(), max_age=30 * 24 * 3600,
                        httponly=True, samesite="lax", secure=secure, path="/")
    return {"ok": True, "tools": list(_OWNER_TOOLS)}


@app.post("/api/owner/lock")
def owner_lock(response: Response):
    """(ud) Drop the owner cookie. No key needed: locking yourself out is always allowed."""
    response.delete_cookie(_OWNER_COOKIE, path="/")
    return {"ok": True}


@app.get("/topic")
def topic_page():
    """Topic mode -- pick or name a topic for a focused mini-lesson."""
    return FileResponse(STATIC_DIR / "topic.html")


# (Removed 2026-07-30, market-prep lockdown:)
#   - GET /avatar-lab: an internal 3D-avatar EXPERIMENT was publicly routed; it exposed internal
#     notes and a free-text call to the paid /api/speak endpoint. The route is gone and
#     static/avatar-lab.html is now a small "retired" stub. progress.py's companion route:
#   - GET /api/progress/{code}: served FABRICATED sample stats (progress.py _PROFILES). Verified
#     no page calls it anymore (the dashboard uses the real /api/courses + /api/topics data), so
#     the route and the `import progress` are removed. progress.py itself is now unused and can
#     be deleted from the repo whenever convenient.


@app.get("/privacy")
def privacy_page():
    """Parents & Privacy -- the plain-language privacy commitments (attorney review pending)."""
    return FileResponse(STATIC_DIR / "privacy.html")


@app.get("/terms")
def terms_page():
    """Terms of use, billing and refund basics (attorney review pending)."""
    return FileResponse(STATIC_DIR / "terms.html")


# ---- DISCOVERY FILES (2026-08-02: AI search + Google) -----------------------
# Three tiny files that make the site findable. robots.txt welcomes Google AND the
# AI assistants' crawlers (GPTBot/ClaudeBot/PerplexityBot -- they power ChatGPT/
# Claude/Perplexity recommendations) while hiding the sign-in-only app pages.
# sitemap.xml lists every public page for Google Search Console / Bing Webmaster.
# llms.txt is a plain-text product summary the AI crawlers read directly.
@app.get("/robots.txt")
def robots_txt():
    return FileResponse(STATIC_DIR / "robots.txt", media_type="text/plain")


@app.get("/sitemap.xml")
def sitemap_xml():
    return FileResponse(STATIC_DIR / "sitemap.xml", media_type="application/xml")


@app.get("/llms.txt")
def llms_txt():
    return FileResponse(STATIC_DIR / "llms.txt", media_type="text/plain")


# =============================================================================
# STUDENT REWARDS (2026-07-30) -- merit badges, course trophies, effort awards
# -----------------------------------------------------------------------------
# Three kinds of recognition, ALL computed from data the app already records
# honestly (nothing invented, nothing participation-trophy about it):
#   - MERIT BADGES: one per unit mastered (check >= store.PASS_PCT, i.e. 90%), collected per course.
#   - COURSE TROPHIES: all nine units of a course mastered.
#   - EFFORT AWARDS: streaks, engaged minutes, practice volume, courage
#     (first check), growth (Bounce Back: mastered a unit after failing a
#     check on it), range (Explorer/Pathfinder). Awards PERSIST once earned
#     (store.awards) -- a streak medal survives the streak breaking.
# Design rule (matches the tutor's pedagogy): every award names something the
# student DID -- worked, persisted, came back -- never "you're smart."
AWARD_DEFS = {
    # id: (icon, name, description, family, threshold-or-None)
    "streak3":    ("🔥", "Spark",         "Worked 3 days in a row", "streak", 3),
    "streak7":    ("🔥", "Blaze",         "Worked 7 days in a row", "streak", 7),
    "streak30":   ("🔥", "Unstoppable",   "Worked 30 days in a row", "streak", 30),
    "min100":     ("⏱", "Century Club",   "100 minutes of real work", "minutes", 100),
    "min500":     ("⏱", "500 Club",       "500 minutes of real work", "minutes", 500),
    "min1000":    ("⏱", "Scholar",        "1,000 minutes of real work", "minutes", 1000),
    "prac10":     ("✏️", "First Ten",     "Practiced 10 problems", "practice", 10),
    "prac50":     ("✏️", "Workhorse",     "Practiced 50 problems", "practice", 50),
    "prac100":    ("✏️", "Centurion",     "Practiced 100 problems", "practice", 100),
    "firstcheck": ("🎯", "Brave Start",   "Took your first quiz", "one", None),
    "perfect":    ("💯", "Perfect Quiz",  "Scored 100% on a quiz", "one", None),
    "bounceback": ("💪", "Bounce Back",   "Mastered a unit after a tough first Unit Quiz", "one", None),
    "explorer":   ("🧭", "Explorer",      "Worked in two different courses", "one", None),
    "pathfinder": ("🗺️", "Pathfinder",   "Completed a course assessment", "one", None),
    # 2026-08-07 (Jim): the Final Exam's reward lives in the trophy case (the diploma was
    # removed the same day -- it read like an accredited-school credential, which we are not).
    "champion":   ("🏅", "Course Champion", "Passed a course Final Exam", "one", None),
}


@app.get("/api/awards/{code}")
def awards_state(request: Request, code: str = Depends(_code_dep)):
    """The student's trophy case: course trophies, per-course merit-badge counts, and
    effort awards (persisted once earned). Honest {tracking:false} when the DB is off."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"tracking": False, "trophies": [], "badges": {}, "awards": []}

    trophies, badges = [], {}
    any_check = perfect = bounce = champion = False
    try:
        activity = store.get_course_activity(code)
    except Exception as exc:  # noqa: BLE001
        print(f"[awards] activity failed: {exc}")
        activity = {}
    stats = {}
    for course_id in activity:
        try:
            mastery = store.get_mastery(code, course_id)
        except Exception as exc:  # noqa: BLE001
            print(f"[awards] mastery({course_id}) failed: {exc}")
            continue
        stats = mastery.get("stats") or stats
        checks = mastery.get("checks", {})
        unit_names = dict(curriculum.units_for(course_id))
        mastered_units = []
        for unit, cinfo in checks.items():
            taken = int(cinfo.get("checks_taken") or 0)
            best = int(cinfo.get("best_pct") or 0)
            if taken:
                any_check = True
            if best >= 100:
                perfect = True
            if taken >= 2 and best >= store.PASS_PCT:
                bounce = True
            if best >= store.PASS_PCT:
                mastered_units.append({"unit": unit, "name": unit_names.get(unit, f"Unit {unit}")})
        mastered_units.sort(key=lambda u: u["unit"])
        total_units = len(unit_names) or 9
        badges[course_id] = {"course_title": curriculum.course_title(course_id),
                             "earned": mastered_units, "total": total_units}
        if len(mastered_units) >= total_units:
            trophies.append({"course": course_id, "title": curriculum.course_title(course_id)})
        # 2026-08-07: Course Champion -- passed this course's Final Exam.
        try:
            if (store.get_final_exam(code, course_id) or {}).get("passed"):
                champion = True
        except Exception as exc:  # noqa: BLE001
            print(f"[awards] final({course_id}) failed: {exc}")

    total_minutes = 0
    try:
        total_minutes = sum(r["minutes"] for r in store.get_time(code, days=400))
    except Exception as exc:  # noqa: BLE001
        print(f"[awards] time failed: {exc}")
    streak = int((stats or {}).get("streak_days") or 0)
    practiced = int((stats or {}).get("problems_practiced") or 0)
    placed = any(bool(read_placement(code, cid)) for cid in curriculum.COURSE_ORDER)

    computed = set()
    for aid, (_ic, _nm, _ds, family, threshold) in AWARD_DEFS.items():
        got = ((family == "streak" and streak >= threshold) or
               (family == "minutes" and total_minutes >= threshold) or
               (family == "practice" and practiced >= threshold) or
               (family == "one" and {"firstcheck": any_check, "perfect": perfect,
                                     "bounceback": bounce, "explorer": len(activity) >= 2,
                                     "pathfinder": placed, "champion": champion}[aid]))
        if got:
            computed.add(aid)
    try:
        store.record_awards(code, sorted(computed))
        earned = store.get_awards(code)          # union: persisted awards never un-earn
    except Exception as exc:  # noqa: BLE001
        print(f"[awards] persist failed: {exc}")
        earned = {a: None for a in computed}

    from datetime import datetime, timezone, timedelta
    fresh_cut = datetime.now(timezone.utc) - timedelta(hours=48)
    out = []
    for aid, when in earned.items():
        if aid not in AWARD_DEFS:
            continue
        ic, nm, ds, _f, _t = AWARD_DEFS[aid]
        is_new = False
        try:
            if when:
                dt = datetime.fromisoformat(when)
                if dt.tzinfo is None:            # SQLite returns naive datetimes; treat as UTC
                    dt = dt.replace(tzinfo=timezone.utc)
                is_new = dt >= fresh_cut
        except (ValueError, TypeError):
            pass
        out.append({"id": aid, "icon": ic, "name": nm, "desc": ds,
                    "earned_at": when, "new": is_new})
    order = list(AWARD_DEFS.keys())
    out.sort(key=lambda a: order.index(a["id"]))

    # "Next up" nudges for the tiered families -- the dashboard shows ONE.
    next_up = []
    for family, value, unit_label in (("streak", streak, "day streak"),
                                      ("minutes", total_minutes, "real minutes"),
                                      ("practice", practiced, "problems practiced")):
        tiers = sorted((t, aid) for aid, (_i, _n, _d, f, t) in AWARD_DEFS.items() if f == family)
        for t, aid in tiers:
            if aid not in earned:
                _i, n, _d, _f, _t = AWARD_DEFS[aid]
                next_up.append({"award": n, "icon": _i, "have": value, "need": t, "what": unit_label})
                break
    next_up.sort(key=lambda x: (x["need"] - x["have"]) / max(x["need"], 1))

    return {"tracking": True, "trophies": trophies, "badges": badges,
            "awards": out, "next_up": next_up[:1]}


# -----------------------------------------------------------------------------
# ENGAGED-TIME TRACKING (2026-07-30) -- "how long did my kid actually work?"
# -----------------------------------------------------------------------------
# static/time-tracker.js (on session/practice/topic/challenge) posts a heartbeat
# once a minute ONLY while the tab is visible AND the student did something real
# recently (typed/clicked) -- so leaving the app open does NOT rack up time. The
# server adds its own guard: at most one COUNTED minute per MIN_BEAT_GAP_SECONDS
# per student, so a tampered client can't inflate the clock either.
MIN_BEAT_GAP_SECONDS = 50
_LAST_BEAT: dict = {}
_DAY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@app.post("/api/heartbeat")
def heartbeat(req: HeartbeatRequest):
    """Record one verified minute of engaged time. Returns counted=false (never an
    error) when the beat arrives too soon or tracking is off, so pages never break."""
    _student_or_404(req.code)
    code = req.code.strip()
    _rate_limit("beat:" + code, limit=30, window_seconds=600, what="activity pings")
    now = time.monotonic()
    with _RL_LOCK:
        if now - _LAST_BEAT.get(code, -10 ** 9) < MIN_BEAT_GAP_SECONDS:
            return {"ok": True, "counted": False}
        _LAST_BEAT[code] = now
    day = (req.day or "").strip()
    if not _DAY_RE.match(day):
        day = ""   # bad/missing client date -> store.record_minutes falls back to the server's date
    if not store.enabled():
        return {"ok": True, "counted": False, "tracking": False}
    try:
        store.record_minutes(code, (req.course or "algebra1").strip(), day=day, minutes_add=1)
    except Exception as exc:  # noqa: BLE001
        print(f"[time] record_minutes failed: {exc}")
        return {"ok": True, "counted": False}
    # build il: honest engaged time earns today-bar ticks (Jim's struggling-hour
    # principle) -- checked on the same beat that just counted the minute.
    _today_time_tick(code, (req.course or "algebra1").strip())
    return {"ok": True, "counted": True}


@app.get("/api/time/{code}")
def time_summary(request: Request, code: str = Depends(_code_dep), days: int = 14):
    """Recent engaged time for the dashboard: per-day totals (newest first) with a
    per-course split. The CLIENT computes 'today' / 'this week' against the days
    it recorded, so the student's local calendar stays authoritative."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"tracking": False, "days": []}
    try:
        rows = store.get_time(code, days=max(1, min(int(days), 60)))
    except Exception as exc:  # noqa: BLE001
        print(f"[time] get_time failed: {exc}")
        return {"tracking": False, "days": []}
    agg: dict = {}
    for r in rows:
        d = agg.setdefault(r["day"], {"day": r["day"], "minutes": 0, "courses": {}})
        d["minutes"] += r["minutes"]
        d["courses"][r["course"]] = d["courses"].get(r["course"], 0) + r["minutes"]
    out = sorted(agg.values(), key=lambda x: x["day"], reverse=True)[:days]
    return {"tracking": True, "days": out}


@app.get("/api/topics/{code}")
def topics_state(request: Request, code: str = Depends(_code_dep), course: str = "algebra1"):
    """
    REAL, honest per-topic progress for the dashboard: all of the CHOSEN COURSE's units with
    the student's actual engagement (explored / learning / practiced) or 'not-started'.
    Only meaningful when the database is on (`tracking:true`); otherwise it reports
    tracking is off so the dashboard can say so rather than invent numbers.
    """
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    student = _student_or_404(code)
    code = code.strip()
    placement = read_placement(code, course)
    tracking = store.enabled()

    recorded = {}
    mastery = {"checks": {}, "stats": {}}
    if tracking:
        try:
            for row in store.get_topics(code, course):
                recorded[row["unit"]] = row
        except Exception as exc:  # noqa: BLE001
            print(f"[topics] get_topics failed: {exc}")
        try:
            mastery = store.get_mastery(code, course)
        except Exception as exc:  # noqa: BLE001
            print(f"[topics] get_mastery failed: {exc}")

    quiz_rows = {}
    if tracking:
        try:
            for q in store.get_topic_quizzes(code, course):
                quiz_rows.setdefault(q["unit"], []).append({
                    "name": q["topic_name"], "best_pct": q["best_pct"],
                    "passed": q["best_pct"] >= store.QUIZ_PASS_PCT})
        except Exception as exc:  # noqa: BLE001
            print(f"[topics] get_topic_quizzes failed: {exc}")

    checks = mastery.get("checks", {})
    lessons = _lessons_by_unit(code, course)      # (ue) lessons done, per unit
    units = []
    for n, name in curriculum.units_for(course):
        r = recorded.get(n)
        c = checks.get(n) or {}
        best = int(c.get("best_pct") or 0)
        uq = quiz_rows.get(n, [])
        lu = lessons.get(n) or {"done": 0, "total": 0}
        units.append({
            "unit": n,
            "name": name,
            "status": (r["status"] if r else "not-started"),
            "touches": (r["touches"] if r else 0),
            "last_touched": (r.get("last_touched") if r else None),
            "best_pct": best,                       # best UNIT QUIZ score (0 if none)
            "checks_taken": int(c.get("checks_taken") or 0),
            "mastered": best >= store.PASS_PCT,     # the 90% Unit Quiz, and nothing else
            "quizzes": uq,                          # topic-quiz rows: {name, best_pct, passed}
            "quizzes_passed": len([q for q in uq if q["passed"]]),
            "lessons_done": lu["done"],             # (ue) finished authored lessons
            "lessons_total": lu["total"],
        })

    started = [u for u in units if u["status"] != "not-started"]
    summary = {
        "units_started": len(started),
        "units_total": len(units),
        "units_mastered": len([u for u in units if u["mastered"]]),
        "total_touches": sum(u["touches"] for u in units),
        "last_active": max([u["last_touched"] for u in started if u["last_touched"]], default=None),
        "stats": mastery.get("stats", {}),          # problems_practiced, accuracy_pct, streak_days
    }
    return {
        "name": student.get("name"),
        "tracking": tracking,
        "placement": placement,
        "units": units,
        "summary": summary,
    }


# =============================================================================
# TEACHER / PARENT CLASSROOM (2026-07-28)
# -----------------------------------------------------------------------------
# A "class" groups EXISTING student codes under a short class code, so a teacher or parent can
# watch several students at once. This is deliberately NOT an accounts system: there is no
# password and no new personal data -- the class code is just a convenience key, and every
# student code added must ALREADY exist in students.json. The roster lives in the database
# (`classes` / `class_members`); when the DB is off these endpoints report tracking:false
# instead of failing, exactly like the rest of the tracking layer.
# =============================================================================
# ⛔ _class_or_404 was REMOVED in build fa. It fetched a class by code with no ownership
# check at all, and it was the helper every leaking endpoint reached for. `_own_class`
# replaces it everywhere. Leaving a ready-made no-auth lookup in the file would invite
# the next handler to use it -- the same reasoning that retired challenge.html's postJSON.


def _safe_goal(code: str):
    """(sb) get_practice_goal that never raises -- roster rows are best-effort."""
    try:
        return store.get_practice_goal(code)
    except Exception:  # noqa: BLE001
        return None


def _class_student_row(code: str, course: str, class_code: str = "") -> dict:
    """One student's snapshot for the classroom view: per-unit best scores + a small summary.
    Mirrors what /api/topics reports, but trimmed to what a roster grid needs. Never raises --
    a student whose data can't be read still appears in the grid (with zeros)."""
    student = _lookup_student(code) or {}     # build fb: parent-created students too
    checks, stats, recorded = {}, {}, {}
    try:
        m = store.get_mastery(code, course)
        checks = m.get("checks", {}) or {}
        stats = m.get("stats", {}) or {}
    except Exception as exc:  # noqa: BLE001
        print(f"[class] get_mastery failed for {code}: {exc}")
    try:
        for row in store.get_topics(code, course):
            recorded[row["unit"]] = row
    except Exception as exc:  # noqa: BLE001
        print(f"[class] get_topics failed for {code}: {exc}")

    units = []
    for n, name in curriculum.units_for(course):
        c = checks.get(n) or {}
        r = recorded.get(n)
        best = int(c.get("best_pct") or 0)
        units.append({
            "unit": n,
            "name": name,
            "best_pct": best,
            "checks_taken": int(c.get("checks_taken") or 0),
            "mastered": best >= store.PASS_PCT,
            "status": (r["status"] if r else "not-started"),
        })
    started = [u for u in units if u["status"] != "not-started" or u["checks_taken"]]
    # FOUNDATION-FIRST, matching the Course Assessment's recommended path: the units to work on
    # are listed in COURSE ORDER (earliest gap first), NOT weakest-first -- a shaky Unit 1 gets
    # attention before a shaky Unit 9, because the later units build on it.
    weak = [u for u in units if u["checks_taken"] and not u["mastered"]]
    last = [r.get("last_touched") for r in recorded.values() if r.get("last_touched")]
    return {
        # build fa: the grid identifies a child by an opaque ref and a MASKED code. It
        # used to carry the raw login code for every student in the class -- the single
        # richest thing finding F2 exposed. `class_code` is passed in purely to key the ref.
        "ref": _member_ref(class_code, code) if class_code else "",
        "code_masked": _mask_code(code),
        "name": student.get("name") or _mask_code(code),
        "known": bool(student),           # False = the code isn't in students.json (typo?)
        "units": units,
        "units_mastered": len([u for u in units if u["mastered"]]),
        "units_started": len(started),
        # (sb) the standing practice goal, for the roster row's control -- minutes,
        # kind and today's ring only, never anything that identifies the code.
        "goal": (lambda g: {"minutes": g["minutes"], "kind": g["kind"],
                            "target": g["target"], "today_done": g["today_done"]}
                 if g else None)(_safe_goal(code)),
        "weakest": [{"unit": u["unit"], "name": u["name"], "best_pct": u["best_pct"]}
                    for u in weak[:3]],
        "last_active": (max(last) if last else None),
        "stats": stats,
    }


# =============================================================================
# TEACHER ACCOUNTS (2026-08-13, build fa) -- SECURITY FINDING F2, CLOSED
# -----------------------------------------------------------------------------
# WHAT WAS WRONG, stated plainly because it was serious: every class endpoint was
# UNAUTHENTICATED. GET /api/class/{code} returned the whole roster INCLUDING every
# child's login code -- and a student code IS the login (students have no password).
# So one guessed class code handed over every child in that class: their codes,
# their progress, their transcripts. Those routes never got F1's _read_guard either,
# so they were enumerable AND unthrottled. The old "teacher code" was documented in
# this file as "a door, not a lock", and it was exactly that.
#
# THE FIX: real teacher accounts, mirroring the parent stack (same PBKDF2 hashing,
# same 30-day token, same single-use email reset), with a separate table so the live
# parent/billing path is untouched. A class now has an OWNER (classes.teacher_id) and
# every read and every write checks it.
#
# WHAT HAPPENS TO CLASSES THAT ALREADY EXIST (Jim's call, 2026-08-13): nothing is
# deleted and nothing is orphaned. They start UNOWNED, and a teacher takes ownership
# either by entering their old teacher code at signup (inherits every class carrying
# it) or by claiming a class by its code while signed in. An UNOWNED class can be
# claimed exactly once; an OWNED class can never be re-claimed, by either path.
#
# ROSTER CODES (Jim's call): the roster no longer ships raw student codes. Each row
# carries a masked code and an opaque `ref`; the owning teacher can reveal ONE code
# at a time through its own endpoint. A projected or screenshotted roster no longer
# leaks thirty children's logins at once.
# =============================================================================
def _require_teacher(token: str) -> dict:
    """Validate a teacher token and return the teacher row (sans password hash)."""
    _require_db()
    teacher_id = store.get_teacher_token((token or "").strip())
    if not teacher_id:
        raise HTTPException(status_code=401, detail="Please sign in again.")
    teacher = store.get_teacher(teacher_id)
    if not teacher:
        raise HTTPException(status_code=401, detail="Please sign in again.")
    teacher.pop("password_hash", None)      # never let the hash near a response
    return teacher


def _own_class(teacher: dict, class_code: str) -> dict:
    """Return the class ONLY if this teacher owns it. The single chokepoint every
    class endpoint goes through -- the ownership rule lives in one place so it cannot
    drift between five handlers.

    A class that exists but belongs to someone else answers 404, not 403: telling a
    stranger "that class exists, it just isn't yours" is a membership oracle, and this
    endpoint family was an enumeration target to begin with."""
    cls = store.get_class((class_code or "").strip())
    if not cls or (cls.get("teacher_id") or "") != teacher["id"]:
        raise HTTPException(status_code=404, detail="No class with that code on your account.")
    return cls


def _member_ref(class_code: str, student_code: str) -> str:
    """A stable, opaque handle for one roster row, so the roster can be rendered and
    edited WITHOUT shipping children's login codes to the page. Not a credential --
    every endpoint that takes a ref is owner-gated anyway; it exists so the codes
    themselves stay off the screen and out of the payload."""
    raw = f"{_norm_class_code(class_code)}|{(student_code or '').strip()}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def _norm_class_code(cc: str) -> str:
    return (str(cc or "").strip().upper())[:32]


def _mask_code(code: str) -> str:
    """MAPLE4821 -> MAPLE••••. Enough for a teacher to recognise a row at a glance,
    useless to somebody reading over their shoulder or looking at a screenshot."""
    c = (code or "").strip()
    if len(c) <= 4:
        return "•" * len(c)
    keep = max(2, len(c) - 4)
    return c[:keep] + "•" * (len(c) - keep)


def _resolve_member(cls: dict, ref_or_code: str) -> str:
    """Turn a roster `ref` (or, for older callers, a raw student code) into the student
    code that is actually IN this class. Returns "" when it matches no member -- so a
    remove can only ever touch this class's own roster."""
    want = (ref_or_code or "").strip()
    for code in cls.get("students", []):
        if want == _member_ref(cls["class_code"], code) or want == code:
            return code
    return ""


def _class_public(cls: dict) -> dict:
    """The class as a page may see it: the roster carries NAMES and MASKED codes plus an
    opaque ref, never a child's raw login code, and the owner id never leaves the server.
    Build fa -- this shape is the whole point of finding F2's fix, so it lives in ONE
    function that every class response goes through."""
    roster = []
    for c in (cls.get("students") or []):
        # build fb: _lookup_student, NOT STUDENTS. The class path predated parent
        # accounts and only ever knew students.json -- so every child a real parent
        # created showed here as an "unknown code" with no name. Found by the
        # full-journey trial.
        stu = _lookup_student(c) or {}
        # (sb) the standing practice goal, visible on the roster row -- minutes,
        # kind and today's ring only; never the child's code, same as everything
        # else in this shape.
        goal = None
        try:
            g = store.get_practice_goal(c)
            if g:
                goal = {"minutes": g["minutes"], "kind": g["kind"],
                        "target": g["target"], "today_done": g["today_done"]}
        except Exception:  # noqa: BLE001
            pass
        roster.append({
            "ref": _member_ref(cls.get("class_code", ""), c),
            "name": stu.get("name") or _mask_code(c),
            "code_masked": _mask_code(c),
            "known": bool(stu),
            "goal": goal,
        })
    return {"class_code": cls.get("class_code", ""), "name": cls.get("name") or "",
            "owner_name": cls.get("owner_name") or "", "roster": roster}


def _teacher_payload(teacher: dict) -> dict:
    """The signed-in teacher + their classes. One place, so signup, login and refresh
    all return exactly the same shape (the parent stack's _parent_payload lesson)."""
    return {
        "ok": True,
        "teacher": {"id": teacher["id"], "email": teacher.get("email") or "",
                    "name": teacher.get("name") or "", "school": teacher.get("school") or ""},
        "classes": store.list_classes_for_teacher_id(teacher["id"]),
    }


@app.post("/api/teacher/signup")
def teacher_signup(body: TeacherSignupIn, request: Request):
    """Create a teacher account. Free, no card. If they give the teacher code they used
    before accounts existed, every UNOWNED class carrying it becomes theirs."""
    _require_db()
    _rate_limit("tsignup:" + _client_ip(request), limit=5, window_seconds=3600,
                what="signup attempts")
    email = (body.email or "").strip().lower()
    if not _EMAIL_RE.match(email):
        raise HTTPException(status_code=400, detail="That doesn't look like an email address.")
    if len(body.password or "") < 8:
        raise HTTPException(status_code=400, detail="Please use a password of at least 8 characters.")
    teacher_id = uuid.uuid4().hex
    if not store.create_teacher(teacher_id, email, body.name, _hash_password(body.password),
                                body.school or ""):
        raise HTTPException(status_code=409, detail=(
            "That email already has a teacher account — use Sign in instead."))
    adopted = 0
    if (body.teacher_code or "").strip():
        adopted = store.adopt_classes_by_teacher_code(body.teacher_code, teacher_id)
    out = _teacher_payload(store.get_teacher(teacher_id))
    out["token"] = _issue_teacher_token(teacher_id)
    out["adopted"] = adopted
    return out


@app.post("/api/teacher/login")
def teacher_login(body: TeacherLoginIn, request: Request):
    _require_db()
    _rate_limit("tlogin:" + _client_ip(request), limit=20, window_seconds=300,
                what="sign-in attempts")
    teacher = store.get_teacher_by_email(body.email)
    # Verify against a real or dummy hash either way, so a wrong email and a wrong
    # password take the same time (no probing which addresses have accounts).
    stored = teacher["password_hash"] if teacher else _hash_password("timing-decoy")
    if not _verify_password(body.password, stored) or not teacher:
        raise HTTPException(status_code=401, detail="Email or password didn't match.")
    out = _teacher_payload(teacher)
    out["token"] = _issue_teacher_token(teacher["id"])
    return out


@app.post("/api/teacher/logout")
def teacher_logout(body: TeacherTokenIn):
    if store.enabled():
        store.delete_teacher_token((body.token or "").strip())
    return {"ok": True}


@app.get("/api/teacher/me")
def teacher_me(request: Request):
    """The signed-in teacher and their classes. Token in the X-Teacher-Token header."""
    teacher = _require_teacher(request.headers.get("x-teacher-token", ""))
    return _teacher_payload(teacher)


@app.post("/api/teacher/claim")
def teacher_claim(body: TeacherClaimIn):
    """Take ownership of an UNOWNED class by its code. The race and the
    already-owned case are both settled inside store.claim_class, in one transaction."""
    teacher = _require_teacher(body.token)
    why = store.claim_class(body.class_code, teacher["id"])
    if why:
        raise HTTPException(status_code=409, detail=why)
    out = _teacher_payload(teacher)
    out["claimed"] = _norm_class_code(body.class_code)
    return out


@app.post("/api/teacher/forgot")
def teacher_forgot(body: TeacherForgotIn, request: Request):
    """Email a password-reset link. SAME answer whether or not the address has an
    account. Single-use, 45 minutes, only the SHA-256 hash is stored. Mirrors the
    parent flow exactly, including its anti-probing behaviour."""
    _require_db()
    _rate_limit("tforgot:" + _client_ip(request), limit=5, window_seconds=3600,
                what="reset requests")
    email = (body.email or "").strip().lower()
    if not _EMAIL_RE.match(email):
        raise HTTPException(status_code=400, detail="That doesn't look like an email address.")
    _rate_limit("tforgot-email:" + email, limit=3, window_seconds=3600,
                what="reset requests")
    if not _smtp_configured():
        return {"ok": True, "sent": False,
                "note": ("Email isn't switched on here yet — write to support@mrcadabra.com "
                         "and we'll reset it for you.")}
    teacher = store.get_teacher_by_email(email)
    if not teacher:
        print("[email] teacher forgot: no account matches that address -- no email sent")
    if teacher:
        raw = secrets.token_urlsafe(32)
        token_hash = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        store.create_teacher_reset(token_hash, teacher["id"], minutes=45)
        base = os.environ.get("APP_BASE_URL", "https://mrcadabra.com").rstrip("/")
        link = f"{base}/teacher?reset={raw}"
        send_err = _send_email(email, "Reset your Mr. Cadabra's Classroom teacher password",
            "Hi" + ((" " + teacher.get("name")) if teacher.get("name") else "") + ",\n\n"
            "Someone asked to reset the password for this Mr. Cadabra's Classroom teacher "
            "account. If that was you, open this link and choose a new password:\n\n"
            f"{link}\n\n"
            "The link works once and expires in 45 minutes.\n\n"
            "If you didn't ask for this, you can safely ignore this email — your password "
            "is unchanged and your classes are unaffected.\n\n"
            "— Mr. Cadabra's Classroom\nsupport@mrcadabra.com")
        if send_err:
            print(f"[email] teacher forgot: send FAILED for a real account: {send_err}")
    return {"ok": True, "sent": True}


@app.post("/api/teacher/reset")
def teacher_reset(body: TeacherResetIn):
    """Spend a reset token and set a new password. Every existing session is signed
    out, so a stolen token cannot outlive the reset."""
    _require_db()
    if len(body.password or "") < 8:
        raise HTTPException(status_code=400, detail="Please use a password of at least 8 characters.")
    token_hash = hashlib.sha256((body.token or "").encode("utf-8")).hexdigest()
    teacher_id = store.use_teacher_reset(token_hash)
    if not teacher_id:
        raise HTTPException(status_code=400, detail=(
            "That reset link has expired or was already used. Please request a new one."))
    store.set_teacher_password(teacher_id, _hash_password(body.password))
    store.delete_teacher_tokens_for(teacher_id)
    out = _teacher_payload(store.get_teacher(teacher_id))
    out["token"] = _issue_teacher_token(teacher_id)
    return out


def _issue_teacher_token(teacher_id: str) -> str:
    token = secrets.token_hex(32)
    store.create_teacher_token(token, teacher_id, days=30)
    return token


@app.post("/api/class")
def post_class(body: ClassIn):
    """Create a class, or update its label if you already own it.

    build fa: creating a class now REQUIRES a signed-in teacher, and the new class is
    owned by them from its first moment. Updating one you do not own is a 404 (see
    _own_class) -- previously ANY caller could rename ANY class, or quietly attach
    their own teacher code to it."""
    teacher = _require_teacher(body.token)
    cc = (body.class_code or "").strip()
    if not cc:
        raise HTTPException(status_code=400, detail="Please choose a class code.")
    existing = store.get_class(cc)
    if existing:
        _own_class(teacher, cc)             # yours to edit, or it does not exist to you
    cls = store.create_class(cc, body.name or "", body.owner_name or "",
                             body.teacher_code or "")
    if not existing:
        store.claim_class(cc, teacher["id"])    # brand new: owned from birth
    return {"ok": True, "tracking": True, "klass": _class_public(store.get_class(cc))}


# ⛔ REMOVED in build fa: GET /api/teacher/{teacher_code}/classes.
# It listed every class run by a teacher code, unauthenticated, and its own docstring
# admitted what it was: "a teacher code is a convenience key, not a password... This is a
# door, not a lock." A short, guessable, unthrottled key is not an acceptable way to reach
# a roster of children. Its replacement is GET /api/teacher/me, behind a real token.
# The teacher code itself survives ONLY as an inheritance hint at signup (build fa).


@app.get("/api/class/{class_code}")
def get_class_info(class_code: str, request: Request,
                   x_teacher_token: str = Header(default="", alias="X-Teacher-Token")):
    """The class label plus its roster -- OWNER ONLY (build fa, finding F2).

    The roster carries names, MASKED codes and opaque refs; a child's real login code is
    never in this response. Use /api/class/{code}/reveal/{ref} for one code at a time.
    _read_guard still fronts it, so even a signed-in account cannot sweep class codes."""
    teacher = _require_teacher(x_teacher_token)
    _read_guard(request, class_code)        # defence in depth: no enumeration, ever
    cls = _own_class(teacher, class_code)
    return {"ok": True, "tracking": True, "klass": _class_public(cls)}


@app.get("/api/class/{class_code}/reveal/{ref}")
def reveal_class_student_code(class_code: str, ref: str, request: Request,
                              x_teacher_token: str = Header(default="", alias="X-Teacher-Token")):
    """Reveal ONE student's login code to the owning teacher (build fa, Jim's call).

    A teacher genuinely needs a code sometimes -- to hand it back to a child who has lost
    it -- and they typed it in the first place to build the roster, so this is not new
    exposure to them. What it stops is thirty codes sitting on a projected screen at once.
    Deliberately one at a time, owner-gated, and throttled."""
    teacher = _require_teacher(x_teacher_token)
    _rate_limit("reveal:" + teacher["id"], limit=40, window_seconds=300,
                what="code reveals")
    cls = _own_class(teacher, class_code)
    code = _resolve_member(cls, ref)
    if not code:
        raise HTTPException(status_code=404, detail="That student isn't in this class.")
    return {"ok": True, "code": code}


@app.post("/api/class/{class_code}/students")
def post_class_student(class_code: str, body: ClassStudentIn,
                       x_teacher_token: str = Header(default="", alias="X-Teacher-Token")):
    """Add an EXISTING student code to the class -- OWNER ONLY (build fa). Unknown codes
    are rejected with a clear message so a teacher sees their typo instead of a silently
    empty row."""
    teacher = _require_teacher(x_teacher_token or body.token)
    _own_class(teacher, class_code)
    code = (body.code or "").strip()
    if not code:
        raise HTTPException(status_code=400, detail="Please enter a student code.")
    # build fb: a teacher must be able to add ANY real student -- including the ones a
    # parent created, which is every real customer's child. This checked students.json
    # alone, so a valid parent-made code was rejected as "no student with that code".
    if not _lookup_student(code):
        raise HTTPException(status_code=404,
                            detail=f"No student with the code '{code}'. Check the code and try again.")
    store.add_student(class_code, code)
    return {"ok": True, "tracking": True}


@app.delete("/api/class/{class_code}/students/{ref}")
def delete_class_student(class_code: str, ref: str,
                         x_teacher_token: str = Header(default="", alias="X-Teacher-Token")):
    """Remove a student from the class -- OWNER ONLY (build fa). The student's own
    progress is NOT deleted. Takes the roster `ref` (a raw code still works for older
    callers); either way _resolve_member confirms the student is in THIS class first, so
    a remove can never reach outside the roster in front of you."""
    teacher = _require_teacher(x_teacher_token)
    cls = _own_class(teacher, class_code)
    code = _resolve_member(cls, ref)
    if not code:
        raise HTTPException(status_code=404, detail="That student isn't in this class.")
    store.remove_student(class_code, code)
    return {"ok": True, "tracking": True}


class ClassGoalIn(BaseModel):
    ref: str = ""              # the roster ref (a raw code still resolves)
    minutes: int = 0           # 5-60 sets the goal; 0 clears it
    kind: str = "general"      # "general" | "latest"


@app.post("/api/class/{class_code}/goal")
def post_class_goal(class_code: str, body: ClassGoalIn,
                    x_teacher_token: str = Header(default="", alias="X-Teacher-Token")):
    """Set or clear ONE student's daily practice goal -- OWNER ONLY (build sb,
    the teacher door of Jim's 2026-09-02 design; /api/parent/student-goal is the
    parent door, and both run the same _set_goal_checked validation so the two
    portals cannot drift). Takes the roster ref; _resolve_member confirms the
    student is in THIS class first, exactly like remove."""
    teacher = _require_teacher(x_teacher_token)
    cls = _own_class(teacher, class_code)
    code = _resolve_member(cls, body.ref)
    if not code:
        raise HTTPException(status_code=404, detail="That student isn't in this class.")
    _set_goal_checked(code, body.minutes, body.kind, "class:" + (class_code or "").strip())
    g = store.get_practice_goal(code)
    return {"ok": True, "goal": ({"minutes": g["minutes"], "kind": g["kind"],
                                  "target": g["target"],
                                  "today_done": g["today_done"]} if g else None)}


@app.get("/api/class/{class_code}/summary")
def get_class_summary(class_code: str, request: Request, course: str = "algebra1",
                      x_teacher_token: str = Header(default="", alias="X-Teacher-Token")):
    """THE CLASSROOM VIEW: every student in the class with their per-unit mastery for ONE
    course, plus class-wide aggregates (which units the class as a whole is weakest on).
    OWNER ONLY since build fa -- this is the richest view of children's data in the app."""
    teacher = _require_teacher(x_teacher_token)
    _read_guard(request, class_code)
    cls = _own_class(teacher, class_code)
    students = [_class_student_row(c, course, cls["class_code"])
                for c in cls.get("students", [])]
    unit_names = curriculum.units_for(course)

    # Class-wide per-unit picture: how many students have mastered each unit, and the average
    # best score among those who have actually been checked on it.
    per_unit = []
    for n, name in unit_names:
        scored = [s for s in students
                  if next((u for u in s["units"] if u["unit"] == n), {}).get("checks_taken")]
        mastered = [s for s in students
                    if next((u for u in s["units"] if u["unit"] == n), {}).get("mastered")]
        avg = None
        if scored:
            avg = round(sum(next(u for u in s["units"] if u["unit"] == n)["best_pct"]
                            for s in scored) / len(scored))
        per_unit.append({"unit": n, "name": name, "assessed": len(scored),
                         "mastered": len(mastered), "avg_best_pct": avg})

    needs_help = sorted([p for p in per_unit if p["assessed"]],
                        key=lambda p: (p["avg_best_pct"] if p["avg_best_pct"] is not None else 999))
    return {
        "ok": True,
        "tracking": True,
        "klass": {"class_code": cls["class_code"], "name": cls.get("name", ""),
                  "owner_name": cls.get("owner_name", "")},
        "course": course,
        "course_title": curriculum.course_title(course),
        "units": [{"unit": n, "name": nm} for n, nm in unit_names],
        "students": students,
        "per_unit": per_unit,
        "needs_help": needs_help[:3],
        "class_size": len(students),
    }


# =============================================================================
# PARENT ACCOUNTS (2026-07-31) -- real signups, the payments foundation
# -----------------------------------------------------------------------------
# A parent signs up with email + password, adds children (FIRST names only), and
# each child gets a friendly login code -- the same kind of code the app has
# always used, so nothing about the student experience changes. Passwords are
# never stored or logged: only a salted PBKDF2-SHA256 hash (390k iterations,
# per-account random salt, constant-time comparison). Sign-in hands out a random
# 30-day token; every parent API call presents that token, never the password.
# All of it REQUIRES the database -- an accounts system must not live in
# throwaway JSON files that vanish on redeploy, so without DATABASE_URL these
# endpoints answer 503 with a clear message instead of pretending.
# =============================================================================

_PBKDF2_ITERATIONS = 390_000
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Kid-friendly words for student login codes (short, unambiguous, easy to say
# out loud). A code looks like MAPLE42. ~50 words x 90 numbers = 4500 combos,
# and we re-roll on collision, so exhaustion is not a concern at this scale.
_CODE_WORDS = [
    "MAPLE", "RIVER", "TIGER", "COMET", "EAGLE", "PIANO", "ROCKET", "PANDA",
    "OTTER", "ACORN", "BADGE", "CEDAR", "DELTA", "EMBER", "FALCON", "GECKO",
    "HARBOR", "IGLOO", "JUNIPER", "KOALA", "LANTERN", "MARBLE", "NUTMEG",
    "ORBIT", "PEBBLE", "QUARTZ", "ROBIN", "SIERRA", "TUNDRA", "UMBER",
    "VIOLET", "WALNUT", "YONDER", "ZEPHYR", "ASPEN", "BREEZE", "CANYON",
    "DUNE", "FERN", "GLACIER", "HAZEL", "INDIGO", "JASPER", "KESTREL",
    "LAGOON", "MESA", "NEBULA", "ONYX", "PRAIRIE", "SUMMIT",
]


def _hash_password(password: str) -> str:
    """Salted PBKDF2-SHA256. The stored string carries its own parameters so the
    iteration count can be raised later without breaking old hashes."""
    salt = secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"),
                             bytes.fromhex(salt), _PBKDF2_ITERATIONS)
    return f"pbkdf2_sha256${_PBKDF2_ITERATIONS}${salt}${dk.hex()}"


def _verify_password(password: str, stored: str) -> bool:
    try:
        algo, iters, salt, want = (stored or "").split("$", 3)
        if algo != "pbkdf2_sha256":
            return False
        dk = hashlib.pbkdf2_hmac("sha256", (password or "").encode("utf-8"),
                                 bytes.fromhex(salt), int(iters))
        return hmac.compare_digest(dk.hex(), want)
    except (ValueError, TypeError):
        return False


def _require_db() -> None:
    if not store.enabled():
        raise HTTPException(status_code=503, detail=(
            "Family accounts need the database, which isn't connected right now. "
            "Please try again shortly or email support@mrcadabra.com."))


def _require_parent(token: str) -> dict:
    """Validate a parent token and return the parent row (sans password hash)."""
    _require_db()
    parent_id = store.get_parent_token((token or "").strip())
    if not parent_id:
        raise HTTPException(status_code=401, detail="Please sign in again.")
    parent = store.get_parent(parent_id)
    if not parent:
        raise HTTPException(status_code=401, detail="Please sign in again.")
    parent.pop("password_hash", None)   # never let the hash near a response
    return parent


def _new_student_code() -> str:
    """A fresh, friendly student code (e.g. MAPLE4821) that collides with nothing:
    not the pilot codes in students.json, not any existing account.

    WIDENED (build ed, 2026-08-12 -- finding F1): the digit block went 2 -> 4 digits,
    so the space is 50 words x 9000 = 450,000 (was 4,500) -- a ~100x jump that makes
    guessing a valid code infeasible even before the read-throttle. Still one short
    word + a number, so it's just as easy for a child to read and type. Existing
    2-digit codes keep working untouched -- nothing validates the digit count; this
    only changes what NEW codes look like."""
    for _ in range(60):
        code = f"{secrets.choice(_CODE_WORDS)}{secrets.randbelow(9000) + 1000}"
        if code in STUDENTS:
            continue
        if store.get_account(code):
            continue
        return code
    return f"STAR{secrets.token_hex(3).upper()}"   # astronomically unlikely fallback


def _issue_token(parent_id: str) -> str:
    token = secrets.token_hex(32)
    store.create_parent_token(token, parent_id, days=30)
    return token


# FAMILY PLAN (2026-08-03): one paid "seat" covers up to this many children, so a
# parent adding a SECOND child pays nothing more; the THIRD child needs a second
# seat, and so on in pairs. Change this one number to change the family policy.
# Oldest children are always covered first (see _student_tier), so buying fewer
# seats never bumps a currently-covered child to Free.
KIDS_PER_SEAT = 2


def _seats_for(n_children: int) -> int:
    """How many paid Stripe seats cover this many children (in pairs, rounded up).
    0 children -> 0 seats, 1 or 2 -> 1 seat, 3 or 4 -> 2 seats, and so on."""
    n = max(0, int(n_children or 0))
    return (n + KIDS_PER_SEAT - 1) // KIDS_PER_SEAT


def _covered_count(seats: int) -> int:
    """How many children `seats` paid seats cover (the inverse of _seats_for)."""
    return max(0, int(seats or 0)) * KIDS_PER_SEAT


def _parent_payload(parent: dict) -> dict:
    """The parent + family picture the /family page renders. One place, so signup,
    login, and refresh all return exactly the same shape."""
    students = store.list_students_for_parent(parent["id"])
    quantity = int(parent.get("sub_quantity") or 0)
    period_end = parent.get("sub_period_end")
    if period_end is not None and getattr(period_end, "tzinfo", None) is None:
        import datetime as _dt2                      # SQLite returns naive datetimes
        period_end = period_end.replace(tzinfo=_dt2.timezone.utc)
    return {
        "ok": True,
        "parent": {"email": parent.get("email"), "name": parent.get("name") or ""},
        "subscription": {
            "status": parent.get("sub_status") or "free",
            "plan": parent.get("sub_plan") or "",
            "quantity": quantity,
            "period_end": period_end.isoformat() if period_end else None,
        },
        "students": [{
            "code": s["code"],
            "name": s.get("name") or "Student",
            "covered": (parent.get("sub_status") == "active"
                        and i < _covered_count(quantity)),
        } for i, s in enumerate(students)],
        "billing_ready": _payments_open(),
    }


def _student_tier(code: str, student: dict) -> str:
    """What level of access does this student have RIGHT NOW?
      'pilot' -- a students.json persona (full access, unchanged forever)
      'full'  -- parent-managed, and the parent's subscription covers them
      'free'  -- parent-managed on the Free plan (placement + first unit + practice)
    Coverage is the parent's live sub_status + paid quantity: the OLDEST students
    are covered first, so adding a new child never bumps a paying child to free."""
    if not student.get("family"):
        return "pilot"
    try:
        parent = store.get_parent(student.get("parent_id") or "")
        if parent and (parent.get("sub_status") or "") == "active":
            quantity = int(parent.get("sub_quantity") or 0)
            kids = store.list_students_for_parent(parent["id"])
            for i, kid in enumerate(kids):
                if kid["code"] == code:
                    return "full" if i < _covered_count(quantity) else "free"
    except Exception as exc:  # noqa: BLE001 -- a billing lookup must never crash a lesson
        print(f"[tier] lookup failed for {code}: {exc}")
    return "free"


def _free_gate(code: str, student: dict, course: str):
    """The Free plan's promise, enforced kindly: one placement + a FIRST unit to
    try + unlimited practice & topic help. Lessons (session mode) stay open until
    the student has MASTERED one unit anywhere; after that, continuing lessons
    needs the Full plan. Returns None (allowed) or a warm message (blocked) --
    and the block happens BEFORE any paid Claude call."""
    if _student_tier(code, student) != "free":
        return None
    try:
        activity = store.get_course_activity(code)
        mastered = sum(int(v.get("units_mastered") or 0) for v in (activity or {}).values())
    except Exception as exc:  # noqa: BLE001
        print(f"[tier] activity lookup failed for {code}: {exc}")
        return None            # if we can't tell, do no harm: let the lesson through
    if mastered < 1:
        return None
    first = (student.get("name") or "there").split()[0]
    return (f"{first}, you did it — you mastered your first unit with me, and that's the whole "
            "free preview! I'd love to keep teaching you. Ask your parent to open the Family "
            "page at mrcadabra.com/family and upgrade your account — then we'll pick up right "
            "here where we left off. (Your Practice and Explore-a-topic tools still work "
            "anytime, free.)")


@app.post("/api/parent/signup")
def parent_signup(body: ParentSignupIn, request: Request):
    """Create a parent account. Free plan, no card, instant."""
    _require_db()
    _rate_limit("psignup:" + _client_ip(request), limit=5, window_seconds=3600,
                what="signup attempts")
    email = (body.email or "").strip().lower()
    if not _EMAIL_RE.match(email):
        raise HTTPException(status_code=400, detail="That doesn't look like an email address.")
    if len(body.password or "") < 8:
        raise HTTPException(status_code=400, detail="Please use a password of at least 8 characters.")
    parent_id = uuid.uuid4().hex
    if not store.create_parent(parent_id, email, body.name, _hash_password(body.password)):
        raise HTTPException(status_code=409, detail=(
            "That email already has an account — use Sign in instead."))
    token = _issue_token(parent_id)
    out = _parent_payload(store.get_parent(parent_id))
    out["token"] = token
    return out


@app.post("/api/parent/login")
def parent_login(body: ParentLoginIn, request: Request):
    _require_db()
    _rate_limit("plogin:" + _client_ip(request), limit=20, window_seconds=300,
                what="sign-in attempts")
    parent = store.get_parent_by_email(body.email)
    # Verify against a real or dummy hash either way, so a wrong email and a wrong
    # password take the same time (no probing which emails have accounts).
    stored = parent["password_hash"] if parent else _hash_password("timing-decoy")
    if not _verify_password(body.password, stored) or not parent:
        raise HTTPException(status_code=401, detail="Email or password didn't match.")
    token = _issue_token(parent["id"])
    out = _parent_payload(parent)
    out["token"] = token
    return out


# -----------------------------------------------------------------------------
# OUTBOUND EMAIL (2026-08-04) -- the app's first sender: password-reset links.
# Uses the EXISTING Titan mailbox over SMTP (no new service, no new cost); the
# same pipe will later carry the weekly parent email. Configure in Render:
#   SMTP_HOST=smtp.titan.email  SMTP_PORT=465
#   SMTP_USER=support@mrcadabra.com  SMTP_PASS=<mailbox password>
#   (optional SMTP_FROM, defaults to SMTP_USER; APP_BASE_URL, defaults below)
# -----------------------------------------------------------------------------
def _smtp_configured() -> bool:
    return bool(os.environ.get("SMTP_HOST") and os.environ.get("SMTP_USER")
                and os.environ.get("SMTP_PASS"))


def _send_email(to_addr: str, subject: str, body: str, attachment=None) -> str:
    """Send one plain-text email. Returns "" on success or the exact failure text
    on error; never raises (a mail hiccup must never 500 an API call). Secrets
    come from env only, and the failure text NEVER includes them.
    build hv: optional `attachment=(filename, bytes)` -- the weekly off-site
    backup rides this; everything else keeps the plain-text path unchanged."""
    if not _smtp_configured():
        return "SMTP env vars not set (need SMTP_HOST, SMTP_USER, SMTP_PASS)"
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    host = os.environ["SMTP_HOST"]
    port = int(os.environ.get("SMTP_PORT", "465") or 465)
    user = os.environ["SMTP_USER"]
    from_addr = os.environ.get("SMTP_FROM", user)
    if attachment:
        from email.mime.multipart import MIMEMultipart
        from email.mime.application import MIMEApplication
        fname, payload = attachment
        msg = MIMEMultipart()
        msg.attach(MIMEText(body, "plain", "utf-8"))
        part = MIMEApplication(payload, Name=fname)
        part["Content-Disposition"] = f'attachment; filename="{fname}"'
        msg.attach(part)
    else:
        msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = formataddr(("Mr. Cadabra's Classroom", from_addr))
    msg["To"] = to_addr
    try:
        if port == 465:
            with smtplib.SMTP_SSL(host, port, timeout=20) as srv:
                srv.login(user, os.environ["SMTP_PASS"])
                srv.sendmail(from_addr, [to_addr], msg.as_string())
        else:
            with smtplib.SMTP(host, port, timeout=20) as srv:
                srv.starttls()
                srv.login(user, os.environ["SMTP_PASS"])
                srv.sendmail(from_addr, [to_addr], msg.as_string())
        return ""
    except Exception as exc:  # noqa: BLE001
        err = f"{type(exc).__name__}: {exc}"
        print(f"[email] send failed: {err}")
        return err


# =============================================================================
# OPS ALERTING (2026-08-05) -- Jim finds out from an email, not from a parent.
# -----------------------------------------------------------------------------
# _ops_alert() emails Jim about an operational problem, at most once per `kind`
# per throttle window (default 60 min -- a crash loop makes ONE email an hour,
# not a thousand). Sends on a background thread so an alert can never slow a
# student's lesson. The global exception handler below feeds it; so does the
# cost watchdog in the scheduler loop. Env (all optional):
#   ALERT_EMAIL        where alerts go (defaults to SMTP_USER, Jim's inbox)
#   ALERT_THROTTLE_MIN minutes between repeat alerts of the same kind (60)
#   COST_ALERT_USD     trailing-24h est. spend that triggers the cost alarm
# =============================================================================

_ALERT_LAST: dict = {}          # kind -> unix time of last email sent
_ALERT_LOCK = threading.Lock()


def _ops_alert(kind: str, subject: str, body: str,
               throttle_minutes: int | None = None) -> None:
    """Fire-and-forget ops email. Never raises; throttled per `kind`."""
    try:
        mins = (throttle_minutes if throttle_minutes is not None
                else int(os.environ.get("ALERT_THROTTLE_MIN", "60") or 60))
        to_addr = (os.environ.get("ALERT_EMAIL", "").strip()
                   or os.environ.get("SMTP_USER", "").strip())
        if not to_addr or not _smtp_configured():
            print(f"[ops] alert (email not configured) {kind}: {subject}")
            return
        now = time.time()
        with _ALERT_LOCK:
            if len(_ALERT_LAST) > 500:          # bounded memory, always
                _ALERT_LAST.clear()
            if now - _ALERT_LAST.get(kind, 0) < mins * 60:
                return                          # throttled -- already emailed recently
            _ALERT_LAST[kind] = now

        def _go():
            err = _send_email(to_addr, "[Mr. Cadabra ops] " + subject,
                body + "\n\n--\nAutomatic ops alert from mrcadabra.com (build "
                + APP_BUILD + "). Repeats of this alert kind are muted for "
                + str(mins) + " minutes.\nAdmin panel: https://mrcadabra.com/admin")
            if err:
                print(f"[ops] alert email failed ({kind}): {err}")
        threading.Thread(target=_go, daemon=True, name="ops-alert").start()
    except Exception as exc:  # noqa: BLE001 -- the alarm must never be the fire
        print(f"[ops] alert error: {exc}")


@app.exception_handler(Exception)
async def _unhandled_error(request: Request, exc: Exception):
    """Any unhandled crash on any route: log it, record it, email Jim (throttled),
    and answer the caller warmly instead of with a bare stack trace. Normal
    HTTPExceptions (sign-in prompts, validation answers) never come through here."""
    where = f"{request.method} {request.url.path}"
    what = f"{type(exc).__name__}: {exc}"
    print(f"[error] UNHANDLED {where}: {what}")
    try:
        store.record_error(where, what)
    except Exception:  # noqa: BLE001
        pass
    _ops_alert("err:" + type(exc).__name__ + ":" + request.url.path,
               f"Server error on {where}",
               f"An unhandled error just occurred.\n\nWhere: {where}\n"
               f"What:  {what}\n\nRecent errors are listed on /admin.")
    return JSONResponse(status_code=500, content={"detail": (
        "Something went wrong on our side — it's been logged and reported. "
        "Please try again in a moment.")})


def _ops_watch_pass() -> None:
    """Cost watchdog, called by the scheduler loop every 30 minutes. Silent unless
    Jim set COST_ALERT_USD in Render AND the price env vars exist (we never guess
    at dollars). Throttled to roughly one alert per 20 hours."""
    try:
        thr = os.environ.get("COST_ALERT_USD", "").strip()
        if not thr:
            return
        limit = float(thr)
        if limit <= 0:
            return
        u = _usage_with_dollars(1)             # trailing 24h, same math as /admin
        brain, tts = u.get("brain_usd"), u.get("tts_usd")
        if brain is None and tts is None:
            return                              # price env vars not set -- no invented dollars
        total = (brain or 0) + (tts or 0)
        if total >= limit:
            _ops_alert("cost24",
                f"spend in the last 24h is about ${total:.2f} (alarm set at ${limit:.2f})",
                "Estimated spend over the trailing 24 hours crossed your alarm threshold.\n\n"
                f"  Brain (Claude):     ${(brain or 0):.2f}\n"
                f"  Voice (ElevenLabs): ${(tts or 0):.2f}\n"
                f"  Total:              ${total:.2f}   (threshold ${limit:.2f})\n\n"
                "The full cost panel is on /admin. If this is expected growth — "
                "congratulations; raise COST_ALERT_USD in Render. If it isn't, check "
                "/admin for a runaway student or an abuse pattern.",
                throttle_minutes=1200)
    except Exception as exc:  # noqa: BLE001
        print(f"[ops] cost watch error: {exc}")


@app.post("/api/parent/forgot")
def parent_forgot(body: ParentForgotIn, request: Request):
    """Email a password-reset link. SAME answer whether or not the address has an
    account -- nobody gets to probe which emails are signed up. The token is
    single-use, expires in 45 minutes, and only its SHA-256 hash is stored."""
    _require_db()
    _rate_limit("pforgot:" + _client_ip(request), limit=5, window_seconds=3600,
                what="reset requests")
    email = (body.email or "").strip().lower()
    if not _EMAIL_RE.match(email):
        raise HTTPException(status_code=400, detail="That doesn't look like an email address.")
    _rate_limit("pforgot-email:" + email, limit=3, window_seconds=3600,
                what="reset requests")
    if not _smtp_configured():
        # Honest, not leaky: this reveals server config, never account existence.
        return {"ok": True, "sent": False,
                "note": ("Email isn't switched on here yet — write to support@mrcadabra.com "
                         "and we'll reset it for you.")}
    parent = store.get_parent_by_email(email)
    if not parent:
        # Same 200 response as the success path (no probing which emails have
        # accounts) -- but the server log tells Jim why nothing arrived.
        print("[email] forgot: no parent account matches that address -- no email sent")
    if parent:
        raw = secrets.token_urlsafe(32)
        token_hash = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        store.create_parent_reset(token_hash, parent["id"], minutes=45)
        base = os.environ.get("APP_BASE_URL", "https://mrcadabra.com").rstrip("/")
        link = f"{base}/family?reset={raw}"
        send_err = _send_email(email, "Reset your Mr. Cadabra's Classroom password",
            "Hi" + ((" " + parent.get("name")) if parent.get("name") else "") + ",\n\n"
            "Someone asked to reset the password for this Mr. Cadabra's Classroom parent "
            "account. If that was you, open this link and choose a new password:\n\n"
            f"{link}\n\n"
            "The link works once and expires in 45 minutes.\n\n"
            "If you didn't ask for this, you can safely ignore this email — your password "
            "is unchanged and your students' learning is unaffected.\n\n"
            "— Mr. Cadabra's Classroom\nsupport@mrcadabra.com")
        if send_err:
            print(f"[email] forgot: send FAILED for a real account: {send_err}")
    return {"ok": True, "sent": True}


@app.get("/api/admin/email-test")
def admin_email_test(key: str = "", to: str = "",
                     x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """Jim's email-pipe diagnostic (admin-key protected): sends ONE real test email
    and returns exactly what happened -- the precise SMTP failure text on error,
    and the active config WITHOUT the password. This is how we debug 'the email
    never arrived' without guessing.
    BUILD dg: key accepted in the X-Admin-Key header (preferred); the query param
    stays for a hand-typed URL, but remember it lands in Render's logs when used."""
    _require_admin(x_admin_key or key)
    cfg = {"SMTP_HOST": os.environ.get("SMTP_HOST", "(not set)"),
           "SMTP_PORT": os.environ.get("SMTP_PORT", "(not set -> 465)"),
           "SMTP_USER": os.environ.get("SMTP_USER", "(not set)"),
           "SMTP_FROM": os.environ.get("SMTP_FROM", "(defaults to SMTP_USER)"),
           "SMTP_PASS": "(set)" if os.environ.get("SMTP_PASS") else "(NOT SET)"}
    to = (to or "").strip()
    if not to or not _EMAIL_RE.match(to):
        return {"ok": False, "config": cfg,
                "error": "Add &to=your@email.address to send a test message."}
    err = _send_email(to, "Mr. Cadabra's Classroom — email pipe test",
                      "This is a test of the app's outbound email. If you're reading it, "
                      "the pipe works: password resets and (later) weekly parent emails "
                      "will deliver.\n\n— Mr. Cadabra's Classroom")
    return {"ok": not err, "sent_to": to if not err else None,
            "error": err or None, "config": cfg}


# -----------------------------------------------------------------------------
# WEEKLY PARENT EMAIL (2026-08-04) -- the promised Friday report, assembled from
# existing parts: _send_email (the proven SMTP pipe), store.week_activity (the
# honest windowed numbers), and tutor.get_assessment in parent voice (the same
# engine as the dashboard's "How are they doing, really?").
# -----------------------------------------------------------------------------
_DIGEST_WINDOW_DAYS = 7
_DIGEST_UTC_WEEKDAY = 4          # Friday (site promise: "Every Friday")
_DIGEST_UTC_HOUR_FROM = 20       # 20:00-23:59 UTC = Friday afternoon/evening US


def _app_base() -> str:
    return os.environ.get("APP_BASE_URL", "https://mrcadabra.com").rstrip("/")


def _fmt_minutes(m: int) -> str:
    m = int(m or 0)
    if m < 60:
        return f"{m}m"
    return f"{m // 60}h {m % 60:02d}m"


def _unit_display_name(course: str, unit: int) -> str:
    for i, u in enumerate(curriculum.units_for(course)):
        if isinstance(u, (list, tuple)) and len(u) >= 2:
            if int(u[0]) == int(unit):
                return str(u[1])
        elif i + 1 == int(unit):
            return str(u)
    return f"Unit {unit}"


def _weekly_child_section(student: dict, week: dict) -> str:
    """One child's block of the digest: honest week numbers, template-built
    (deterministic, free). The AI paragraph is added separately by the caller."""
    name = (student.get("name") or "Your student").strip() or "Your student"
    lines = [f"------  {name.upper()}  ------"]
    if week["minutes_total"] <= 0 and not week["checks"] and not week["touched"]:
        lines.append(f"No tutoring sessions this week. {name}'s login code works any "
                     "time -- even ten minutes of practice moves the needle, and "
                     "Mr. Cadabra picks up exactly where they left off.")
        return "\n".join(lines)
    lines.append(f"This week: {_fmt_minutes(week['minutes_total'])} of real work across "
                 f"{week['days_active']} day(s). Idle time never counts.")
    if len(week["minutes_by_course"]) > 1:
        parts = [f"{curriculum.course_title(c)} {_fmt_minutes(m)}"
                 for c, m in sorted(week["minutes_by_course"].items(),
                                    key=lambda kv: -kv[1]) if m > 0]
        if parts:
            lines.append("By course: " + "; ".join(parts) + ".")
    if week["checks"]:
        parts = []
        for c in week["checks"]:
            uname = _unit_display_name(c["course"], c["unit"])
            if c["best_pct"] >= store.PASS_PCT:
                parts.append(f"{uname} -- {c['best_pct']}% (MASTERED, 90%+ bar)")
            else:
                parts.append(f"{uname} -- best so far {c['best_pct']}% (mastery is 90%+)")
        lines.append("Unit checks this week: " + "; ".join(parts) + ".")
    touched_named = [t["unit_name"] for t in week["touched"] if t.get("unit_name")]
    if touched_named:
        seen, uniq = set(), []
        for n in touched_named:
            if n not in seen:
                seen.add(n)
                uniq.append(n)
        lines.append("Worked on: " + ", ".join(uniq[:6]) +
                     ("..." if len(uniq) > 6 else "") + ".")
    if week["award_ids"]:
        names = [f"{AWARD_DEFS[a][0]} {AWARD_DEFS[a][1]}"
                 for a in week["award_ids"] if a in AWARD_DEFS]
        if names:
            lines.append("New awards earned: " + ", ".join(names) + ".")
    # 2026-08-11 (build du, parent lens item 6): the question every parent asks --
    # "what did they struggle with?" -- answered with the ACTUAL problems from this
    # week's quizzes (rule 55's rows). Capped at 3; absent when the week had none.
    try:
        import datetime as _dt
        cutoff = (_dt.date.today() - _dt.timedelta(days=7)).isoformat()
        tricky = [m for m in store.get_misses(student.get("code") or "", limit=15)
                  if (m.get("when") or "") >= cutoff][:3]
    except Exception as exc:  # noqa: BLE001
        print(f"[digest] get_misses failed (ignored): {exc}")
        tricky = []
    if tricky:
        lines.append("Tricky this week (worth five minutes together): " + "; ".join(
            f"\"{m['question']}\" -- they answered \"{m['answer']}\"" for m in tricky)
            + ". Mr. Cadabra brings one of these back himself, gently, next session.")
    return "\n".join(lines)


def _weekly_ai_summary(code: str, student: dict, week: dict) -> str:
    """The parent-voice analytical paragraph for this child's most-worked course
    this week. Returns "" on any problem -- the numbers-only email still goes out."""
    active = {c: m for c, m in week["minutes_by_course"].items() if m > 0}
    if not active:
        return ""
    course = max(active, key=active.get)
    if course not in curriculum.COURSES:
        return ""
    try:
        facts = _assessment_facts(code, student, course)
        facts += (f"\nTHIS SPECIFIC WEEK (the report period): "
                  f"{week['minutes_total']} real working minutes across "
                  f"{week['days_active']} active day(s); "
                  f"{len(week['checks'])} unit check(s) taken; "
                  f"{len(week['award_ids'])} new award(s) earned.")
        text = tutor.get_assessment(facts, "parent", code=code, course=course)
        if not text or text.startswith("("):
            return ""
        return text.strip()
    except Exception as exc:  # noqa: BLE001
        print(f"[digest] AI summary failed for {code}: {exc}")
        return ""


def _build_weekly_digest(parent: dict):
    """(subject, body) for this parent's weekly email, or (None, None) when there
    is nothing to send (no children). Never raises."""
    children = store.list_students_for_parent(parent["id"])
    if not children:
        return None, None
    state = store.ensure_digest_state(parent["id"])
    names = [(c.get("name") or "").strip() or "your student" for c in children]
    if len(names) == 1:
        subject = f"{names[0]}'s week with Mr. Cadabra's Classroom"
    elif len(names) == 2:
        subject = f"{names[0]} & {names[1]}'s week with Mr. Cadabra's Classroom"
    else:
        subject = "Your family's week with Mr. Cadabra's Classroom"
    pname = (parent.get("name") or "").strip()
    blocks = [f"Hi{(' ' + pname) if pname else ''},",
              "Here's the honest weekly report -- real numbers from real work, "
              "never padded."]
    for child in children:
        week = store.week_activity(child["code"], days=_DIGEST_WINDOW_DAYS)
        blocks.append(_weekly_child_section(child, week))
        ai = _weekly_ai_summary(child["code"], child, week)
        if ai:
            blocks.append(ai)
    base = _app_base()
    blocks.append(f"Full dashboard any time: {base}/family")
    blocks.append("Questions? Just reply to this email, or write "
                  "support@mrcadabra.com -- a person reads it.")
    blocks.append("--\nYou're receiving this weekly report because you have a "
                  "Mr. Cadabra's Classroom parent account.\n"
                  f"Unsubscribe (one click): {base}/api/parent/weekly-email/"
                  f"unsubscribe?token={state['optout_token']}\n"
                  "Mr. Cadabra's Classroom · Hyperion Shift LLC")
    return subject, "\n\n".join(blocks)


@app.get("/api/parent/weekly-email/unsubscribe")
def weekly_email_unsubscribe(request: Request, token: str = "", resub: str = ""):
    """One-click unsubscribe from the weekly report (the token grants ONLY this).
    ?resub=1 flips it back on -- the confirmation page offers exactly that."""
    _require_db()
    _rate_limit("unsub:" + _client_ip(request), limit=30, window_seconds=3600,
                what="unsubscribe requests")
    pid = store.parent_id_for_digest_token(token)
    page_top = ("<!doctype html><html><head><meta charset='utf-8'>"
                "<meta name='viewport' content='width=device-width,initial-scale=1'>"
                "<title>Weekly email — Mr. Cadabra's Classroom</title>"
                "<style>body{font-family:system-ui,sans-serif;background:#f7f6ff;"
                "margin:0;display:grid;place-items:center;min-height:100vh}"
                ".card{background:#fff;border:1px solid #e5e2f5;border-radius:14px;"
                "padding:34px 38px;max-width:460px;box-shadow:0 8px 30px rgba(60,50,140,.08)}"
                "h1{font-size:21px;color:#3d3480;margin:0 0 10px}p{color:#555;line-height:1.5}"
                "a{color:#5b5bd6}</style></head><body><div class='card'>")
    page_end = "</div></body></html>"
    if not pid:
        return Response(page_top + "<h1>That link isn't valid</h1>"
                        "<p>It may be from an old email. Nothing was changed. If you "
                        "want to stop the weekly report, use the link in your most "
                        "recent email, or write support@mrcadabra.com.</p>" + page_end,
                        media_type="text/html")
    if (resub or "").strip() == "1":
        store.set_digest_optout(pid, False)
        return Response(page_top + "<h1>Welcome back 👋</h1>"
                        "<p>The weekly report is switched on again. The next one "
                        "arrives Friday.</p>" + page_end, media_type="text/html")
    store.set_digest_optout(pid, True)
    return Response(page_top + "<h1>You're unsubscribed</h1>"
                    "<p>No more weekly report emails. Your account and your "
                    "students' tutoring are completely unaffected, and the same "
                    "numbers are always on your parent dashboard.</p>"
                    f"<p>Changed your mind? <a href='/api/parent/weekly-email/"
                    f"unsubscribe?token={token}&resub=1'>Turn it back on</a>.</p>"
                    + page_end, media_type="text/html")


@app.get("/api/admin/digest-test")
def admin_digest_test(key: str = "", email: str = "", to: str = "",
                      x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """Jim's weekly-email diagnostic (admin-key protected): builds a REAL parent's
    digest and returns it as JSON WITHOUT sending. Add &to=an@address to also send
    exactly one copy there for eyeballing. Never marks the parent as sent.
    BUILD dg: key accepted in the X-Admin-Key header (preferred); the query param
    stays for a hand-typed URL, but remember it lands in Render's logs when used."""
    _require_admin(x_admin_key or key)
    _require_db()
    email = (email or "").strip().lower()
    if not email:
        return {"ok": False, "error": "Add &email=<parent email> to pick the parent."}
    parent = store.get_parent_by_email(email)
    if not parent:
        return {"ok": False, "error": "No parent account with that email."}
    subject, body = _build_weekly_digest(parent)
    if not subject:
        return {"ok": False, "error": "That parent has no students yet -- nothing to send."}
    sent_to, err = None, None
    to = (to or "").strip()
    if to:
        if not _EMAIL_RE.match(to):
            err = "That &to= address doesn't look like an email."
        else:
            err = _send_email(to, subject, body) or None
            sent_to = to if not err else None
    return {"ok": err is None, "subject": subject, "body": body,
            "sent_to": sent_to, "error": err}


def _weekly_email_off() -> bool:
    """True when the WEEKLY_EMAIL env flag disables the weekly parent email. Gates ONLY
    the email (build gz) -- the heartbeat thread and every other pass run regardless."""
    return os.environ.get("WEEKLY_EMAIL", "on").strip().lower() in ("off", "0", "false", "no")


def _weekly_digest_pass(force: bool = False) -> dict:
    """One send pass: every parent who is due gets this week's email. Returns
    counts for the log. `force` ignores the Friday window (admin/testing only --
    the 3-day resend guard still applies). build gz: the WEEKLY_EMAIL flag is
    honoured HERE (email only), not at the heartbeat -- `force` overrides it so
    the admin test endpoint still works while the flag is off."""
    from datetime import datetime, timezone
    out = {"checked": 0, "sent": 0, "skipped": 0, "failed": 0}
    if not force and _weekly_email_off():
        return out
    if not (store.enabled() and _smtp_configured()):
        return out
    now = datetime.now(timezone.utc)
    if not force and not (now.weekday() == _DIGEST_UTC_WEEKDAY
                          and now.hour >= _DIGEST_UTC_HOUR_FROM):
        return out
    for parent in store.list_parents():
        out["checked"] += 1
        try:
            state = store.ensure_digest_state(parent["id"])
            if int(state.get("optout") or 0):
                out["skipped"] += 1
                continue
            last = state.get("last_sent_at")
            if last is not None:
                if hasattr(last, "tzinfo") and last.tzinfo is None:
                    last = last.replace(tzinfo=timezone.utc)
                if (now - last).total_seconds() < 3 * 86400:
                    out["skipped"] += 1
                    continue
            subject, body = _build_weekly_digest(parent)
            if not subject:
                out["skipped"] += 1
                continue
            err = _send_email(parent["email"], subject, body)
            if err:
                out["failed"] += 1
                print(f"[digest] send FAILED for parent {parent['id']}: {err}")
            else:
                store.mark_digest_sent(parent["id"])
                out["sent"] += 1
        except Exception as exc:  # noqa: BLE001
            out["failed"] += 1
            print(f"[digest] pass error for parent {parent.get('id')}: {exc}")
    if out["sent"] or out["failed"]:
        print(f"[digest] pass done: {out}")
    return out


def _digest_loop():
    """Daemon thread: wake every 30 minutes; inside the Friday window, send to
    everyone due. Restart-safe (last_sent_at lives in the database) and duplicate-
    safe (the 3-day guard means one send per parent per window).
    2026-08-05: the same heartbeat now also runs the ops cost watchdog
    (_ops_watch_pass) -- each pass is fenced in its own try so one failing can
    never stop the other."""
    while True:
        time.sleep(1800)          # sleep FIRST: never race the module import at boot
        # build ha: the heartbeat stamps itself so /health can report its AGE. A loop
        # that dies between ticks used to be invisible; now it is a growing number.
        try:
            store.record_event("ops_pass", "heartbeat")
        except Exception:  # noqa: BLE001 -- the stamp must never stop the passes
            pass
        try:
            _weekly_digest_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[digest] loop error: {exc}")
        try:
            _ops_watch_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[ops] watch loop error: {exc}")
        # build cn: the usage log is one row per model call and per TTS request. At
        # 10,000 students that is millions of rows a month, and nothing ever removed
        # one. The cost dashboard only ever looks back weeks, so anything older than
        # USAGE_LOG_DAYS is dead weight in the same database the lessons run on.
        try:
            _usage_purge_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[usage] purge loop error: {exc}")
        # build dj: the nightly database snapshot rides the same heartbeat, fenced in
        # its own try like everything else here -- a failing backup must never stop
        # the digests, and vice versa. The pass itself decides whether a day has gone
        # by (it reads the newest file on disk, so it is restart-safe).
        try:
            _backup_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[backup] loop error: {exc}")
        # build hv: the weekly OFF-SITE copy rides the same heartbeat, same fence.
        try:
            _offsite_backup_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[offsite] loop error: {exc}")
        # build go: LAST on the heartbeat, and by far the longest -- the digests, the
        # ops watch, the purge and the snapshot all matter more than the watch and must
        # never queue behind it. Fenced like everything else here.
        try:
            _nightwatch_pass()
        except Exception as exc:  # noqa: BLE001
            print(f"[nightwatch] loop error: {exc}")


# =============================================================================
# THE NIGHT WATCH (2026-08-16, build go) -- AI GOVERNING AI, ON A CADENCE
# -----------------------------------------------------------------------------
# Jim: "only AI is gonna be capable of governing AI... depending on me to fix it or notice
# problems is only going to address some of those problems and probably just the big ones."
# Everything else we own is a RATCHET -- it makes a defect permanent-proof once a human has
# found it. This is the part that goes looking. See nightwatch.py for the design; the four
# rules that shape it are: every finding is challenged before Jim sees it, only NEW ones are
# reported, it can never touch a lesson, and it always says what it did not cover.
# It rides this heartbeat rather than a Render Cron Job on purpose: production was created
# by hand and is not attached to render.yaml, so a background pass is the only form of
# "nightly" that needs nothing from Jim but a push.
def _nightwatch_termgap(scenario, transcript) -> None:
    """Lend the [termgap] probe to the night watch, ONE TURN AT A TIME.
    The probe's whole question is "was this word introduced BEFORE it was used?", so it
    must see each tutor reply against the history that existed when it was written --
    handing it the whole lesson as a single blob would make every term look introduced.
    Wrapped: a probe never breaks the watch, exactly as it never breaks a lesson."""
    history = []
    for role, text in transcript:
        if role == "assistant":
            try:
                _record_unintroduced("AUDIT", scenario.get("course", ""), text, list(history))
            except Exception as exc:  # noqa: BLE001
                print(f"[termgap] night-watch probe skipped: {exc}")
        history.append({"role": "user" if role == "user" else "assistant", "content": text})


def _nightwatch_pass() -> None:
    if nightwatch is None or not nightwatch.enabled():
        return
    if not nightwatch.due(DATA_DIR):
        return
    print("[nightwatch] starting tonight's pass")
    result = nightwatch.run_night(
        DATA_DIR,
        # The server-side probes live here, not in tutor.py, so the watch would be blind
        # to them unless we lend them across. Anything omitted simply does not run, and
        # the report names what it did not cover.
        probe_hooks={"termgap": _nightwatch_termgap},
        # (so) lent across like the probes: the closure's rendered-vs-not count, so
        # the report can say "run the prewarm" on the morning it matters.
        extras={"closure": _closure_render_status()})
    path = nightwatch.write_report(DATA_DIR, result, APP_BUILD)
    print(f"[nightwatch] {result.get('ran', 0)} lessons \u00b7 "
          f"{len(result.get('new', []))} new \u00b7 {result.get('recurring', 0)} known \u00b7 "
          f"{result.get('refuted', 0)} refuted \u00b7 {result.get('seconds', 0)}s"
          + (f" \u00b7 {path}" if path else ""))
    store.record_event("ops_pass", "nightwatch",
                       f"{result.get('ran', 0)} lessons, {len(result.get('new', []))} new, "
                       f"{result.get('refuted', 0)} refuted, {result.get('seconds', 0)}s")
    digest = nightwatch.email_digest(result, APP_BUILD)
    if digest:
        subject, body = digest
        # Not throttled away: a new confirmed teaching defect is exactly what Jim asked to
        # be told about, and there is at most one of these a night.
        _ops_alert("nightwatch", subject, body, throttle_minutes=0)


USAGE_LOG_DAYS = int(os.environ.get("USAGE_LOG_DAYS", "180") or 180)
EVENTS_DAYS = int(os.environ.get("EVENTS_DAYS", "90") or 90)   # build ha: telemetry retention
_last_usage_purge = [0.0]


# =============================================================================
# NIGHTLY DATABASE SNAPSHOT (2026-08-11, build dj)
# -----------------------------------------------------------------------------
# Jim: "if Render falters or something falters, do we have sufficient backup so that
# we could recreate everything right away?" The honest answer was NO for exactly one
# asset: the database. This writes one gzipped JSON snapshot of every table per day
# to DATA_DIR/backups -- which since the 08-11 infrastructure change is the Render
# PERSISTENT DISK, so snapshots survive deploys. Restart-safe (the gate is the newest
# file's mtime on disk, not process memory), atomic (write .tmp, then rename), and
# rotated (BACKUP_KEEP newest are kept, default 14). Copies leave the machine via the
# /admin download button -- the third copy lives on Jim's own computer. The full
# recovery drill is RECOVERY.md in the repo.
# =============================================================================
BACKUP_KEEP = int(os.environ.get("BACKUP_KEEP", "14") or 14)
_BACKUP_DIR = DATA_DIR / "backups"


def _backup_blob() -> tuple[bytes, dict]:
    """The current database as gzipped JSON bytes, plus the snapshot's row counts."""
    snap = store.export_all()
    blob = gzip.compress(json.dumps(snap, separators=(",", ":")).encode("utf-8"))
    return blob, snap["row_counts"]


def _backup_pass() -> None:
    """Write today's snapshot if a day has passed since the newest one on disk.
    Called from the 30-minute heartbeat; silent and harmless when the DB is off.
    build hv: a FAILURE inside this pass now writes an ops_fail system_events row
    and emails Jim (throttled) -- /health showed backup_age null on a healthy
    Starter-plan deploy and nothing could say why, which is Class A's disease
    wearing an ops hat. Also: when the pass SKIPS because today's snapshot already
    exists, it still refreshes the ops_pass marker, so /health's backup age means
    "age of the newest snapshot", not "age of the last WRITE" -- the null had two
    innocent readings and now has one."""
    if not store.enabled() or BACKUP_KEEP <= 0:
        return
    try:
        _BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        existing = sorted(_BACKUP_DIR.glob("backup-*.json.gz"))
        if existing:
            newest = max(p.stat().st_mtime for p in existing)
            if time.time() - newest < 24 * 3600 - 300:   # 5-min grace so the slot can't drift
                if not store.last_event_at("ops_pass", "backup"):
                    store.record_event("ops_pass", "backup",
                                       "snapshot current (marker refreshed after deploy)")
                return
        _backup_write()
    except Exception as exc:  # noqa: BLE001
        print(f"[backup] PASS FAILED: {exc}")
        store.record_event("ops_fail", "backup", str(exc)[:300])
        _ops_alert("backup-failed", "Nightly backup FAILED",
                   f"The snapshot pass raised: {exc}\nCheck DATA_DIR and the disk on "
                   "Render; /health ops.backup_age_s stays stale until this heals.")


def _backup_write() -> None:
    blob, counts = _backup_blob()
    name = "backup-" + time.strftime("%Y%m%d-%H%M%S", time.gmtime()) + ".json.gz"
    tmp = _BACKUP_DIR / (name + ".tmp")
    tmp.write_bytes(blob)
    os.replace(tmp, _BACKUP_DIR / name)              # atomic: never a half-written snapshot
    print(f"[backup] wrote {name} ({len(counts)} tables, {sum(counts.values())} rows, "
          f"{len(blob):,} bytes)")
    store.record_event("ops_pass", "backup",
                       f"{name}: {sum(counts.values())} rows, {len(blob)} bytes")
    for p in sorted(_BACKUP_DIR.glob("backup-*.json.gz"))[:-BACKUP_KEEP]:
        try:
            p.unlink()
            print(f"[backup] rotated out {p.name}")
        except OSError as exc:
            print(f"[backup] rotation could not remove {p.name}: {exc}")


OFFSITE_BACKUP_DAYS = int(os.environ.get("OFFSITE_BACKUP_DAYS", "7") or 7)   # 0 = off


def _offsite_backup_pass() -> None:
    """BUILD hv (Phase 5 -- review Class F): THE OFF-SITE COPY IS AUTOMATED. The
    nightly snapshot lands on the same Render disk as the database's machine; the
    off-site copy used to be Jim remembering to click /admin's download button.
    Now, every OFFSITE_BACKUP_DAYS days, the freshest snapshot is EMAILED to
    ALERT_EMAIL -- an inbox is off this machine, which is the whole point, and it
    needs no new service or credential. Restart-safe (asks the DB when one last
    went out); size-capped with a loud alert instead of a silent skip; every
    outcome is an ops_pass/ops_fail row /health can age."""
    if not store.enabled() or OFFSITE_BACKUP_DAYS <= 0:
        return
    try:
        from datetime import datetime as _odt, timezone as _otz
        last = store.last_event_at("ops_pass", "offsite")
        if last is not None:
            if last.tzinfo is None:
                last = last.replace(tzinfo=_otz.utc)
            if ((_odt.now(_otz.utc) - last).total_seconds()
                    < OFFSITE_BACKUP_DAYS * 86400 - 300):
                return
        to_addr = (os.environ.get("ALERT_EMAIL", "").strip()
                   or os.environ.get("SMTP_USER", "").strip())
        if not to_addr or not _smtp_configured():
            return          # unconfigured email is already reported by the alert path
        blob, counts = _backup_blob()
        rows = sum(counts.values())
        if len(blob) > 15_000_000:
            _ops_alert("offsite-too-big", "Off-site backup too large to email",
                       f"This week's snapshot is {len(blob):,} bytes -- too big for an "
                       "email attachment. Download it from /admin and store it off-site; "
                       "a real off-site target (S3/B2) is the next step at this size.")
            return
        name = "mrcadabra-backup-" + time.strftime("%Y%m%d", time.gmtime()) + ".json.gz"
        err = _send_email(
            to_addr, f"Weekly off-site backup — {rows} rows",
            "Attached is this week's full database snapshot (gzipped JSON).\n\n"
            "Keep a few of these somewhere safe -- they are the copy that survives "
            "losing Render itself. Restore with restore_backup.py (see RECOVERY.md).\n\n"
            "— the ops heartbeat",
            attachment=(name, blob))
        if err:
            store.record_event("ops_fail", "offsite", err[:300])
            _ops_alert("offsite-failed", "Off-site backup email FAILED", err[:500])
        else:
            print(f"[offsite] emailed {name} ({rows} rows, {len(blob):,} bytes) to inbox")
            store.record_event("ops_pass", "offsite", f"{rows} rows, {len(blob)} bytes")
    except Exception as exc:  # noqa: BLE001
        print(f"[offsite] pass failed: {exc}")
        store.record_event("ops_fail", "offsite", str(exc)[:300])


def _usage_purge_pass() -> None:
    """Drop usage rows older than USAGE_LOG_DAYS. Runs at most once a day, from the
    heartbeat that already exists. Counts only -- no conversation text was ever in
    there. Silent and harmless when the DB is off."""
    if not store.enabled() or USAGE_LOG_DAYS <= 0:
        return
    now = time.monotonic()
    if _last_usage_purge[0] and now - _last_usage_purge[0] < 86400:
        return
    _last_usage_purge[0] = now
    removed = store.purge_usage_log(USAGE_LOG_DAYS)
    if removed:
        print(f"[usage] purged {removed} rows older than {USAGE_LOG_DAYS} days")
    # build ha: the telemetry table obeys the same discipline -- it can never grow
    # forever. Counts only, so nothing about a student is lost when rows age out.
    removed_ev = store.purge_system_events(EVENTS_DAYS)
    if removed_ev:
        print(f"[events] purged {removed_ev} rows older than {EVENTS_DAYS} days")


_digest_thread_started = False


def _start_digest_thread() -> None:
    # build gz (2026-08-17): THE HEARTBEAT ALWAYS BEATS. This thread is not "the weekly
    # email" -- it is the app's entire ops plane: the nightly DB snapshot, the cost
    # watchdog, the usage purge AND the night watch all ride it. The old WEEKLY_EMAIL
    # early-return here meant one misnamed flag silently disabled BACKUPS and the AI
    # governor -- found by the 2026-08-17 full-app review ("the app cannot see its own
    # failures" class). The flag now lives inside _weekly_digest_pass, where it gates
    # exactly what its name promises: the email, and nothing else.
    global _digest_thread_started
    if _digest_thread_started:
        return
    if _weekly_email_off():
        print("[digest] WEEKLY_EMAIL=off -- weekly parent email disabled "
              "(heartbeat still runs: backups, cost watch, purge, night watch)")
    _digest_thread_started = True
    threading.Thread(target=_digest_loop, daemon=True, name="weekly-digest").start()


_start_digest_thread()


@app.post("/api/parent/reset")
def parent_reset(body: ParentResetIn, request: Request):
    """Redeem a reset link: set the new password and sign the parent out everywhere."""
    _require_db()
    _rate_limit("preset:" + _client_ip(request), limit=10, window_seconds=3600,
                what="reset attempts")
    if len(body.password or "") < 8:
        raise HTTPException(status_code=400, detail="Please use a password of at least 8 characters.")
    token_hash = hashlib.sha256((body.token or "").encode("utf-8")).hexdigest()
    parent_id = store.consume_parent_reset(token_hash)
    if not parent_id:
        raise HTTPException(status_code=400, detail=(
            "That reset link isn't valid anymore — it may have expired (they last 45 minutes) "
            "or already been used. Request a fresh one from the Sign in page."))
    store.update_parent(parent_id, password_hash=_hash_password(body.password))
    store.delete_parent_tokens_for(parent_id)      # whoever had the old password is out
    return {"ok": True}


@app.post("/api/parent/logout")
def parent_logout(body: ParentTokenIn):
    _require_db()
    store.delete_parent_token((body.token or "").strip())
    return {"ok": True}


@app.get("/api/parent/me")
def parent_me(request: Request):
    """The signed-in parent's family picture. Token comes in the X-Parent-Token header."""
    parent = _require_parent(request.headers.get("x-parent-token", ""))
    return _parent_payload(parent)


@app.post("/api/parent/students")
def parent_add_student(body: ParentStudentIn):
    """Add a child (first name only) and mint their login code."""
    parent = _require_parent(body.token)
    name = (body.name or "").strip()[:40]
    if not name:
        raise HTTPException(status_code=400, detail="Please enter your student's first name.")
    existing = store.list_students_for_parent(parent["id"])
    if len(existing) >= 8:
        raise HTTPException(status_code=400, detail=(
            "That's 8 students on one account — email support@mrcadabra.com and "
            "we'll set your family up properly."))
    code = _new_student_code()
    store.create_student_account(code, name, parent["id"])
    return _parent_payload(parent)


@app.get("/api/parent/overview")
def parent_overview(request: Request):
    """MISSION CONTROL for /family (build dq -- Four-Lens Review, homeschool item 1).
    One parent-token-gated call returns the numbers a parent actually wants next to
    each child's name: real minutes this week (idle never counts), active days, total
    units mastered, last-active date, and the child's most-worked course (so the
    "How are they doing?" button asks about the right one) -- plus the weekly-email
    setting so the page can show the toggle. Every per-child block is wrapped: a
    stats panel is a BONUS and must never break the family page."""
    parent = _require_parent(request.headers.get("x-parent-token", ""))
    import datetime as _dt
    today = _dt.date.today()
    week_ago = (today - _dt.timedelta(days=6)).isoformat()
    titles = dict(curriculum.list_courses())
    kids = []
    for s in store.list_students_for_parent(parent["id"]):
        code = s["code"]
        minutes, days_set, per_course = 0, set(), {}
        try:
            for row in store.get_time_between(code, week_ago, today.isoformat()):
                m = int(row.get("minutes") or 0)
                minutes += m
                if m:
                    days_set.add(row.get("day"))
                    per_course[row["course"]] = per_course.get(row["course"], 0) + m
        except Exception:  # noqa: BLE001
            pass
        mastered, last_active, act = 0, None, {}
        try:
            act = store.get_course_activity(code)
            for a in act.values():
                mastered += int(a.get("units_mastered") or 0)
                la = a.get("last_active")
                if la and (last_active is None or la > last_active):
                    last_active = la
        except Exception:  # noqa: BLE001
            pass
        top = max(per_course, key=per_course.get) if per_course else None
        if not top and act:
            top = max(act, key=lambda c: act[c].get("last_active") or "")
        steer = None
        try:
            s = store.get_steer(code)
            if s and 1 <= int(s.get("unit") or 0) <= 9:
                steer = {"course": s["course"], "unit": s["unit"],
                         "course_title": titles.get(s["course"], s["course"]),
                         "unit_name": curriculum.unit_name(s["course"], s["unit"])}
        except Exception:  # noqa: BLE001
            pass
        goal = None
        try:
            g = store.get_practice_goal(code)
            if g:
                goal = {"minutes": g["minutes"], "kind": g["kind"],
                        "target": g["target"], "today_done": g["today_done"]}
        except Exception:  # noqa: BLE001
            pass
        kids.append({"code": code, "minutes_week": minutes,
                     "active_days_week": len(days_set), "units_mastered": mastered,
                     "last_active": last_active, "top_course": top,
                     "top_course_title": titles.get(top, ""), "steer": steer,
                     "goal": goal})
    state = store.ensure_digest_state(parent["id"])
    return {"ok": True, "students": kids,
            "weekly_email_on": not int(state.get("optout") or 0)}


class WeeklyEmailIn(BaseModel):
    token: str = ""
    on: bool = True


@app.post("/api/parent/weekly-email")
def parent_weekly_email(body: WeeklyEmailIn, request: Request):
    """The IN-PRODUCT toggle for the Friday report (build dq). Before this, the only
    way to stop the weekly email was the tokenized link inside the email itself --
    a setting with no switch. Same store flag the unsubscribe link flips."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    store.set_digest_optout(parent["id"], not bool(body.on))
    return {"ok": True, "on": bool(body.on)}


# =============================================================================
# PARENT CHILD-MANAGEMENT (2026-08-11, build dy -- Four-Lens parent item 2).
# Rename / new code / remove / attach: everything that used to be a support email.
# Every endpoint is parent-token gated AND ownership-checked -- a parent can only
# ever touch their OWN children. Remove additionally demands the child's name typed
# back (a mis-tap must never delete a childhood of progress).
# =============================================================================
class ParentChildIn(BaseModel):
    token: str = ""
    code: str = ""
    name: str = ""             # rename: the new name · remove: the typed confirmation


def _own_student(parent: dict, code: str) -> str:
    """The child must be THIS parent's. 404 (not 403) on a miss: an outsider probing
    codes learns nothing about which codes exist."""
    code = (code or "").strip()
    mine = {s["code"] for s in store.list_students_for_parent(parent["id"])}
    if code not in mine:
        raise HTTPException(status_code=404, detail="That student isn't on your account.")
    return code


class ParentSteerIn(BaseModel):
    token: str = ""
    code: str = ""
    course: str = ""
    unit: int = 0              # 1-9 sets the plan; 0 clears it


@app.post("/api/parent/student-steer")
def parent_student_steer(body: ParentSteerIn, request: Request):
    """The pacing control (build ea): "center their sessions on Unit N for now."
    Applies when the child opens that course without a focus of their own; the
    child's explicit choice always outranks it (rule 50). unit=0 clears the plan."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    code = _own_student(parent, body.code)
    unit = int(body.unit or 0)
    if unit == 0:
        store.clear_steer(code)
        return _parent_payload(store.get_parent(parent["id"]))
    if not (1 <= unit <= 9):
        raise HTTPException(status_code=400, detail="Pick a unit from 1 to 9 (or clear the plan).")
    course = (body.course or "").strip()
    if course not in curriculum.COURSES:
        # default to where the child actually works: most engaged-time course, else
        # most recently active, else algebra1 -- resolved HERE so the page never
        # needs its own course list (unit names live in six files already; no seventh).
        try:
            act = store.get_course_activity(code)
            course = max(act, key=lambda c: act[c].get("last_active") or "") if act else "algebra1"
        except Exception:  # noqa: BLE001
            course = "algebra1"
    store.set_steer(code, course, unit)
    return _parent_payload(store.get_parent(parent["id"]))


class ParentGoalIn(BaseModel):
    token: str = ""
    code: str = ""
    minutes: int = 0           # 5-60 sets the goal; 0 clears it
    kind: str = "general"      # "general" | "latest"


def _set_goal_checked(code: str, minutes: int, kind: str, set_by: str):
    """Shared validation for the parent and teacher goal doors (build sb). One
    place, so the two portals cannot drift on what a legal goal is."""
    minutes = int(minutes or 0)
    if minutes == 0:
        store.clear_practice_goal(code)
        return
    if not (5 <= minutes <= 60):
        raise HTTPException(status_code=400,
                            detail="Pick 5 to 60 minutes (or clear the goal).")
    kind = (kind or "general").strip().lower()
    if kind not in ("general", "latest"):
        raise HTTPException(status_code=400,
                            detail="The goal kind is 'general' or 'latest'.")
    store.set_practice_goal(code, minutes, kind, set_by)


@app.post("/api/parent/student-goal")
def parent_student_goal(body: ParentGoalIn, request: Request):
    """The daily practice goal (build sb, Jim's design 2026-09-02): "fifteen
    minutes of practice", stored as minutes but measured in problems so it
    cannot be idled through. kind='general' is a friendly mix; kind='latest'
    nudges toward the newest MASTERED skills -- by design nothing untaught can
    ever be assigned, because the goal never names content at all: it only asks
    for practice, and practice serves what the child's own record has earned.
    minutes=0 clears it. Same ownership gate as every parent door."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    code = _own_student(parent, body.code)
    _set_goal_checked(code, body.minutes, body.kind,
                      "family:" + str(parent.get("email") or parent.get("id") or ""))
    return _parent_payload(store.get_parent(parent["id"]))


@app.post("/api/parent/student-rename")
def parent_student_rename(body: ParentChildIn, request: Request):
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    code = _own_student(parent, body.code)
    name = (body.name or "").strip()[:40]
    if not name:
        raise HTTPException(status_code=400, detail="Please enter the new name.")
    store.rename_student(code, name)
    return _parent_payload(store.get_parent(parent["id"]))


@app.post("/api/parent/student-newcode")
def parent_student_newcode(body: ParentChildIn, request: Request):
    """A leaked login code is a leaked key. Mint a fresh one; every scrap of the
    child's history moves with it in one transaction; the old code dies instantly."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    code = _own_student(parent, body.code)
    new_code = _new_student_code()
    res = store.change_student_code(code, new_code)
    if not res.get("ok"):
        raise HTTPException(status_code=500, detail="Couldn't change the code — nothing was altered. Try again.")
    out = _parent_payload(store.get_parent(parent["id"]))
    out["new_code"] = new_code
    return out


@app.post("/api/parent/student-remove")
def parent_student_remove(body: ParentChildIn, request: Request):
    """PERMANENT. Deletes the child's account and every per-student row (the same
    cascade Start Fresh uses -- accounts is in the reset family). The parent must
    type the child's name back exactly (case-insensitive) as consent."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    code = _own_student(parent, body.code)
    acct = store.get_account(code) or {}
    want = (acct.get("name") or "").strip().lower()
    typed = (body.name or "").strip().lower()
    if not want or typed != want:
        raise HTTPException(status_code=400, detail=(
            "To remove this student, type their name exactly as it appears — this "
            "permanently deletes their progress."))
    store.reset_student_data(code)
    return _parent_payload(store.get_parent(parent["id"]))


@app.post("/api/parent/student-attach")
def parent_student_attach(body: ParentChildIn, request: Request):
    """Attach an existing UNOWNED student code (an early beta student, a code made
    before the parent signed up). A code owned by another parent is never
    transferable here; pilot demo codes can't be claimed at all."""
    parent = _require_parent(body.token or request.headers.get("x-parent-token", ""))
    _require_db()
    code = (body.code or "").strip().upper()
    if not code:
        raise HTTPException(status_code=400, detail="Please enter the student's login code.")
    if code in STUDENTS:
        raise HTTPException(status_code=400, detail="That's a shared demo code — it can't join a family account.")
    result = store.attach_student(code, parent["id"])
    if result == "missing":
        raise HTTPException(status_code=404, detail="No student found with that code — check it letter by letter.")
    if result == "owned":
        raise HTTPException(status_code=409, detail=(
            "That code already belongs to another family account. If it's yours, "
            "email support@mrcadabra.com and a person will sort it out."))
    return _parent_payload(store.get_parent(parent["id"]))


# =============================================================================
# BETA PASS ADMIN (2026-07-31) -- Jim's generator
# -----------------------------------------------------------------------------
# Keyed on FORUM_MOD_KEY (Jim's one admin key). The /beta page shows a generator
# panel when opened as /beta?admin=<key>; these endpoints back it.
# =============================================================================

class BetaCreateIn(BaseModel):
    key: str = ""              # build hx: legacy body form; the header is preferred
    label: str = ""            # who this pass is for (shows only to Jim)
    uses: int = 5
    hours: int = 2


class BetaRevokeIn(BaseModel):
    key: str = ""              # build hx: legacy body form; the header is preferred
    code: str


def _require_admin(key: str, tier: str = "general") -> None:
    """BUILD ht (2026-08-18, Phase 5): THE GOD-KEY IS SPLIT (review Class F). One
    shared key used to gate forum moderation, the FULL database export (including
    parent password hashes) and destructive family resets -- so a leaked moderation
    key could exfiltrate or erase everything. Now:
      tier="general" -> FORUM_MOD_KEY    (admin panel, moderation, beta codes,
                                          diagnostics -- everything read-mostly)
      tier="export"  -> DATA_EXPORT_KEY  (the full DB snapshot download)
      tier="reset"   -> FAMILY_RESET_KEY (destructive student/family resets)
    A graver tier NEVER falls back to the general key, and an UNSET graver key is
    FAIL-CLOSED with a 503 that says exactly which env var to add in Render --
    silence is how the last two key problems shipped. Constant-time compare, as
    since build dg."""
    envname = {"general": "FORUM_MOD_KEY", "export": "DATA_EXPORT_KEY",
               "reset": "FAMILY_RESET_KEY"}.get(tier, "FORUM_MOD_KEY")
    admin = os.environ.get(envname, "").strip()
    if not admin:
        if tier == "general":
            raise HTTPException(status_code=401, detail="Not authorized.")
        raise HTTPException(status_code=503, detail=(
            f"This action is disabled until {envname} is set in Render "
            "(build ht split it from the general admin key on purpose)."))
    if not hmac.compare_digest((key or "").strip(), admin):
        raise HTTPException(status_code=401, detail="Not authorized.")


def _new_beta_code() -> str:
    for _ in range(60):
        code = f"TRY-{secrets.choice(_CODE_WORDS)}{secrets.randbelow(90) + 10}"
        if code in STUDENTS or store.get_account(code) or store.get_beta_code(code):
            continue
        return code
    return f"TRY-{secrets.token_hex(3).upper()}"


@app.post("/api/beta/create")
def beta_create(body: BetaCreateIn,
                x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    # build hx: the header is preferred (the key never rides a URL or a stored
    # request body); body.key stays accepted for any stale cached page.
    _require_db()
    _require_admin(x_admin_key or body.key)
    code = _new_beta_code()
    store.create_beta_code(code, body.label, body.uses, body.hours)
    return {"ok": True, "code": code, "codes": store.list_beta_codes()}


@app.get("/api/beta/list")
def beta_list(key: str = "",
              x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    # BUILD dg: the key belongs in the X-Admin-Key HEADER -- query strings are written
    # into Render's request logs in plaintext. The query param stays accepted so old
    # bookmarks keep working, but no page we ship sends it that way any more.
    _require_db()
    _require_admin(x_admin_key or key)
    return {"ok": True, "codes": store.list_beta_codes()}


@app.post("/api/beta/revoke")
def beta_revoke(body: BetaRevokeIn,
                x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    _require_db()
    _require_admin(x_admin_key or body.key)   # build hx: header preferred
    if not store.revoke_beta_code(body.code):
        raise HTTPException(status_code=404, detail="No pass with that code.")
    return {"ok": True, "codes": store.list_beta_codes()}


@app.post("/api/beta/delete")
def beta_delete(body: BetaRevokeIn,
                x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """2026-08-07 (build bb, Jim): fully DELETE a beta pass -- the pass row AND every
    scrap of student data recorded under that code (sessions, progress, quizzes, stats,
    time, awards, final exams, account). Revoke only disables the code and leaves the
    data; this is the true 'this tester never happened' button. Admin-key protected."""
    _require_db()
    _require_admin(x_admin_key or body.key)   # build hx: header preferred
    res = store.delete_beta_cascade(body.code)
    if not res.get("existed"):
        raise HTTPException(status_code=404, detail="No pass with that code.")
    return {"ok": True, "deleted": res.get("deleted") or {}, "codes": store.list_beta_codes()}


# =============================================================================
# ADMIN DASHBOARD (2026-08-03) -- Jim's one-stop status + tools page at /admin.
# Keyed on the SAME FORUM_MOD_KEY as the beta generator and forum moderation.
# Returns only aggregate COUNTS/TOTALS (store.admin_stats()) plus the same facts
# /health shows -- never a child's name, a parent's email, or a login code.
# =============================================================================

def _usage_with_dollars(days: int, since=None) -> dict:
    """store.usage_stats(days) plus estimated DOLLARS -- computed ONLY from prices Jim
    sets in Render env vars (nothing invented; dollars stay null until prices exist):
      ANTHROPIC_IN_USD_PER_MTOK   price per MILLION input tokens
      ANTHROPIC_OUT_USD_PER_MTOK  price per MILLION output tokens
      ELEVEN_USD_PER_1K_CHARS     price per 1,000 ElevenLabs characters
    Cache math per Anthropic's published multipliers: cached reads bill at 10% of the
    input price; cache writes at 125%."""
    u = store.usage_stats(days, since=since)
    def _price(name):
        try:
            v = os.environ.get(name, "").strip()
            return float(v) if v else None
        except ValueError:
            return None
    pin, pout = _price("ANTHROPIC_IN_USD_PER_MTOK"), _price("ANTHROPIC_OUT_USD_PER_MTOK")
    # BUILD jp: THE SECOND OPINION IS PRICED SEPARATELY, ON PURPOSE. LIVE_CRITIC is
    # seated with claude-opus-5, which is NOT priced like the teaching model, so
    # borrowing the teaching prices would understate the critic by several times over.
    # Unset means null means the tile says "—" and names the vars: never an invented
    # cost, and never a cost quietly computed at the wrong rate.
    cin, cout = _price("CRITIC_IN_USD_PER_MTOK"), _price("CRITIC_OUT_USD_PER_MTOK")
    ptts = _price("ELEVEN_USD_PER_1K_CHARS")
    brain_usd = tts_usd = None
    if pin is not None and pout is not None:
        brain_usd = round((u["input_tokens"] * pin
                           + u["cache_read_tokens"] * pin * 0.10
                           + u["cache_write_tokens"] * pin * 1.25
                           + u["output_tokens"] * pout) / 1_000_000, 2)
    if ptts is not None:
        tts_usd = round(u["tts_chars_generated"] / 1000 * ptts, 2)
        # (na) ⚠️ THE SAME DOLLARS, SPLIT ON WHY THEY WERE SPENT. store.py has already
        # separated the characters on mode; this only prices each half. tts_usd above
        # is UNCHANGED and still means build+serve -- the cost alarm and the 30-day
        # tiles read it and must keep reading the same number.
        u["tts_build_usd"] = round(u.get("tts_chars_build", 0) / 1000 * ptts, 2)
        u["tts_serve_usd"] = round(u.get("tts_chars_serve", 0) / 1000 * ptts, 2)
    else:
        u["tts_build_usd"] = u["tts_serve_usd"] = None
    critic_usd = None
    if cin is not None and cout is not None:
        critic_usd = round((u.get("critic_input_tokens", 0) * cin
                            + u.get("critic_cache_read_tokens", 0) * cin * 0.10
                            + u.get("critic_cache_write_tokens", 0) * cin * 1.25
                            + u.get("critic_output_tokens", 0) * cout) / 1_000_000, 2)
    u["critic_usd"] = critic_usd
    u["brain_usd"] = brain_usd
    u["tts_usd"] = tts_usd
    u["total_usd"] = round(brain_usd + tts_usd + (critic_usd or 0.0), 2) \
        if (brain_usd is not None and tts_usd is not None) else None
    # (na) BUILD vs SERVE, IN DOLLARS. The two questions the old single total could
    # not tell apart:
    #   build_usd -- what it cost to MAKE the course. Paid once. Capital.
    #   serve_usd -- what it costs to TEACH. Paid every hour. Marginal.
    # Every brain and critic token is serve: nothing pre-generates teaching turns.
    # Only the voice splits, and it splits on the render passes named in
    # store.TTS_BUILD_MODES.
    u["build_usd"] = u["tts_build_usd"]
    u["serve_usd"] = (round((brain_usd or 0.0) + (critic_usd or 0.0)
                            + (u["tts_serve_usd"] or 0.0), 2)
                      if (brain_usd is not None and u["tts_serve_usd"] is not None)
                      else None)
    # (mq) COST PER STUDENT-HOUR -- the number Jim actually asked for on 2026-08-24,
    # and the only cost figure that means anything as the app grows. Cost per STUDENT
    # flatters a quiet week and punishes a busy one; an HOUR of teaching is the unit
    # the product is actually sold in.
    # ⚠️ NULL, NEVER ZERO, when there are no hours yet. Dividing by nothing and
    # printing "$0.00 per hour" would read as "teaching is free", which is the exact
    # opposite of unmeasured.
    mins = store.student_minutes_since(since=since, days=(0 if since is not None
                                                          else int(days)))
    u["student_minutes"] = int(mins or 0)
    u["student_hours"] = round(mins / 60.0, 1) if mins else 0.0
    # ⚠️ (na) 2026-08-24 -- THIS KEY CHANGED MEANING. IT NOW DIVIDES SERVE COST, NOT
    # TOTAL COST. Jim's dashboard read "$610.76 per student-hour", which was true
    # arithmetic and a false statement: it was dividing ~$1,000 of ONE-TIME course
    # construction by ONE WEEK of children's hours. Render the course again next
    # month and the number would double while teaching got no more expensive; teach
    # ten times as many children and it would collapse while nothing improved.
    # The question "what does an hour of teaching cost?" has exactly one honest
    # numerator, and it is serve_usd.
    # The blended figure is NOT lost -- total_usd is right above, and build_usd is
    # reported beside it so the capital cost is visible instead of smuggled.
    u["usd_per_student_hour"] = (round(u["serve_usd"] / (mins / 60.0), 2)
                                 if (u.get("serve_usd") is not None and mins) else None)
    # (na) kept so the old blended figure stays inspectable rather than deleted --
    # nothing displays it as a headline any more, but a number that vanishes with no
    # trace is how a dashboard loses an argument with its own history.
    u["usd_per_student_hour_blended"] = (round(u["total_usd"] / (mins / 60.0), 2)
                                         if (u["total_usd"] is not None and mins) else None)
    return u


@app.get("/api/admin/stats")
def admin_stats_api(key: str = "",
                    x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """The numbers behind /admin. Admin-key protected (constant-time compare).
    BUILD dg: key accepted in the X-Admin-Key header (preferred -- query strings land
    in Render's logs); the query param stays for old bookmarks only."""
    _require_db()
    _require_admin(x_admin_key or key)
    # (mq) Read the epoch ONCE, before the payload, so the two keys below cannot
    # disagree -- a panel whose header says one era and whose tiles measure another
    # is worse than no epoch at all.
    _ep = store.get_cost_epoch()
    return {
        "ok": True,
        "build": APP_BUILD,
        # (qg) the brain SEAT, not the Anthropic default: /admin must say who is
        # actually teaching -- provider, model, thinking effort, and the reason a
        # configured seat fell back, if it did.
        "model": tutor.active_brain()["model"],
        "brain": tutor.active_brain(),
        # build ny (latency deep dive): the SEATS, visible. The critic tile used to
        # hardcode "Opus reads" -- if Jim A/Bs a faster critic model the panel must
        # tell the truth about which model is actually in the seat.
        "critic_seat": (lambda _s: {"provider": _s[0] or "off", "model": _s[1] or ""})(
            tutor._live_critic_seat()),
        "prompt_cache_ttl": (os.environ.get("PROMPT_CACHE_TTL", "") or "5m (default)"),
        "payments_open": _payments_open(),
        "storage": store.status(),
        "stats": store.admin_stats(),
        "usage7": _usage_with_dollars(7),
        "usage30": _usage_with_dollars(30),
        # (mq) THE COST EPOCH. `usage_epoch` is None until Jim starts an era, so the
        # panel shows the trailing windows exactly as it always has and the new tiles
        # simply do not appear. Nothing about the old view changes on deploy.
        "cost_epoch": (_ep.isoformat() if _ep else None),
        "usage_epoch": (_usage_with_dollars(0, since=_ep) if _ep else None),
        # OPS (2026-08-05): unhandled-error visibility for the System section.
        "errors24": store.errors_count(24),
        "errors_recent": store.recent_errors(24, 20),
    }


class CostEpochIn(BaseModel):
    key: str = ""
    note: str = ""
    clear: bool = False          # go back to measuring all of history


@app.post("/api/admin/cost-epoch")
def admin_cost_epoch(body: CostEpochIn,
                     x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """(mq) START A NEW COST MEASUREMENT ERA -- Jim, 2026-08-24: "we should zero out
    our current cost measurement so it is measuring cost based on how we do it now."

    ⚠️ IT DELETES NOTHING. Not one usage_log row is touched; the 7- and 30-day panels
    keep working unchanged. This writes a timestamp, and the cost tiles gain a second
    reading measured from it. The reason Jim needs one is that the trailing windows
    are dominated by ONE-TIME spend -- ~$806 to render the course -- which says
    nothing about what teaching a child costs today and would go on saying nothing
    for a month.

    Idempotent in the only sense that matters: a second call simply starts a newer
    era, and the older marker stays in the ledger."""
    _require_db()
    _require_admin(x_admin_key or body.key)
    if body.clear:
        store.clear_cost_epoch(body.note)
        return {"ok": True, "cost_epoch": None,
                "note": "Measuring all of history again. Nothing was deleted."}
    stamp = store.set_cost_epoch(body.note)
    return {"ok": True, "cost_epoch": stamp or None,
            "note": ("Cost is now measured from this moment. Every earlier row is "
                     "still in the usage log and the 7- and 30-day panels are "
                     "unchanged.")}


# =============================================================================
# BACKUP ENDPOINTS (2026-08-11, build dj) -- download and status. READ-ONLY both:
# there is deliberately NO restore endpoint (a remote wipe-and-replace is a foot-gun;
# restores run offline via restore_backup.py with an explicit flag). Key rides in the
# X-Admin-Key header like every admin call since build dg.
# =============================================================================
@app.get("/api/admin/backup/status")
def admin_backup_status(key: str = "",
                        x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """What the nightly snapshot has been doing: every snapshot on the persistent
    disk, newest first, plus the retention setting. Feeds the /admin Backups card."""
    _require_admin(x_admin_key or key)
    snaps = []
    try:
        for p in sorted(_BACKUP_DIR.glob("backup-*.json.gz"), reverse=True):
            st = p.stat()
            snaps.append({"name": p.name, "bytes": st.st_size,
                          "written_utc": time.strftime("%Y-%m-%d %H:%M UTC",
                                                       time.gmtime(st.st_mtime))})
    except OSError:
        pass
    return {"ok": True, "db": store.enabled(), "keep": BACKUP_KEEP,
            "dir": str(_BACKUP_DIR), "snapshots": snaps}


# =============================================================================
# THE NIGHT WATCH CARD (2026-08-17, build gp)
# -----------------------------------------------------------------------------
# go shipped the governor and forgot to give it a face: the findings went to a markdown
# file on the persistent disk that nothing served, so the only readable output was a
# one-line count in the Render log. A governor whose reports are hard to reach is a
# governor that gets ignored -- go's own header says so, and go proved it in twelve hours.
@app.get("/api/admin/events")
def admin_events(key: str = "",
                 x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """build ha: the telemetry card's feed. 7- and 30-day event counts grouped
    kind -> name -> count, plus the newest alarming events (crashes, client errors,
    pass-throughs) so a spike has faces, not just a number."""
    _require_admin(x_admin_key or key)
    return {
        "ok": True,
        "stats7": store.event_stats(7),
        "stats30": store.event_stats(30),
        "recent": store.recent_events(hours=168, limit=50,
                                      kinds=["referee_crash", "clienterror",
                                             "pass_through", "failopen", "promptsize"]),
    }


@app.get("/api/admin/seat-check")
def admin_seat_check(provider: str = "", model: str = "", effort: str = "",
                     size: str = "", course: str = "", key: str = "",
                     x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """(qh, widened in qi) ONE cheap call to a brain seat, and the vendor's own words
    back if it fails.

    ⚠️ WHY THIS EXISTS. Build qg moved the teaching seat to DeepSeek and the first
    night on it produced 120 fail-opens -- every turn of every lesson an apology --
    because the seat raised on every call. Nothing anywhere could answer "does the
    configured seat actually work?" without spending a child's turn to find out.

    ⭐ AND IT TESTS A SEAT THAT IS NOT LIVE. Jim, 2026-08-30: "the problem was somehow
    the DeepSeek wasn't being called." That question is only answerable by TRYING
    DeepSeek -- and after the outage the live seat is (rightly) back on Anthropic. So
    ?provider=deepseek tests DeepSeek while production keeps teaching on Anthropic.
    ?model= and ?effort= override the env for the test only; nothing here changes what
    any child gets.

    ⭐ REACHED vs REFUSED. The single most useful bit: `reached` is false when the call
    NEVER GOT THERE (DNS, egress, TLS -- tutor.BrainUnreachable) and true when the
    vendor answered and said no (401/404/400). Those are different problems with
    different fixes, and the outage looked identical either way.

    Never raises: a broken seat returns ok=false WITH the reason, which is the whole
    point of the endpoint."""
    _require_admin(x_admin_key or key)
    seat = tutor.active_brain()
    want = (provider or seat.get("provider") or "anthropic").strip().lower()
    if want not in ("anthropic", "deepseek", "openai"):
        return {"ok": False, "reached": False, "seat": seat, "tested": {},
                "error": f"unknown provider {want!r}",
                "verdict": "that is not a seat this app knows.",
                "remedy": "provider must be anthropic, deepseek or openai."}
    if want == "deepseek":
        use_model = model or os.environ.get("DEEPSEEK_TUTOR_MODEL",
                                            tutor.DEFAULT_DEEPSEEK_TUTOR_MODEL)
        use_effort = (effort or tutor.deepseek_effort()).strip().lower()
        api_key = os.environ.get("DEEPSEEK_API_KEY", "")
        key_name = "DEEPSEEK_API_KEY"
    elif want == "openai":
        use_model = model or os.environ.get("OPENAI_TUTOR_MODEL",
                                            tutor.DEFAULT_OPENAI_TUTOR_MODEL)
        use_effort, api_key = "", os.environ.get("OPENAI_API_KEY", "")
        key_name = "OPENAI_API_KEY"
    else:
        use_model = model or os.environ.get("CLAUDE_MODEL", tutor.DEFAULT_MODEL)
        use_effort, api_key = "", os.environ.get("ANTHROPIC_API_KEY", "")
        key_name = "ANTHROPIC_API_KEY"
    out = {"ok": False, "reached": False, "seat": seat, "error": "",
           "verdict": "", "remedy": "", "reply": "", "seconds": 0.0,
           "tested": {"provider": want, "model": use_model, "effort": use_effort}}
    if not api_key:
        out["error"] = f"there is no {key_name} in this service's environment"
        out["verdict"] = f"{want} has no key here, so nothing was sent."
        out["remedy"] = f"add {key_name} in Render -> Environment."
        return out
    # (qj) ⭐ THE SIZE THE REAL LESSON SENDS. The qi button asked a fifteen-token
    # question and reported "this seat works" -- while every REAL turn, which carries
    # the ~46k-token cached teaching prompt, had been failing all night. A preflight
    # that does not reproduce production conditions does not vouch for them; it
    # gives false confidence, which is worse than no check at all. size=lesson builds
    # the ACTUAL system prompt the tutor sends (build_system_prompt, the same call
    # the pipeline makes) and the same 3000-token ceiling.
    big = str(size or "").strip().lower() in ("lesson", "real", "full", "big")
    if big:
        try:
            sys_text = tutor.build_system_prompt({"name": "Seat Check", "code": "SEATCHK"},
                                                 course or "prealgebra")
        except Exception as exc:  # noqa: BLE001 -- fall back to the small probe, loudly
            sys_text = "You are a maths tutor. Answer in one short sentence."
            out["error"] = f"(could not build a real lesson prompt: {exc}) "
            big = False
    else:
        sys_text = "You are a maths tutor. Answer in one short sentence."
    out["prompt_chars"] = len(sys_text)
    out["size"] = "lesson" if big else "small"
    t0 = time.time()
    try:
        if want == "deepseek":
            client = tutor.deepseek_brain(api_key, effort=use_effort)
        elif want == "openai":
            client = tutor._OpenAIBrain(api_key)
        else:
            client = tutor.Anthropic(api_key=api_key,
                                     timeout=tutor.ANTHROPIC_TIMEOUT_S, max_retries=0)
        resp = client.messages.create(
            model=use_model, max_tokens=3000 if big else 64,
            system=tutor._cacheable_system(sys_text) if big else sys_text,
            messages=[{"role": "user", "content": "What is 2 plus 2?"}])
        text = "".join(b.text for b in resp.content
                       if getattr(b, "type", None) == "text")
        # (qk) THE TOKENS, so a SECOND press proves whether the prefix cache is warm.
        # 21.9s on the first real-size DeepSeek call is a COLD 46k prompt; if the
        # cache works, the next identical call is far cheaper and faster, and that
        # difference decides whether this seat can teach a child at all.
        tk = {}
        try:
            tutor._add_usage(tk, resp)
        except Exception:  # noqa: BLE001 -- counts are a bonus, never a failure
            tk = {}
        out.update(reached=True, ok=bool(text.strip()), reply=text.strip()[:200],
                   seconds=round(time.time() - t0, 2),
                   tokens_in=tk.get("in", 0), tokens_out=tk.get("out", 0),
                   tokens_cached=tk.get("cr", 0))
        if out["ok"]:
            out["verdict"] = (
                f"{want}/{use_model} answered in {out['seconds']}s with a "
                f"{out['size']} prompt ({out['prompt_chars']:,} characters). "
                + ("This seat works on a REAL lesson-sized turn."
                   if big else
                   "⚠️ This was a TINY prompt. A real turn sends ~185,000 characters "
                   "-- press the lesson-size test before trusting the seat."))
            # (qk) ⭐ WORKING IS NOT THE SAME AS USABLE. Build ny measured a whole
            # Sonnet turn at ~16s, of which 12.3s is the teaching call, and Jim
            # already called that slow. A turn can spend this TWICE MORE
            # (MATHCHECK_MAX_ATTEMPTS = 3) before a child sees a word, plus the
            # critic seat if one is filled. So the seconds below are a floor, not
            # an estimate -- and a seat that passes can still be unfit to teach.
            if big and out["seconds"] > 12:
                worst = round(out["seconds"] * tutor.MATHCHECK_MAX_ATTEMPTS, 1)
                out["remedy"] = (
                    f"⚠️ TOO SLOW TO TEACH AS IT STANDS. {out['seconds']}s is one "
                    f"call; a refereed turn may make up to {tutor.MATHCHECK_MAX_ATTEMPTS} "
                    f"(~{worst}s) before the child sees anything, and Sonnet's whole "
                    "turn is ~16s. Press this button AGAIN -- if 'cached' jumps and "
                    "the seconds fall, the first call was just a cold prefix. If it "
                    "stays this slow, try thinking off, or the flash model.")
            elif big:
                out["remedy"] = (f"{out['seconds']}s for one call, against ~12.3s for "
                                 "the Sonnet baseline. Press again to see the cached "
                                 "figure.")
        else:
            out["error"] = "the seat answered with EMPTY text"
            out["verdict"] = f"{want}/{use_model} replied, but said nothing."
            out["remedy"] = ("the call succeeded and produced no words -- for a "
                             "thinking model that usually means the whole budget went "
                             "to reasoning. Try effort=off.")
        return out
    except Exception as exc:  # noqa: BLE001 -- reporting the failure IS the job
        msg = " ".join(str(exc).split())[:400]
        low = msg.lower()
        unreachable = isinstance(exc, tutor.BrainUnreachable) or any(
            w in type(exc).__name__.lower() for w in ("connection", "timeout"))
        out.update(error=(out.get("error") or "") + msg, reached=not unreachable,
                   seconds=round(time.time() - t0, 2))
        if unreachable:
            out["verdict"] = (f"the request NEVER REACHED {want} -- this service could "
                              "not open the connection.")
            out["remedy"] = ("this is the network, not the model name and not the key. "
                             "Check that this service can make outbound calls to that "
                             "host (a proxy, a firewall, a region block, or DNS), and "
                             "whether the vendor is up.")
        elif "not found" in low or "404" in low:
            out["verdict"] = (f"{want} answered and does not serve {use_model!r} on "
                              "this key.")
            out["remedy"] = ("set the model env var to a name it does serve "
                             "(DEEPSEEK_TUTOR_MODEL / CLAUDE_MODEL / "
                             "OPENAI_TUTOR_MODEL), then test again.")
        elif "401" in low or "403" in low or "auth" in low or "invalid" in low:
            out["verdict"] = f"{want} answered and refused the key."
            out["remedy"] = (f"check {key_name} in Render for a stray space, a "
                             "truncated paste, or a key from the wrong account.")
        elif "400" in low:
            out["verdict"] = f"{want} answered and refused the REQUEST itself."
            out["remedy"] = ("read the message above -- if it names thinking or "
                             "reasoning_effort, test again with effort=off.")
        else:
            out["verdict"] = f"{want} failed, and its own words are above."
            out["remedy"] = "start with the message; it is the vendor's, not ours."
        if big:
            out["remedy"] += (" ⚠️ This was the LESSON-SIZED prompt "
                              f"({out['prompt_chars']:,} characters). If the small "
                              "test passes and this one does not, the problem is the "
                              "SIZE or duration of a real turn, not the seat's "
                              "identity -- that is the shape of the 2026-08-30 "
                              "outage.")
        return out


@app.get("/api/admin/nightwatch/status")
def admin_nightwatch_status(key: str = "",
                            x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """Last night's counts, the refuted ratio (the health metric), the findings that keep
    coming back, and which nights are readable. Feeds the /admin Night watch card."""
    _require_admin(x_admin_key or key)
    if nightwatch is None:
        return {"ok": False, "enabled": False, "reports": [], "last": "",
                "note": "nightwatch.py is not deployed on this build"}
    return nightwatch.summary(DATA_DIR)


@app.get("/api/admin/nightwatch/report")
def admin_nightwatch_report(date: str = "", key: str = "",
                            x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """One night's full report as markdown text. `date` is YYYY-MM-DD and is validated as
    a date inside nightwatch.read_report, so no path can be traversed from here."""
    _require_admin(x_admin_key or key)
    if nightwatch is None:
        raise HTTPException(status_code=404, detail="nightwatch.py is not deployed")
    text = nightwatch.read_report(DATA_DIR, date)
    if not text:
        raise HTTPException(status_code=404, detail=f"no night-watch report for {date!r}")
    return {"ok": True, "date": date, "markdown": text}


@app.get("/api/admin/backup")
def admin_backup_download(key: str = "",
                          x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """A FRESH full snapshot, streamed as a download -- not a file from the disk, so
    what Jim saves is the database as of this click. This is the offsite copy: the
    nightly file protects against deploys and app mistakes; this one protects against
    losing Render itself.
    build ht: EXPORT tier -- this download contains every family's data including
    parent password hashes, so it demands DATA_EXPORT_KEY, never the general key."""
    _require_admin(x_admin_key or key, tier="export")
    _require_db()
    blob, counts = _backup_blob()
    fname = "mrcadabra-backup-" + time.strftime("%Y%m%d-%H%M%S", time.gmtime()) + ".json.gz"
    return Response(blob, media_type="application/gzip",
                    headers={"Content-Disposition": f'attachment; filename="{fname}"',
                             "X-Backup-Rows": str(sum(counts.values())),
                             "X-Backup-Tables": str(len(counts))})


# =============================================================================
# ADMIN "START FRESH" (2026-08-05) -- full reset of ONE parent account by email.
# -----------------------------------------------------------------------------
# Jim's testing tool: delete his own parent account so he can re-run the brand-
# new-parent signup with the same email and see the site exactly as a first-time
# visitor would. Admin-key gated (same FORUM_MOD_KEY as every other admin tool),
# scoped to the ONE email passed in. It deletes that parent + their children +
# all their data (store.delete_parent_cascade, atomic); it never touches another
# account, the admin key, or any Render env var.
# =============================================================================

class ParentResetAdminIn(BaseModel):
    key: str
    email: str


class PrewarmAdminIn(BaseModel):
    key: str
    course: str = ""       # blank = every course
    limit: int = 0         # 0 = no cap; otherwise render at most this many this call
    dry_run: bool = False   # count and price it without spending anything


class CourseTrialIn(BaseModel):
    key: str
    course: str = "prealgebra"   # which level to walk
    validate_units: int = 3      # how many opening units the student "validates" on the
                                 # Course Assessment rather than actually passing


class LessonAuditIn(BaseModel):
    key: str
    limit: int = 2          # scenarios THIS call -- a lesson takes a minute or two
    offset: int = 0         # where to start, so the cast can be walked in batches
    turns: int = 0          # 0 = the file's default
    dry_run: bool = False   # price it and spend nothing


@app.post("/api/admin/course-trial")
def admin_course_trial(body: CourseTrialIn):
    """Run THE FULL-JOURNEY TRIAL from the dashboard and hand back the report.

    2026-08-13 (build fc). Jim: "is it possible to build that into the admin dashboard?
    And maybe it could even ask a couple of questions like, what do you want to trial? Or
    maybe it just runs a trial like you just did, and it reports back to me."

    It walks ONE student's whole life through the real app: sign up -> validate the first
    N units on the Course Assessment -> work the rest -> meet the LOCKED Final Exam and
    read what it says -> go back and pass the owed quizzes -> take the exam -> Course
    Champion in the trophy case -> and the same picture on the parent AND teacher views.
    On its first ever run it found a live bug (see course_trial.py's notes), which is the
    argument for having it one click away instead of only on a laptop.

    ⚠️ IT NEVER TOUCHES PRODUCTION DATA. course_trial.py runs as a SEPARATE PROCESS with
    DATABASE_URL and DATA_DIR pointed at a throwaway temp directory, so the parent, child,
    teacher and class it creates live and die there. That isolation is the whole reason
    this is a subprocess rather than an in-process call -- the store is a module-level
    singleton and there is no safe way to swap its engine underneath a live server.

    ⚠️ AND IT REFUSES TO RUN IF THE BOX IS TIGHT. A second interpreter importing the app
    costs ~120 MB; on Render's free 512 MB instance that is affordable but not free. If
    less than MIN_TRIAL_MB is available we decline with a plain message rather than risk
    the OOM killer taking the live web service down in the middle of someone's lesson."""
    _require_admin(body.key)
    trial = BASE_DIR / "course_trial.py"
    if not trial.exists():
        raise HTTPException(status_code=503, detail="course_trial.py is not on this deploy.")
    course = (body.course or "prealgebra").strip()
    if course not in curriculum.COURSES:
        raise HTTPException(status_code=400, detail=f"'{course}' is not one of the courses.")
    n_units = len(curriculum.units_for(course))
    validate = max(1, min(int(body.validate_units or 3), n_units - 1))

    # Memory guard -- an honest refusal beats an OOM-killed web service.
    MIN_TRIAL_MB = 200
    try:
        with open("/proc/meminfo") as fh:
            avail_kb = next(int(l.split()[1]) for l in fh if l.startswith("MemAvailable"))
        avail_mb = avail_kb // 1024
        if avail_mb < MIN_TRIAL_MB:
            raise HTTPException(status_code=503, detail=(
                f"Not enough free memory to run the trial right now ({avail_mb} MB free; "
                f"it needs about {MIN_TRIAL_MB}). It runs in its own process so it can't "
                f"touch real data, and that costs memory. Try again in a moment."))
    except HTTPException:
        raise
    except Exception:  # noqa: BLE001 -- no /proc here: proceed rather than block
        pass

    import subprocess as _sp
    import sys as _sys          # main.py does not import sys at module level
    import tempfile as _tf
    import json as _json
    with _tf.TemporaryDirectory() as tmp:
        env = dict(os.environ)
        env["DATABASE_URL"] = "sqlite:///" + os.path.join(tmp, "trial.db")
        env["DATA_DIR"] = tmp                 # keep its cache + files out of /var/data
        env["WEEKLY_EMAIL"] = "off"
        env["PYTHONPATH"] = str(BASE_DIR) + os.pathsep + env.get("PYTHONPATH", "")
        try:
            r = _sp.run([_sys.executable, str(trial), "--json", "--course", course,
                         "--validate", str(validate)],
                        cwd=str(BASE_DIR), env=env, capture_output=True, text=True,
                        timeout=180)
        except _sp.TimeoutExpired:
            raise HTTPException(status_code=504, detail=(
                "The trial did not finish within three minutes. That is itself a finding "
                "-- something in the journey is hanging."))
    out = r.stdout or ""
    marker = "<<<COURSE-TRIAL-JSON>>>"
    if marker not in out:
        raise HTTPException(status_code=500, detail=(
            "The trial did not produce a report. Last output: " + (out + r.stderr)[-500:]))
    try:
        report = _json.loads(out.split(marker, 1)[1].strip())
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Unreadable trial report: {exc}")
    report["exit_code"] = r.returncode
    return report



# =============================================================================
# THE SCRIPTED LESSON LANE (build jt, 2026-08-21) -- Jim's scripted-first ruling.
# -----------------------------------------------------------------------------
# The engine (lessonscripts.py) is pure and battery-verified; this is its server.
# Three invariants, each of which PART 3cw pins:
#   1. NO ANSWER EVER REACHES THE CLIENT. The engine's "expected" stays server-side;
#      every payload is sanitized. Grading is code, here, always.
#   2. THE MODEL NEVER STEERS. A wrong answer buys at most SCRIPT_AI_TURNS bounded
#      Model-Lead-Test turns on that one problem; the redo is graded by CODE against
#      the known answer, and the engine's own retest resumes the script. If the AI
#      fails or is unreachable, the lesson falls back to the scripted retest -- a
#      dead model costs a child one worked example, never the lesson.
#   3. A SCRIPT TURN COSTS NOTHING. Every non-intervention request is served from
#      data, logged kind="script" with its wall time -- so /admin's usage log can
#      prove the pilot's latency claim with the same instrument jm built.
# Sessions are in-memory (state is ~200 bytes; a deploy mid-lesson restarts the
# lesson -- acceptable for the pilot and HONEST: better than resuming corrupted).
# =============================================================================
SCRIPT_AI_TURNS = int(os.environ.get("SCRIPT_AI_TURNS", "3") or 3)
_SCRIPT_SESSIONS: dict = {}
_SCRIPT_TTL_S = 2 * 3600

# =============================================================================
# (uh, 2026-09-08) THE DEMO LESSON LANE -- P3 OF THE DEEP LOOK
# -----------------------------------------------------------------------------
# The review: "the demo is a tour of the furniture with an empty board; it never
# shows a lesson, while the app has a hundred and more authored lessons that draw
# the picture before the rule." Jim chose P3 after P0/P2/P1.
#
# ONE COURSE, ONE LESSON, THE REAL ENGINE. /api/demo/lesson/start picks the course's
# FIRST authored lesson (DEMO_LESSON_BY_COURSE, derived from COURSE_ORDER so a
# re-cut course moves it by itself), runs lessonscripts.start + step("begin") with a
# FIXED seed (every visitor hears the same opening), and returns the beats up to the
# first ask through the same _script_clean the classroom uses -- never an answer key.
# /api/demo/lesson/answer grades a tap or typed words with the same code paths
# (read_answer, reason_option_for, ans()) and returns the engine's own praise,
# walk-back and next beat.
#
# WHAT IT DELIBERATELY DOES NOT DO. No student, so nothing is written to the store
# (no record_topic, no script_done, no script_answers, no streak) and no student
# code is needed or accepted. No model: the engine's `intervene` step (the one door
# to the AI in the classroom) is answered here by the engine's own "resume" -- the
# retest problem -- exactly as the classroom does when the model is unreachable.
# Sessions are opaque tokens in memory, capped and short-lived; a visitor gets at
# most DEMO_LESSON_MAX_ANSWERS graded answers per token. The VOICE rides the
# "demo" lane of /api/speak-prep: closure-only and cache-only (mj's drill rule), so
# a visitor can never make the paid renderer run.
# =============================================================================
_DEMO_LESSON_SESSIONS: dict = {}
_DEMO_LESSON_TTL_S = 30 * 60
_DEMO_LESSON_CAP = 800
DEMO_LESSON_SEED = 7
DEMO_LESSON_MAX_ANSWERS = 8


def _demo_lesson_by_course() -> dict:
    """{course: lesson_id} -- the first authored lesson of each course, in the course
    order the picker and the classroom use. Derived, never hand-kept."""
    out = {}
    try:
        for lid in lessonscripts.COURSE_ORDER:
            les = lessonscripts.LESSON_BY_ID.get(lid) or {}
            c = les.get("course")
            if c and c not in out:
                out[c] = lid
    except Exception as exc:  # noqa: BLE001
        print(f"[demo-lesson] course walk failed: {exc}")
    return out


def _demo_lesson_session(token: str):
    now = _time.monotonic()
    for k in [k for k, v in _DEMO_LESSON_SESSIONS.items()
              if now - v.get("t0", now) > _DEMO_LESSON_TTL_S]:
        _DEMO_LESSON_SESSIONS.pop(k, None)
    return _DEMO_LESSON_SESSIONS.get((token or "").strip())


class DemoLessonStartIn(BaseModel):
    course: str = "entry"


class DemoLessonAnswerIn(BaseModel):
    token: str
    value: int | None = None
    said: str | None = None
    unheard: bool = False


@app.get("/api/demo/lesson/levels")
def demo_lesson_levels():
    """The picker: every course with an authored first lesson, its title, unit and
    topic. Public and harmless: titles only."""
    titles = {}
    try:
        titles = {k: v.get("title", k) for k, v in curriculum.COURSES.items()}
    except Exception as exc:  # noqa: BLE001
        print(f"[demo-lesson] course titles unavailable: {exc}")
    out = []
    for cid, lid in _demo_lesson_by_course().items():
        les = lessonscripts.LESSON_BY_ID.get(lid) or {}
        out.append({"course": cid, "title": titles.get(cid, cid), "lesson_id": lid,
                    "topic": les.get("topic", ""), "unit": les.get("unit", 1)})
    return {"ok": True, "levels": out}


@app.post("/api/demo/lesson/start")
def demo_lesson_start(body: DemoLessonStartIn, request: Request):
    _rate_limit("demo-lesson:" + (request.client.host if request.client else "?"),
                limit=40, window_seconds=600, what="demo lessons")
    course = (body.course or "").strip().lower()
    lid = _demo_lesson_by_course().get(course)
    lesson = lessonscripts.LESSON_BY_ID.get(lid or "")
    if not lesson:
        raise HTTPException(status_code=404, detail="No demo lesson for that level.")
    state = lessonscripts.start(lesson, seed=DEMO_LESSON_SEED)
    steps, state = lessonscripts.step(lesson, state, ("begin",))
    token = secrets.token_urlsafe(18)
    if len(_DEMO_LESSON_SESSIONS) >= _DEMO_LESSON_CAP:
        _DEMO_LESSON_SESSIONS.pop(next(iter(_DEMO_LESSON_SESSIONS)), None)   # oldest-in first
    _DEMO_LESSON_SESSIONS[token] = {"state": state, "lesson": lesson, "answers": 0,
                                    "t0": _time.monotonic()}
    titles = {}
    try:
        titles = {k: v.get("title", k) for k, v in curriculum.COURSES.items()}
    except Exception:  # noqa: BLE001
        pass
    return {"ok": True, "token": token, "course": course,
            "title": titles.get(course, course), "topic": lesson.get("topic", ""),
            "unit": lesson.get("unit", 1), "lesson_id": lesson.get("id", ""),
            "steps": _script_clean(steps, lesson["id"])}


@app.post("/api/demo/lesson/answer")
def demo_lesson_answer(body: DemoLessonAnswerIn, request: Request):
    """One graded answer, the classroom's own three doors (tap, typed words, the
    reason question) without the store, the streak or the model."""
    sess = _demo_lesson_session(body.token)
    if not sess:
        raise HTTPException(status_code=409, detail=(
            "That demo lesson has ended -- start it again."))
    if sess["answers"] >= DEMO_LESSON_MAX_ANSWERS:
        raise HTTPException(status_code=429, detail="That is plenty for a demo -- try the classroom.")
    lesson, state = sess["lesson"], sess["state"]
    pre = []

    right = None

    def _finish(steps_out):
        """Play `intervene` (the AI's door) as the engine's own resume, and never
        ship an answer key. Every `end` simply ends -- nothing to record. `right`
        is the engine's own verdict, so the page can end the excerpt after ONE
        right answer without ever holding the key."""
        out = list(pre)
        for st in steps_out:
            if st["kind"] == "intervene":
                more, st2 = lessonscripts.step(lesson, sess["state"], ("resume",))
                sess["state"] = st2
                out.extend(_script_clean(more, lesson["id"]))
            else:
                out.extend(_script_clean([st], lesson["id"]))
        return {"ok": True, "steps": out, "right": right,
                "answers_left": max(0, DEMO_LESSON_MAX_ANSWERS - sess["answers"])}

    # the reason question, by its label (sp)
    if (state.get("pending") or {}).get("reason"):
        label = lessonscripts.reason_option_for(lesson, body.said or "")
        if body.unheard or not label:
            got = lessonscripts.read_answer(body.said or "")
            if got["kind"] == "unsure":
                pre.append({"kind": "say", "spoken": lessonscripts.LINE_UNSURE, "board": ""})
            steps, state = lessonscripts.step(lesson, state, ("unheard",))
            sess["state"] = state
            return _finish(steps)
        sess["answers"] += 1
        right = bool(lessonscripts.reason_right(lesson, label))
        steps, state = lessonscripts.step(lesson, state, ("answer", label))
        sess["state"] = state
        return _finish(steps)

    # typed or spoken words become the integer a tap would send (ou)
    if body.value is None and (body.said or "").strip():
        got = lessonscripts.read_answer(body.said)
        if got["kind"] == "value":
            body.value = got["value"]
        else:
            if got["kind"] == "notwhole":
                pre.append({"kind": "say", "spoken": lessonscripts.LINE_WHOLE, "board": ""})
            elif got["kind"] == "unsure":
                pre.append({"kind": "say", "spoken": lessonscripts.LINE_UNSURE, "board": ""})
            body.unheard = True

    if body.unheard or body.value is None:
        steps, state = lessonscripts.step(lesson, state, ("unheard",))
        sess["state"] = state
        return _finish(steps)
    sess["answers"] += 1
    _pend = (state.get("pending") or {}).get("problem")
    right = bool(_pend is not None and int(body.value) == lessonscripts.ans(_pend))
    steps, state = lessonscripts.step(lesson, state, ("answer", int(body.value)))
    sess["state"] = state
    return _finish(steps)
# (rj, 2026-09-01) THE SEAM'S MEMORY. When a scripted lesson ends, _script_finish
# leaves a one-entry note here so the very next __script_done__ chat turn can tell
# the live tutor WHICH lesson just ended and whether it was mastered -- Jim watched
# the unannounced handoff ("acted as if we had been working on subtraction") and
# ruled: announce it, then continue. Read-and-popped by the chat route; in-memory
# like the sessions themselves (a deploy loses at most one announcement).
_SCRIPT_DONE_NOTES: dict = {}


def _script_intervene(code, course, context, history):
    """Module-level seam so ruletests can stub the model out (PART 3cw)."""
    return tutor.script_intervention(code, course, context, history)


_AI_TAG = re.compile(r"\[\[[^\]]*\]\]")


def _split_ai_reply(reply: str):
    """(pv) Split an intervention reply into (spoken prose, board tags).

    ⚠️ WHY THIS EXISTS. The intervention returned {"kind": "ai", "spoken": reply,
    "board": ""} -- the model's WHOLE reply, tags and all, in the SPOKEN field. The
    scripted player renders `spoken` as bubble text and `board` through handleTags,
    so every [[step]] and [[choices]] the model wrote was PRINTED TO THE CHILD as
    literal text. Jim's screenshot shows exactly that:

        [[step eq="9 + 0 = 9"]]
        [[step eq="2 + 0 = 2"]]
        [[choices options="61 | 151 | 29"]]

    ...sitting in the bubble as words, with an empty whiteboard beside them. Every
    other step kind in this lane carries prose in `spoken` and tags in `board`; the
    AI step was the one that did not, so it is split here to match. The live lane
    never had this bug because its client parses tags out of the reply itself.

    Never raises: on any surprise the reply is returned unsplit, which is exactly
    today's behaviour and no worse."""
    try:
        text = str(reply or "")
        tags = "".join(_AI_TAG.findall(text))
        prose = _AI_TAG.sub(" ", text)
        # a removed tag leaves a whitespace-only line behind; the child should not
        # get a gap where a board line used to be
        prose = "\n".join(ln.rstrip() for ln in prose.split("\n"))
        prose = re.sub(r"[ \t]{2,}", " ", prose)
        prose = re.sub(r"\n\s*\n\s*\n+", "\n\n", prose).strip()
        return prose, tags
    except Exception:  # noqa: BLE001 -- never brick a lesson over formatting
        return reply, ""


# (uq, 2026-09-08) THE PROBLEM ASKED IS ALWAYS ON THE BOARD. Jim's flags 22:03/22:05 on a
# live precalc lesson: after a wrong answer the intervention re-taught and re-asked
# ("Now try it yourself: what is f of g of 2?") with NO board tag in its reply -- the
# question existed only in the air, and he "had to guess since there was audio of the
# problem but no text and no visual". script_intervention TELLS the model to draw the
# same kind of board; it did not, and nothing in code made it. Now code does: an ai
# step whose reply carries no board tag at all gets the ask's own board -- the one the
# engine put on the intervene step (the ask as it was drawn) -- prepended, so the
# machines, the number line, the column, whatever the lesson drew, are in front of the
# student while the tutor talks about them. NARROW: only a reply with no board tag; a
# reply that drew something of its own is left alone (judging whether it drew the RIGHT
# thing is a referee's job, not this floor's). Counted as code_repair "askboard".
# the families that DRAW or WRITE -- a [[choices]] row, a [[mark]] or a [[nice]] is not a board
_AI_BOARD_FAMILY = tuple(getattr(tags, "FIGURE_TAGS", ()) or ()) + tuple(getattr(tags, "WRITING_TAGS", ()) or ())


def _ai_board_floor(board_tags: str, ask_board: str, code: str = "", course: str = "") -> str:
    """The intervention's board, with the ask's own board prepended when the model
    drew nothing. Never raises: any surprise returns the tags as they came."""
    try:
        brd = str(board_tags or "")
        if not str(ask_board or "").strip():
            return brd
        names = {m.lower() for m in re.findall(r"\[\[\s*([\w-]+)", brd)}
        if names & set(_AI_BOARD_FAMILY):
            return brd                            # it drew something; leave it be
        tutor._event("code_repair", "askboard",
                     "the intervention carried no board tag; the ask's board was restored",
                     code, course)
        return str(ask_board) + brd
    except Exception:  # noqa: BLE001 -- never brick a lesson over a board
        return str(board_tags or "")


# (sl, 2026-09-04) THE NEXT LESSON IS ALREADY WRITTEN DOWN. Jim's ruling: a MASTERED
# lesson advances on its own, no student choice; a "still learning" end does NOT advance.
# COURSE_ORDER (lessonscripts) is the authored sequence -- 360 lessons, 36 per course, and
# its own note records that it exists because an earlier build "had accidentally placed
# carrying before two-digit-no-carry". Until now nothing read it at the seam: _script_finish
# popped the session and the LIVE tutor was asked to NAME "the new topic" without ever being
# told WHICH -- which is exactly the 09-01 bug Jim watched ("one-less reads as subtraction").
# Build rj made the model announce its guess; this makes the guess unnecessary.
# Returns (id, topic) for the next lesson IN THE SAME COURSE, or (None, "") at a course
# boundary or the end of the order -- a course ending is a bigger moment than a lesson
# ending, so it still falls through to the live tutor until Jim rules on it.
def _next_lesson_id(current_id: str):
    """The next authored lesson after `current_id`, within the same course."""
    try:
        order = lessonscripts.COURSE_ORDER
        i = order.index(str(current_id or ""))
    except (ValueError, AttributeError):
        return (None, "")
    if i + 1 >= len(order):
        return (None, "")
    nxt = order[i + 1]
    cur_lesson = lessonscripts.LESSON_BY_ID.get(order[i]) or {}
    nxt_lesson = lessonscripts.LESSON_BY_ID.get(nxt) or {}
    if not nxt_lesson:
        return (None, "")
    if nxt_lesson.get("course") != cur_lesson.get("course"):
        return (None, "")          # course boundary: not this ruling's business
    return (nxt, nxt_lesson.get("topic", ""))


def _script_clean(steps, lesson_id: str = ""):
    """The client payload: never the expected answer, never the raw problem.
    (sl) An `end` step also carries WHERE THE COURSE GOES NEXT, so the page can
    advance inside the scripted lane instead of handing the seam to the model.
    (sn) Jim's ruling ③ supersedes sl's "still learning does not advance": a
    still-learning end ALSO carries next_id -- and `choice`: True -- so the page can
    offer the WARM CHOICE (go on, or review). A mastered end carries next_id and no
    choice (it auto-advances, ruling #1). Both are "" / False at a course boundary,
    where the live tutor still takes over until ruling ④ lands. Purely additive --
    a caller that passes no lesson_id gets byte-identical output to before sl."""
    out = []
    _les = lessonscripts.LESSON_BY_ID.get(lesson_id) if lesson_id else None
    for s in steps:
        c = {"kind": s["kind"], "spoken": s.get("spoken", ""),
             "board": s.get("board", "")}
        if s["kind"] == "say":
            # (us) which authored beat this is, so the page can pause on it -- the
            # check after a picture, teach or worked beat, the ready gate after the
            # practice intro. "" for everything else; a step that already carries one
            # (the orientation, built in script_start) keeps it.
            c["beat"] = s.get("beat") or (lessonscripts.beat_of(_les, c["spoken"]) if _les else "")
        if s["kind"] == "ask":
            c["choices"] = s.get("choices", "")
            c["tap_only"] = bool(s.get("tap_only"))
            c["guided"] = bool(s.get("guided"))
            # (sp) the reason question: TEXT options, graded by label below
            c["reason"] = bool(s.get("reason"))
        if s["kind"] == "end":
            c["mastered"] = bool(s.get("mastered"))
            c["graceful"] = bool(s.get("graceful"))
            c["next_id"], c["next_topic"], c["choice"] = "", "", False
            if lesson_id:
                _nid, _ntopic = _next_lesson_id(lesson_id)
                c["next_id"], c["next_topic"] = (_nid or ""), (_ntopic or "")
                # (sn) the warm choice: still learning, and there IS a next lesson
                c["choice"] = bool(_nid) and not c["mastered"]
        out.append(c)
    return out


def _script_session(code: str):
    now = _time.monotonic()
    for k in [k for k, v in _SCRIPT_SESSIONS.items()
              if now - v.get("t0", now) > _SCRIPT_TTL_S]:
        _SCRIPT_SESSIONS.pop(k, None)
    return _SCRIPT_SESSIONS.get(code)


def _script_finish(code: str, sess, end_step):
    """Record the outcome through the SAME store calls the live lanes use.
    (ue) A mastered end writes "taught" -- "Lesson done" on every page -- not
    "mastered": Jim's ruling (2026-09-07) keeps that word for the 90% Unit Quiz,
    whose only writer is store.record_check. A still-learning end stays "learning"."""
    try:
        lesson = sess["lesson"]
        status = "taught" if end_step.get("mastered") else "learning"
        store.record_topic(code, lesson["unit"], lesson["topic"], status,
                           lesson["course"])
    except Exception as exc:  # noqa: BLE001
        print(f"[script] outcome record failed (non-fatal): {exc}")
    # (rk, 2026-09-01) THE PER-LESSON RECORD. Jim: "it keeps starting over from the
    # beginning" -- record_topic above is one row per UNIT and cannot say WHICH
    # lesson finished, so the picker restarted lesson one every login. This is the
    # durable answer the picker resumes from (/api/session ships the mastered ids).
    try:
        store.record_script_done(code, sess["lesson"]["course"],
                                 sess["lesson"]["id"],
                                 bool(end_step.get("mastered")))
    except Exception as exc:  # noqa: BLE001
        print(f"[script] script_done record failed (non-fatal): {exc}")
    # (rj) leave the seam note for the __script_done__ turn that follows -- see
    # _SCRIPT_DONE_NOTES above. Fail-open: a missing note just means a plainer
    # announcement.
    try:
        _SCRIPT_DONE_NOTES[code] = {
            "topic": sess["lesson"].get("topic", ""),
            "course": sess["lesson"].get("course", ""),
            "mastered": bool(end_step.get("mastered")),
        }
    except Exception as exc:  # noqa: BLE001
        print(f"[script] seam note failed (non-fatal): {exc}")
    _SCRIPT_SESSIONS.pop(code, None)


def _script_note_ask(sess, steps):
    """(ue) Remember the question on the screen so its answer can be written down.
    Called with the steps of every response the lane sends. A NEW question (a
    different pending problem, or the reason question) resets the try counter and
    starts the clock; a re-ask of the same question after an unheard answer keeps
    both -- unheard is not a try. Reads the engine's pending state, never a step's
    answer key."""
    try:
        for st in steps or []:
            if st.get("kind") != "ask":
                continue
            pend = (sess.get("state") or {}).get("pending") or {}
            key = ("reason" if pend.get("reason")
                   else json.dumps(pend.get("problem"), sort_keys=True, default=str))
            if key != sess.get("ask_key"):
                sess["ask_key"] = key
                sess["ask_tries"] = 0
                sess["ask_t"] = _time.monotonic()
            sess["ask_spoken"] = st.get("spoken", "")
            sess["ask_guided"] = bool(st.get("guided"))
    except Exception as exc:  # noqa: BLE001
        print(f"[script] ask note failed (non-fatal): {exc}")


# =============================================================================
# BUILD vb (2026-09-10) -- WHAT COMES NEXT IF THEY ARE RIGHT.
# -----------------------------------------------------------------------------
# Jim, 2026-09-10, on a scripted lesson: "10 second latency is too long when we
# know this is next after a correct answer we need to load that so it is ready to
# go." He is exactly right about what we know. Every batch this lane sends ends in
# a QUESTION, and the engine is a pure state machine: given the question's own
# answer, the beats that follow a CORRECT reply are already computable, here, with
# no model and no network.
#
# So we compute them and send their SPOKEN LINES along with the batch, as `warm`.
# The page hands them to voice.js's shelf (build vb, static/voice.js) while the
# current beat is still playing, so the first beat AFTER the child answers plays
# off bytes that are already in the browser. That first beat is the one Jim was
# waiting ten seconds for: every other beat of a batch was already covered by the
# page's own look-ahead, because the whole batch arrives at once.
#
#   ⚠️ IT IS A GUESS ABOUT THE CHILD, NOT ABOUT THE LESSON. If they answer
#      WRONGLY the warmed lines are simply not needed yet -- they are the same
#      authored lines the lesson will reach after the re-teach, so nothing is
#      wasted, only early. The engine is not advanced: the speculative step runs
#      on a DEEP COPY (step() returns the state object it was handed, mutated in
#      place -- "Pure" in its docstring means "no I/O", not "no mutation"), and
#      nothing here writes to the session, the store or the streak.
#   ⚠️ TEXT ONLY, AND CAPPED. No boards, no kinds, no answer keys -- a warm list
#      that carried the next question's board would put the answer on the wire
#      before it was asked. Three lines is the cap: enough to cover the seam,
#      small enough that a wrong guess costs at most three authored renders that
#      the prewarm was always going to pay for.
#   ⚠️ FAIL-OPEN, TOTAL. Any exception at all returns [] and the lane behaves
#      exactly as it did before this build. A latency feature must never be able
#      to cost a lesson.
# =============================================================================
SCRIPT_WARM_LINES = 3


def _script_warm(lesson, state) -> list:
    """The spoken lines that follow a CORRECT answer to the question now pending.
    [] when there is no pending question, when the answer cannot be derived, or on
    any error whatsoever. Never mutates `state`, never touches the store."""
    try:
        pend = (state or {}).get("pending") or {}
        if not pend:
            return []
        if pend.get("reason"):
            # (sp) the reason question is graded by its LABEL, and the engine wrote
            # the right label into its own pending record (_ask_reason: "expected").
            # Read it there -- exactly where _script_note_ask reads the same state --
            # rather than re-deriving a second opinion from the lesson dict.
            label = pend.get("expected") or ""
            if not label:
                return []
            event = ("answer", label)
        else:
            problem = pend.get("problem")
            if problem is None:
                return []
            event = ("answer", int(lessonscripts.ans(problem)))
        steps, _ = lessonscripts.step(lesson, copy.deepcopy(state), event)
        out = []
        for st in steps or []:
            spoken = (st or {}).get("spoken") or ""
            if spoken.strip():
                out.append(spoken)
            if len(out) >= SCRIPT_WARM_LINES:
                break
        return out
    except Exception as exc:  # noqa: BLE001 -- a warm guess must never cost a lesson
        print(f"[script] warm look-ahead skipped (non-fatal): {exc}")
        return []


def _script_record_answer(code, sess, kind, answer, expected, correct):
    """(ue) THE AUTHORED LANE WRITES IT DOWN. One row per graded answer -- the
    question as spoken, the answer, the expected, right or not, which try, and the
    milliseconds since the question (or the previous try) -- through
    store.record_script_answer, which never raises. Fail-open: a lost row never
    costs a turn. Returns nothing; the streak and the engine are untouched."""
    try:
        sess["ask_tries"] = int(sess.get("ask_tries", 0)) + 1
        now = _time.monotonic()
        ms = int((now - sess.get("ask_t", now)) * 1000)
        sess["ask_t"] = now                      # the next try's clock starts here
        lesson = sess["lesson"]
        store.record_script_answer(
            code, lesson.get("course", ""), lesson.get("id", ""), lesson.get("unit", 0),
            kind, sess.get("ask_spoken", ""), str(answer), str(expected), bool(correct),
            attempt=sess["ask_tries"], ms=ms, guided=bool(sess.get("ask_guided")))
    except Exception as exc:  # noqa: BLE001
        print(f"[script] answer record failed (non-fatal): {exc}")


def _script_log(code, course, t_start, kind="script"):
    try:
        store.log_usage(kind=kind, code=code, course=course, mode="script",
                        model="", attempts=1, verify_status="script",
                        ms_total=int((_time.monotonic() - t_start) * 1000),
                        ms_model=0)
    except Exception:  # noqa: BLE001
        pass


class ScriptStartIn(BaseModel):
    code: str
    course: str = "basic"
    lesson: str = ""        # build jw: a lesson id from /api/script/lessons; blank = first


class ScriptAnswerIn(BaseModel):
    code: str
    value: int | None = None
    unheard: bool = False
    # (ur, 2026-09-08) THE WRONG ANSWER IS ANSWERED AT ONCE. A page that sends
    # defer_ai=True gets the verdict and the authored hold line back immediately and
    # a {"kind": "ai_pending"} marker in place of the model's re-teach; it then POSTs
    # /api/script/intervene, which runs the model turn and returns the ai step. A page
    # that does not send it (pilot.html) gets exactly the old shape: the re-teach
    # resolved before this call returns.
    defer_ai: bool = False
    # build ou (2026-08-27): the child's OWN words -- typed, or transcribed from
    # their voice. Read by CODE (lessonscripts.read_answer), never by a model:
    # the whole latency case for this lane is that nothing thinks between the
    # child and the next sentence. `value` still wins when both arrive, so a tap
    # is byte-for-byte the request it has always been.
    said: str | None = None


# (ur, 2026-09-08) THE WRONG ANSWER IS ANSWERED AT ONCE. Jim's flag 21:41 on a live
# algebra2 lesson: "more than 30 second wait after a wrong answer". The engine emits
# "Not quite -- let's look at it together" BEFORE its intervene step, but this endpoint
# resolved the model's re-teach (one call, verified up to three times, ~10 s each) before
# responding, so the student heard nothing for the whole wait. Now, when the page asks
# for it (defer_ai), the answer turn returns at once -- the verdict, the star, the hold
# line, and an "ai_pending" marker -- and the page fetches the re-teach from
# /api/script/intervene while the hold line plays. The model turn itself, its
# bookkeeping (mode, history, redo, the askboard floor) and its fail-open (no reply ->
# the engine's own retest) are unchanged: they moved from the answer turn into
# _script_deferred_run. FAIL-SAFE: an answer that arrives while a re-teach is still
# deferred (a page that never asked) resolves it first, silently, so the session can
# never wedge.
def _script_deferred_run(code, sess, lesson, t0):
    """Run the deferred intervention and return the steps the page should play: the
    ai step (with the askboard floor), or the engine's resume steps when the model
    gave nothing. None when nothing was deferred."""
    d = sess.pop("deferred", None)
    if not d:
        return None
    reply = _script_intervene(code, lesson["course"], d["context"], list(d.get("history") or []))
    if reply:
        _say, _brd = _split_ai_reply(reply)
        _brd = _ai_board_floor(_brd, (d.get("context") or {}).get("board"), code, lesson["course"])
        if d.get("kind") == "redo":
            sess["ai_turns"] = int(sess.get("ai_turns") or 0) + 1
            sess.setdefault("history", []).append({"role": "assistant", "content": reply})
        else:
            sess.update(mode="intervene", ai_turns=1,
                        history=[{"role": "assistant", "content": reply}],
                        redo=d.get("redo"))
        out = [{"kind": "ai", "spoken": _say, "board": _brd}]
    else:
        # the model is unreachable or produced nothing: the script absorbs it --
        # straight to the engine's retest, no dead air, no error page
        steps, state = lessonscripts.step(lesson, sess["state"], ("resume",))
        sess.update(state=state, mode="script", ai_turns=0, history=[], redo=None)
        out = _script_clean(steps, lesson["id"])
        for s in steps:
            if s["kind"] == "end":
                _script_finish(code, sess, s)
    _script_note_ask(sess, out)
    _script_log(code, lesson["course"], t0)
    return out


class ScriptInterveneIn(BaseModel):
    code: str


@app.post("/api/script/intervene")
def script_intervene_run(body: ScriptInterveneIn):
    """(ur) The deferred re-teach: the model turn the answer endpoint put off."""
    t0 = _time.monotonic()
    code = (body.code or "").strip()
    sess = _script_session(code)
    if not sess:
        raise HTTPException(status_code=409, detail=(
            "No scripted lesson is running for this code -- POST /api/script/start."))
    if not sess.get("deferred"):
        raise HTTPException(status_code=409, detail="nothing is waiting to be taught")
    out = _script_deferred_run(code, sess, sess["lesson"], t0)
    return {"ok": True, "steps": out or []}


# =============================================================================
# (uv, 2026-09-09) WHAT HAPPENED LAST TIME, FROM THE RECORD.
# -----------------------------------------------------------------------------
# Jim, 2026-09-09: "They are not an AI. They don't remember instantly what they did
# before yesterday. So we have to familiarize them. This is where we are. Then we
# have to say, this is what we're gonna do."
#
# us gave every lesson an orientation beat, but it could only say THAT the previous
# lesson was finished -- a boolean. Everything else a returning child needs was
# already in the store (ue's script_answers, one row per graded answer; script_done's
# last_at) and nothing read it. This does, and hands lessonscripts.lesson_orientation
# a small prepared dict so that function stays pure and the battery can replay it.
#
# ⚠️ IT GOES ON THE CARD, NOT INTO THE VOICE. The orientation's two spoken variants
# are pre-rendered clips; a per-student sentence would make the second beat of every
# lesson a live text-to-speech call -- a bill and a wait on the one beat that must
# land instantly. The board holds a score better than the ear does anyway.
#
# ⚠️ AND IT NEVER GUESSES. Every field is optional and any miss simply drops that
# part of the line (rule 0: a recap is a memory, not a guess). No store, no rows, a
# bad date, an impossible score -> the card falls back to exactly what us shipped.
# FIRST-TRY answers to REAL questions only: the guided pairs are the "I do" beats,
# and counting them would inflate a child's own score with the tutor's own work.
def _days_ago_phrase(stamp: str) -> str:
    """"yesterday" / "3 days ago" / "last week" from an ISO timestamp, or "" when
    nothing honest can be said. Never raises."""
    try:
        from datetime import datetime, timezone
        raw = str(stamp or "").strip()
        if not raw:
            return ""
        then = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        if then.tzinfo is None:
            then = then.replace(tzinfo=timezone.utc)
        days = (now.date() - then.astimezone(timezone.utc).date()).days
        if days < 0:
            return ""
        if days == 0:
            return "earlier today"
        if days == 1:
            return "yesterday"
        if days < 7:
            return f"{days} days ago"
        if days < 14:
            return "last week"
        if days < 60:
            return f"{days // 7} weeks ago"
        return ""
    except Exception:  # noqa: BLE001 -- a date must never cost a lesson
        return ""


def _orientation_last(code: str, course: str, prev_id: str, last_at: str = ""):
    """How the previous lesson went: {"when", "right", "asked"}, any key optional,
    or None when the record says nothing. Never raises."""
    out = {}
    when = _days_ago_phrase(last_at)
    if when:
        out["when"] = when
    try:
        rows = store.get_script_answers(code, course, limit=400) or []
        mine = [r for r in rows
                if r.get("lesson_id") == prev_id and r.get("kind") == "ask"
                and not r.get("guided") and int(r.get("attempt") or 1) == 1]
        if mine:
            day = mine[0].get("day")          # newest first: their last sitting at it
            sitting = [r for r in mine if r.get("day") == day]
            out["asked"] = len(sitting)
            out["right"] = sum(1 for r in sitting if r.get("correct"))
    except Exception as exc:  # noqa: BLE001 -- a missing score is a missing line, not an error
        print(f"[script] last-time score unavailable (non-fatal): {exc}")
    return out or None


@app.post("/api/script/start")
def script_start(body: ScriptStartIn):
    t0 = _time.monotonic()
    code = (body.code or "").strip()
    if not code:
        raise HTTPException(status_code=400, detail="A student code is required.")
    lesson = lessonscripts.LESSON_BY_ID.get((body.lesson or "").strip()) \
        if (body.lesson or "").strip() else lessonscripts.LESSONS[0]
    if lesson is None:
        raise HTTPException(status_code=404, detail=(
            "Unknown lesson id -- GET /api/script/lessons lists them."))
    # (sz) the pass's shuffle seed: drawn here, once, so two students do not meet
    # the times table in the same order; a lesson without a table never reads it
    state = lessonscripts.start(lesson, seed=secrets.randbits(30))
    steps, state = lessonscripts.step(lesson, state, ("begin",))
    # (us, 2026-09-09) THE LESSON ORIENTS THE STUDENT. Right after the intro line
    # (course, unit, lesson i of n, topic): what came before -- only when the RECORD
    # says the previous lesson in the order was finished -- what today is, and the
    # plan, on a card. Fail-open: no record, no store, any error -> the "Today" form.
    prev_done = False
    _last = None
    try:
        prev = lessonscripts.prev_lesson(lesson)
        if prev is not None and store is not None:
            rows = store.get_script_done(code, lesson["course"]) or []
            done = {d.get("lesson_id") for d in rows}
            prev_done = prev["id"] in done
            # (uv) ...and HOW it went, for the card. Only when the record says it
            # was finished -- a score for a lesson they never completed would be a
            # claim about a past that did not happen.
            if prev_done:
                _at = next((d.get("last_at") for d in rows
                            if d.get("lesson_id") == prev["id"]), "")
                _last = _orientation_last(code, lesson["course"], prev["id"], _at or "")
    except Exception as exc:  # noqa: BLE001 -- no record (dev file mode, a store hiccup): the "Today" form
        prev_done = False
        _last = None
    try:
        _osp, _obd = lessonscripts.lesson_orientation(lesson, prev_done, _last)
        steps.insert(1, {"kind": "say", "spoken": _osp, "board": _obd, "beat": "orientation"})
    except Exception as exc:  # noqa: BLE001 -- the orientation must never cost a lesson
        print(f"[script] orientation skipped (non-fatal): {exc}")
    _SCRIPT_SESSIONS[code] = {"state": state, "lesson": lesson, "mode": "script",
                              "ai_turns": 0, "history": [], "redo": None,
                              "t0": _time.monotonic()}
    _script_note_ask(_SCRIPT_SESSIONS[code], steps)      # (ue) the first question
    _script_log(code, lesson["course"], t0)
    # kd: the id rides along so the pilot page can offer "Next lesson" from the
    # course order without guessing which lesson this session is in.
    return {"ok": True, "lesson": lesson["topic"], "id": lesson["id"],
            "steps": _script_clean(steps, lesson["id"])}


# (oq) THE RAISED HAND -- Jim's expansion order after approving Unit 1. Bounds:
# five questions per lesson (then an authored hold line), ten per five minutes
# per code, 300 characters each. A model failure or an over-cap ask both play
# authored lines, so this door can never stall or brick a lesson. The model
# call rides mode="script", so the admin card's Scripted-lane tile counts it
# among the lane's AI interventions automatically.
SCRIPT_QUESTIONS_PER_LESSON = 5
_SCRIPT_Q_HOLD = ("Hold that thought — we are almost done! Ask me again when "
                  "the lesson ends.")
_SCRIPT_Q_FALLBACK = ("That is a good question. Let me think about it while we "
                      "finish this lesson — ask me again at the end!")


class ScriptAskIn(BaseModel):
    code: str
    question: str = ""
    heard: str = ""      # what the bubble showed when the hand went up (context only)
    pending: str = ""    # the pending ask's SPOKEN text, if one is on screen


@app.post("/api/script/ask")
def script_ask(body: ScriptAskIn):
    t0 = _time.monotonic()
    code = (body.code or "").strip()
    sess = _script_session(code)
    if not sess:
        raise HTTPException(status_code=409, detail=(
            "No scripted lesson is running for this code -- POST /api/script/start."))
    _rate_limit("scriptq:" + code, limit=10, window_seconds=300, what="questions")
    q = (body.question or "").strip()[:300]
    if not q:
        raise HTTPException(status_code=400, detail="Type your question first.")
    lesson = sess["lesson"]
    asked = sess.get("q_turns", 0)
    if asked >= SCRIPT_QUESTIONS_PER_LESSON:
        _script_log(code, lesson["course"], t0)
        return {"ok": True, "answer": _SCRIPT_Q_HOLD, "capped": True}
    sess["q_turns"] = asked + 1
    reply = tutor.script_question(
        code, lesson["course"], lesson.get("topic", ""),
        (body.heard or "").strip()[:300], (body.pending or "").strip()[:200], q)
    _script_log(code, lesson["course"], t0)
    return {"ok": True, "answer": reply or _SCRIPT_Q_FALLBACK,
            "capped": False}


@app.get("/api/script/lessons")
def script_lessons():
    """The course, in order (build jw). Public and harmless: ids and titles only."""
    # build kk: DERIVED, not hand-typed. This map had exactly two entries, so the
    # moment Prealgebra was authored the picker would have shown the raw course id
    # "prealgebra" as its heading. curriculum.COURSES already carries every title;
    # a second hand-kept copy is the Class-B disease tags.py exists to end.
    titles = {}
    try:
        titles = {k: v.get("title", k) for k, v in curriculum.COURSES.items()}
    except Exception as exc:  # noqa: BLE001 -- a title is cosmetic; ids still work
        print(f"[script] course titles unavailable: {exc}")
    return {"ok": True, "lessons": [{"id": les["id"], "topic": les["topic"],
                                     "unit": les["unit"],
                                     "course": les["course"],
                                     "course_title": titles.get(les["course"],
                                                                les["course"])}
                                    for les in lessonscripts.LESSONS]}


def _script_streak(code: str, correct: bool):
    """(rd, 2026-08-31) THE MAIN ROAD MOVES THE STAR. The scripted lane grades every
    tap in code and never emits a [[mark]], so until this build today's
    correct-in-a-row streak moved neither up nor down here -- the qz chips sat still
    through a whole scripted lesson (measured in code, then watched live). One door:
    a correct answer bumps, a wrong tap resets (Jim's ruling: a miss is ANY wrong
    tap, guided asks included), and the fresh pair rides the /api/script/answer
    response into the chips. NO counters move -- scripted problems stay out of
    problems_practiced/accuracy, exactly like rc's slips. Returns the fresh
    {today_streak, streak_days} or None (fail open: never costs a turn)."""
    try:
        if not store.enabled():
            return None
        return (store.bump_today_streak(code) if correct
                else store.reset_today_streak(code))
    except Exception as exc:  # noqa: BLE001
        print(f"[scriptstreak] failed open: {exc}")
        return None


@app.post("/api/script/answer")
def script_answer(body: ScriptAnswerIn):
    t0 = _time.monotonic()
    code = (body.code or "").strip()
    sess = _script_session(code)
    if not sess:
        raise HTTPException(status_code=409, detail=(
            "No scripted lesson is running for this code -- POST /api/script/start."))
    lesson, state = sess["lesson"], sess["state"]
    if sess.get("deferred"):
        # (ur) a page that never fetched its re-teach: resolve it now, silently, so the
        # redo below is graded against the question the model was asked to re-teach
        _script_deferred_run(code, sess, lesson, t0)
        state = sess["state"]

    # ---- build ou: THE CHILD'S OWN WORDS BECOME AN ANSWER, IN CODE ----------
    # A tap sends `value` and nothing here runs. A typed or spoken answer sends
    # `said`, and lessonscripts.read_answer -- a pure parser, no model, no
    # network -- turns it into the same integer a tap would have sent. It
    # REFUSES rather than guesses, and each refusal has an authored line:
    #   none      -> exactly the unheard path (Let me say that again / Tap it),
    #                which already escalates to tap-only after two.
    #   notwhole  -> "that one wants a whole number", then the same re-ask.
    #   unsure    -> "saying you are not sure is a good move" + the ✋ is right
    #                there, then the same re-ask. Never graded wrong for it.
    pre = []

    # ---- (sp, 2026-09-05) THE REASON QUESTION IS GRADED BY ITS LABEL -------------
    # Beat six of the shape ("Say it"): the engine asked WHY, with text options, and
    # the tapped (or typed) label comes back in `said`. read_answer would scan it for
    # a number -- "because 8 is 5 or bigger" reads as 5 -- so this door runs FIRST and
    # in code: an exact option match is the answer (the star moves on it like any tap,
    # rd's ruling: a wrong tap is a wrong tap); "I'm not sure" gets its authored line
    # and the re-ask; anything else is the unheard path, which ends in "Tap it".
    # No model call exists on this path.
    if sess["mode"] == "script" and (state.get("pending") or {}).get("reason"):
        label = lessonscripts.reason_option_for(lesson, body.said or "")
        if body.unheard or not label:
            got = lessonscripts.read_answer(body.said or "")
            if got["kind"] == "unsure":
                pre.append({"kind": "say", "spoken": lessonscripts.LINE_UNSURE,
                            "board": ""})
            steps, state = lessonscripts.step(lesson, state, ("unheard",))
            sess["state"] = state
            _script_note_ask(sess, steps)
            _script_log(code, lesson["course"], t0)
            return {"ok": True, "steps": pre + _script_clean(steps, lesson["id"])}
        _right = lessonscripts.reason_right(lesson, label)
        _streak = _script_streak(code, _right)
        _script_record_answer(code, sess, "reason", label,
                              (state.get("pending") or {}).get("expected", ""), _right)
        steps, state = lessonscripts.step(lesson, state, ("answer", label))
        sess["state"] = state
        _script_note_ask(sess, steps)
        for s in steps:
            if s["kind"] == "end":
                _script_finish(code, sess, s)
        _script_log(code, lesson["course"], t0)
        resp = {"ok": True, "steps": _script_clean(steps, lesson["id"])}
        if _streak:
            resp["streak"] = _streak
        return resp

    if body.value is None and (body.said or "").strip():
        got = lessonscripts.read_answer(body.said)
        if got["kind"] == "value":
            body.value = got["value"]
        else:
            if got["kind"] == "notwhole":
                pre.append({"kind": "say", "spoken": lessonscripts.LINE_WHOLE,
                            "board": ""})
            elif got["kind"] == "unsure":
                pre.append({"kind": "say", "spoken": lessonscripts.LINE_UNSURE,
                            "board": ""})
            body.unheard = True

    # ---- the child is inside an AI intervention: CODE grades the redo ----
    if sess["mode"] == "intervene":
        redo = sess["redo"]
        if body.unheard:
            _script_log(code, lesson["course"], t0)
            return {"ok": True, "steps": pre + [{"kind": "say",
                    "spoken": lessonscripts.LINE_TAP, "board": redo["choices"]}]}
        if body.value is not None and int(body.value) == redo["expected"]:
            _streak = _script_streak(code, True)   # (rd) a right redo climbs the star
            _script_record_answer(code, sess, "redo", body.value, redo["expected"], True)
            praise = lessonscripts.praise_for(redo["problem"], state["done"])
            steps, state = lessonscripts.step(lesson, state, ("resume",))
            sess.update(state=state, mode="script", ai_turns=0,
                        history=[], redo=None)
            _script_note_ask(sess, steps)
            out = [{"kind": "say", "spoken": praise, "board": ""}]                 + _script_clean(steps, lesson["id"])
            for s in steps:
                if s["kind"] == "end":
                    _script_finish(code, sess, s)
            _script_log(code, lesson["course"], t0)
            resp = {"ok": True, "steps": out}
            if _streak:
                resp["streak"] = _streak
            return resp
        # (rd) a wrong redo is still a wrong tap: the star falls NOW, whichever of
        # the two exits below this turn leaves through.
        _streak = _script_streak(code, False)
        _script_record_answer(code, sess, "redo", body.value, redo["expected"], False)
        # wrong again: another bounded AI turn, or fall back to the scripted retest
        if sess["ai_turns"] < SCRIPT_AI_TURNS:
            sess["history"].append({"role": "user",
                                    "content": f"My answer is {body.value}."})
            if body.defer_ai:
                # (ur) the verdict and the hold line now; the re-teach on the next call
                sess["deferred"] = {"kind": "redo", "context": redo["context"],
                                    "history": list(sess["history"])}
                _script_log(code, lesson["course"], t0)
                resp = {"ok": True, "steps": pre + [
                    {"kind": "say", "spoken": lessonscripts.LINE_WRONG, "board": ""},
                    {"kind": "ai_pending", "spoken": "", "board": ""}]}
                if _streak:
                    resp["streak"] = _streak
                return resp
            reply = _script_intervene(code, lesson["course"], redo["context"],
                                      sess["history"])
            if reply:
                sess["ai_turns"] += 1
                sess["history"].append({"role": "assistant", "content": reply})
                _script_log(code, lesson["course"], t0)
                _say, _brd = _split_ai_reply(reply)
                _brd = _ai_board_floor(_brd, (redo.get("context") or {}).get("board"),
                                       code, lesson["course"])          # (uq)
                resp = {"ok": True, "steps": [{"kind": "ai", "spoken": _say,
                                               "board": _brd}]}
                if _streak:
                    resp["streak"] = _streak
                return resp
        steps, state = lessonscripts.step(lesson, state, ("resume",))
        sess.update(state=state, mode="script", ai_turns=0, history=[], redo=None)
        _script_note_ask(sess, steps)
        for s in steps:
            if s["kind"] == "end":
                _script_finish(code, sess, s)
        _script_log(code, lesson["course"], t0)
        resp = {"ok": True, "steps": _script_clean(steps, lesson["id"])}
        if _streak:
            resp["streak"] = _streak
        return resp

    # ---- ordinary scripted turn ----
    event = ("unheard",) if body.unheard else ("answer", int(body.value or 0))
    # (rd) the engine's own verdict, taken at the engine's own line -- the pending
    # problem's ans() against the tapped value, computed BEFORE step() consumes the
    # pending state. Unheard is not an answer and moves nothing; guided asks count
    # both ways (a wrong tap is a wrong tap, Jim's ruling).
    _streak = None
    if (not body.unheard) and body.value is not None:
        _pend = (state.get("pending") or {}).get("problem")
        if _pend is not None:
            _exp = lessonscripts.ans(_pend)
            _streak = _script_streak(code, int(body.value) == _exp)
            # (ue) written down at the engine's own line, same verdict as the star
            _script_record_answer(code, sess, "ask", body.value, _exp,
                                  int(body.value) == _exp)
    steps, state = lessonscripts.step(lesson, state, event)
    sess["state"] = state
    out = list(pre)          # build ou: the authored refusal line leads, then the re-ask
    for s in steps:
        if s["kind"] == "intervene":
            context = dict(s)
            context["choices"] = lessonscripts.choices_for(s["problem"])
            if body.defer_ai:
                # (ur) the engine's LINE_WRONG is already in `out`; the re-teach waits
                sess["deferred"] = {"kind": "first", "context": context, "history": [],
                                    "redo": {"problem": s["problem"], "expected": s["expected"],
                                             "choices": context["choices"], "context": context}}
                out.append({"kind": "ai_pending", "spoken": "", "board": ""})
                continue
            reply = _script_intervene(code, lesson["course"], context, [])
            if reply:
                sess.update(mode="intervene", ai_turns=1,
                            history=[{"role": "assistant", "content": reply}],
                            redo={"problem": s["problem"],
                                  "expected": s["expected"],
                                  "choices": context["choices"],
                                  "context": context})
                _say, _brd = _split_ai_reply(reply)
                _brd = _ai_board_floor(_brd, context.get("board"), code, lesson["course"])   # (uq)
                out.append({"kind": "ai", "spoken": _say, "board": _brd})
            else:
                # the model is unreachable or produced nothing: the script absorbs
                # it -- straight to the engine's retest, no dead air, no error page
                steps2, state = lessonscripts.step(lesson, state, ("resume",))
                sess["state"] = state
                out.extend(_script_clean(steps2, lesson["id"]))
        else:
            out.extend(_script_clean([s], lesson["id"]))
            if s["kind"] == "end":
                _script_finish(code, sess, s)
    _script_note_ask(sess, out)          # (ue) whichever question is on screen now
    _script_log(code, lesson["course"], t0)
    resp = {"ok": True, "steps": out}
    if _streak:
        resp["streak"] = _streak
    return resp

class ScriptWarmIn(BaseModel):
    code: str = ""


@app.post("/api/script/warm")
def script_warm(body: ScriptWarmIn):
    """(vb, 2026-09-10) THE LINES THAT FOLLOW A CORRECT ANSWER, SO THE PAGE CAN
    LOAD THEM WHILE THE CHILD IS STILL THINKING.

    ⭐ WHY A DOOR OF ITS OWN, AND NOT A FIELD ON THE ANSWER RESPONSE. Two reasons,
    and the second is the better one:
      1. script_answer leaves through five different returns. Adding a field to
         each is precisely the drift this file's history keeps paying for ("only
         the lesson lane ever ran ensure_today_tag"), and a latency feature is not
         worth that risk. This endpoint reads the session's CURRENT pending
         question, so there is one site and it cannot drift out of step.
      2. The best moment to render the next line is not when the batch is sent --
         it is while the QUESTION is on screen and the child is working it out.
         That is dead air measured in seconds, and it is free.

    Returns spoken TEXT ONLY (see _script_warm): no boards, no kinds, no answer
    keys. Never an error -- no session, no pending question, or any failure at all
    returns {"ok": True, "lines": []} and the page simply speaks the ordinary way.
    """
    code = (body.code or "").strip()
    _rate_limit("scriptwarm:" + code, limit=120, window_seconds=300,
                what="look-ahead requests")
    sess = _script_session(code)
    if not sess:
        return {"ok": True, "lines": []}
    return {"ok": True, "lines": _script_warm(sess.get("lesson"), sess.get("state"))}


# =============================================================================
# THE TOPIC QUIZ, THROUGH THE AUTHORED SPINE  (build ov, 2026-08-27)
# -----------------------------------------------------------------------------
# Jim ordered the flip: the scripted lane becomes the main road. A child on the
# main road finishes a topic and needs to be ASSESSED -- and until this build
# they hit a wall and had to cross to the slow lane for it.
#
# ⭐ NOTHING IN A QUIZ THINKS. No model call exists on either route below. A
# quiz is code asking pinned questions and code grading them, which is what
# makes a score mean something and what keeps the lane fast.
#
# ⭐ NO HELP, BY DESIGN. The engine's quiz machine says only "Right." or "Not
# that one." (rule 47: the one time help is held back, or the score measures the
# help). The page hides the ✋ door for the duration -- the raised hand is a
# teaching door, and a quiz is not teaching.
#
# ⭐ THE SAME STORE CALL THE LIVE LANE USES. store.record_topic_quiz, at the
# same 80% bar, into the same table the dashboard and the unit gate already
# read -- so a topic passed in the fast lane is passed everywhere, and no second
# notion of "mastered" comes into existence.
# =============================================================================
_QUIZ_SESSIONS = {}          # code -> {lesson, state}; in memory, dies with the process


class ScriptQuizStartIn(BaseModel):
    code: str
    lesson: str = ""


class ScriptQuizAnswerIn(BaseModel):
    code: str
    value: int | None = None
    said: str | None = None


def _quiz_clean(steps):
    """Never ship the answer key. The engine's qask carries `expected` nowhere,
    but the problem dict itself would let a determined child compute it, so the
    payload is rebuilt field by field rather than filtered."""
    out = []
    for s in steps:
        k = s.get("kind")
        if k == "qask":
            out.append({"kind": "qask", "spoken": s.get("spoken", ""),
                        "board": s.get("board", ""), "choices": s.get("choices", ""),
                        "n": s.get("n", 0), "total": s.get("total", 0)})
        elif k == "qend":
            out.append({"kind": "qend", "spoken": s.get("spoken", ""), "board": "",
                        "correct": s.get("correct", 0), "total": s.get("total", 0),
                        "pct": s.get("pct", 0), "passed": bool(s.get("passed"))})
        else:
            out.append({"kind": "say", "spoken": s.get("spoken", ""),
                        "board": s.get("board", "")})
    return out


def _quiz_questions(lesson):
    """The pinned set for this lesson (quizsets.py), or nothing when it has none."""
    try:
        import quizsets
        ps = quizsets.QUIZ_SETS.get(lesson.get("id")) or []
        if ps:
            return ps
    except Exception:  # noqa: BLE001
        pass
    try:                      # a lesson added since the table was generated
        return drillpool.quiz_problems(lesson) if drillpool else []
    except Exception:  # noqa: BLE001
        return []


@app.post("/api/script/quiz/start")
def script_quiz_start(body: ScriptQuizStartIn):
    t0 = _time.monotonic()
    code = (body.code or "").strip()
    if not code or not store.get_student(code):
        raise HTTPException(status_code=403, detail="That student code is not valid.")
    lesson = lessonscripts.LESSON_BY_ID.get((body.lesson or "").strip())
    if not lesson:
        raise HTTPException(status_code=404, detail="No such lesson.")
    steps, state = lessonscripts.quiz_start(lesson, _quiz_questions(lesson))
    if not state:
        # This lesson cannot honestly field a quiz. Say so plainly; the page
        # simply does not offer the button, so this is a belt-and-braces path.
        return {"ok": False, "reason": "no-quiz", "steps": []}
    _QUIZ_SESSIONS[code] = {"lesson": lesson, "state": state}
    _script_log(code, lesson["course"], t0, kind="quiz")
    return {"ok": True, "lesson": lesson["topic"], "total": state["total"],
            "steps": _quiz_clean(steps)}


@app.post("/api/script/quiz/answer")
def script_quiz_answer(body: ScriptQuizAnswerIn):
    t0 = _time.monotonic()
    code = (body.code or "").strip()
    sess = _QUIZ_SESSIONS.get(code)
    if not sess:
        raise HTTPException(status_code=409, detail=(
            "No quiz is running for this code -- POST /api/script/quiz/start."))
    lesson, state = sess["lesson"], sess["state"]

    # build ou's reader, reused verbatim: a quiz answer may be tapped, typed or
    # spoken. A refusal is NOT graded -- the child is asked the same question
    # again, because a quiz that marks "I could not hear you" as wrong is
    # measuring the microphone.
    value = body.value
    if value is None:
        got = lessonscripts.read_answer(body.said)
        if got["kind"] != "value":
            line = (lessonscripts.LINE_WHOLE if got["kind"] == "notwhole"
                    else lessonscripts.LINE_TAP)
            again = lessonscripts._quiz_ask(state)
            _script_log(code, lesson["course"], t0, kind="quiz")
            return {"ok": True, "steps": [{"kind": "say", "spoken": line, "board": ""}]
                    + _quiz_clean([again])}

    steps, state = lessonscripts.quiz_answer(lesson, state, int(value))
    sess["state"] = state
    result = None
    for s in steps:
        if s.get("kind") == "qend":
            result = s
    if result is not None:
        _QUIZ_SESSIONS.pop(code, None)
        try:
            store.record_topic_quiz(code, lesson["unit"], lesson["topic"],
                                    result["correct"], result["total"],
                                    lesson["course"])
            if result["passed"]:
                # (ue) "taught", not "mastered": the topic quiz is the lesson's
                # own door at 80%; "Mastered" is the 90% Unit Quiz alone (Jim).
                # The pass itself is on record in topic_quizzes, as before.
                store.record_topic(code, lesson["unit"], lesson["topic"],
                                   "taught", lesson["course"])
        except Exception as exc:  # noqa: BLE001
            print(f"[quiz] outcome record failed (non-fatal): {exc}")
    _script_log(code, lesson["course"], t0, kind="quiz")
    return {"ok": True, "steps": _quiz_clean(steps)}


# =============================================================================
# ABRABOT -- THE DRILL LANE  (build mh, phase 2 of Abrabot)
# -----------------------------------------------------------------------------
# WHAT THIS IS. drillpool.py (build mg) turned every op's own check() into a pool of
# EXTRA problems per lesson -- 24,880 of them across 275 lessons, each one put through
# the real lessonscripts.validate() before it was admitted. Phase 1 was data with no
# door. This is the door: three small routes and an in-memory session, so a child who
# has finished a lesson can keep working problems from it.
#
# ⭐ THE ONE RULE THAT SHAPES EVERYTHING HERE: A DRILL PROBLEM HAS NO CLIP.
# Mr. Cadabra's voice is pre-rendered per line and the cache is keyed on the verbatim
# text (_tts_cache_path). Every line of every SCRIPTED lesson is in that closure and
# therefore free forever. A GENERATED problem's sentence was never rendered, so
# speaking it in his voice would be a cache MISS -- a live ElevenLabs call, per
# problem, per child, at full price and full latency. That is why Abrabot exists and
# why he sounds different: he speaks in the BROWSER's own voice, which costs nothing,
# starts instantly, and needs no cache. The drill page therefore never sets
# elevenEnabled, so voice.js takes its browser-speech path -- and the battery pins
# that the page contains no reference to /api/speak or speak-prep at all.
#
# ⭐ ABRABOT DRILLS; MR. CADABRA TEACHES. Jim's ruling, 2026-08-23: "Drill is practice,
# quizzes are for mastery." So NOTHING in this lane writes a topic row, touches
# mastery, or moves a unit. It logs usage (kind="drill") so /admin can see the lane
# working and price its latency with the same instrument every other lane uses, and
# that is the whole of its persistence. A drill session lives in memory and dies with
# the process, exactly like a scripted one.
#
# WHAT PHASE 2 DELIBERATELY DOES NOT DO. It detects struggle and REPORTS it
# (`struggling` in the payload) but does not act on it: fetching Mr. Cadabra is phase
# 4, and the fly-in and the replayed teach beat land there. Abrabot must not say "let
# me fetch Mr. Cadabra" in a build where he cannot -- telling a stuck child that help
# is coming and then not sending it is a worse defect than the silence it replaces.
#
# WHAT PHASE 2 KNOWS IT IS MISSING, recorded so it is not mistaken for a bug:
#   - the pool is walked from its easiest end on every new session, because nothing
#     is persisted. A child who drills twice in one session keeps advancing; a child
#     who comes back tomorrow starts easy again. Persisting that position is a store
#     write, and this lane does not write. It lands with the effort awards or not at
#     all.
#   - 53 of the 328 lessons have no pool (their ops admit no extra tuple the validator
#     will accept). /api/drill/lessons reports the count per lesson so the picker can
#     say so up front instead of failing at the tap.
# =============================================================================
# ⚠️ (mm) OPTIONAL, LIKE EVERY OTHER SUBSYSTEM IN THIS FILE. drillpool.py is a NEW
# file (build mg). `git commit -am` does NOT stage a new untracked file -- so the
# realistic failure on the very first deploy of this lane is that main.py imports a
# module that never reached the repo. A bare `import drillpool` would make that an
# ImportError at module load: not "drill is missing", but THE WHOLE SITE DOWN, for a
# feature nobody was using yet.
# misconceptions, foundations, sprints and nightwatch are all imported exactly this
# way and reported in /health's `subsystems` block. Drill is a smaller thing than any
# of them and has no business being the one that can take the app with it.
try:
    import drillpool
except Exception as _dp_exc:  # noqa: BLE001
    drillpool = None
    print(f"[main] drillpool.py unavailable ({_dp_exc}) -- extra practice disabled")

_DRILL_SESSIONS: dict = {}
_DRILL_TTL_S = 2 * 3600
_DRILL_ROUND = 8                 # problems in one round before Abrabot totals up
_DRILL_STRUGGLE_STREAK = 3       # wrong three in a row
_DRILL_STRUGGLE_MISSES = 2       # or two problems missed even on the second try

# The pool memo. Building ONE lesson's pool costs ~0.07s (measured across the course:
# 21.7s for all 328), so the first child to drill a lesson pays milliseconds and
# everyone after pays nothing. The lock guards the DICT, never the computation: two
# threads racing on the same lesson do the same deterministic work twice, which is
# cheap and correct, where holding a lock through a 20-second warm walk would stall
# every other request behind it.
_DRILL_POOLS: dict = {}
_DRILL_POOL_LOCK = threading.Lock()
_DRILL_WARM: dict = {"state": "cold", "done": 0, "total": 0}
_DRILL_WARM_LOCK = threading.Lock()


def _drill_pool(lesson) -> list:
    """This lesson's extra problems, built once per process."""
    lid = lesson["id"]
    got = _DRILL_POOLS.get(lid)
    if got is not None:
        return got
    if drillpool is None:
        return []                      # (mm) the module never loaded: no extra practice
    try:
        pool = drillpool.pool_for(lesson)
    except Exception as exc:  # noqa: BLE001 -- a lesson we cannot pool is one we skip
        print(f"[drill] pool build failed for {lid}: {exc}")
        pool = []
    with _DRILL_POOL_LOCK:
        _DRILL_POOLS[lid] = pool
    return pool


def _drill_warm_worker() -> None:
    """Fill the memo for the whole course in the background (~22s, once per process).

    Started by the first /api/drill/lessons call, never at boot: a cold Render
    instance has a redeploy's worth of work to do already, and nothing about drill is
    needed until somebody asks for it."""
    try:
        for les in lessonscripts.LESSONS:
            _drill_pool(les)
            _DRILL_WARM["done"] = len(_DRILL_POOLS)
        _DRILL_WARM["state"] = "ready"
        print(f"[drill] pools ready: {sum(len(v) for v in _DRILL_POOLS.values())} "
              f"extra problems across {len(_DRILL_POOLS)} lessons")
    except Exception as exc:  # noqa: BLE001 -- warming is an optimisation, never a duty
        _DRILL_WARM["state"] = "cold"
        print(f"[drill] warm walk stopped: {exc}")


def _drill_warm_start() -> None:
    if drillpool is None:
        return                          # (mm) nothing to warm
    with _DRILL_WARM_LOCK:
        if _DRILL_WARM["state"] != "cold":
            return
        _DRILL_WARM["state"] = "warming"
        _DRILL_WARM["total"] = len(lessonscripts.LESSONS)
    threading.Thread(target=_drill_warm_worker, daemon=True, name="drill-warm").start()


# ---- Abrabot's own words ----------------------------------------------------
# He is a different character from Mr. Cadabra and says so. These lines are spoken by
# the browser, so they are free and they are NOT part of the audio closure -- but they
# obey lessonscripts.VOCABULARY exactly as an authored lesson does, because a child
# must not hear "subtract" from the helper and "take away" from the teacher. The
# battery pins that against the real VOCABULARY table.
# ---- (mx) ABRABOT HAS A PERSONALITY NOW -------------------------------------
# Jim, 2026-08-24, after drilling with him: "it's very strict. What is this minus
# this? What is that minus that? And there's no personality to it. It feels like a
# strict teacher that's gonna spank me if I do something wrong."
#
# He was right, and the OLD lines are worth keeping here as the evidence: "Correct!"
# / "Yes!" / "That is right!" / "Not quite. Have one more try." / "The answer was
# {v}. Let's keep going." Eight clipped lines, no warmth, no play. A scorekeeper.
#
# ⭐ AND THE REWRITE IS FREE. Abrabot speaks in the BROWSER'S voice, never the paid
# one, so his words are not in the rendered closure and cost nothing to change. Mr.
# Cadabra's lines are the opposite -- every one of his is a paid render.
#
# WHO HE IS: a machine who genuinely likes problems, is pleased when you get one,
# and is completely unbothered when you do not. He never scolds and never says a
# child is wrong -- a miss is just a number he has not got yet.
_ABRA_HELLO = ("Beep! I am Abrabot, Mr. Cadabra's practice helper. Problems are my "
               "favourite thing. Here is one now.")
_ABRA_YES = ("Correct! My circuits are pleased.", "Yes! I knew you had that one.",
             "That is right! Beep!", "Nice work. Filing that one under easy.",
             "Got it! You are quick today.", "Correct! Straight into my memory banks.",
             "Yes! That is the one.",
             "Right again. I am impressed, and I do not say that to everyone.")
_ABRA_RETRY = ("Hmm! My circuits say not quite. Have one more try — I have all day, "
               "I am a robot.")
_ABRA_TELL = "The answer was {v}. Now you know it, and so do I. Onwards!"
_ABRA_ROUND = ("That is {right} out of {asked}. Shall we do some more? I never get "
               "tired.")
_ABRA_EMPTY = ("You have worked every single extra problem I have for this lesson. "
               "Every one! My problem box is empty and I am very impressed.")
# ---- (mj) THE HANDOFF ---------------------------------------------------------
# Jim, 2026-08-23: "if it detects a child is struggling, it needs to call in Mr
# Cadabra to do some more teaching." Phase 2 detected it and said nothing, on
# purpose: Abrabot must not promise help he cannot send. He can now, so he says so.
_ABRA_FETCH = ("Ooh, this one is tricky. That is a job for a human — let me go "
               "and get Mr. Cadabra.")
_ABRA_BACK = "Thank you, Mr. Cadabra! Right — let us try another one."
# (mn) Mr. Cadabra's two lines around the re-teach ARE closure text now. mj declared
# them "not authored closure text" and Jim heard the result on 2026-08-24: the first
# words of the fly-in arrived in the browser voice, then his real voice "came back"
# for the re-teach. The strings live in lessonscripts beside ABRABOT_INTRO -- the
# closure's ONE owner -- and these names are aliases, never copies, so the prewarm
# renders them, the evictor protects them, and the drill gate admits them.
_CAD_HELLO = lessonscripts.CADABRA_HANDOFF_HELLO
_CAD_BYE = lessonscripts.CADABRA_HANDOFF_BYE

# ---- (mk) THE INTRODUCTION ----------------------------------------------------
# Mr. Cadabra brings Abrabot on, in four authored lines, IN HIS REAL VOICE. They live
# in lessonscripts.ABRABOT_INTRO because that is where the closure is enumerated --
# so the prewarm renders them, the evictor protects them, the estimator prices them
# and the drill lane's closure gate admits them, all without a second list anywhere.
# 525 characters, about twelve cents, once, for the whole product's lifetime.
#
# ⚠️ ONCE PER CHILD, PER PROCESS. There is no store write in this lane, so "has this
# child met Abrabot?" is memory: a redeploy re-introduces them. That is the honest
# trade and it is the RIGHT way round -- hearing the introduction a second time next
# week is a small cost; skipping it for a child who never heard it is the feature
# not existing. Persisting it belongs with the effort awards, or nowhere.
_DRILL_INTRODUCED: set = set()
_DRILL_INTRODUCED_CAP = 5000


def _drill_intro_steps(code: str) -> list:
    """Mr. Cadabra's introduction, the first time this child opens the drill room."""
    if code in _DRILL_INTRODUCED:
        return []
    if len(_DRILL_INTRODUCED) >= _DRILL_INTRODUCED_CAP:
        _DRILL_INTRODUCED.clear()          # a bounded set; the worst case is a repeat
    _DRILL_INTRODUCED.add(code)
    lines = list(lessonscripts.ABRABOT_INTRO)
    if not lines:
        return []
    kinds = ["arrive"] + ["teach"] * (len(lines) - 2) + ["leave"]
    # (om, 2026-08-27) Jim: "The introduction to Abrabot should have a skip
    # introduction button, so I don't have to listen to it over and over again."
    # Each intro step is MARKED, so the page can offer "Skip the intro" exactly
    # while one is playing and drop the rest of the marked run -- and nothing
    # else: a lesson step never carries the mark, so skip can never eat teaching.
    return [{"kind": k, "who": "cadabra", "spoken": ln, "board": "", "intro": True}
            for k, ln in zip(kinds, lines)]


def _drill_teach_steps(lesson, depth: int) -> list:
    """Mr. Cadabra's re-teach, straight out of the lesson. A LADDER, not a lecture.

    ⭐ EVERY LINE HERE IS ALREADY PAID FOR. lessonscripts.audio_lines() enumerates
    exactly these strings, so each one was rendered once by the prewarm and is a cache
    hit forever. That is the whole reason the handoff is free: the teaching a stuck
    child needs was written and voiced months before they got stuck.

    depth 1 -- ONE WORKED EXAMPLE. A child who has missed two problems usually needs
              to watch one done, not to hear the lesson again from the top.
    depth 2+ -- THE FULL TEACH SEQUENCE, then the worked example. If watching one done
              did not land, the idea underneath it is what is missing.
    """
    out = []
    if depth >= 2:
        # (sp) the full teach sequence now opens on the PICTURE when the lesson has
        # one -- the representation is the re-teach, the rule is its summary
        for spoken, board in list(lesson.get("picture") or []) + list(lesson.get("teach", [])):
            out.append({"kind": "teach", "who": "cadabra",
                        "spoken": spoken, "board": board})
    pairs = lesson.get("pairs") or []
    if pairs:
        worked = pairs[0].get("worked") or ("", "")
        out.append({"kind": "teach", "who": "cadabra",
                    "spoken": worked[0], "board": worked[1]})
    return out


def _drill_speakable(text) -> bool:
    """Is this line one the course has already rendered? (Reporting only.)

    The page does not have to trust this -- /api/speak-prep refuses a drill ticket for
    anything outside the closure, and the ticket is cache-only on top. This just lets
    the page ask for the natural voice ONLY where it stands a chance, so a stuck child
    is not made to wait on a request that was always going to 204."""
    try:
        # (vc) the LESSON's text arrives raw here; the closure is keyed on what the
        # page asks for, so it is asked in the page's own words.
        return _tts_cache_path(_spoken(str(text or ""))).name in _script_closure_paths()
    except Exception:  # noqa: BLE001
        return False


def _drill_praise(p, index: int) -> str:
    """Abrabot's praise: HIS opener, the LESSON'S own sentence about the answer.

    praise_for() is the one place that knows how each op says its result out loud, and
    re-deriving that here would be a second copy of 300-odd op branches to drift. So
    the real function is called and Mr. Cadabra's opener is taken off the front --
    Abrabot does not borrow the teacher's voice OR his catchphrases."""
    line = lessonscripts.praise_for(p, index)
    for pre in lessonscripts.PRAISE_PREFIXES:
        if line.startswith(pre):
            line = line[len(pre):].strip()
            break
    opener = _ABRA_YES[index % len(_ABRA_YES)]
    return (opener + " " + line).strip() if line else opener


def _drill_record(code: str, sess, right: int, day: str = "") -> None:
    """(mt) Count ONE retired practice problem. Jim, 2026-08-24: a child should be
    able to show a parent that they practised.

    ⚠️ CALLED ONLY WHERE A PROBLEM IS RETIRED -- the right answer, or the second
    miss. NOT on the second-chance re-ask, or one problem a child eventually got
    would count as two and their practice accuracy would be quietly wrong.

    ⚠️ AND IT CANNOT MARK MASTERY. store.record_drill writes the practice ledger and
    the day streak; it does not touch unit_checks or topic_progress. Jim's ruling of
    2026-08-23 stands and PART 3df pins it."""
    try:
        store.record_drill(code, sess["lesson"]["id"], right=int(right), asked=1,
                           course=sess["lesson"]["course"], day=day)
    except Exception as exc:  # noqa: BLE001 -- a counter must never fail a problem
        print(f"[drill] could not count a problem: {exc}")


def _drill_session(code: str):
    now = _time.monotonic()
    for k in [k for k, v in _DRILL_SESSIONS.items()
              if now - v.get("t0", now) > _DRILL_TTL_S]:
        _DRILL_SESSIONS.pop(k, None)
    return _DRILL_SESSIONS.get(code)


def _drill_ask(sess) -> dict:
    """The next problem as an ask beat, and the session remembers what it expects."""
    lesson, pool = sess["lesson"], sess["pool"]
    p = pool[sess["i"]]
    level = (lesson.get("levels") or lessonscripts.LEVELS)[0]
    expected = lessonscripts.ans(p)
    sess["pending"] = {"problem": p, "expected": expected}
    return {"kind": "ask",
            "spoken": lessonscripts.spoken_for(p, level),
            "board": lessonscripts.board_for(p, level),
            "choices": lessonscripts.choices_for(p),
            "expected": expected}


def _drill_clean(steps) -> list:
    """The client payload. Same rule as _script_clean: the expected answer and the raw
    problem NEVER leave the server, because a tap that can be read out of the page is
    not an answer."""
    out = []
    for s in steps:
        c = {"kind": s["kind"], "spoken": s.get("spoken", ""),
             "board": s.get("board", "")}
        # (mj) WHO IS TALKING. The page swaps face and voice on this and nothing else,
        # so a step that forgets to say lands on Abrabot -- the safe default, because
        # Abrabot never uses the paid voice.
        c["who"] = s.get("who", "abrabot")
        # (mj) and whether the natural voice is even worth asking for: true only for
        # lines the course authored AND rendered. Advisory -- the server refuses a
        # drill ticket for anything else regardless of what the page believes.
        c["natural"] = bool(s.get("who") == "cadabra" and _drill_speakable(s.get("spoken")))
        # (om) the introduction's mark rides to the page -- it is what makes the
        # "Skip the intro" button appear on those steps and only those.
        if s.get("intro"):
            c["intro"] = True
        if s["kind"] == "ask":
            c["choices"] = s.get("choices", "")
        if s["kind"] == "end":
            c["right"] = int(s.get("right", 0))
            c["asked"] = int(s.get("asked", 0))
            c["more"] = bool(s.get("more"))
        out.append(c)
    return out


def _drill_struggling(sess) -> bool:
    return (sess["wrong_streak"] >= _DRILL_STRUGGLE_STREAK
            or sess["misses"] >= _DRILL_STRUGGLE_MISSES)


def _drill_handoff(sess) -> list:
    """Abrabot fetches Mr. Cadabra, he re-teaches, and he hands back.

    ⚠️ WHAT TRIPS THIS, HONESTLY. The scope I wrote for Jim said "the same
    misconception twice". misconceptions.py cannot deliver that here: match() reads
    the WORDS of an answer for detect-strings like "5x", and a drill answer is a
    TAPPED NUMBER with no words in it at all -- many catalogue entries carry no detect
    strings whatever. Claiming misconception detection off a tap would be a
    measurement that does not exist. What the lane can honestly see is the counters it
    has kept since mh: three wrong in a row, or two problems missed even on the second
    try. That is what fetches him, and it is what the payload has always called
    `struggling`.

    ⚠️ AND THE COUNTERS RESET AFTER HE COMES. Without this he arrives, teaches, and
    is instantly re-fetched by the same still-true counters on the very next miss --
    a child who is having a bad day would get the same lecture five times in a row,
    which is how a helpful feature becomes a punishment."""
    lesson = sess["lesson"]
    sess["fetches"] += 1
    steps = ([{"kind": "say", "who": "abrabot", "spoken": _ABRA_FETCH, "board": ""},
              {"kind": "arrive", "who": "cadabra", "spoken": _CAD_HELLO, "board": ""}]
             + _drill_teach_steps(lesson, sess["fetches"])
             + [{"kind": "leave", "who": "cadabra", "spoken": _CAD_BYE, "board": ""},
                {"kind": "say", "who": "abrabot", "spoken": _ABRA_BACK, "board": ""}])
    sess["wrong_streak"] = 0
    sess["misses"] = 0
    return steps + _drill_advance(sess)


def _drill_advance(sess) -> list:
    """Retire the problem just finished and hand back what comes next: the next ask,
    the end of a round, or the end of the pool."""
    sess["i"] += 1
    sess["asked"] += 1
    sess["round_asked"] += 1
    if sess["i"] >= len(sess["pool"]):
        sess["pending"] = None
        return [{"kind": "end", "spoken": _ABRA_EMPTY, "board": "",
                 "right": sess["round_right"], "asked": sess["round_asked"],
                 "more": False}]
    if sess["round_asked"] >= _DRILL_ROUND:
        sess["pending"] = None
        return [{"kind": "end",
                 "spoken": _ABRA_ROUND.format(right=sess["round_right"],
                                              asked=sess["round_asked"]),
                 "board": "", "right": sess["round_right"],
                 "asked": sess["round_asked"], "more": True}]
    return [_drill_ask(sess)]


class DrillStartIn(BaseModel):
    code: str
    lesson: str = ""


class DrillAnswerIn(BaseModel):
    code: str
    value: int | None = None
    # (mt) the CHILD'S local day, same as the hours tiles send. A kid practising at
    # 8pm is practising today; the server's date is the fallback, not the truth.
    day: str = ""


class DrillNextIn(BaseModel):
    code: str


@app.get("/api/drill/lessons")
def drill_lessons():
    """The course with a drill count against each lesson.

    `ready` is false while the background warm walk is still running, in which case a
    count of null means "not measured yet", NOT "no problems". The picker says so
    rather than hiding a lesson that is about to become available."""
    _drill_warm_start()
    titles = {}
    try:
        titles = {k: v.get("title", k) for k, v in curriculum.COURSES.items()}
    except Exception as exc:  # noqa: BLE001 -- a title is cosmetic; ids still work
        print(f"[drill] course titles unavailable: {exc}")
    known = dict(_DRILL_POOLS)
    out = []
    for les in lessonscripts.LESSONS:
        pool = known.get(les["id"])
        out.append({"id": les["id"], "topic": les["topic"], "unit": les["unit"],
                    "course": les["course"],
                    "course_title": titles.get(les["course"], les["course"]),
                    "drill": (None if pool is None else len(pool))})
    return {"ok": True, "ready": _DRILL_WARM["state"] == "ready",
            # (mm) If drillpool.py never loaded, every count is "not measured yet" and
            # the picker would say "checking..." forever -- true of the memo, useless
            # to a person. This says the real thing instead.
            "available": drillpool is not None,
            "warmed": len(known), "total": len(lessonscripts.LESSONS),
            "lessons": out}


@app.post("/api/drill/start")
def drill_start(body: DrillStartIn):
    t0 = _time.monotonic()
    code = (body.code or "").strip()
    if not code:
        raise HTTPException(status_code=400, detail="A student code is required.")
    _student_or_404(code)
    _rate_limit("drill:" + code, limit=400, window_seconds=300, what="problems")
    lesson = lessonscripts.LESSON_BY_ID.get((body.lesson or "").strip()) \
        if (body.lesson or "").strip() else lessonscripts.LESSONS[0]
    if lesson is None:
        raise HTTPException(status_code=404, detail=(
            "Unknown lesson id -- GET /api/drill/lessons lists them."))
    if drillpool is None:
        raise HTTPException(status_code=503, detail=(
            "Abrabot's extra problems are not loaded on this server right now."))
    pool = _drill_pool(lesson)
    if not pool:
        raise HTTPException(status_code=409, detail=(
            "Abrabot has no extra problems for this lesson yet -- try another one."))
    sess = {"lesson": lesson, "pool": pool, "i": 0, "asked": 0, "right": 0,
            "wrong_streak": 0, "misses": 0, "second_chance": False,
            "pending": None, "round_asked": 0, "round_right": 0,
            "fetches": 0,                      # (mj) how often Mr. Cadabra has come
            "t0": _time.monotonic()}
    _DRILL_SESSIONS[code] = sess
    steps = (_drill_intro_steps(code)
             + [{"kind": "say", "who": "abrabot", "spoken": _ABRA_HELLO, "board": ""},
                _drill_ask(sess)])
    _script_log(code, lesson["course"], t0, kind="drill")
    return {"ok": True, "lesson": lesson["topic"], "id": lesson["id"],
            "pool": len(pool), "struggling": False,
            "score": {"right": 0, "asked": 0},
            "steps": _drill_clean(steps)}


@app.post("/api/drill/answer")
def drill_answer(body: DrillAnswerIn):
    t0 = _time.monotonic()
    code = (body.code or "").strip()
    sess = _drill_session(code)
    if not sess:
        raise HTTPException(status_code=409, detail=(
            "No drill is running for this code -- POST /api/drill/start."))
    _rate_limit("drill:" + code, limit=400, window_seconds=300, what="problems")
    pending = sess.get("pending")
    if not pending:
        raise HTTPException(status_code=409, detail=(
            "Abrabot is not waiting on an answer -- POST /api/drill/next."))
    lesson = sess["lesson"]
    value = None if body.value is None else int(body.value)

    if value is not None and value == pending["expected"]:
        sess["right"] += 1
        sess["round_right"] += 1
        sess["wrong_streak"] = 0
        sess["second_chance"] = False
        _drill_record(code, sess, right=1, day=body.day)
        steps = ([{"kind": "say",
                   "spoken": _drill_praise(pending["problem"], sess["asked"]),
                   "board": ""}]
                 + _drill_advance(sess))
    elif not sess["second_chance"]:
        # ONE second try, on the SAME problem, before Abrabot says the answer. A tap
        # can be a slip; a lesson's own engine gives a re-ask too. The problem is not
        # retired here, so it is not counted twice.
        sess["wrong_streak"] += 1
        sess["second_chance"] = True
        steps = [{"kind": "say", "spoken": _ABRA_RETRY, "board": ""},
                 _drill_ask(sess)]
    else:
        # Missed twice. Abrabot TELLS -- he still does not teach; teaching is Mr.
        # Cadabra's, and as of mj Abrabot can actually go and get him.
        sess["wrong_streak"] += 1
        sess["misses"] += 1
        sess["second_chance"] = False
        _drill_record(code, sess, right=0, day=body.day)
        steps = [{"kind": "say",
                  "spoken": _ABRA_TELL.format(v=pending["expected"]), "board": ""}]
        if _drill_struggling(sess):
            steps += _drill_handoff(sess)
        else:
            steps += _drill_advance(sess)

    _script_log(code, lesson["course"], t0, kind="drill")
    return {"ok": True, "struggling": _drill_struggling(sess),
            "score": {"right": sess["right"], "asked": sess["asked"]},
            "steps": _drill_clean(steps)}


@app.get("/api/drill/stats/{code}")
def drill_stats_api(request: Request, code: str = Depends(_code_dep), days: int = 7):
    """(mt) What a child can SHOW a parent: problems practised today, this week, and
    all time, plus which lessons they have been grinding.

    Honest {tracking: false} when the database is off, exactly like /api/awards."""
    _read_guard(request, code)
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": True, "tracking": False}
    st = store.drill_stats(code, days=max(1, min(int(days or 7), 60)))
    st["ok"] = True
    st["tracking"] = True
    st["accuracy_pct"] = (round(100.0 * st["total_right"] / st["total_asked"])
                          if st["total_asked"] else None)
    return st


@app.post("/api/drill/next")
def drill_next(body: DrillNextIn):
    """Another round from where this session left off in the pool."""
    t0 = _time.monotonic()
    code = (body.code or "").strip()
    sess = _drill_session(code)
    if not sess:
        raise HTTPException(status_code=409, detail=(
            "No drill is running for this code -- POST /api/drill/start."))
    _rate_limit("drill:" + code, limit=400, window_seconds=300, what="problems")
    if sess["i"] >= len(sess["pool"]):
        raise HTTPException(status_code=409, detail=(
            "Abrabot has no extra problems left for this lesson."))
    sess["round_asked"] = 0
    sess["round_right"] = 0
    sess["second_chance"] = False
    steps = [_drill_ask(sess)]
    _script_log(code, sess["lesson"]["course"], t0, kind="drill")
    return {"ok": True, "struggling": _drill_struggling(sess),
            "score": {"right": sess["right"], "asked": sess["asked"]},
            "steps": _drill_clean(steps)}


# =============================================================================
# BUILD kq -- THE PREWARM RENDER IS A JOB, NOT A REQUEST
# -----------------------------------------------------------------------------
# It used to render every missing line serially INSIDE the HTTP request. A whole
# course is hundreds of ElevenLabs calls, so the browser had to hold one connection
# open for minutes; Render's proxy cuts a request that long, and a redeploy kills it
# outright ("Waiting for connections to close"). Either way admin.html saw a non-2xx
# with no JSON body and printed its fallback -- "Request failed." -- while the work
# may well have been half done. Nothing was ever lost (each clip is cached the moment
# it arrives, and the cache is keyed on the verbatim text, so re-running skips what is
# already paid for) but NOTHING SAID SO.
#
# Three things change here and nothing else:
#   (a) the render runs on a background thread; the POST returns in milliseconds,
#   (b) ONE LOCK, process-wide, so a second job cannot start on top of a running one
#       -- two overlapping jobs paying twice for the same lines is exactly what
#       emptied Jim's ElevenLabs credits,
#   (c) the job's progress is written to disk as it goes, so after the process is
#       restarted mid-render the next status call can say "interrupted at 210 of 354"
#       instead of pretending nothing happened.
#
# dry_run is UNTOUCHED: it is free, it is fast, it answers in the same request, and
# every battery pin on this endpoint exercises that path.
_PREWARM_STATE_LOCK = threading.Lock()   # guards _PREWARM_JOB and nothing else
_PREWARM_JOB: dict = {}                  # {} means no job has run in this process
_PREWARM_RECORD = DATA_DIR / "tts_prewarm_job.json"
_PREWARM_FAIL_CAP = 25                   # keep the record small; the count is exact


def _prewarm_write_record(job: dict) -> None:
    """Persist the job so a redeploy cannot erase the fact that it was running.
    Best-effort by design: a failed write must never abort a paid render."""
    try:
        # A PRIVATE temp name per writer, exactly as build ke made the TTS cache do.
        # A fixed ".part" beside the target is the same shape of bug that spliced two
        # renders into one clip -- the lock makes a collision unlikely here, not
        # impossible, and "unlikely" is what ke was about.
        fd, tmp_name = tempfile.mkstemp(dir=str(DATA_DIR), suffix=".jobpart")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(job, fh)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_name, str(_PREWARM_RECORD))
    except Exception as exc:  # noqa: BLE001
        print(f"[script-prewarm] could not write the job record: {exc}")


def _prewarm_read_record() -> dict:
    try:
        if _PREWARM_RECORD.exists():
            with open(_PREWARM_RECORD, encoding="utf-8") as fh:
                return dict(json.load(fh))
    except Exception as exc:  # noqa: BLE001
        print(f"[script-prewarm] could not read the job record: {exc}")
    return {}


def _prewarm_recover_record() -> None:
    """At boot: a record still saying "running" belongs to a process that is gone.
    THAT IS THE BUG JIM SAW, written down. Mark it interrupted so the admin page can
    report where it got to and tell him that pressing render again resumes."""
    rec = _prewarm_read_record()
    if rec.get("state") == "running":
        rec["state"] = "interrupted"
        rec["note"] = ("This job was still running when the server restarted -- a "
                       "deploy, a restart, or the instance sleeping. Everything it had "
                       "already rendered is cached and paid for; press render again "
                       "and it picks up from there.")
        _prewarm_write_record(rec)
        print(f"[script-prewarm] recovered an interrupted job: "
              f"{rec.get('done')} of {rec.get('total')} lines")


_prewarm_recover_record()


def _prewarm_snapshot() -> dict:
    """The live job if this process has one, otherwise whatever is on disk."""
    with _PREWARM_STATE_LOCK:
        if _PREWARM_JOB:
            return dict(_PREWARM_JOB)
    rec = _prewarm_read_record()
    return rec or {"state": "idle", "note": "No render has been started."}


def _prewarm_worker(job_id: str, todo: list, already: int) -> None:
    """The render loop, exactly as it was -- only now it is nobody's HTTP request."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}"
    headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
    rendered, failed, spent, done = 0, [], 0, 0

    def publish(**extra):
        with _PREWARM_STATE_LOCK:
            if _PREWARM_JOB.get("id") != job_id:
                return None                       # superseded; stop touching it
            _PREWARM_JOB.update(done=done, rendered=rendered, chars_spent=spent,
                                failed=failed[:_PREWARM_FAIL_CAP],
                                failed_count=len(failed), **extra)
            return dict(_PREWARM_JOB)

    try:
        for say in todo:
            try:
                r = httpx.post(url, headers=headers, timeout=60.0, json={
                    "text": say, "model_id": _tts_model_for(say),   # kf
                    "output_format": "mp3_44100_128",
                    "voice_settings": {"stability": 0.55, "similarity_boost": 0.75,
                                       "use_speaker_boost": True},
                })
                if r.status_code != 200 or not r.content:
                    failed.append(f"HTTP {r.status_code}: {say[:40]}")
                elif not _tts_cache_store(say, r.content, source="script-prewarm"):
                    failed.append(f"damaged render (not cached): {say[:40]}")
                else:
                    rendered += 1
                    spent += len(say)
                    store.log_usage(kind="tts", code="", mode="script-prewarm",
                                    model=str(_tts_model_for(say) or ""),
                                    tts_chars=len(say), tts_cache_hit=False)
            except Exception as exc:  # noqa: BLE001
                failed.append(f"{type(exc).__name__}: {say[:40]}")
            done += 1
            # Every tenth line, and on the last one, the record on disk catches up.
            # A restart can then only ever lose the last few lines of PROGRESS -- never
            # a rendered clip, which was cached the instant it arrived.
            snap = publish()
            if snap is None:
                return
            if done % 10 == 0 or done == len(todo):
                _prewarm_write_record(snap)
        # BUILD ke: settle the cache up here, where the closure is protected, rather
        # than letting the next ordinary playback cull hundreds of fresh clips at once.
        try:
            _evict_tts_cache()
        except Exception as exc:  # noqa: BLE001
            print(f"[script-prewarm] evict skipped: {exc}")
        snap = publish(state=("done" if not failed else "done_with_failures"),
                       finished_at=int(_time.time()),
                       disk=_tts_cache_projection(0),
                       note=("Every line rendered." if not failed else
                             f"{len(failed)} line(s) failed -- press render again and "
                             f"only those are retried."))
    except Exception as exc:  # noqa: BLE001
        snap = publish(state="error", finished_at=int(_time.time()),
                       note=f"{type(exc).__name__}: {exc}")
    if snap:
        _prewarm_write_record(snap)


def _prewarm_start(todo: list, already: int, lesson: str, force: bool) -> dict:
    """Claim the lock and start ONE job. Returns the job, or raises 409 if a render
    is already in flight -- the refusal that stops two jobs paying for the same line
    twice. There is no way to run two: this is the only door."""
    global _PREWARM_JOB
    with _PREWARM_STATE_LOCK:
        if _PREWARM_JOB.get("state") == "running":
            live = dict(_PREWARM_JOB)
            raise HTTPException(status_code=409, detail=(
                f"A render is already running ({live.get('done', 0)} of "
                f"{live.get('total', 0)} lines, started for "
                f"{live.get('lesson') or '(whole course)'}). Two renders at once pay "
                f"TWICE for the same lines -- that is what emptied the credits before. "
                f"Watch this one finish, or wait for it to stop."))
        job_id = uuid.uuid4().hex[:12]
        _PREWARM_JOB = {
            "id": job_id, "state": "running", "started_at": int(_time.time()),
            "finished_at": None, "lesson": lesson or "(whole course)",
            "forced": bool(force), "total": len(todo), "done": 0, "rendered": 0,
            "already_cached": already, "chars_spent": 0, "failed": [],
            "failed_count": 0,
            "model": _tts_model_for(todo[0]) if todo else str(ELEVEN_MODEL),
            "note": "Running on the server. It keeps going if you close this tab.",
        }
        job = dict(_PREWARM_JOB)
    _prewarm_write_record(job)
    threading.Thread(target=_prewarm_worker, args=(job_id, todo, already),
                     name=f"tts-prewarm-{job_id}", daemon=True).start()
    return job


class PrewarmStatusIn(BaseModel):
    key: str = ""


@app.post("/api/admin/script-prewarm-status")
def admin_script_prewarm_status(body: PrewarmStatusIn,
                                x_admin_key: str = Header(default="",
                                                          alias="X-Admin-Key")):
    """Where the render got to. Free, instant, and safe to poll -- it reads a dict
    and, at worst, one small file."""
    _require_admin(x_admin_key or body.key)
    job = _prewarm_snapshot()
    return {"ok": True, "job": job, "state": job.get("state", "idle"),
            "running": job.get("state") == "running"}


class ScriptPrewarmIn(BaseModel):
    key: str
    dry_run: bool = False
    limit: int = 0
    lesson: str = ""           # kf: restrict to ONE lesson's closure ("" = whole course)
    force: bool = False        # kf: re-render even lines that are already cached
    over_cap_ok: bool = False  # lb: render ANYWAY, knowing the evictor will cull it


class CourseAudioAuditIn(BaseModel):
    key: str = ""
    lesson: str = ""           # "" = the whole course
    tolerance: float = 2.5     # how many times off the median before it is an outlier


class ClipBytesIn(BaseModel):
    key: str = ""
    lesson: str = ""           # which lesson's closure to index into
    index: int = 0             # which line of it (sorted, stable)


class TtsCacheRepairIn(BaseModel):
    key: str = ""
    dry_run: bool = True       # default SAFE: look, report, delete nothing
    limit: int = 0             # 0 = scan the whole cache


def _tts_cache_bytes_per_char() -> float:
    """Bytes of mp3 per character of text, measured from clips already in the cache.

    Falls back to ~1,070 B/char, which is what 128 kbps (16 KB/s) works out to at a
    normal speaking rate of ~15 characters a second."""
    # BUILD me (2026-08-23) -- THE NUMERATOR AND THE DENOMINATOR CAME FROM
    # DIFFERENT POPULATIONS, and the answer was ~35% light.
    #
    # This used to take the average size of some cached clips and divide it by the
    # average line length of the WHOLE closure -- including every line not rendered
    # yet. Those are not the same set. Jim's cache held 19,002 clips averaging 92.7
    # characters, while the closure as a whole averages 124.9, so the estimate came
    # out at 923 B/char when those very clips were sitting on disk at 1,244. The
    # admin panel then told him a finished render would reach 3,762 MB when the
    # honest figure was ~4,344 -- a 582 MB error, against a 4,500 MB cap, and he
    # was about to plan a $418 render around it.
    #
    # Now every sampled clip is weighed against ITS OWN text length: sum the bytes
    # of clips we can identify, sum exactly those clips' characters, divide. Clips
    # from the generated lane are skipped rather than guessed at, because we do not
    # know their text. If nothing identifiable is on disk we fall back as before.
    try:
        by_name = _script_closure_chars()
        sample_bytes, sample_chars, n = 0, 0, 0
        for f in _TTS_CACHE_DIR.iterdir():
            if f.suffix != ".mp3":
                continue
            chars = by_name.get(f.name)
            if not chars:                    # generated lane: text unknown, skip it
                continue
            try:
                sample_bytes += f.stat().st_size
            except Exception:  # noqa: BLE001 -- vanished mid-scan
                continue
            sample_chars += chars
            n += 1
            if n >= 400:                     # plenty for a stable mean
                break
        if n >= 20 and sample_chars > 0:
            return sample_bytes / float(sample_chars)
    except Exception:  # noqa: BLE001 -- an estimate must never break the endpoint
        pass
    return 1070.0


def _tts_cache_projection(chars_to_render: int) -> dict:
    """What the cache holds now, what the pending render adds, and whether the cap
    can take it. Numbers only -- the caller decides what to do about them."""
    used, count = 0, 0
    try:
        for f in _TTS_CACHE_DIR.iterdir():
            if f.suffix == ".mp3":
                used += f.stat().st_size
                count += 1
    except Exception:  # noqa: BLE001 -- no cache dir yet is a legitimate zero
        pass
    adding = int(max(0, chars_to_render) * _tts_cache_bytes_per_char())
    cap = int(_TTS_CACHE_MAX_BYTES)
    return {"cached_clips": count,
            "used_bytes": used, "used_mb": round(used / 1048576.0, 1),
            "projected_add_bytes": adding, "projected_add_mb": round(adding / 1048576.0, 1),
            "projected_total_mb": round((used + adding) / 1048576.0, 1),
            "cap_mb": round(cap / 1048576.0, 1),
            "fits": (used + adding) <= cap}


@app.post("/api/admin/tts-cache-repair")
def admin_tts_cache_repair(body: TtsCacheRepairIn,
                           x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """BUILD ke -- FIND AND REMOVE THE DAMAGED CLIPS.

    Jim's kd playtest: "several of the lessons have the voice slurring and speaking
    nonsense". The cause was three cache writers sharing one temp filename, so a line
    rendered from two places at once was stored as two renders spliced together (see
    the change note at the top of this file). Build ke makes that impossible going
    forward -- but the clips already written are still on disk and will replay their
    garble forever, because a cache HIT never re-renders.

    This walks every clip, checks it with mp3_is_intact(), and deletes the ones that
    fail, along with any stray .part files left by the old writers. A deleted clip is
    not lost: the next play re-renders it at normal cost (a few cents), and the repair
    reports the character count so that cost is known before it is spent.

    dry_run defaults to TRUE -- it will look and report without deleting anything.
    POST again with dry_run=false to actually remove them.

    The response reports `xing_coverage`: the share of clips carrying an Xing/Info
    header, which is what the byte-count cross-check needs. If that is high the
    detector has real teeth on this cache; if it is low, splices between equal-length
    renders could still hide, and that is worth knowing rather than assuming."""
    _require_admin(x_admin_key or body.key)
    scanned = bad = with_counts = 0
    freed = 0
    parts = 0
    damaged = []
    try:
        entries = sorted(_TTS_CACHE_DIR.iterdir()) if _TTS_CACHE_DIR.exists() else []
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Cannot read the cache: {exc}")

    # Stray temp files from the OLD shared-name writers. They are never served (the
    # cache only reads .mp3) but they are wasted disk and a sign of the very bug we
    # are repairing, so they go either way.
    for f in entries:
        if f.suffix == ".part":
            parts += 1
            if not body.dry_run:
                try:
                    f.unlink(missing_ok=True)
                except Exception:  # noqa: BLE001
                    pass

    for f in entries:
        if f.suffix != ".mp3":
            continue
        if body.limit and scanned >= body.limit:
            break
        scanned += 1
        try:
            data = f.read_bytes()
        except Exception as exc:  # noqa: BLE001
            damaged.append({"file": f.name, "bytes": 0, "why": f"unreadable: {exc}"})
            bad += 1
            continue
        if mp3_has_counts(data):
            with_counts += 1
        if mp3_is_intact(data):
            continue
        bad += 1
        freed += len(data)
        if len(damaged) < 50:
            damaged.append({"file": f.name, "bytes": len(data),
                            "why": "failed the frame-chain / Xing byte-count check"})
        if not body.dry_run:
            try:
                f.unlink(missing_ok=True)
            except Exception as exc:  # noqa: BLE001
                print(f"[repair] could not delete {f.name}: {exc}")

    coverage = round((with_counts / float(scanned)) * 100.0, 1) if scanned else 0.0
    return {"ok": True,
            "dry_run": bool(body.dry_run),
            "scanned": scanned,
            "damaged": bad,
            "healthy": scanned - bad,
            "stray_part_files": parts,
            "bytes_freed": freed,
            "mb_freed": round(freed / 1048576.0, 1),
            "xing_coverage_pct": coverage,
            "examples": damaged[:50],
            "note": ("Nothing was deleted. POST again with dry_run=false to remove "
                     "these; each one re-renders on its next play."
                     if body.dry_run else
                     "Damaged clips removed. They re-render on the next play -- run "
                     "script-prewarm afterwards to render them all at once.")}


@app.post("/api/admin/script-prewarm")
def admin_script_prewarm(body: ScriptPrewarmIn,
                         x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """Render a lesson's (or the whole course's) ENTIRE audio closure into the TTS
    cache. lessonscripts.audio_lines() enumerates every line the engine can ever speak
    (battery-proved), so after this runs, a scripted lesson NEVER waits on ElevenLabs
    and never spends a TTS character again. Idempotent; dry_run prices it without
    spending, in this request.

    BUILD kq: a real render no longer happens in this request. It STARTS a background
    job and returns at once -- poll /api/admin/script-prewarm-status to watch it.
    Only one job may run at a time; a second attempt is refused with a 409 rather
    than quietly paying for the same lines twice."""
    _require_admin(x_admin_key or body.key)
    # build jw: the WHOLE course's closure, deduped -- shared lines (praise, the
    # fixed one-liners) render once and serve every lesson.
    # build kf: `lesson` narrows that to one lesson, so a bad clip (or a model change)
    # can be tested for pennies instead of re-rendering the whole course unheard.
    lessons = lessonscripts.LESSONS
    if body.lesson:
        lessons = [l for l in lessonscripts.LESSONS if l["id"] == body.lesson]
        if not lessons:
            raise HTTPException(status_code=404,
                                detail=f"No scripted lesson with id {body.lesson!r}.")
    # (mk) ONE OWNER FOR THE CLOSURE. `lessons` is the full course unless the caller
    # narrowed it, and course_audio_lines() adds the standalone lines (Abrabot's
    # introduction) only in the un-narrowed case -- rendering one lesson must not
    # quietly re-price course-level speech.
    lines = _closure_lines(
        None if len(lessons) == len(lessonscripts.LESSONS) else lessons)
    todo, already = [], 0
    for say in lines:
        if body.force:
            # kf: FORCE means re-render over the top. A cache HIT never re-renders, so
            # without this a clip that is structurally perfect but SOUNDS wrong (the
            # exact thing Jim heard) can never be replaced except by emptying the cache.
            todo.append(say)
            continue
        try:
            pth = _tts_cache_path(say)
            if pth.exists() and pth.stat().st_size > 0:
                already += 1
                continue
        except Exception:  # noqa: BLE001
            pass
        todo.append(say)
    chars = sum(len(s) for s in todo)
    if body.dry_run or not todo:
        # BUILD ke: price the render in DISK too. The cache has a hard cap and the
        # evictor enforces it; a course that does not fit would be silently culled
        # right after Jim paid for it, so he should see that BEFORE spending.
        disk = _tts_cache_projection(chars)
        return {"ok": True, "dry_run": True, "already_cached": already,
                "to_render": len(todo), "chars": chars,
                "lesson": body.lesson or "(whole course)",
                "force": bool(body.force),
                "model": _tts_model_for(lines[0]) if lines else str(ELEVEN_MODEL),
                "disk": disk,
                "note": ("Nothing was spent. POST again with dry_run=false to render."
                         + ("" if disk["fits"] else
                            f"  WARNING: this does NOT fit the voice cache "
                            f"({disk['projected_total_mb']} MB needed, cap is "
                            f"{disk['cap_mb']} MB). Whatever you render past the cap "
                            f"is deleted by the evictor and billed again next time. "
                            f"Set TTS_CACHE_MAX_MB="
                            f"{int(disk['projected_total_mb'] * 1.25) + 50} in Render "
                            f"-> Environment and redeploy BEFORE rendering."))}
    if not ELEVEN_API_KEY:
        raise HTTPException(status_code=503,
                            detail="ELEVENLABS_API_KEY is not set on this deploy.")
    if body.limit and body.limit > 0:
        todo = todo[:body.limit]

    # ---------------------------------------------------------------------
    # BUILD lb -- THE MONEY GUARD. Build ke computed this projection and build kl
    # made every button say FREE or SPENDS, but NOTHING EVER REFUSED, and admin.html
    # never displayed the numbers. So when the course outgrew the cap (at build ko,
    # pre-u5-times-by-ten, ~300 MB) the render began paying for clips the evictor
    # deleted minutes later -- and the only symptom Jim could see was that it "keeps
    # running and running". Reproduced locally: with a cap smaller than the course,
    # every round paid for 810 lines and kept 335, forever.
    # Rendering into a cache that cannot hold the result is not a render. It is a
    # purchase with a receipt and no goods, so it is REFUSED unless Jim says
    # otherwise in so many words.
    _proj = _tts_cache_projection(sum(len(t) for t in todo))
    if not _proj["fits"] and not body.over_cap_ok:
        _need = int(_proj["projected_total_mb"] * 1.25) + 50
        raise HTTPException(status_code=409, detail=(
            f"REFUSED -- this render does not fit in the voice cache, so most of it "
            f"would be deleted by the evictor and you would pay for it again next "
            f"time. Cache holds {_proj['used_mb']} MB of {_proj['cap_mb']} MB; this "
            f"job adds {_proj['projected_add_mb']} MB, for "
            f"{_proj['projected_total_mb']} MB total. "
            f"FIX: set TTS_CACHE_MAX_MB={_need} in Render -> Environment (and make "
            f"sure the mounted disk is bigger than that), redeploy, then render. "
            f"To spend anyway, knowing clips will be culled, send over_cap_ok."))
    # BUILD kq: hand the work to a background job and answer NOW. The render loop
    # itself moved to _prewarm_worker unchanged -- what changed is that no browser has
    # to hold a connection open for the length of it. _prewarm_start owns the lock,
    # so this is also the point where a second concurrent render is refused with a 409.
    job = _prewarm_start(todo, already, body.lesson, bool(body.force))
    return {"ok": True, "started": True, "job_id": job["id"], "state": "running",
            "to_render": job["total"], "already_cached": already, "chars": chars,
            "lesson": job["lesson"], "forced": job["forced"], "model": job["model"],
            "disk": _proj,          # lb: what the cache can actually keep
            "over_cap": not _proj["fits"],
            "note": ("The render is running ON THE SERVER, not in your browser. Every "
                     "clip is cached the moment it arrives, so if it is interrupted -- "
                     "a deploy, a restart, an instance going to sleep -- pressing "
                     "render again picks up where it stopped and never pays twice. "
                     "Keep the tab open to watch it; the watching is also the traffic "
                     "that keeps an idle instance awake.")}


@app.post("/api/admin/clip-bytes")
def admin_clip_bytes(body: ClipBytesIn,
                     x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """BUILD kh -- HAND THE REAL AUDIO TO SOMETHING THAT CAN DECODE IT.

    Five builds have now tried to stop the first words being swallowed (bl: leading
    silence; cb: the keep-alive loop; gn: the resume race; jb: the clip probe; kg: the
    pilot page finally getting all of the above). voice.js's own build jb note records
    that the delivery path was PROVEN INNOCENT by measurement, leaving one unmeasured
    link -- what ElevenLabs actually renders. Nothing on this server can decode an mp3;
    the browser can. So this endpoint simply hands one cached clip to the admin page,
    which decodes it and measures where the sound really starts.

    Returns the clip verbatim from the cache -- it renders nothing and spends nothing.
    `index` walks the lesson's closure in the same sorted order the audit uses, so the
    two reports line up line for line."""
    _require_admin(x_admin_key or body.key)
    lessons = [l for l in lessonscripts.LESSONS if l["id"] == body.lesson] \
        if body.lesson else list(lessonscripts.LESSONS)
    if not lessons:
        raise HTTPException(status_code=404,
                            detail=f"No scripted lesson with id {body.lesson!r}.")
    # (mk) ONE OWNER FOR THE CLOSURE. `lessons` is the full course unless the caller
    # narrowed it, and course_audio_lines() adds the standalone lines (Abrabot's
    # introduction) only in the un-narrowed case -- rendering one lesson must not
    # quietly re-price course-level speech.
    lines = _closure_lines(
        None if len(lessons) == len(lessonscripts.LESSONS) else lessons)
    i = int(body.index or 0)
    if i < 0 or i >= len(lines):
        raise HTTPException(status_code=404,
                            detail=f"index {i} is outside 0..{len(lines) - 1}.")
    say = lines[i]
    pth = _tts_cache_path(say)
    try:
        data = pth.read_bytes()
    except Exception:  # noqa: BLE001 -- simply not rendered yet
        return {"ok": True, "index": i, "total": len(lines), "text": say,
                "cached": False, "b64": "", "bytes": 0,
                "note": "Not in the cache yet -- render this lesson first."}
    # A clip is a few tens of KB; this is a diagnostic, not a download service.
    if len(data) > 4 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="That cached clip is implausibly large.")
    return {"ok": True, "index": i, "total": len(lines), "text": say,
            "cached": True, "bytes": len(data),
            "model": _tts_model_for(say),
            "b64": _b64.b64encode(data).decode("ascii")}


@app.post("/api/admin/course-audio-audit")
def admin_course_audio_audit(body: CourseAudioAuditIn,
                             x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """BUILD kf -- IS THE COURSE AUDIO ANY GOOD? Free, reads only, deletes nothing.

    ke's repair pass asks "is this file a valid mp3". That question found nothing,
    because the clip Jim heard as garbled IS a valid mp3 -- a bad RENDER, not a bad
    file. This asks the two questions a valid file can still fail:

      1. IS IT THE RIGHT SHAPE? Every clip should be MPEG-1 Layer III, 44,100 Hz,
         mono, 128 kbps -- what we ask ElevenLabs for, and what the leading silence
         we concatenate at serve time is. A clip in any other shape can decode oddly
         once that silence is glued to its front, which sounds exactly like "right
         words, bad audio".

      2. IS IT A PLAUSIBLE LENGTH FOR ITS WORDS? Because this walks the CLOSURE it
         knows the TEXT behind every clip, so it can compare seconds-per-character
         against the MEDIAN of the course itself. Self-calibrating: no guessed
         speaking rate, no magic constant, and it moves automatically if the voice or
         model changes. A line that renders far short of its words was truncated; far
         long, and something was repeated or drawn out.

    It reports the offending LINES, not hashes, so Jim can go listen to the named ones
    and re-render just those (script-prewarm with lesson=... force=true).

    Duration is computed from the file size at the declared constant bitrate rather
    than by walking every frame -- exact for CBR, and it keeps a 4,000-clip audit to a
    stat() and a 4 KB read per file instead of reading ~200 MB."""
    _require_admin(x_admin_key or body.key)
    lessons = lessonscripts.LESSONS
    if body.lesson:
        lessons = [l for l in lessonscripts.LESSONS if l["id"] == body.lesson]
        if not lessons:
            raise HTTPException(status_code=404,
                                detail=f"No scripted lesson with id {body.lesson!r}.")
    # (mk) ONE OWNER FOR THE CLOSURE. `lessons` is the full course unless the caller
    # narrowed it, and course_audio_lines() adds the standalone lines (Abrabot's
    # introduction) only in the un-narrowed case -- rendering one lesson must not
    # quietly re-price course-level speech.
    lines = _closure_lines(
        None if len(lessons) == len(lessonscripts.LESSONS) else lessons)

    CANON = {"mpeg": "1", "layer": 3, "rate": 44100, "kbps": 128, "channels": "mono"}
    clips, missing, unreadable = [], [], []
    shapes = {}
    for say in lines:
        pth = _tts_cache_path(say)
        try:
            size = pth.stat().st_size
        except Exception:  # noqa: BLE001 -- not rendered yet
            missing.append(say)
            continue
        try:
            with open(pth, "rb") as fh:
                head = fh.read(4096)
        except Exception as exc:  # noqa: BLE001
            unreadable.append(f"{say[:50]} ({exc})")
            continue
        shape = _mp3_shape(head)
        if not shape:
            unreadable.append(f"{say[:50]} (no readable MPEG header)")
            continue
        key = f"{shape['rate']}/{shape['channels']}/{shape['kbps']}k/MPEG{shape['mpeg']}L{shape['layer']}"
        shapes[key] = shapes.get(key, 0) + 1
        audio_bytes = max(0, size - _id3v2_len(head))
        seconds = (audio_bytes * 8.0) / (shape["kbps"] * 1000.0) if shape["kbps"] else 0.0
        clips.append({"text": say, "seconds": round(seconds, 2), "bytes": size,
                      "shape": key, "canon": all(shape[k] == v for k, v in CANON.items()),
                      "sec_per_char": (seconds / len(say)) if say else 0.0})

    odd_shape = [c for c in clips if not c["canon"]]

    # median seconds-per-character across the course -- the course is its own yardstick
    rates = sorted(c["sec_per_char"] for c in clips if c["sec_per_char"] > 0)
    median = rates[len(rates) // 2] if rates else 0.0
    tol = max(1.2, float(body.tolerance or 2.5))
    outliers = []
    if median > 0:
        for c in clips:
            r = c["sec_per_char"]
            if r <= 0:
                continue
            ratio = r / median
            if ratio > tol or ratio < (1.0 / tol):
                outliers.append({"text": c["text"], "seconds": c["seconds"],
                                 "expected_seconds": round(len(c["text"]) * median, 2),
                                 "times_off": round(ratio, 2)})
    outliers.sort(key=lambda o: abs(1.0 - o["times_off"]), reverse=True)

    return {"ok": True,
            "lesson": body.lesson or "(whole course)",
            "model_in_use": _tts_model_for(lines[0]) if lines else str(ELEVEN_MODEL),
            "script_model_set": bool(SCRIPT_TTS_MODEL),
            "lines": len(lines),
            "cached": len(clips),
            "not_yet_rendered": len(missing),
            "shapes": shapes,
            "odd_shape_count": len(odd_shape),
            "odd_shape": [{"text": c["text"][:90], "shape": c["shape"]} for c in odd_shape[:25]],
            "median_seconds_per_char": round(median, 5),
            "tolerance_x": tol,
            "outlier_count": len(outliers),
            "outliers": outliers[:40],
            "unreadable": unreadable[:20],
            "note": ("Nothing was changed. Listen to the lines named above, then "
                     "re-render just that lesson with force to replace them.")}


@app.post("/api/admin/lesson-audit")
def admin_lesson_audit(body: LessonAuditIn):
    """Run the OFFLINE LESSON AUDITOR and return its report.

    2026-08-10 (build cw). Jim: "I need to build some sort of effectiveness/reality check
    so we don't keep having these problems."

    Two things check quality today and there is a gap between them: ruletests.py checks
    the CODE and the WORDS OF THE PROMPT and cannot judge teaching, and Jim reads lessons
    one at a time, which does not scale past Jim. This closes that gap: scripted student
    PERSONAS (played by OpenAI) take real lessons from the real prompt, and OpenAI then
    marks each transcript against the generated rule index as a picky maths teacher.

    NOTHING HERE CHANGES THE TEACHING. It returns a report a human reads. A critic can be
    wrong, and a wrong critic quietly sanding down good teaching is exactly the failure
    this is meant to prevent. A real finding becomes a rule AND a test, in one commit.

    It lives behind the admin key because it spends real money on two APIs, and it runs
    HERE rather than on a laptop because this is where the keys are. `dry_run` prices it
    for free. `limit`/`offset` walk the cast in batches so a request never runs long
    enough to time out -- two scenarios a call is comfortable.

    Needs OPENAI_API_KEY in the environment (Render -> Environment). The key is read,
    never printed, never returned, never logged."""
    _require_admin(body.key)
    try:
        import lessonaudit
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=503,
                            detail=f"lessonaudit.py is not available on this deploy: {exc}")
    turns = int(body.turns) or lessonaudit.TURNS
    limit = max(0, int(body.limit)) or None
    if body.dry_run:
        return lessonaudit.dry_run(limit, int(body.offset), turns)
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        raise HTTPException(status_code=503,
                            detail=("No OPENAI_API_KEY on this service. Add it in Render -> "
                                    "Environment and redeploy; it is used only here, only "
                                    "when you call this endpoint."))
    run = lessonaudit.audit(limit, int(body.offset), turns)
    run["report_markdown"] = lessonaudit.report_markdown(run)
    run["next_offset"] = int(body.offset) + run.get("scenarios_run", 0)
    run["remaining"] = max(0, len(lessonaudit.SCENARIOS) - run["next_offset"])
    return run


@app.post("/api/admin/prewarm-foundations")
def admin_prewarm_foundations(body: PrewarmAdminIn):
    """Render every canonical foundation script into the TTS cache, up front.

    2026-08-09 (build cf, proactive audit #2 item 21). The TTS cache is keyed by the
    TEXT of a line and starts empty, so the FIRST student to reach each of the 173
    scripts pays a live ElevenLabs render -- several seconds of silence on the exact
    turn that introduces a brand-new idea to them. Every student after that gets it
    instantly. We know all 173 strings in advance, so there is no reason for that first
    student to be a real child.

    Idempotent and safe to re-run: a script already in the cache is skipped for free, so
    running this after adding scripts renders only the new ones. `dry_run` prices the
    job without spending a cent. `limit` renders in batches if you would rather not do
    it in one request.

    Admin-key protected -- this endpoint spends real ElevenLabs money."""
    _require_admin(body.key)
    if foundations is None:
        raise HTTPException(status_code=503, detail="foundations.py is not available on this deploy.")
    courses = ([body.course.strip()] if body.course.strip()
               else list(getattr(foundations, "FOUNDATIONS", {}).keys()))
    todo = []
    already = 0
    for c in courses:
        for f in foundations.for_course(c):
            # (vc) ⚠️ EVERY ONE OF THE 306 FOUNDATION SCRIPTS RE-KEYED, not some:
            # each opens with a **bold** term and forSpeech strips the asterisks, so
            # this prewarm has been filing every clip under a label no page has ever
            # asked for -- rendered once for nothing, then rendered LIVE again on
            # every play, for every student, since build cf. _spoken() is the fix and
            # it is applied here, at the top, so the check, the render, the cache
            # write and the usage log all speak of the same string.
            say = _spoken((f.get("say") or "").strip())
            if not say:
                continue
            try:
                if _tts_cache_path(say).exists() and _tts_cache_path(say).stat().st_size > 0:
                    already += 1
                    continue
            except Exception:  # noqa: BLE001 -- an unreadable cache entry just gets re-rendered
                pass
            todo.append((c, f["term"], say))
    chars = sum(len(s) for _c, _t, s in todo)
    if body.dry_run or not todo:
        return {"ok": True, "dry_run": True, "courses": courses, "already_cached": already,
                "to_render": len(todo), "characters": chars,
                "note": "Nothing was spent. POST again with dry_run=false to render."}
    if not ELEVEN_API_KEY:
        raise HTTPException(status_code=503, detail="ELEVENLABS_API_KEY is not set on this deploy.")
    if body.limit and body.limit > 0:
        todo = todo[:body.limit]

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}"
    headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
    rendered, failed, spent = 0, [], 0
    for course, term, say in todo:
        try:
            r = httpx.post(url, headers=headers, timeout=60.0, json={
                "text": say,
                "model_id": ELEVEN_MODEL,
                "output_format": "mp3_44100_128",
                "voice_settings": {"stability": 0.55, "similarity_boost": 0.75,
                                   "use_speaker_boost": True},
            })
            if r.status_code != 200 or not r.content:
                failed.append(f"{course}/{term}: HTTP {r.status_code}")
                continue
            # BUILD ke: the one cache door -- private temp file, validated first.
            if not _tts_cache_store(say, r.content, source="prewarm-foundations"):
                failed.append(f"{course}/{term}: damaged render (not cached)")
                continue
            rendered += 1
            spent += len(say)
            store.log_usage(kind="tts", code="", mode="prewarm", model=str(_tts_model_for(say) or ""),
                            tts_chars=len(say), tts_cache_hit=False)
        except Exception as exc:  # noqa: BLE001 -- one bad script must not stop the batch
            failed.append(f"{course}/{term}: {exc}")
    try:
        _evict_tts_cache()
    except Exception as exc:  # noqa: BLE001
        print(f"[prewarm] evict skipped: {exc}")
    print(f"[prewarm] rendered {rendered}, failed {len(failed)}, {spent} characters")
    return {"ok": not failed, "already_cached": already, "rendered": rendered,
            "characters_spent": spent, "failed": failed[:20], "failed_count": len(failed),
            "remaining": max(0, len(todo) - rendered)}


class StudentResetAdminIn(BaseModel):
    key: str
    code: str


@app.post("/api/admin/student-reset")
def admin_student_reset(body: StudentResetAdminIn):
    """2026-08-07 (build bc, Jim): wipe ONE student code's data -- pilot personas
    (0000/1234/...), demo codes, any student -- so the code can be used as brand new.
    The code keeps working (pilot codes live in students.json; the account row is
    re-created on next login). Admin-key protected; 404 for a code that isn't a known
    student, so a typo can never silently 'succeed'."""
    _require_db()
    _require_admin(body.key, tier="reset")   # build ht: destructive -- FAMILY_RESET_KEY
    code = (body.code or "").strip()
    if not _lookup_student(code):
        raise HTTPException(status_code=404, detail=(
            "That code isn't a known student, so nothing was wiped. (Beta passes are "
            "deleted from the pass table instead.)"))
    res = store.reset_student_data(code)
    if not res.get("ok"):
        raise HTTPException(status_code=500, detail="Couldn't complete the wipe — nothing was deleted.")
    removed = sum(int(v or 0) for v in (res.get("deleted") or {}).values())
    return {"ok": True, "code": code, "rows_removed": removed, "deleted": res.get("deleted") or {}}


@app.post("/api/admin/parent-reset")
def admin_parent_reset(body: ParentResetAdminIn):
    """Fully delete ONE parent account (and its children + data) by email, so the
    email is free to sign up from scratch. Admin-key protected. Returns a summary
    of what was removed. 404 (harmless) if no account exists for that email."""
    _require_db()
    _require_admin(body.key, tier="reset")   # build ht: destructive -- FAMILY_RESET_KEY
    email = (body.email or "").strip().lower()
    if not _EMAIL_RE.match(email):
        raise HTTPException(status_code=400, detail="That doesn't look like an email address.")
    parent = store.get_parent_by_email(email)
    if not parent:
        raise HTTPException(status_code=404, detail=(
            f"No account found for {email}, so there's nothing to reset — that email "
            "is already free to sign up fresh."))
    result = store.delete_parent_cascade(parent["id"])
    if not result.get("ok"):
        raise HTTPException(status_code=500, detail=(
            "Couldn't complete the reset — nothing was deleted. Please try again."))
    return {
        "ok": True,
        "email": email,
        "children_removed": len(result.get("student_codes") or []),
        "deleted": result.get("deleted") or {},
    }


# =============================================================================
# BILLING -- Stripe Checkout + Customer Portal + webhook (2026-07-31)
# -----------------------------------------------------------------------------
# Cards never touch this server. "Subscribe" sends the parent to a Stripe-hosted
# Checkout page; "Manage billing" sends them to Stripe's hosted portal (update
# card, switch plan, cancel). Stripe then tells US what happened on the webhook
# below -- and THAT (signature-verified) is the only thing that ever changes a
# parent's subscription status in the database. Prices are found (or created,
# once) in Stripe by lookup key, so Jim never has to click around the Stripe
# dashboard to set up products:
#   mytutor_monthly  $29 / student / month
#   mytutor_annual   $288 / student / year   ($24/mo, as the pricing page says)
# Env (set in Render): STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET. Optional:
# SITE_URL (defaults to https://mrcadabra.com).
# =============================================================================

_PLAN_LOOKUP = {"monthly": "mytutor_monthly", "annual": "mytutor_annual"}
_PLAN_AMOUNTS = {"monthly": 2900, "annual": 28800}     # cents
_PRICE_ID_CACHE: dict = {}
SITE_URL = (os.environ.get("SITE_URL", "").strip() or "https://mrcadabra.com").rstrip("/")

# 2026-07-31: Stripe accounts now enable "Managed Payments" by default, which
# REQUIRES products to carry a tax code (it's how Stripe computes sales tax for
# you). This is Stripe's tax classification for a digital service delivered
# online ("General - Electronically Supplied Services"). If an accountant later
# advises a more specific education classification, change it here (or set the
# STRIPE_TAX_CODE env var) -- existing products are updated automatically.
PRODUCT_TAX_CODE = (os.environ.get("STRIPE_TAX_CODE", "").strip() or "txcd_10000000")
_TAX_CODE_OK: set = set()      # product ids already verified/updated this process


class CheckoutIn(BaseModel):
    token: str
    plan: str = "monthly"      # 'monthly' | 'annual'


def _payments_open() -> bool:
    """Are we ACCEPTING payments? (2026-08-01, Jim: 'we're in beta — not taking
    payment at this time.') Self-managing: payments open automatically when the
    configured Stripe key is a LIVE key (sk_live_...). With a test key or no key,
    the site shows an honest beta notice instead of subscribe buttons, and the
    billing endpoints refuse politely. Env override PAYMENTS_OPEN=open|closed
    forces either state (e.g. 'open' to demo the test-mode checkout on purpose)."""
    override = os.environ.get("PAYMENTS_OPEN", "").strip().lower()
    if override in ("1", "true", "yes", "open"):
        return True
    if override in ("0", "false", "no", "closed"):
        return False
    return os.environ.get("STRIPE_SECRET_KEY", "").strip().startswith("sk_live_")


def _require_payments_open() -> None:
    if not _payments_open():
        raise HTTPException(status_code=503, detail=(
            "We're in our beta period and not taking payments yet. Full access is "
            "currently by beta pass — see mrcadabra.com/beta — or email "
            "support@mrcadabra.com."))


def _stripe():
    """The configured Stripe client module, or a clear 503 when payments are off."""
    key = os.environ.get("STRIPE_SECRET_KEY", "").strip()
    if not key:
        raise HTTPException(status_code=503, detail=(
            "Payments aren't switched on yet — email support@mrcadabra.com."))
    import stripe
    stripe.api_key = key
    return stripe


def _ensure_product_tax_code(stripe, product_id: str) -> None:
    """Make sure the product carries a tax code (required by Stripe's Managed
    Payments, on by default for new accounts). Heals products created before
    this fix existed; checked at most once per product per process."""
    if not product_id or product_id in _TAX_CODE_OK:
        return
    try:
        product = stripe.Product.retrieve(product_id)
        if not getattr(product, "tax_code", None):
            stripe.Product.modify(product_id, tax_code=PRODUCT_TAX_CODE)
            print(f"[billing] set tax_code {PRODUCT_TAX_CODE} on product {product_id}")
        _TAX_CODE_OK.add(product_id)
    except Exception as exc:  # noqa: BLE001 -- let checkout surface the real error
        print(f"[billing] tax-code check failed for {product_id}: {exc}")


def _price_id(stripe, plan: str) -> str:
    """Find (or create, exactly once) the Stripe Price for a plan, by lookup key."""
    lookup = _PLAN_LOOKUP[plan]
    if lookup in _PRICE_ID_CACHE:
        return _PRICE_ID_CACHE[lookup]
    found = stripe.Price.list(lookup_keys=[lookup], active=True, limit=1)
    if found.data:
        # Heal a product made before the tax-code fix (Managed Payments needs it).
        _ensure_product_tax_code(stripe, getattr(found.data[0], "product", None))
        _PRICE_ID_CACHE[lookup] = found.data[0].id
        return found.data[0].id
    # First ever run against this Stripe account: create the product + price.
    product_id = None
    # 2026-08-03 REBRAND: match the old "MyTutor" product too, so an account that already
    # has it reuses (and renames) it instead of creating a duplicate.
    for p in stripe.Product.list(active=True, limit=100).auto_paging_iter():
        if p.name in ("Mr. Cadabra's Classroom — Full access", "MyTutor Full access"):
            product_id = p.id
            if p.name != "Mr. Cadabra's Classroom — Full access":
                try:
                    stripe.Product.modify(product_id, name="Mr. Cadabra's Classroom — Full access")
                except Exception as exc:  # noqa: BLE001 -- a rename must never block checkout
                    print(f"[billing] product rename skipped: {exc}")
            break
    if not product_id:
        product_id = stripe.Product.create(
            name="Mr. Cadabra's Classroom — Full access",
            tax_code=PRODUCT_TAX_CODE,     # required by Managed Payments (default-on)
            description="All ten math courses with Mr. Cadabra — placement to mastery, "
                        "real spoken conversation, honest dashboards.").id
    else:
        _ensure_product_tax_code(stripe, product_id)
    _TAX_CODE_OK.add(product_id)
    price = stripe.Price.create(
        product=product_id, currency="usd", unit_amount=_PLAN_AMOUNTS[plan],
        recurring={"interval": ("month" if plan == "monthly" else "year")},
        lookup_key=lookup, transfer_lookup_key=True)
    _PRICE_ID_CACHE[lookup] = price.id
    return price.id


def _stripe_customer_id(stripe, parent: dict) -> str:
    """This parent's Stripe customer, created on first need and remembered."""
    if parent.get("stripe_customer_id"):
        return parent["stripe_customer_id"]
    customer = stripe.Customer.create(
        email=parent.get("email"), name=parent.get("name") or None,
        metadata={"parent_id": parent["id"]})
    store.update_parent(parent["id"], stripe_customer_id=customer.id)
    return customer.id


@app.post("/api/billing/checkout")
def billing_checkout(body: CheckoutIn):
    """Start a Stripe Checkout for this parent: quantity = their number of students."""
    _require_payments_open()
    parent = _require_parent(body.token)
    plan = (body.plan or "monthly").strip().lower()
    if plan not in _PLAN_LOOKUP:
        raise HTTPException(status_code=400, detail="Plan must be 'monthly' or 'annual'.")
    students = store.list_students_for_parent(parent["id"])
    if not students:
        raise HTTPException(status_code=400, detail=(
            "Add your student first — the subscription covers each student you add."))
    stripe = _stripe()
    try:
        session = stripe.checkout.Session.create(
            mode="subscription",
            customer=_stripe_customer_id(stripe, parent),
            line_items=[{"price": _price_id(stripe, plan),
                         "quantity": _seats_for(len(students))}],
            allow_promotion_codes=True,
            client_reference_id=parent["id"],
            subscription_data={"metadata": {"parent_id": parent["id"]}},
            success_url=SITE_URL + "/family?checkout=success",
            cancel_url=SITE_URL + "/family?checkout=canceled",
        )
    except Exception as exc:  # noqa: BLE001
        print(f"[billing] checkout failed for {parent['id']}: {exc}")
        raise HTTPException(status_code=502, detail=(
            "Stripe couldn't start the checkout — please try again in a minute."))
    return {"ok": True, "url": session.url}


@app.post("/api/billing/portal")
def billing_portal(body: ParentTokenIn):
    """Send the parent to Stripe's hosted portal: update card, switch plan, cancel."""
    _require_payments_open()
    parent = _require_parent(body.token)
    if not parent.get("stripe_customer_id"):
        raise HTTPException(status_code=400, detail="No billing set up yet — subscribe first.")
    stripe = _stripe()
    try:
        session = stripe.billing_portal.Session.create(
            customer=parent["stripe_customer_id"],
            return_url=SITE_URL + "/family")
    except Exception as exc:  # noqa: BLE001
        print(f"[billing] portal failed for {parent['id']}: {exc}")
        raise HTTPException(status_code=502, detail=(
            "Stripe couldn't open the billing page — please try again in a minute."))
    return {"ok": True, "url": session.url}


@app.post("/api/billing/cover")
def billing_cover(body: ParentTokenIn):
    """Parent added a child while subscribed: bump the subscription quantity to
    cover every student (Stripe prorates the difference automatically)."""
    _require_payments_open()
    parent = _require_parent(body.token)
    if (parent.get("sub_status") or "") != "active" or not parent.get("stripe_customer_id"):
        raise HTTPException(status_code=400, detail="No active subscription to update.")
    students = store.list_students_for_parent(parent["id"])
    stripe = _stripe()
    try:
        subs = stripe.Subscription.list(customer=parent["stripe_customer_id"],
                                        status="active", limit=1)
        if not subs.data:
            raise HTTPException(status_code=400, detail="No active subscription found in Stripe.")
        sub = subs.data[0]
        item = sub["items"]["data"][0]
        stripe.Subscription.modify(
            sub.id,
            items=[{"id": item.id, "quantity": _seats_for(len(students))}],
            proration_behavior="create_prorations")
    except HTTPException:
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"[billing] cover failed for {parent['id']}: {exc}")
        raise HTTPException(status_code=502, detail=(
            "Stripe couldn't update the plan — please try again in a minute."))
    # The webhook will confirm, but reflect the new seat count right away too.
    store.update_parent(parent["id"], sub_quantity=_seats_for(len(students)))
    return _parent_payload(store.get_parent(parent["id"]))


def _apply_subscription(sub: dict) -> None:
    """Fold a Stripe subscription object into the parent's row. Called ONLY from
    the signature-verified webhook. Maps Stripe's status vocabulary to ours."""
    customer_id = sub.get("customer") or ""
    parent = store.get_parent_by_customer(customer_id)
    if not parent:
        pid = ((sub.get("metadata") or {}).get("parent_id") or "").strip()
        parent = store.get_parent(pid) if pid else None
        if parent and customer_id:
            store.update_parent(parent["id"], stripe_customer_id=customer_id)
    if not parent:
        print(f"[billing] webhook: no parent for customer {customer_id}")
        return
    s = sub.get("status") or ""
    status = ("active" if s in ("active", "trialing")
              else "past_due" if s in ("past_due",)
              else "canceled" if s in ("canceled", "unpaid", "incomplete_expired")
              else parent.get("sub_status") or "free")   # 'incomplete' etc: no change
    items = ((sub.get("items") or {}).get("data") or [{}])
    quantity = int(items[0].get("quantity") or 0)
    lookup = ((items[0].get("price") or {}).get("lookup_key") or "")
    plan = ("annual" if "annual" in lookup
            else "monthly" if "monthly" in lookup
            else parent.get("sub_plan") or "")
    period_end = None
    ts = sub.get("current_period_end") or items[0].get("current_period_end")
    if ts:
        import datetime as _dt3
        period_end = _dt3.datetime.fromtimestamp(int(ts), tz=_dt3.timezone.utc)
    if status == "canceled":
        quantity = 0
    store.update_parent(parent["id"], sub_status=status, sub_plan=plan,
                        sub_quantity=quantity, sub_period_end=period_end)
    # build hs: the log line carries a MASKED address -- a parent's email is PII and
    # these logs live on infrastructure we do not control (review Class F).
    _be = str(parent.get("email") or "")
    print(f"[billing] {_be[:2]}***@{_be.split('@')[-1] if '@' in _be else '?'}: "
          f"{status} x{quantity} ({plan})")


@app.post("/api/stripe/webhook")
async def stripe_webhook(request: Request):
    """Stripe's messenger. Signature-verified with STRIPE_WEBHOOK_SECRET -- an
    unsigned or tampered call changes nothing and gets a 400."""
    _require_db()
    secret = os.environ.get("STRIPE_WEBHOOK_SECRET", "").strip()
    if not secret:
        raise HTTPException(status_code=503, detail="Webhook not configured.")
    import stripe
    payload = await request.body()
    sig = request.headers.get("stripe-signature", "")
    try:
        stripe.Webhook.construct_event(payload, sig, secret)   # signature check
    except Exception:  # bad signature or malformed payload
        raise HTTPException(status_code=400, detail="Invalid signature.")
    # Signature verified -- now read the payload as PLAIN dicts (the Stripe SDK's
    # wrapper objects change shape between versions; raw JSON does not).
    try:
        event = json.loads(payload)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise HTTPException(status_code=400, detail="Invalid payload.")
    etype = event.get("type") or ""
    obj = (event.get("data") or {}).get("object") or {}
    if etype == "checkout.session.completed":
        # Remember which Stripe customer this parent became; the subscription
        # events (below) carry the actual status/quantity.
        pid = (obj.get("client_reference_id") or "").strip()
        cust = obj.get("customer") or ""
        if pid and cust:
            parent = store.get_parent(pid)
            if parent and not parent.get("stripe_customer_id"):
                store.update_parent(pid, stripe_customer_id=cust)
    elif etype in ("customer.subscription.created", "customer.subscription.updated",
                   "customer.subscription.deleted"):
        _apply_subscription(obj)
    return {"received": True}


# =============================================================================
# COMMUNITY FORUM (2026-07-31) -- parents post, everyone reads
# -----------------------------------------------------------------------------
# Four sections: what's working / ideas for improvement / resources for parents /
# course requests. Reading is public. WRITING requires a signed-in parent (the
# accounts built today) -- students never post, and no email or child data ever
# appears: authors show as the parent's first name only, or "A MyTutor parent".
# Moderation: FORUM_MOD_KEY env var + POST /api/forum/moderate soft-deletes
# (hides, never destroys). Writes are rate-limited per parent AND per IP.
# =============================================================================

FORUM_SECTION_TITLES = {
    "working": "What's working for your family",
    "ideas": "Ideas for improvement",
    "resources": "Resources for parents",
    "courses": "Courses you'd like to see",
}


class ForumPostIn(BaseModel):
    token: str
    section: str
    title: str
    body: str = ""


class ForumReplyIn(BaseModel):
    token: str
    post_id: str
    body: str


class ForumModIn(BaseModel):
    key: str = ""              # LEGACY transport (build dn): the page now sends the key
                               # in the X-Admin-Key header; the body field stays accepted
                               # so an old cached page keeps working across the deploy.
    kind: str                  # 'post' | 'reply'
    item_id: str


def _forum_author(parent: dict) -> str:
    first = (parent.get("name") or "").strip().split(" ")[0]
    return first if first else "A parent"


@app.get("/api/forum/{section}")
def forum_list(section: str):
    """Public: the posts in one section, newest first."""
    _require_db()
    if section not in store.FORUM_SECTIONS:
        raise HTTPException(status_code=404, detail="No such section.")
    return {"ok": True, "section": section,
            "title": FORUM_SECTION_TITLES[section],
            "posts": store.list_forum_posts(section)}


@app.get("/api/forum/post/{post_id}")
def forum_post_detail(post_id: str):
    """Public: one post with its replies."""
    _require_db()
    post = store.get_forum_post((post_id or "").strip())
    if not post:
        raise HTTPException(status_code=404, detail="That post isn't here anymore.")
    return {"ok": True, "post": post}


@app.post("/api/forum/post")
def forum_create_post(body: ForumPostIn, request: Request):
    parent = _require_parent(body.token)
    _rate_limit("forum:" + parent["id"], limit=6, window_seconds=600, what="posts")
    _rate_limit("forumip:" + _client_ip(request), limit=12, window_seconds=600, what="posts")
    section = (body.section or "").strip().lower()
    if section not in store.FORUM_SECTIONS:
        raise HTTPException(status_code=400, detail="Please pick a section.")
    title = (body.title or "").strip()[:140]
    text = (body.body or "").strip()[:4000]
    if len(title) < 4:
        raise HTTPException(status_code=400, detail="Please give your post a short title.")
    store.create_forum_post(uuid.uuid4().hex, section, title, text,
                            parent["id"], _forum_author(parent))
    return {"ok": True, "posts": store.list_forum_posts(section)}


@app.post("/api/forum/reply")
def forum_create_reply(body: ForumReplyIn, request: Request):
    parent = _require_parent(body.token)
    _rate_limit("forum:" + parent["id"], limit=6, window_seconds=600, what="posts")
    _rate_limit("forumip:" + _client_ip(request), limit=12, window_seconds=600, what="posts")
    text = (body.body or "").strip()[:4000]
    if len(text) < 2:
        raise HTTPException(status_code=400, detail="Please write a reply first.")
    if not store.create_forum_reply(uuid.uuid4().hex, (body.post_id or "").strip(),
                                    text, parent["id"], _forum_author(parent)):
        raise HTTPException(status_code=404, detail="That post isn't here anymore.")
    return {"ok": True, "post": store.get_forum_post((body.post_id or "").strip())}


@app.post("/api/forum/moderate")
def forum_moderate(body: ForumModIn,
                   x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """Jim's moderation: soft-delete a post or reply. Needs FORUM_MOD_KEY (env).
    BUILD dn: key accepted in the X-Admin-Key header (preferred -- the old
    /community?mod= link put it in a URL, and query strings land in Render's logs
    in plaintext); the body key stays accepted for a cached pre-dn page only.
    Same _require_admin constant-time gate as every other admin call."""
    _require_db()
    _require_admin(x_admin_key or body.key)
    if body.kind not in ("post", "reply"):
        raise HTTPException(status_code=400, detail="kind must be 'post' or 'reply'.")
    if not store.delete_forum_item(body.kind, (body.item_id or "").strip()):
        raise HTTPException(status_code=404, detail="Nothing with that id.")
    return {"ok": True}


class FlagIn(BaseModel):
    """(nq) One owner-flagged sentence from a live lesson."""
    key: str = ""              # legacy transport; the page sends X-Admin-Key header
    page: str = ""             # 'session' | 'practice' | 'topic' | ...
    course: str = ""
    code: str = ""             # the student login code the owner was watching
    quote: str = ""            # the bubble text he tapped
    note: str = ""             # what should have been said / what's wrong


class FlagResolveIn(BaseModel):
    key: str = ""
    id: int


@app.post("/api/flag")
def flag_sentence(body: FlagIn,
                  x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """BUILD nq (2026-08-25): the owner's flag. Jim taps the flag on a tutor bubble,
    types what's wrong, and the sentence lands in his corrections queue on /admin.
    ADMIN-KEY GATED on purpose -- Jim: "I only want it when I'm online. I don't want
    the parents or teachers to see it." No key, no write; the button itself never
    renders without the key, but the server does not trust the page."""
    _require_db()
    _require_admin(x_admin_key or body.key)
    quote = (body.quote or "").strip()
    if len(quote) < 2:
        raise HTTPException(status_code=400, detail="Nothing to flag -- empty quote.")
    fid = store.add_flag(page=(body.page or "").strip(),
                         course=(body.course or "").strip(),
                         code=(body.code or "").strip(),
                         quote=quote,
                         note=(body.note or "").strip())
    if not fid:
        raise HTTPException(status_code=500, detail="Could not save the flag.")
    return {"ok": True, "id": fid}


@app.get("/api/admin/student")
def admin_student(request: Request, code: str = "",
                  x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """(uf, 2026-09-08) THE PER-STUDENT VIEW -- P2 of the deep look, second half.
    The admin console could see totals and tables but could not answer "how is
    Sam doing". This is one student, everything, read-only: the courses they have
    touched with every unit's status (in the ue words: "Lesson done" is a finished
    lesson, "Mastered" is the 90% Unit Quiz), the lessons done with dates, every
    graded answer in the authored lane (script_answers, newest first), the topic
    quizzes and Unit Quizzes, the engaged minutes by day, the awards, the streaks.
    BY CODE, TYPED -- there is deliberately no route that LISTS student codes
    (finding F2 closed enumeration); the owner types the code the family has.
    General admin tier, header only (build dg), rate-limited. 404 for a code that
    is not a known student."""
    _require_db()
    _require_admin(x_admin_key)
    _rate_limit("admin-student", limit=120, window_seconds=600, what="student lookups")
    code = (code or "").strip()
    if not code:
        raise HTTPException(status_code=400, detail="Type a student code.")
    student = _lookup_student(code)
    if not student:
        raise HTTPException(status_code=404, detail="That code isn't a known student.")

    # ---- whole-student numbers (get_mastery's stats are whole-student by design)
    courses_seen = store.student_courses(code)
    try:
        stats = (store.get_mastery(code, courses_seen[0] if courses_seen else "algebra1")
                 or {}).get("stats", {})
    except Exception as exc:  # noqa: BLE001
        print(f"[admin-student] get_mastery failed: {exc}")
        stats = {}
    try:
        answer_stats = store.script_answer_stats(code)
    except Exception as exc:  # noqa: BLE001
        print(f"[admin-student] script_answer_stats failed: {exc}")
        answer_stats = {}

    # ---- per course: units, lessons done, quizzes, checks
    courses, lessons, quizzes, checks = [], [], [], []
    for cid in courses_seen:
        if cid not in curriculum.COURSES:
            continue
        try:
            recorded = {r["unit"]: r for r in store.get_topics(code, cid)}
            uchecks = (store.get_mastery(code, cid) or {}).get("checks", {})
            quiz_rows = store.get_topic_quizzes(code, cid)
            done_rows = store.get_script_done(code, cid) or []
        except Exception as exc:  # noqa: BLE001
            print(f"[admin-student] course {cid} read failed: {exc}")
            continue
        lu = _lessons_by_unit(code, cid)
        units = []
        for n, name in curriculum.units_for(cid):
            r = recorded.get(n) or {}
            c = uchecks.get(n) or {}
            best = int(c.get("best_pct") or 0)
            l = lu.get(n) or {"done": 0, "total": 0}
            units.append({"unit": n, "name": name,
                          "status": r.get("status") or "not-started",
                          "touches": int(r.get("touches") or 0),
                          "last_touched": r.get("last_touched"),
                          "lessons_done": l["done"], "lessons_total": l["total"],
                          "quizzes_passed": len([q for q in quiz_rows if q["unit"] == n
                                                 and q["best_pct"] >= store.QUIZ_PASS_PCT]),
                          "best_pct": best, "checks_taken": int(c.get("checks_taken") or 0),
                          "mastered": best >= store.PASS_PCT})
            if c:
                checks.append({"course": cid, "course_title": curriculum.course_title(cid),
                               "unit": n, "name": name, "best_pct": best,
                               "last_pct": int(c.get("last_pct") or 0),
                               "checks_taken": int(c.get("checks_taken") or 0),
                               "mastered": best >= store.PASS_PCT})
        for q in quiz_rows:
            quizzes.append({"course": cid, "course_title": curriculum.course_title(cid),
                            "unit": q["unit"], "topic": q["topic_name"],
                            "best_pct": q["best_pct"],
                            "passed": q["best_pct"] >= store.QUIZ_PASS_PCT})
        for d in done_rows:
            les = lessonscripts.LESSON_BY_ID.get(d.get("lesson_id") or "") or {}
            lessons.append({"course": cid, "course_title": curriculum.course_title(cid),
                            "lesson_id": d.get("lesson_id"),
                            "topic": les.get("topic") or d.get("lesson_id"),
                            "unit": les.get("unit"), "three_in_a_row": bool(d.get("mastered")),
                            "runs": int(d.get("runs") or 0), "last_at": d.get("last_at")})
        last = [u["last_touched"] for u in units if u["last_touched"]]
        courses.append({"course": cid, "title": curriculum.course_title(cid), "units": units,
                        "units_mastered": len([u for u in units if u["mastered"]]),
                        "units_started": len([u for u in units if u["status"] != "not-started"]),
                        "lessons_done": sum(u["lessons_done"] for u in units),
                        "lessons_total": sum(u["lessons_total"] for u in units),
                        "last_active": max(last) if last else None})
    lessons.sort(key=lambda x: x.get("last_at") or "", reverse=True)
    courses.sort(key=lambda c: c.get("last_active") or "", reverse=True)

    # ---- every graded answer in the authored lane, newest first
    answers = []
    try:
        for a in store.get_script_answers(code, limit=150):
            les = lessonscripts.LESSON_BY_ID.get(a.get("lesson_id") or "") or {}
            a = dict(a)
            a["topic"] = les.get("topic") or a.get("lesson_id")
            a["course_title"] = curriculum.course_title(a.get("course") or "")
            answers.append(a)
    except Exception as exc:  # noqa: BLE001
        print(f"[admin-student] get_script_answers failed: {exc}")

    # ---- engaged minutes by day, 30 days
    time_days, minutes_7d, minutes_all = [], 0, 0
    try:
        agg: dict = {}
        for r in store.get_time(code, days=30):
            d = agg.setdefault(r["day"], {"day": r["day"], "minutes": 0, "courses": {}})
            d["minutes"] += r["minutes"]
            d["courses"][r["course"]] = d["courses"].get(r["course"], 0) + r["minutes"]
        time_days = sorted(agg.values(), key=lambda x: x["day"], reverse=True)[:30]
        import datetime as _dtm
        cutoff7 = (_dtm.date.today() - _dtm.timedelta(days=6)).isoformat()
        minutes_7d = sum(d["minutes"] for d in time_days if d["day"] >= cutoff7)
        minutes_all = sum(r["minutes"] for r in store.get_time(code, days=3650))
    except Exception as exc:  # noqa: BLE001
        print(f"[admin-student] get_time failed: {exc}")

    awards = []
    try:
        for aid, earned in store.get_awards(code).items():
            if aid in AWARD_DEFS:
                awards.append({"id": aid, "icon": AWARD_DEFS[aid][0],
                               "title": AWARD_DEFS[aid][1], "earned_at": earned})
        awards.sort(key=lambda a: a.get("earned_at") or "", reverse=True)
    except Exception as exc:  # noqa: BLE001
        print(f"[admin-student] get_awards failed: {exc}")

    return {"ok": True, "code_masked": _mask_code(code),
            "name": student.get("name") or "", "grade": student.get("grade") or "",
            "family": bool(student.get("family")),
            "stats": stats, "answer_stats": answer_stats,
            "time": {"days": time_days, "minutes_7d": minutes_7d, "minutes_all": minutes_all,
                     "active_days_30d": len([d for d in time_days if d["minutes"] > 0])},
            "courses": courses, "lessons": lessons, "answers": answers,
            "quizzes": quizzes, "checks": checks, "awards": awards}


@app.get("/api/admin/flags")
def admin_flags(key: str = "", include_resolved: int = 0,
                x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """(nq) The owner's corrections queue, newest first. Same admin gate."""
    _require_db()
    _require_admin(x_admin_key or key)
    flags = store.list_flags(include_resolved=bool(include_resolved))
    return {"ok": True, "flags": flags,
            "open": sum(1 for f in flags if not f.get("resolved"))}


@app.post("/api/admin/flags/resolve")
def admin_flags_resolve(body: FlagResolveIn,
                        x_admin_key: str = Header(default="", alias="X-Admin-Key")):
    """(nq) Mark a flag handled once the correction has shipped."""
    _require_db()
    _require_admin(x_admin_key or body.key)
    if not store.resolve_flag(body.id):
        raise HTTPException(status_code=404, detail="No flag with that id.")
    return {"ok": True, "flags": store.list_flags(include_resolved=False)}


@app.get("/api/courses/{code}")
def student_courses(request: Request, code: str = Depends(_code_dep)):
    """EVERY course this student has actually worked in, with units mastered/started -- for the
    dashboard's "My courses" strip. Returns courses with REAL activity only, in ladder order, so
    a student sees their whole picture at a glance and can switch with one click. When tracking is
    off it reports that rather than inventing anything."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False, "courses": []}
    try:
        activity = store.get_course_activity(code)
    except Exception as exc:  # noqa: BLE001
        print(f"[courses] get_course_activity failed: {exc}")
        activity = {}
    courses = []
    for cid, title in curriculum.list_courses():          # ladder order
        a = activity.get(cid)
        if not a:
            continue                                      # never opened -> don't show a shell
        courses.append({
            "course": cid,
            "title": title,
            "units_total": len(curriculum.units_for(cid)),
            "units_started": a.get("units_started", 0),
            "units_mastered": a.get("units_mastered", 0),
            "units_checked": a.get("units_checked", 0),
            "avg_best_pct": a.get("avg_best_pct"),
            "last_active": a.get("last_active"),
        })
    return {"ok": True, "tracking": True, "courses": courses}


@app.post("/api/placement/{code}")
def post_placement(body: PlacementIn, code: str = Depends(_code_dep), course: str = "algebra1"):
    """Save the result of Mr. Cadabra's Challenge for this student, for THIS course."""
    _student_or_404(code)
    save_placement(code.strip(), body.model_dump(), course)
    return {"ok": True}


# =============================================================================
# LOOK-IT-UP LIBRARY (2026-08-07, Jim) -- the searchable reference database
# -----------------------------------------------------------------------------
# A stuck student clicks 📖 Look it up, types a topic ("binomial theorem", "adding
# dollars and cents"), and gets a READABLE article in a bubble -- the tutor's voice
# and the chat turn are never involved. Resolution order (see library.py):
#   curated seed -> saved article (exact key) -> fuzzy match across both -> the
#   GENERATE-ONCE fallback (one model call, saved forever, ~2 cents).
# Reading level follows the course's band, so the same search reads gently in
# Basic Math and tersely in Algebra II.
# =============================================================================
@app.get("/api/library")
def library_lookup(q: str = "", course: str = "algebra1", code: str = "",
                   x_student_code: str = Header(default="", alias="X-Student-Code")):
    """Serve one reference article for a student's search. Students only; the
    generation path is rate-limited separately (it spends model money).
    build hs: the code prefers the X-Student-Code header (library.js sends it that
    way now); the query form remains for stale cached pages."""
    code = (x_student_code or code or "").strip()
    _student_or_404(code)
    code = code.strip()
    q = (q or "").strip()[:160]
    if len(q) < 2:
        raise HTTPException(status_code=400, detail="Type a topic to look up first.")
    _rate_limit("lib:" + code, limit=30, window_seconds=300, what="lookups")
    band = library.band_for(course if course in curriculum.COURSES else "algebra1")
    key = library.norm_key(q)

    # 1) Curated seed, exact alias.
    seed = library.find_seed(q, band)
    if seed:
        return {"title": seed["title"], "body": library.scrub_html(seed["body"]),
                "source": "library"}
    # 2) Saved article, exact key.
    if store.enabled():
        hit = store.get_library_article(key, band)
        if hit:
            store.bump_library_hits(key, band)
            return {"title": hit["title"], "body": hit["body"], "source": "library"}
    # 3) Fuzzy match across seeds (this band's neighborhood) + saved titles.
    candidates = [s for s in library.SEEDS if library.find_seed(s["title"], band)]
    if store.enabled():
        try:
            candidates = candidates + store.list_library_titles(band)
        except Exception as exc:  # noqa: BLE001
            print(f"[library] title list failed: {exc}")
    pick = library.fuzzy_pick(q, candidates)
    if pick:
        if "body" in pick:      # a seed
            return {"title": pick["title"], "body": library.scrub_html(pick["body"]),
                    "source": "library"}
        hit = store.get_library_article(pick["key"], band) if store.enabled() else {}
        if hit:
            store.bump_library_hits(pick["key"], band)
            return {"title": hit["title"], "body": hit["body"], "source": "library"}
    # 4) Generate once, save forever. Tighter limit -- this path costs money.
    _rate_limit("libgen:" + code, limit=6, window_seconds=300, what="new lookups")
    art = library.generate_article(q, band)
    if not art:
        return {"title": "", "body": "", "source": "none",
                "detail": "I couldn't find that in the library — try different words, "
                          "or ask Mr. Cadabra about it in the lesson."}
    if store.enabled():
        try:
            store.save_library_article(key, band, art["title"], art["body"])
        except Exception as exc:  # noqa: BLE001
            print(f"[library] save failed: {exc}")
    return {"title": art["title"], "body": art["body"], "source": "new"}


# =============================================================================
# FINAL EXAM (2026-08-07, Jim) -- a real course final, HARD-GATED on mastery
# -----------------------------------------------------------------------------
# The rule, in Jim's words: "to take the final exam, they have to have mastered
# everything else in the course ahead of time" -- and the optional 'Prepare for the
# Final Exam' overview is gated exactly the same way. The gate is enforced HERE, on
# the server, on every chat turn and every score post; the page's button state is
# only a courtesy. Mastered = best Unit Quiz >= store.PASS_PCT (90) on all 9 units.
# =============================================================================
FINAL_GATE_MESSAGE = (
    "The Final Exam preparation and the Final Exam are only available to students who "
    "have mastered all the previous units of the course. You've mastered {n} of {req} so far "
    "-- every unit you master gets you one step closer. Keep going; I'll be right here "
    "when you're ready!")


def _units_required(course: str) -> int:
    """How many units this course's Final Exam requires -- ALWAYS derived from the
    course's real unit list, never a literal.

    2026-08-13 (build ew). The old code said `\"required\": 9` and `>= 9` -- correct for
    every course today only by coincidence (all ten happen to have nine units). The day
    any course gained or lost a unit, the exam would silently unlock early or never
    unlock at all, and nothing would fail. Fallback 9 (today's universal truth) only if
    curriculum itself errors, because a locked-forever exam is the worse failure."""
    try:
        n = len(curriculum.units_for(course))
        if n > 0:
            return n
    except Exception as exc:  # noqa: BLE001
        print(f"[final] units_required fell back for {course!r}: {exc}")
    return 9


def _final_gate_message(code: str, course: str, state: dict) -> str:
    """The locked-door message, with the door's key attached.

    2026-08-10 (build cu, Jim): "I can do all the units and still be carrying an
    eighty-five with me, which is gonna keep me from mastering the final exam. There needs
    to be some type of option to review and retake that quiz."
    The old message said "you've mastered 3 of 9" and stopped there -- true, useless, and
    arriving months after the unit it is about. A student standing at a locked door needs
    to know WHICH units are holding it shut, how close each one is, and that a retake can
    only ever help them. Units already ATTEMPTED come first and carry their best score,
    because those are the ones a single good session can finish. Falls back to the old
    wording if the record cannot be read -- a locked door must never also be a silent one.
    """
    try:
        names = {}
        for i, u in enumerate(curriculum.units_for(course)):
            if isinstance(u, (list, tuple)) and len(u) >= 2:
                names[int(u[0])] = str(u[1])
            else:
                names[i + 1] = str(u)
        checks = (store.get_mastery(code, course) or {}).get("checks", {}) if store.enabled() else {}
        close, untouched = [], []
        for unit in sorted(names):
            if unit in set(state.get("mastered_units") or []):
                continue
            c = checks.get(unit) or checks.get(str(unit)) or {}
            best = int(c.get("best_pct") or 0)
            if int(c.get("checks_taken") or 0) > 0:
                close.append(f"Unit {unit}, {names[unit]} (best Unit Quiz so far: {best}%)")
            else:
                untouched.append(f"Unit {unit}, {names[unit]}")
        req = int(state.get("required") or _units_required(course))
        if not close and not untouched:
            return FINAL_GATE_MESSAGE.format(n=state.get("mastered_count", 0), req=req)
        msg = (f"The Final Exam unlocks when all {req} units are mastered -- 90% or better on "
               f"each Unit Quiz. You've mastered {state.get('mastered_count', 0)} of {req}.\n\n")
        if close:
            msg += ("These you've already taken a run at, so they're the quickest to finish:\n  - "
                    + "\n  - ".join(close)
                    + "\n\nAny of those we can review together and retake right now -- new questions, "
                      "and the record always keeps your BEST score, so a retake can only ever help "
                      "you. Just say which one.\n\n")
        if untouched:
            msg += "Still to come:\n  - " + "\n  - ".join(untouched) + "\n\n"
        return msg + "Tell me where you'd like to start and I'll get us going."
    except Exception as exc:  # noqa: BLE001
        print(f"[final] gate message fell back: {exc}")
        return FINAL_GATE_MESSAGE.format(n=state.get("mastered_count", 0),
                                         req=_units_required(course))


def _final_exam_state(code: str, course: str) -> dict:
    """The student's final-exam picture for a course: which units are mastered, whether
    the exam is unlocked, and any recorded exam result. Honest when the DB is off."""
    mastered = []
    if store.enabled():
        try:
            checks = (store.get_mastery(code, course) or {}).get("checks", {})
            mastered = sorted(int(u) for u, c in checks.items()
                              if int((c or {}).get("best_pct") or 0) >= store.PASS_PCT)
        except Exception as exc:  # noqa: BLE001
            print(f"[final] mastery read failed: {exc}")
    exam = {}
    if store.enabled():
        try:
            exam = store.get_final_exam(code, course) or {}
        except Exception as exc:  # noqa: BLE001
            print(f"[final] exam read failed: {exc}")
    required = _units_required(course)   # build ew: derived, never a literal 9
    return {
        "mastered_units": mastered,
        "mastered_count": len(mastered),
        "required": required,
        "eligible": len(mastered) >= required,
        "exam": exam,
    }


@app.get("/api/sprints/{code}")
def api_sprint_record(request: Request, code: str = Depends(_code_dep), course: str = "prealgebra"):
    """The student's whole sprint history for one course, oldest first -- the
    dashboard's '⚡ Your sprint record' card (2026-08-11, build dm). WWC guide 26
    rec. 6 says track progress AND SHOW it; the data has recorded since build dd and
    nothing displayed it. Self-referential only (rule 42): this student's rounds,
    this student's best, nobody else's anything. Empty history -> the card never
    renders (sprints never gate and never nag)."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    if not store.enabled():
        return {"ok": True, "history": [], "best_b": 0}
    try:
        rows = store.get_sprint_history(code.strip(), course, unit=None, limit=30)
    except Exception as exc:  # noqa: BLE001 -- the card is a bonus, never a 500
        print(f"[sprint] record read failed: {exc}")
        rows = []
    rows = list(reversed(rows))                      # oldest first, for a growth line
    return {"ok": True, "history": rows,
            "best_b": max([r["b"] for r in rows], default=0)}


@app.get("/api/sprint/{code}")
def get_sprint(request: Request, code: str = Depends(_code_dep), course: str = "prealgebra", unit: int = 1):
    """The day's fluency sprint for this student+course+unit, or {available:false}.

    2026-08-11 (build dd). WWC guide 26 recommendation 6 (STRONG): "regularly include
    timed activities... track and monitor progress". Format follows Eureka's Sprints
    (studied, not copied -- see sprints.py's licence note): two sibling halves, the
    celebrated number is B minus A, and the ONLY comparison is with this student's own
    history (rule 42).
    Seeded per student-per-day: a re-request today rebuilds the SAME sprint (a reload
    mid-sprint changes nothing); tomorrow's is fresh. ⚠️ NEVER GATES: nothing anywhere
    reads sprint results as a requirement, and declining is simply not calling this."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    code = code.strip()
    if sprints is None or not sprints.available(course, unit):
        return {"available": False}
    import datetime as _dt
    day = _dt.date.today().isoformat()
    built = sprints.build(course, unit, f"{code}|{course}|{unit}|{day}")
    out = {"available": True, "skill": built["skill"], "unit": int(unit),
           "a": built["a"], "b": built["b"], "seconds": 60,
           "history": [], "best_b": 0, "done_today": False}
    if store.enabled():
        try:
            hist = store.get_sprint_history(code, course, unit, limit=8)
            out["history"] = hist
            out["best_b"] = max([h["b"] for h in hist], default=0)
            out["done_today"] = any(h["day"] == day for h in hist)
        except Exception as exc:  # noqa: BLE001
            print(f"[sprint] history read failed: {exc}")
    return out


@app.post("/api/sprint/{code}")
def post_sprint(body: SprintResultIn, code: str = Depends(_code_dep)):
    """Record a finished sprint. Counts are re-clamped in store.record_sprint (correct
    <= attempted <= 30) so the dashboards this feeds stay honest. Returns the
    celebration facts: improvement, best_b, personal_best -- all self-referential."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    try:
        res = store.record_sprint(code, body.course, int(body.unit), body.skill,
                                  int(body.a_correct), int(body.a_attempted),
                                  int(body.b_correct), int(body.b_attempted))
        return {"ok": True, "tracking": True, **res}
    except Exception as exc:  # noqa: BLE001
        print(f"[sprint] record failed: {exc}")
        return {"ok": False, "tracking": True}


# =============================================================================
# BUILD hu (2026-08-18, Phase 5 -- review Class E): FACTS ENTER THE DATABASE
# THROUGH THE SERVER. Mastery used to be CLIENT-WRITTEN: the browser parsed the
# model's [[check]]/[[quiz]]/[[finalexam]] tags and POSTed the scores, and the
# server accepted them with format-only validation -- anyone holding a student code
# could mint mastery, unlock the Final, and stamp the printable record.
# Now the SERVER parses the same tags from the reply it just generated (it saw them
# first) and records the results itself. The client POSTs remain as ECHOES:
#   - an echo matching what the server just recorded  -> deduplicated, {recorded:
#     "server"} (stale cached pages keep working across the deploy; nothing double-
#     counts);
#   - a result the server never saw the model emit    -> 409 + a system_events row
#     ("client_result_rejected") -- minted mastery becomes telemetry, not truth.
# The echo ledger is in-memory with a TTL (single-process app); a restart between
# reply and echo rejects the echo harmlessly -- the server-side write already
# happened. Sprints remain client-counted for now (they never gate anything, by
# design) -- named in the Phase 5 notes, not silently skipped.
# =============================================================================
_RESULT_TAG_RE = re.compile(r"\[\[\s*(check|quiz|finalexam)\b([^\]]*?)\]\]", re.I)
_RESULT_ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
_RESULT_LEDGER: dict = {}
_RESULT_LEDGER_LOCK = threading.Lock()
_RESULT_LEDGER_TTL = 900


def _result_pct(correct, total) -> int:
    c = max(0, int(correct or 0)); t = max(1, int(total or 1))
    return (c * 100) // t


def _ledger_mark(code, course, kind, unit, topic, pct) -> None:
    with _RESULT_LEDGER_LOCK:
        if len(_RESULT_LEDGER) > 4000:
            now = time.time()
            for k in [k for k, v in _RESULT_LEDGER.items() if v[1] <= now]:
                _RESULT_LEDGER.pop(k, None)
        _RESULT_LEDGER[(code, course, kind, int(unit or 0), int(topic or 0), int(pct))] = \
            (int(pct), time.time() + _RESULT_LEDGER_TTL)


def _ledger_match(code, course, kind, unit, topic, pct) -> bool:
    with _RESULT_LEDGER_LOCK:
        v = _RESULT_LEDGER.get((code, course, kind, int(unit or 0), int(topic or 0), int(pct)))
    return bool(v and v[1] > time.time())


def _parse_missed_attr(raw) -> list:
    """The tag's missed="question => their answer | ..." into [{q, a}] -- the same
    parse the pages do, clamped downstream by _keep_misses."""
    out = []
    try:
        for part in str(raw or "").split("|"):
            if "=>" in part:
                q, _, a = part.partition("=>")
                if q.strip():
                    out.append({"q": q.strip()[:200], "a": a.strip()[:80]})
    except Exception:  # noqa: BLE001
        return []
    return out


def _record_result_tags(code: str, course: str, reply: str,
                        final_allowed: bool = False) -> None:
    """Parse the model's result tags out of the reply the server JUST generated and
    record them server-side (build hu). Never raises -- a recording surprise must
    not cost the turn; the client echo and its 409 telemetry remain the net."""
    try:
        code = (code or "").strip()
        if not code or not reply:
            return
        for m in _RESULT_TAG_RE.finditer(str(reply)):
            kind = m.group(1).lower()
            attrs = dict(_RESULT_ATTR_RE.findall(m.group(2)))
            correct = max(0, int(float(attrs.get("correct") or 0)))
            total = max(1, int(float(attrs.get("total") or 1)))
            missed = _parse_missed_attr(attrs.get("missed"))
            pct = _result_pct(correct, total)
            if kind == "check":
                unit = int(float(attrs.get("unit") or 0))
                if not (1 <= unit <= 9):
                    continue
                if store.enabled():
                    store.record_check(code, unit, correct, total,
                                       curriculum.unit_name(course, unit), course)
                    _keep_misses(code, course, unit, 0, "check", missed, correct, total)
                _ledger_mark(code, course, "check", unit, 0, pct)
                # build il: a recorded check may complete a today item (the server's call)
                _today_match_tick(code, course, curriculum.unit_name(course, unit))
            elif kind == "quiz":
                unit = int(float(attrs.get("unit") or 0))
                if not (1 <= unit <= 9):
                    continue
                topic = int(float(attrs.get("topic") or 0))
                name = str(attrs.get("name") or "").strip()[:80]
                if store.enabled():
                    store.record_topic_quiz(code, unit, name, correct, total, course,
                                            topic_idx=topic)
                    _keep_misses(code, course, unit, topic, "quiz", missed, correct, total)
                _ledger_mark(code, course, "quiz", unit, topic, pct)
                # build il: a recorded quiz may complete a today item (the server's call)
                _today_match_tick(code, course,
                                  name or curriculum.unit_name(course, unit))
            elif kind == "finalexam":
                if not final_allowed:
                    # a final tag outside an exam turn is itself a finding
                    store.record_event("client_result_rejected", "final-tag-no-exam",
                                       f"{correct}/{total}", code, course)
                    continue
                if store.enabled():
                    state = _final_exam_state(code, course)
                    if state["eligible"]:
                        store.record_final_exam(code, correct, total, course)
                        _keep_misses(code, course, 0, 0, "final", missed, correct, total)
                        _ledger_mark(code, course, "final", 0, 0, pct)
    except Exception as exc:  # noqa: BLE001
        print(f"[results] server-side recording failed (client echo remains): {exc}")


def _reject_client_result(code, course, kind, detail):
    try:
        store.record_event("client_result_rejected", kind, detail, code, course)
    except Exception:  # noqa: BLE001
        pass
    raise HTTPException(status_code=409, detail=(
        "That result didn't come from a lesson this server taught, so it wasn't "
        "recorded."))


@app.post("/api/final/{code}")
def post_final(body: FinalIn, code: str = Depends(_code_dep)):
    """Record a FINAL EXAM score ([[finalexam]] tag). Server-side gate: the score only
    records for an eligible student. Same contract style as /api/check."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    # build hu: the exam turn's [[finalexam]] tag was recorded (and gate-checked)
    # server-side in /api/chat; this POST is an echo or a mint.
    course = body.course if body.course in curriculum.COURSES else "algebra1"
    if not _ledger_match(code, course, "final", 0, 0,
                         _result_pct(body.correct, body.total)):
        _reject_client_result(code, course, "final",
                              f"{body.correct}/{body.total}")
    return {"ok": True, "tracking": True, "recorded": "server"}


@app.post("/api/check/{code}")
def post_check(body: CheckIn, code: str = Depends(_code_dep)):
    """PHASE A: record an end-of-unit CHECK score for this student (feeds mastery). No-op
    (tracking:false) when the DB is off; never raises to the caller."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    # build hu: the server already recorded this from the model's own tag; the POST
    # is an echo. Match -> dedup; no match -> the score was minted client-side.
    course = getattr(body, "course", None) or "algebra1"
    if not _ledger_match(code, course, "check", int(body.unit), 0,
                         _result_pct(body.correct, body.total)):
        _reject_client_result(code, course, "check",
                              f"unit={body.unit} {body.correct}/{body.total}")
    return {"ok": True, "tracking": True, "recorded": "server"}


@app.get("/api/records/{code}")
def records_report(request: Request, code: str = Depends(_code_dep), days: int = 90):
    """Everything the printable homeschool records report needs (2026-08-04), in one
    call: the full-range hours log, per-course unit progress (statuses, topic quizzes,
    Unit Quiz best, mastered at 90%), placement titles, and dated awards. Read-only;
    honest {tracking:false} when the DB is off."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    student = _student_or_404(code)
    code = code.strip()
    days = max(7, min(730, int(days or 90)))
    if not store.enabled():
        return {"tracking": False, "name": student.get("name"), "days": days,
                "time": [], "courses": [], "awards": []}
    from datetime import datetime, timezone, timedelta
    today = datetime.now(timezone.utc).date()
    day_from = (today - timedelta(days=days - 1)).isoformat()

    time_rows = store.get_time_between(code, day_from, today.isoformat())
    for r in time_rows:
        r["course_title"] = curriculum.course_title(r["course"]) if r["course"] in curriculum.COURSES else r["course"]

    courses = []
    try:
        activity = store.get_course_activity(code)
    except Exception as exc:  # noqa: BLE001
        print(f"[records] get_course_activity failed: {exc}")
        activity = {}
    for cid in activity:
        if cid not in curriculum.COURSES:
            continue
        try:
            recorded = {r["unit"]: r for r in store.get_topics(code, cid)}
            checks = (store.get_mastery(code, cid) or {}).get("checks", {})
            quiz_rows = {}
            for q in store.get_topic_quizzes(code, cid):
                quiz_rows.setdefault(q["unit"], []).append({
                    "name": q["topic_name"], "best_pct": q["best_pct"],
                    "passed": q["best_pct"] >= store.QUIZ_PASS_PCT})
        except Exception as exc:  # noqa: BLE001
            print(f"[records] course {cid} read failed: {exc}")
            continue
        units = []
        lessons = _lessons_by_unit(code, cid)      # (ue) lessons done, per unit
        for n, name in curriculum.units_for(cid):
            r = recorded.get(n)
            c = checks.get(n) or {}
            best = int(c.get("best_pct") or 0)
            lu = lessons.get(n) or {"done": 0, "total": 0}
            units.append({"unit": n, "name": name,
                          "status": (r["status"] if r else "not-started"),
                          "best_pct": best, "checks_taken": int(c.get("checks_taken") or 0),
                          "mastered": best >= store.PASS_PCT,
                          "quizzes": quiz_rows.get(n, []),
                          "lessons_done": lu["done"], "lessons_total": lu["total"]})
        placement = read_placement(code, cid) or {}
        courses.append({"course": cid, "title": curriculum.course_title(cid),
                        "placement": placement.get("level_title") or "",
                        "units": units,
                        "units_mastered": len([u for u in units if u["mastered"]])})
    courses.sort(key=lambda c: -c["units_mastered"])

    awards = []
    try:
        for aid, earned in store.get_awards(code).items():
            if aid in AWARD_DEFS:
                d = AWARD_DEFS[aid]
                awards.append({"icon": d[0], "title": d[1], "desc": d[2], "earned_at": earned})
        awards.sort(key=lambda a: a["earned_at"] or "")
    except Exception as exc:  # noqa: BLE001
        print(f"[records] awards read failed: {exc}")

    return {"tracking": True, "name": student.get("name"), "days": days,
            "time": time_rows, "courses": courses, "awards": awards}


@app.post("/api/quiz/{code}")
def post_quiz(body: QuizIn, code: str = Depends(_code_dep)):
    """Record a mid-unit TOPIC QUIZ score (2026-08-04). Same contract style as
    /api/check: no-op (tracking:false) when the DB is off; never raises."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    # build hu: echo of the server-recorded tag, or a minted score (see the note
    # above post_final).
    course = body.course if body.course in curriculum.COURSES else "algebra1"
    if not _ledger_match(code, course, "quiz", int(body.unit), int(body.topic or 0),
                         _result_pct(body.correct, body.total)):
        _reject_client_result(code, course, "quiz",
                              f"unit={body.unit} topic={body.topic} "
                              f"{body.correct}/{body.total}")
    return {"ok": True, "tracking": True, "recorded": "server"}


@app.get("/api/misses/{code}")
def get_misses_api(request: Request, code: str = Depends(_code_dep), course: str = ""):
    """The student's recent missed problems (build dt) for the dashboard's review
    card: newest first, with unit names attached. Student-gated like every
    per-student read; honest {tracking:false} when the DB is off."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False, "misses": []}
    course = course if course in curriculum.COURSES else ""
    try:
        rows = store.get_misses(code, course or None, limit=30)
    except Exception as exc:  # noqa: BLE001
        print(f"[misses] read failed: {exc}")
        rows = []
    for r in rows:
        try:
            r["unit_name"] = (curriculum.unit_name(course or "algebra1", r["unit"])
                              if r.get("unit") else "")
        except Exception:  # noqa: BLE001
            r["unit_name"] = ""
    return {"ok": True, "tracking": True, "misses": rows}


def _goal_suggest(code: str) -> str:
    """(sb) For a kind='latest' goal: the child's most recently touched MASTERED
    unit name in their most-worked course -- 'a great one to practice today'.
    Falls back to the most recently touched unit at all, then to "". Never
    raises: the suggestion is a bonus."""
    try:
        act = store.get_course_activity(code)
        course = (max(act, key=lambda c: act[c].get("last_active") or "")
                  if act else "algebra1")
        rows = store.get_topics(code, course)
        best = None
        for r in rows:
            # (ue) a unit whose lesson is done is as good a practice pick as a
            # mastered one -- "taught" is what a finished authored lesson writes now
            if r.get("status") in ("mastered", "taught") and (
                    best is None or (r.get("last_touched") or "") >
                    (best.get("last_touched") or "")):
                best = r
        if best is None:
            for r in rows:
                if best is None or (r.get("last_touched") or "") > \
                        (best.get("last_touched") or ""):
                    best = r
        return str((best or {}).get("unit_name") or "")[:60]
    except Exception:  # noqa: BLE001
        return ""


@app.get("/api/goal/{code}")
def get_goal(request: Request, code: str = Depends(_code_dep)):
    """(sb) Today's practice goal, for the child's own page: {} when no goal is
    set, else {minutes, kind, target, done, suggest}. The child's page shows a
    ring, never who set it -- Mr. Cadabra owns the goal in the child's eyes
    (Jim: it must never feel adversarial)."""
    _read_guard(request, code)
    _student_or_404(code)
    g = store.get_practice_goal(code.strip())
    if not g:
        return {}
    out = {"minutes": g["minutes"], "kind": g["kind"],
           "target": g["target"], "done": g["today_done"]}
    if g["kind"] == "latest":
        out["suggest"] = _goal_suggest(code.strip())
    return out


@app.post("/api/mark/{code}")
def post_mark(body: MarkIn, code: str = Depends(_code_dep)):
    """PHASE A: count a practice problem the tutor marked right/wrong (problems practiced +
    accuracy + streak). No-op when the DB is off; never raises to the caller.

    (qz) Returns the fresh today_streak/streak_days read back from the write, so the
    client can show the AUTHORITATIVE number on its prominent streak bar rather than
    guessing from the mark it just sent -- the same reasoning /api/check already uses
    for best_pct."""
    _student_or_404(code)
    code = code.strip()
    if not store.enabled():
        return {"ok": False, "tracking": False}
    try:
        # (rc) a [[miss]] is a wrong tap on a STILL-GOING problem: the today-streak
        # falls, nothing else moves -- no finished problem, no counters, no accuracy.
        if int(body.miss or 0):
            fresh = store.reset_today_streak(code)
        else:
            fresh = store.record_practice(code, int(body.correct), int(body.attempted))
        out = {"ok": True, "tracking": True,
               "today_streak": fresh.get("today_streak", 0),
               "streak_days": fresh.get("streak_days", 0)}
        # (sb) the practice-goal ring rides the mark response, so the page can
        # move the ring on the answer that earned it -- no extra call, and a
        # reply with no goal set carries no goal key at all.
        try:
            g = store.get_practice_goal(code)
            if g:
                out["goal"] = {"target": g["target"], "done": g["today_done"]}
        except Exception:  # noqa: BLE001 -- the bonus never breaks the mark
            pass
        return out
    except Exception as exc:  # noqa: BLE001
        print(f"[mark] record_practice failed: {exc}")
        return {"ok": False, "tracking": True}


@app.get("/api/placement/{code}")
def get_placement(request: Request, code: str = Depends(_code_dep), course: str = "algebra1"):
    """Return this student's saved placement result for a course (or {})."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    _student_or_404(code)
    return read_placement(code.strip(), course)


# Bump this string whenever ANYTHING SHIPPED changes -- backend or the lesson pages. It is
# shown at /health so we can CONFIRM Render actually redeployed (if /health still shows an
# old build, the deploy did not happen -- which would explain why a prompt or whiteboard
# change is not taking effect).
# 2026-08-14: widened from "the backend" to "anything shipped", because a session.html-only
# build is exactly the kind whose deploy you most want to confirm, and the old wording
# excused leaving the stamp alone. And it is no longer a habit: ruletests PART 3ai FAILS THE
# BUILD when any shipped file carries a dated change note newer than this stamp. It went
# nine builds stale before that existed, and cost Jim part of a live debugging session --
# he could not tell a stale deploy from a real bug, which is the one question this answers.
APP_BUILD = "2026-09-10vc-one-label-for-every-clip"


@app.get("/health")
def health():
    """Simple check that the service is up (handy for Render). Includes the active
    student-facing model and DB status so you can confirm both at a glance.

    build ha (2026-08-17): DEGRADATION IS REPORTED, NOT SWALLOWED. `subsystems` says
    which defensive imports actually loaded (False = that capability silently off --
    a broken mathcheck.py used to ship an unverified tutor indistinguishable from a
    healthy one). `ops` gives the AGE in seconds of the last heartbeat / backup /
    night-watch pass (null = never recorded or DB off) -- a dead ops thread becomes
    a number you can alarm on instead of a silence. Booleans and ages only: nothing
    here leaks content or secrets."""
    subsystems = {"misconceptions": misconceptions is not None,
                  "foundations": foundations is not None,
                  "sprints": sprints is not None,
                  "nightwatch": nightwatch is not None,
                  # (mm) so a deploy that lost drillpool.py SAYS so on /health rather
                  # than looking fine until a child taps a lesson and gets nothing.
                  "drillpool": drillpool is not None}
    try:
        subsystems.update(tutor.subsystems())
    except Exception as exc:  # noqa: BLE001
        print(f"[health] tutor.subsystems failed: {exc}")
    ops = {}
    try:
        from datetime import datetime as _hdt, timezone as _htz
        for nm in ("heartbeat", "backup", "nightwatch", "offsite"):
            ts = store.last_event_at("ops_pass", nm)
            if ts is not None and ts.tzinfo is None:
                ts = ts.replace(tzinfo=_htz.utc)
            ops[nm + "_age_s"] = (int((_hdt.now(_htz.utc) - ts).total_seconds())
                                  if ts else None)
    except Exception as exc:  # noqa: BLE001
        print(f"[health] ops ages failed: {exc}")
        ops = {"heartbeat_age_s": None, "backup_age_s": None, "nightwatch_age_s": None}
    return {
        "status": "ok",
        "build": APP_BUILD,
        "students_loaded": len(STUDENTS),
        "model": tutor.active_brain()["model"],      # (qg) the seat that is teaching
        "brain": tutor.active_brain(),
        "storage": store.status(),
        "subsystems": subsystems,
        "ops": ops,
        # (ud) two booleans a deploy can be checked against: does /login print the
        # test codes (it must not on Render), and is the owner gate armed (an unset
        # admin key means the owner's tools are closed to everyone).
        "flags": {"test_codes": bool(SHOW_TEST_CODES), "owner_tools": bool(_owner_token())},
    }


class ClientErrorIn(BaseModel):
    page: str = ""
    message: str = ""
    stack: str = ""
    url: str = ""
    kind: str = ""       # (so) a NAMED client event; whitelisted below, else "clienterror"


# (so, 2026-09-04) the named client events this route will file. Anything else from the
# wild is filed as a plain clienterror, so an unknown kind can never invent a counter.
_CLIENT_EVENT_KINDS = {"voice_fallback"}


@app.post("/api/client-error")
def client_error(body: ClientErrorIn, request: Request):
    """build ha (2026-08-17): THE BROWSER STOPS BEING A BLACK BOX. The full-app review
    found ~70 empty catch blocks and zero client->server error reporting -- two
    JavaScript defects (undeclared variables killing every spoken answer on /topic and
    /practice) fired on every use, invisibly, until a human review read the source.
    static/client-log.js beacons window.onerror / unhandledrejection here.
    Deliberately unauthenticated (errors happen on the login page too), so it is
    strictly bounded instead: per-IP rate limit, hard field caps, counts-and-messages
    only, and the standard purge. Never returns an error to the page -- an error
    reporter that errors is noise."""
    try:
        _rate_limit("cerr:" + _client_ip(request), limit=10, window_seconds=300,
                    what="error reports")
    except HTTPException:
        return {"ok": True}     # silently drop the flood; never punish the page
    page = re.sub(r"[^A-Za-z0-9_./-]", "", str(body.page or ""))[:80]
    msg = " ".join(str(body.message or "").split())[:300]
    stack = " ".join(str(body.stack or "").split())[:400]
    url = str(body.url or "")[:120]
    kind = str(body.kind or "").strip().lower()
    kind = kind if kind in _CLIENT_EVENT_KINDS else "clienterror"
    print(f"[{kind}] {page or url}: {msg}")
    store.record_event(kind, page or url or "unknown",
                       msg + ((" | " + stack) if stack else ""))
    return {"ok": True}


@app.post("/api/login")
def login(req: LoginRequest, request: Request):
    """
    Validate a login code and return who the student is, PLUS the two flags the
    entry flow branches on:
      - placed:    has this student done Mr. Cadabra's Challenge yet? If not, the
                   login screen sends them there first ("find your level").
      - returning: do we have prior conversation for them? If so, the tutor
                   welcomes them back with a recap instead of a first-time tour.
    """
    # Brute-force guard: codes are short, so cap guesses per IP (20 / 5 min).
    _rate_limit("login:" + _client_ip(request), limit=20, window_seconds=300, what="login attempts")
    code = req.code.strip()

    # FORGIVING BETA-CODE ENTRY (2026-08-07 build bd, Jim: generated a pass, typed it in,
    # "not recognized"). Passes look like TRY-TIGER42; real people type "tiger42",
    # "TRY TIGER42", or "try-tiger 42". If the code as typed isn't a known pass, retry a
    # few honest normalizations (squash spaces, add the TRY- prefix, fix a missing dash)
    # and use the first that IS one. Pilot 4-digit codes and parent-student codes are
    # looked up with the code exactly as typed, same as always.
    if store.enabled():
        compact = re.sub(r"\s+", "", code).upper()
        for candidate in (code, compact,
                          "TRY-" + compact if not compact.startswith("TRY") else compact,
                          "TRY-" + compact[3:].lstrip("-") if compact.startswith("TRY") else compact):
            if candidate and store.get_beta_code(candidate):
                code = candidate
                break

    # BETA PASS sign-in (2026-07-31): consumes one of its uses and opens a timed
    # window (unless a window is already open, which rides free). The response
    # carries the pass status so the login page can say "3 of 5 sign-ins left".
    if store.enabled() and store.get_beta_code(code):
        status = store.beta_login(code)
        if not status.get("ok"):
            raise HTTPException(status_code=403, detail=_beta_404_detail(code) or
                                "This beta pass can't be used right now.")
        bcode = store.get_beta_code(code)["code"]        # normalized (uppercase)
        session = get_session(bcode)
        placement = read_placement(bcode)
        return {
            "ok": True,
            "code": bcode,
            "name": store.get_beta_code(code).get("label") or "Beta tester",
            # build hl (review F15): "returning" means returning to ANY course -- a
            # student whose only history is Geometry no longer gets the first-time
            # tour because the default-course session happened to be empty.
            "returning": bool(session.get("history")) or _has_any_history(bcode),
            "placed": bool(placement),
            "tutor_name": tutor.TUTOR_NAME,
            "beta": True,
            "beta_uses_left": status.get("uses_left"),
            "beta_window_ends": (status["window_expires_at"].isoformat()
                                  if status.get("window_expires_at") else None),
        }

    student = _student_or_404(req.code)
    session = get_session(code)
    placement = read_placement(code)
    return {
        "ok": True,
        "code": code,
        "name": student.get("name"),
        # build hl (review F15): any course counts -- see the beta branch above.
        "returning": bool(session.get("history")) or _has_any_history(code),
        "placed": bool(placement),
        "tutor_name": tutor.TUTOR_NAME,
    }


@app.get("/api/session/{code}")
def session_state(request: Request, code: str = Depends(_code_dep), course: str = "algebra1"):
    """
    Return the student's info, remembered conversation (for resume), and their
    placement -- ALL scoped to the given course. The hub/session page uses `placed`
    to enforce the flow (a never-placed student with no history is sent to the
    Challenge first) and `history` to decide between a first-time tour and a
    welcome-back recap.
    """
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    student = _student_or_404(code)
    code = code.strip()
    session = get_session(code, course)
    placement = read_placement(code, course)
    # PROGRESS PICTURE (2026-08-07): everything the lesson page's new bars + final-exam
    # button need, in the call the page already makes. Wrapped: a data hiccup never
    # blocks the lesson from loading.
    progress = {"mastered_units": [], "unit_quiz_best": {}, "topic_quizzes": {},
                "today": {}, "stats": {},
                "final": {"eligible": False, "mastered_count": 0,
                          "required": _units_required(course), "exam": {}}}
    if store.enabled():
        try:
            mastery = store.get_mastery(code, course) or {}
            # (qz) ONE call now feeds both checks and stats -- the day streak and
            # today's correct-in-a-row streak the classroom page's new bar needs,
            # without a second round trip to the database.
            checks = mastery.get("checks", {})
            progress["stats"] = mastery.get("stats", {})
            for u, c in checks.items():
                best = int((c or {}).get("best_pct") or 0)
                progress["unit_quiz_best"][int(u)] = best
                if best >= store.PASS_PCT:
                    progress["mastered_units"].append(int(u))
            progress["mastered_units"].sort()
            for q in store.get_topic_quizzes(code, course):
                progress["topic_quizzes"].setdefault(q["unit"], []).append(
                    {"idx": q["topic_idx"], "name": q["topic_name"],
                     "passed": q["best_pct"] >= store.QUIZ_PASS_PCT})
            # (rk, 2026-09-01) the scripted lessons this student has MASTERED, by
            # lesson id -- what scriptPick resumes from. Jim: "it keeps starting
            # over from the beginning"; the picker had no true record to read.
            progress["script_done"] = [
                r["lesson_id"] for r in (store.get_script_done(code, course) or [])
                if r.get("mastered")]
            # build cg: today's goal bar, so a reload/resume shows all THREE bars.
            progress["today"] = store.get_today_goals(code, course) or {}
            # build gs: THE UNIT THE LESSON IS ACTUALLY IN, for the rail. The most recently
            # touched unit is the one being taught -- and now that _track_topic files
            # activity under the tutor's own declaration rather than under placement, this
            # is a true answer instead of an echo of the placement number.
            try:
                rows = [r for r in (store.get_topics(code, course) or [])
                        if r.get("unit") and r.get("last_touched")]
                if rows:
                    rows.sort(key=lambda r: str(r.get("last_touched")), reverse=True)
                    progress["current_unit"] = int(rows[0]["unit"])
            except Exception as exc:  # noqa: BLE001 -- the rail is never worth a 500
                print(f"[session] current-unit lookup failed: {exc}")
            fstate = _final_exam_state(code, course)
            progress["final"] = {"eligible": fstate["eligible"],
                                 "mastered_count": fstate["mastered_count"],
                                 "required": fstate["required"],
                                 "exam": fstate["exam"]}
        except Exception as exc:  # noqa: BLE001
            print(f"[session] progress read failed: {exc}")
    return {
        "name": student.get("name"),
        "tutor_name": tutor.TUTOR_NAME,
        "history": session.get("history", []),
        "placement": placement,
        "placed": bool(placement),
        "progress": progress,
        # 2026-08-01: the screen tour runs ONCE PER STUDENT... 2026-08-03 refinement (Jim's
        # playtest: an already-toured demo code got NO intro in Entry-Level Math): the tour is
        # now once per student PER CLASSROOM TYPE. The elementary classroom (entry/basic,
        # tap-to-answer) is a genuinely different experience from the typing classroom, so
        # history in one group no longer suppresses the other group's first-time tour.
        # build ik (2026-08-18, Jim's live catch: tour -> placement -> return, and
        # the introduction played AGAIN): "toured" is no longer only an inference
        # from lesson history -- the tour writes none, so his exact path re-armed
        # it. The RECORDED fact (store.tour_seen, written the moment __tour_done__
        # arrives) now counts too. History still counts (pre-ik students never
        # re-tour), and a store outage degrades to the old inference, never worse.
        "toured": (_has_any_history(code, _tour_group(course))
                   or store.tour_seen(code, _tour_group_key(course))),
    }


# The two classroom types for tour purposes: elementary (tap-to-answer) vs typing.
_ELEM_COURSES = ("entry", "basic")


def _tour_group(course: str):
    """The set of courses whose history counts as 'has seen this classroom's tour'."""
    if course in _ELEM_COURSES:
        return _ELEM_COURSES
    return tuple(c for c in curriculum.COURSE_ORDER if c not in _ELEM_COURSES)


def _tour_group_key(course: str) -> str:
    """The tours_seen row key for this course's classroom type (build ik)."""
    return "elem" if course in _ELEM_COURSES else "typing"


def _has_any_history(code: str, courses=None) -> bool:
    """True if the student has lesson history (DB or JSON files). `courses` optionally
    limits the check to those course ids (see _tour_group); None = any course."""
    try:
        if store.enabled():
            return store.has_any_history(code, courses)
        allx = _read_all_sessions()
        for key, sess in allx.items():
            # build hl (review F7): this branch searched for "CODE|course" keys while
            # _ck() -- the ONE writer of these keys -- writes "CODE::course". Written
            # one way, searched another: the same fact encoded independently in two
            # places, latent only because production runs the DB, and armed the moment
            # the DB fallback fires. The parse now mirrors _ck exactly.
            if not ((key == code or key.startswith(code + "::"))
                    and (sess or {}).get("history")):
                continue
            if courses:
                # _ck keys are "CODE" (the default course) or "CODE::course".
                kcourse = key.split("::", 1)[1] if "::" in key else curriculum.DEFAULT_COURSE
                if kcourse not in courses:
                    continue
            return True
    except Exception as exc:  # noqa: BLE001 -- worst case: they see the tour again
        print(f"[tour] has_any_history failed for {code}: {exc}")
    return False


# =============================================================================
# NARRATIVE ASSESSMENT (2026-08-01) -- "How am I doing?" / the parent's honest read
# -----------------------------------------------------------------------------
# Gathers ONLY real recorded facts (units, checks, accuracy, streak, engaged
# minutes, awards, placement) and asks the tutor brain for one warm, honest
# paragraph. Cached in memory for 30 minutes per (student, course, audience) so
# repeat taps are free; rate-limited on top. The same engine will write the
# weekly parent/teacher emails when those ship.
# =============================================================================

_ASSESS_CACHE: dict = {}
_ASSESS_TTL_SECONDS = 1800


def _assessment_facts(code: str, student: dict, course: str) -> str:
    """Everything true we know about this student, as compact plain text."""
    from datetime import datetime, timezone, timedelta      # build qp: the real 14-day window
    title = curriculum.course_title(course)
    lines = [f"Student first name: {student.get('name') or 'Student'}",
             f"Course: {title}"]
    placement = read_placement(code, course)
    if placement:
        lines.append(f"Placement: tested as '{placement.get('level_title','')}' -- "
                     f"recommended start at unit {placement.get('start_unit')} "
                     f"({placement.get('start_unit_name','')})")
    else:
        lines.append("Placement: has not taken the course assessment yet")
    if store.enabled():
        m = store.get_mastery(code, course)
        checks = m.get("checks", {})
        # units_for() yields (unit_number, name) pairs; tolerate bare names too.
        unit_names = {}
        for i, u in enumerate(curriculum.units_for(course)):
            if isinstance(u, (list, tuple)) and len(u) >= 2:
                unit_names[int(u[0])] = str(u[1])
            else:
                unit_names[i + 1] = str(u)
        mastered, working, unchecked = [], [], []
        for u, name in unit_names.items():
            c = checks.get(u)
            if c and int(c.get("best_pct") or 0) >= store.PASS_PCT:
                mastered.append(f"{name} (best check {c['best_pct']}%)")
            elif c and int(c.get("checks_taken") or 0) > 0:
                working.append(f"{name} (best check so far {c['best_pct']}%, "
                               f"{c['checks_taken']} attempt(s))")
        lines.append("Units MASTERED (proved on a scored check): " +
                     ("; ".join(mastered) if mastered else "none yet"))
        lines.append("Units checked but not yet mastered: " +
                     ("; ".join(working) if working else "none"))
        st = m.get("stats", {})
        lines.append(f"Practice: {st.get('problems_practiced') or 0} problems practiced overall; "
                     f"accuracy across checks+practice: "
                     f"{str(st.get('accuracy_pct')) + '%' if st.get('accuracy_pct') is not None else 'no data yet'}; "
                     f"current day streak: {st.get('streak_days') or 0}; "
                     f"last active: {st.get('last_active') or 'no activity recorded'}")
        # ⚠️ BUILD qp -- THIS FACT WAS FALSE, AND A PARENT WAS READING IT. Jim's live page
        # said "206 real working minutes across 25 ACTIVE DAYS" for a 14-day window, which
        # cannot be true. Two separate defects, both here:
        #   (a) store.get_time() has NO DATE FILTER -- it returns the newest `days * 12`
        #       ROWS, headroom for 12 courses a day, not the last 14 days. Summing those
        #       raw rows could reach back months. (/api/time survives this because it
        #       aggregates per day and then slices [:days]; this call site did not.)
        #   (b) a row is (day, COURSE), so counting rows counted a child who worked in
        #       three courses on one afternoon as three active days.
        # The honest reader already existed: get_time_between() takes a real ISO window and
        # is what the printed records report uses. Use it, and count DISTINCT days.
        _t_to = datetime.now(timezone.utc).date()
        _t_from = _t_to - timedelta(days=13)          # inclusive window = 14 calendar days
        try:
            time_rows = store.get_time_between(code, _t_from.isoformat(), _t_to.isoformat())
        except Exception as exc:  # noqa: BLE001
            print(f"[assessment] get_time_between failed: {exc}")
            time_rows = []
        total_min = sum(r["minutes"] for r in time_rows)
        days_active = len({r["day"] for r in time_rows if r["minutes"] > 0})
        lines.append(f"Engaged time, last 14 days: {total_min} real working minutes across "
                     f"{days_active} active day(s) "
                     f"(idle time is never counted; a day counts once however many courses "
                     f"were touched)")
        earned = store.get_awards(code)
        names = [AWARD_DEFS[a][1] for a in earned if a in AWARD_DEFS]
        lines.append("Effort awards earned: " + (", ".join(names) if names else "none yet"))
        activity = store.get_course_activity(code)
        others = [curriculum.course_title(c) for c in activity if c != course]
        if others:
            lines.append("Also has activity in: " + ", ".join(others))
    else:
        lines.append("(Progress tracking is offline right now -- only basic info available.)")
    return "\n".join(lines)


@app.get("/api/assessment/{code}")
def assessment(request: Request, code: str = Depends(_code_dep), course: str = "algebra1",
               audience: str = "student"):
    """A warm, honest narrative assessment -- student voice or parent voice."""
    _read_guard(request, code)            # F1: throttle read-by-code enumeration
    student = _student_or_404(code)
    code = code.strip()
    audience = "parent" if audience == "parent" else "student"
    if course not in curriculum.COURSES:
        course = "algebra1"
    key = (code, course, audience)
    now = time.monotonic()
    hit = _ASSESS_CACHE.get(key)
    if hit and now - hit[0] < _ASSESS_TTL_SECONDS:
        return {"ok": True, "text": hit[1], "audience": audience, "cached": True}
    # Paid call: modest per-student cap on top of the cache.
    _rate_limit("assess:" + code, limit=8, window_seconds=3600, what="assessment requests")
    facts = _assessment_facts(code, student, course)
    text = tutor.get_assessment(facts, audience, code=code, course=course)
    if not text.startswith("("):                      # don't cache error placeholders
        if len(_ASSESS_CACHE) > 2000:
            _ASSESS_CACHE.clear()
        _ASSESS_CACHE[key] = (now, text)
    return {"ok": True, "text": text, "audience": audience, "cached": False}



# =============================================================================
# FIRST-USE KEY-TERM BOLDING -- deterministic (2026-08-01, from the live audit)
# -----------------------------------------------------------------------------
# The prompt asks the tutor to **bold** a term's first use, and it does so when
# formally DEFINING a term -- but the live audit showed it misses passing first
# mentions ("that's the derivative..."). Style rules deserve a guarantee, not a
# hope (same philosophy as the old board guarantee): the server wraps the first
# occurrence of a curated key term in ** ** itself, skipping [[tags]], skipping
# terms the tutor already used in an earlier turn, and never double-wrapping.
# The pages render **term** bold red; the voice never reads the asterisks.
# =============================================================================

KEY_TERMS = [
    "differential equation", "standard deviation", "line of best fit", "unit circle",
    "pythagorean theorem", "absolute value", "order of operations", "scientific notation",
    "distributive property", "greatest common factor", "least common multiple",
    "rational function", "integrating factor", "complementary", "supplementary",
    "perpendicular", "transversal", "hypotenuse", "congruent", "isosceles", "equilateral",
    "scalene", "circumference", "diameter", "bisect", "polynomial", "coefficient",
    "reciprocal", "numerator", "denominator", "inequality", "proportion", "y-intercept",
    "quadratic", "parabola", "vertex", "exponent", "logarithm", "asymptote", "amplitude",
    "radian", "sine", "cosine", "secant line", "tangent line", "derivative",
    "antiderivative", "integral", "chain rule", "product rule", "quotient rule",
    "separable", "permutation", "combination", "factorial", "probability", "median",
    "quartile", "variance", "histogram", "scatter plot", "box plot", "variable",
]
_TAG_SPLIT_RE = re.compile(r"(\[\[[^\]]*\]\])")


# ===== FOUNDATION MEMORY (2026-08-09, build ce) ==============================
# Jim: "if a student is returning, nothing tells him which scripts that student has
# heard, so a loyal student can re-hear it. We need to fix it... we should just query
# him and say, do you think you got it, or do you want me to refresh your memory?"
#
# Two halves, both here. READ: before the turn, load this student's heard terms out of
# the store and put them on the student record, where tutor.build_system_prompt picks
# them up. WRITE: after the turn, look for [[learned term="..."]] -- the invisible tag
# rule 40(f) asks him to emit whenever he actually delivers an introduction -- and
# record it. The tag parsing and the "is this a real script name?" filter both live in
# foundations.learned_terms_in(), so a mistyped tag can never retire an introduction the
# student still needs -- and ruletests.py can test that filter without booting the app.


# ===== THE TODAY BAR MUST SURVIVE A RELOAD (2026-08-09, build cg) ============
# Jim, on a resumed Pre-Algebra session: "there's only two of the three tracking bars
# across the top. I don't know where the third one is, and I don't know why it keeps
# disappearing."
#
# Why it kept disappearing: the UNIT and COURSE bars are rebuilt by the page at load
# from the server's mastery data (build br did that for the unit bar). The TODAY bar
# never had a server side at all -- it existed only as a [[today items]] tag the model
# emitted once, held in browser memory. Close the tab, resume tomorrow, refresh: gone,
# and it could only come back if the model happened to emit the tag again. The
# ensure_today_tag() net could not help either, because it deliberately stands down
# when an earlier [[today]] exists in history -- true within a session, wrong across a
# page load, where the bar it is protecting no longer exists.
# So we store what the tutor wrote. Same shape as the other two bars: the page renders
# it at load, and a later [[today]] simply replaces it.
# THE UNIT THE TUTOR IS ACTUALLY TEACHING (2026-08-17, build gs)
# -----------------------------------------------------------------------------
# Jim, twice: "it still says unit one on the top when we are talking about unit five."
# On 2026-08-16 this was diagnosed backwards -- the rail was called correct and the tutor
# accused of inventing Unit 5. Jim overruled that, and he was right: the real defect is
# that NOTHING RECONCILES THE TWO. The rail was seeded from placement.start_unit (Unit 1,
# where she was PLACED, a number that never moves), the tutor chose its own topic, and the
# two could drift apart forever. Worse, _track_topic recorded activity against the
# PLACEMENT unit too -- so the store agreed with the rail and the whole system was
# confidently wrong together, which is why nothing caught it.
# Jim's ruling (2026-08-17): THE UNIT FOLLOWS WHAT IS BEING TAUGHT. The tutor already has
# a way to say so -- [[unitplan unit="N"]] -- so that declaration becomes the authority,
# it is what gets tracked, and the rail reads it back on a resume.
# build hm: the pattern lives in tags.py (one grammar source; tutor.py's nineteenth
# referee compiles the same string).
_UNITPLAN_TAG_RE = re.compile(tags.UNITPLAN_UNIT_PATTERN, re.I)


def _declared_unit(reply: str):
    """The unit this reply says it is teaching ([[unitplan unit="N"]]), or None."""
    try:
        m = _UNITPLAN_TAG_RE.search(str(reply or ""))
        if not m:
            return None
        n = int(m.group(1))
        return n if 1 <= n <= 9 else None
    except Exception:  # noqa: BLE001
        return None


def _probe_unit_drift(code: str, course: str, reply: str, declared, tracked,
                      resolved=None, source="") -> None:
    """MEASUREMENT ONLY (build gs). Three answers to "which unit is this?" now exist: what
    the tutor DECLARED, what the content CLASSIFIES as, and what we TRACKED. Log it when
    they disagree, because Jim reported this symptom twice and both diagnoses were guesses
    about which source was lying. Never enforces, never raises -- the honest move when you
    do not yet know which signal to trust (a referee that cannot check its own fix loops)."""
    try:
        classified = None
        if curriculum is not None:
            try:
                text = re.sub(r"\[\[[^\]]*\]\]", " ", str(reply or ""))[:1200]
                classified, _name = curriculum.classify_unit(text, course)
            except Exception:  # noqa: BLE001
                classified = None
        vals = {v for v in (declared, classified, tracked) if v}
        if len(vals) > 1:
            print(f"[unitdrift] code={code[:3]}*** course={course} declared={declared} "
                  f"classified={classified} tracked={tracked} resolved={resolved}"
                  f"({source}) -- the tutor, the content and the tracker disagree "
                  f"about which unit this lesson is in")
            store.record_event("probe", "unitdrift",
                               f"declared={declared} classified={classified} "
                               f"tracked={tracked} resolved={resolved}({source})",
                               code, course)
    except Exception as exc:  # noqa: BLE001 -- a probe must never affect a lesson
        print(f"[unitdrift] probe failed (ignored): {exc}")


_TODAY_TAG_RE = re.compile(r'\[\[\s*today\b[^\]]*?items\s*=\s*"([^"]{1,400})"[^\]]*\]\]', re.I)
_TODAYDONE_TAG_RE = re.compile(r'\[\[\s*todaydone\b[^\]]*?n\s*=\s*"?(\d{1,2})"?[^\]]*\]\]', re.I)


def _record_today_bar(code: str, course: str, reply: str) -> None:
    """Persist this reply's [[today items]] / [[todaydone n]] so the bar survives."""
    try:
        if not store.enabled() or not code or not reply:
            return
        m = _TODAY_TAG_RE.search(reply)
        items = [x.strip() for x in m.group(1).split("|") if x.strip()][:8] if m else []
        done = [int(n) for n in _TODAYDONE_TAG_RE.findall(reply)]
        if items or done:
            store.save_today_goals(code, course, items=items, done=done)
    except Exception as exc:  # noqa: BLE001 -- a bar is never worth failing a turn over
        print(f"[today] recording failed: {exc}")


# =============================================================================
# THE TODAY BAR MAKES REAL CALLS (2026-08-18, build il -- Jim's design ruling).
# -----------------------------------------------------------------------------
# Jim, after a session where he finished a QUIZ and a whole UNIT while the Today
# bar sat empty: "today needs to be a combination of how much time did they spend
# working and how much progress did they make... a struggling hour is a good
# day's work; a two-minute completion is not... the app needs to make some type
# of call." The bar's ADVANCE used to be pure model judgment ([[todaydone]] --
# wish-tier, sitting beside unit progress that build hu promoted to machinery).
# Now the SERVER makes both calls Jim named, from facts it already holds:
#   COMPLETION -- when build hu's writer records a quiz/check result, the result's
#     name is matched against the plan's unfinished items (word overlap, stopwords
#     out); a clear match ticks that item as COMPLETED.
#   HONEST WORK-TIME -- the engaged-minutes clock (time_daily; idle never counts)
#     earns a WORKED tick: every ~15 engaged minutes today entitles the day to one
#     more tick, applied to the first unfinished item. A struggling hour fills the
#     bar; a two-minute whiz-through lights one segment and leaves the rest.
# Ticks reach the page deterministically: _ensure_today_ticks appends a
# [[todaydone n kind]] tag for any server-marked tick the page hasn't seen (the
# same net pattern as ensure_today_tag). The model's own [[todaydone]] stays
# welcome -- the server merely guarantees the bar can never sit frozen through a
# day of real work again. Completed outranks worked; nothing ever un-ticks.
# =============================================================================
_TODAY_TICK_MINUTES = 15          # one earned tick per this many engaged minutes
_TODAY_MATCH_STOP = {"the", "a", "an", "and", "or", "of", "to", "our", "your", "with",
                     "on", "in", "for", "one", "two", "three", "quiz", "check", "try",
                     "own", "problems", "problem", "practice", "finish", "start",
                     "more", "new", "next", "first", "second", "unit", "topic"}


def _today_words(text: str) -> set:
    return {w for w in re.findall(r"[a-z]{3,}", str(text or "").lower())
            if w not in _TODAY_MATCH_STOP}


def _today_match_tick(code: str, course: str, name: str) -> None:
    """A result named `name` was just RECORDED -- if it clearly matches one
    unfinished today item, tick that item as COMPLETED. Never raises."""
    try:
        if not store.enabled() or not code or not name:
            return
        goals = store.get_today_goals(code, course)
        items = goals.get("items") or []
        if not items:
            return
        completed = set(goals.get("done") or []) - set(goals.get("worked") or [])
        rwords = _today_words(name)
        if not rwords:
            return
        best, best_overlap = 0, 0
        for i, item in enumerate(items, start=1):
            if i in completed:
                continue
            overlap = len(rwords & _today_words(item))
            if overlap > best_overlap:
                best, best_overlap = i, overlap
        if best and best_overlap >= 1:
            store.save_today_goals(code, course, done=[best])
    except Exception as exc:  # noqa: BLE001 -- a bar is never worth failing a turn
        print(f"[today] match-tick failed: {exc}")


def _today_time_tick(code: str, course: str) -> None:
    """Every ~{_TODAY_TICK_MINUTES} engaged minutes today earns the day one more
    tick (kind WORKED) on the first unfinished item -- Jim's struggling-hour
    principle. Called from the minute beat. Never raises."""
    try:
        if not store.enabled() or not code:
            return
        goals = store.get_today_goals(code, course)
        items = goals.get("items") or []
        done = set(goals.get("done") or [])
        if not items or len(done) >= len(items):
            return
        today = store._today()
        minutes = sum(r["minutes"] for r in store.get_time(code, days=2)
                      if r["day"] == today and r["course"] == course)
        if minutes >= _TODAY_TICK_MINUTES * (len(done) + 1):
            nxt = next((i for i in range(1, len(items) + 1) if i not in done), 0)
            if nxt:
                store.save_today_goals(code, course, worked=[nxt])
    except Exception as exc:  # noqa: BLE001
        print(f"[today] time-tick failed: {exc}")


def _ensure_today_ticks(code: str, course: str, history, reply: str) -> str:
    """Append a [[todaydone]] tag for every server-marked tick the page has not
    been shown yet -- the deterministic net that keeps the bar honest across the
    whole conversation. Never raises; on any doubt the reply passes untouched."""
    try:
        if not store.enabled() or not code or not reply:
            return reply
        goals = store.get_today_goals(code, course)
        done = goals.get("done") or []
        if not done:
            return reply
        seen_text = " ".join(str(m.get("content", "")) for m in (history or [])
                             if m.get("role") == "assistant") + " " + reply
        shown = {int(n) for n in _TODAYDONE_TAG_RE.findall(seen_text)}
        worked = set(goals.get("worked") or [])
        extra = ""
        for n in done:
            if n not in shown:
                kind = "worked" if n in worked else "completed"
                extra += ' [[todaydone n="%d" kind="%s"]]' % (n, kind)
        return (reply.rstrip() + extra) if extra else reply
    except Exception as exc:  # noqa: BLE001
        print(f"[today] tick net failed: {exc}")
        return reply


def _foundations_heard(code: str, course: str) -> list:
    """The canonical terms this student has already been introduced to in this course."""
    try:
        if not store.enabled() or not code:
            return []
        return sorted(store.get_foundations_heard(code, course).keys())
    except Exception as exc:  # noqa: BLE001 -- never break a turn over a memory lookup
        print(f"[foundations] heard-list lookup failed: {exc}")
        return []


def _record_learned(code: str, course: str, reply: str) -> None:
    """Persist every [[learned term="..."]] the tutor emitted in this reply."""
    try:
        if foundations is None or not store.enabled() or not code or not reply:
            return
        for term in foundations.learned_terms_in(course, reply):
            store.record_foundation_heard(code, course, term)
    except Exception as exc:  # noqa: BLE001
        print(f"[foundations] recording failed: {exc}")


def _record_term_gap(code: str, course: str, message: str, history) -> None:
    """build gi (2026-08-14): when a student has to ask what a word MEANS and the tutor
    had just used it, that question is the most honest evidence we get that an
    introduction was missing. Log it and nothing else -- no reply is changed, no model
    call is made, and the student's own words are never written down: only the term,
    the course, and which kind of gap it is.

      [termgap] unintroduced -- we HAVE a script for this and the tutor used the word
                without delivering it. A rule 36/40 violation, not new information.
      [termgap] NO SCRIPT    -- nobody has written one. New teaching content: it needs
                words and a voice clip, so a human decides, not a machine.

    Jim's ask, after having to interrupt a Geometry lesson to find out that a right
    angle is ninety degrees: "it should have said, I got a question about something I
    was teaching that told me I wasn't being clear, and I'm gonna use that in future."
    """
    try:
        if foundations is None or not message:
            return
        last_tutor = ""
        for m in reversed(list(history or [])):
            if m.get("role") == "assistant":
                last_tutor = str(m.get("content", ""))
                break
        if not last_tutor:
            return
        heard = _foundations_heard(code, course) if code else []
        term, kind = foundations.term_gap(course, message, last_tutor, heard)
        if not term:
            return
        if kind == "no-script":
            print(f"[termgap] NO SCRIPT [{course}] \"{term}\" -- a student had to ask what "
                  f"it means and nothing in foundations.py defines it")
        else:
            print(f"[termgap] unintroduced [{course}] \"{term}\" -- we have a script for "
                  f"this and the tutor used the word without delivering it (rule 36)")
        store.record_event("probe", "termgap", f"{kind}: {term}", code, course)
    except Exception as exc:  # noqa: BLE001 -- a probe must never affect a lesson
        print(f"[termgap] probe failed (ignored): {exc}")


def _bold_first_terms(reply: str, history) -> str:
    """Wrap the FIRST use of each key term in **bold** (rendered red by the app).
    Skips [[tags]], terms already used in an earlier tutor turn, and anything the
    model already bolded. Wrapped so a failure can never break a lesson."""
    try:
        if not reply:
            return reply
        # Tag text ([[card ...]] etc.) is NOT spoken prose -- a term that has only
        # ever appeared inside a tag hasn't been "introduced" yet, and terms inside
        # tags are never wrapped. Strip tags before both checks.
        _strip = lambda t: _TAG_SPLIT_RE.sub(" ", str(t))
        prior = " ".join(_strip(m.get("content", "")) for m in (history or [])
                         if m.get("role") == "assistant").lower()
        parts = _TAG_SPLIT_RE.split(reply)
        low = _strip(reply).lower()
        for term in sorted(KEY_TERMS, key=len, reverse=True):
            tl = term.lower()
            if tl not in low or tl in prior or ("**" + tl) in low:
                continue
            pat = re.compile(r"(?<![*\w])(" + re.escape(term) + r"s?)(?![\w*])", re.IGNORECASE)
            for i, seg in enumerate(parts):
                if seg.startswith("[["):
                    continue
                mt = pat.search(seg)
                if mt:
                    parts[i] = seg[:mt.start()] + "**" + mt.group(1) + "**" + seg[mt.end():]
                    break
        return "".join(parts)
    except Exception as exc:  # noqa: BLE001 -- styling must never break a turn
        print(f"[terms] bolding skipped: {exc}")
        return reply


def _record_unintroduced(code: str, course: str, reply: str, history) -> None:
    """build gj (2026-08-14): rule 37 says a mathematical word is DEFINED the moment it is
    first said, never assumed. The 2026-08-16 audits caught the tutor saying "you kept the
    denominator the same" to a confused nine-year-old -- and `denominator` is not a word we
    hoped it would explain, it is a WRITTEN CANONICAL SCRIPT in Basic Math, with a voice
    clip already paid for. The child got the word and not the meaning. It is the same
    defect Jim hit himself in Geometry, where "right angle" was used without ever saying
    ninety degrees.

    This LOGS and does nothing else, and the reason is worth stating rather than assuming.
    The observable half of rule 37 -- marking the term **like this** -- is already patched
    up by _bold_first_terms below, so a referee demanding it would be arguing with a helper
    that has already fixed it. The half that actually matters -- whether the term was
    DEFINED -- cannot be verified mechanically, and a referee that cannot check its own fix
    is a referee that loops. So this measures instead, and the rate decides what to do:
    sharpen rule 37, or deliver the canonical script automatically. Both cost something.

    Precision comes from reusing the two lists that already exist: KEY_TERMS is 63 curated
    technical words with no ordinary-English collisions in it (no "point", no "mean", no
    "area"), and `foundations` knows which of them have a script for THIS course.
    """
    try:
        if foundations is None or not reply:
            return
        _strip = lambda t: _TAG_SPLIT_RE.sub(" ", str(t))
        prior = " ".join(_strip(m.get("content", "")) for m in (history or [])
                         if m.get("role") == "assistant").lower()
        low = _strip(reply).lower()
        heard = {t.lower() for t in (_foundations_heard(code, course) if code else [])}
        for term in KEY_TERMS:
            tl = term.lower()
            if tl not in low or tl in prior:
                continue                      # not said here, or already said earlier today
            canon = foundations.known_term(course, term)
            if not canon or canon.lower() in heard:
                continue                      # no script to owe, or they have already had it
            script = ""
            for f in foundations.for_course(course):
                if f["term"] == canon:
                    script = f["say"]; break
            if script and script[:60] in reply:
                continue                      # he DID deliver the canonical introduction
            print(f"[rule37] [{course}] \"{canon}\" was said for the first time with no "
                  f"canonical introduction -- we have a written script and a voice clip "
                  f"for it, and this student did not get them")
            store.record_event("probe", "rule37", canon, course=course)
    except Exception as exc:  # noqa: BLE001 -- a probe must never affect a lesson
        print(f"[rule37] probe failed (ignored): {exc}")


# =============================================================================
# THE STARTING BLOCKS (build og, 2026-08-26) -- Jim's design, his words: "we got
# a fifty-fifty chance of getting this right. Why don't we just put the right
# answer response in the starting blocks? If he gets it right, it's ready to go.
# If he gets it wrong, we don't have anything in the starting blocks, so we
# gotta wait the five seconds and we'll pay for that one as well."
# HOW IT WORKS: when a shipped reply ends in a COMPUTABLE pending line ("3 + 8
# = ?"), a background thread generates the follow-up for the RIGHT answer
# through the FULL verified pipeline (referees, retries, critic -- all off the
# clock) and stashes it. If the student's next message IS that answer, the
# stashed reply ships instantly and the recording path runs exactly as live; on
# ANY mismatch the stash is discarded and the live path runs untouched.
# WHY RIGHT-ANSWER-ONLY (Jim's ruling, latency report Lever 4): the hit rate
# beats 50/50 (rule 47's no-cold-quizzes bar), and the WRONG branch cannot be
# pre-built honestly -- rule 49 says the response to a miss depends on WHICH
# wrong answer arrived. V1 SCOPE, deliberately narrow: numeric pending lines
# only; quiz/check/exam turns never speculate (their grading writes mastery);
# turns that recorded result tags never speculate (the context snapshot would
# be stale). Costs: a hit costs nothing extra (the speculative call replaces
# the live one); a miss discards one call (~+25%% brain tokens on practice
# turns at a 75%% hit rate). Probes spec_armed / spec_hit / spec_miss make the
# real hit rate visible on /admin's telemetry panel.
# =============================================================================
_SPEC_STASH: dict = {}
_SPEC_LOCK = threading.Lock()
_SPEC_TTL_S = 600
_SPEC_WORDNUM = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
                 "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                 "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
                 "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
                 "eighteen": 18, "nineteen": 19, "twenty": 20}
# ⚠️ character ORDER is load-bearing: star-then-slash (or slash-then-star)
# ANYWHERE in this file pairs with the stray slash-star sequences that live in
# old comments ("shots" globs, the api wildcard paths) and makes the battery's
# comment-stripper swallow 400KB of code between them -- it did exactly that in
# this build's own dry run, and two pinned tts call sites vanished. In every
# regex and string here, star and slash never touch.
_SPEC_EXPR_OK = re.compile(r"^[\d\s.+*\-/()]+$")


def _spec_expected_answer(reply: str):
    """The numeric answer to the reply's LAST computable pending line, or None.
    "hundredths: 0 + 5 = ?" -> 5.  Anything with letters left after symbol
    normalization is not V1's business."""
    try:
        vals = [v for v in tutor._note_tag_vals(str(reply or "")) if "= ?" in v or "=?" in v]
        if not vals:
            return None
        line = vals[-1]
        line = line.split(":", 1)[-1]                    # drop a label prefix
        lhs = line.rsplit("=", 1)[0]
        lhs = (lhs.replace("×", "*").replace("·", "*").replace("÷", "/")
                  .replace("−", "-").replace("–", "-"))
        lhs = lhs.strip()
        if not lhs or not _SPEC_EXPR_OK.match(lhs):
            return None
        val = eval(lhs, {"__builtins__": {}})            # noqa: S307 -- whitelisted charset
        if not isinstance(val, (int, float)) or abs(val) > 1e9:
            return None
        return float(val)
    except Exception:
        return None


def _spec_norm_hit(message: str, expected: float) -> bool:
    """Does this short answer SAY the expected number, and nothing else?"""
    try:
        s = str(message or "").strip().lower()
        if not s or len(s) > 24:
            return False
        for w, n in _SPEC_WORDNUM.items():
            s = re.sub(r"\b" + w + r"\b", str(n), s)
        nums = re.findall(r"-?\d+(?:\.\d+)?", s)
        if len(nums) != 1:
            return False
        leftover = re.sub(r"-?\d+(?:\.\d+)?", "", s)
        if re.search(r"[0-9]", leftover):
            return False
        return abs(float(nums[0]) - expected) < 1e-9
    except Exception:
        return False


def _spec_turn_note(course: str, message: str, code: str) -> str:
    """The SAME per-turn note the live path would build for this message."""
    note = ""
    try:
        if misconceptions is not None and message and not message.startswith("__"):
            note = misconceptions.hint_note(course, message)
    except Exception:
        note = ""
    try:
        note += tutor.phrasing_note(code, course)
    except Exception:
        pass
    return note


def _speculate_next(code: str, course: str, context: dict, history2: list,
                    expected: float) -> None:
    """Generate + stash the right-answer follow-up. Runs in a daemon thread; any
    failure just means no stash (the live path is always intact)."""
    try:
        msg = str(int(expected)) if float(expected).is_integer() else f"{expected:g}"
        note = _spec_turn_note(course, msg, code)
        reply = _bold_first_terms(
            tutor.get_tutor_reply(context, history2, msg, course, code=code,
                                  turn_note=note), history2)
        if not reply:
            return
        with _SPEC_LOCK:
            _SPEC_STASH[(code, course)] = {
                "hist_len": len(history2), "expected": float(expected),
                "reply": reply, "ts": time.time()}
        _event_safe("probe", "spec_armed", f"expected={msg}", code, course)
    except Exception as exc:  # noqa: BLE001 -- speculation must never break anything
        print(f"[spec] speculation failed (ignored): {exc}")


def _spec_take(code: str, course: str, history: list, message: str):
    """The stashed reply if THIS message is the speculated right answer in the
    same conversation state, else None. Single-use either way."""
    with _SPEC_LOCK:
        st = _SPEC_STASH.pop((code, course), None)
    if not st:
        return None
    if time.time() - st["ts"] > _SPEC_TTL_S or len(history) != st["hist_len"]:
        return None
    if _spec_norm_hit(message, st["expected"]):
        _event_safe("probe", "spec_hit", f"answer={message[:20]}", code, course)
        return st["reply"]
    _event_safe("probe", "spec_miss", f"answer={message[:20]}", code, course)
    return None


def _event_safe(kind: str, name: str, detail: str, code: str = "", course: str = "") -> None:
    try:
        store.record_event(kind, name, detail, code, course)
    except Exception:
        pass


@app.post("/api/chat")
def chat(req: ChatRequest):
    """Send the student's message to the tutor and return the tutor's reply."""
    _deg = _degraded_reply()          # build hv: no teaching into a stranded file fork
    if _deg:
        return _deg
    student = _student_or_404(req.code)
    code = req.code.strip()
    # Paid Anthropic call behind this -- cap the pace per code (40 turns / 5 min is
    # far above a real student's speed; it only stops abuse/runaway scripts).
    _rate_limit("brain:" + code, limit=40, window_seconds=300, what="messages")

    message = (req.message or "").strip()
    if not message:
        raise HTTPException(status_code=400, detail="Please type a message first.")

    # FREE PLAN GATE (2026-07-31): a free student who has mastered their first unit
    # gets a warm upgrade note instead of a lesson -- checked BEFORE the paid call.
    gate = _free_gate(code, student, req.course)
    if gate:
        return {"reply": gate, "upgrade_required": True}

    # FINAL EXAM MODES (2026-08-07): "prep" or "exam" -- HARD SERVER GATE, re-checked on
    # EVERY turn. An ineligible request gets the gate message with no paid model call;
    # the page's button state is only a courtesy, never the enforcement.
    final_mode = (req.final or "").strip().lower()
    if final_mode not in ("prep", "exam"):
        final_mode = ""
    if final_mode:
        fstate = _final_exam_state(code, req.course)
        if not fstate["eligible"]:
            return {"reply": _final_gate_message(code, req.course, fstate),
                    "final_locked": True}

    session = get_session(code, req.course)
    history = session.get("history", [])

    # (rc, 2026-08-31) THE STAR FALLS WHEN THE CHILD SLIPS -- code's own grade, the
    # floor under the prompt's [[miss]] tag (a model tag is a nudge, never a
    # guarantee -- the qw lesson). The server holds this conversation, so when the
    # previous tutor turn left a question whose answer code can COMPUTE (the qw/ra
    # parsers, one grammar) and the child's message is a BARE answer that disagrees,
    # the today-streak resets right here, whether or not the model remembers to say
    # [[miss]]. Cautious on purpose: anything uncertain is not a slip (see
    # tutor.answer_slip), because a wrongly fallen star is worse than a late one.
    # A reset is idempotent, so code and the model both reporting one slip is free.
    try:
        if store.enabled():
            _prev = next((m.get("content", "") for m in reversed(history)
                          if isinstance(m, dict) and m.get("role") == "assistant"), "")
            if _prev and tutor.answer_slip(_prev, message):
                store.reset_today_streak(code)
                print("[slip] a computable ask answered wrong -- today-streak reset")
    except Exception as exc:  # noqa: BLE001 -- the guard must never cost a turn
        print(f"[slip] guard failed open: {exc}")

    # Give the tutor the student's remembered progress plus the live history.
    student_context = dict(student)
    if final_mode:
        student_context["final_mode"] = final_mode   # tutor.py appends the matching note
    placement = read_placement(code, req.course)

    # Phase B -- MASTERY STEERING: tell the tutor what they've mastered vs. still need, and
    # (from the dashboard "Work on it" link) which unit to focus on today.
    focus_unit = 0
    try:
        focus_unit = int(getattr(req, "unit", 0) or 0)
    except (TypeError, ValueError):
        focus_unit = 0
    # 2026-08-11 (build ea): the PARENT'S STANDING PLAN. When the student opens this
    # course with no focus of their own, the steer set on /family supplies one. An
    # explicit dashboard link always wins -- the student's own intent outranks the plan.
    focus_unit, steered = _resolve_focus(code, req.course, focus_unit)
    mnote = _mastery_note(code, focus_unit, req.course, steered=steered)
    if mnote:
        student_context["mastery_note"] = mnote
    if 1 <= focus_unit <= 9:
        student_context["focus_unit"] = focus_unit

    # build hj: ONE OWNER FOR THE UNIT. Resolved once, consumed everywhere as a FIELD
    # -- the prompt's playbook and foundation filter, the fourteenth referee, and the
    # tracker all read this instead of re-deriving their own answers (the unit-rail
    # class: five sources, confidently wrong together).
    resolved_unit, unit_source = _resolve_unit(code, req.course, placement, focus_unit)
    student_context["current_unit"] = resolved_unit
    # build hm (Phase 4, Class D): the units this turn's [[unitplan]] could honestly
    # declare -- computed from the SAME store facts the prompt was built on, handed to
    # the nineteenth referee (tutor.unitplan_conflict) via meta, and re-checked at
    # filing time by _accept_declared_unit below. The model's word about "which unit"
    # is now vetoed by the server that holds the record, exactly as [[verify]]/SymPy
    # vetoes its arithmetic.
    student_context["allowed_units"] = _unit_allowed_set(
        code, req.course, resolved_unit, focus_unit, message)
    # build ho (Phase 4, Class D): the compact past-facts record for the twentieth
    # referee -- claims about scores, mastery and units-in-progress are judged by
    # the record that actually holds the past. None (DB off) = referee silent.
    student_context["claim_record"] = _claim_record(code, req.course)
    # build ig: the delivered-scripts list for the twenty-ninth referee (the quiz
    # vocabulary gate) -- durable across sessions and history caps, unlike the
    # conversation text. The referee needs BOTH this and `heard` to speak.
    student_context["terms_known"] = _foundations_heard(code, req.course)
    # THE PLACEMENT NOTE EXPIRES (review F4a). It used to be appended to the progress
    # prose every turn forever -- and tutor.py regex-read "Unit N" back OUT of that
    # prose to pick the teaching playbook, so a student eight units past their
    # placement could get Unit 1's playbook with the referee calibrated to the same
    # stale number. The note now rides only while placement is genuinely the best
    # answer (a brand-new student); after that, current_unit carries the truth as
    # data and the sentence is retired.
    if placement and unit_source in ("placement", "default"):
        note = (" [Placement result from the Challenge: this student tested as "
                f"'{placement.get('level_title', '')}' and should start around "
                f"Unit {placement.get('start_unit')} "
                f"({placement.get('start_unit_name', '')}). Strengths: "
                f"{', '.join(placement.get('strengths', [])) or 'building foundations'}. "
                "Meet them at that level -- don't start below it unless they struggle. "
                # build nw (2026-08-26), Jim's ruling after being handed "fact
                # families" cold in a unit his placement skipped: "it might be
                # worthwhile to first spend a few minutes reviewing... so people
                # aren't caught off guard." Rule 40(h) holds the durable law; this
                # rides only while the placement note does (the placed-student's
                # first sessions), which is exactly when the tour belongs.
                "⚠️ PLACEMENT VALIDATES SKILLS, NOT VOCABULARY (rule 40h): they "
                "have never heard this classroom's NAMES for the earlier units' "
                "ideas. Open their first session with a two-minute friendly tour "
                "of the key words from the units they skipped ('you clearly know "
                "this stuff -- let me show you what we call things around here'), "
                "and forever after introduce any skipped-unit term as brand new "
                "the first time you use it.]")
        student_context["progress"] = (str(student_context.get("progress", "")) + note).strip()

    # REWARDS AWARENESS (2026-07-30): if the student earned an award in the last 48h, tell the
    # tutor so he can congratulate them ONCE, by name, for what they DID. Wrapped: never breaks a turn.
    try:
        if store.enabled():
            from datetime import datetime, timezone, timedelta
            cut = datetime.now(timezone.utc) - timedelta(hours=48)
            fresh = []
            for aid, when in store.get_awards(code).items():
                if aid not in AWARD_DEFS or not when:
                    continue
                dt = datetime.fromisoformat(when)
                if dt.tzinfo is None:            # SQLite returns naive datetimes; treat as UTC
                    dt = dt.replace(tzinfo=timezone.utc)
                if dt >= cut:
                    _i, nm, ds, _f, _t = AWARD_DEFS[aid]
                    fresh.append(f"{nm} ({ds})")
            if fresh:
                student_context["mastery_note"] = (str(student_context.get("mastery_note", "")) +
                    "\n[AWARDS: this student JUST earned: " + "; ".join(fresh[:3]) +
                    ". If it fits naturally, congratulate them briefly ONCE for the effort it took "
                    "-- then keep teaching. Don't repeat the congratulations every turn.]")
    except Exception as exc:  # noqa: BLE001
        print(f"[awards] tutor note failed: {exc}")

    # LIKELY MISCONCEPTION (2026-08-10, build ck). Rules 20-22 say what to DO about a
    # wrong answer; rule 49 says to work out WHICH RULE produced it first. This is the
    # part the model cannot do from the prompt alone at speed: match what the student
    # just said against the 148 catalogued error patterns for this course and, on a hit,
    # hand him the diagnosis AND the remedy in the same breath.
    # Framed as a possibility he may discard, always. The matcher is conservative --
    # bare numbers were stripped from the evidence at build time, matches are on word
    # boundaries, and at most two theories come back -- but it is still a guess about a
    # child's thinking, and a confident wrong diagnosis is worse than none (rule 49d/e).
    # build cm: this note travels with the TURN, not in the system prompt. Appending it
    # to the prompt (as build ck did) moved the cache prefix and re-billed ~16k tokens
    # on exactly the turns the hint fired. It is per-turn information; it belongs next
    # to the message it is about.
    turn_note = ""
    try:
        if misconceptions is not None and message and not message.startswith("__"):
            turn_note = misconceptions.hint_note(req.course, message)
    except Exception as exc:  # noqa: BLE001 -- a hint is never worth failing a turn over
        print(f"[misconceptions] hint failed: {exc}")
        turn_note = ""
    # build jr: CONSISTENCY MEMORY. The words this student was first taught for a rule,
    # so the same idea never arrives in two costumes ("over nine" one turn, "ten or
    # more" four turns later -- Jim's live catch, 2026-08-20). Rides the TURN for
    # exactly the reason build cm gives above: the cached system prefix must not move.
    # Empty for a student who has been taught nothing yet, so a first lesson pays zero.
    # (ox) HOW LONG THIS SESSION ACTUALLY IS. Jim's Entry flag: "Don't ask me every
    # 2 minutes if I want to stop." Rule 29(b) offers the keep-going/stop fork at
    # "roughly twenty-five or thirty minutes of back-and-forth" -- and the model has
    # NO CLOCK. It was guessing from the feel of the transcript, writing "you've been
    # working hard for a while now" after three exchanges, and build nz's scoping of
    # 29(c) could not help because this is 29(b), the LENGTH branch. So the server
    # states the fact, the way it already states the gap and the phrasing memory:
    # a count the model cannot misjudge, with the ruling attached. Cheap (one short
    # line), rides the TURN so the cached prefix never moves.
    try:
        _turns = sum(1 for h in history
                     if isinstance(h, dict) and h.get("role") == "user"
                     and not str(h.get("content", "")).startswith("__"))
        if _turns < 25:
            turn_note += ("\n(SESSION LENGTH: this session is " + str(_turns)
                          + " student turns old. Rule 29(b)'s long-session mark is "
                          "about 25-30 minutes of back-and-forth, which you have NOT "
                          "reached. Do NOT offer to stop, take a break, or call this "
                          "a good stopping point. Ask 'ready for another?' instead. "
                          "The ONLY exceptions are the student saying they must go, "
                          "or a real boundary under rule 29(c).)")
    except Exception as _sexc:  # noqa: BLE001 -- a note must never cost a lesson
        print(f"[session] length note failed (ignored): {_sexc}")
    try:
        turn_note += tutor.phrasing_note(code, req.course)
    except Exception as _pexc:  # noqa: BLE001 -- a memory must never cost a lesson
        print(f"[phrasing] note skipped (non-fatal): {_pexc}")

    # (rj, 2026-09-01) THE ANNOUNCED SEAM. A mastered scripted lesson hands the class
    # here via "__script_done__" (or "__script_done_mastered__"), and Jim watched the
    # unannounced result: "it stopped after 3 in a row then thought for a bit and
    # then acted as if we had been working on subtraction. This is strange." His
    # ruling (asked): ANNOUNCE IT, THEN CONTINUE. The page already spoke the fixed
    # bridge line (lessonscripts.LINE_NEW_TOPIC, pre-rendered); this note makes the
    # live tutor's first sentence NAME what changed. Fail-open on a missing note.
    if message.startswith("__script_done"):
        try:
            _sd = _SCRIPT_DONE_NOTES.pop(code, None) or {}
            _sd_topic = str(_sd.get("topic", "")).replace('"', "'")
            _sd_mastered = bool(_sd.get("mastered")) or message == "__script_done_mastered__"
            turn_note += (
                "\n(SYSTEM: The SCRIPTED lesson"
                + (f' on "{_sd_topic}"' if _sd_topic else "")
                + (" was just MASTERED — three right answers in a row"
                   if _sd_mastered else " just ended (saved as still learning)")
                + ". The app already told the student something new is coming and to "
                "watch the board. Your FIRST sentence must NAME the new topic in plain "
                "words, and your first board tag must put that name up — never slide "
                "into new material as if it were the old topic. Then teach it from the "
                "beginning: introduce the idea before asking anything. Do NOT re-greet "
                "and do NOT re-teach the lesson that just finished.)")
        except Exception as _sdexc:  # noqa: BLE001 -- a note must never cost a lesson
            print(f"[script] seam turn note failed (ignored): {_sdexc}")

    # FOUNDATION MEMORY (2026-08-09, build ce): which canonical introductions this
    # student has already sat through, so rule 40 can ASK instead of replaying one.
    # This is the ONLY place the tutor can learn it -- a new session's history is empty.
    student_context["foundations_heard"] = _foundations_heard(code, req.course)
    # THE PROMPT IS DELIBERATELY STABLE (2026-08-10, build cn -- reversing build cl).
    # Build cl deferred the wording of already-heard scripts to save ~6,500 characters on
    # an ordinary turn. Then we did the cache arithmetic, and it was the wrong trade:
    #   deferring saves    ~$0.0005 on each ordinary turn
    #   but every flip between the two prompt shapes rebuilds the cached prefix, and
    #   there are two flips per refresher, at ~$0.24
    #   -> it only pays if a student goes 460 turns between refreshers, and rule 40 has
    #      him OFFER one every time a known term comes up.
    # It was also a slower turn each time, which is the thing Jim asked for least of all.
    # So the wording is always carried and the system prompt is byte-identical for the
    # whole of a student's session. A STABLE prompt beats a smaller one: the cache is
    # what makes size cheap, and at ~34k tokens we are using 17% of the context window.
    # The mechanism is left in place (foundations.prompt_block(..., verbatim=False) and
    # wants_refresher) because it becomes the right answer if the library ever grows to
    # where it does not fit, or if the cache lifetime changes. It is dormant, not gone.
    student_context["foundations_verbatim"] = True
    # build gz (2026-08-17): THE DORMANT MECHANISM'S DAY CAME. tutor.py now enforces
    # PROMPT_CEILING at assembly time, and for the student whose heard scripts push the
    # prompt over it (all-heard students overflow on every course -- measured), the heard
    # WORDING is deferred: exactly the cl mechanism the note above kept "dormant, not
    # gone". Rule 40's contract is that the exact words come back the moment the student
    # asks -- so this turn-level flag tells tutor.py "carry the words no matter what",
    # set when the student asks for a refresher outright or accepts the offer the tutor
    # just made. foundations.wants_refresher fails OPEN (True): when unsure, carry the
    # words. Students under the ceiling see a byte-identical prompt -- cn's cache
    # arithmetic still wins for them and nothing changes.
    try:
        _last_tutor_text = next((str((m or {}).get("content") or "")
                                 for m in reversed(history)
                                 if (m or {}).get("role") == "assistant"), "")
        student_context["foundations_force_verbatim"] = bool(
            foundations is not None
            and foundations.wants_refresher(message, _last_tutor_text))
    except Exception as exc:  # noqa: BLE001 -- never fail a turn over this
        print(f"[foundations] wants_refresher failed ({exc}) -- carrying the words")
        student_context["foundations_force_verbatim"] = True
    # build cg: does the TODAY bar genuinely exist right now? The net in tutor.py used to
    # infer that from history, which is wrong the moment the page reloads.
    try:
        student_context["today_live"] = bool(store.enabled()
                                             and store.get_today_goals(code, req.course))
    except Exception as exc:  # noqa: BLE001
        print(f"[today] live-check failed: {exc}")
        student_context["today_live"] = False

    # OPENER: the app auto-sends "__open__" when the student opens the lesson (they did NOT
    # type anything). The OLD app sent a literal "Hi!" that got stored as a student turn, so
    # after a few logins the tutor saw "Hi Hi Hi..." and turned snappish. Fix: never store a
    # fake student greeting, strip any leftover junk ones, generate a warm recap, and save
    # ONLY the tutor's reply so the conversation stays coherent.
    if message in ("__open__", "__tour_done__", "__open_declined__", "__tour_done_declined__",
                   "__open_fresh__", "__unit_quiz__"):
        after_tour = message.startswith("__tour_done")
        # build ik: the tour just ended (watched OR skipped -- both arrive as
        # __tour_done...) -- write the fact down BEFORE any model call, so a failed
        # or slow opener can never cost the student a second sit-through.
        if after_tour:
            try:
                store.record_tour_seen(code, _tour_group_key(req.course))
            except Exception as exc:  # noqa: BLE001 -- never fail a turn over this
                print(f"[tour] record failed (ignored): {exc}")
        # 2026-08-07 (build at): "_declined" = the student JUST answered the on-screen
        # assessment-invitation card with "Not right now" -- the tutor must respect it.
        assess_declined = message.endswith("_declined__")
        # 2026-08-07 (build au): "__open_fresh__" = the welcome overlay's "take me to my
        # course path" choice. The student does NOT want to resume the recent side-trip
        # (an explored topic / practice problem); they want their next unmastered unit,
        # which the page sent as the focus unit.
        fresh_start = (message == "__open_fresh__")
        # 2026-08-11 (build du): "__unit_quiz__" = the dashboard's "Retake the Unit
        # Quiz" button. The student came for exactly one thing; deliver exactly that.
        quiz_intent = (message == "__unit_quiz__")
        junk = ("hi", "hi!", "hi.", "hello", "hey", "__open__", "__tour_done__",
                "__open_declined__", "__tour_done_declined__", "__open_fresh__",
                "__unit_quiz__")
        history = [m for m in history if not (
            m.get("role") == "user" and str(m.get("content", "")).strip().lower() in junk)]
        _has_record, _record_note = False, ""    # build hm: set on the non-tour branch
        if after_tour:
            # 2026-08-01 (Jim: "after the tour he restates his name as if I just logged in"):
            # the guided screen tour JUST ended, and the tour already introduced Mr. Cadabra
            # by name -- so the lesson opener must not re-introduce him.
            opener_note = (
                "(SYSTEM: The guided SCREEN TOUR just finished — you ALREADY introduced yourself "
                "by name seconds ago, so do NOT say your name again and do NOT re-greet. Flow "
                "straight on from the tour: one enthusiastic bridge sentence, then the one-line "
                "big idea of this course, today's goal + the goals card, and your first question. "
                "The student did NOT type anything; this is NOT an interruption.)")
        else:
            # build hm (Phase 4, Class D): THE SERVER DECIDES WHETHER YOU HAVE MET.
            # The old note said "If you have met before... recap; if this is your
            # first meeting..." and left the choice -- and the recap's facts -- to
            # the model. When the record was empty, compliance required invention,
            # and the invented recap was then STORED in history and replayed by
            # every later opener as memory. Now the branch happens in code, and a
            # returning student's recap facts are stated BY the server FROM the
            # record (history is style, not truth).
            _has_record, _record_note = _opener_record_note(
                code, req.course, resolved_unit, history)
            if _has_record:
                opener_note = (
                    "(SYSTEM: The student just OPENED the lesson — they did NOT type anything, and this "
                    "is NOT an interruption. You HAVE met before. Warmly greet them back by name and "
                    "give a SHORT recap of where you two are and what's next, then invite them to keep "
                    "going." + _record_note + " Do NOT scold "
                    "them, do NOT tell them to focus, and do NOT act annoyed.)")
            else:
                opener_note = (
                    "(SYSTEM: The student just OPENED the lesson — they did NOT type anything, and this "
                    "is NOT an interruption. THE SERVER RECORD SHOWS NO PRIOR LESSONS together in this "
                    "course and no stored conversation: this IS your first meeting here, whatever the "
                    "conversation may appear to suggest. Begin the first-meeting flow. Do NOT welcome "
                    "them 'back', do NOT recap, and do NOT reference or invent any past session "
                    "together. Do NOT scold "
                    "them, do NOT tell them to focus, and do NOT act annoyed.)")
        # 2026-08-11 (build dw, Jim live: "welcome back, we were looking at this chart,
        # ready to keep going?" after DAYS away): the opener now knows the gap. A day
        # or more since the last session in this course -> a real refresher, not a
        # one-liner. Fail-open: no data, no gap note, opener unchanged.
        gap_days = 0
        try:
            if store.enabled():
                la = (store.get_course_activity(code).get(req.course) or {}).get("last_active")
                if la:
                    import datetime as _dt
                    gap_days = max(0, (_dt.date.today()
                                       - _dt.date.fromisoformat(str(la)[:10])).days)
        except Exception as exc:  # noqa: BLE001
            print(f"[opener] gap check failed (ignored): {exc}")
        if gap_days >= 1 and not (after_tour or fresh_start) and _has_record:
            # build hm: the refresher's FACTS come from the server record note above
            # (the unit is named there); the conversation supplies tone and recent
            # wording, never facts. The old text invited the model to treat its own
            # stored prose as memory -- exactly the disease.
            opener_note += (
                f" (ALSO: it has been {gap_days} day{'s' if gap_days != 1 else ''} since "
                "your last session together in this course. Do NOT open with a bare "
                "'ready to keep going?'. Give a REAL refresher first, warmly and briefly "
                "(3-4 sentences): name the unit the SERVER RECORD above puts you two in "
                "-- never any other -- remind them in plain words what that unit has "
                "been about and what the mastery notes show they had already figured "
                "out or nailed, put the key thing back on the board if it helps, THEN "
                "ask one gentle memory-jog question before moving forward. Memory fades "
                "in a few days -- back up a little; it should feel like a friend "
                "catching you up, never a test. And if a PROBLEM was mid-flight "
                "when they left, re-derive it together in two quick lines or "
                "start it fresh (rule 40i) -- never resume at its last step "
                "trusting their memory of a value from a week ago.)")
        # 2026-08-11 (build dw, Jim live: "it's only showing two bars"): the server KNOWS
        # when the TODAY bar is empty. When it is, the opener's standing instruction to
        # emit [[today items]] becomes a per-turn order it cannot miss.
        if not student_context.get("today_live"):
            opener_note += (
                " (ALSO: the TODAY progress bar at the top of the student's screen is "
                "EMPTY right now. Your FIRST message must state today's short plan (2-3 "
                "items) and emit the matching [[today items=\"...\"]] tag -- resumed "
                "sessions included, every time. No session starts without today's map "
                "on the wall.)")
        if quiz_intent:
            # replaces the generic opener outright -- this door has one purpose
            opener_note = (
                "(SYSTEM: The student clicked 'Retake the Unit Quiz' on their dashboard for "
                "their FOCUS unit -- they came specifically to take that Unit Quiz NOW, and "
                "the app already confirmed the intent. One warm welcome-back sentence, remind "
                "them the record keeps their BEST score so a retake can only help (rule 50), "
                "then administer the FOCUS unit's Unit Quiz per the QUIZZES rules -- the full "
                "quiz, no teaching lesson first, and do NOT make them ask again. Exception: if "
                "your notes show they have genuinely never met some of this unit's topics, say "
                "so plainly and offer a very short warm-up first -- their choice.)")
        if assess_declined:
            opener_note += (
                " (ALSO: the app just showed the Course Assessment invitation card ON SCREEN and "
                "the student chose 'Not right now -- start me at Unit 1.' That question is ASKED "
                "AND ANSWERED. Do NOT mention, offer, or hint at the assessment or placement "
                "again this session -- welcome them warmly and start teaching at Unit 1.)")
        if fresh_start:
            opener_note += (
                " (ALSO: the student clicked 'Take me to my course path' -- they explicitly do "
                "NOT want to pick up the recent side work your notes may mention (an explored "
                "topic or practice problem from another part of the course). Do NOT recap or "
                "resume it. Welcome them back briefly, then run the full opening sequence for "
                "their FOCUS unit (today's topic, the goal + goals card, ready-check) and teach "
                "that unit from where their mastery actually stands.)")
        # (ol) THE DANGLING ANSWER. Jim's live catch, 2026-08-26 23:23: he signed in
        # after a break and the opener's first words were "Nice -- categorical is
        # exactly right for house numbers!" -- an answer from the PREVIOUS session
        # graded as the greeting, and a quiz "wrapped up" out of nowhere. When the
        # stored conversation ends with a student turn the tutor never answered
        # (that session closed before the reply), the model's instinct is to finish
        # the thread. The note now names the trap, and referee 53 (opener_grade_
        # conflict, keyed on the "opener" flag below) rejects any opener that
        # grades instead of greeting.
        try:
            _tail = history[-1] if history else None
            if isinstance(_tail, dict) and _tail.get("role") == "user":
                _stale = " ".join(str(_tail.get("content", "")).split())[:80].replace('"', "'")
                opener_note += (
                    " (ALSO: the stored conversation ENDS with a student message -- \""
                    + _stale + "\" -- that was never answered, because that session "
                    "closed before your reply. That answer is STALE: it was given "
                    "before this sign-in, possibly days ago. Do NOT grade it and do "
                    "NOT continue that thread as if no time passed. Greet them back "
                    "first; then, if the hanging question still matters, RE-POSE it "
                    "fresh (rule 40i) and let them answer it NOW.)")
        except Exception as exc:  # noqa: BLE001 -- a broken note must not cost the opener
            print(f"[opener] dangling-answer note failed (ignored): {exc}")
        student_context["opener"] = True   # (ol) referee 53's server-side gate
        reply = _bold_first_terms(tutor.get_tutor_reply(student_context, history, opener_note, req.course, code=code), history)
        _record_learned(code, req.course, reply)
        _record_result_tags(code, req.course, reply)   # build hu: openers can carry tags too
        # build il: recording first, then the tick net -- so a result that just
        # completed a today item reaches the page in this same reply.
        reply = _ensure_today_ticks(code, req.course, history, reply)
        _record_today_bar(code, req.course, reply)
        # build hk: the junk-strip is re-applied to the FRESH history inside the
        # atomic transform (idempotent), then the opener's reply is appended -- so an
        # opener racing a typed first message can no longer erase it.
        _opener_reply = {"role": "assistant", "content": reply}
        mutate_history(code, req.course, lambda h: [
            m for m in h
            if not (m.get("role") == "user"
                    and str(m.get("content", "")).strip().lower() in junk)
        ] + [_opener_reply])
        return {"reply": reply}

    # build gi: BEFORE this turn is appended, `history` still ends with the tutor's
    # PREVIOUS words -- which is exactly what the student was reacting to.
    _record_term_gap(code, req.course, message, history)
    # build og: THE STARTING BLOCKS. If the previous turn speculated this very
    # answer, the fully-verified reply is already waiting -- ship it with zero
    # model calls. Any mismatch discarded the stash inside _spec_take; the live
    # path below is byte-identical to before this build.
    reply = None
    if not final_mode:
        reply = _spec_take(code, req.course, history, message)
    if reply is None:
        reply = _bold_first_terms(tutor.get_tutor_reply(student_context, history, message, req.course,
                                                        code=code, turn_note=turn_note), history)
    _record_learned(code, req.course, reply)
    # build hu (Class E): the SERVER records the reply's own result tags -- the
    # client's POST is only an echo now (see the note above post_final).
    _record_result_tags(code, req.course, reply, final_allowed=(final_mode == "exam"))
    # build il: recording first, then the tick net -- a result that just completed
    # a today item (or work-time earned since last turn) reaches the page in THIS
    # reply's tags, and the augmented reply is what history remembers below.
    reply = _ensure_today_ticks(code, req.course, history, reply)
    _record_today_bar(code, req.course, reply)
    # build gj: measure rule 37 -- a term with a written script, used without it.
    _record_unintroduced(code, req.course, reply, history)

    # Remember this exchange so the tutor recalls it next time. build hk: appended
    # ATOMICALLY -- the fresh history is re-read under a row lock inside the store, so
    # a concurrent turn's exchange (two tabs, a double-submit, a retry) survives
    # beside this one instead of being overwritten by whichever save landed last.
    _exchange = [{"role": "user", "content": message},
                 {"role": "assistant", "content": reply}]
    mutate_history(code, req.course, lambda h: h + _exchange)

    # build og: ARM THE STARTING BLOCKS for the next turn. Only when this reply
    # ends in a computable pending line; never on quiz/check/exam turns (their
    # grading writes mastery) and never on turns that recorded result tags (the
    # context snapshot below would be stale). The thread runs the FULL verified
    # pipeline off the clock; SPEC_DISABLE_THREAD=1 lets the battery call the
    # speculation body synchronously instead.
    try:
        _spec_expected = None
        if (not final_mode
                and not re.search(r"\[\[\s*(?:quiz|check|finalexam)\b", reply)):
            _spec_expected = _spec_expected_answer(reply)
        if _spec_expected is not None:
            _spec_hist2 = list(history) + _exchange
            if os.environ.get("SPEC_DISABLE_THREAD") == "1":
                pass          # the battery drives _speculate_next directly
            else:
                threading.Thread(
                    target=_speculate_next,
                    args=(code, req.course, dict(student_context), _spec_hist2,
                          _spec_expected),
                    daemon=True).start()
    except Exception as _sexc:  # noqa: BLE001 -- arming must never break a turn
        print(f"[spec] arm failed (ignored): {_sexc}")

    # Real tracking: the COURSE now teaches all 9 units starting at the student's
    # placed unit, so course activity counts as "learning" whatever unit they're on.
    # UNPLACED (2026-08-07 build ba, Jim's dashboard catch): count activity toward the
    # FIRST UNMASTERED unit -- a brand-new student's is Unit 1. The old flat default of 2
    # made fresh elementary students SKIP Unit 1 entirely: the first turn logged "learning
    # Unit 2", the mastery note then steered the tutor there, and Counting & Number Sense
    # was never taught.
    # build hj: the tracker consumes the SAME resolved unit the prompt and the referee
    # were given -- the derivation this block used to re-do by hand let placement
    # outrank progression forever on any turn without a [[unitplan]] tag (the pre-gs
    # bug, quietly re-emerging every tagless turn; review finding F4c).
    # build gs, preserved: THE TUTOR'S OWN DECLARATION OUTRANKS EVERYTHING except an
    # explicit focus -- what the tutor says it is teaching is the truth for THIS turn,
    # and (completing gs) it persists into the next resolution via topic_progress.
    # build hm (Phase 4, Class D): ...but only a declaration the RECORD can justify.
    # A hallucinated [[unitplan unit="5"]] used to file a real topic_progress row here
    # and return as the rail's truth on the next resume -- the likeliest phantom-Unit-5
    # mechanism. The nineteenth referee already regenerates such drafts upstream;
    # because every referee fails open, the filing gate re-checks what shipped.
    declared = _declared_unit(reply)
    course_unit, _up_verdict = _accept_declared_unit(
        declared, resolved_unit, unit_source,
        student_context.get("allowed_units"), code, req.course)
    _probe_unit_drift(code, req.course, reply, declared, course_unit,
                      resolved=resolved_unit, source=unit_source)
    _track_topic(code, course_unit, curriculum.unit_name(req.course, course_unit),
                 "learning", req.course)

    return {"reply": reply}


@app.post("/api/practice")
def practice(req: PracticeRequest):
    """
    Coach the student through a SPECIFIC problem they brought (homework help).

    Unlike /api/chat, practice is NOT tied to the curriculum, placement, or saved
    session memory. The browser holds the practice conversation and sends it back in
    `history` each turn, so nothing is persisted here -- a homework problem is a
    one-off. We validate the code so only real students can use it.
    """
    _deg = _degraded_reply()          # build hv: no teaching into a stranded file fork
    if _deg:
        return _deg
    student = _student_or_404(req.code)
    _rate_limit("brain:" + req.code.strip(), limit=40, window_seconds=300, what="messages")

    message = (req.message or "").strip()
    if not message:
        raise HTTPException(status_code=400, detail="Please say what you're stuck on first.")

    # Sanitize the client-supplied history to just clean user/assistant text turns.
    safe_history = []
    for m in (req.history or [])[-tutor.MAX_HISTORY_MESSAGES:]:
        if not isinstance(m, dict):
            continue
        role = m.get("role")
        content = m.get("content")
        if role in ("user", "assistant") and isinstance(content, str) and content.strip():
            safe_history.append({"role": role, "content": content})

    # FOUNDATION MEMORY (build cf): practice and topic teach vocabulary too, so they get
    # the same canonical scripts AND the same "already introduced -- ask first" list. A
    # student must not hear one definition of "denominator" in the lesson and a different
    # one on the topic page (rule 28), and a term they met here counts as met.
    student["foundations_heard"] = _foundations_heard(req.code.strip(), req.course)
    reply = _bold_first_terms(tutor.get_practice_reply(student, req.problem, safe_history, message, req.course, code=req.code.strip()), req.history)
    _record_learned(req.code.strip(), req.course, reply)
    _record_result_tags(req.code.strip(), req.course, reply)   # build hu (Class E)

    # Real tracking: classify the problem to a unit WITHIN this course, count "practiced".
    unit, name = curriculum.classify_unit(req.problem or message, req.course)
    _track_topic(req.code.strip(), unit, name, "practiced", req.course)

    return {"reply": reply}


def _sanitize_history(raw):
    """Keep only clean {user|assistant: text} turns from client-supplied history."""
    out = []
    for m in (raw or [])[-tutor.MAX_HISTORY_MESSAGES:]:
        if not isinstance(m, dict):
            continue
        role, content = m.get("role"), m.get("content")
        if role in ("user", "assistant") and isinstance(content, str) and content.strip():
            out.append({"role": role, "content": content})
    return out


@app.post("/api/topic")
def topic(req: TopicRequest):
    """
    Give a focused mini-lesson on the topic the student chose (topic mode).

    Like /api/practice, this is NOT tied to the curriculum/placement/saved memory:
    the browser holds the conversation and passes it back each turn, so nothing is
    persisted. (Real per-topic tracking lands in the next phase, once durable
    storage is on.)
    """
    _deg = _degraded_reply()          # build hv: no teaching into a stranded file fork
    if _deg:
        return _deg
    student = _student_or_404(req.code)
    _rate_limit("brain:" + req.code.strip(), limit=40, window_seconds=300, what="messages")
    message = (req.message or "").strip()
    if not message:
        raise HTTPException(status_code=400, detail="Please pick or name a topic first.")
    student["foundations_heard"] = _foundations_heard(req.code.strip(), req.course)
    reply = _bold_first_terms(tutor.get_topic_reply(student, req.topic, _sanitize_history(req.history), message, req.course, code=req.code.strip()), req.history)
    _record_learned(req.code.strip(), req.course, reply)
    _record_result_tags(req.code.strip(), req.course, reply)   # build hu (Class E)

    # Real tracking: classify the chosen topic to a unit WITHIN this course, count "explored".
    unit, name = curriculum.classify_unit(req.topic or message, req.course)
    _track_topic(req.code.strip(), unit, name, "explored", req.course)

    return {"reply": reply}


@app.get("/api/voice-status")
def voice_status():
    """Tell the frontend whether the natural ElevenLabs voice is configured."""
    return {"eleven": bool(ELEVEN_API_KEY)}


# -----------------------------------------------------------------------------
# TTS AUDIO CACHE -- ElevenLabs charges per character, so we cache the generated audio keyed by the
# EXACT text (+ voice + model). Identical text -> serve the saved render instead of paying to generate
# it again. Most teaching speech is unique (rare hits), but fixed/repeated lines (openers, the tour,
# stock encouragements, UI prompts) hit and cost nothing after the first time. The cached bytes are the
# SAME ElevenLabs render replayed, so there is NO quality change. (Added 2026-07-30.)
# -----------------------------------------------------------------------------
import hashlib
_TTS_CACHE_DIR = DATA_DIR / "tts_cache"


def _script_closure_texts() -> set:
    """Every line the scripted course can speak, as TEXT. Memoised -- LESSONS is
    static for the life of the process. Empty set if lessonscripts cannot be read,
    which degrades kf to the old single-model behaviour rather than breaking the voice."""
    global _SCRIPT_CLOSURE_TEXTS
    if _SCRIPT_CLOSURE_TEXTS is None:
        try:
            # (mk) one owner -- see lessonscripts.course_audio_lines()
            _SCRIPT_CLOSURE_TEXTS = set(_closure_lines())
        except Exception as exc:  # noqa: BLE001
            print(f"[speak] closure unavailable, scripted model split is off: {exc}")
            _SCRIPT_CLOSURE_TEXTS = set()
    return _SCRIPT_CLOSURE_TEXTS


_SCRIPT_CLOSURE_TEXTS = None


def _tts_model_for(text: str) -> str:
    """BUILD kf -- THE ONE PLACE that decides which model voices a line.

    Membership of the scripted closure is the test, so no caller has to declare its
    lane and no client has to be trusted to. Critically, the cache PATH and the
    RENDER both come through here: if they could disagree, every scripted line would
    be written under one key and looked up under another, miss forever, and re-bill
    the whole course on every single play."""
    try:
        if SCRIPT_TTS_MODEL and text in _script_closure_texts():
            return SCRIPT_TTS_MODEL
    except Exception:  # noqa: BLE001 -- never let the split break the voice
        pass
    return ELEVEN_MODEL


# =============================================================================
# BUILD vc (2026-09-10) -- THE LABEL ON THE SHELF AND THE LABEL ON THE REQUEST.
# -----------------------------------------------------------------------------
# A voice clip is filed under a label, and the label IS the sentence (see
# _tts_cache_path below: sha256 of voice + model + text). The prewarm filed it under
# the sentence AS AUTHORED. The page asks for it after speech-text.js's forSpeech()
# has tidied it for speaking -- "Algebra II" -> "Algebra Two" (so the numeral is not
# read as the letter I), "3:2" -> "3 to 2", "**Area**" -> "Area".
#
# Where those two differ the clip is NEVER FOUND. The course pays to render one no
# page will ever ask for, and then pays AGAIN, live, in front of a student, on every
# single play, forever. Measured 2026-09-10, and it was not a rounding error:
#     1,943 of 39,969 course lines   (11.0% of geometry, 8.7% of algebra2)
#       306 of 306 foundations lines (ALL of them -- each opens with a **bold** term
#                                     that forSpeech strips)
# It is also why Jim heard "10 second delay before this started" and why the drill
# lane's closure gate 409'd lines that were plainly in the closure.
#
# ⭐ JIM'S RULING, 2026-09-10, given both options in plain words: have the RECORDER
#    tidy the sentence the same way the page does -- and generate the server's copy
#    from the page's, so the two can never drift apart. forSpeech stays where it
#    lives, in JavaScript, because that is also what the browser voice needs; and
#    tools/genspeechmap.py runs the real function, in node, over every authored line
#    and writes the differences to speechmap.py. ruletests PART 3ky rebuilds that in
#    memory and fails the build if the committed file is stale, so it cannot rot.
#
# _spoken() is the ONE reader. Everything absent from the map is its own answer, so a
# gap degrades to exactly the behaviour that shipped before this build, never worse.
# =============================================================================
def _spoken(text: str) -> str:
    """The authored line as THE PAGE WILL ACTUALLY ASK FOR IT (forSpeech applied).

    Call this wherever authored text becomes a cache key -- what the prewarm renders,
    what the closure protects, what the estimator prices. Never call it on text that
    came FROM a page: that has already been through forSpeech, and running the map
    over it a second time is how you would invent a third label."""
    try:
        return speechmap.MAP.get(text, text)
    except Exception:  # noqa: BLE001 -- a broken map must never break the voice
        return text


def _closure_lines(lessons=None) -> list:
    """(mk's one owner, wearing (vc)'s label.) Every line the course can speak, as the
    page asks for it. The SIX sites that used to call course_audio_lines() directly
    call this instead -- one owner of what the closure IS, and now one owner of what
    it is CALLED, because a set that disagrees with the page about either is a set
    that protects the wrong files and prices the wrong job."""
    # sorted(set(...)) keeps course_audio_lines' own contract ("deduped and sorted")
    # on the far side of the map: two different authored lines CAN tidy to the same
    # sentence ("Algebra II" and "Algebra Two" both become "Algebra Two"), and a
    # closure that listed one clip twice would price and render it twice. There are
    # no such pairs today (PART 3ky measures it at zero) -- this is what keeps it
    # harmless on the day there is one.
    return sorted({_spoken(s) for s in lessonscripts.course_audio_lines(lessons)})


def _tts_cache_path(text: str) -> Path:
    key = hashlib.sha256(("|".join([str(ELEVEN_VOICE_ID), str(_tts_model_for(text)), text])).encode("utf-8")).hexdigest()
    return _TTS_CACHE_DIR / (key + ".mp3")


# =============================================================================
# BUILD ke (2026-08-21) -- IS THIS CLIP WHOLE?
# =============================================================================
# Jim heard "slurring and nonsense" on several lessons. It was not missing audio --
# a missing clip is SILENT on the pilot page. It was cache entries containing two
# different renders spliced together (see the change note at the top of this file).
#
# TWO independent checks, because either alone has a blind spot:
#
#   1. FRAME-CHAIN WALK -- every MPEG frame header must parse and the chain must run
#      to the end with nothing left over. Catches truncation, zero fill, JSON/HTML
#      error bodies, garbage, and anything appended past the end.
#
#   2. Xing/Info CROSS-CHECK -- mainstream encoders put a header in the first frame
#      declaring the clip's TOTAL byte count. We compare it with what is actually
#      on disk.
#
# Why BOTH: ElevenLabs renders constant-bitrate mp3_44100_128, so every clip has the
# same uniform frame geometry. Splice two clips at any offset and the frame chain
# still walks cleanly -- check 1 is blind to it. But the surviving Xing header still
# describes the clip it came from, so check 2 catches it. Proved both ways in
# ruletests PART 3cx against real encoder output and 26 synthetic corruptions.
#
# KNOWN LIMIT, stated plainly: a single flipped byte INSIDE a frame's payload leaves
# both the chain and the counts intact. Catching that needs a full decode and a
# dependency we do not have on Render -- and payload bit-rot makes a click, not a
# melted line, so it is not the failure we are chasing.
import struct
import tempfile

_MP3_BITRATES_V1 = {  # kbps, MPEG-1, by layer number then bitrate index
    1: [0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448, -1],
    2: [0, 32, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384, -1],
    3: [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, -1],
}
_MP3_BITRATES_V2 = {  # kbps, MPEG-2 / MPEG-2.5
    1: [0, 32, 48, 56, 64, 80, 96, 112, 128, 144, 160, 176, 192, 224, 256, -1],
    2: [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, -1],
    3: [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, -1],
}
_MP3_RATES = {3: [44100, 48000, 32000, 0],      # MPEG-1
              2: [22050, 24000, 16000, 0],      # MPEG-2
              0: [11025, 12000, 8000, 0]}       # MPEG-2.5

# A one-word clip ("Yes!") at 44.1kHz/128kbps is ~0.4s ~= 7 KB, so 900 bytes sits far
# below anything real and comfortably above any error body.
_TTS_MIN_CACHE_BYTES = 900
_TTS_MIN_CACHE_FRAMES = 8


def _mp3_frame_len(head) -> int:
    """Byte length of the MPEG frame whose 4-byte header this is, or 0 if the header
    is not a valid one. Pure arithmetic -- no decoding, no dependencies."""
    if len(head) < 4 or head[0] != 0xFF or (head[1] & 0xE0) != 0xE0:
        return 0
    ver = (head[1] >> 3) & 0x03          # 3=MPEG-1, 2=MPEG-2, 0=MPEG-2.5, 1=reserved
    layer = (head[1] >> 1) & 0x03        # 3=Layer I, 2=Layer II, 1=Layer III, 0=reserved
    if ver == 1 or layer == 0:
        return 0
    layer_n = 4 - layer                  # -> 1, 2 or 3
    br_i = (head[2] >> 4) & 0x0F
    sr_i = (head[2] >> 2) & 0x03
    if br_i in (0, 15) or sr_i == 3:     # "free"/"bad" bitrate, reserved sample rate
        return 0
    table = _MP3_BITRATES_V1 if ver == 3 else _MP3_BITRATES_V2
    bitrate = table[layer_n][br_i] * 1000
    rate = _MP3_RATES[ver][sr_i]
    if bitrate <= 0 or rate <= 0:
        return 0
    pad = (head[2] >> 1) & 0x01
    if layer_n == 1:
        return ((12 * bitrate // rate) + pad) * 4
    if ver == 3:                          # MPEG-1, Layer II/III
        return (144 * bitrate // rate) + pad
    return (72 * bitrate // rate) + pad   # MPEG-2/2.5, Layer II/III


def _id3v2_len(data) -> int:
    """Total byte length of the ID3v2 tag at the head of `data`, or 0 if there is none."""
    if len(data) < 10 or data[:3] != b"ID3":
        return 0
    flags = data[5]
    size_bytes = data[6:10]
    if any(b & 0x80 for b in size_bytes):        # a real tag's size is synchsafe
        return 0
    size = 0
    for b in size_bytes:
        size = (size << 7) | (b & 0x7F)
    total = 10 + size + (10 if flags & 0x10 else 0)
    return total if 0 < total <= len(data) else 0


def _xing_counts(data, pos):
    """(declared_frames, declared_bytes) from the Xing/Info header of the frame at
    `pos`, or (None, None) when the clip carries none."""
    head = data[pos:pos + 4]
    if len(head) < 4 or head[0] != 0xFF or (head[1] & 0xE0) != 0xE0:
        return (None, None)
    ver = (head[1] >> 3) & 0x03
    mono = ((head[3] >> 6) & 0x03) == 3
    side = (17 if mono else 32) if ver == 3 else (9 if mono else 17)
    off = pos + 4 + side
    if data[off:off + 4] not in (b"Xing", b"Info") or len(data) < off + 8:
        return (None, None)
    flags = struct.unpack(">I", data[off + 4:off + 8])[0]
    p, frames, nbytes = off + 8, None, None
    if flags & 0x01:
        if len(data) < p + 4:
            return (None, None)
        frames = struct.unpack(">I", data[p:p + 4])[0]
        p += 4
    if flags & 0x02:
        if len(data) < p + 4:
            return (None, None)
        nbytes = struct.unpack(">I", data[p:p + 4])[0]
    return (frames, nbytes)


def mp3_is_intact(data) -> bool:
    """True when `data` is a coherent, complete MPEG audio clip. NEVER raises -- a
    validator that throws would take the whole voice down with it."""
    try:
        if not data or len(data) < _TTS_MIN_CACHE_BYTES:
            return False
        if data[:1] in (b"{", b"<"):        # a JSON or HTML error body, not audio
            return False
        end = len(data)
        if end > 128 and data[end - 128:end - 125] == b"TAG":   # ID3v1 trailer
            end -= 128
        audio_start = _id3v2_len(data)
        if audio_start >= end:
            return False
        declared_frames, declared_bytes = _xing_counts(data, audio_start)
        pos, frames = audio_start, 0
        while pos + 4 <= end:
            size = _mp3_frame_len(data[pos:pos + 4])
            if size <= 0 or pos + size > end:
                return False                # chain broke: truncated, spliced or filled
            pos += size
            frames += 1
        if frames < _TTS_MIN_CACHE_FRAMES or (end - pos) >= 4:
            return False
        # The BYTE count is exact and does the real work: every splice leaves a file
        # whose length disagrees with the header of whichever clip landed first.
        if declared_bytes is not None and declared_bytes != (end - audio_start):
            return False
        # The FRAME count is +/-1 by encoder convention (LAME and ffmpeg do not count
        # the Xing frame itself, others do), so it is checked with that tolerance and
        # never tighter -- a false positive here re-renders a clip we already paid for.
        if declared_frames is not None and abs(declared_frames - frames) > 1:
            return False
        return True
    except Exception:       # noqa: BLE001 -- a validator must never raise
        return False


def _mp3_shape(data):
    """BUILD kf: the MPEG parameters of the first frame -- {mpeg, layer, rate, kbps,
    channels} -- or None. Reads a header, decodes nothing. Used by the course audio
    audit to spot a clip that is not the shape everything else is, because the leading
    silence we concatenate at serve time assumes 44,100 Hz mono 128 kbps and a clip in
    another shape can decode oddly once that silence is glued to its front."""
    try:
        pos = _id3v2_len(data)
        h = data[pos:pos + 4]
        if len(h) < 4 or h[0] != 0xFF or (h[1] & 0xE0) != 0xE0:
            return None
        ver = (h[1] >> 3) & 0x03
        layer = (h[1] >> 1) & 0x03
        if ver == 1 or layer == 0:
            return None
        layer_n = 4 - layer
        br_i = (h[2] >> 4) & 0x0F
        sr_i = (h[2] >> 2) & 0x03
        if br_i in (0, 15) or sr_i == 3:
            return None
        table = _MP3_BITRATES_V1 if ver == 3 else _MP3_BITRATES_V2
        return {"mpeg": {3: "1", 2: "2", 0: "2.5"}[ver],
                "layer": layer_n,
                "rate": _MP3_RATES[ver][sr_i],
                "kbps": table[layer_n][br_i],
                "channels": "mono" if ((h[3] >> 6) & 0x03) == 3 else "stereo"}
    except Exception:  # noqa: BLE001 -- an audit helper must never raise
        return None


def mp3_has_counts(data) -> bool:
    """True when the clip carries an Xing/Info header, i.e. the cross-check has teeth
    on it. The repair endpoint reports this so we know the detector's real coverage."""
    try:
        if not data or len(data) < 64:
            return False
        f, b = _xing_counts(data, _id3v2_len(data))
        return f is not None or b is not None
    except Exception:       # noqa: BLE001
        return False


def _tts_cache_store(text: str, data: bytes, source: str = "speak") -> bool:
    """THE ONE DOOR into the TTS cache. Returns True when the clip was stored.

    BUILD ke: every writer gets its OWN temp file. The old code derived the temp name
    from the text (`path.with_suffix(".part")`), so the prewarm loop and a child's
    playback rendering the same line at the same moment collided on one path and
    produced a spliced, permanently-cached clip. mkstemp in the cache directory gives
    each writer a private name; os.replace is atomic; last writer wins and BOTH files
    were whole. Same-filesystem by construction, so the rename never degrades to a copy.

    Nothing is stored unless it validates -- a bad render must not become a bad clip
    that replays forever."""
    if not mp3_is_intact(data):
        print(f"[speak] REFUSED to cache a damaged clip from {source} "
              f"({len(data or b'')} bytes) -- it will re-render on the next play")
        return False
    fd, tmp_name = None, None
    try:
        _TTS_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(dir=str(_TTS_CACHE_DIR), suffix=".part")
        with os.fdopen(fd, "wb") as fh:
            fd = None                      # fdopen owns it now; do not double-close
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())          # the bytes are on disk before we publish them
        os.replace(tmp_name, str(_tts_cache_path(text)))
        tmp_name = None                    # renamed: nothing left to clean up
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"[speak] cache write error ({source}): {exc}")
        return False
    finally:
        if fd is not None:
            try:
                os.close(fd)
            except Exception:  # noqa: BLE001
                pass
        if tmp_name:
            try:
                os.unlink(tmp_name)        # never leave our own debris behind
            except Exception:  # noqa: BLE001
                pass


# BUILD hs (2026-08-18, Phase 5): THE SPOKEN LINE LEAVES THE URL TOO. An <audio src>
# cannot send headers, so /api/speak was the one place the credential COULD NOT move
# to X-Student-Code -- and worse, the TEXT (a child's lesson, usually carrying their
# first name) rode the same query string into every HTTP log. The pages now POST
# /api/speak-prep {code, text, lead} and get back an opaque one-use-style ticket id;
# the audio element streams GET /api/speak?t=<id> exactly as before (same caching,
# same leading silence, same low-latency stream). Tickets live in memory with a short
# TTL -- a restart invalidates them and the page simply mints a fresh one; they are
# NOT single-use because <audio> legitimately re-requests (ranges, replays, retries).
# The legacy ?text=&code= form still works so a stale cached page keeps its voice
# across the deploy; the shipped pages no longer send it.
_SPEAK_TICKETS: "dict[str, tuple]" = {}
_SPEAK_TICKETS_LOCK = threading.Lock()
_SPEAK_TICKET_TTL = 900        # seconds -- a clip is fetched within moments of minting
_SPEAK_TICKET_CAP = 4000       # entries -- far above any real classroom's burst


class SpeakPrepIn(BaseModel):
    code: str = ""
    text: str = ""
    lead: int = 0
    # (mj) Which lane is asking. "drill" is the only value with a meaning: it demands
    # closure text and mints a ticket that can never spend money. Anything else is the
    # ordinary lane and behaves exactly as it did before this build.
    lane: str = ""


@app.post("/api/speak-prep")
def speak_prep(req: SpeakPrepIn, request: Request):
    """Mint an utterance ticket (build hs -- see the note above). Same gate and rate
    limit as /api/speak itself: this is the endpoint that now spends the budget."""
    code = (req.code or "").strip()
    lane = (req.lane or "").strip().lower()
    if lane == "demo":
        # (uh) THE DEMO LESSON HAS NO STUDENT. Its lines are the authored course's
        # own (closure-only, below) and the ticket is cache-only, so nothing here
        # can spend money; the budget that remains to guard is the cache's
        # bandwidth, keyed by the visitor, not by a code nobody typed.
        code = "demo"
        _rate_limit("speak-demo:" + (request.client.host if request.client else "?"),
                    limit=120, window_seconds=600, what="voice requests")
    else:
        _require_student(code)
        # ⭐ (vb, 2026-09-10) 60 -> 150, AND THE ARITHMETIC IS THE REASON.
        # This limit guards the budget by counting TICKETS, and until this build a
        # lesson minted exactly one per spoken line: a beat lands every ~10-15s
        # (readMs's 2.6s floor, plus the clip, plus SCR_BREATH), so ~20-30 in a
        # five-minute window against a ceiling of 60. Comfortable.
        # Build vb's shelf mints the ticket EARLY instead -- one per line still when
        # the shelf is used (startClip finds the clip and returns before it preps) --
        # but a shelf MISS costs a second one, and /api/script/warm adds up to three
        # per question. Worst case lands near 90 in a window, so the old ceiling
        # would have started answering a real lesson with 429s, and a 429 here is not
        # a small thing: the page falls to the mechanical browser voice mid-lesson.
        # ⚠️ THIS DOES NOT LOOSEN THE BUDGET, because a ticket is not a render: the
        # money is spent by /api/speak, and every extra ticket this build mints is
        # for an AUTHORED line the course pays for exactly once and then caches
        # forever. What the ceiling still does -- stop a logged-in student pumping
        # arbitrary text through a paid renderer -- it does at 150 as well as at 60.
        _rate_limit("speak:" + code, limit=150, window_seconds=300, what="voice requests")
    text = (req.text or "").strip()
    if len(text) > MAX_SPEAK_CHARS:
        raise HTTPException(status_code=413, detail="That text is too long to speak.")
    if not text:
        raise HTTPException(status_code=400, detail="Nothing to speak.")
    # ⭐ (mj) THE DRILL LANE'S TICKETS ARE CLOSURE-ONLY AND CACHE-ONLY.
    # Builds mh and mi pinned this the crude way -- "drill.html must not name
    # /api/speak" -- because at the time it never needed to. Phase 4 fetches Mr.
    # Cadabra to re-teach, in his own real voice, so the page DOES need the route.
    # The invariant was never "do not name the route". It was always: NEVER SEND
    # GENERATED TEXT TO A PAID RENDERER, because a generated problem's sentence was
    # never pre-rendered and is a guaranteed cache miss. That invariant now lives
    # HERE, on the server, where a page cannot get it wrong:
    #   (a) the text must be in the scripted closure, or there is no ticket at all;
    #   (b) the ticket is cache-only, so even a closure line that has not been
    #       rendered yet costs nothing -- it 204s and the browser voice takes over.
    # A server-side gate beats a grep over a file, and this one is exact.
    cached_only = False
    if lane in ("drill", "demo"):        # (uh) the demo lane is the drill lane's twin
        cached_only = True
        try:
            in_closure = _tts_cache_path(text).name in _script_closure_paths()
        except Exception as exc:  # noqa: BLE001 -- a broken memo must not bill anybody
            print(f"[speak] closure check failed, refusing the drill ticket: {exc}")
            in_closure = False
        if not in_closure:
            raise HTTPException(status_code=409, detail=(
                "The drill lane may only speak lines the course has already "
                "authored -- this text is not in the scripted closure."))
    t = secrets.token_urlsafe(16)
    now = time.time()
    with _SPEAK_TICKETS_LOCK:
        if len(_SPEAK_TICKETS) >= _SPEAK_TICKET_CAP:
            expired = [k for k, v in _SPEAK_TICKETS.items() if v[3] <= now]
            for k in expired:
                _SPEAK_TICKETS.pop(k, None)
            while len(_SPEAK_TICKETS) >= _SPEAK_TICKET_CAP:
                _SPEAK_TICKETS.pop(next(iter(_SPEAK_TICKETS)), None)   # oldest-in first
        _SPEAK_TICKETS[t] = (code, text,
                             max(0, min(int(req.lead or 0), 4)), now + _SPEAK_TICKET_TTL,
                             cached_only)
    return {"t": t, "voice": bool(ELEVEN_API_KEY)}


@app.get("/api/speak")
def speak(text: str = "", code: str = "", lead: int = 0, t: str = ""):
    if t:
        with _SPEAK_TICKETS_LOCK:
            tk = _SPEAK_TICKETS.get(t.strip())
        if not tk or tk[3] <= time.time():
            # 410: the page's voice engine mints a fresh ticket and retries once.
            raise HTTPException(status_code=410, detail="That voice ticket expired.")
        code, text, lead = tk[0], tk[1], tk[2]
        # (mj) tickets minted before this deploy are 4-tuples; len() keeps them valid
        # rather than 500-ing a child mid-lesson on the way past a redeploy.
        cached_only = bool(tk[4]) if len(tk) > 4 else False
        if not text or not ELEVEN_API_KEY:
            return Response(status_code=204)
        return _tts_stream_response(text, lead, code=code,
                                    mode=("drill" if cached_only else "speak"),
                                    cached_only=cached_only)
    return _speak_legacy(text, code, lead)


def _speak_legacy(text: str = "", code: str = "", lead: int = 0):
    """
    STREAM the tutor's words as a natural ElevenLabs voice (low latency): audio
    starts playing in the browser before the whole clip is generated. The browser
    plays this via <audio src="/api/speak?text=...&code=...">.

    LOCKED DOWN (2026-07-30): requires a valid student code and caps the text length --
    this endpoint spends real ElevenLabs money, and before this change any stranger
    could call it with arbitrary text and run up the bill. Rate limited per code.

    Identical text is served from an on-disk cache (no ElevenLabs call), saving cost + latency on
    repeated lines. If ELEVENLABS_API_KEY is not set, returns 204 and the browser uses its built-in
    voice instead. (Check /api/voice-status first to avoid an empty request.)

    `lead` (2026-08-03, Jim: "the initial talk almost always misses his first couple of words"):
    extra ~280ms blocks of leading silence, 0-4. The page sends lead=3 (~1.1s total) on the FIRST
    clip of a session -- audio outputs (especially Bluetooth) close during the quiet thinking wait
    and reopen slowly, eating the head of the clip; a longer silent lead means they eat silence.
    Later clips keep the standard single block.
    """
    _require_student(code)
    _rate_limit("speak:" + code.strip(), limit=60, window_seconds=300, what="voice requests")
    text = (text or "").strip()
    if len(text) > MAX_SPEAK_CHARS:
        raise HTTPException(status_code=413, detail="That text is too long to speak.")
    if not text or not ELEVEN_API_KEY:
        return Response(status_code=204)
    return _tts_stream_response(text, lead, code=code.strip(), mode="speak")


# 2026-08-01 (Jim's beta run: "he sometimes drops the first word"): audio output paths
# (especially Bluetooth) take ~100-300ms to open, swallowing the start of playback. We
# prepend ~280ms of REAL MP3 SILENCE (mono 44.1kHz 128k, matching ElevenLabs' format) to
# every served clip, so what gets swallowed is silence -- the first word survives. The
# silence is added at SERVE time only; cached files stay pure voice.
import base64 as _b64
_TTS_LEAD_SILENCE = _b64.b64decode(
    "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjYwLjE2LjEwMAAAAAAAAAAAAAAA//uQwAAAAAAAAAAAAAAAAAAAAAAASW5mbwAAAA8AAAAMAAAVOAAnJycnJycnJzs7Ozs7Ozs7Tk5OTk5OTk5iYmJiYmJiYmJ2dnZ2dnZ2domJiYmJiYmJnZ2dnZ2dnZ2dsbGxsbGxsbHExMTExMTExNjY2NjY2NjY2Ozs7Ozs7Ozs//////////8AAAAATGF2YzYwLjMxAAAAAAAAAAAAAAAAJAOEAAAAAAAAFTh99LqRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//uQxAADwAABpAAAACAAADSAAAAETEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//uSxDkDwAABpAAAACAAADSAAAAEVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7ksQ5A8AAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVMQU1FMy4xMDBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVX/+5LEOQPAAAGkAAAAIAAANIAAAARVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//uSxDkDwAABpAAAACAAADSAAAAEVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7ksQ5A8AAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVMQU1FMy4xMDBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVX/+5LEOQPAAAGkAAAAIAAANIAAAARVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//uSxDkDwAABpAAAACAAADSAAAAEVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7ksQ5A8AAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVMQU1FMy4xMDBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVX/+5LEOQPAAAGkAAAAIAAANIAAAARVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//uSxDkDwAABpAAAACAAADSAAAAEVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7ksQ5A8AAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVU=")


def _tts_stream_response(text: str, lead: int = 0, code: str = "", mode: str = "speak",
                        cached_only: bool = False):
    """Shared TTS pipeline (used by /api/speak and /api/demo-audio): serve the cached
    render if we have it, otherwise stream from ElevenLabs while caching atomically.
    `lead` = extra leading-silence blocks (0-4) beyond the standard one -- the first clip
    of a session gets more so a sleeping audio output eats silence, not words.
    `code`/`mode` (2026-08-04): attribute this request in the usage log -- character
    count + cache hit/miss only, never the text itself."""
    lead_silence = _TTS_LEAD_SILENCE * (1 + max(0, min(int(lead or 0), 4)))
    # Cache HIT: replay the saved render, no ElevenLabs call.
    cache_path = _tts_cache_path(text)
    cache_hit = False
    try:
        cache_hit = cache_path.exists() and cache_path.stat().st_size > 0
    except Exception as exc:  # noqa: BLE001
        print(f"[speak] cache stat error: {exc}")
    # USAGE LOG (2026-08-04): a miss is about to spend ElevenLabs characters; a hit is free.
    # Fire-and-forget -- log_usage swallows its own errors and no-ops when the DB is off.
    store.log_usage(kind="tts", code=code, mode=mode, model=str(_tts_model_for(text) or ""),
                    tts_chars=len(text), tts_cache_hit=cache_hit)
    try:
        if cache_hit:
            return Response(content=lead_silence + cache_path.read_bytes(),
                            media_type="audio/mpeg")
    except Exception as exc:  # noqa: BLE001
        print(f"[speak] cache read error: {exc}")

    # ⭐ BUILD mj -- cached_only: A LANE THAT MAY NEVER SPEND. The drill lane fetches
    # Mr. Cadabra in his real voice when a child is stuck, and every line it asks for
    # is authored closure text that the course has already paid to render. But "has
    # already been rendered" is a fact about the cache at this instant, not a law --
    # half the course is still unrendered while Jim's quota refills. A cached_only
    # request therefore serves the hit and, on a MISS, returns 204 without touching
    # ElevenLabs at all. The page falls back to the browser voice, the child still
    # gets taught, and drilling cannot put a single character on the bill. When the
    # render finishes, his real voice appears in the drill lane by itself.
    if cached_only:
        return Response(status_code=204)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}/stream"
    headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
    payload = {
        "text": text,
        "model_id": _tts_model_for(text),      # kf: same decision as the cache key
        "output_format": "mp3_44100_128",
        "voice_settings": {"stability": 0.55, "similarity_boost": 0.75, "use_speaker_boost": True},
    }

    def audio_stream():
        yield lead_silence               # leading silence: see note above (never cached)
        buf = bytearray()
        complete = False
        try:
            with httpx.stream("POST", url, headers=headers, json=payload, timeout=30.0) as r:
                if r.status_code != 200:
                    print(f"[speak] ElevenLabs {r.status_code}: {r.read()[:200]!r}")
                    return
                for chunk in r.iter_bytes():
                    if chunk:
                        buf.extend(chunk)
                        yield chunk
                complete = True
        except Exception as exc:  # noqa: BLE001
            print(f"[speak] stream error: {exc}")
        # Cache WRITE: only after a fully-streamed, non-empty clip; write atomically so a partial
        # (e.g. client disconnect / error) never leaves a truncated file behind.
        if complete and buf:
            # BUILD ke: one door, private temp file, validated before it is published.
            if _tts_cache_store(text, bytes(buf), source=mode or "speak"):
                _evict_tts_cache()

    return StreamingResponse(audio_stream(), media_type="audio/mpeg")


# -----------------------------------------------------------------------------
# DEMO VOICE (2026-07-30) -- the marketing demo speaks with Mr. Cadabra's REAL voice.
# -----------------------------------------------------------------------------
# The interactive demo (static/demo.html) is fully scripted, so its spoken lines are a
# FIXED, finite list. This endpoint serves ONLY those whitelisted lines -- no arbitrary
# text, so it cannot be abused to spend ElevenLabs money beyond ~14 lines that each
# cache after their first render (then replay free, forever). No login code needed
# (it's the public demo); per-IP rate limited. KEEP THIS LIST IDENTICAL to VOICE_LINES
# in static/demo.html -- update both together.
DEMO_VOICE_LINES = [
    "Hi! I'm Mr. Cadabra. Let's solve this one together — two x plus three equals eleven. Our whole goal is to get x all by itself. First move: what should we do to BOTH sides to undo that plus three? Type your move with the keyboard.",
    "Exactly — subtract three from both sides, and the threes cancel on the left.",
    "Not quite — the plus three is being added, so we do the opposite: subtract. Try typing your move again!",
    "Now we've got two x equals eight. Two x means two TIMES x — so what undoes a times two? Type your move.",
    "Nice — divide both sides by two. Notice the board is waiting for YOU — it never gives away the answer.",
    "Careful — two x means two times x, so we undo it with division. Give it another go!",
    "So — eight divided by two. What does x equal? Work it out and type it with the keyboard.",
    "You got it — x equals four! And look: it checks out, two times four plus three really is eleven.",
    "Close — eight divided by two. What number is that? Type it in.",
    "One quick challenge to show off the keyboard. Type two, then tap the x-to-the-n key, then type three — that builds two to the third power.",
    "Beautiful — two to the third, which is eight. You used the power key like a pro.",
    "Order matters: type 2 first, then the xⁿ key, then 3 — that builds 2^3. Try it!",
    "That's it — you just solved a two-step equation and checked it yourself. Great work! That's how Mr. Cadabra's Classroom teaches: one friendly step at a time.",
    "Hi! I'm Mr. Cadabra. Let's count together! Look — I put some stars on the board. Count them with your finger… how many stars do you see? Tap your answer.",
    "Yes! Five stars — you counted every single one.",
    "Almost! Point at each star and count them one at a time — then tap your answer.",
    "Now watch the magic — here comes one more star! How many stars are there now? Tap your answer.",
    "Six! Five stars plus one more makes six. You just did adding!",
    "Count the new star too — five stars, then one more. Tap your answer!",
    "Fractions — the friendly way. The board shows one half plus one fourth. Here's the trick: one half is the same as two fourths. So two fourths plus one more fourth makes how many fourths? Tap your answer.",
    "Three fourths! Once the bottom numbers match, you just add the tops.",
    "Look at the board — two fourths plus one more fourth. Count the fourths and tap again!",
    "Decimals now. Which is bigger — zero point five, or zero point four five? Careful — more digits does not mean bigger! Tap your answer.",
    "Right! Zero point five is five tenths, and zero point four five is only four and a half tenths. You didn't fall for the trap!",
    "Line them up: zero point five zero versus zero point four five. Which has more tenths? Tap again!",
    "Negative numbers — the number one key to algebra. The board shows negative three plus five. Start three below zero and climb up five… where do you land? Type it in.",
    "Two! You climbed from three below zero up to positive two. Negatives hold no fear for you.",
    "Start at three below zero and climb up five steps, one at a time. Where do you land? Type it!",
    "One more: negative four times negative two. Remember the rule — when the two signs match, the answer is positive. Type it in.",
    "Eight! A negative times a negative flips positive. That one rule unlocks half of algebra.",
    "Both signs are negative — a matching pair — so the answer is POSITIVE four times two. Type it!",
    "Every triangle's angles add up to one hundred eighty degrees — always. This one has a ninety and a thirty-five. How big is the mystery angle? Type it in.",
    "Fifty-five degrees! Ninety plus thirty-five is one twenty-five, and one eighty minus that leaves fifty-five.",
    "Add the two angles you know first — ninety plus thirty-five — then subtract from one eighty. Type it!",
    "Now the most famous theorem in math. A right triangle has legs three and four — the board shows Pythagoras at work. What's the long side? Type it in.",
    "Five! The three-four-five triangle — builders have trusted it for four thousand years.",
    "c squared is twenty-five — so c is the number that times itself makes twenty-five. Type it!",
    "Exponentials — where algebra gets powerful. The board asks: two to what power makes thirty-two? Count the doublings. Type the power.",
    "Five! Two, four, eight, sixteen, thirty-two — five doublings. You just did a logarithm without the scary name.",
    "Keep doubling: two, four, eight… count how many steps it takes to reach thirty-two. Type that count!",
    "Now a quadratic, factored and ready: x minus five, times x plus two, equals zero. For the whole thing to be zero, one piece must be zero. What x makes the FIRST piece zero? Type it.",
    "Five! And x equals negative two kills the other piece. Two solutions, no sweat — that's the zero-product property.",
    "Look at the first piece: x minus five. What x makes it exactly zero? Type it!",
    "Welcome to the unit circle — the heart of trigonometry. Half a spin around the circle is pi radians. How many degrees is that? Type it in.",
    "One hundred eighty degrees! Radians are just another ruler for angles — pi is exactly half the circle.",
    "A FULL circle is three hundred sixty degrees, and pi radians is exactly half of it. Type the degrees!",
    "Now the launchpad to calculus: sine of ninety degrees — the very top of the circle. What's its value? Type it in.",
    "One! At the top of the circle you're at full height. Trig is just reading heights and shadows off a circle.",
    "At ninety degrees you're at the very TOP of the unit circle — as high as it gets. That height is… type it!",
    "Statistics time. Three quiz scores on the board: three, five, and ten. The mean is the fair-share average — add them up, split them evenly. What's the mean? Type it in.",
    "Six! Eighteen points split evenly three ways. The mean shares everything out fairly.",
    "Add all three first — three plus five plus ten — then divide by how many scores there are. Type it!",
    "Now the median — the MIDDLE value once they're in order. Same three scores. What's the median? Type it in.",
    "Five! Mean six, median five — two different stories from the same data. That gap is where statistics gets interesting.",
    "Line them up smallest to biggest and take the one sitting in the middle. Type it!",
    "Calculus asks one big question: how fast is something changing? For x cubed, the power rule answers it — bring the three down front, drop the power by one. What's the new power? Type it in.",
    "Two! So the derivative is three x squared — you just took your very first derivative.",
    "The rule says drop the power by ONE. Three minus one is… type it!",
    "Let's use it. The slope of x cubed at x equals two is three times two squared. Work that out — type the slope.",
    "Twelve! At x equals two the curve is climbing twelve units per step. That's calculus — exact speed at an exact instant.",
    "Two squared is four, times three is… type it!",
    "Differential equations describe how things change — and rule one is: classify first. The board shows y double-prime plus y equals zero. The ORDER is the highest derivative in sight. What order is this? Type the number.",
    "Second order — the double-prime is the giveaway. This little equation runs every pendulum and guitar string on Earth.",
    "Count the tick marks on the busiest y — double-prime means the SECOND derivative. Type the order!",
    "One more to classify: y prime equals three y. What order is this one? Type the number.",
    "First order! And it's the equation of growth itself — money, bacteria, radioactive decay. Every model starts with classify.",
    "Just one tick mark on the y — that's the FIRST derivative. Type the order!",
    "And that's how I teach — I talk, the board shows every step, and you do the thinking. Try another level, or come meet me in the real classroom!",
    "Let's look at it a different way — I've put the whole move on the board. Follow it through, then type your answer!",
    "Let's look at it a different way — I've put the whole move on the board. Follow it through, then tap your answer!",
    "No worries — I'll show you this one! The answer is on the board now. In my real classroom I keep trying new ways — smaller steps, new pictures — until it clicks. On we go!",
    "Hi, I'm Mr. Cadabra! Here's how I teach: I talk you through it in my own voice, the board shows every step, and you do the thinking — I never just hand over the answer. Come try a free lesson, and I'll meet your student right at their level.",
    "Welcome to the demo! This is Mr. Cadabra's Classroom — the very screen your student will learn on. Before we solve anything, let me show you around.",
    "This big space is my board. Every step of every problem gets drawn right here — the board leads, and my voice follows. Nothing ever happens only in words.",
    "See the bars up top? That's your student's map — today's goals, the current unit with a marker for every quiz, and the whole course marching gold toward the Final Exam. They always know exactly where they are.",
    "And this is me, Mr. Cadabra! In the real classroom we simply talk — your student says their answer out loud and we go back and forth like a real teacher and student. Here in the demo, you'll type or tap your answers instead.",
    "That's the classroom! Ready to try a real problem? Pick your student's level — anywhere from counting stars to differential equations — and I'll teach you the exact way I teach them.",
    "Entry-Level Math — where the adventure begins! We make numbers friendly with pictures you can count. Here's a real one from my classroom.",
    "Basic Math — fractions and decimals, the friendly way. Here's a real one from my classroom.",
    "Pre-Algebra — where negative numbers stop being scary. Here's a real one from my classroom.",
    "Algebra One — the mystery-number hunt! Let's solve a real two-step equation together, exactly like a lesson.",
    "Geometry — shapes, angles, and the most famous theorem in all of math. Here's a real one from my classroom.",
    "Algebra Two — exponents and quadratics, the real power tools. Here's a real one from my classroom.",
    "Trig and Pre-Calc — where everything flows from one beautiful circle. Here's a real one from my classroom.",
    "Probability and Statistics — teaching numbers to tell the truth. Here's a real one from my classroom.",
    "Calculus — the mathematics of change itself. Let's take your very first derivative together.",
    "Differential Equations — the equations that run the physical world. Let's classify one like a pro.",
    "Congratulations — you just worked a real problem, step by step, exactly the way your student will! In the full classroom we talk back and forth by voice, quizzes unlock new topics, and medals land in the trophy case. Come meet me for a free lesson — I'll start right at your student's level.",
    "Over here on the left is your Curriculum — everything in the course, laid out in nine units. Your student can open any unit and see exactly what's inside it, so the whole year is never a mystery.",
    "Right below it, the Course Assessment. Whenever they're ready, it finds their strengths and builds a recommended path just for them. It's completely optional, and it's always waiting right there.",
    "Next, the Progress dashboard. That's where they watch themselves win — units mastered, accuracy, streaks, and a trophy case for every award they earn.",
    "Then Practice a problem. When your student is stuck on one specific problem — homework, a worksheet, anything — they bring it here and we work through it together.",
    "Right under it, Explore a topic. Curious about just one thing, like fractions or slope? They open it, name the topic, and we dig into exactly that.",
    "And the Final Exam — the top of the mountain. It unlocks only after all nine units are mastered, and passing it makes them a Course Champion.",
    "Last one on the left: Look it up. Any time they just want to READ about something, they tap it, type the topic, and a page opens right on top of the lesson. Their place is waiting when they close it.",
    "Before we count anything, here's the trick: we touch each one and say the numbers in order. Watch me count these three stars — one… two… three. The last number you say is how many there are. Now you try with a new group!",
    "A fraction is just a number cut into equal pieces. Look at the bar on the board: it's cut into four equal pieces, so each piece is one fourth. Shade two of them and you have two fourths — which is exactly the same amount as one half. Now let's use that.",
    "Here's a number line. Zero sits in the middle, positive numbers run to the right, and negative numbers run to the left. Adding moves you to the right; subtracting moves you left. Watch: start at negative two, climb three steps right, and you land on positive one. Your turn next.",
    "Solving means getting x all by itself, and the one rule is: whatever you do to one side, you do to the other. Watch a quick one — x plus four equals ten. Subtract four from both sides, and x equals six. Now let's do a two-step one together.",
    "Every triangle's three angles add up to one hundred eighty degrees — always, no exceptions. Watch a friendly one: sixty plus sixty plus sixty is one hundred eighty. Now let's find a missing angle.",
    "An exponent just counts how many times you multiply. Two to the third means two times two times two, which is eight — each step doubles what you had. Now let's run that backwards.",
    "The unit circle measures turns two ways. A quarter turn is ninety degrees, and in radians we call that same quarter turn pi over two. Degrees and radians are just two rulers for the same angle. Now let's convert one.",
    "The mean is the fair-share average: add everything up, then split it evenly. Watch — two scores, four and eight. Together that's twelve, split between two people is six each. Now let's do three scores.",
    "The power rule is the first tool in calculus: bring the power down in front, then drop the power by one. Watch — x squared becomes two x. That's it, that's the whole move. Now you try it on a bigger one.",
    "Rule one in differential equations is: classify before you solve. The ORDER is simply the highest derivative in sight — count the tick marks. Watch: y triple-prime has three ticks, so that's third order. Now you classify one.",
    "And that's a real lesson! Now let me show you what the grown-ups see. There are three windows into your student's progress — theirs, a teacher's, and a parent's. Pick whichever one you'd like to look at, and I'll walk you through it.",
    "This is the student's own dashboard — the one they open to watch themselves win. Right up top: units mastered, how accurate they've been, problems practiced, and the day streak they're protecting.",
    "Below that is their course map — nine units, turning gold as each one is mastered, marching toward the Final Exam. It's the same map they see on the bars during a lesson, so their progress is never a mystery.",
    "And this is the trophy case. Every award is earned by real work — exploring a topic, practicing it, learning it, mastering the unit, and the effort medal for sticking with something hard. Nothing here is decoration.",
    "This is the teacher's view — the whole class on one screen. Each student's current unit, their accuracy, when they last worked, and a flag when someone needs a hand today.",
    "This column is the one teachers tell us they use most: what to strengthen next, for each student, in plain words. It comes from what actually went wrong in their lessons, not from a generic level number.",
    "And down here is my honest read on the class — where the group is solid, where several students are wobbling on the same idea, and what I'd teach next. A teacher can use it or overrule it; it's a colleague's opinion, not a verdict.",
    "This is the parent's view, and it answers the only question that really matters: how is my student actually doing? No jargon, no scores to decode — just an honest read in plain English.",
    "Here's the week at a glance — time spent, what they mastered, and what they struggled with. If your student had a rough day, you'll see it here, because a dashboard that only shows good news isn't worth having.",
    "And this button prints the whole record — every unit, every quiz, every hour — for a homeschool portfolio or a school district's file. It's your data; you can take it with you any time.",
    "Your turn. The board shows negative three plus five, and there's your number line right underneath it. Start three steps below zero, climb five steps to the right, and tell me where you land. Tap the microphone and say it out loud.",
    "Not quite — let's walk it together. Put your finger on negative three, then count five hops to the right: negative two, negative one, zero, one… and one more. Tap the mic and say where you land.",
    "Now a real one — it's on the board: two x plus three equals eleven. Our whole goal is to get x all by itself, so the first move is undoing that plus three. What should we do to BOTH sides? Tap the microphone and say your move.",
    "Close — the three is being ADDED, so we undo it with the opposite move. Tap the mic and tell me what to do to both sides.",
    "Look at the board now: two x equals eight. Two x means two TIMES x — so what undoes a times two? Tap the microphone and say your move.",
    "Careful — two x means two times x, so we undo it with division, not subtraction. Tap the mic and try that once more.",
    "Last step. The board says eight divided by two — so what does x equal? Tap the microphone and say the number.",
    "Almost — think of eight split into two equal groups. Tap the mic and say how many are in each group.",
    "Now look at the triangle on the board. Two of its angles are marked for you — ninety degrees and thirty-five degrees — and the third one has a question mark. All three together must add to one hundred eighty. Tap the microphone and tell me that missing angle.",
    "Let's build it up in two moves — first add the two angles you can see, ninety plus thirty-five. Then take that away from one hundred eighty. Tap the mic and say what's left.",
    "Here's the puzzle on the board: two to WHAT power makes thirty-two? Start at two and count how many times you double. Tap the microphone and say the power.",
    "Keep doubling out loud with me — two, four, eight, and so on. Count each step until you reach thirty-two, then tap the mic and say how many steps that took.",
    "Now look at the circle on the board. The arrow sweeps exactly HALF the way around, and half a turn is what we call pi radians. How many degrees is that half turn? Tap the microphone and say it.",
    "Think about the whole circle first — all the way around is three hundred sixty degrees. Our arrow goes exactly half that far. Tap the mic and say the number.",
    "Three quiz scores are on the board — three, five and ten — drawn as bars so you can see their sizes. The mean is the fair share: add them all up, then split the total evenly three ways. Tap the microphone and say the mean.",
    "Let's do it in two moves — first add three, five and ten together. Then split that total into three equal shares. Tap the mic and say what one share is.",
    "Your turn with the power rule. The board shows x CUBED. Bring the three down in front, then drop the power by one — what is the NEW power? Tap the microphone and say it.",
    "Just the second half of the rule: the old power is three, and we drop it by one. Tap the mic and say what that leaves.",
    "Now you classify one. The board shows y double-prime plus y equals zero. The order is simply the highest derivative in sight — count the tick marks on the busiest y. Tap the microphone and say that number.",
    "Look right at the y carrying the most tick marks — two of them means the SECOND derivative. Tap the mic and say that order as a number.",
    "This is Maya's own dashboard — the screen your student opens to watch themselves win. Right at the top, the numbers that matter: four units mastered, ninety-one percent accuracy, three hundred twelve problems worked, and an eleven-day streak she is very proud of.",
    "Here's her whole course, all nine units. The gold ones are mastered — she's finished Numbers, Fractions, Ratios and Percents. Unit five is where she's working right now, and the four ahead are still waiting. At the end sits the Final Exam, locked until every unit is gold.",
    "Open the unit she's in and you see the ladder inside it: every topic, every quiz, and the score she earned. Comparing decimals, eighty-eight percent. Adding and subtracting, ninety-two. Multiplying is where she is today, and the Unit Quiz waits at the top.",
    "These two charts are her habits. On the left, accuracy week by week — you can see the dip in week three when percents got hard, and the climb back after we slowed down. On the right, minutes per day this week. Honest pictures, both of them; a dashboard that only shows good news isn't worth having.",
    "And this is the trophy case — twelve awards, every one of them earned. Explored a topic. Practiced it. Learned it. Mastered a whole unit. The Course Champion medal from finishing Basic Math last spring. And the effort medal, which she got for coming back to percents four days in a row until they clicked.",
    "Last, what's coming: the exact next three sessions, so she never wonders what happens tomorrow. And down here, her courses — Basic Math finished and championed, Pre-Algebra in progress, with everything from her old course still on the record.",
    "Now the teacher's view. This is Room Twelve — six students in Pre-Algebra — and the top row is the class at a glance: average accuracy, how many are on track, how many need a hand today, and the hours the class put in this week.",
    "Here's the roster. Every student, the unit they're in, their accuracy, their streak, and when they last worked. Ben hasn't been in for four days and his accuracy is sliding — so he's flagged in red at the top of your attention, not buried on page three.",
    "This grid is the one that saves a teacher a whole planning period. Nine units across, six students down, and every square colored: mastered, in progress, or not started. In one glance you can see that the whole class stalled in the same place — Unit two, fractions.",
    "Then, in plain words, what to strengthen next for each student — and WHY. Not a level number, not a percentile. Ben is stalling on borrowing across a zero. Aiden can't find a common denominator yet. That's what actually went wrong in their lessons this week.",
    "And this is my honest read on the class. Where they're solid, where several of them are wobbling on the very same idea, and what I would teach next if it were my room. A teacher can take it or overrule it — it's a colleague's opinion, never a verdict.",
    "Down at the bottom: what's coming. Who has a Unit Quiz this week, who is close to their Final Exam, and the class time chart so a teacher can see who is quietly doing nothing.",
    "And now the view most parents care about. It opens with the only question that really matters — how is my student actually doing? — answered in plain English, with no jargon and no scores to decode.",
    "Here's her week: four days in, two hours and fifteen minutes, one unit mastered, and the thing she struggled with. We put the hard part right next to the good part on purpose. If your student had a rough week, this page will tell you so.",
    "This is the longer arc — every week since she started in September. Hours, accuracy, units mastered. You can watch her get better, and you can see exactly which week percents nearly beat her.",
    "Everything she has mastered, with the date and the quiz score that proved it. This is the list you'd want if anyone ever asks what your student has actually learned this year.",
    "And this is the part I'd read first: what's hard for her right now, and what we are doing about it. Lining up decimal points when the numbers have different lengths. My plan is smaller numbers and money problems until it feels ordinary — and I'll tell you here when it does.",
    "Finally, the record. Every unit, every quiz, every hour, printable in one click for a homeschool portfolio or a school district file. It's your data and your student's work — you can take it with you any time, and you never have to ask us for it.",
    "Look at the board — two fourths plus one more fourth. Count the shaded pieces and tap again!",
    "Your turn. The board shows negative three plus five, and there's your number line right underneath it. Start three steps below zero, climb five steps to the right, and type where you land.",
    "Not quite — let's walk it together. Put your finger on negative three, then count five hops to the right: negative two, negative one, zero, one… and one more. Type where you land.",
    "Now a real one — it's on the board: two x plus three equals eleven. Our whole goal is to get x all by itself, so the first move is undoing that plus three. What should we do to BOTH sides? Type your move.",
    "Close — the three is being ADDED, so we undo it with the opposite move. Type what you'd do to both sides.",
    "Look at the board now: two x equals eight. Two x means two TIMES x — so what undoes a times two? Type your move.",
    "Careful — two x means two times x, so we undo it with division, not subtraction. Try that once more.",
    "Last step. The board says eight divided by two — so what does x equal? Type the number.",
    "Almost — think of eight split into two equal groups. Type how many are in each group.",
    "Now look at the triangle on the board. Two of its angles are marked for you — ninety degrees and thirty-five degrees — and the third one has a question mark. All three together must add to one hundred eighty. Type that missing angle.",
    "Let's build it up in two moves — first add the two angles you can see, ninety plus thirty-five. Then take that away from one hundred eighty. Type what's left.",
    "Here's the puzzle on the board: two to WHAT power makes thirty-two? Start at two and count how many times you double, then type the power.",
    "Keep doubling with me — two, four, eight, and so on. Count each step until you reach thirty-two, then type how many steps that took.",
    "Now look at the circle on the board. The arrow sweeps exactly HALF the way around, and half a turn is what we call pi radians. How many degrees is that half turn? Type it in.",
    "Think about the whole circle first — all the way around is three hundred sixty degrees. Our arrow goes exactly half that far. Type the number.",
    "Three quiz scores are on the board — three, five and ten — drawn as bars so you can see their sizes. The mean is the fair share: add them all up, then split the total evenly three ways. Type the mean.",
    "Let's do it in two moves — first add three, five and ten together. Then split that total into three equal shares. Type what one share is.",
    "Your turn with the power rule. The board shows x CUBED. Bring the three down in front, then drop the power by one — what is the NEW power? Type it in.",
    "Just the second half of the rule: the old power is three, and we drop it by one. Type what that leaves.",
    "Now you classify one. The board shows y double-prime plus y equals zero. The order is simply the highest derivative in sight — count the tick marks on the busiest y, and type that number.",
    "Look right at the y carrying the most tick marks — two of them means the SECOND derivative. Type that order as a number.",
    "This is Maya's own dashboard — the real screen your student opens. These five numbers are exactly the ones the product tracks: units mastered, accuracy, problems practiced, time this week, and the day streak she's protecting.",
    "Below it, her course — all nine units. The gold ones are mastered, and mastered here means ninety percent or better on the Unit Quiz with no hints. Unit five is where she's working now, and the Final Exam at the end stays locked until every unit is gold.",
    "Open a unit and you see the quiz results inside it — every topic quiz, the score, and the date. This is the same detail a parent or a teacher sees, because there's only one set of numbers and everybody gets the truth.",
    "Strengthen next is my short list for her: the specific things that actually went wrong in her lessons this week. Not a level, not a percentile — the two habits I'd fix first.",
    "And the trophy case. Explored, practiced, learning, mastered, the effort medal, and the Course Champion medal she earned for finishing Basic Math. Every one of them comes from real work; none of them are participation stickers.",
    "Now the teacher's side. A teacher opens a class with its class code — this is Room Twelve — and every class they run sits in one place.",
    "Here's the class. One row per student, showing how many of the nine units they've mastered, how many they've started, and a star when a unit is finished. Nothing here is guessed; it's the same mastery record the student sees.",
    "The column that matters most is this one: needs attention. A student who has stalled, or whose scores are sliding, gets flagged here so they're the first thing a teacher sees instead of the last thing they find out.",
    "And a teacher can open any student to see their full dashboard, read-only — the same numbers, the same quiz history, the same short list of what to strengthen next. Adding a student is one box: their student code.",
    "And this is the parent's view. It's the same dashboard, opened with a parent's link — but it leads with the question a parent actually has: how is my student really doing, in plain English.",
    "That's my honest read. It names what she's good at, what she's stuck on, and what I'm doing about it. If your student had a hard week, this paragraph will say so — a report that only ever says 'great job' isn't worth reading.",
    "Underneath are the same five numbers her teacher and I see. One record, one set of facts, no separate parent version that quietly rounds things up.",
    "Strengthen next tells you exactly where she is wobbling right now — and because it comes from her actual lessons, it's specific enough to help with at the kitchen table.",
    "And this prints the whole record: every unit, every quiz, every hour, ready for a homeschool portfolio or a school district file. It's your student's work, and you can take it with you any time.",
    "Welcome — this is the parent's view of Mr. Cadabra's Classroom, using a made-up student so no real student's record is ever on display. In a moment I'll walk you through the dashboard you'd open: what your student has actually mastered, what they're working on right now, what's hard this week, and the printable record you can take with you. Everything you'll see comes from real work — we never invent a number to make a week look better than it was.",
    "Welcome — this is the teacher's view of Mr. Cadabra's Classroom, built from a made-up class so no real student is ever on display. I'll walk you through the roster, who needs you this week and why, the mastery picture across the whole class, and the time each student actually spent. Every number is earned: mastery means ninety percent or better on a unit quiz with no hints from me.",
    "Welcome — this is the homeschool view of Mr. Cadabra's Classroom, using a made-up student so no real student's record is ever on display. I'll show you the dashboard you'd open each week, and the part homeschool families ask about first: the printable record. Every unit, every quiz, every hour, dated and ready for a portfolio or a district file. It's your student's work and you can take it with you any time.",
    "Hi! This is your dashboard — the screen you'd open every time you come back. I'm using a made-up student called Maya so nobody's real work is on show. I'll walk you through your five numbers, your course map with the gold units you've mastered, what you're working on next, and the trophies you've earned. Everything here is stuff you actually did.",
    "This is the dashboard you'd open on a Monday morning. You are the teacher here, so it leads with the thing you actually need to know before you plan the week: how is this student really doing, in plain English, not a score out of ten.",
    "That's the honest read. It names what she has genuinely got, what she is stuck on, and what Mr. Cadabra is doing about it. If she had a rough week it will say so plainly — a record that only ever says 'great job' is no use to a parent who is also the teacher.",
    "These five numbers are the ones a homeschool week turns on: units mastered, accuracy, problems practised, time on task this week, and the day streak. The hours are measured engaged time, not a timer left running, because in most states the hours are the part you have to be able to stand behind.",
    "Strengthen next is your lesson plan for the week, already written. It comes from her actual work, so it is specific enough to sit down at the kitchen table with — not 'review fractions', but the exact step that is wobbling.",
    "And this is the one homeschool families ask about first. It prints the whole record — every unit, every quiz, every hour, dated — ready for a portfolio, an end-of-year review, or a district file. It is your student's work, and you can take it with you any time, whether or not you stay with us.",
    "And that's the parent's view. Every number on it was earned by a real piece of work — nothing on that screen is a guess, and nothing is rounded up to make a week look better than it was. If you'd like to see what your student actually does in a lesson, I can teach you one right now, at any level from counting to calculus.",
    "And that's the teacher's view. One room, every student, and no guessing about who needs you this week — the flags come from the work itself, not from a survey or a self-report. If you'd like to see what a lesson looks like from the student's side, I can teach you one right now, at any level you choose.",
    "And that's the homeschool view. The week in front of you and the record behind you, both ready whenever you need them, and both built from work your student actually did. If you'd like to see what a lesson looks like, I can teach you one right now, at any level from counting to calculus.",
    "And that's your dashboard! Every gold unit, every trophy, every number on it — you earned all of that yourself. Want to see what a real lesson is like? Pick any level you want and I'll teach you one right now, exactly the way I'd teach you for real.",
    "If you only have a minute, this box is the whole dashboard in four lines: what she has mastered, her streak, how accurate she is, and how many problems she has actually done. Underneath it, where to help next — and the link that prints her records.",
    "Here are her nine units. The gold ones are mastered, and every gold unit carries the date she proved it and the score she proved it with. Mastered means ninety percent or better on the Unit Quiz with no hints from me — so a gold unit is evidence, not encouragement.",
    "This is the same nine units drawn as a path, so you can see the shape of her year at a glance: four behind her, decimals under her feet right now, four still ahead. Beside it, the same thing counted up, with the hours she has actually put in since September.",
    "Her trophy case. A Course Champion medal for finishing Basic Math, a badge for every unit she has mastered, and an effort medal she earned for coming back four days running when percents beat her. None of these are participation stickers — every one came from recorded work.",
    "And her courses. She finished Basic Math and moved up, and one subscription covers every course we teach, so she moves on when she is ready rather than when a term ends. Beside it, the strengths her placement check found on the very first day.",
    "If Monday is busy, this box is your whole week in four lines — mastered, streak, accuracy, problems done — and then where to help next. The records link underneath it is the one that matters at filing time.",
    "Here are the nine units, and every mastered one carries a date and a score. That pairing is what turns a checkbox into evidence, which is exactly what an end-of-year review or a portfolio asks you for.",
    "The same nine units as a path, so you can see the whole year at a glance and plan against it. Beside it, the hours — measured engaged time since September, not a timer left running, because in most states the hours are the part you have to be able to stand behind.",
    "The trophy case does a job in a homeschool that is easy to underrate: it is the part your student can show somebody. A medal for finishing a whole course, a badge for every unit mastered, and one for effort — earned the week percents nearly beat her.",
    "And her courses. One subscription covers all ten, so a student who is ahead in one subject and behind in another is not a billing problem — she moves on when she is ready. Beside it, what her placement check found on the very first day.",
    "Three numbers first, and the third one is really a question. Six students, eighteen units mastered between them — and then the unit the class as a whole is struggling with. Here that's Unit 2, fractions, at a seventy-eight percent class average.",
    "This is the heatmap: every student down the side, every unit across the top, and the real score in each box. Read down a column and you find the wall — Unit 2, where Aiden and Ben both stopped. Read across a row and you get one student's whole story in a second.",
    "And this is my honest read on the class. Aiden isn't lazy — he's missing an idea underneath, he's treating a fraction as two separate whole numbers. Ben isn't stuck, he's stopped. And one you didn't ask about: Sofia is being under-served. She's ready for Algebra One now, and keeping her in step with the class is costing her a term.",
    "Strengthen next, one line per student, and every line names the broken rule rather than the wrong answer. Fixing an answer leaves the rule intact, and it fires again next week.",
    "And time on task — engaged time, not a tab left open. It is the fastest way to tell stuck apart from stopped, and those two need opposite responses from you.",
    "This is the part you can ask for any time: how am I doing, in plain words. It's written from your own work — what you're good at, what's hard right now, and what we're going to do about it.",
    "Your nine units drawn as a path, so you can see the whole year at once: four behind you, decimals right where you're standing, and four still ahead. Beside it, the same thing counted up, with every hour you've put in since September.",
    "And your next three sessions, already planned. Finish multiplying decimals, then dividing, then the Unit Five Quiz — ninety percent with no hints and Unit Five turns gold. And I won't offer you that quiz until you've got two right on your own first.",
    "Your courses. You finished Basic Math and moved up, and every course is included — so Algebra One opens the day you are ready for it, not when a term ends.",
    "These five numbers are yours: how many units you've mastered, how accurate you are, how many problems you've done, your time this week, and the day streak you're protecting. Every one of them comes from work you actually did.",
    "Below that is your whole course — all nine units. The gold ones you've mastered, and mastered means ninety percent or better on the Unit Quiz with no hints from me. Unit five is where you are right now, and the Final Exam stays locked until every unit is gold.",
    "Open a unit and you can see every quiz inside it — the score and the date. Your parents and your teacher see exactly this same page, because there is only one set of numbers and everybody gets the truth.",
    "Strengthen next is my short list for you: the specific things that went wrong in your lessons this week. Not a level, not a percentile — the two things I would fix first.",
    "And your trophy case. Explored, practiced, learning, mastered, the effort medal, and the Course Champion medal you earned for finishing Basic Math. Every one of them came from real work — none of them are participation stickers.",
    "Two charts here, and they are her habits. On the left, accuracy week by week — the dip is week eight, the week percents beat her, and the climb after it is four days of coming anyway. On the right, minutes a day this week, including the two days she did nothing. Honest pictures, both of them: a dashboard that only ever shows good news isn't worth having.",
    "These two charts are your habits. On the left, how accurate you were week by week — that dip is the week percents beat you, and the climb right after it is you coming back four days running. On the right, your minutes a day this week, days off included. I'd rather show you the truth than a flattering picture.",
    "Hello, and come on in — this is the parent's side of Mr. Cadabra's Classroom, shown with a made-up student named Maya so no real student's record is ever on display. Parents bring me the same two questions everywhere: is my student actually learning, and will she actually want to do this? Every panel on this screen answers one of those two — and every number on it comes from real work, because we never invent a good week.",
    "This is the dashboard you'd open at home, and it leads with the question you'd ask me at a parent-teacher conference: how is my student really doing? Not a score out of ten, not a percentile — an answer in plain English, written from the work she actually did.",
    "That's my honest read. It names what she's genuinely got, what she's stuck on, and what I'm doing about it — because I teach: out loud, one step at a time, and I never just hand her the answer. When this paragraph says she owns something, she earned it. And when she has a hard week, it says that too, plainly.",
    "These five numbers are the same five her teacher and I see — one record, one set of facts, nothing rounded up. And the day streak is my favorite of the five, because nobody can assign a streak: it only grows on days she opens the classroom herself, and a student protects a streak she built.",
    "Strengthen next tells you exactly where she's wobbling right now — specific enough to sit down with at the kitchen table. And a problem she misses doesn't just vanish into a percentage: a few days later I bring back a fresh one just like it, so a miss becomes a second chance instead of a quiet gap.",
    "Her trophy case — and this panel is my answer to the question 'will she actually use it?' The badges are earned, never given: a Course Champion medal for finishing Basic Math, a badge for every unit she's mastered, and an effort medal for coming back four days running the week percents beat her. This is why a student opens the classroom without being asked.",
    "And that's the parent's window. One more thing, because careful parents always ask: in a lesson your student talks with me out loud, her speech becomes text, and the audio is deleted right away — never stored — while I stay warmly on the math and nothing else. If you'd like to see how I actually teach, I can give you a real lesson right now, at any level from counting to calculus.",
    "Hi there! I'm Mr. Cadabra — and yes, I really talk, and I really listen. In a real lesson you just say your answer out loud, I hear you, and we work it out together on my board, step by step, at your speed. This is your dashboard — I'm using a made-up student called Maya so nobody's real work is on show — and I'll show you your five numbers, your course map with its gold units, and the trophy case you're going to fill. Everything on this screen is stuff you actually did.",
    "This is the part you can just ask me for, out loud, any time: how am I doing? And I'll tell you straight, in plain words — what you're good at, what's hard right now, and what we're going to do about it together. No mystery numbers, no report-card code: you always know exactly where you stand.",
    "And here it is — the trophy case. A badge for every unit you turn gold, an effort medal for the week you refused to give up, and the big one: a Course Champion medal for finishing a whole course. Nobody can give you these — not me, not anyone. The only way a trophy gets into this case is that you earned it, and that's exactly why it feels so good to open this page.",
    "And that's your dashboard, top to bottom! Every gold unit and every trophy on it, you'd earn yourself — I can't hand those out, and I wouldn't want to. Two promises before you go: I only ever talk about math — ask me about anything else and I'll smile and steer us straight back — and I never just give you the answer, because you getting it yourself is the whole fun. Want to see? Pick any level you like and I'll teach you a real lesson right now.",
    "Welcome! And let me say the most important thing first: I am not here to replace you. I'm a teaching assistant — the kind that gives every one of your students patient, one-on-one practice at their own pace, and then reports back to you. This is the teacher's view, built from a made-up class so no real student is ever on display, and every number in it is earned: mastery means ninety percent or better on a unit quiz with no hints from me. Your class stays yours — let me show you what I hand back.",
    "Now the teacher's side — and here is the right way to think of me: I'm the assistant who does what no teacher has thirty hours a day for, the patient one-on-one practice, while you do the teaching. A teacher opens a class with its class code — this is Room Twelve — and every class they run sits in one place.",
    "This column — needs attention — is me doing your triage: a student who has stalled, or whose scores are sliding, gets flagged before they get lost in the middle of a class. And the students pulling ahead surface too, in my honest read below — because no class learns at one speed, and with an assistant watching every student every day, you never have to teach as if it does.",
    "And you can open any student for their full dashboard, read-only — the same numbers, the same quiz history, the same short list of what to strengthen next. What happens with all of it is your call: I gather the picture, you make the teaching decisions. Adding a student is one box — their student code.",
    "And that's the teacher's side of the classroom. Notice what it doesn't do: it doesn't plan your lessons, grade your judgment, or run your room — it hands you what you can't get any other way, a patient assistant for every single student and an honest picture of exactly who needs you and who's ready to run ahead. If you'd like to see what your students would experience, I can teach you a lesson right now, at any level you choose.",
    "Before we finish — Abrabot, they are all yours. A couple of practice problems, and I will be right here.",
    "And see Extra practice — the one with the robot? That's Abrabot, my practice helper. Practice a problem is for a problem your student brings me; Abrabot is the other way round — he hands out more problems on lessons already done, as many as they want, always free, and he keeps count so your student can show you how hard they've worked. Stay to the end of the lesson and you'll meet him yourself — or tap his button any time.",
    "Next, the Progress dashboard — here is a corner of it. We will spend proper time in there after the lesson, when you can open all three views and click through them yourself.",
    "And see Extra practice — the one with the robot? That one is not mine at all. Let me introduce you.",
    "And these two bubbles at the top are the streak. The flame counts days in a row your student has worked; the star counts problems right in a row today. Small, honest numbers — and students watch them like a scoreboard.",
    "One more thing before you go. See Extra practice on the left? That is Abrabot — my teaching assistant. He is a robot, and proud of it. Any time you want more of a skill you already know, he has a box of problems that never runs out. He is the one to practise with; I am the one to learn with.",
    "And one thing that is not on this screen, because it never needs to be: the drilling. Extra practice belongs to Abrabot, my teaching assistant — a robot with a virtually unlimited box of problems on skills already taught. He handles the repetition, so your class time with me goes to the teaching, and yours goes to the five students who need you.",
    "Last thing. Extra practice is not me — it is Abrabot, my teaching assistant, a robot with a virtually unlimited box of problems on skills your student has already learned. There is no such thing as running out. Which means \"can I do more?\" is always a yes.",
    "Last thing, and it matters for a homeschool week: Extra practice is not me — it is Abrabot, my teaching assistant, a robot with a virtually unlimited box of problems on skills already taught. It never runs out. So the repetition your student needs is there whenever you have a spare ten minutes, without you writing a single worksheet.",
    "Next, the Progress dashboard. Here is a small look at it — how your student is doing, the streaks, the awards, the trophy case, all of it. We will come back and go through it properly after the lesson, when you can open all three views yourself."   # (rs) the miniature dashboard line, APPENDED
    ,
    "One more trick before we pick a problem. My board can be a white board or a dark one — this button right here. Watch: white... and back to dark. Choose whichever is easier on your eyes; I teach exactly the same on both."
    # (sc) ^ the board-choice line, APPENDED -- identical to demo.html
]


@app.get("/api/demo-audio/{idx}")
def demo_audio(idx: int, request: Request):
    """Serve one whitelisted demo line in the tutor's real voice (cached). 204 when the
    ElevenLabs key isn't configured -- the demo falls back to the browser voice."""
    _rate_limit("demoaudio:" + _client_ip(request), limit=60, window_seconds=300,
                what="demo audio requests")
    if idx < 0 or idx >= len(DEMO_VOICE_LINES):
        raise HTTPException(status_code=404, detail="Unknown demo line.")
    if not ELEVEN_API_KEY:
        return Response(status_code=204)
    return _tts_stream_response(DEMO_VOICE_LINES[idx], mode="demo")


def _script_closure_chars() -> dict:
    """BUILD me: {cache filename -> how many characters of text that clip speaks}.

    The companion to _script_closure_paths(): same walk, same model-sensitive key,
    but it keeps the LENGTH so a clip on disk can be weighed against its own text
    instead of against the course average. Memoised for the life of the process and
    invalidated by a scripted-model change, exactly as the path set is."""
    global _SCRIPT_CLOSURE_CHARS, _SCRIPT_CLOSURE_CHARS_MODEL
    if (_SCRIPT_CLOSURE_CHARS is not None
            and _SCRIPT_CLOSURE_CHARS_MODEL != SCRIPT_TTS_MODEL):
        _SCRIPT_CLOSURE_CHARS = None
    if _SCRIPT_CLOSURE_CHARS is None:
        _SCRIPT_CLOSURE_CHARS_MODEL = SCRIPT_TTS_MODEL
        out = {}
        try:
            # (mk) one owner -- the estimator and the guard must never disagree
            # about what the closure contains, or the projection drifts again.
            for say in _closure_lines():
                out[_tts_cache_path(say).name] = len(say)
        except Exception as exc:  # noqa: BLE001 -- degrade to the fallback estimate
            print(f"[speak] closure chars unavailable: {exc}")
            out = {}
        _SCRIPT_CLOSURE_CHARS = out
    return _SCRIPT_CLOSURE_CHARS


def _closure_render_status() -> dict:
    """(so, 2026-09-04) HOW MUCH OF THE CLOSURE IS ACTUALLY RENDERED. The prewarm is a
    manual /admin job, so every line added to the closure since it last ran -- qs's
    count-along lines, rj's seam line, sn's choice line -- is silence-or-browser-voice
    in production until Jim presses the button, and nothing said so. Jim heard exactly
    that on 09-04. This is the number the morning report prints beside a nudge to run
    the prewarm. Same closure, same cache path, as the prewarm itself uses. Never
    raises; an unreadable cache reports -1 rather than a comforting zero."""
    try:
        want = _script_closure_paths()
        have = {p.name for p in _TTS_CACHE_DIR.iterdir()} if _TTS_CACHE_DIR.exists() else set()
        missing = [n for n in want if n not in have]
        return {"total": len(want), "unrendered": len(missing)}
    except Exception as exc:  # noqa: BLE001
        print(f"[closure] render status failed: {exc}")
        return {"total": -1, "unrendered": -1}


def _script_closure_paths() -> set:
    """The cache filenames every scripted lesson can ever need.

    BUILD ke: computed once and memoised -- LESSONS is static for the life of the
    process, and this is ~4k sha256 hashes we should not redo on every eviction.
    Returns an empty set if lessonscripts cannot be read, which degrades this to the
    old behaviour rather than breaking eviction."""
    global _SCRIPT_CLOSURE_PATHS, _SCRIPT_CLOSURE_PATHS_MODEL
    # kf: the closure's PATHS depend on the model (it is in the cache key), so the memo
    # is invalidated if the scripted model changes. Env cannot change mid-process, but a
    # memo that silently protected the wrong files would be a nasty thing to debug later.
    if (_SCRIPT_CLOSURE_PATHS is not None
            and _SCRIPT_CLOSURE_PATHS_MODEL != SCRIPT_TTS_MODEL):
        _SCRIPT_CLOSURE_PATHS = None
    if _SCRIPT_CLOSURE_PATHS is None:
        _SCRIPT_CLOSURE_PATHS_MODEL = SCRIPT_TTS_MODEL
        paths = set()
        try:
            # (mk) one owner: a line this set misses is a line the evictor will
            # happily delete after the course has paid to render it.
            for say in _closure_lines():
                paths.add(_tts_cache_path(say).name)
        except Exception as exc:  # noqa: BLE001
            print(f"[speak] closure unavailable, eviction unprotected: {exc}")
            paths = set()
        _SCRIPT_CLOSURE_PATHS = paths
    return _SCRIPT_CLOSURE_PATHS


_SCRIPT_CLOSURE_PATHS = None
_SCRIPT_CLOSURE_PATHS_MODEL = None
_SCRIPT_CLOSURE_CHARS = None            # build me: {cache name -> chars of its text}
_SCRIPT_CLOSURE_CHARS_MODEL = None


def _evict_tts_cache() -> None:
    """Keep the TTS cache under _TTS_CACHE_MAX_BYTES, spending the GENERATED-lane clips
    before any line the scripted course needs.

    BUILD ke -- why the order matters. This used to delete oldest-first across the whole
    cache. Right after a whole-course prewarm the oldest clips ARE the course, in lesson
    order, so the first thing evicted was lesson one -- Counting to 10. That quietly
    undid the prewarm Jim had just paid for and put the scripted lane back on the
    streaming path (which is where the slurring lived). Scripted lines are now evicted
    only if culling everything else still leaves us over the cap, and we say so loudly
    when that happens, because at that point the cap is genuinely too small and that is
    a decision for Jim, not something to paper over."""
    try:
        files = [f for f in _TTS_CACHE_DIR.iterdir() if f.suffix == ".mp3"]
        total = sum(f.stat().st_size for f in files)
        if total <= _TTS_CACHE_MAX_BYTES:
            return
        protected = _script_closure_paths()
        # BUILD me (2026-08-23) -- THE 80% TARGET COULD NOT SEE THE COURSE.
        # The old target was a flat 80% of the cap. That is a fine anti-thrash
        # rule and a terrible floor: with the cap at 4,500 MB the target was
        # 3,600 MB, while the scripted closure is 3,738 MB. So the FIRST time
        # anything tipped the cache over the cap, this evicted every generated
        # clip, found itself still above target, and started deleting COURSE
        # audio that Jim had paid to render -- putting those lessons back on
        # the streaming path, which is where build ke's slurring lived.
        # The target now never falls below what the protected course actually
        # occupies (plus a small margin so we do not re-enter immediately).
        # If the course alone will not fit under the cap, the warning below
        # still fires and the decision is Jim's, exactly as before.
        protected_bytes = 0
        for f in files:
            if f.name in protected:
                try:
                    protected_bytes += f.stat().st_size
                except Exception:  # noqa: BLE001 -- already gone
                    pass
        floor = protected_bytes + _TTS_EVICT_MARGIN_BYTES
        target = max(int(_TTS_CACHE_MAX_BYTES * 0.8), min(floor, int(_TTS_CACHE_MAX_BYTES)))
        spare = sorted((f for f in files if f.name not in protected),
                       key=lambda f: f.stat().st_mtime)      # oldest first
        keep = sorted((f for f in files if f.name in protected),
                      key=lambda f: f.stat().st_mtime)
        freed = 0
        for f in spare + keep:              # generated lane first, course last
            if total <= target:
                break
            try:
                size = f.stat().st_size
            except Exception:  # noqa: BLE001 -- already gone
                continue
            if f.name in protected and freed == 0:
                print(f"[speak] WARNING: cache cap {_TTS_CACHE_MAX_BYTES} bytes cannot hold "
                      f"the scripted course ({total} bytes in use). Evicting course audio "
                      f"-- raise the cap or the course will keep re-rendering.")
            f.unlink(missing_ok=True)
            total -= size
            freed += size
        print(f"[speak] cache evicted down to {total} bytes")
    except Exception as exc:  # noqa: BLE001
        print(f"[speak] cache evict error: {exc}")


# Speech-to-text engines (Scribe/Whisper-family) HALLUCINATE non-speech captions on silence
# or background noise -- things like "[outro jingle]", "[music]", "(applause)", "* silence *",
# or musical notes. If one of those slips through as if the student "said" it, the tutor can
# mistake it for a real cue (e.g. "[outro jingle]" once made Mr. Cadabra wrap up a whole topic
# after one question). So we scrub bracketed/parenthesized non-speech captions, and if nothing
# real remains, return "" -- which the UI treats as "I didn't catch that, try again."
# build gr (2026-08-17): the language hint for speech-to-text. Empty string = let
# ElevenLabs auto-detect (the old behaviour, which heard an English "c" as Spanish "si").
STT_LANGUAGE = os.environ.get("STT_LANGUAGE", "eng").strip()

# THE SPOKEN LETTER (build gr). When a child says a single letter aloud, every engine on
# earth returns the WORD that sounds like it -- "see" for c, "bee" for b, "ex" for x. Jim's
# came back as the Spanish "si". This maps the name of a letter back to the letter, and it
# is deliberately applied ONLY when the whole utterance is that one word, because "see" in
# a sentence is a verb and "a" is an article. A short standalone word, spoken in answer to
# a question, is the letter.
# NOT included on purpose: "oh" (o), "eye"/"I" (i), "you" (u), "are" (r) and "why" (y) --
# each is a plausible whole utterance from a child in its own right ("oh!", "you?"), and
# turning an interjection into a variable would invent an answer they never gave, which is
# the very thing rule 64 forbids.
_SPOKEN_LETTER = {
    "see": "c", "sea": "c", "cee": "c", "si": "c", "s\u00ed": "c", "csi": "c",
    "bee": "b", "be": "b", "dee": "d", "ee": "e", "eff": "f", "gee": "g",
    "jay": "j", "kay": "k", "el": "l", "ell": "l", "em": "m", "en": "n",
    "pee": "p", "cue": "q", "queue": "q", "ess": "s", "tee": "t", "tea": "t",
    "vee": "v", "zee": "z", "zed": "z", "ex": "x", "eks": "x",
}


def spoken_letter(text: str) -> str:
    """The letter a one-word utterance names, or "". Never raises."""
    try:
        t = re.sub(r"[^A-Za-z\u00c0-\u017f]", "", str(text or "")).strip().lower()
        if not t:
            return ""
        if len(t) == 1 and t.isalpha():
            return t                       # already a bare letter
        return _SPOKEN_LETTER.get(t, "")
    except Exception:  # noqa: BLE001
        return ""


def _clean_transcript(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return ""
    # Remove [ ... ] / ( ... ) caption blocks (STT non-speech annotations) and musical notes.
    scrubbed = re.sub(r"[\[\(][^\]\)]{0,60}[\]\)]", " ", t)
    scrubbed = scrubbed.replace("♪", " ").replace("♫", " ").replace("*", " ").strip()
    # If what's left has no letters or digits, it was pure annotation/noise -> treat as silence.
    if not re.search(r"[A-Za-z0-9]", scrubbed):
        return ""
    return scrubbed


@app.post("/api/transcribe")
async def transcribe(audio: UploadFile = File(...), code: str = "", expect: str = "",
                     x_student_code: str = Header(default="", alias="X-Student-Code")):
    """
    Transcribe the student's recorded audio with ElevenLabs Speech-to-Text (Scribe).
    Browser records the audio (works in every modern browser) and posts it here;
    we return {"text": "..."}. Returns empty text on any failure so the UI can ask
    the student to try again. Reuses ELEVENLABS_API_KEY. Non-speech hallucinations
    (e.g. "[outro jingle]") are scrubbed via _clean_transcript so they never reach the tutor.

    LOCKED DOWN (2026-07-30): requires a valid student code (?code=) + rate limited --
    this endpoint spends real ElevenLabs money. 2026-08-07: voice input is LIVE on ALL
    THREE teaching pages (session + practice + topic; session got it 2026-08-06) -- the
    tap-to-talk button posts here for the typing courses on capable browsers; elementary
    tap-to-answer courses don't use it. TRANSCRIBE-AND-DELETE: the audio lives only in
    memory in this request, goes to ElevenLabs for transcription, and is discarded when
    the request ends -- never written to disk, never stored, only the text survives.
    """
    # build hs: the code prefers the X-Student-Code header (mic.js sends it that
    # way now); the query form remains for stale cached pages.
    code = (x_student_code or code or "").strip()
    _require_student(code)
    _rate_limit("stt:" + code.strip(), limit=20, window_seconds=300, what="voice uploads")
    if not ELEVEN_API_KEY:
        return {"text": "", "error": "no_key"}
    try:
        # SECURITY (build ec, 2026-08-12 -- finding F5): read at most MAX_AUDIO_BYTES + 1
        # so a giant upload can't be pulled whole into memory. A few seconds of student
        # speech is well under a megabyte; the cap (default 12 MB, env-tunable) is roomy
        # for a long answer yet closes the memory/cost hole. Over the cap -> a clean 413.
        content = await audio.read(MAX_AUDIO_BYTES + 1)
        if len(content) > MAX_AUDIO_BYTES:
            raise HTTPException(status_code=413, detail=(
                "That recording is too large — try a shorter answer, "
                "or type it instead."))
        if not content:
            return {"text": ""}
        files = {"file": (audio.filename or "speech.webm", content,
                          audio.content_type or "audio/webm")}
        # 2026-08-17 (build gr, Jim live in Geometry): he was asked which side was the
        # hypotenuse, said the letter "c", and Scribe transcribed it as the SPANISH "si"
        # / "CSI". The tutor then told him he was wrong and demanded a letter -- a student
        # marked incorrect for a machine's mistake, which is about the most corrosive thing
        # this app can do to a child's confidence.
        # We were sending NO language hint at all, so auto-detection was free to hear a
        # single English letter as another language. `language_code` is a documented
        # optional parameter (ISO 639-1 or 639-3). Env-tunable, and blank disables it.
        payload = {"model_id": ELEVEN_STT_MODEL}
        if STT_LANGUAGE:
            payload["language_code"] = STT_LANGUAGE
        with httpx.Client(timeout=60.0) as client:
            r = client.post(
                "https://api.elevenlabs.io/v1/speech-to-text",
                headers={"xi-api-key": ELEVEN_API_KEY},
                data=payload,
                files=files,
            )
            # A LANGUAGE HINT MUST NEVER COST US VOICE INPUT. If the parameter is ever
            # rejected, retry once without it: a slightly worse transcript beats a student
            # whose microphone silently stopped working.
            if r.status_code == 422 and "language_code" in payload:
                print(f"[transcribe] language_code={STT_LANGUAGE!r} rejected -- retrying "
                      f"without the hint")
                r = client.post(
                    "https://api.elevenlabs.io/v1/speech-to-text",
                    headers={"xi-api-key": ELEVEN_API_KEY},
                    data={"model_id": ELEVEN_STT_MODEL},
                    files=files,
                )
        if r.status_code != 200:
            print(f"[transcribe] ElevenLabs {r.status_code}: {r.text[:200]}")
            return {"text": ""}
        said = _clean_transcript((r.json() or {}).get("text", ""))
        # THE SPOKEN LETTER (build gr). The page sets expect=letter only when the tutor's
        # last line actually asked for one, so the context does the disambiguating and a
        # "see" inside ordinary speech is never touched. Note what this is and is not: it
        # corrects OUR transcription of what the student said -- it does not trade their
        # answer for a different one, which rule 64 forbids and which is precisely what the
        # tutor did to Jim when it heard "minus five" and taught on with 5.
        if expect.strip().lower() == "letter":
            letter = spoken_letter(said)
            if letter and letter != said.strip().lower():
                print(f"[sttletter] heard {said!r} where a letter was expected -> {letter!r}")
                return {"text": letter, "heard": said}
        return {"text": said}
    except HTTPException:
        # The 413 "too large" refusal (build ec) is a real answer -- it must reach the
        # caller, not be swallowed by the catch-all below that turns errors into "".
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"[transcribe] error: {exc}")
        return {"text": ""}


# NOTE (2026-08-09, build bz): /api/demo-transcribe was removed when the demo dropped
# voice answering (Jim). It lived here, was IP rate limited, and used the same
# transcribe-and-delete path as /api/transcribe -- see git history if the demo ever
# speaks again. Nothing calls it today, and an unused endpoint that spends
# ElevenLabs money is a surface we do not need open.


# Serve the static folder (css/js/images if we add them) under /static.
# (ud) the owner's tools under static/ answer 404 to the public -- see _OwnerGatedStatic.
app.mount("/static", _OwnerGatedStatic(directory=str(STATIC_DIR)), name="static")


# I did no harm and this file is not truncated.
