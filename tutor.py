# =============================================================================
# tutor.py  --  Math Tutor MVP  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-16  BUILD gl -- THE TUTOR MAY NOT BE SEEN CHANGING ITS MIND (eleventh referee).
#               The one HIGH finding of the 2026-08-16 audits: "3/4 is smaller than 3/4...
#               wait, let's just confirm..." -- a false comparison, then the grown-up
#               visibly losing faith in their own sentence, all shipped to a child. The
#               ACCURACY block always said "fix it BEFORE you say it"; nothing checked that
#               the fixing happened in PRIVATE. Every course now also says "fix it SILENTLY"
#               and this referee enforces it. Narrow on purpose: correcting the STUDENT is
#               the job ("actually comes out to 3.45" passes); only the tutor retracting
#               itself is caught.
#   2026-08-16  BUILD gk -- A FRACTION IS ONLY "READ ALOUD" WHEN ITS HALVES ARE SAID
#               TOGETHER. _pq_spoken_covers looked for the numerator anywhere and the
#               denominator anywhere, independently, so the 2026-08-16 fractions audit
#               walked through rule 44 untouched: board "3/4 + 1/4 = ?", words "three plus
#               one really is four" -- about the NUMERATORS, never reading the problem --
#               and the referee scored it as spoken because a "three" and a "four" existed
#               somewhere. A confused nine-year-old was then asked a question they had only
#               ever seen written. Now the two halves must be adjacent ("three fourths",
#               "three over four", or the literal 3/4), which is the only form a listening
#               student actually hears.
#   2026-08-14  BUILD gj -- RULE 41 IS NOW A REFEREE (the tenth check). The 2026-08-16
#               lesson audits found FOUR figures drawn with no caption -- a fractions pie
#               and three cookie pictures -- in the two lessons aimed at the youngest and
#               most confused students. Rule 41 is written absolutely ("use it, every
#               time") and nothing enforced it. This is the cheapest referee there is: no
#               model call to detect, no judgement, no argument -- a figure either carries
#               a caption or it does not. All 306 canonical scripts already pass, so it
#               never fights authored content; it only catches what the model improvises.
#   2026-08-14  BUILD gf -- FILTERING IS NOT OPTIONAL (ruletests caught it). Build gb filters
#               the foundation block to the lesson's unit, but when NO unit could be
#               determined -- an unplaced student, or a practice problem the classifier
#               cannot place -- it filtered nothing, and algebra2 came out at 185,595
#               characters against the 180,000 ceiling. Every gb measurement passed an
#               explicit unit, so every gb measurement missed it. There is now a fallback:
#               a student with no placement is at the START of the course, so unit 1;
#               practice and topic prefer the student's own placed unit first.
#   2026-08-14  BUILD gd -- THE MISSING-MARK PROBE (measurement only, no behaviour change).
#               [[mark]] records that a student FINISHED a problem: their score, their
#               accuracy, and since build fy the signal that folds the finished problem off
#               the board. The prompt calls it REQUIRED in all ten courses and ruletests
#               checks that the PROMPT SAYS SO -- but nothing has ever checked that the tutor
#               emits one. Jim's 2026-08-14 Render log: an Algebra I lesson posted /api/mark
#               three times; a Geometry lesson posted it ZERO times after handing the student
#               "130 + ? = 180", hearing "fifty", and answering "exactly right".
#               This prints [markcheck] when the previous turn left a pending "?" line, the
#               student answered, and this reply settles it while recording neither [[mark]]
#               nor [[nice]]. It does NOT regenerate and does NOT award the mark itself -- a
#               net that guessed would inflate a child's recorded accuracy, and retired
#               ensure_board is the standing lesson about nets that guess. Measure first.
#   2026-08-14  BUILD gb -- THE FOUNDATION BLOCK IS NOW FILTERED TO THE LESSON'S UNIT.
#               _foundation_block() gains unit= and passes it to foundations.prompt_block;
#               build_system_prompt hands it the unit it already computed for the playbook,
#               and the practice/topic builders hand it the unit they classify from the
#               problem/topic text. Scripts from other units are NAMED, not quoted. This is
#               what makes room for the ~120 foundation terms still owed on the other nine
#               courses. Backward compatible in both directions: unit=None filters nothing,
#               and an older foundations.py without the argument falls through the existing
#               TypeError path and teaches unfiltered.
#   2026-08-13  BUILD fe -- THE TRIANGLE-SLOT REFEREE (rule 63c, born ENFORCED). From
#               the 2026-08-13 lesson audit's HIGH geometry finding: sides="6,?,10"
#               with right="C" puts 6 in the hypotenuse's slot (sides= is AB, BC, CA;
#               the hypotenuse skips the right-angle vertex, so right="C" -> AB, the
#               FIRST slot) while the words said the hypotenuse was 10. Three of four
#               triangles in one lesson were mis-slotted. New triangle_side_conflict()
#               fires only on the geometric impossibility -- a numeric hypotenuse slot
#               with some other numeric side >= it -- and joins the prose_board_conflict
#               sweep after board_notation_conflict. "?" hypotenuses, algebraic sides,
#               and right= values that name no vertex are never judged (fail open,
#               like every referee). ruletests: TRIANGLE_CASES in PART 2 + PART 3ah.
#   2026-08-12  BUILD eq -- TWO MECHANICAL GUARDS from the 2026-08-12 audits.
#               (1) NEW malformed_tag_conflict, and it runs FIRST in the sweep: nothing
#               in eight referees checked whether a tag was even well-formed. The audit
#               caught [[choices options="yes, let's go! | show me one more]] -- no
#               closing quote -- which the page renders as ONE answer button reading
#               '"yes,' with the second choice simply absent. Silent, student-visible
#               breakage with no guard. Fires only on provable damage: unbalanced
#               quotes, an unterminated attribute, or a tag never closed.
#               (2) prose_unspoken_problem_conflict (rule 44) had TWO blind spots that
#               six findings in five lessons walked straight through. It required TWO
#               numeric tokens, and a fraction counts as ONE by design -- so an entire
#               quiz of "8/12 = ?" and "6/9 = ?" was invisible to it while the tutor
#               said only "what's this fraction reduced to lowest terms?". And ANY
#               number anywhere in the prose exempted the whole reply, so "two numbers
#               that multiply to 10 and add to 7" excused never reading the equation
#               aloud. Now: ONE stated quantity is enough to be worth reading, the line
#               must actually pose something (an operator or a fraction, not a label),
#               and the test is whether the words carry THIS problem's numbers --
#               numerals or the words a person says, with "eight twelfths" counting for
#               both halves of 8/12. Verified against the real audit lines: the three
#               caught, the innocent ones untouched.
#   2026-08-11  BUILD do -- THE WORDS MOVED TO prompts.py. This file had grown to
#               539 KB and two thirds of it was TEXT, not code: the eleven course/mode
#               system-prompt templates, GROUND_RULES, the shared teaching-rules block
#               (GRAPH_TOOL_NOTE), the session/progress/final-exam overlays, the
#               per-course practice+topic scopes, and the two assessment voices. All
#               of it now lives in prompts.py, moved VERBATIM (extracted by line
#               range, never retyped) and PROVEN byte-identical: 52 built prompts --
#               every course x lesson/first-meeting/practice/topic, plus final
#               prep/exam, focus-unit, and the standalone constants -- hashed before
#               and after the split, 52 of 52 equal. Nothing the model reads changed
#               by one byte. This file keeps the ENGINE: API calls, the negotiated
#               continuation, mathcheck, the nine-referee prose sweep, and the
#               build_* functions that assemble prompts.py's text per request. The
#               import (just below the model constants) re-exports every moved name,
#               so tutor.<NAME> works exactly as before. WHERE TO EDIT NOW: the
#               WORDS (rules, templates, scopes) -> prompts.py; the MACHINERY
#               (referees, pipeline, builders) -> here. BOARD_TAG_SYSTEM stayed: it
#               belongs to the (parked) whiteboard safety net beside its own code.
#               The change notes BELOW this line predate the split -- where an old
#               note says a rule or template text lives "in this file", read
#               prompts.py; the history itself is untouched.
#   2026-08-11  BUILD dl -- THE TWO STRONGEST REMAINING EVIDENCE GAPS, CLOSED AS RULES
#               (Teaching_Evidence_Base gaps 2 and 3, both WWC Strong; the Forward
#               Plan's queue item 3).
#               NEW RULE 53 -- THE NUMBER LINE IS A TOOL YOU USE ON PURPOSE: magnitude
#               and comparison (two numbers on one line settles size arguments),
#               fractions introduced BETWEEN 0 and 1 against the 0 / 1/2 / 1
#               benchmarks and then deliberately extended past 1, equivalent fractions
#               (and the decimal and percent costumes of the same value) at ONE
#               position with their names in the caption. Written against what
#               [[numberline]] can actually draw today (points, open circles, ineq --
#               no point labels), so the rule never asks for an undrawable picture.
#               NEW RULE 54 -- A WORD PROBLEM HAS A TYPE: name it (Change, Equal
#               Groups, Compare; part-whole/rate/proportion upstairs) BEFORE any
#               arithmetic, schema on the board, the equation comes FROM the schema.
#               54(b) BANS teaching key-word rules -- the WWC guide's own warning --
#               and is ENFORCED from day one: board_notation_conflict also catches
#               "altogether always means add" (prose or board), with the vocabulary
#               distinction honoured: "sum means add" is a DEFINITION (rule 37), not a
#               shortcut; the banned list is story-cue words only.
#   2026-08-11  BUILD dk -- BATCH E: the audit RE-RUN's six small accuracy fixes
#               (Audit_Findings_2026-08-11.md, PART 9; the re-run scored 30->17
#               findings, 10->2 high, 6->0 stumbles -- these close most of what
#               remained). In THIS file:
#               - rule 48(e): when the student SAYS a symbol wrongly ("f BRACKET x"),
#                 affirm the idea and hand back the right words in the same breath --
#                 in a voice classroom a wrong reading you let stand is one you taught;
#               - rule 52(d): a request to COMPUTE is not a rule-52 question -- coach
#                 the work as always; rule 52 is about questions ABOUT the mathematics
#                 (the critic misapplied our own new rule; now neither model nor critic
#                 can);
#               - NEW deterministic referee board_notation_conflict (EIGHTH check in
#                 prose_board_conflict): "$50 + 10% = $55" (a bare percent added to a
#                 plain quantity and COMPLETED -- invisible to mathcheck, $ and % are
#                 not sympy) and "a^2 + 64 = 100 = ?" (a chained equals ending in "= ?"
#                 after a bare number). Both quoted from real re-run boards; the legal
#                 shapes (the "of" form, percent-with-percent, conversions, pending
#                 lines, worked chains ending in a number) are FALSE fixtures. Rule 27
#                 moves COVERED -> ENFORCED for the percent shape.
#               Elsewhere in dk: math-figures.js drops any labeled point sitting on a
#               declared hole; notation.py gains the fraction-slash bridge for the four
#               lower courses ("the number AFTER the slash is the denominator -- the
#               BOTTOM number when written stacked").
#   2026-08-11  BUILD di -- BATCH D: the board tools the audit proved missing. The
#               shared block gains ONE tool note (reaches all ten courses; PART 3r
#               checks it): [[graph]] pieces may carry a domain with "for"
#               (func="x+1 for x<2; x+4 for x>=2") -- clipped, with the boundary marked
#               automatically, OPEN circle for strict, CLOSED dot for inclusive (S-4:
#               the audit's jump was two full parallel lines under a caption claiming a
#               jump); and [[column align="last"]] draws the DELIBERATELY-WRONG
#               last-digit lineup, amber + badged, for contrast teaching (S-9) -- never
#               with result=, always followed by the correct lineup. Renderer work in
#               math-figures.js and the three teaching pages; prompt cost ~1.4k chars.
#   2026-08-11  BUILD dh -- THE AUDIT'S TEACHING FINDINGS BECOME RULES AND REFEREES
#               (Batches B + C of Audit_Findings_2026-08-11.md; build dg was Batch A).
#               PROMPT (shared block, all ten courses; budget checked):
#                 rule 13 gains THE FALSE-CRITERION TRAP (S-11/S-3: "a different number
#                   pops out", "denominator zero so there's a hole" -- an example
#                   hardened into a wrong definition);
#                 rule 14: a figure's OWN labels are notation too (S-12, the [[machine]]
#                   box showing 2x+1 to a nine-year-old);
#                 rule 15: "= ?" is never a missing right-hand side -- an equation to
#                   solve is written "= 0" whole (S-16);
#                 rule 17: THE BOARD IS PART OF THE SAME BREATH -- never ask what a board
#                   line already answers (S-2);
#                 rule 18(a): "close" is a measurement, not a comfort (S-7);
#                 rule 43: never credit work that did not happen (S-15);
#                 rule 47(d): the instrument is part of the honesty -- "Unit Quiz" may
#                   only introduce the ten-question unit-wide instrument (S-10);
#                 rule 51(e): UNDEFINED IS NOT YET A HOLE -- classify only after the
#                   cancellation or the blow-up is shown (S-3);
#                 NEW RULE 52: a direct mathematical question is answered before
#                   anything else happens (S-5 -- the ignored "is that because it
#                   simplifies to x + 2?" conjecture).
#               REFEREES (both NARROW, both fail open, both swept clean against all 186
#               foundation scripts and all 227 demo lines before ship):
#                 prose_answered_question_conflict -- rule 17 COVERED -> ENFORCED: the
#                   prose asks "what's A op B?" while a board tag in the SAME reply
#                   states A op B = C with numeric C (commutativity honoured; a pending
#                   "= ?" line never trips it; offers excluded the build-dg way);
#                 prose_unspoken_problem_conflict -- rule 44 COVERED -> ENFORCED: a
#                   pending or Q-numbered board problem carrying two or more numbers
#                   while the ENTIRE spoken prose asks its question with no number in
#                   any spelling (one spoken number anywhere = silent, by design).
#               prose_board_conflict is now SEVEN checks. Tiers after dh:
#               16 enforced · 10 exercised · 25 covered · 1 unverified.
#   2026-08-11  BUILD dg -- RELIABILITY: THE AUDIT'S STUMBLES WERE OURS, NOT RATE LIMITS.
#               The first full audit's Render logs (Audit_Findings_2026-08-11.md, PART 5)
#               named the mechanisms; all are fixed here.
#               (1) THE REFEREE CRIED WOLF. prose_pending_question_conflict counted the
#               pronoun "one" as a number ("Want to try ONE yourself, or see ONE more
#               worked example?" read as two-number arithmetic) and had no concept of an
#               OFFER, so it killed good drafts a dozen times in forty minutes of audit
#               traffic -- and one geometry lesson shipped WITHOUT its worked example
#               because the drafts that contained it kept being discarded, and the third
#               draft wrote as if the student had seen them. Offers and look-questions
#               are now excluded (both rule-15 and rule-39(b) referees), "one" counts as
#               a number only in arithmetic company, the sentence splitter no longer
#               merges a quote-ended sentence into the question after it, and every
#               misfire quoted in the logs is a permanent ruletests case.
#               (2) BOTH REGENERATION NUDGES now order the rewrite to STAND ALONE -- a
#               regenerated draft must re-carry everything the student needs (worked
#               example, definition, board lines) and never pick up mid-thought from a
#               draft the student never saw.
#               (3) _create_full: claude-sonnet-5 intermittently REJECTS assistant-prefill
#               continuation (400: "does not support assistant message prefill"), and
#               each rejection surfaced as a stumble the student watches. Continuation is
#               now NEGOTIATED like the build-cz token parameter: prefill first, and on
#               that named 400 a user-message continuation nudge, remembered for the rest
#               of the process. Ceiling 1600 -> 3000 (MAX_REPLY_TOKENS): the logs show
#               tag-heavy teaching turns hitting 1600 constantly, and five replies
#               shipped as admitted "stitched partials" in forty minutes. A ceiling is
#               not a target -- normal turns end far under it and cost nothing extra.
#               (4) _create_verified retries ONCE, silently, on an empty reply before the
#               student ever hears "I lost my train of thought" -- the audit counted that
#               apology 6 times in 10 lessons.
#   2026-08-11  BUILD de -- the DIFFEQ course arc restructured to the CUPM mainstream
#               syllabus (Jim: "the one most acceptable to most schools"). Qualitative
#               analysis and numerical methods become units 3-4; systems get two units;
#               old 6-7 merge; exact equations shrink to a topic; series solutions drop.
#               Only the NINE UNITS block changed -- every teaching rule is untouched.
#   2026-08-10  BUILD cy -- THE FIFTH REFEREE: prose_self_answer_conflict(), and rule
#               39(b) moves from COVERED to ENFORCED.
#               Source: the MAA Instructional Practices Guide (CP.1.2, wait time).
#               Teachers wait under 1.5 seconds before answering their own question; the
#               evidence says wait seven; the first benefit listed is fewer "I don't know"
#               responses -- the exact thing Jim keeps meeting. The guide's vignette is an
#               instructor asking eight questions and answering all eight himself.
#               NARROW, because every false positive costs a real model call. It fires
#               only when the reply asks something ANSWERABLE and then states a number the
#               QUESTION DID NOT ALREADY CONTAIN. That last clause was not in the first
#               version and had to be: sweeping our own 227 demo lines found "two to WHAT
#               power makes thirty-two? Start at two and count how many times you double"
#               -- a HINT restating the question's own number, and never the answer. A
#               referee that cannot tell a hint from an answer punishes good teaching.
#               Swept clean afterwards against all 182 foundation scripts (all of which
#               are shaped "What is a numerator? The numerator is...") and all 227 demo
#               lines. Fails open, like every other referee.
#   2026-08-10  BUILD cv -- RULE 51 (a feature on the board must belong to the function)
#               and the [[graph]] window doc. Jim, reading a limits lesson: "it doesn't
#               say WHY there is no value at x = 2... and it completely ignores the graph
#               that continues to the right after x = 2." Both true. y = x^2 has no hole
#               at 2 -- f(2) = 4 -- so a hole painted onto it is an assertion, and a hole
#               is never an assertion: it is a CONSEQUENCE OF A DEFINITION, nearly always
#               a factor that cancels. 51(c) also fixes the second half: a hole does not
#               end the graph, and an approach must be narrated on BOTH sides.
#               THE WINDOW DOC WAS BROKEN TOO. It said range="-1,5" and the renderer's
#               parseRange only accepted "a..b", so the window was silently discarded --
#               and this doc exists because of Jim's EARLIER catch about a bad window,
#               which means that fix never worked. Doc now leads with "-1..5";
#               math-figures.js accepts both; ruletests checks every range= we write
#               against the renderer's own regex.
#   2026-08-10  BUILD cu -- QUIZ LENGTHS, AND RULE 50 (chase the unfinished unit).
#               Jim: "if I pass an exam with an eighty-five... I can do all the units and
#               still be carrying an eighty-five with me, which is gonna keep me from
#               mastering the final exam."
#               ⭐ THE REAL DEFECT WAS ARITHMETIC. Mastery is 90% and the Unit Quiz asked
#               for FOUR OR FIVE questions, so the only scores it could produce were 80%
#               and 100% -- there is no 85, and the 90% bar silently meant a PERFECT
#               PAPER. Topic quizzes had it too: three or four questions against an 80%
#               bar is four out of four. Nobody wrote that on purpose; the bar moved from
#               80 to 90 on 2026-08-04 in store.py and the question counts stayed here.
#               Unit Quiz -> TEN questions, topic quiz -> FIVE, in all NINE templates
#               (ten courses). The example tags moved with them (correct="9" total="10",
#               correct="4" total="5"). ruletests PART 3k now multiplies the bar by the
#               question count for every quiz in the system and fails if the only passing
#               score is a perfect one.
#               NEW RULE 50 -- AN UNFINISHED UNIT IS YOUR JOB, NOT THEIRS TO REMEMBER.
#               A student may move on with a unit unmastered (Jim's call: momentum
#               matters), so the tutor now raises it ONCE at the start of a session from
#               the "checked but not yet mastered" list, reviews before it re-quizzes
#               (rule 47 still applies), always uses NEW questions, and says out loud that
#               the record keeps their BEST score -- fear of losing a good score is the
#               most common reason a student refuses a retry, and it was never addressed.
#   2026-08-10  BUILD co -- RULES 2 AND 8 ARE NOW ENFORCED, NOT JUST WRITTEN DOWN.
#               Generating the rule index (audit #2 item 23) made something plain that a
#               person reading 49 rules would never notice: rules 2, 5 and 8 were the
#               only ones in the entire prompt that NOTHING checked -- not a referee, not
#               an audit, not even a coverage grep. Two of the three turned out to be the
#               same shape as rule 7 seen from the other side, so the visual referee
#               learned them rather than growing a new one:
#                 rule 2 -- the student ASKED to see something ("show me", "can I see",
#                   "draw it") and the reply puts nothing on the board. There is no
#                   legitimate version of that: re-drawing is free and always right.
#                   prose_visual_conflict() now takes the student's message to see it.
#                 rule 8 -- the tutor SAYS he is about to show or draw something and then
#                   draws nothing. Uses the same deferral guard as the rest of the
#                   referee, so "next time I'll draw you one" is still fine -- the
#                   battery caught that on the first run, because the case was already a
#                   fixture from build ce.
#               _last_user_text() feeds the student's real words in, skipping the SYSTEM
#               nudges the referee itself appends on a retry.
#               Rule 5 (don't narrate symbols) is left honestly UNVERIFIED: judging it
#               needs to know what a reply SOUNDED like, and a bad guess there would
#               re-roll good teaching.
#   2026-08-10  BUILD cm -- PER-TURN NOTES RIDE WITH THE MESSAGE, NOT THE PROMPT.
#               Found while answering Jim's question about whether prompt size costs
#               money or performance. The system prompt is ONE cached block, so anything
#               written into it MOVES THE CACHE PREFIX and re-bills every token from that
#               point on. Build ck appended the misconception hint into the prompt (via
#               mastery_note), 63,629 characters in -- so every turn a hint fired threw
#               away roughly 15,000 tokens of cache and paid a cache write on top, to
#               deliver about 195 tokens of actual note.
#               get_tutor_reply() gained turn_note=, appended to THIS turn's user
#               message where nothing is cached anyway. The note reaches the model
#               exactly as before -- arguably better placed, right beside the answer it
#               is about -- and the system prompt is byte-identical from turn to turn.
#               RULE OF THUMB for anyone adding one: if it changes every turn, it is not
#               a system prompt, it is a message.
#   2026-08-10  BUILD cl -- _foundation_block() gained verbatim=, threaded through the
#               lesson, practice and topic prompts from student["foundations_verbatim"].
#               See foundations.py: a script the student has already heard is OFFERED,
#               not replayed (rule 40), so its wording only needs to be in the prompt on
#               the turn they accept the offer. Defaults to True everywhere; the older
#               two-argument foundations.py still works via the existing TypeError path.
#   2026-08-10  RULE 49 + THE MISCONCEPTION CATALOGUE (build ck, Jim: "I want to
#               pursue the misconception box"). Proactive audit #2 item 2.
#               49 A WRONG ANSWER IS THE OUTPUT OF A RULE -- FIND THE RULE. Rules 20-22
#                  say what to DO about a wrong answer and never say what to work out
#                  first. A student who says 3 + 2 x 4 is twenty is not guessing: they
#                  are evaluating left to right, faithfully, and will do it again next
#                  week. A student who says twenty-one made a slip. Same topic, same
#                  wrongness, OPPOSITE remedies. 49 makes him reconstruct the procedure
#                  from the number, fix the RULE rather than the answer, check the
#                  hypothesis with one question before acting on it, never announce a
#                  diagnosis as a fact about the student (rule 42), and diagnose from
#                  what they actually said when nothing in the catalogue fits.
#               NEW misconceptions.py carries 148 catalogued wrong rules; this file
#               appends the course's catalogue to the lesson, practice and topic
#               prompts (TELL + RULE + FIX -- the ready-made wording is delivered
#               just-in-time by main.py instead, so the prompt is not paying for 146
#               sets of words that will not come up this turn). Defensive import.
#   2026-08-09  THE SYMBOL TABLE REACHES THE TUTOR (build cj). Jim: "it looks like
#               we've fixed the function notation, but math is filled with these kinds
#               of things. How can we make sure that every one of these is caught all
#               of the time?"
#               Rule 48 (build ci) told him to read every symbol aloud and to deny the
#               wrong reading BY NAME -- and never told him our readings. That is the
#               same mistake as rule 40 before foundation memory: a rule the model has
#               no data to obey. NEW notation.py registers all 28 families once, and
#               _notation_block(course) appends a compact "HOW TO SAY WHAT YOU WRITE"
#               table to the lesson, practice AND topic prompts, listing only the
#               symbols that course actually uses, each with the words to say and the
#               wrong reading to deny. Defensive import, like foundations.
#   2026-08-09  RULE 48 -- TEACH THEM HOW TO *SAY* THE SYMBOL (build ci, Jim's live
#               Algebra I session: "it's never been clearly stated to me what f of x is,
#               how to say f of x... and then it flipped over to g of x").
#               Rule 14 has always said "define every notation the first time it
#               appears". That is only half a rule, and the missing half is the half that
#               failed here. A student who cannot SAY a symbol cannot ask a question
#               about it, cannot answer one out loud in a voice classroom, and quietly
#               stops trying. So 48 requires: (a) say the words a person says, and put
#               the written form up in the same breath, so the sound and the shape arrive
#               together; (b) deny the wrong reading BY NAME -- f of x is NOT f times x,
#               because that guess is predictable and naming it is what prevents it;
#               (c) a letter is a NAME, not a new idea -- when f becomes g, say so, or a
#               student who was following perfectly assumes a new concept nobody taught
#               them; (d) the first time is not the only time, and f of x, f of g of x and
#               f prime of x each get their own first time.
#               The five canonical scripts that carry this live in foundations.py.
#   2026-08-09  RULES 45-47 + THE SCORE REFEREE (build ch, audit #2 items 9/10/11).
#               45 THE TALLY IS ARITHMETIC, NOT JUDGMENT -- report the exact count, never
#                  round up, never "basically", never award mastery out of sympathy, and
#                  the only percentage you may state as the SCORE is the one the tally
#                  gives (naming the bar itself is fine). Warmth belongs in HOW you
#                  deliver the number; rule 35 already says how. 45(d) spells out why it
#                  is not negotiable: a score nudged once becomes a mastered unit, a
#                  green bar, and a line in a record a parent may have to defend.
#               46 A QUIZ QUESTION TESTS ONE SKILL -- name the topic before question one,
#                  and keep the supporting arithmetic at or below what they have already
#                  mastered. A question that needs the new skill AND long division fails
#                  a student who has the new skill, and nobody outside can tell.
#               47 NO COLD QUIZZES -- two unaided correct on this topic, this session,
#                  before any quiz is offered. Rule 35 already required exactly that
#                  before a RETAKE; it should always have been true the first time.
#               ⭐ prose_score_conflict() -- the FOURTH check in prose_board_conflict().
#               The server has always recomputed the percentage from correct/total, so no
#               number the model asserts is ever STORED. Nothing checked what the student
#               HEARS: the tag can read 3 of 5 while the sentence beside it says "you
#               passed!". Same shape as the 2026-08-08 dimes contradiction, except this
#               one lands on the progress bars. Now caught and silently rewritten.
#               Thresholds are mirrored here as QUIZ_PASS_PCT / UNIT_PASS_PCT /
#               FINAL_PASS_PCT (tutor.py must not import the storage layer) and
#               ruletests.py asserts they never drift from store.py's.
#               THREE false positives were caught by the battery before shipping: the
#               "%" regex had a trailing \b so it never matched "80% — great!" at all and
#               the whole percentage check was silently dead; quoting the bar ("you need
#               80% to pass") had to stay legal; and in a percents lesson "what is 25% of
#               80?" is the PROBLEM, not a score claim, so a percentage now only counts
#               when its sentence is actually reporting the result.
#   2026-08-09  THE PENDING-QUESTION REFEREE + AN HONEST TODAY-BAR NET (build cg).
#               Jim: "it gave me a problem without putting it on the board, and this is
#               the exact example that we've already used once before that was supposedly
#               fixed. And I don't understand why it's not fixed."
#               He is right to be annoyed. Rule 15 does not just forbid this in general --
#               it NAMES this exact column-addition scenario, quotes it, and prints the
#               exact fix ([[step eq="dollars: 2 + 1 + 1 = ?"]]). It has said so since
#               build bm, and the reply still went out with the question spoken and the
#               board empty. That is the difference between a rule the model is TOLD and
#               a rule the machine ENFORCES, and this one has now changed sides:
#               prose_pending_question_conflict() is the third check inside
#               prose_board_conflict(). If a sentence asks the student to COMPUTE
#               something -- two or more numbers, or an operator word and a number, or a
#               written expression -- and the reply emits no board tag containing a "?",
#               the draft is discarded and silently rewritten, exactly like a failed math
#               check. Narrow by design (a re-roll is a real model call): number WORDS
#               count because he speaks in words; a bare "-" or "/" does not count as an
#               operator ("three-fourths", "1/2" are single values -- both caught by the
#               test battery on its first two runs); and rule 39(d)'s constant
#               "does that click, or should I show it another way?" never triggers it.
#               ALSO: ensure_today_tag() gained today_live=. Its history guard used to
#               read "a [[today]] was emitted earlier, so a bar is up -- don't reset it."
#               True inside one sitting; FALSE across a page load, which is precisely
#               where Jim kept losing the bar. It now stands down only when the SERVER
#               confirms the bar really exists (main.py passes student["today_live"]).
#   2026-08-09  RULES 41-44 (build cf, proactive audit #2 "do first").
#               41 EVERY PICTURE CARRIES A CAPTION THAT SAYS WHAT TO NOTICE -- and it
#                  captions the POINT, not the object: "both are four steps from zero",
#                  never "a number line". A caption-less figure hands the student back
#                  the one job the picture was supposed to do for them. ruletests.py
#                  PART 3c now enforces this on our own 64 foundation figures (10 of them
#                  had no caption and now do).
#               42 NEVER COMPARE THIS STUDENT TO ANYONE BUT THIS STUDENT -- not to
#                  classmates, siblings, "most kids", or a grade level. It slips out as
#                  kindness: "most kids find this hard" is meant as comfort and lands as
#                  a measurement against a room the child cannot see. The only comparison
#                  allowed is to their OWN earlier work, which our progress data actually
#                  supports. No invented percentiles or grade equivalents, ever.
#               43 YOU PERCEIVE EXACTLY TWO THINGS -- what they typed or said, and what
#                  you put on the board. Never "I can see you're working hard", never
#                  "you sound tired". Warm, ordinary teacher sentences, every one of them
#                  a false claim about watching a child: unsettling to a student who half
#                  believes there is a person here, alarming to a parent reading the
#                  transcript, and untrue, which is reason enough (rule 13).
#               44 READ THE PROBLEM ALOUD, IN FULL, EVERY TIME -- rule 15 got it onto the
#                  screen; this gets it into the student's ears. Some of our students are
#                  seven, some are dyslexic, some are listening with the screen off to
#                  one side; a problem that exists only as text is one they cannot
#                  attempt, and their silence would look like a math failure in every
#                  number we report about them.
#               ALSO: build_practice_prompt() and build_topic_prompt() now append
#               _foundation_block() with the student's heard list, exactly like the
#               lesson prompt. Found while auditing audit #1: those two modes carried
#               rules 36-40 but not the scripts the rules refer to.
#   2026-08-09  RULES 39 + 40 AND THE VISUAL REFEREE (build ce, Jim's three items).
#               RULE 39 -- TALK LESS, CHECK IN OFTEN, AND MAKE THE CHECK FAILABLE.
#               Jim: "we need to have a cap on how long we talk to an eight year old.
#               I think you need to check in with them every now and then." There was no
#               length rule anywhere in the prompt. In a voice product that is the fastest
#               way to lose a young student, and you cannot see them drift. 39(a) caps a
#               turn at ~90 spoken words, ~60 for the elementary courses and any student
#               around ten or younger, with exactly two exceptions (a canonical foundation
#               script, and the rule-0 opening message). 39(b) one question per turn, last.
#               39(c) check in at every new idea and never more than ~3 turns without one.
#               39(d) is the part that matters: "does that make sense?", "got it?", "any
#               questions?" and "okay?" asked ALONE are BANNED. Every student says yes to
#               those and a confused child says yes fastest, because saying no to a teacher
#               costs them something -- a check that cannot fail is worse than no check,
#               because it buys false confidence. He must always hand them an easy way out
#               in the same breath ("…or should I show it a different way?") or ask for
#               CONTENT, which a yes cannot fake. 39(e) thank a student who says they are
#               lost. NOTE this does NOT contradict audit #2 item 3: Jim asked for more
#               check-ins and the audit asked for better ones; 39 is both.
#               RULE 40 -- ASK BEFORE YOU REPEAT AN INTRODUCTION. Jim: "a loyal student can
#               re-hear it… we should just query him and say, do you think you got it, or
#               do you want me to refresh your memory?" Exactly that: name the term in one
#               sentence, ask, and STOP. If they want it, speak the canonical script WORD
#               FOR WORD (same words = same lesson, and the audio is already paid for). If
#               they say they have it, believe them -- but if a problem then goes wrong
#               because of that term, give the script anyway and never as "you said you
#               knew it". 40(e): the youngest students are poor judges of their own memory,
#               so for Entry-Level and Basic Math he asks ONE small concrete question about
#               the term instead and lets the answer decide. 40(f): he ends any reply that
#               delivered an introduction with [[learned term="..."]] -- invisible to the
#               student, and the only way the system remembers next month.
#               _foundation_block()/build_system_prompt now pass the student's heard list
#               through to foundations.prompt_block(); an older foundations.py without the
#               second argument still works (TypeError -> retry).
#               ⭐ THE VISUAL REFEREE -- prose_visual_conflict(), now the FIRST half of
#               prose_board_conflict(). Jim: "you can't say one thing and then have the
#               numbers say something different." The numeric half has done that since bu;
#               nothing has ever checked the OTHER way a reply lies about the board. Rule 7
#               has forbidden describing an undrawn picture since ao -- in words only. A
#               reply that says "here's a number line" and emits no [[numberline]] passed
#               mathcheck (tags only) and passed the prose referee (numbers only), and the
#               student sat in front of a blank board. That is exactly the demo failure Jim
#               called "we got one shot to do it right, and it failed". Now it is caught and
#               silently regenerated like any other referee finding.
#               Deliberately narrow, because every false positive costs a real model call:
#               it fires only when ONE SENTENCE both names something this board can draw
#               and claims in the present tense that it is appearing now. Bare "triangle"
#               and "circle" are excluded (too common in ordinary prose), and a sentence
#               that DEFERS ("next time I'll draw one"), OFFERS ("want me to draw it?") or
#               looks BACK ("remember the number line we used yesterday?") is not a claim.
#               A second, weaker check covers "look at the board" when the reply writes
#               nothing at all. FIGURE_TAGS is a constant here (tutor.py must not read the
#               static files at request time) and ruletests.py PART 3c proves it has not
#               drifted from session.html's handleTags(). Fails open, always.
#   2026-08-09  ★ FOUNDATION FIRST -- RULES 36-38 (build cc, Jim). "Socratic" was the
#               wrong description of what a math classroom should do, and it showed:
#               students met fractions without being told what a fraction, a numerator
#               or a denominator IS. Rule 36 teach the thing before you ask about it
#               (name it, name every part, define, worked example, check the IDEA, THEN
#               questions) · rule 37 vocabulary is taught, never assumed · rule 38
#               concrete -> picture -> symbols with I-do/we-do/you-do and guidance that
#               fades only as competence grows. All per-course "Socratic, one-step-at-a-
#               time" wording replaced with "foundation-first"; rules 36-38 explicitly
#               override anything older. New foundations.py supplies 24 CANONICAL
#               scripts spoken VERBATIM (also a cost win -- the TTS cache is keyed by
#               text, so a verbatim script renders once for the platform, ever).
#   2026-08-09  RULE 35 -- FIX, THEN RETRY (build cb, Jim asked directly: "if a student
#               fails a quiz, do we give the quiz immediately again, or make them review
#               what they had trouble with first?"). The old wording only said to
#               "re-teach the gaps, then offer a fresh quiz when they're ready", which
#               permits an instant retake. Now explicit and shared across all ten
#               courses: name the win first · diagnose the ONE or TWO skills under the
#               misses · re-teach each with a worked example (rule 19) · require TWO
#               UNAIDED correct problems on that skill before a retake is offered ·
#               fresh questions, never the same items · a second failure steps BACK to
#               the prerequisite rather than looping a third time · never say the
#               student "failed" -- the quiz hasn't passed YET.
#   2026-08-09  THE PROACTIVE RULES + THE PROSE REFEREE (build bu, Jim: "implement the
#               proactive rules as you see fit" -- from claude/Proactive_Rules_Audit_
#               2026-08-08.md, 25 rules written BEFORE a student finds them).
#               NEW SHARED RULES 20-34 (all verified in all ten course prompts):
#                 20 partially-right is not wrong · 21 "I don't know" earns a SMALLER
#                 step, never a repeat · 22 the escalation ladder (never ask the same
#                 way twice; miss 3 = work it together) · 23 equivalent answers are
#                 correct · 24 self-corrections / leaps / "just tell me" · 25 when the
#                 student says YOU are wrong · 26 a wrong board line is corrected on
#                 the board + [[clear]] discipline + short lines · 27 units on final
#                 answers, "≈" for estimates · 28 one name per thing · 29 how a session
#                 ENDS (+ long-session check-in) · 30 off-topic/personal questions
#                 (never claim to be human) · 31 ⚠️ when something bigger than math
#                 shows up (self-criticism / personal info / harm) -- QUEUED FOR
#                 COUNSEL · 32 story problems survive a sanity check · 33 difficulty
#                 moves one notch · 34 keep old skills sharp (spaced review).
#               SPEECH: number-words bullet added to all ELEVEN "HOW YOU SPEAK" blocks
#               (negative VALUES are "negative", percents, ratios, mixed numbers, big
#               numbers whole); transcription charity now states that spoken number
#               words ("twelve hundred", "a half") ARE exact answers.
#               ⭐ THE PROSE REFEREE (audit #24) -- prose_board_conflict() + wiring into
#               _create_verified. mathcheck sees only TAGS; this catches the shipped
#               2026-08-08 bug where the spoken words adopted the student's wrong
#               "fifteen" while the board correctly wrote 16. Deliberately NARROW (a
#               false positive throws away a good reply): flags only when a labeled
#               board conclusion is contradicted by the spoken words AND the words
#               never once say the board's number. Fails OPEN everywhere; a flagged
#               draft is silently regenerated (the student never sees it) and, if it
#               cannot be resolved, passes through rather than bricking the lesson.
#               Companion: ruletests.py (audit #25) -- the regression battery.
#   2026-08-08  RULE 19 -- WORKED EXAMPLE FIRST (build bs, Jim: "start every new topic
#               with a complete worked example before the student tries one -- more
#               teaching, not 100% teaching-by-doing"). New rule 19 in the SHARED
#               precision block: (a) one complete example worked BY THE TUTOR on the
#               board, every step + the answer, narrating the why (rule 6 explicitly
#               does not apply to the tutor's own example -- collision noted so it
#               can't cause step-skipping); (b) demo may span 2-3 short turns ending
#               in continue-checks, never computation questions; (c) then "you try
#               one" -- similar problem, at/below the example, "?"-line style, with
#               the worked example LEFT on the board until their first success;
#               (d) fires on new topics and re-teaching after struggle, not every
#               problem. 10-course scan verified.
#   2026-08-08  RESUME BARS + THE "?" LINE (build br, Jim's resumed-session screenshot).
#               (1) PROGRESS_TAGS_NOTE: [[today items]] is now required in the FIRST
#               message of EVERY session -- resumed sessions included (a welcome-back
#               opener dove straight into the problem and the today bar stayed empty).
#               Companion: session.html now renders the UNIT bar at page load from
#               curriculum + placement + server quiz history (like the course bar), so
#               it no longer depends on the model's [[unitplan]] tag at all.
#               (2) Rule 15 gains the concrete device for asked steps: write the step
#               as a PENDING "?" line -- [[step eq="dollars: 2 + 1 + 1 = ?"]] -- in the
#               same reply as the question; next reply replaces "?" with the confirmed
#               number. (Second miss of the same kind in one lesson: the dollars-column
#               question was spoken with no board line.)
#   2026-08-08  RULE 18 -- CHECK THE STUDENT'S ANSWER (build bq, Jim's screenshot,
#               carrying dimes: asked "seven plus eight plus one?", student said
#               "fifteen" (wrong -- it's 16), and the tutor ACCEPTED it aloud ("write
#               the five and carry a dollar") while its own board correctly wrote
#               dimes: 7 + 8 + 1 = 16 -- spoken lesson and board contradicted each
#               other, and the wrong digit was taught. New rule 18 in the SHARED rules
#               block (all courses, verified by 10-course scan): (a) compute the
#               student's numeric answer YOURSELF before accepting/building on it --
#               a wrong answer is a coaching moment, never adopted; (b) spoken numbers
#               must MATCH the board's numbers in the same reply. Related: the parked
#               "prose referee" decision (mathcheck only checks tagged computations,
#               not prose) -- rule 18 is the prompt-side fix; a mechanical prose check
#               remains open in Teaching_Precision_Review_2026-08-06.
#   2026-08-08  MONEY IS SPOKEN AS MONEY + ALL-COURSE RULE COVERAGE (build bp, Jim:
#               "$1.85" was voiced "one dot eight five -- no dollar, no cents").
#               (1) New bullet in EVERY "HOW YOU SPEAK" block (each course template has
#               its own -- 11 total): prices are spoken "one dollar and eighty-five
#               cents", plain decimals "three point seven five"; the board keeps the
#               symbols. Client twin in forSpeech() on all three teaching pages.
#               (2) COVERAGE AUDIT: the bk MULTIPLICATION SIGN bullet had landed in a
#               course-specific whiteboard block and reached only 3 of 10 courses --
#               MOVED into the shared "BOARD LEADS" section (rule 4 area). Verified:
#               ×-rule, money rule, and all recent rule sharpenings now present in the
#               built prompts of ALL TEN courses. LESSON LEARNED for future edits:
#               "HOW YOU SPEAK" and the whiteboard tag docs are PER-COURSE (11 copies);
#               shared blocks are GRAPH_TOOL_NOTE (rules 1-17), SESSION_OPENER_RULES,
#               and PROGRESS_TAGS_NOTE -- put universal rules THERE, then verify with a
#               10-course build_system_prompt scan.
#   2026-08-08  TODAY-BAR NET + FINAL-STEP LINE (build bo, Jim's Pre-Algebra screenshots).
#               (1) TODAY bar never rendered: the opener skipped [[today items]]. Fixes:
#               rule 0(c) now explicitly requires the [[today]] tag right after the goals
#               card, AND new ensure_today_tag() -- a DETERMINISTIC net (never guesses,
#               unlike the retired ensure_board): if a lesson reply announces goals (card
#               or [[goal]] banner) with no [[today]] in the reply or session history, it
#               appends [[today]] with the model's own goal items verbatim. Lesson only.
#               (2) Column-addition finale skipped its board line ("dollars: 2 + 1 = 3"
#               never written; board jumped to 2.30 + 1.45 = 3.75): rule 4 sharpened --
#               every answered sub-step gets its own line BEFORE any combined line.
#   2026-08-08  NO MORE TRUNCATED TURNS (build bn, Jim's live freeze: a first Basic-Math
#               teaching turn collapsed to the single word "Let" with an empty board --
#               the tag-heavy reply hit the 1200-token max_tokens ceiling MID-TAG and
#               nothing checked stop_reason; the client stripped the dangling tag and
#               the lesson stalled). New _create_full(): every logical turn now checks
#               stop_reason == "max_tokens" and CONTINUES via assistant prefill, stitching
#               the pieces (up to 2 continuations); ceiling raised 1200 -> 1600. All three
#               teaching modes (lesson/practice/topic) flow through it via
#               _create_verified, so one fix covers them all.
#   2026-08-08  RULE 15 SHARPENED -- "YOUR TURN" GOES ON THE BOARD (build bm, Jim's live
#               catch in Pre-Algebra: the tutor worked 3 + 2 × 4 on the board, then asked
#               "your turn -- what's ten minus two times three?" with the NEW problem
#               existing only in the spoken words). Rule 15 now says explicitly: the
#               problem handed to the student is written in symbols ([[step]]/[[write]])
#               in the SAME reply it is asked; only its answer/worked steps stay off the
#               board (never conflicts with rule 6). Additive sharpening only.
#   2026-08-07  MULTIPLICATION SIGN RULE (build bk, Jim's screenshot: "3 + 2 X 4" showed
#               a red variable X). New bullet in the whiteboard section: write
#               multiplication as × (or ·), NEVER the letter x -- the board styles every
#               lone letter as a variable. Client-side safety net shipped in the same
#               build (styleVarsCore on all three teaching pages).
#   2026-08-07  RULE 16 SHARPENED (build bh, Jim's second live catch on it: the reply wrote
#               the SUBSTITUTED check line but still said "plug five back into the original
#               equation on the board" while 5x-3=2x+12 had scrolled away). Rule 16 now
#               explicitly requires re-writing THE ORIGINAL EQUATION ITSELF, labeled, above
#               the check line -- and bans speaking "the original equation" unless this
#               reply shows it. Additive sharpening only.
#   2026-08-07  RULE 17 -- NEVER ANSWER YOUR OWN QUESTION (build az, Jim's live catch in
#               Basic Math: "five yummy cookies: how many cookies do you see?" -- the count
#               was spoken in the setup of the counting question). New rule 17 in the
#               shared 13-16 block, all courses/modes: a reply that asks a question must
#               not state or hint at its answer anywhere in the same reply -- counting
#               questions never name the object count; recaps name the TOPIC, not the
#               pending answer. The spoken twin of rule 6 (board never runs ahead).
#   2026-08-07  GRAPH HOLES + WINDOW FRAMING (build av, Jim's live catch in Calculus: the
#               tutor said "I've punched a hole out at x = 2" over an UNBROKEN y=x² whose
#               window barely showed the parabola). (1) [[graph]] docs teach the NEW
#               hole="a" attr (math-figures.js draws an open circle on the first curve) --
#               a spoken hole MUST carry the attr. (2) BOARD HONESTY rule 1 extended:
#               features WITHIN a figure (holes/asymptotes/intersections) must be drawn,
#               never narrated invisibly. (3) Window-framing guidance: range must put the
#               discussed point comfortably inside the picture with room on both sides.
#               Companion: math-figures.js hole rendering; forSpeech on all three pages now
#               says "squared" for ² (the voice read "x²" as "x two").
#   2026-08-07  RULE 16 -- CHECK QUESTIONS RE-WRITE THE EQUATION (build at, Jim's live catch:
#               "plug 4 back into two x plus five equals thirteen" was asked with the board
#               showing only "x = 4" -- the equation lived in speech only / scrolled away).
#               New rule 16 in the shared 13-15 block, all courses, all modes: any
#               substitution / verify / "check it" question must [[write]] the full equation
#               in the SAME reply -- "on the board from earlier" does not count. Additive.
#   2026-08-07  DIPLOMA -> COURSE CHAMPION (build ar, Jim: a diploma implies an accredited
#               school -- we are not one). FINAL_PREP_NOTE + FINAL_EXAM_NOTE reworded: passing
#               the Final Exam now earns the 🏅 COURSE CHAMPION medal in the trophy case (the
#               tutor points the student at their dashboard, never at a printable credential).
#               Never write prompt language promising diplomas/certificates/transcripts.
#   2026-08-07  PROGRESS BARS + FINAL EXAM (Jim: "a nervous student should always see where
#               they are" + a real gated course final). Three additions, all appended to the
#               LESSON prompt only:
#               (1) PROGRESS_TAGS_NOTE -- teaches two new hidden tags feeding the lesson
#                   page's new bars: [[today items="..."]] (emitted in the opener right after
#                   the goals card) + [[todaydone n="1"]] (when the student demonstrates goal
#                   n -- honest, never decorative), and [[unitplan unit="3" topics="a|b|c"]]
#                   (the unit's stable topic ladder, emitted when a unit starts/resumes; the
#                   bar lights passed topics from the existing [[quiz]] tags).
#               (2) FINAL_PREP_NOTE / FINAL_EXAM_NOTE -- appended by build_system_prompt ONLY
#                   when main.py set student["final_mode"] after SERVER-SIDE verification that
#                   all nine units are mastered (>= 90% Unit Quiz). Prep = optional overview +
#                   warm review (never the exam). Exam = 18 questions, two per unit, one at a
#                   time on the board, NO hints, private tally, then the new hidden
#                   [[finalexam correct total]] tag (pass = 90% -> Course Diploma; below =
#                   warm shore-up + fresh exam offer; abandoning = unscored, never shamed).
#               Additive only -- no existing rule, template, or function changed; the gate
#               itself lives in main.py.
#   2026-08-07  OPENING SEQUENCE -- FIXED ORDER, ALL COURSES (Jim's live check, second fix today:
#               a first visit to Pre-Algebra greeted, asked the warm-up question IN the greeting,
#               and only then showed the "By the end you'll be able to" card and the numbers --
#               "the order is often just mixed up"). The 2026-08-03 fix for this ("YOUR OPENING
#               REPLY -- set the table first, no problem yet") was ELEMENTARY-ONLY; the other
#               eight courses never got it, which is why it kept recurring. Now UNIVERSAL:
#               SESSION_OPENER_RULES (appended after EVERY lesson template, overrides them)
#               gained rule 0 -- first message = (a) greeting (course welcome if first time in
#               this course, welcome-back recap if returning, never "great to meet you" to a
#               known student) -> (b) today's topic -> (c) today's goal spoken + [[goal]] +
#               goals card -> (d) "Ready to get started?" and STOP. No math problem, numbers,
#               or content question in the first message; the first problem comes next turn,
#               board-first per rule 15. Additive only -- rules 1-3 and all templates untouched.
#   2026-08-07  VOICE-FIRST CLASSROOM (Jim: "back to the conversational back-and-forth").
#               GRAPH_TOOL_NOTE (the STUDENT'S TOOLS block prepended to every mode's prompt)
#               rewritten to match the restored voice input and the retired controls:
#               - The student now TALKS: they tap 🎙️, speak, and their words arrive as text
#                 (ElevenLabs Scribe transcription; audio deleted after transcription). They
#                 can also type. Elementary courses still tap answer buttons. The old first
#                 line said "The student types their answers (there is no microphone)" --
#                 that was making the tutor talk about typing to a student who is speaking.
#               - The 🧮 MATH KEYBOARD paragraph is REMOVED (the keypad is retired app-wide);
#                 the tutor now knows spoken math ("x squared plus three") and plain typed
#                 math (x^2 + 3/4) are both fine and should never mention a math keyboard.
#               - Transcription-slip guidance added: spoken math arrives through a
#                 transcriber, so near-miss words ("sign" for sine, "eggs" for x) should be
#                 read charitably and confirmed, never mocked or marked wrong outright.
#               - The 📈 GRAPH PAPER paragraph and rules 13-15 etc. are UNCHANGED.
#               Prompt-block text only; no function, template, or rule outside the tools
#               block was touched.
#   2026-08-06  PRECISION + NO-ASSUMPTIONS + COMPLETE-QUESTIONS (Jim's live audit: ~50% of
#               checked lesson problems failed -- wrong verbal claims ("the line keeps
#               climbing forever in both directions" for y=2x+1), notation assumed known
#               (trig course used f(x) without saying f(x) = y), and questions asked without
#               their numbers/graph on the board). GRAPH_TOOL_NOTE gained rules 13-15, so
#               they reach lesson + practice + topic in ALL courses:
#                 13. every spoken mathematical sentence must be LITERALLY true (the SymPy
#                     referee only checks tagged computations, not prose -- the prose rule
#                     lives here); the reason given for a fact must be as correct as the fact.
#                 14. define EVERY notation at its first use in the conversation (f(x), theta,
#                     |x|, interval notation...) -- never assume a prior course taught it.
#                 15. a question must be complete on screen before it is asked: referenced
#                     numbers/graphs visible on the board, answer form named, self-contained.
#               PLUS: the four advanced-course "WHO THIS STUDENT IS" blocks (Algebra II,
#               Pre-Calc, Calculus, Diff Eq) said "they know functions / do NOT re-teach the
#               basics" -- the very line that made the trig course use f(x) without defining
#               it. Each gained a reconciling sentence: prior exposure is FAMILIARITY, not
#               mastery; rule 14's one-sentence definition at first use still always applies.
#               Additive only -- no existing rule, template, or function removed.
#   2026-08-04  QUIZZES (Jim: checkpoints within units). All nine courses' 'QUICK CHECKS'
#               prompt sections replaced with a 'QUIZZES' section teaching a two-tier system:
#               (1) TOPIC QUIZ -- 3-4 questions after each topic; PASS = 80%+; passing is how
#               the student earns the next topic (fail -> re-teach the gaps -> fresh quiz;
#               never a dead end); emits NEW tag [[quiz unit topic name correct total]].
#               (2) UNIT QUIZ -- the end-of-unit check renamed; 4-5 questions across the unit;
#               90%+ = MASTERED; still emits [[check unit correct total]] (tag/API unchanged,
#               so every existing mastery pipe keeps working). The student's mastery note
#               (main._mastery_note) now lists passed/unpassed topic quizzes per unit, and the
#               section tells the tutor to resume at the first unpassed topic and never
#               re-quiz passed ones. Cross-references '(see QUIZZES)' updated.
#   2026-08-04  MASTERY = 90% (Jim): every check-result prompt line that told the tutor "80% or
#               better means MASTERED" now says 90%, matching store.PASS_PCT. Nine phrase edits
#               across the course templates; nothing else touched.
#   2026-08-04  USAGE LOGGING (Measurement plan #1). Every brain call now records what it
#               actually consumed: _create_verified() sums token counts (input/output/cache)
#               across its attempts straight from the Anthropic responses and hands the totals
#               -- plus the attempt count and the verifier's verdict (ok / fixed / unresolved /
#               unverifiable / none) -- to store.log_usage(); get_assessment() logs its single
#               call the same way. The three get_*_reply functions and get_assessment gained an
#               optional trailing `code=""` parameter so main.py can attribute usage to a
#               student code (privacy: the CODE only, never any text; defaults keep every
#               existing caller working unchanged). store is imported defensively like pedagogy
#               -- if it's missing, logging is silently off and teaching is untouched.
#   2026-08-03  THE MATH VERIFIER (Jim's pick for the next build): every reply the tutor
#               generates is now refereed by a real math engine (SymPy) BEFORE the student
#               sees it. GRAPH_TOOL_NOTE gained rules 10-12 ("THE SILENT ANSWER KEY"): any
#               reply stating a new problem or a computed result also appends a hidden
#               [[verify expr="..." answer="..."]] tag holding the claim in SymPy syntax.
#               New module mathcheck.py parses the tag and actually DOES the math
#               (equations incl. systems and multiple roots, computations, simplifications,
#               inequalities, derivatives/integrals). A provably wrong claim triggers a
#               SILENT regeneration (up to 3 attempts) with SymPy's computed correction fed
#               back; the student only ever sees a verified reply. Undecidable tags FAIL
#               OPEN (pass through) so a checker gap can never stall a lesson. Tags are
#               stripped server-side -- the frontend needed no changes at all. Applies to
#               all 10 courses x lesson/practice/topic (the three get_*_reply functions now
#               share _create_verified below). sympy was added to requirements.txt.
#   2026-08-03  BOARD IS THE LESSON, WORDS ARE THE BACKUP (Jim). GRAPH_TOOL_NOTE -- the shared
#               block prepended to EVERY course's lesson/practice/topic prompt -- gained rules 7-9:
#               (7) never ask the student to IMAGINE what the toolkit can draw (with [[objects]]
#               taught inline so all ten courses know it); (8) SHOW change -- adding a star draws
#               ⭐⭐⭐⭐⭐ + ⭐ via [[objects ... add="1"]], story problems draw frame by frame;
#               (9) the sound-off check -- every reply must be followable with the audio muted, at
#               every level. Elementary template's objects doc updated for add=. One shared block,
#               so all 10 courses x 3 modes inherit it.
#   2026-08-03  ELEMENTARY OPENING PACING + [[objects]] (Jim's playtest: the opener welcomed AND
#               posed a problem in one breath, with the plan card landing after the problem; and he
#               asked a child to IMAGINE five stars). New "YOUR OPENING REPLY" section: first reply
#               = welcome + goal + plan card + ready-check ONLY; the first problem comes next turn,
#               board first. The whiteboard toolkit and BOARD FIRST rule gained [[objects
#               emoji="⭐" groups="5"]] (two rows to compare: "5 | 3") -- countable things are DRAWN,
#               never imagined; count not printed. Same line added to entry/basic practice+topic
#               scopes. Elementary template only; other courses untouched.
#   2026-08-03  ELEMENTARY GUARDRAILS (Jim's playtest: persona notes about algebra made Entry-Level
#               Math teach two-step equations, and the warm-up question never hit the board). The
#               ELEMENTARY template gained (1) a HARD "stay inside this course" wall -- other-course
#               notes are ignored for content, breeze-through students get richer problems (and a
#               suggestion to move up), never harder topics; (2) "board first, buttons second" --
#               every asked question is written with [[step]] in the same reply BEFORE [[choices]].
#               Companion fix: students.json personas are now course-neutral (see that file).
#   2026-08-03  TAP-TO-ANSWER CHOICES (Jim: young kids can't type -- "multiple choice answers,
#               and they can just click"). The ELEMENTARY lesson brain gained a TAP-TO-ANSWER
#               section: whenever the tutor asks a question with a specific expected answer it
#               also emits [[choices options="a | b | c"]] (3 short options, one correct, others
#               plausible child slips, right answer in a varying spot; never spoken aloud; used
#               for quick-check questions too). The same instruction was appended to the entry/
#               basic PRACTICE_SCOPE and TOPIC_SCOPE so all three modes tap. The app renders the
#               buttons (session/practice/topic.html) and always adds an "I'm not sure" button;
#               typing stays available as a backup. Elementary-only by prompt; the tag itself is
#               generic. Purely additive; no other course's prompts changed.
#   2026-08-03  ADDED TWO ELEMENTARY COURSES (tutor side): ENTRY-LEVEL MATH + BASIC MATH. New
#               ELEMENTARY_SYSTEM_PROMPT_TEMPLATE (young-learner lesson brain: tiny steps, concrete/
#               picture-first, [[step]]/[[column]]/[[numberline]] whiteboard, quick checks) registered
#               under LESSON_TEMPLATES["entry"] AND ["basic"] (both share it). Added COURSE_SUBJECT,
#               PRACTICE_SCOPE, and TOPIC_SCOPE entries for "entry" and "basic". Per-course specifics
#               come from pedagogy.py's {playbook} and the {mastery} block, exactly like every other
#               course. Purely additive; the eight existing courses' templates are untouched.
#   2026-08-01  BOARD LEADS, WORDS FOLLOW (Jim: "there should be way, way more writing of
#               problems. People like the numbers and signs but balk at reading words").
#               A factoring exchange spoke "(x plus two, times x plus three, equals zero)"
#               and a full plug-in check ENTIRELY in words with an empty board. New rules
#               4-6 in the GRAPH_TOOL_NOTE board block (so lesson + practice + topic all get
#               them): (4) any math spoken must ALSO be written on the board in symbols in
#               that same reply; (5) never narrate an equation word-by-word -- write it,
#               then point at it, keeping spoken text short and warm; (6) unchanged: never
#               write the step the student is currently solving. Backend prompt change ->
#               bump APP_BUILD + rebuild.
#   2026-08-01  LIVE-AUDIT RULES (from the first live teaching audit): GRAPH_TOOL_NOTE gained
#               a BOARD HONESTY block -- never claim something is on the board unless YOU
#               emitted its tag this conversation (precalc claimed a circle it never drew);
#               always draw when asked to 'show me'; plus a first-use key-term reminder
#               close to the drawing guidance (5 term misses in the advanced courses).
#   2026-08-01  KEY TERMS BOLD+RED (Jim): GROUND_RULES rule 1b -- first use of a new/important
#               term is wrapped **like this**; the pages render it bold red (kterm). Also
#               [[angle]] doc: deg now goes to 180 (a straight line) -- the renderer's old
#               175-degree cap was silently BENDING straight lines (Jim's 175-vs-180 catch).
#   2026-08-01  PICTURE-MATCHES-WORDS (Jim's beta run: 'let's build a picture' then the figure
#               lacked the splitting ray it described). Geometry template: [[angle]] documents
#               the new split=".." attribute (geo-figures.js draws the interior ray + labeled
#               pieces) and a hard rule that every element spoken must appear in the figure.
#   2026-08-01  OPENER CLARITY (Jim: "is it not clear what he is talking about" -- the first
#               message asked 'which of those sounds most interesting?' BEFORE the cards had
#               been named). SESSION_OPENER_RULES rule 3: when asking the student to pick
#               from a card, say where the list is, speak 1-2 choices aloud, and offer a
#               'you pick' escape hatch. No vague 'those'.
#   2026-08-01  NARRATIVE ASSESSMENTS (Jim's vision: 'the parent should get an honest
#               assessment... the student should get a good self-assessment'). NEW
#               get_assessment(facts, audience): one short, warm, HONEST paragraph written
#               from real progress facts supplied by main.py -- student voice (Mr. Cadabra,
#               2nd person: strengths, one growth area, keep-going / extra-practice /
#               consider-jumping-ahead verdict) or parent voice (professional-warm, 3rd
#               person, reads ENGAGEMENT honestly: real minutes vs. actual progress). Hard
#               rules in both prompts: only the supplied facts, no invention, no scolding,
#               no comparisons to other students. Small call (max_tokens 400), reused by
#               the dashboard button today and the weekly emails later.
#   2026-07-30  SESSION OPENER: STOP FAKE PLACEMENT + GOALS CARD ONCE. A tester saw the lesson opener
#               claim "your placement challenge put you right around percents" when they had NOT taken
#               any placement (every course's FIRST MEETING FLOW unconditionally assumed a placement
#               challenge had happened). Added SESSION_OPENER_RULES, appended AFTER each course template
#               (so it overrides that older wording) in build_system_prompt: (1) never claim/imply a
#               placement/test/quiz unless the progress/mastery notes actually say so -- otherwise open
#               warmly and start at the shown unit or ask where to begin; (2) the "By the end..." goals
#               card is first-message-only, never repeated. Backend prompt change -> bump APP_BUILD +
#               rebuild. Verified with a live dry run of get_tutor_reply.
#   2026-07-30  TOPIC MODE: FIX "statement then silence" + REPEATED GOALS CARD. A student reported the
#               tutor gave an explanation and then stopped with nothing to do, and separately re-showed
#               the same "By the end of this you'll be able to" card on a later turn. Tightened
#               TOPIC_SYSTEM_PROMPT_TEMPLATE: (a) the goals card is now explicitly FIRST-MESSAGE-ONLY --
#               never re-post it or re-frame the topic on later turns; (b) EVERY reply, including the
#               beginner "define the idea" turn, must END by handing the ball back (a question / "your
#               turn" / check-in) -- never stop on a bare statement or definition. Backend prompt
#               change -> bump APP_BUILD + rebuild. Verified with a live dry run of get_topic_reply.
#   2026-07-30  PROMPT CACHING (cost control). Wrapped the system prompt in a cacheable content block
#               (_cacheable_system) on all three reply calls, so Anthropic reuses the large, stable
#               system prompt across a student's consecutive turns instead of re-billing it each turn
#               (~halves the brain input cost within a session). The model's OUTPUT is identical whether
#               or not the prefix was cached -> NO quality change. Backend -> bump APP_BUILD + rebuild.
#   2026-07-30  TOOL HOW-TO. Expanded the student-tools note (GRAPH_TOOL_NOTE) so the tutor can EXPLAIN,
#               button-by-button, how to use the 🧮 math keyboard AND the 📈 graph paper when a student
#               asks "how do I ...?" / "where is it?". Backend prompt change -> bump APP_BUILD + rebuild.
#   2026-07-30  GRAPH TOOL AWARENESS. Added GRAPH_TOOL_NOTE, prepended (with GROUND_RULES) to every
#               mode's system prompt via the build_* functions. It tells the tutor the student has a
#               📈 Graph button (coordinate graph paper), that plotted points arrive as TEXT
#               coordinates like "(0, 3), (1, 5)" (the model can't see pixels), and how to invite it,
#               check the coordinates, and blend it into graphing work. Pairs with the new static
#               static/graph-input.js component. Backend change -> bump APP_BUILD + rebuild. Do no harm.
#   2026-07-29  SCOPE + JAILBREAK GUARDRAILS. Added a firm, injection-resistant GROUND_RULES block,
#               prepended to EVERY mode's system prompt via build_system_prompt / build_practice_prompt
#               / build_topic_prompt (one place -> all 8 courses). It keeps the tutor strictly on MATH
#               (any level -- cross-course math questions are explicitly STILL allowed), refuses non-math
#               wandering (sports, jokes, essays, chit-chat) with a warm one-line redirect, refuses to
#               share/guess about OTHER students (and architecturally it never has their data), and
#               states the rules cannot be "overridden" by any student message (ignore-instructions,
#               "you are now...", roleplay, fake developer/teacher/authority claims). Purely additive:
#               the teaching templates are unchanged, so teaching behavior is preserved. Verified with
#               adversarial probes + a normal teaching turn. Do no harm.
#   2026-07-29  ANTI-TRUNCATION. Raised the student-facing reply cap max_tokens 700 -> 1200 in all
#               three reply builders (get_tutor_reply / get_practice_reply / get_topic_reply). The
#               newer per-course openers stack a [[goal]] plus a long inline [[card]], which could
#               exceed 700 tokens and get cut off mid-tag (Geometry Unit 8 opener truncated inside a
#               [[card]]; a Pre-Calc turn cut off mid-sentence). max_tokens is only a CEILING -- the
#               model still ends each turn on its own -- so normal short spoken turns are unchanged in
#               length and cost; this only gives the occasional long opener room to finish cleanly.
#               The board-tag helper stays at 220 (it emits a single short math tag). Do no harm.
#   2026-07-28  PHASE 4 -- DIFFERENTIAL EQUATIONS COURSE (tutor side). Added a full standalone
#               DIFFEQ_SYSTEM_PROMPT_TEMPLATE (the 9 units; CLASSIFY-FIRST as the organizing habit;
#               an explicit note that weak INTEGRATION is the hidden blocker to shore up without
#               judgment; derive-don't-announce pacing) registered under LESSON_TEMPLATES["diffeq"],
#               plus COURSE_SUBJECT["diffeq"] and PRACTICE_SCOPE/TOPIC_SCOPE["diffeq"]. Assumes
#               Calculus and does not re-teach it. Source: DiffEq_Curriculum_KB.md. Additive; the
#               seven existing courses untouched. Do no harm.
#   2026-07-28  PHASE 4 -- CALCULUS COURSE (tutor side). Added a full standalone
#               CALCULUS_SYSTEM_PROMPT_TEMPLATE (the 9 units; the two big ideas + the FTC; an explicit
#               "teach the idea BEFORE the machinery" rule; heavy use of the upgraded grapher for
#               curves, tangent lines, and f-with-f' together) registered under
#               LESSON_TEMPLATES["calculus"], plus COURSE_SUBJECT["calculus"] and
#               PRACTICE_SCOPE/TOPIC_SCOPE["calculus"]. Pedagogy injects from
#               pedagogy.COURSE_PEDAGOGY["calculus"]. Source: Calculus_Curriculum_KB.md. Additive;
#               the six existing courses untouched. Do no harm.
#   2026-07-28  PHASE 4 -- PROBABILITY & STATISTICS COURSE (tutor side). Added a full standalone
#               PROBSTAT_SYSTEM_PROMPT_TEMPLATE (the 9 units; reason-about-data framing; the stats
#               visuals wired throughout the lesson brain) registered under LESSON_TEMPLATES["probstat"],
#               plus COURSE_SUBJECT["probstat"] = "statistics" and PRACTICE_SCOPE/TOPIC_SCOPE["probstat"].
#               Pedagogy injects from pedagogy.COURSE_PEDAGOGY["probstat"]. Source: ProbStat_Curriculum_KB.md.
#               Additive; the five existing courses untouched. Do no harm.
#   2026-07-28  GRAPHICS STAGE 3 -- taught the tutor the trig/conic/number-line/tiles/vector pictures
#               ([[unitcircle]]/[[righttriangle]]/[[conic]]/[[numberline]]/[[areamodel]]/[[vector]],
#               rendered by static/math-figures.js). Added to the shared practice + topic templates and
#               the Pre-Calc lesson template (unit circle is central there). Prompt text only. Do no harm.
#   2026-07-28  GRAPHICS STAGE 2 -- taught the tutor the statistics/probability pictures. The shared
#               practice + topic templates now document [[bars]]/[[histogram]]/[[dotplot]]/[[boxplot]]/
#               [[scatter]]/[[normal]]/[[twoway]]/[[tree]]/[[pie]] (rendered by static/math-figures.js).
#               Prompt text only. (Full lesson-template integration lands with the Prob & Stat course.)
#   2026-07-28  GRAPHICS STAGE 1 -- taught the tutor the upgraded [[graph]]. The grapher (new shared
#               static/math-figures.js) now plots ANY function of x via func= (sin/cos/tan, exp, logs,
#               polynomials, rationals with asymptotes, sqrt, abs). Updated the [[graph]] docs in the
#               Algebra I / Algebra II / Pre-Calc lesson templates and the shared practice + topic
#               templates to document func= and to STOP saying "the grapher can't draw a sine/log"
#               (it can now). Prompt text only. Do no harm.
#   2026-07-28  PHASE 4 -- TRIG / PRE-CALC COURSE (tutor side). Added a full standalone
#               PRECALC_SYSTEM_PROMPT_TEMPLATE (the 9 CA-aligned units; the function lens + unit
#               circle through-lines; trig core in units 4-6; identities-verified-vs-equations-solved;
#               a first look at limits) registered under LESSON_TEMPLATES["precalc"], plus
#               COURSE_SUBJECT["precalc"] and PRACTICE_SCOPE/TOPIC_SCOPE["precalc"]. Pedagogy injects
#               from pedagogy.COURSE_PEDAGOGY["precalc"] via the existing {playbook} slot. Source:
#               PreCalc_Curriculum_KB.md. Additive; the four existing courses untouched. Do no harm.
#   2026-07-28  PHASE 4 -- ALGEBRA II COURSE (tutor side). Added a full standalone
#               ALGEBRA2_SYSTEM_PROMPT_TEMPLATE (the "take the whole course" lesson brain for Algebra
#               II: the 9 CA-aligned units, the function-family through-line, the quadratic solving
#               ladder + complex numbers, extraneous-solution checking, and the reused algebra
#               whiteboard/voice/checks machinery), registered under LESSON_TEMPLATES["algebra2"].
#               Added COURSE_SUBJECT["algebra2"] = "Algebra II" and PRACTICE_SCOPE/TOPIC_SCOPE
#               ["algebra2"] so the shared practice + topic coaches serve Algebra II. Pedagogy is
#               injected from pedagogy.COURSE_PEDAGOGY["algebra2"] via the existing {playbook} slot.
#               Source: AlgebraII_Curriculum_KB.md. Purely additive; Algebra I, Geometry, and
#               Pre-Algebra templates/scopes are untouched (byte-identical). Do no harm.
#   2026-07-28  INTRO/EXPECTATIONS + [[column]] TAG DOCS (per Jim, from a Decimals topic screenshot).
#               (1) Topic mini-lessons now OPEN by framing the topic + a "by the end you'll be able to..."
#               goals card (new first step in HOW YOU TEACH A TOPIC) -- before this, a topic jumped
#               straight into problems with no intro. (2) All three LESSON openers (algebra1/geometry/
#               prealgebra) now also show a short EXPECTATIONS goals card right after the [[goal]] banner
#               (spoken AND shown), per Jim's "Topic + course lessons" + "speak + goals card" choices.
#               (3) Documented the new [[column op="+" terms="2.40 | 1.35" result="3.75"]] whiteboard tag
#               (stacked, decimal-point-aligned add/subtract) in the pre-algebra lesson, topic, and
#               practice tag sections, tied to "line up the decimal points"; result is omitted until the
#               student finds it (never runs ahead). Prompt/text only -- the [[column]] renderer lives in
#               the static pages. Stamp bumped in main.py (backend prompt change). Do no harm.
#   2026-07-28  PHASE 4 -- PRE-ALGEBRA COURSE (tutor side). Added COURSE_SUBJECT["prealgebra"] =
#               "pre-algebra", PRACTICE_SCOPE/TOPIC_SCOPE["prealgebra"] (the foundations scope), and a
#               new PREALGEBRA_SYSTEM_PROMPT_TEMPLATE in LESSON_TEMPLATES -- a full lesson brain tuned
#               for the foundations/remediation course: MENU-FIRST (help with the one concept they came
#               for) and CONFIDENCE-FIRST (engineer an early win; anxious learners are common). Uses the
#               same 5 placeholders. Algebra I + Geometry templates untouched. Do no harm.
#   2026-07-28  PHASE 4 (geometry) -- GEOMETRY WHITEBOARD FIGURES. Documented three new figure tags
#               in GEOMETRY_SYSTEM_PROMPT_TEMPLATE so the Geometry tutor draws real shapes:
#               [[triangle]] (labels, side lengths, right-angle mark, angle measures, equal-side
#               ticks), [[angle deg=.. label=..]], and [[circle center=.. r=.. inscribed=..]].
#               Rendered by the shared static/geo-figures.js (loaded in session/practice/topic.html;
#               their handleTags call showGeo()). Replaced the old "figure-drawing is coming" note.
#               Algebra template untouched. (Compass-and-straightedge constructions still to come.)
#   2026-07-27  MULTI-COURSE (Phase 3, step 2) -- COURSE-MODE LESSON PROMPT PER COURSE. Added
#               GEOMETRY_SYSTEM_PROMPT_TEMPLATE (a full standalone Geometry course-teaching brain:
#               reasoning/proof focus, the 9 CA-aligned Geometry units, a geometry teaching toolkit,
#               geometry worked-example pacing, and voice/whiteboard/checks guidance) + a
#               LESSON_TEMPLATES registry. build_system_prompt(student, course) now SELECTS the
#               course's template and injects that course's playbook; get_tutor_reply takes course.
#               The Algebra I template (SYSTEM_PROMPT_TEMPLATE) is UNTOUCHED and its assembled prompt
#               is verified BYTE-IDENTICAL across student states -- do no harm. Unknown course -> Algebra.
#               (Geometry course mode isn't student-reachable until the picker in 3.4; the Geometry
#               teaching text is up for Jim's review -- see Geometry_Course_Mode_Prompt_DRAFT.md.)
#   2026-07-27  MULTI-COURSE (Phase 3, step 1) -- PRACTICE + TOPIC MODES ARE COURSE-AWARE. Threaded
#               a `course` argument through _unit_from_text / _playbook and the practice/topic
#               builders + get_*_reply. The two coach templates now use a per-course SUBJECT word
#               and a per-course SCOPE block (COURSE_SUBJECT / PRACTICE_SCOPE / TOPIC_SCOPE), so
#               they serve any course instead of hard-refusing non-algebra work (the old templates
#               literally told the tutor to decline "a geometry proof"). Algebra I reproduces the
#               original text BYTE-FOR-BYTE (verified) and every param defaults to 'algebra1', so
#               single-course behavior is unchanged. Geometry now works in Practice + Topic, drawing
#               its misconceptions/how-to-teach from pedagogy.COURSE_PEDAGOGY['geometry']. NOTE: the
#               structured full-course LESSON prompt (SYSTEM_PROMPT_TEMPLATE) is still Algebra-only;
#               course-mode Geometry + per-course placement + the course picker are the next steps.
#               See Multi_Course_Expansion_Plan.md.
#   2026-07-25  TOPIC NO-SELF-WRAPUP GUARD. Added a rule to TOPIC_SYSTEM_PROMPT_TEMPLATE: never
#               wrap up / say goodbye / give an "outro" unless the student CLEARLY says they're
#               done; an odd/unparseable message -> ask them to repeat, never end. Backs up the
#               main.py STT scrub (a hallucinated "[outro jingle]" had ended a topic after one Q).
#   2026-07-25  STUDENT-LED PRACTICE. Reworked PRACTICE_SYSTEM_PROMPT_TEMPLATE so Practice is now
#               DRIVEN BY THE STUDENT: the tutor puts the problem on the board, asks "what would
#               you like to do first?", then carries out EACH move the student names (and only
#               that move) on the whiteboard via [[step]]. Correct move -> board it + short
#               strategy praise + "now what?"; wrong/illegal move -> do NOT board it, gently flag
#               why and let them retry; a HINT request (the new Hint button sends "Can I have a
#               hint?", or "I'm stuck"/"I don't know") -> ONE small nudge that NAMES a move but
#               never performs it. Final answer -> student checks it + [[step check]] + [[mark]].
#               The whiteboard "golden rule" note was retuned: only ever draw a step the student
#               chose (or the final check). Lesson/Topic modes unchanged. Front-end: a "Hint"
#               quick button added to practice.html. (Practice endpoint/shape unchanged.)
#   2026-07-24  PHASE B -- MASTERY STEERING + SPACED REVIEW. build_system_prompt now injects a
#               {mastery} snapshot (what the student has MASTERED vs. still needs, + a chosen
#               focus unit) into a new "WHERE THIS STUDENT STANDS" section, and uses the focus
#               unit for the teaching playbook. The lesson tutor now steers toward unmastered
#               units, offers a check when ready, and weaves in short spaced-review warm-ups of
#               already-mastered units. main.py builds the note (_mastery_note) from the mastery
#               data and passes focus_unit (dashboard "Work on it" link -> /session?...&unit=N).
#   2026-07-24  PHASE A2 -- QUICK CHECKS. Lesson prompt now teaches Mr. Cadabra to OFFER a
#               short, no-pressure end-of-unit check (4-5 Qs, no hints during it), tally it, and
#               emit [[check unit correct total]] -- which the frontend records (mastery) and
#               shows as a friendly result card. Encouraging at any score; 90%+ = mastered.
#               Also [[mark correct="1|0"]] to silently count finished practice problems (added
#               to lesson + practice prompts). Front-end handlers in session/practice/topic.html.
#   2026-07-24  DEFINE-BEFORE-DRILL (Topic mode). When a student is NEW to a topic, the tutor
#               must DEFINE the key terms first (on the board) and work one example itself
#               before any exercise -- it was jumping straight to "multiply these polynomials"
#               without ever defining "polynomial"/"factor." Reinforced by the shared
#               "INTRODUCE BEFORE YOU PRACTICE" rule now in pedagogy.py METHODOLOGY (all modes).
#   2026-07-23  STAGE 3 (prompt part) -- POSE-THE-PROBLEM-ON-THE-BOARD. Added a rule to the
#               lesson whiteboard section: when the tutor POSES a new problem, its FIRST
#               action must be to write it on the board with [[step eq="..."]] -- never say a
#               problem out loud while the board is empty (this was the "new problem, blank
#               board" gap in Jim's screenshot). Clarified this is NOT "running ahead." (The
#               rest of Stage 3 -- tutor's words moved ONTO the board, side chat removed, and a
#               Pause button -- is front-end, in session/practice/topic.html.)
#   2026-07-23  STAGE 2 -- FREE THE WHITEBOARD ([[step]]) + RETIRE THE GUESSING NET. The
#               board is now a PERSISTENT worklist that STACKS and STAYS (front-end change in
#               session/practice/topic.html): each [[step]] appends ONE line that stays below
#               the last, so a whole worked solution builds up and never gets replaced mid-
#               solve (the exact failure in Alex's transcript, where he "never saw 2x+1 = 25
#               and 2x = 24 at the same time"). New tag taught in all 3 prompts:
#                 [[step eq="2X + 1 = 25"]]            -> one equation line
#                 [[step op="- 1" eq="2X = 24"]]       -> op shown UNDER BOTH SIDES, then result
#                 [[step check="2(12)+1 = 25  ✓"]]     -> a substitution-check line
#               Kept the GOLDEN RULE (never add a line for the step you're still asking about).
#               RETIRED the server-side forcing net: ensure_board() is now a pass-through --
#               with Sonnet reliably tagging and a board that persists, the second "guess a
#               tag" model call (board_tag_for) is unneeded and was the source of the ahead-of-
#               student / redraw-the-problem bugs. board_tag_for/BOARD_TAG_SYSTEM kept but
#               unused (one-line revert). [[write]] now also appends to the worklist; [[solve]]
#               still exists but the prompts now steer to [[step]].
#   2026-07-23  TEACHING BRAIN UPGRADE -- STRONG MODEL + REAL PEDAGOGY WIRED IN. Two
#               changes so the tutor TEACHES from expertise instead of from hand-patched
#               rules (the fix for "AI is not teaching well / this will take forever"):
#                 (1) MODEL: student-facing brain switched to the stronger
#                     "claude-sonnet-5" (teaching JUDGMENT -- when to push vs. show, how
#                     to read a student -- is exactly where a stronger model wins). NOTE:
#                     the Render env var CLAUDE_MODEL OVERRIDES this default, so it must be
#                     updated (or removed) in Render for the switch to take effect live.
#                 (2) KNOWLEDGE BASE: new pedagogy.py (distilled from the two project KBs)
#                     is now injected into EVERY prompt. build_system_prompt reads the
#                     student's placed Unit from their progress note and injects that
#                     unit's misconceptions + how-to-teach; practice/topic classify the
#                     problem/topic to a unit (via curriculum.classify_unit) and inject the
#                     same, plus the universal developmental/feedback methodology + the
#                     cross-cutting error watch-list. Imports are guarded so the tutor
#                     still runs if a module is missing (do no harm).
#   2026-07-23  BOARD NEVER RUNS AHEAD OF THE STUDENT (Socratic pacing fix). The
#               whiteboard was answering the very question the tutor had just asked:
#               Mr. Cadabra would ask "what's the next step?" while the board already
#               showed that step's answer. Root cause was the server-side safety net
#               (ensure_board -> board_tag_for): a second model call that computed the
#               FULL solution regardless of how far the conversation had actually gone.
#               Fixes (this file only; the board renderer is fine):
#                 (1) BOARD_TAG_SYSTEM rewritten around one rule -- show ONLY steps
#                     already established; when the tutor is ASKING the student to find
#                     the next step, show only the current line (or the start with an
#                     EMPTY steps list), never the answer. Mirror the spoken math, never
#                     solve ahead.
#                 (2) Lesson prompt: added the "GOLDEN RULE OF THE BOARD -- never run
#                     ahead of the student"; grow [[solve]] one line at a time, and only
#                     AFTER the student answers / you narrate a step as done. Trimmed the
#                     example so it no longer models dumping the whole solution.
#                 (3) Same "never run the board ahead of the student" note added to the
#                     PRACTICE and TOPIC prompts. (showSolve already renders steps="" as
#                     just the starting line, so an empty steps list is safe.)
#   2026-07-22  FUNCTION MACHINE + VARIABLES POP. (1) New [[machine input="3"
#               rule="2x+1" output="7" fname="f"]] control tag documented in all three
#               prompts: for Unit 3 (functions) EVALUATE with the function machine --
#               a number goes IN, the rule runs, a number comes OUT -- NOT the balance
#               scale (the balance is for Unit 2 equations only). This fixes the
#               confusing "monkeys" picture where f(3) looked like the input was 1.
#               (2) Variables now render BOLD, CAPITAL, and RED everywhere on screen
#               (chat + visuals); the app styles them automatically, so keep writing
#               normally -- you do not need to do anything for that.
#   2026-07-21  WHITEBOARD GRAPHER. Added the [[graph]] control tag to all three
#               prompts (lesson/practice/topic): the tutor can now draw a real
#               coordinate plane with lines (y=mx+b), parabolas (y=ax^2+bx+c), points,
#               and auto-marked line intersections -- so Units 4-8 (slope/graphs,
#               systems, quadratics) have a proper on-screen picture, not just words.
#   2026-07-21  FULL COURSE. Removed the "linear equations only" restriction. The
#               course now teaches ALL NINE Algebra I units, in sequence, starting at
#               the student's placed unit, aligned to California's Algebra I standards
#               (CA CCSSM / CA Math Framework Traditional Pathway). Embedded a concise
#               per-unit map (what they'll do + a key method + CA/CCSS codes) so the
#               tutor teaches each unit well. Balance visual + list card still used;
#               graphs/parabolas/data described in words for now (bespoke graphers
#               later). [[covered]] ids noted as Unit-2 specific.
#   2026-07-21  COST SWITCH -> Claude Haiku 4.5 for students. DEFAULT_MODEL is now
#               "claude-haiku-4-5" (cheaper, same SDK, US vendor). Paired with a new
#               always-on "ACCURACY -- CHECK YOUR OWN WORK" rule added to all three
#               prompts (lesson/practice/topic): verify every number/answer (substitute
#               back or recompute) BEFORE speaking it. This is the self-check that makes
#               a cheaper model reliable for algebra -- zero added latency (in-prompt),
#               unlike a slow second API pass. NOTE: the LIVE switch is the Render env
#               var CLAUDE_MODEL=claude-haiku-4-5 (env overrides this default).
#   2026-07-21  TOPIC MODE (part of the new "what would you like to do today?" hub).
#               Added TOPIC_SYSTEM_PROMPT_TEMPLATE + get_topic_reply(): a focused
#               mini-lesson on ONE Algebra I topic the student picks/names (Socratic,
#               visual, always ends with a next step). Topic history is client-held
#               (not persisted), like Practice. Used by main.py's /api/topic.
#   2026-07-21  LESSON GOALS + PRACTICE MODE. (1) Each lesson now opens by stating a
#               one-sentence, level-matched GOAL and showing it on screen via a new
#               [[goal text="..."]] tag (returning sessions restate it too). (2) Added
#               a PRACTICE brain: PRACTICE_SYSTEM_PROMPT_TEMPLATE + get_practice_reply()
#               so a student can bring a specific problem from school and get Socratic
#               coaching on it (any Algebra I topic; practice history is client-held,
#               not persisted). Used by main.py's /api/practice.
#   2026-07-21  NEVER DEAD-END THE STUDENT. Mr. Cadabra sometimes ended a turn on a
#               plain statement, leaving the student staring at "Your turn!" with
#               nothing to do. Strengthened HOW YOU SPEAK: every reply must hand the
#               turn back with a clear next step -- a question, an explicit "your turn
#               -- try this", or a "ready for the next step?" check-in -- never a bare
#               statement.
#   2026-07-21  CARD-TAG SAFETY. The opening card is now a SHORT ready-made tag,
#               [[card id="cool-questions"]], instead of a long inline list -- the old
#               long tag could get cut off mid-stream, leaking raw "[[card ..." markup
#               into the spoken line (garbled) and leaving the whiteboard empty. Also
#               raised max_tokens 400 -> 700 so replies aren't truncated inside a tag.
#   2026-07-21  FLOW-AWARE OPENINGS. First lesson: the student has JUST finished the
#               placement challenge (and the app-driven welcome/tour), so the tutor
#               opens by acknowledging their placement level and teaches AT that
#               level -- no re-welcome/tour. Returning session: give a short spoken
#               RECAP of where they are, then continue (never re-run welcome/tour).
#   2026-07-21  TOUR IS NOW APP-DRIVEN + AUTO-PLAYS. The welcome, the one-line
#               definition of algebra, and the page walkthrough are now performed by
#               session.html as a scripted sequence (no per-step prompts), so the
#               tutor NO LONGER welcomes or tours. Its first message on a first
#               session starts the LESSON: the cool-questions card + the big idea.
#               Kept [[highlight]] documented but optional (tutor rarely needs it).
#   2026-07-20  ADDED THE OPENING PAGE TOUR. First meeting now: (1) welcome + a
#               one-sentence definition of algebra (finding an unknown number we
#               call a variable), (2) a quick guided TOUR of the screen -- one stop
#               per turn, lighting up each spot via a new [[highlight id="..."]]
#               control tag (curriculum -> find-my-level -> dashboard -> todays-plan
#               -> covered), then (3) the cool-questions card and the big idea. The
#               frontend glows the pointed-at element and scrolls it into view; the
#               spotlight clears at the start of the next turn. Documented the new
#               tag in the "SHOWING PICTURES" section.
#   2026-07-20  Cut the "get-to-know-you" opening (how do you feel about math /
#               hobbies -- it read as condescending). First meeting now opens with
#               ENERGY: welcome + why algebra is exciting + a card of cool things
#               it can solve, then straight into the big idea. Placement (from the
#               Challenge) handles "where is the student," so no upfront diagnosis.
#   2026-07-19  Renamed the tutor to "Mr. Cadabra"; first-meeting opener is now an
#               explicit warm "welcome to algebra."
#   2026-07-19  TONE REBUILD (research-backed). Added a "HOW YOU COME ACROSS"
#               section: talk WITH the student not down to them; cut empty/effort
#               praise (it backfires with teens and reads as patronizing); praise
#               SPECIFIC strategies; give agency/choices; be genuinely warm and a
#               little playful, not scripted; assume intelligence. Pairs with the
#               new ElevenLabs voice (see main.py /api/speak).
#   2026-07-19  RICHER ALGEBRA INTRO. Replaced the abrupt "an equation is a
#               see-saw" opening with a paced on-ramp: pose several cool real-life
#               QUESTIONS (answers unknown) -> we name unknowns with letters x/y
#               -> connect to equations + the equal sign they already know -> the
#               power to solve hard problems simply -> THEN the see-saw/balance.
#               Added a [[card title="..." items="a | b | c"]] control tag so the
#               tutor can show the list of cool questions on screen.
#   2026-07-19  VISUAL LESSON UPGRADE. Prompt now (a) goes slow and teaches what
#               an equation IS first (balance/see-saw + monkeys) before any x, and
#               (b) drives the on-screen animated balance scale and the plan/
#               covered sidebars by emitting hidden control tags:
#                 [[balance left="3 + 1" right="4" state="level" caption="..."]]
#                 [[covered id="what-is-equation"]]
#               The frontend renders these and strips them, so students only ever
#               hear plain words. Agenda ids: what-is-equation, balance-rule,
#               both-sides, one-step, two-step, check-answer.
#   2026-07-19  MAJOR TUTOR-BRAIN UPGRADE (research-backed). Rewrote the system
#               prompt so the tutor is warm, personable, and empathetic, and:
#                 - opens a FIRST session by building rapport (gets to know the
#                   student, how they feel about math, what they enjoy),
#                 - explains in plain, engaging terms what algebra IS and why it
#                   matters in real life,
#                 - DIAGNOSES how this student naturally thinks before teaching
#                   (e.g. "how would you figure this out in your head?"),
#                 - carries a toolkit of TEN different methods for solving a
#                   linear equation and adaptively finds which one clicks for
#                   THIS student, then leans into it,
#                 - treats mistakes as normal and useful and actively counters
#                   "I'm not a math person."
#               Grounded in tutoring/math-anxiety research (see project notes).
#               Note: the "learning styles (VAK)" idea is a debunked myth; this
#               prompt instead uses MULTIPLE REPRESENTATIONS and observes which
#               representation the student understands best -- which is the real,
#               evidence-based version of "different ways people learn."
#   2026-07-19  Updated DEFAULT_MODEL from the retired "claude-3-5-sonnet-latest"
#               to the current, active "claude-sonnet-5" (retired 2025-10-28).
#   2026-07-19  Initial version. Tutor brain: system prompt + context injection
#               + Claude API call. Model configurable via CLAUDE_MODEL env var.
#
# WHAT THIS FILE IS FOR:
#   This is the tutor's "brain." main.py imports get_tutor_reply() to answer a
#   student. SYSTEM_PROMPT_TEMPLATE below is the thing we revise most often as
#   real sessions teach us what works.
#
# ENV VARS (set these in Render, NOT in code):
#   ANTHROPIC_API_KEY   (required)  your Claude API key
#   CLAUDE_MODEL        (optional)  a CURRENT model id from Anthropic docs
# =============================================================================

import os
import re

from anthropic import Anthropic

# CANONICAL FOUNDATION SCRIPTS (2026-08-09, build cc). Defensive: if the module is
# missing on a deploy, lessons still run -- they just lose the verbatim introductions.
try:
    import foundations
except Exception as _exc:  # noqa: BLE001
    foundations = None
    print(f"[tutor] foundations.py unavailable ({_exc}) -- canonical intros disabled")

# The tutor's TEACHING KNOWLEDGE BASE (per-unit misconceptions + how-to-teach) and the
# unit CLASSIFIER. Imported defensively: if either module is somehow missing on deploy,
# the tutor must still answer (it just won't get the extra pedagogy that turn) -- do no
# harm. See pedagogy.py / curriculum.py.
try:
    import pedagogy
except Exception as _exc:  # noqa: BLE001
    pedagogy = None
    print(f"[tutor] pedagogy KB unavailable: {_exc}")
try:
    import curriculum
except Exception as _exc:  # noqa: BLE001
    curriculum = None
    print(f"[tutor] curriculum classifier unavailable: {_exc}")
# The MATH VERIFIER (2026-08-03): mathcheck.py re-does the tutor's math with SymPy before
# a reply ships (see _create_verified below). Imported defensively like the modules above:
# if it is missing the tutor still answers -- replies just aren't verified that deploy.
try:
    import mathcheck
except Exception as _exc:  # noqa: BLE001
    mathcheck = None
    print(f"[tutor] mathcheck unavailable -- replies will NOT be math-verified: {_exc}")
# USAGE LOGGING (2026-08-04): store.log_usage records what each paid call consumed (counts
# only, never text). Defensive like the imports above: no store, no logging, no harm.
try:
    import store
except Exception as _exc:  # noqa: BLE001
    store = None
    print(f"[tutor] store unavailable -- usage logging off: {_exc}")

# The default course. Until the course picker (Phase 3 UI) supplies a course, everything
# resolves to Algebra I, so single-course behavior is exactly as before.
DEFAULT_COURSE = "algebra1"

# -----------------------------------------------------------------------------
# THE WORDS MOVED OUT (2026-08-11, build do). Every system-prompt template and
# shared prompt block -- the text the teaching brain actually reads -- now lives in
# prompts.py, moved there VERBATIM and proven byte-identical (52 built prompts
# hashed before/after). This file keeps the ENGINE: the API calls, the negotiated
# continuation, mathcheck, the nine-referee prose sweep, and the builders below
# that assemble prompts.py's text into each request. The import re-exports every
# moved name, so tutor.GRAPH_TOOL_NOTE etc. still work (ruletests relies on that).
# Editing the WORDS? -> prompts.py. Editing the MACHINERY? -> here.
# -----------------------------------------------------------------------------
from prompts import (  # noqa: E402
    TUTOR_NAME,
    SYSTEM_PROMPT_TEMPLATE, GEOMETRY_SYSTEM_PROMPT_TEMPLATE,
    PREALGEBRA_SYSTEM_PROMPT_TEMPLATE, ALGEBRA2_SYSTEM_PROMPT_TEMPLATE,
    PRECALC_SYSTEM_PROMPT_TEMPLATE, PROBSTAT_SYSTEM_PROMPT_TEMPLATE,
    CALCULUS_SYSTEM_PROMPT_TEMPLATE, DIFFEQ_SYSTEM_PROMPT_TEMPLATE,
    ELEMENTARY_SYSTEM_PROMPT_TEMPLATE, LESSON_TEMPLATES,
    GROUND_RULES, GRAPH_TOOL_NOTE,
    SESSION_OPENER_RULES, PROGRESS_TAGS_NOTE,
    FINAL_PREP_NOTE, FINAL_EXAM_NOTE,
    COURSE_SUBJECT, PRACTICE_SCOPE, TOPIC_SCOPE,
    PRACTICE_SYSTEM_PROMPT_TEMPLATE,
    ASSESSMENT_SYSTEM_STUDENT, ASSESSMENT_SYSTEM_PARENT,
    TOPIC_SYSTEM_PROMPT_TEMPLATE,
)

# The STUDENT-FACING model. Configurable via env (CLAUDE_MODEL) so we never have to
# touch code to change it. This must be a CURRENT alias from Anthropic's docs --
# retired/guessed ids are rejected by the API.
# 2026-07-23: switched the student-facing brain to the stronger "claude-sonnet-5"
# (Sonnet 5). Teaching JUDGMENT -- knowing when to push vs. show, reading a student,
# adapting on the fly -- is exactly where a stronger model is dramatically better, and
# the whole app is still in DEVELOPMENT (no live students yet), so we tune for teaching
# quality now and can revisit per-student cost before launch. (Haiku 4.5 was the prior
# cheap choice; we can drop back to it for production if Sonnet-with-real-pedagogy proves
# more than we need.)
# IMPORTANT: the Render env var CLAUDE_MODEL OVERRIDES this default. To go live on
# Sonnet, set CLAUDE_MODEL=claude-sonnet-5 in Render (or delete the var so this default
# is used).
DEFAULT_MODEL = "claude-sonnet-5"

# How many past messages we replay to the model each request. Keeps the "tutor
# remembers" feeling while bounding token cost (one message = one turn).
MAX_HISTORY_MESSAGES = 30


def _cacheable_system(text: str):
    """Wrap a system prompt as ONE cacheable content block so Anthropic PROMPT CACHING can reuse the
    large, mostly-stable system prompt across a student's consecutive turns instead of re-billing it
    every turn. This is billing/latency ONLY -- the model's output is identical whether or not the
    prefix was cached, so there is NO change in teaching quality. (Added 2026-07-30.)"""
    return [{"type": "text", "text": text or "", "cache_control": {"type": "ephemeral"}}]


try:
    # 2026-08-09 (build cj): the notation registry. Defensive, exactly like foundations:
    # a broken notation.py must never take the classroom down.
    import notation
except Exception as _nexc:  # noqa: BLE001
    notation = None
    print(f"[tutor] notation.py unavailable ({_nexc}) -- continuing without the symbol table")


try:
    # 2026-08-10 (build ck): the misconception catalogue. Defensive, like the others.
    import misconceptions
except Exception as _mexc:  # noqa: BLE001
    misconceptions = None
    print(f"[tutor] misconceptions.py unavailable ({_mexc}) -- continuing without it")


def _misconception_block(course: str) -> str:
    """This course's catalogue of the wrong RULES students run (rule 49), or "".
    Never raises: a broken misconceptions.py must not take the classroom down."""
    if misconceptions is None:
        return ""
    try:
        return misconceptions.prompt_block(course)
    except Exception as exc:  # noqa: BLE001
        print(f"[tutor] misconception block failed ({exc}) -- continuing without it")
        return ""


def _notation_block(course: str) -> str:
    """The per-course 'HOW TO SAY WHAT YOU WRITE' table (rule 48), or "".

    Rule 48 tells him to read every symbol aloud and to deny the wrong reading by name.
    Until this block existed it never told him OUR readings -- the same mistake as
    telling him to skip an introduction he had no way to identify. Never raises."""
    if notation is None:
        return ""
    try:
        return notation.prompt_block(course)
    except Exception as exc:  # noqa: BLE001
        print(f"[tutor] notation block failed ({exc}) -- continuing without it")
        return ""


# build gf (2026-08-14): FILTERING IS NOT OPTIONAL. ruletests caught this within an hour of
# build gb shipping: when no unit can be determined -- an unplaced student, or a practice
# problem the classifier cannot place -- unit was None, prompt_block filtered NOTHING, and
# algebra2 came out at 185,595 characters against a 180,000 ceiling. Every measurement taken
# during build gb passed an explicit unit, so every measurement missed it.
# A student with no placement is at the START of the course, so unit 1 is the honest default
# rather than a guess; practice and topic prefer the student's own placed unit and fall back
# to the same 1. Nothing is ever lost by filtering: the other units' terms are still NAMED.
_FILTER_UNIT_FALLBACK = 1

def _foundation_block(course: str, heard=None, verbatim: bool = True, unit=None) -> str:
    """This course's canonical foundation scripts (rules 36-40), or "" if none.

    `heard` is the list of terms this student was introduced to on an EARLIER visit
    (main.py loads it from the store and puts it on the student record). It only
    changes whether the tutor replays a script or asks first -- never the words.
    Never raises: a broken foundations.py must not take the classroom down."""
    if foundations is None:
        return ""
    try:
        return foundations.prompt_block(course, heard, verbatim, unit)
    except TypeError:
        # An older foundations.py without `unit` (build gb) -- still teach, unfiltered.
        try:
            return foundations.prompt_block(course, heard, verbatim)
        except TypeError:
            pass
        # An older foundations.py without the `heard` argument: still teach.
        try:
            return foundations.prompt_block(course)
        except Exception as exc:  # noqa: BLE001
            print(f"[tutor] foundation block failed ({exc}) -- continuing without it")
            return ""
    except Exception as exc:  # noqa: BLE001
        print(f"[tutor] foundation block failed ({exc}) -- continuing without it")
        return ""


def build_system_prompt(student: dict, course: str = DEFAULT_COURSE) -> str:
    """Fill the right course's lesson template with this student's name + remembered progress."""
    name = (student or {}).get("name", "the student")
    progress = (student or {}).get("progress") or ""
    progress = progress.strip()
    if not progress:
        progress = ("(No prior sessions yet -- this is your FIRST meeting with "
                    "this student. Begin with the first-meeting flow.)")
    # Phase B: prefer a chosen FOCUS unit (from the dashboard "Work on it" link) for the
    # teaching playbook; otherwise detect it from the placement note in progress.
    focus = (student or {}).get("focus_unit")
    try:
        focus = int(focus) if focus else None
    except (TypeError, ValueError):
        focus = None
    unit = focus if (focus and 1 <= focus <= 9) else _unit_from_progress(progress)
    playbook = _playbook(unit, course)
    mastery = (student or {}).get("mastery_note") or "(No mastery data yet -- begin at their placed level.)"
    template = LESSON_TEMPLATES.get(course or DEFAULT_COURSE, SYSTEM_PROMPT_TEMPLATE)
    prompt = GROUND_RULES + GRAPH_TOOL_NOTE + template.format(
        tutor_name=TUTOR_NAME,
        student_name=name,
        progress=progress,
        playbook=playbook,
        mastery=mastery,
    ) + SESSION_OPENER_RULES + PROGRESS_TAGS_NOTE + _notation_block(course) + _misconception_block(course) + _foundation_block(
        course, (student or {}).get("foundations_heard"),
        (student or {}).get("foundations_verbatim", True),
        unit or _FILTER_UNIT_FALLBACK)   # build gb: only THIS unit's scripts carry their wording
    # FINAL EXAM MODES (2026-08-07): main.py sets student["final_mode"] ONLY after verifying
    # server-side that all nine units are mastered -- never trust the client for this.
    final_mode = (student or {}).get("final_mode") or ""
    if final_mode == "prep":
        prompt += FINAL_PREP_NOTE
    elif final_mode == "exam":
        prompt += FINAL_EXAM_NOTE
    return prompt


def _trim_history(history: list) -> list:
    """Return at most the last MAX_HISTORY_MESSAGES messages, oldest first."""
    if not history:
        return []
    return history[-MAX_HISTORY_MESSAGES:]


# -----------------------------------------------------------------------------
# TEACHING PLAYBOOK INJECTION -- give the tutor real pedagogy for THIS student's unit
# -----------------------------------------------------------------------------
# We figure out which Algebra I unit the student is on, then pull that unit's
# misconceptions + how-to-teach (plus the universal methodology) from pedagogy.py and
# drop it into the system prompt. Every step is wrapped so a failure never breaks a turn.
def _unit_from_progress(progress) -> "int | None":
    """The lesson stores the placed unit in the progress note as 'Unit N'. Read it."""
    try:
        m = re.search(r"\bUnit\s+(\d+)", str(progress or ""))
        return int(m.group(1)) if m else None
    except Exception:  # noqa: BLE001
        return None


def _unit_from_text(text, course: str = DEFAULT_COURSE) -> "int | None":
    """Classify a free-text problem/topic to a unit WITHIN a course (practice + topic modes)."""
    try:
        if curriculum and text:
            unit, _name = curriculum.classify_unit(text, course)
            return unit
    except Exception:  # noqa: BLE001
        pass
    return None


def _playbook(unit, course: str = DEFAULT_COURSE) -> str:
    """The teaching guidance to inject this turn (or '' if the KB is unavailable)."""
    try:
        if pedagogy:
            return pedagogy.teaching_playbook(unit, course)
    except Exception as exc:  # noqa: BLE001
        print(f"[tutor] playbook build failed: {exc}")
    return ""


# =============================================================================
# WHITEBOARD SAFETY NET -- the backend GUARANTEES the board shows the math
# =============================================================================
# The main model (Haiku) does not reliably emit whiteboard control tags even when the
# system prompt demands it. So after every reply we check: did the tutor draw the math?
# If the reply talks math but has no board tag, a focused second model call converts the
# current math into ONE tag and we append it. Wrapped so any failure is a silent no-op.
_BOARD_TAG_RE = re.compile(r"\[\[\s*(balance|machine|graph|card|write|solve|clear)\b", re.I)
_MATH_HINT_RE = re.compile(
    r"[0-9]\s*[-+=]|[0-9]\s*x\b|\bx\s*[-+=]|"
    r"\b(equals?|equation|plus|minus|times|divide[sd]?|dividing|subtract|multipl|"
    r"solve|solving|squared?|slope|intercept|graph|function|variable|f of)\b", re.I)

BOARD_TAG_SYSTEM = """\
You turn a math tutor's spoken message into ONE hidden whiteboard control tag that shows
ONLY the math that has ALREADY been established in the conversation -- never math the
student has not reached yet. The tutor speaks in words (e.g. "two x plus one equals
eleven"); you output SYMBOLIC math inside a tag. Use lowercase x and y for variables.

⛔ THE ONE RULE THAT MATTERS MOST -- NEVER RUN AHEAD OF THE STUDENT.
The board must never reveal a step the tutor is currently ASKING the student to find. Read
the tutor's message: if it hands the next step to the student -- a question or a "your turn"
like "what should we do first?", "what's the next step?", "your turn -- try it", "what do
we get?", "can you solve for x?" -- then you must NOT compute or show that step. Show only
the equation AS IT STANDS right now (the starting equation, or the steps already worked out
together), and stop there. Do the SAME arithmetic the tutor has actually spoken -- never
solve further than the conversation has gone. When in doubt, show LESS, not more.

Pick exactly ONE tag:
- SOLVING an equation -- show ONLY the steps already completed together (starting equation
  on top, then each FINISHED step as "operation : resulting equation"):
    [[solve start="2x + 1 = 11" steps="subtract 1 from both sides : 2x = 10" caption="solve for x"]]
  Include ONLY steps the tutor has already stated as done. If they are still on the starting
  equation -- the tutor just posed it, or is asking what to do first -- use the start with an
  EMPTY steps list (this shows just the one line, spoiling nothing):
    [[solve start="2x + 1 = 11" steps="" caption="solve for x"]]
- A single equation / expression / function definition (not a solve in progress):
    [[write lines="f(x) = 2x + 1 | 2x + 1 = 15"]]
- Evaluating a function at a value the tutor has already stated:
    [[machine input="4" rule="2x+1" output="9" fname="f"]]
- A straight line or parabola the tutor has already stated:
    [[graph lines="y=2x+1"]]

Output ONLY the tag -- no other words. If there is genuinely NO specific equation, number
sentence, expression, or function that has been stated yet, output exactly: NONE"""


def board_tag_for(tutor_message: str, user_message: str = "", history=None) -> str:
    """Focused second call: return ONE whiteboard tag for the current math, or ""."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return ""
    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)
    ctx = ""
    for m in (history or [])[-4:]:
        who = "Tutor" if m.get("role") == "assistant" else "Student"
        ctx += who + ": " + str(m.get("content", ""))[:300] + "\n"
    user = ("Recent conversation:\n" + ctx +
            "Student just said: " + (user_message or "(nothing)") + "\n"
            "Tutor just said (out loud): " + tutor_message + "\n\n"
            "Output the ONE whiteboard tag for the math being worked right now, or NONE.")
    client = Anthropic(api_key=api_key)
    resp = client.messages.create(model=model, max_tokens=220, system=BOARD_TAG_SYSTEM,
                                  messages=[{"role": "user", "content": user}])
    out = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text").strip()
    if not out or out.upper().startswith("NONE"):
        return ""
    hit = re.search(r"\[\[[\s\S]*\]\]", out)
    return hit.group(0) if hit else ""


def ensure_board(reply: str, user_message: str = "", history=None) -> str:
    """RETIRED (Stage 2, 2026-07-23): now a pass-through -- the tutor drives the board itself.

    Why retired: the whiteboard is now a PERSISTENT worklist that stacks and stays, and the
    student-facing brain is claude-sonnet-5, which reliably emits the [[step]] tags the prompt
    asks for. The old behavior here was a SECOND model call (board_tag_for) that GUESSED a tag
    whenever it thought math went undrawn -- and that guessing was the source of two real bugs:
    it answered the very step the tutor was asking the student to find, and it redrew the whole
    problem on a 'check' turn. With a persistent board, a missed tag just means 'no new line
    this turn' (the earlier lines stay up), so the net is no longer needed and did more harm
    than good. board_tag_for / BOARD_TAG_SYSTEM above are kept but UNUSED, so re-enabling a net
    later is a one-line change if we ever want one back.
    """
    return reply


# -----------------------------------------------------------------------------
# TODAY-BAR SAFETY NET (2026-08-08, build bo, Jim's screenshot: a Pre-Algebra
# session showed the UNIT and COURSE bars but NO TODAY bar for the whole lesson --
# the opener emitted [[goal]] and the goals card but skipped the [[today items]]
# tag the PROGRESS BARS note asks for, so the top bar never rendered).
# Unlike the retired ensure_board net above, this one NEVER GUESSES: it copies the
# goal items the model itself just wrote (the "By the end you'll be able to" card,
# falling back to the [[goal]] banner text) into the [[today]] tag verbatim --
# exactly the tag the prompt told the model to emit. It fires only when this reply
# announces goals, has no [[today]] of its own, AND no [[today]] was ever emitted
# earlier in the session (so it can never reset a live bar mid-lesson).
# Lesson mode only (the today bar exists only on the lesson page).
# -----------------------------------------------------------------------------
_GOALS_CARD_RE = re.compile(r'\[\[\s*card\s+title="By the end[^"]*"\s+items="([^"\]]+)"', re.I)
_GOAL_BANNER_RE = re.compile(r'\[\[\s*goal\s+text="([^"\]]+)"', re.I)


def ensure_today_tag(reply: str, history=None, today_live: bool = False) -> str:
    """`today_live` (2026-08-09, build cg) = the SERVER already has today's goal bar
    stored for this student and course, so the page can render it without help.

    That flag replaced a bad assumption. The history guard below reads "a [[today]] was
    emitted earlier, so a bar is already up -- do not reset it." True inside one sitting;
    FALSE across a page load, which is exactly where Jim kept losing the bar: history
    still held yesterday's tag, the net stood down, and the reloaded page had no bar at
    all. Now history only silences the net when the bar genuinely still exists."""
    if re.search(r"\[\[\s*today\b", reply, re.I):
        return reply                                   # model did its job
    if today_live:
        for msg in (history or []):
            if msg.get("role") == "assistant" and "[[today" in str(msg.get("content", "")):
                return reply                           # bar is really up -- never reset it
    m = _GOALS_CARD_RE.search(reply)
    items = m.group(1).strip() if m else ""
    if not items:
        g = _GOAL_BANNER_RE.search(reply)
        items = g.group(1).strip() if g else ""
    if not items:
        return reply                                   # no goals announced this turn -- nothing to mirror
    return reply.rstrip() + ' [[today items="' + items + '"]]'


# =============================================================================
# THE MATH VERIFIER HOOK (2026-08-03) -- shared by lesson, practice, and topic.
# -----------------------------------------------------------------------------
# mathcheck.py is the referee (SymPy actually re-does the math in the tutor's
# hidden [[verify]] tags -- see GRAPH_TOOL_NOTE rules 10-12). This helper is the
# loop around the model call:
#   generate -> verify -> (if a claim is provably wrong) tell the model exactly
#   what SymPy computed and SILENTLY regenerate -> strip the tags -> return.
# The student only ever sees the final, verified text. Fail-open on anything
# undecidable: an imperfect checker must never stall a child's lesson.
# Cost note: a retry is one extra model call and happens only when a real error
# was caught -- rare by design, and exactly the turn worth paying twice for.
# =============================================================================
# =============================================================================
# THE PROSE REFEREE (2026-08-09, build bu -- proactive audit #24)
# -----------------------------------------------------------------------------
# mathcheck.py re-computes the math inside the tutor's TAGS. It is deaf to PROSE --
# which is exactly how this shipped bug reached a live student (2026-08-08):
#     board:  [[step eq="dimes: 7 + 8 + 1 = 16"]]      (correct, and verified)
#     spoken: "Fifteen dimes -- so we write the five and carry a dollar."
# The student's wrong answer was adopted in words while the board said otherwise, and
# nothing could see it. Rule 18(b) tells the model not to do this; THIS is the net.
#
# It is deliberately NARROW, because a false positive silently throws away a good reply.
# It flags one unambiguous shape only -- the reply CONTRADICTS ITSELF about a labeled
# quantity, and its words never once say the number its own board concluded:
#   1. a board line in this reply reads "<label>: ... = R"   (R a plain number)
#   2. the spoken text says "<P> <label>"                    (P a numeral or number-word)
#   3. P != R
#   4. R appears NOWHERE in the spoken text (numeral or word)   <-- the discriminator
#   5. P is not an operand of that same board line
# Condition 4 is what makes this safe: a legitimate mention of an intermediate value
# lands on the right answer in the same breath ("fifteen dimes plus the carried one
# makes SIXTEEN") and is never flagged; an adopted wrong answer never says the correct
# number at all. Everything is wrapped so any surprise fails OPEN -- an imperfect
# referee must never stall a child's lesson.
# =============================================================================
_PR_ONES = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
            "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
            "eighteen": 18, "nineteen": 19}
_PR_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
            "seventy": 70, "eighty": 80, "ninety": 90}


def _pr_word_value(phrase: str):
    """'fifteen' -> 15, 'twenty-one' -> 21, 'one hundred eighty' -> 180. None if not a number."""
    words = re.split(r"[\s-]+", str(phrase).strip().lower())
    words = [w for w in words if w and w != "and"]
    if not words:
        return None
    total, current, seen = 0, 0, False
    for w in words:
        if w in _PR_ONES:
            current += _PR_ONES[w]; seen = True
        elif w in _PR_TENS:
            current += _PR_TENS[w]; seen = True
        elif w == "hundred" and seen:
            current *= 100
        else:
            return None
    return total + current if seen else None


_PR_NUMWORD = "(?:" + "|".join(sorted(list(_PR_ONES) + list(_PR_TENS), key=len, reverse=True)) + \
              r")(?:[\s-](?:hundred|" + "|".join(sorted(list(_PR_ONES) + list(_PR_TENS), key=len, reverse=True)) + r"))*"
# "<label>: <anything> = <number>"  -- the shape our own board rules ask for.
_PR_BOARD_LINE = re.compile(r"([A-Za-z][A-Za-z' ]{0,24}?)\s*:\s*([^=]{0,80}?)=\s*(-?\d+(?:\.\d+)?)\s*$")


def _pr_numbers_in(text: str) -> set:
    """Every number stated in `text`, numerals AND number-words, as floats."""
    out = set()
    for m in re.findall(r"-?\d+(?:\.\d+)?", text or ""):
        try:
            out.add(float(m))
        except ValueError:
            pass
    for m in re.findall(_PR_NUMWORD, (text or "").lower()):
        v = _pr_word_value(m)
        if v is not None:
            out.add(float(v))
    return out


# =============================================================================
# THE VISUAL-REFERENCE CHECK (2026-08-09, build ce) -- half of the prose referee.
# -----------------------------------------------------------------------------
# Jim, on the demo: "the lesson referred to a diagram that didn't show up on the
# board... We got one shot to do it right, and it failed."
#
# Rule 7 has forbidden this in WORDS since build ao. Nothing has ever CHECKED it.
# mathcheck reads tags. prose_board_conflict (below) compares spoken NUMBERS with
# written numbers. A reply that says "here's a number line" and emits no
# [[numberline]] passes every referee we own, and the student sits in front of a
# blank board listening to a description of nothing.
#
# The check is deliberately narrow, because a false positive costs a real model
# call: it fires only when a sentence BOTH names something the board can draw AND
# claims, in the present tense, that it is appearing right now. "A number line has
# zero in the middle" is fine. "Here's a number line" with nothing drawn is not.
# Anything it is unsure about, it lets through -- like every referee here, it fails
# open, because a checker must never brick a lesson.
# =============================================================================

# Tags that put a PICTURE on the board. Kept as a constant (tutor.py must not read
# static files at request time); ruletests.py PART 3c asserts this list still matches
# session.html's handleTags(), so it cannot silently drift out of date.
FIGURE_TAGS = (
    "graph", "numberline", "bars", "histogram", "dotplot", "boxplot", "scatter",
    "normal", "twoway", "tree", "pie", "unitcircle", "righttriangle", "conic",
    "areamodel", "vector", "triangle", "angle", "circle", "objects", "machine",
    "balance",
)
# Every tag that puts ANYTHING on the board, picture or writing.
_BOARD_TAGS = FIGURE_TAGS + ("write", "step", "solve", "column", "card", "check",
                             "quiz", "goal", "today", "unitplan", "finalexam",
                             "choices", "highlight")

# Nouns the board can DRAW. Bare "triangle"/"circle" are deliberately absent: they
# appear in ordinary mathematical prose far too often to judge from one sentence.
_VIS_NOUN = (r"(?:number ?line|graph|diagram|picture|drawing|sketch|figure|chart|plot|"
             r"histogram|scatter ?plot|box ?plot|dot ?plot|bar chart|bar graph|pie chart|"
             r"unit circle|area model|tape diagram|tree diagram|balance scale|"
             r"function machine|right triangle)")
# Phrases that claim it is appearing NOW (not "we could draw one", not "last time").
_VIS_CUE = (r"(?:here'?s|here is|here are|i'?ve drawn|i have drawn|i drew|i just drew|"
            r"i'?m drawing|i am drawing|i'?m putting|i am putting|let me draw|let me sketch|"
            r"let me graph|let me plot|let me put|i'?ll draw|i will draw|i'?ll sketch|"
            r"i'?ll graph|i'?ll plot|look at (?:the|this)|take a look at|notice (?:the|this)|"
            r"see (?:the|this)|watch (?:me|as i)|on the board|on screen|below|above|"
            r"this shows|these show)")
_VIS_SENT = re.compile(_VIS_CUE + r"[^.!?]{0,60}?" + _VIS_NOUN, re.I)
_VIS_SENT_REV = re.compile(_VIS_NOUN + r"[^.!?]{0,40}?" + r"(?:below|above|on the board|on screen)", re.I)
# "look at the board" / "up on the screen" -- needs SOMETHING written, not a picture.
_VIS_BOARD_ONLY = re.compile(r"(?:look at|take a look at|see|check|glance at)\s+"
                             r"(?:the|your|our)\s+(?:board|screen|whiteboard)", re.I)
# A sentence that DEFERS the drawing, or asks whether to draw, or points BACK at an
# earlier one, is not a claim that a picture is on the board right now. Without this
# guard the referee re-rolls perfectly good replies -- and every re-roll is a real
# model call, so a false positive is not free.
_VIS_DEFER = re.compile(
    r"\b(?:next time|later|tomorrow|next session|another day|in a (?:minute|second|moment|bit)|"
    r"want me to|would you like|should i|shall i|do you want|if you(?:'d| would) like|"
    r"we could|we can|i could|remember|last time|yesterday|earlier|before|"
    r"we (?:used|drew|made|had)|you (?:drew|made)|back when)\b", re.I)


def _vis_sentences(prose: str):
    """The spoken text as sentences, so a claim is judged in its own context."""
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", str(prose or "")) if s.strip()]


def _spoken_only(text: str) -> str:
    """The words the student actually HEARS: control tags removed, including a
    dangling one from a reply that was cut off mid-tag."""
    prose = re.sub(r"\[\[[^\]]*\]\]", " ", str(text or ""))
    return re.sub(r"\[\[[\s\S]*$", " ", prose)


def _tags_present(text: str, names) -> bool:
    """True if the reply emits at least one tag from `names`."""
    found = {m.lower() for m in re.findall(r"\[\[\s*([\w-]+)", str(text or ""))}
    return bool(found & set(names))


# Rules 2 and 8 are the same shape as rule 7 from the other side: the student ASKED to
# see something ("show me", "can I see a picture", "draw it"), or the tutor is narrating
# a CHANGE that ought to be shown happening. Both end with a student looking at a board
# that has nothing new on it. Added build co, when the rule index made it plain these
# were the only two rules in the whole prompt that nothing checked at all.
_VIS_ASKED = re.compile(
    r"\b(?:show me|can i see|could i see|let me see|draw (?:it|one|that|me)|"
    r"can you draw|would you draw|picture of (?:it|that))\b", re.I)
_VIS_PROMISE = re.compile(
    r"\b(?:here'?s|here is|let me|i'?ll|i will|watch)\b[^.!?]{0,40}"
    r"\b(?:show|draw|sketch|graph|plot)\b", re.I)


def prose_asked_to_see(student_message: str) -> bool:
    """Did the student just ask to be SHOWN something? (rules 2 and 8)"""
    try:
        return bool(_VIS_ASKED.search(str(student_message or "")))
    except Exception:  # noqa: BLE001
        return False


def prose_visual_conflict(reply: str, student_message: str = ""):
    """Return a description of a picture that was promised and never drawn, or "".

    `student_message` (build co) lets this also enforce rules 2 and 8: if the student
    ASKED to see something, this reply must draw something, full stop -- re-drawing is
    free and always right, so there is no legitimate reason to answer "show me" with a
    board that gains nothing.
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        if prose_asked_to_see(student_message) and not _tags_present(text, _BOARD_TAGS):
            return ('the student just asked to SEE something and this reply puts nothing '
                    'on the board at all. Rule 2: "show me" / "can I see" / "draw it" '
                    'means your reply MUST include the figure or board tag, even if '
                    'something similar is already up -- re-drawing is free and always '
                    'right.')
        if not _tags_present(text, _BOARD_TAGS):
            # Same guard as the rest of this referee: "next time I'll draw you one" is a
            # promise about later, not a claim about now. (Caught by the battery the
            # moment rule 8 was added -- the deferral case was already a fixture.)
            for sent in _vis_sentences(prose):
                if _VIS_DEFER.search(sent):
                    continue
                if _VIS_PROMISE.search(sent):
                    return ('you say you are going to show or draw something and then '
                            'draw nothing. Rule 8: show the change, do not describe it.')
        sentences = _vis_sentences(prose)
        if not _tags_present(text, FIGURE_TAGS):
            for sent in sentences:
                if _VIS_DEFER.search(sent):
                    continue                      # "next time I'll draw one" is not a claim
                for rx in (_VIS_SENT, _VIS_SENT_REV):
                    m = rx.search(sent)
                    if m:
                        said = " ".join(m.group(0).split())[:70]
                        return ('you say "{s}" but this reply draws NO figure at all -- the '
                                'student is looking at a board with no picture on it while '
                                'you talk about one. Rule 7: never describe a picture you '
                                'did not draw.').format(s=said)
        if not _tags_present(text, _BOARD_TAGS):
            for sent in sentences:
                if _VIS_DEFER.search(sent):
                    continue
                m = _VIS_BOARD_ONLY.search(sent)
                if m:
                    said = " ".join(m.group(0).split())[:70]
                    return ('you say "{s}" but this reply puts NOTHING on the board -- no '
                            'figure, no written line. Rule 7: never point at a board you '
                            'did not write on.').format(s=said)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[viscHeck] crashed (fail open): {exc}")
        return ""


# =============================================================================
# THE PENDING-QUESTION CHECK (2026-08-09, build cg) -- third part of the referee.
# -----------------------------------------------------------------------------
# Jim, on a live Pre-Algebra resume: "it gave me a problem without putting it on the
# board, and this is the exact example that we've already used once before that was
# supposedly fixed. And I don't understand why it's not fixed."
#
# He is right, and the reason is worth writing down. Rule 15 does not just forbid this
# in general -- it names THIS EXACT SCENARIO, quotes the column-addition lesson, and
# prints the fix ([[step eq="dollars: 2 + 1 + 1 = ?"]]). It has said so since build bm.
# The reply still went out with "what's two plus one plus one?" spoken and no board
# line, because a rule in a prompt is guidance, not a guarantee. So this stops being a
# rule and becomes a referee: ask the student to compute something, and if the board
# shows no pending line in that same reply, the draft is thrown away and rewritten.
#
# Narrow on purpose (a false positive costs a real model call): it fires only on a
# question that asks for a COMPUTATION -- two or more numbers, or an operator word and
# a number -- so "ready to try one?", "does that click, or should I show it another
# way?" (rule 39d) and "how are you doing today?" are all untouched. Number WORDS count,
# because the tutor speaks in words ("what's two plus one plus one?").
# =============================================================================
# Operator WORDS only. A bare "-" or "/" must never count: "three-fourths" and "1/2" are
# single values, and treating their punctuation as an operator made the very first test
# run flag "which number is the denominator in three-fourths?" as a computation.
_PQ_OPERATOR = (r"\b(?:plus|minus|times|multiplied by|divided by|add|adds|added|subtract|"
                r"subtracted|multiply|multiplied|divide|divided|sum of|product of|"
                r"difference between|square root of|percent of)\b")
# A written arithmetic expression counts on its own: digit, operator, digit. The
# unambiguous operators (+ × ÷) count tight or spaced; "-", "*" and "/" only count when
# they are SPACED, because "1/2" and "3-4" are single values, not operations. (Caught on
# the second test run: "is 1/2 bigger than the piece we shaded?" was being read as
# arithmetic.)
_PQ_SYMBOL_EXPR = re.compile(r"\d\s*[+×÷]\s*\d|\d\s+[\-*/]\s+\d")
# tags whose text can carry the pending "?" line rule 15 asks for
_PQ_BOARD_TAGS = ("step", "write", "solve", "column", "card", "graph", "numberline",
                  "objects", "balance", "machine", "areamodel", "choices")

# BUILD dg (2026-08-11): TWO FALSE-POSITIVE CLASSES, FOUND IN THE FIRST FULL AUDIT'S
# RENDER LOGS. This referee killed good drafts a dozen times in forty minutes, and one
# geometry lesson shipped WITHOUT its worked example because the drafts that contained
# it kept being discarded (Audit_Findings_2026-08-11.md, S-1 and L-3). The exact quoted
# misfires are permanent cases in ruletests.py. The two classes:
#   (a) OFFERS. "Want to try one yourself now, or see one more worked example first?"
#       asks the student's PREFERENCE, not for a computed answer. If they accept, the
#       problem goes up NEXT turn, where rule 15 applies in full force. Look-questions
#       ("See how the five sits under the four?") direct the eyes at a board that is
#       already drawn -- there is nothing pending to compute. ("See how MANY..." still
#       counts: that asks for a count, which is a computation.)
#   (b) THE PRONOUN "one". "try ONE more", "see ONE yourself" made offers read as
#       two-number arithmetic. "one" now counts as a number only in arithmetic company:
#       beside an operator word, a fraction word, or "more/less than".
_PQ_OFFER = re.compile(
    r"^(?:(?:and|so|now|or|okay|ok|alright|great|nice|perfect)[,\s]+)*"
    r"(?:do you want|want to|want me to|want another|want more|wanna|"
    r"would you (?:like|rather|prefer)|are you ready|ready to|ready for|"
    r"shall we|should we|how about|care to|up for|feel like|what do you say|"
    r"(?:do you|can you)?\s*see (?:how|that|why|where|it)(?!\s+(?:many|much|few|long))|"
    r"notice (?:how|that|the)(?!\s+(?:many|much))|look at)\b", re.I)


def _pq_is_offer(sentence: str) -> bool:
    """True when a question asks the student's PREFERENCE or directs their eyes --
    an invitation or a look-question, never a computation handed to them. Offers need
    no pending board line: the problem itself arrives on the turn the student accepts."""
    return bool(_PQ_OFFER.match(str(sentence or "").strip()))


# "one" in arithmetic company -- the only "one" that counts as a number (build dg).
_PQ_ONE_ARITH = re.compile(
    r"\b(?:plus|minus|times|add|adds|added|subtract|multiplied|divided|of)\s+one\b"
    r"|\bone\s+(?:plus|minus|times|divided|multiplied|more\s+than|less\s+than|"
    r"hundred|thousand|half|halves|third|thirds|fourth|fourths|fifth|fifths|"
    r"sixth|sixths|seventh|sevenths|eighth|eighths|ninth|ninths|tenth|tenths)\b", re.I)

# A sentence-splitter that sees a sentence ending INSIDE a closing quote. The old split
# key ((?<=[.!?])\s+) stopped dead at «...goes in." Want me to...» -- the period hides
# before the quote mark, the two sentences merged, and a statement full of numbers
# inherited the next sentence's "?" (the third false-positive class in the audit logs).
_PQ_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+|(?<=[.!?][\"'”’])\s+|\n+")


def _pq_numeric_tokens(sentence: str) -> int:
    """How many numbers a sentence states, numerals and number-words alike.

    A written fraction ("1/2", "3/4") is ONE number, not two -- counting its halves
    separately made "is 1/2 bigger than the piece we shaded?" look like arithmetic.
    And "one" only counts in arithmetic company (build dg) -- as a bare pronoun
    ("try one more", "see one yourself") it is not a number at all."""
    low = re.sub(r"\d+\s*/\s*\d+", " ½ ", sentence.lower())
    n = len(re.findall(r"\d+(?:\.\d+)?", low)) + low.count("½")
    words = sorted([w for w in list(_PR_ONES) + list(_PR_TENS) if w != "one"],
                   key=len, reverse=True)
    n += len(re.findall(r"\b(?:" + "|".join(words) + r")\b", low))
    n += len(_PQ_ONE_ARITH.findall(low))
    return n


def prose_pending_question_conflict(reply: str):
    """Return a description of a computation asked with nothing on the board, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        asks = []
        for sent in _PQ_SENT_SPLIT.split(prose):
            sent = sent.strip()
            if not sent.endswith("?"):
                continue
            if _pq_is_offer(sent):
                continue          # an invitation, not a computation (build dg)
            nums = _pq_numeric_tokens(sent)
            if (nums >= 2
                    or (nums >= 1 and re.search(_PQ_OPERATOR, sent, re.I))
                    or _PQ_SYMBOL_EXPR.search(sent)):
                asks.append(sent)
        if not asks:
            return ""
        # Does the board carry a PENDING line -- a "?" standing in for the unknown?
        for tag in re.findall(r"\[\[\s*(" + "|".join(_PQ_BOARD_TAGS) + r")\b([^\]]*)\]\]",
                              text, re.I):
            if "?" in tag[1]:
                return ""
        asked = " ".join(asks[-1].split())[:90]
        return ('you ask the student to work out "{q}" but this reply puts no pending line '
                'on the board -- nothing with a "?" in it. Rule 15: the problem you hand '
                'them goes UP, in symbols, in the same reply you ask it, written as a '
                'pending line like [[step eq="dollars: 2 + 1 + 1 = ?"]]. The "?" keeps the '
                'question complete on the board without running ahead of them '
                '(rule 6).').format(q=asked)
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[pendcheck] crashed (fail open): {exc}")
        return ""


# =============================================================================
# THE SELF-ANSWER CHECK (2026-08-10, build cy) -- fifth part of the referee.
# -----------------------------------------------------------------------------
# WAIT TIME, and why this is not a new rule but an old one finally enforced.
#
# From the MAA Instructional Practices Guide (CP.1.2), which Jim put in the tutor folder:
# instructors wait on average LESS THAN 1.5 SECONDS before answering their own question
# or asking another; the research says wait at least SEVEN, and that an average above
# three seconds is the threshold at which the discourse actually changes (Fuller et al.
# 1985; Tobin 1987). The first benefit the guide lists for waiting is "a decrease in the
# number of 'I don't know' responses" -- which is the exact thing Jim keeps meeting.
#
# The guide's vignette is a calculus instructor asking eight questions in a row and
# answering EVERY ONE of them himself a second later. We cannot rush our students -- they
# type or speak whenever they like -- but we can rush OURSELVES, in exactly that way: ask
# a question and then supply the answer in the same reply. The student never gets the
# seven seconds because the answer was already on the screen.
#
# RULE 39(b) ALREADY FORBIDS THIS: one question per turn, and it comes LAST. It has been
# COVERED since build ce -- written into all ten prompts and never checked. Moving a rule
# up a tier is worth more than writing a new one, so this enforces 39(b) rather than
# adding rule 52 (and it costs no prompt budget, which at 134,476 characters matters).
#
# NARROW ON PURPOSE, because every false positive costs a real model call. It fires only
# when BOTH halves are true:
#   1. the reply asks something ANSWERABLE -- the same test rule 15's referee uses, so a
#      rhetorical "so what happens next?" is not a question for these purposes; and
#   2. after that question, the reply keeps talking AND states a NUMBER.
# "What is 7 plus 5? Take your time." is clean -- no number after the question.
# "What is 7 plus 5? It's 12." is not.
# A question that is genuinely last is clean, which is the behaviour we want.
_SA_TRAILING_NUM = re.compile(r"\d")
# A second way in, for questions that carry no numbers of their own ("how much work is
# done on each slice?" -- the guide's own vignette). Widening the QUESTION test would have
# caught our foundation scripts, which are all shaped "What is a numerator? The numerator
# is ..." -- teaching, not self-answering. So the widening goes on the TAIL instead:
# nobody announces a definition with "the answer is". Both halves still required.
_SA_ANSWER_MARKER = re.compile(
    r"\b(?:the answer is|that'?s just|that is just|it'?s just|which is just|"
    r"so the answer|comes out to|works out to|equals)\b", re.I)


def _sa_number_tokens(text: str) -> set:
    """The number tokens a sentence states, numerals and number-words alike, as a SET --
    so the tail can be compared against the question and a restated number recognised as
    a hint rather than an answer."""
    low = str(text or "").lower()
    out = set(re.findall(r"\d+(?:\.\d+)?", low))
    words = sorted(list(_PR_ONES) + list(_PR_TENS), key=len, reverse=True)
    out |= set(re.findall(r"\b(?:" + "|".join(words) + r")\b", low))
    return out


def prose_self_answer_conflict(reply: str):
    """Return a description of the tutor answering its own question, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        sentences = [x.strip() for x in _PQ_SENT_SPLIT.split(prose) if x.strip()]
        last_ask = -1
        asked = ""
        for i, sent in enumerate(sentences):
            if not sent.endswith("?"):
                continue
            if _pq_is_offer(sent):
                continue          # an invitation, not a question he can self-answer (dg)
            nums = _pq_numeric_tokens(sent)
            rest = " ".join(sentences[i + 1:])
            if (nums >= 2
                    or (nums >= 1 and re.search(_PQ_OPERATOR, sent, re.I))
                    or _PQ_SYMBOL_EXPR.search(sent)
                    or _SA_ANSWER_MARKER.search(rest)):
                last_ask, asked = i, sent
        if last_ask < 0:
            return ""
        tail = " ".join(sentences[last_ask + 1:]).strip()
        if not tail:
            return ""                      # the question is last -- exactly right
        # Words of encouragement after a question are fine and often kind. Stating a
        # number gives the answer away -- but ONLY a number the question did not already
        # contain. Caught on the sweep of our own 227 demo lines: "two to WHAT power makes
        # thirty-two? Start at two and count how many times you double" restates "two"
        # from the question as a HINT and never says five. A hint is not an answer, and a
        # referee that cannot tell them apart would punish good teaching.
        asked_nums = _sa_number_tokens(asked)
        novel = [t for t in _sa_number_tokens(tail) if t not in asked_nums]
        if not novel:
            return ""
        return ('you ask "{q}" and then keep talking, and what follows states a number -- '
                '"{t}". Rule 39(b): ONE question per turn and it comes LAST. The research '
                'behind it is blunt: teachers wait about a second and a half before '
                'answering their own question, the evidence says wait seven, and the first '
                'thing that improves when you wait is how often a student says "I don\'t '
                'know". Ask, then stop. Their answer is the next turn\'s job, and if they '
                'are stuck, rule 24 gives you the whole ladder -- on the NEXT turn.'
                ).format(q=" ".join(asked.split())[:70], t=" ".join(tail.split())[:60])
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[selfanswer] crashed (fail open): {exc}")
        return ""


# =============================================================================
# THE BOARD-NOTATION CHECK (2026-08-11, build dk) -- deterministic, no model call.
# -----------------------------------------------------------------------------
# Two abuses of notation the audit RE-RUN shipped to real boards, each teaching a
# broken rule in writing, and neither visible to mathcheck ($ and % are not sympy):
#   1. "$50 + 10% = $55" -- a bare percent ADDED to a plain quantity, COMPLETED. The
#      missing idea is "10% OF $50" (rules 13/27). Percent-with-percent arithmetic
#      ("100% - 40% = 60%") stays legal: the pattern requires a plain first operand.
#   2. "a^2 + 64 = 100 = ?" -- a chain of equals signs ending in "= ?" straight after
#      a bare number: "100 = ?" asks what one hundred equals (rule 15's "?" is a value
#      to compute, never a dangling continuation).
# Deterministic and NARROW: a legitimate pending line ("50 - 25% = ?"), a percent
# conversion ("3/4 = 75%"), and the "of" form all pass untouched. Swept against every
# canonical script before ship, like every referee since cy.
_BN_PCT = re.compile(
    r"(?:\$\s*)?\d+(?:\.\d+)?\s*[+\-−]\s*\d+(?:\.\d+)?\s*%\s*=\s*\$?\s*\d")
_BN_CHAIN = re.compile(r"=\s*-?\d+(?:\.\d+)?\s*=\s*\?")
# BUILD dl -- rule 54(b)'s referee: the tutor TEACHING a key-word-to-operation rule.
# The WWC guide names this as a habit tutors install by accident, and it is exactly
# the kind of confident, friendly sentence a model produces ("remember: 'altogether'
# always means add!"). Narrow: it requires the quoted-word/means/operation SHAPE, so
# talking ABOUT a key word ("the word 'altogether' tells us the story combines
# things") stays legal, and so does honest notation reading ("the fraction bar means
# divide"). Fails open like every referee.
# The banned list is STORY-CUE words only. "Sum means add" and "difference means
# subtract" are VOCABULARY -- those words are the operations' names, and rule 37
# requires teaching them. The trap the guide warns about is narrative cue words that
# merely CORRELATE with an operation ("altogether", "left", "more") being taught as if
# they decided it.
_KW_SHORTCUT = re.compile(
    r"\b(?:altogether|all together|in all|in total|left(?:\s+over)?|remain(?:s|ing)?|"
    r"fewer|more)\b[\"'”’)]?\s*"
    r"(?:always\s+|usually\s+|just\s+)?means?\s+(?:you\s+|to\s+|we\s+)?"
    r"(?:add(?:ing|ition)?|plus|subtract(?:ing|ion)?|minus|take\s+away|"
    r"multipl(?:y|ying|ication)|times|divid(?:e|ing)|division)\b", re.I)


def board_notation_conflict(reply: str):
    """Return a description of a malformed board line, or "". Never raises: any
    unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        for tag in re.findall(r"\[\[[^\]]*\]\]", text):
            for val in re.findall(r'"([^"]*)"', tag):
                if _BN_PCT.search(val):
                    v = " ".join(val.split())[:60]
                    return ('the board completes "{v}" -- a bare percent ADDED to a '
                            "plain quantity. Rule 27: a percent is not an amount; the "
                            'missing idea is "of". Write "$50 + 10% of $50 = $55", or '
                            'convert first ("10% of $50 = $5" then "$50 + $5 = $55") -- '
                            "never complete the malformed form.").format(v=v)
                if _BN_CHAIN.search(val):
                    v = " ".join(val.split())[:60]
                    return ('the board writes "{v}" -- a chain of equals signs ending '
                            'in "= ?" right after a bare number, which asks what that '
                            'number equals. Rule 15: the "?" marks a value to COMPUTE. '
                            'Write the true equation alone ("a^2 + 64 = 100"), then the '
                            'pending step as its own line ("a^2 = ?").').format(v=v)
        # rule 54(b), build dl: teaching a key-word-to-operation shortcut, in prose or
        # on the board. The words that get banned are story CUES only (see above).
        m = _KW_SHORTCUT.search(_spoken_only(text))
        if not m:
            for tag in re.findall(r"\[\[[^\]]*\]\]", text):
                for val in re.findall(r'"([^"]*)"', tag):
                    m = _KW_SHORTCUT.search(val)
                    if m:
                        break
                if m:
                    break
        if m:
            return ('you teach "{q}" -- a key-word rule. Rule 54(b): key words do NOT '
                    "reliably signal operations, and a key-word rule installs a "
                    "misconception with your authority behind it. Name the problem's "
                    "TYPE instead (Change, Equal Groups, Compare) and let the type "
                    "choose the operation. Words describe the story; the schema decides "
                    "the arithmetic.").format(q=" ".join(m.group(0).split())[:60])
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[boardnote] crashed (fail open): {exc}")
        return ""


# =============================================================================
# THE TRIANGLE-SLOT CHECK (2026-08-13, build fe) -- rule 63(c) is born ENFORCED.
# -----------------------------------------------------------------------------
# The 2026-08-13 lesson audit (geometry-picture, HIGH): a lesson said "one leg is 6,
# the hypotenuse is 10" while its tag read sides="6,?,10" right="C" -- and sides= is
# AB, BC, CA by contract (geo-figures.js draws it exactly so), so with the right angle
# at C the FIRST slot is the hypotenuse. The drawn hypotenuse said 6; every spoken
# sentence said 10. Three of that lesson's four triangles were mis-slotted, which is
# the worst kind of board bug: the words and the picture each perfectly plausible,
# and a student who believes both learns that labels are decoration.
# NARROW, like every referee: it fires ONLY when a [[triangle]] tag carries BOTH
# right= (naming one of its vertices) and sides=, the hypotenuse slot holds a NUMBER,
# and some other slot holds a number >= it -- a geometric impossibility, never a
# style call. A pending "?" hypotenuse is always clean; algebraic side lengths are
# never judged; a right= that names no vertex is not ours to guess about.
_TRI_TAG = re.compile(r"\[\[\s*triangle\b([^\]]*)\]\]", re.I)
_TRI_ATTR = re.compile(r'([A-Za-z_]\w*)\s*=\s*"([^"]*)"')


def triangle_side_conflict(reply: str):
    """Return a description of a right-triangle tag whose hypotenuse slot holds a
    side that cannot be the hypotenuse, or "". Never raises: any unexpected input
    yields "" (fail open)."""
    try:
        text = str(reply or "")
        for m in _TRI_TAG.finditer(text):
            attrs = {k.lower(): v for k, v in _TRI_ATTR.findall(m.group(1))}
            right = (attrs.get("right") or "").strip()
            sides_raw = (attrs.get("sides") or "").strip()
            if not right or not sides_raw:
                continue
            v = [s.strip() for s in (attrs.get("v") or "A,B,C").split(",")]
            sides = [s.strip() for s in sides_raw.split(",")]
            if len(v) != 3 or len(sides) != 3:
                continue
            try:
                ridx = [x.upper() for x in v].index(right.upper())
            except ValueError:
                continue          # right= names no vertex of this triangle: not ours
            # slots are AB, BC, CA; the hypotenuse is the side that SKIPS the right-
            # angle vertex: right at A -> BC (slot 1), at B -> CA (2), at C -> AB (0).
            hyp = {0: 1, 1: 2, 2: 0}[ridx]

            def _num(s):
                try:
                    return float(s)
                except ValueError:
                    return None

            hv = _num(sides[hyp])
            if hv is None:
                continue          # a pending "?" (or algebraic) hypotenuse is fine
            offenders = [sides[i] for i in range(3) if i != hyp
                         and _num(sides[i]) is not None and _num(sides[i]) >= hv]
            if offenders:
                pair = v[hyp].upper() + v[(hyp + 1) % 3].upper()
                return ("your [[triangle]] tag has the right angle at {r}, which makes "
                        "{p} the hypotenuse -- the sides list is AB, BC, CA in that "
                        "order -- but the {p} slot holds {h}, while another side is "
                        "{o}. The hypotenuse is always the strictly longest side, so "
                        "this drawing contradicts itself. Rule 63(c): put the "
                        "hypotenuse's length (or its pending \"?\") in the {p} slot "
                        "and the legs in theirs.").format(
                            r=right.upper(), p=pair,
                            h=sides[hyp], o=offenders[0])
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[triangleslot] crashed (fail open): {exc}")
        return ""


# =============================================================================
# THE ANSWERED-QUESTION CHECK (2026-08-11, build dh) -- rule 17 moves COVERED -> ENFORCED.
# -----------------------------------------------------------------------------
# First full audit, twice in one run, two courses apart: a worked card said
# "tickets cost: 3 × 2 = 6 dollars" while the prose asked "so what's 3 times 2?", and
# "f(a) = 2a + 1 = ?" stood on the board while the prose asked what 2(a)+1 looks like
# "written cleaner". A question the board has already answered CANNOT fail, and the
# student's "success" is then treated as evidence of understanding.
# NARROW, like every referee -- a false positive costs a real model call and (proven in
# build dg) can cost the student the good draft: it fires ONLY when the prose asks a
# lead-in question ("what's", "what do you get", "how much is") for A op B with explicit
# numbers, AND a board tag in the SAME reply states that exact A op B = C with a NUMERIC
# C. A pending "= ?" line never trips it -- that is rule 15 done right. Commutativity is
# honoured for + and ×. Offers are excluded the build-dg way.
_AQ_OPS = {"plus": "+", "add": "+", "added to": "+", "+": "+",
           "minus": "-", "take away": "-", "less": "-", "-": "-", "−": "-",
           "times": "*", "multiplied by": "*", "x": "*", "×": "*", "*": "*",
           "divided by": "/", "over": "/", "÷": "/", "/": "/"}
_AQ_Q = re.compile(
    r"\b(?:what'?s|what is|what do you get|what does that (?:come|work) (?:to|out to)|"
    r"how much is|so what'?s)\b[^.?!]*?"
    r"(\d+(?:\.\d+)?|" + _PR_NUMWORD + r")\s*"
    r"(plus|minus|times|multiplied by|divided by|added to|take away|[+\-−×x*/÷])\s*"
    r"(\d+(?:\.\d+)?|" + _PR_NUMWORD + r")", re.I)
_AQ_BOARD = re.compile(
    r"(\d+(?:\.\d+)?)\s*([+\-−×x*/÷])\s*(\d+(?:\.\d+)?)\s*=\s*(-?\d+(?:\.\d+)?)")


def prose_answered_question_conflict(reply: str):
    """Return a description of a question whose answer this reply's own board already
    states, or "". Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        asked = []
        for sent in _PQ_SENT_SPLIT.split(prose):
            sent = sent.strip()
            if not sent.endswith("?") or _pq_is_offer(sent):
                continue
            m = _AQ_Q.search(sent)
            if not m:
                continue
            a = _sc_val(m.group(1))
            op = _AQ_OPS.get(m.group(2).strip().lower())
            b = _sc_val(m.group(3))
            if a is None or op is None or b is None:
                continue
            asked.append((a, op, b, sent))
        if not asked:
            return ""
        stated = set()
        for tag in re.findall(r"\[\[[^\]]*\]\]", text):
            for m in _AQ_BOARD.finditer(tag):
                try:
                    a, b = float(m.group(1)), float(m.group(3))
                    float(m.group(4))          # the RHS must be numeric ("?" never is)
                except ValueError:
                    continue
                op = _AQ_OPS.get(m.group(2).strip().lower())
                if op is None:
                    continue
                stated.add((a, op, b))
                if op in ("+", "*"):
                    stated.add((b, op, a))
        for a, op, b, sent in asked:
            if (a, op, b) in stated:
                q = " ".join(sent.split())[:80]
                return ('you ask the student "{q}" while a board line in this same reply '
                        "already states that computation WITH its answer. Rule 17: a "
                        "question the board has answered cannot fail, and the success "
                        "that follows is not evidence. If you want the student to do the "
                        'step, write it PENDING -- like [[step eq="3 × 2 = ?"]] -- and '
                        "complete it only after they answer.").format(q=q)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[answeredq] crashed (fail open): {exc}")
        return ""


# =============================================================================
# THE UNSPOKEN-PROBLEM CHECK (2026-08-11, build dh) -- rule 44 moves COVERED -> ENFORCED.
# -----------------------------------------------------------------------------
# First full audit, a prealgebra quiz turn: 'First question:
# [[step eq="Q1: Evaluate 5x - 2 when x = 4"]] What's the answer?' -- the problem
# existed only as text on the board. This is a VOICE classroom: some students are
# seven, some are dyslexic, some listen with the screen off to one side. A problem
# that was never spoken is a problem they cannot attempt, and their silence will read
# as a math failure in every number we report about them (rule 44's own words).
# NARROW: fires only when a pending "?"-line or a Q-numbered quiz line carries TWO or
# more numbers while the ENTIRE spoken prose asks a question yet contains NO number at
# all, in any spelling. If the tutor spoke even one number, we stay silent.
# BUILD eq (2026-08-12). The rule-44 referee used to give up the moment the SPOKEN text
# contained any number at all -- so "two numbers that multiply to 10 and add to 7" was
# enough to excuse never reading "x squared plus seven x plus ten equals zero" out loud.
# The honest question is not "does the prose contain a number" but "does the prose carry
# THIS problem's numbers". Every quantity the board line states has to appear in the
# words, as a numeral or as the word a person would say. Fractions are checked as a pair
# ("8/12" needs eight AND twelve, or the spoken "eight twelfths"), because that is the
# exact case the audits caught twice in one quiz.
_EQ_NUMWORD = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
               7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
               13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
               17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
               30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
               80: "eighty", 90: "ninety", 100: "hundred"}
# the spoken names of a fraction's bottom number ("8/12" -> "twelfths")
_EQ_DENOM_WORD = {2: "half|halves", 3: "third", 4: "fourth|quarter", 5: "fifth",
                  6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth",
                  12: "twelfth", 16: "sixteenth", 100: "hundredth"}


def _pq_spoken_covers(prose: str, board_value: str) -> bool:
    """True if the SPOKEN words carry the numbers this board line states.

    Deliberately generous -- this decides whether to REGENERATE a reply, so it errs
    toward 'the tutor said it'. A single missing quantity is not enough; the words have
    to miss EVERY number the problem states before we call it unspoken."""
    try:
        low = " " + re.sub(r"[^a-z0-9/\.\s-]", " ", str(prose or "").lower()) + " "
        # a spoken fraction ("eight twelfths", "three fourths") counts for both halves
        frac = re.search(r"(\d+)\s*/\s*(\d+)", board_value or "")
        if frac:
            top, bot = int(frac.group(1)), int(frac.group(2))
            # BUILD gk (2026-08-16) -- THE HALVES MUST BE SPOKEN TOGETHER.
            # This used to look for the numerator ANYWHERE and the denominator ANYWHERE,
            # independently. The 2026-08-16 fractions audit walked straight through it:
            # the board said 3/4 + 1/4 = ? and the words said "three plus one really is
            # four" -- which is about the NUMERATORS, and never reads the problem at all --
            # yet "three" and "four" were both present, so the referee called it spoken and
            # the child was asked a question they had only ever seen written down. That is
            # precisely the failure rule 44 exists to stop, in the course whose students can
            # least afford it. A fraction now only counts as read when its two halves are
            # said TOGETHER -- "three fourths", "three over four", or the literal 3/4 --
            # which is the only way a listening student actually hears the quantity.
            if re.search(r"\b%d\s*/\s*%d\b" % (top, bot), low):
                return True
            tops = [re.escape(str(top))]
            if top in _EQ_NUMWORD:
                tops.append(re.escape(_EQ_NUMWORD[top]))
            # NOTE: _EQ_DENOM_WORD values are already alternations ("half|halves",
            # "fourth|quarter") -- group them, never escape them.
            bots = [re.escape(str(bot))]
            if bot in _EQ_DENOM_WORD:
                bots.append("(?:%s)" % _EQ_DENOM_WORD[bot])
            if bot in _EQ_NUMWORD:
                bots.append(re.escape(_EQ_NUMWORD[bot]))
            together = r"\b(?:%s)\b(?:\s+\w+){0,2}\s+(?:%s)s?\b" % (
                "|".join(tops), "|".join(bots))
            return bool(re.search(together, low))
        nums = [int(n) for n in re.findall(r"\b\d{1,4}\b", board_value or "")]
        if not nums:
            return True                      # nothing numeric to read aloud
        for n in nums:
            if re.search(r"\b%d\b" % n, low):
                return True
            w = _EQ_NUMWORD.get(n)
            if w and re.search(r"\b%s\b" % w, low):
                return True
        return False
    except Exception:                        # noqa: BLE001 -- fail open, always
        return True


def prose_unspoken_problem_conflict(reply: str):
    """Return a description of a board problem the spoken words never read aloud,
    or "". Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        prose = _spoken_only(text)
        low = prose.lower()
        if "?" not in prose and "your turn" not in low:
            return ""
        pend = []
        for tag in re.findall(r"\[\[\s*(?:" + "|".join(_PQ_BOARD_TAGS) + r")\b([^\]]*)\]\]",
                              text, re.I):
            for val in re.findall(r'"([^"]*)"', tag):
                if not ("?" in val or re.match(r"\s*Q\d+\s*:", val)):
                    continue
                # BUILD eq (2026-08-12) -- TWO BLIND SPOTS THE 2026-08-12 AUDITS WALKED
                # STRAIGHT THROUGH, six findings in five lessons.
                # (1) THE BAR WAS TWO NUMBERS. A fraction counts as ONE token by design
                #     (see _pq_numeric_tokens), so a whole quiz of "8/12 = ?" and
                #     "6/9 = ?" could never qualify no matter how silent the prose was --
                #     and "what's this fraction reduced to lowest terms?" is precisely
                #     the sentence a listening student cannot act on. A board problem
                #     needs ONE stated quantity to be worth reading aloud, not two.
                # (2) It must still be a PROBLEM, not a label: "Q1: ..." or a line that
                #     poses something with an operator or a fraction in it. A bare
                #     "denominator = ?" asks about the board, not for arithmetic.
                if _pq_numeric_tokens(val) < 1:
                    continue
                if not (re.match(r"\s*Q\d+\s*:", val)
                        or re.search(r"[+\-−×x*/÷^=]", val)
                        or re.search(r"\d+\s*/\s*\d+", val)):
                    continue
                spoken_here = _pq_spoken_covers(prose, val)
                if not spoken_here:
                    pend.append(" ".join(val.split()))
        if not pend:
            return ""
        return ('the board hands the student a problem -- "{p}" -- but the spoken words '
                "never read it: the prose asks its question without a single number in "
                "it. Rule 44: READ THE PROBLEM ALOUD, IN FULL, EVERY TIME -- this is a "
                "voice classroom, and a problem that exists only as text is a problem "
                "some students cannot attempt. Speak the whole problem the way a person "
                "says it, then ask.").format(p=pend[0][:70])
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[unspoken] crashed (fail open): {exc}")
        return ""


# =============================================================================
# THE SCORE CHECK (2026-08-09, build ch) -- fourth part of the referee.
# -----------------------------------------------------------------------------
# Proactive audit #2 item 9. The server already recomputes every percentage from
# correct/total, so no percentage the model asserts is ever STORED. What nothing
# checked is what the student HEARS. The tally in [[quiz]] / [[check]] / [[finalexam]]
# is honest, and the sentence next to it is free to say "you passed!" to a discouraged
# child who scored 3 of 5. That is the same class of bug as the 2026-08-08 dimes
# contradiction -- the words disagreeing with the tag -- except this one lands on the
# progress bars, which are the product's central promise.
#
# Thresholds live in store.py; they are mirrored here as constants because tutor.py must
# not import the storage layer, and ruletests.py asserts the two never drift apart.
QUIZ_PASS_PCT = 80          # a topic quiz
UNIT_PASS_PCT = 90          # a Unit Quiz / end-of-unit check
FINAL_PASS_PCT = 90         # the Final Exam
_SCORE_TAGS = {"quiz": QUIZ_PASS_PCT, "check": UNIT_PASS_PCT, "finalexam": FINAL_PASS_PCT}
_SC_PASS_CLAIM = re.compile(
    r"\b(?:you(?:'ve| have)?\s+(?:just\s+)?(?:passed|mastered)|that'?s a pass|"
    r"you passed|passed it|unit (?:is )?mastered|you'?re through|that'?s a mastery)\b", re.I)
_SC_FAIL_CLAIM = re.compile(
    r"\b(?:did ?n'?t (?:quite )?pass|not (?:quite )?a pass|didn'?t make it|"
    r"we'?ll (?:try|take) (?:that|it|this) again|short of the bar)\b", re.I)
# NOTE the boundary: "percent" takes a \b, "%" must NOT. A trailing \b after "%" asks for
# a word character next to a non-word character, so "80% — great!" never matched at all and
# the whole percentage check was silently dead. Caught by the test battery on run two.
_SC_PCT = re.compile(r"(\d{1,3})\s*(?:%|percent\b)", re.I)
_SC_RESULT_CONTEXT = re.compile(
    r"\b(?:score[sd]?|you got|you'?ve got|you'?re at|you are at|result|that'?s|that is|"
    r"came out|ended up|you were|final tally|altogether that)\b", re.I)
_SC_BAR_CONTEXT = re.compile(
    r"\b(?:need|needs|needed|to pass|passing|the bar|or better|or higher|required|"
    r"requires|at least|cut ?off|takes|aiming for|target)\b", re.I)
_SC_FRACTION = re.compile(r"\b(\d{1,2}|" + _PR_NUMWORD + r")\s+out of\s+(\d{1,2}|" + _PR_NUMWORD + r")\b", re.I)


def _sc_val(token: str):
    try:
        return float(token) if re.match(r"^\d", token.strip()) else _pr_word_value(token)
    except (TypeError, ValueError):
        return None


# =============================================================================
# BUILD eq (2026-08-12) -- THE MALFORMED-TAG REFEREE
# =============================================================================
# The 2026-08-12 audit caught this on a Basic Math board:
#     [[choices options="yes, let's go! | show me one more]]
# The closing quote is missing. Traced through the page's own parser: the tag IS
# recognised, the attribute regex cannot match an unterminated quoted value, so it falls
# back to the next whitespace-delimited token and the child is shown ONE answer button
# reading   "yes,   -- and the second choice does not exist at all.
#
# EIGHT referees ran on that reply and not one of them looks at whether a tag is even
# well-formed. Every other referee asks whether the tutor said something WRONG; this one
# asks whether what he emitted can be drawn at all. A malformed tag is silent: nothing
# errors, the lesson continues, and only the student sees the broken control.
#
# DELIBERATELY NARROW -- this regenerates a reply, so it only fires on damage it can
# prove: an odd number of quotes inside a tag, an attribute whose value is unterminated,
# or a tag opened and never closed. Prose that merely contains "[[" is not a tag.
_EQ_TAGNAME = re.compile(r"\[\[\s*([\w-]+)")


def malformed_tag_conflict(reply: str):
    """Return a description of a board tag the page cannot parse, or "". Fail open."""
    try:
        text = str(reply or "")
        if "[[" not in text:
            return ""
        # 1. A tag opened and never closed swallows the rest of the reply. Count only
        #    REAL openings -- "[[" followed by a tag name. Prose that merely contains
        #    two brackets ("we write it like this: [[ ...") is not a tag and must not
        #    cost a regeneration.
        opens = len(re.findall(r"\[\[[\w-]+", text))   # "[[step", never "[[ is how a tag"
        closes = text.count("]]")
        if opens > closes:
            frag = text[text.rindex("[["):][:70]
            return ('a board tag is opened and never closed -- "{f}". The page reads to '
                    "the end of the reply looking for ]] and draws nothing, so the "
                    "student loses that control entirely. Close every tag."
                    ).format(f=" ".join(frag.split()))
        # 2. Inside each tag, quotes must pair up and every attr= must be terminated.
        for m in re.finditer(r"\[\[(.*?)\]\]", text, re.S):
            body = m.group(1)
            name_m = _EQ_TAGNAME.match("[[" + body)
            name = name_m.group(1).lower() if name_m else "?"
            if body.count('"') % 2:
                return ('the board tag [[{n} ...]] has an ODD number of quote marks, so '
                        'one of its values is never closed -- "{f}". The page cannot '
                        "parse that attribute: it falls back to the next word, and the "
                        "student sees a broken or missing control instead of what you "
                        "meant. Every attribute is name=\"value\", quotes balanced."
                        ).format(n=name, f=" ".join(("[[" + body + "]]").split())[:80])
            # an attribute that opens a quote with no closing quote before the tag ends
            for am in re.finditer(r'([\w-]+)\s*=\s*"', body):
                rest = body[am.end():]
                if '"' not in rest:
                    return ('the board tag [[{n} ...]] leaves {a}="..." unterminated -- '
                            '"{f}". The student sees a broken control. Close the quote.'
                            ).format(n=name, a=am.group(1),
                                     f=" ".join(("[[" + body + "]]").split())[:80])
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[malformed-tag] crashed (fail open): {exc}")
        return ""


def prose_score_conflict(reply: str):
    """Return a description of a spoken score that disagrees with the reply's own score
    tag, or "". Never raises: any unexpected input yields "" (fail open)."""
    try:
        text = str(reply or "")
        scored = []
        for name, attrs in re.findall(r"\[\[\s*(quiz|check|finalexam)\b([^\]]*)\]\]", text, re.I):
            a = dict((k.lower(), v) for k, v in re.findall(r'([\w-]+)\s*=\s*"([^"]*)"', attrs))
            try:
                c, t = int(a.get("correct", "")), int(a.get("total", ""))
            except (TypeError, ValueError):
                continue
            if t <= 0:
                continue
            scored.append((name.lower(), c, t, (c * 100) // t, _SCORE_TAGS[name.lower()]))
        if not scored:
            return ""
        prose = _spoken_only(text)
        for name, c, t, pct, thr in scored:
            passed = pct >= thr
            if not passed and _SC_PASS_CLAIM.search(prose):
                return ('your words tell the student they passed, but your own [[{n}]] tag '
                        'says {c} of {t} -- {p}%, and the bar is {b}%. Rule 45: the tally is '
                        'arithmetic, not judgment. Say the real score warmly and use rule 35 '
                        'to make the next step feel like a plan, but never call a fail a '
                        'pass.').format(n=name, c=c, t=t, p=pct, b=thr)
            if passed and _SC_FAIL_CLAIM.search(prose):
                return ('your words tell the student they did not pass, but your own [[{n}]] '
                        'tag says {c} of {t} -- {p}%, which clears the {b}% bar. Rule 45: say '
                        'the real result.').format(n=name, c=c, t=t, p=pct, b=thr)
            # Only percentages spoken ABOUT THE RESULT count. In Pre-Algebra half the
            # lesson is percentages -- "what is 25% of 80?" is the problem, not a score
            # claim, and treating it as one flagged a perfectly good reply on test run
            # three. So a sentence has to sound like it is reporting the outcome.
            pct_hits = []
            for sent in re.split(r"(?<=[.!?])\s+|\n+", prose):
                if not _SC_RESULT_CONTEXT.search(sent):
                    continue
                for mm in _SC_PCT.finditer(sent):
                    pct_hits.append((int(mm.group(1)), sent, mm.start(), mm.end()))
            for v, sent, s0, s1 in pct_hits:
                if v == pct:
                    continue
                # The BAR is fair to quote -- "you need 80% to pass" is teaching, not a
                # score claim -- but only when it reads like the bar. Saying "that is 80%"
                # over a 60% tally is the inflation this check exists to stop, and letting
                # the threshold through unconditionally missed exactly that case on the
                # first test run.
                near = sent[max(0, s0 - 45):s1 + 45].lower()
                if v == thr and _SC_BAR_CONTEXT.search(near):
                    continue
                return ('you say "{v}%" but your own [[{n}]] tag is {c} of {t}, which is '
                        '{p}%. Rule 45: the only percentage you may state as the score is '
                        'the one your tally actually gives.').format(
                            v=v, n=name, c=c, t=t, p=pct)
            for num, den in _SC_FRACTION.findall(prose):
                nv, dv = _sc_val(num), _sc_val(den)
                if nv is None or dv is None or int(dv) != t:
                    continue
                if int(nv) != c:
                    return ('you say "{n} out of {d}" but your own [[{g}]] tag records {c} of '
                            '{t}. Rule 45: the score you SAY is the score you WROTE.').format(
                                n=int(nv), d=int(dv), g=name, c=c, t=t)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[scorecheck] crashed (fail open): {exc}")
        return ""


# =============================================================================
# THE CAPTION CHECK (2026-08-14, build gj) -- rule 41, and the tenth referee.
# -----------------------------------------------------------------------------
# From the 2026-08-16 lesson audits: four figures drawn with no caption at all --
# a fractions pie and three cookie pictures, in the two lessons aimed at the
# youngest and most confused students. Rule 41 is not a preference, it is written
# absolutely: "Every figure tag takes caption='...'. Use it, every time."
#
# Why it earns a regeneration rather than a shrug. Rule 41's own words: a picture
# with no caption "hands the student back the one piece of work the picture was
# supposed to do for them -- working out what they are meant to be looking at --
# and a student who is already lost will look at the wrong part of it and feel
# worse." Both audited lessons were exactly that student.
#
# This is the cheapest possible referee: no model call to detect, no judgement, no
# false positives to argue about. A figure either carries a caption or it does not.
# All 306 canonical foundation scripts already pass it, so it never fights the
# authored content -- it only catches what the model improvises.
# -----------------------------------------------------------------------------
_FIGURE_TAGS = ("pie", "objects", "graph", "numberline", "bars", "histogram",
                "dotplot", "boxplot", "scatter", "normal", "twoway", "tree",
                "unitcircle", "righttriangle", "conic", "areamodel", "vector",
                "triangle", "angle", "circle", "machine", "balance")
_FIG_RE = re.compile(r"\[\[\s*(" + "|".join(_FIGURE_TAGS) + r")\b([^\]]*)\]\]", re.I)
_CAPTION_RE = re.compile(r'\bcaption\s*=\s*"\s*([^"]*?)\s*"')


def missing_caption_conflict(reply: str):
    """Return a description of a picture drawn with no caption, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        for m in _FIG_RE.finditer(str(reply or "")):
            cap = _CAPTION_RE.search(m.group(2))
            if cap and cap.group(1).strip():
                continue
            kind = m.group(1).lower()
            return ('you drew a picture -- [[{k} ...]] -- with no caption. Rule 41: EVERY '
                    'figure carries caption="...", every time, and it names what to NOTICE '
                    'rather than what the thing is ("both are four steps from zero", not "a '
                    'number line"). A picture with no caption hands the student back the one '
                    'job the picture was there to do for them, and a student who is already '
                    'lost will look at the wrong part of it and feel worse. Add the caption '
                    'and say its idea out loud too.').format(k=kind)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[caption] crashed (fail open): {exc}")
        return ""


# =============================================================================
# THE SELF-CORRECTION CHECK (2026-08-16, build gl) -- the eleventh referee.
# -----------------------------------------------------------------------------
# The one HIGH finding in the 2026-08-16 audits, quoted exactly:
#
#     "3/4 is smaller than 3/4... wait, let's just confirm: 3 1/4 minus 1 3/4
#      really is 1 1/2."
#
# Read what the child actually received. A false comparison, then the grown-up
# visibly losing confidence in their own sentence, then a recovery -- all shipped.
# The ACCURACY block has always said "fix it BEFORE you say it"; nothing checked
# whether the fixing happened in private. Build gl adds the missing half of that
# rule to every course ("fix it SILENTLY: never let the student watch you change
# your mind") and this referee, which is what makes it true rather than hoped for.
#
# Why it matters more here than in most products: these students are with a tutor
# because they are already unsure. A child who is lost does not read "wait, let me
# check that" as diligence. They read it as the grown-up not knowing either, and
# that is the moment a struggling student stops trusting the room.
#
# DELIBERATELY NARROW. Correcting the STUDENT is the job and must never be touched:
# "actually comes out to 3.45", "not quite -- it's 11", "let's check that one" all
# pass. This fires only on the tutor retracting ITSELF -- a trailing-off "... wait,",
# a "hold on", "scratch that", "actually, no", "my mistake". Fails open.
# -----------------------------------------------------------------------------
_SELF_CORRECT = (
    re.compile(r"\.\.\.\s*wait\b", re.I),
    re.compile(r"\bwait,\s*(?:let'?s|let me|actually|no\b|hang on|i )", re.I),
    re.compile(r"\b(?:hold on|hang on)\b[,\s]", re.I),
    re.compile(r"\bscratch that\b", re.I),
    re.compile(r"\blet me (?:re-?check|redo|try that again|start over)\b", re.I),
    re.compile(r"\bignore (?:that|what i just)\b", re.I),
    re.compile(r"\bactually,?\s*no\b", re.I),
    re.compile(r"\b(?:my mistake|my bad|oops)\b", re.I),
    re.compile(r"\bsorry,?\s*(?:i mean|that'?s wrong|let me)\b", re.I),
    re.compile(r"\bthat'?s not right\b[^.?!]{0,20}\blet me\b", re.I),
)


def self_correction_conflict(reply: str):
    """Return a description of the tutor visibly correcting ITSELF, or "".
    Never raises: any unexpected input yields "" (fail open)."""
    try:
        prose = _spoken_only(str(reply or ""))
        for pat in _SELF_CORRECT:
            m = pat.search(prose)
            if not m:
                continue
            frag = " ".join(prose[max(0, m.start() - 45):m.end() + 25].split())
            return ('you changed your mind out loud -- "...{f}...". Check it BEFORE you '
                    'speak, then say the checked version ONCE. A student watching you '
                    'retract your own sentence does not read it as care; a child who is '
                    'already unsure reads it as the grown-up not knowing either, and that '
                    'is the moment they stop trusting the room. Work it out, decide, and '
                    'give them only the answer you have checked.').format(f=frag)
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[selfcorrect] crashed (fail open): {exc}")
        return ""


def prose_board_conflict(reply: str, student_message: str = ""):
    """Return a short description of a prose-vs-board contradiction, or "" if clean.
    Never raises: any unexpected input yields "" (fail open).

    ELEVEN checks, in order (gj added the caption check, gl the self-correction): a malformed tag (build eq), a picture promised and never
    drawn (rule 7), a computation asked with no pending line on the board (rule 15), a
    spoken score that disagrees with the reply's own score tag (rule 45), the tutor
    answering its OWN question in the same breath (rule 39b -- wait time), a question
    this reply's own board already answers (rule 17, build dh), a board problem the
    spoken words never read aloud (rule 44, build dh), a board notation violation
    (rules 27/15/54, builds dk/dl), a right triangle whose hypotenuse slot cannot be
    the hypotenuse (rule 63c, build fe), then spoken numbers that disagree with the
    board's own written conclusion (rule 18b)."""
    try:
        # build eq: FIRST -- if a tag cannot be parsed, every other referee below is
        # reading a board the student will never actually see.
        malformed = malformed_tag_conflict(reply)
        if malformed:
            return malformed
        # build gj: second, because an uncaptioned picture is the cheapest defect to
        # find and one of the most expensive to a lost student (rule 41).
        caption = missing_caption_conflict(reply)
        if caption:
            return caption
        # build gl: third, and cheap -- the tutor must never be seen changing its mind.
        selfcorrect = self_correction_conflict(reply)
        if selfcorrect:
            return selfcorrect
        visual = prose_visual_conflict(reply, student_message)
        if visual:
            return visual
        pending = prose_pending_question_conflict(reply)
        if pending:
            return pending
        score = prose_score_conflict(reply)
        if score:
            return score
        selfans = prose_self_answer_conflict(reply)
        if selfans:
            return selfans
        answered = prose_answered_question_conflict(reply)
        if answered:
            return answered
        unspoken = prose_unspoken_problem_conflict(reply)
        if unspoken:
            return unspoken
        boardnote = board_notation_conflict(reply)
        if boardnote:
            return boardnote
        triangle = triangle_side_conflict(reply)
        if triangle:
            return triangle
        text = str(reply or "")
        # 1. the board's labeled conclusions, from this reply's own tags
        labeled = {}
        for tag in re.findall(r"\[\[\s*(?:step|write|solve)\b([^\]]*)\]\]", text, re.I):
            for val in re.findall(r'"([^"]*)"', tag):
                m = _PR_BOARD_LINE.match(val.strip())
                if not m:
                    continue
                label = m.group(1).strip().lower()
                if not label or label in ("http", "https"):
                    continue
                try:
                    labeled[label] = (float(m.group(3)), m.group(2))
                except ValueError:
                    pass
        if not labeled:
            return ""
        # 2. the SPOKEN text only (tags stripped -- the student never hears them)
        prose = re.sub(r"\[\[[^\]]*\]\]", " ", text)
        prose = re.sub(r"\[\[[\s\S]*$", " ", prose)
        spoken_numbers = _pr_numbers_in(prose)
        low = prose.lower()
        for label, (result, operands) in labeled.items():
            # 4. if the words DO say the board's number anywhere, there is no contradiction
            if result in spoken_numbers:
                continue
            pat = re.compile(r"(-?\d+(?:\.\d+)?|" + _PR_NUMWORD + r")\s+" + re.escape(label) + r"\b")
            for hit in pat.findall(low):
                try:
                    claimed = float(hit) if re.match(r"^-?\d", hit) else _pr_word_value(hit)
                except ValueError:
                    claimed = None
                if claimed is None:
                    continue
                claimed = float(claimed)
                if claimed == result:
                    continue
                # 5. an operand of the same line is fair to mention in passing
                if claimed in _pr_numbers_in(operands):
                    continue
                return ('your spoken words say "{c} {lab}", but your own board line for '
                        '"{lab}" concludes {r}. Rule 18(b): the numbers you SAY must match '
                        'the numbers you WRITE.').format(
                            c=(int(claimed) if float(claimed).is_integer() else claimed),
                            lab=label,
                            r=(int(result) if float(result).is_integer() else result))
        return ""
    except Exception as exc:  # noqa: BLE001 -- referee crash = fail open, always
        print(f"[prosecheck] crashed (fail open): {exc}")
        return ""


_PROSE_NUDGE = (
    "(SYSTEM: A consistency check found a contradiction in your previous draft: {detail} "
    "The student NEVER saw that draft. Write your reply again from scratch -- same warm "
    "teaching flow -- so that what you SAY and what is actually on the board agree: every "
    "picture you mention is DRAWN by a tag in this same reply, and every number you say "
    "matches the number you write. Your new reply must STAND ALONE: the student saw and "
    "heard NOTHING of the discarded draft, so any worked example, definition, or board "
    "line they need must appear here IN FULL -- never open mid-thought, never say 'so' "
    "about a result you have not shown in THIS reply, never refer to anything only the "
    "draft contained. If the student's answer was wrong, coach the recount "
    "(rules 18 and 22); do not adopt their number. Do not mention this note or any "
    "checking.)")


MATHCHECK_MAX_ATTEMPTS = 3   # 1 normal attempt + up to 2 corrected retries

_MATHCHECK_NUDGE = (
    "(SYSTEM: A math engine checked your previous draft and found an error: {detail}. "
    "The student NEVER saw that draft. Write your reply again from scratch with the "
    "correct math -- same warm teaching flow, same board tags, corrected numbers and "
    "corrected [[verify]] tag(s). Your new reply must STAND ALONE: the student saw and "
    "heard nothing of the discarded draft, so everything they need must appear here in "
    "full -- never open mid-thought or build on something only the draft contained. "
    "Do not mention this note, the mistake, or any checking.)")


def _log_brain_usage(meta, model, tokens, attempts, verify_status):
    """Hand one brain turn's consumption to the store (fire-and-forget; never raises)."""
    if store is None or not meta:
        return
    try:
        store.log_usage(kind="brain", code=meta.get("code", ""), course=meta.get("course", ""),
                        mode=meta.get("mode", ""), model=model,
                        input_tokens=tokens.get("in", 0), output_tokens=tokens.get("out", 0),
                        cache_read_tokens=tokens.get("cr", 0), cache_write_tokens=tokens.get("cw", 0),
                        attempts=attempts, verify_status=verify_status)
    except Exception as exc:  # noqa: BLE001
        print(f"[usage] log failed (non-fatal): {exc}")


def _add_usage(tokens, response):
    """Accumulate the token counts the API just reported into `tokens` (in place)."""
    u = getattr(response, "usage", None)
    if u is None:
        return
    tokens["in"] = tokens.get("in", 0) + int(getattr(u, "input_tokens", 0) or 0)
    tokens["out"] = tokens.get("out", 0) + int(getattr(u, "output_tokens", 0) or 0)
    tokens["cr"] = tokens.get("cr", 0) + int(getattr(u, "cache_read_input_tokens", 0) or 0)
    tokens["cw"] = tokens.get("cw", 0) + int(getattr(u, "cache_creation_input_tokens", 0) or 0)


# BUILD dg (2026-08-11): the continuation is NEGOTIATED, and the ceiling rose.
# The first full audit's Render logs showed claude-sonnet-5 intermittently REJECTING the
# assistant-prefill continuation with a 400 that names its objection ("This model does
# not support assistant message prefill. The conversation must end with a user
# message."). Intermittent is worse than always: it looked like it worked. Every
# rejection surfaced to the student as a stumble. Same philosophy as the build-cz token
# parameter: the API SAYS what it will not accept, so take it at its word -- try prefill
# (seamless when accepted), and on that named 400 switch to a continuation nudge in a
# user message and remember the choice for the rest of the process. Never guessed from
# the model name; names change, and guessing is how you ship a break.
_PREFILL_OK: dict = {}    # model name -> False once the API has refused prefill once

_CONTINUE_NUDGE = (
    "(SYSTEM: Your reply above was cut off by a length limit, mid-flow. Continue it "
    "EXACTLY from where it stopped: output ONLY the continuation -- no greeting, no "
    "recap, no repeated words -- and close any unfinished board tag first. The student "
    "will see your earlier text and this continuation joined as one message.)")

# A CEILING, not a target -- normal turns end far under it and unused headroom costs
# nothing. Raised 1600 -> 3000 (build dg): the audit logs showed tag-heavy teaching
# turns hitting 1600 CONSTANTLY, and five replies shipped as admitted partials in forty
# minutes. Referee retries multiply the exposure, so the ceiling must fit a long,
# figure-heavy teaching turn with room to spare.
MAX_REPLY_TOKENS = 3000


def _is_prefill_rejection(exc) -> bool:
    """True when the API's own words say it refused the assistant-prefill shape."""
    msg = str(exc).lower()
    return "prefill" in msg or "must end with a user message" in msg


def _create_full(client, model, system_blocks, msgs, tokens, log_prefix=""):
    """One LOGICAL model turn that can never be silently truncated. 2026-08-08 (Jim's
    live freeze in Basic Math): the first teaching turn -- tag-heavy ([[today]],
    [[unitplan]], goals, objects) -- hit the old 1200-token ceiling mid-tag; the client
    stripped the dangling tag and the student saw the single word "Let" with an empty
    board and no answer buttons. Nothing anywhere checked stop_reason.
    Now: if the response stops at the max_tokens ceiling (stop_reason == "max_tokens"),
    the model is asked to continue exactly where it stopped -- by assistant prefill when
    the model accepts that shape, by a user-message nudge when it does not (build dg;
    see _PREFILL_OK above) -- and the pieces are stitched together. Up to 2
    continuations (~9000 tokens total -- far beyond any real teaching turn), then we
    return whatever we have rather than loop forever."""
    reply = ""
    hop = 0
    while hop < 3:
        if not reply:
            convo = msgs
        elif _PREFILL_OK.get(model, True):
            convo = msgs + [{"role": "assistant", "content": reply.rstrip()}]
        else:
            convo = msgs + [{"role": "assistant", "content": reply.rstrip()},
                            {"role": "user", "content": _CONTINUE_NUDGE}]
        try:
            response = client.messages.create(
                model=model,
                max_tokens=MAX_REPLY_TOKENS,
                system=system_blocks,
                messages=convo,
            )
        except Exception as exc:  # noqa: BLE001 -- only the NAMED rejection is handled
            if reply and _PREFILL_OK.get(model, True) and _is_prefill_rejection(exc):
                print(f"[tutor]{log_prefix} model refuses assistant prefill -- switching "
                      f"continuations to a user-message nudge for the rest of this run")
                _PREFILL_OK[model] = False
                continue          # retry the SAME hop in the fallback shape
            raise
        part = "".join(block.text for block in response.content
                       if getattr(block, "type", None) == "text")
        _add_usage(tokens, response)
        reply = (reply.rstrip() + part) if reply else part
        if getattr(response, "stop_reason", "") != "max_tokens":
            break
        hop += 1
        if hop < 3:
            print(f"[tutor]{log_prefix} reply hit max_tokens -- continuing (hop {hop}/2)")
        else:
            print(f"[tutor]{log_prefix} reply STILL at max_tokens after 2 continuations -- returning stitched partial")
    return reply.strip()


def _last_user_text(msgs) -> str:
    """The student's most recent words, for the referees that need to know what was
    asked (rules 2 and 8). Ignores the SYSTEM nudges the referee itself appends."""
    try:
        for m in reversed(list(msgs or [])):
            if m.get("role") == "user":
                t = str(m.get("content", ""))
                if not t.lstrip().startswith("(SYSTEM:"):
                    return t
    except Exception:  # noqa: BLE001
        pass
    return ""


# -----------------------------------------------------------------------------
# THE MISSING-MARK PROBE (2026-08-14, build gd) -- MEASUREMENT ONLY. It prints a line
# and changes NOTHING about the reply the student sees.
#
# WHY IT EXISTS. [[mark]] is what records "the student finished a problem" -- their
# score, their accuracy, and (since build fy) the signal that folds a finished problem
# away on the board. The prompt calls it "REQUIRED, not optional" in all ten courses,
# and ruletests checks that the PROMPT SAYS SO -- but nothing has ever checked that the
# tutor actually emits one. On 2026-08-14 Jim's Render log showed the difference plainly:
# an Algebra I lesson posted /api/mark three times and behaved perfectly, while a
# Geometry lesson posted it ZERO times even though the student was handed
# "130 + ? = 180", answered fifty, and was told "exactly right".
#
# WHY IT ONLY MEASURES. The obvious next step is a referee that regenerates the reply,
# or a net that awards the mark itself. Both are premature and one is dangerous: a net
# that guesses would inflate a child's recorded accuracy, which is worse than losing a
# point. Retired ensure_board is the standing lesson here -- a net that guesses caused
# more harm than the gap it filled. So this counts the gap first, on real lessons, and
# the decision comes after the number does.
#
# DELIBERATELY NARROW, so a logged line means something: it fires only when the tutor's
# PREVIOUS turn put a pending line on the board (a "?" standing in for the unknown --
# the same signal rule 15 and prose_pending_question_conflict already use), the student
# then said something, and THIS reply writes a settled line while recording neither
# [[mark]] nor [[nice]]. Fails open everywhere.
# -----------------------------------------------------------------------------
def _last_assistant_text(messages) -> str:
    """The tutor's own previous turn, from the ORIGINAL message list (never the
    discarded drafts a referee retry appends)."""
    try:
        for m in reversed(list(messages or [])):
            if m.get("role") == "assistant":
                return str(m.get("content", ""))
    except Exception:  # noqa: BLE001
        pass
    return ""


def _board_attr_strings(text):
    """The attribute text of every board tag in this reply."""
    try:
        return [t[1] for t in re.findall(
            r"\[\[\s*(" + "|".join(_PQ_BOARD_TAGS) + r")\b([^\]]*)\]\]",
            str(text or ""), re.I)]
    except Exception:  # noqa: BLE001
        return []


def missing_mark_probe(reply: str, messages) -> str:
    """Describe a turn that looks like a finished problem carrying no [[mark]] and no
    [[nice]], or "" when there is nothing to report. Never raises."""
    try:
        text = str(reply or "")
        if re.search(r"\[\[\s*(mark|nice)\b", text, re.I):
            return ""                       # something was recorded -- nothing to say
        pending = [a for a in _board_attr_strings(_last_assistant_text(messages)) if "?" in a]
        if not pending:
            return ""                       # no problem was posed, so none was finished
        if not [a for a in _board_attr_strings(text) if "?" not in a]:
            return ""                       # still open -- they have not finished it yet
        if not _last_user_text(messages).strip():
            return ""                       # the student has not answered anything
        return ('the previous turn left a pending line on the board ("%s") and this reply '
                'writes a settled one while recording neither [[mark]] nor [[nice]] -- if '
                'the student just finished that problem, the credit was not recorded'
                % " ".join(pending[-1].split())[:70])
    except Exception:  # noqa: BLE001 -- a probe must never affect a lesson
        return ""


def _create_verified(client, model, system_blocks, messages, log_prefix, meta=None):
    """One model call, refereed. Returns the verified reply with [[verify]] tags
    stripped, or "" if the model returned nothing (caller shows its fallback).
    `meta` ({code, course, mode}) attributes the turn's usage to a student for the
    cost log -- counts only, never text."""
    msgs = list(messages)
    reply = ""
    tokens = {}
    for attempt in range(1, MATHCHECK_MAX_ATTEMPTS + 1):
        reply = _create_full(client, model, system_blocks, msgs, tokens, log_prefix)
        if not reply:
            # BUILD dg: a student who hears "I lost my train of thought" repeats
            # themselves -- so the code repeats itself FIRST. One silent retry before
            # the apology; the audit counted that apology 6 times in 10 lessons, so
            # this path is common enough to matter.
            print(f"[tutor]{log_prefix} model returned an EMPTY reply -- retrying once")
            reply = _create_full(client, model, system_blocks, msgs, tokens, log_prefix)
        if not reply:
            _log_brain_usage(meta, model, tokens, attempt, "empty")
            return ""
        if mathcheck is None:
            # Verifier missing on this deploy (defensive import failed): skip the
            # check, but STILL strip any [[verify]] tags so they never leak out.
            _log_brain_usage(meta, model, tokens, attempt, "")
            return re.sub(r"\[\[\s*verify\b[^\]]*\]\]", "", reply).strip()
        try:
            verdict, detail = mathcheck.verify_reply(reply)
        except Exception as exc:  # noqa: BLE001 -- referee crash = fail open
            print(f"[mathcheck]{log_prefix} checker crashed (fail open): {exc}")
            verdict, detail = "unverifiable", str(exc)
        if verdict != "wrong":
            if verdict == "unverifiable":
                print(f"[mathcheck]{log_prefix} unverifiable (passed through): {detail}")
            # THE PROSE REFEREE (2026-08-09): the tags are sound -- now check that the
            # SPOKEN words agree with them (see prose_board_conflict above). Same
            # treatment as a failed math check: the student never saw this draft.
            prose_detail = prose_board_conflict(reply, _last_user_text(msgs))
            if prose_detail and attempt < MATHCHECK_MAX_ATTEMPTS:
                print(f"[prosecheck]{log_prefix} CONTRADICTION on attempt "
                      f"{attempt}/{MATHCHECK_MAX_ATTEMPTS}: {prose_detail}")
                msgs = msgs + [{"role": "assistant", "content": reply},
                               {"role": "user", "content": _PROSE_NUDGE.format(detail=prose_detail)}]
                continue
            if prose_detail:
                print(f"[prosecheck]{log_prefix} UNRESOLVED -- passing through: {prose_detail}")
            # build gd: MEASUREMENT ONLY -- see missing_mark_probe above. Never alters
            # the reply, never costs a model call; it just counts a gap we cannot
            # currently see. Runs on the ACCEPTED draft only.
            try:
                _mark_gap = missing_mark_probe(reply, messages)
                if _mark_gap:
                    print(f"[markcheck]{log_prefix} POSSIBLE MISSED MARK: {_mark_gap}")
            except Exception as _exc:  # noqa: BLE001 -- a probe must never fail a turn
                print(f"[markcheck]{log_prefix} probe crashed (ignored): {_exc}")
            status = verdict if verdict != "ok" else ("ok" if attempt == 1 else "fixed")
            if prose_detail:
                status = "prose-unresolved"
            _log_brain_usage(meta, model, tokens, attempt, status)
            return mathcheck.strip_verify_tags(reply)
        print(f"[mathcheck]{log_prefix} WRONG on attempt {attempt}/{MATHCHECK_MAX_ATTEMPTS}: {detail}")
        if attempt < MATHCHECK_MAX_ATTEMPTS:
            msgs = msgs + [{"role": "assistant", "content": reply},
                           {"role": "user", "content": _MATHCHECK_NUDGE.format(detail=detail)}]
    # Three drafts in a row judged wrong, WITH the correction in hand, almost always
    # means the CHECKER mis-read an unusual claim -- so pass the last draft through
    # (fail open) rather than brick the lesson, and log loudly for the developer.
    print(f"[mathcheck]{log_prefix} UNRESOLVED after {MATHCHECK_MAX_ATTEMPTS} attempts -- passing through")
    _log_brain_usage(meta, model, tokens, MATHCHECK_MAX_ATTEMPTS, "unresolved")
    return mathcheck.strip_verify_tags(reply)


def get_tutor_reply(student: dict, history: list, user_message: str,
                    course: str = DEFAULT_COURSE, code: str = "",
                    turn_note: str = "") -> str:
    """
    Ask Claude for the tutor's next reply.

    student       -- the student record (name, progress, ...)
    history       -- prior conversation as a list of {"role","content"} dicts
                     where role is "user" (the student) or "assistant" (tutor)
    user_message  -- what the student just said

    Returns the tutor's reply as plain text. On a configuration or API problem
    it returns a friendly, human-readable message instead of crashing, so the
    app keeps running and the tester sees a clear explanation.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return ("(Setup needed: I can't reach my brain yet. Please add the "
                "ANTHROPIC_API_KEY environment variable in Render, then reload "
                "this page.)")

    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)

    messages = _trim_history(list(history or []))
    # PER-TURN NOTES RIDE WITH THE STUDENT'S MESSAGE, NOT THE SYSTEM PROMPT
    # (2026-08-10, build cm). The system prompt is ONE cached block. Anything that
    # changes it changes the cache prefix, so a note appended into it re-bills every
    # token from that point on -- the build-ck misconception hint sat 63,629 characters
    # in, which threw away ~16k tokens of cache on the exact turns it fired. A note is
    # about THIS turn, so it belongs beside THIS turn's message, where nothing is cached
    # anyway. The system prompt is now byte-identical from turn to turn.
    messages.append({"role": "user",
                     "content": (user_message + turn_note) if turn_note else user_message})

    try:
        client = Anthropic(api_key=api_key)
        # MATH VERIFIER (2026-08-03): the reply is generated AND refereed in here --
        # see _create_verified above. Same model, same prompt, same max_tokens.
        reply = _create_verified(
            client, model,
            _cacheable_system(build_system_prompt(student, course)),
            messages, " [lesson]",
            meta={"code": code, "course": course, "mode": "lesson"},
        ) or "(Sorry, I lost my train of thought. Could you say that again?)"
        # build bo: deterministic TODAY-bar net (lesson mode only) -- see ensure_today_tag.
        return ensure_today_tag(ensure_board(reply, user_message, history), history,
                                today_live=bool((student or {}).get("today_live")))
    except Exception as exc:  # noqa: BLE001  -- we want a graceful UI message
        # We deliberately never leak a raw stack trace to a student. We log it
        # for the developer and show a calm message instead.
        print(f"[tutor] Claude API error: {exc}")
        return ("(I'm having trouble thinking right now -- give me a moment and "
                "try again.)")


def _subject(course: str) -> str:
    return COURSE_SUBJECT.get(course or DEFAULT_COURSE, "math")


# =============================================================================
# NARRATIVE ASSESSMENTS (2026-08-01) -- "How am I doing?" in a human voice
# =============================================================================


def get_assessment(facts: str, audience: str = "student", code: str = "",
                   course: str = "") -> str:
    """One honest narrative paragraph from real progress facts. `audience` is
    'student' or 'parent'. Returns friendly error text on config/API problems.
    `code`/`course` (2026-08-04) attribute the call's usage to the cost log."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return ("(Setup needed: the assessment writer can't reach its brain yet -- "
                "the ANTHROPIC_API_KEY environment variable is missing.)")
    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)
    system = ASSESSMENT_SYSTEM_PARENT if audience == "parent" else ASSESSMENT_SYSTEM_STUDENT
    try:
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model=model, max_tokens=400,
            system=_cacheable_system(system),
            messages=[{"role": "user", "content": facts}],
        )
        parts = [b.text for b in response.content if getattr(b, "type", None) == "text"]
        tokens = {}
        _add_usage(tokens, response)
        _log_brain_usage({"code": code, "course": course, "mode": "assessment"},
                         model, tokens, 1, "")
        return "".join(parts).strip() or "(I couldn't put the words together just now -- try again in a moment.)"
    except Exception as exc:  # noqa: BLE001
        print(f"[assessment] Claude API error: {exc}")
        return "(I couldn't write the assessment just now -- give it a moment and tap again.)"


def build_practice_prompt(student: dict, problem: str, course: str = DEFAULT_COURSE) -> str:
    """Fill the practice template with this student's name and their problem, for a course."""
    name = (student or {}).get("name", "the student")
    problem = (problem or "").strip() or "(The student hasn't stated the problem clearly yet -- ask them what it is.)"
    _u = _unit_from_text(problem, course)          # build gb: also filters the scripts
    # build gf: never leave the filter off -- fall back to their placed unit, then to 1.
    _fu = _u or _unit_from_progress((student or {}).get("progress") or "") or _FILTER_UNIT_FALLBACK
    playbook = _playbook(_u, course)
    return GROUND_RULES + GRAPH_TOOL_NOTE + PRACTICE_SYSTEM_PROMPT_TEMPLATE.format(
        tutor_name=TUTOR_NAME,
        student_name=name,
        problem=problem,
        playbook=playbook,
        subject=_subject(course),
        scope_block=PRACTICE_SCOPE.get(course or DEFAULT_COURSE, PRACTICE_SCOPE[DEFAULT_COURSE]),
    ) + _notation_block(course) + _misconception_block(course) + _foundation_block(course, (student or {}).get("foundations_heard"),
                      (student or {}).get("foundations_verbatim", True), _fu)


def get_practice_reply(student: dict, problem: str, history: list, user_message: str,
                       course: str = DEFAULT_COURSE, code: str = "") -> str:
    """
    Ask Claude for the coach's next reply in a PRACTICE session.

    student       -- the student record (name, ...)
    problem       -- the specific problem the student is stuck on (their words)
    history       -- prior practice conversation [{"role","content"}, ...]
    user_message  -- what the student just said (or the problem, on the first turn)

    Practice history is held by the browser and passed in each request, so nothing
    is persisted server-side -- a homework problem is a one-off. Returns plain text,
    with a friendly message (never a stack trace) on any error.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return ("(Setup needed: I can't reach my brain yet. Please add the "
                "ANTHROPIC_API_KEY environment variable in Render, then reload "
                "this page.)")

    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)

    messages = _trim_history(list(history or []))
    messages.append({"role": "user", "content": user_message})

    try:
        client = Anthropic(api_key=api_key)
        # MATH VERIFIER (2026-08-03): generated AND refereed -- see _create_verified.
        reply = _create_verified(
            client, model,
            _cacheable_system(build_practice_prompt(student, problem, course)),
            messages, " [practice]",
            meta={"code": code, "course": course, "mode": "practice"},
        ) or "(Sorry, I lost my train of thought. Could you say that again?)"
        return ensure_board(reply, user_message, history)
    except Exception as exc:  # noqa: BLE001
        print(f"[practice] Claude API error: {exc}")
        return ("(I'm having trouble thinking right now -- give me a moment and "
                "try again.)")


def build_topic_prompt(student: dict, topic: str, course: str = DEFAULT_COURSE) -> str:
    """Fill the topic template with this student's name and their chosen topic, for a course."""
    name = (student or {}).get("name", "the student")
    topic = (topic or "").strip() or "(The student hasn't named a topic yet -- ask them what they'd like to explore.)"
    _u = _unit_from_text(topic, course)            # build gb: also filters the scripts
    # build gf: never leave the filter off -- fall back to their placed unit, then to 1.
    _fu = _u or _unit_from_progress((student or {}).get("progress") or "") or _FILTER_UNIT_FALLBACK
    playbook = _playbook(_u, course)
    return GROUND_RULES + GRAPH_TOOL_NOTE + TOPIC_SYSTEM_PROMPT_TEMPLATE.format(
        tutor_name=TUTOR_NAME,
        student_name=name,
        topic=topic,
        playbook=playbook,
        subject=_subject(course),
        scope_block=TOPIC_SCOPE.get(course or DEFAULT_COURSE, TOPIC_SCOPE[DEFAULT_COURSE]),
    ) + _notation_block(course) + _misconception_block(course) + _foundation_block(course, (student or {}).get("foundations_heard"),
                      (student or {}).get("foundations_verbatim", True), _fu)


def get_topic_reply(student: dict, topic: str, history: list, user_message: str,
                    course: str = DEFAULT_COURSE, code: str = "") -> str:
    """
    Ask Claude for the tutor's next reply in a TOPIC mini-lesson.

    Same shape as get_practice_reply: topic history is held by the browser and passed
    in each request, so nothing is persisted here. Returns plain text, with a friendly
    message (never a stack trace) on any error.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return ("(Setup needed: I can't reach my brain yet. Please add the "
                "ANTHROPIC_API_KEY environment variable in Render, then reload "
                "this page.)")

    model = os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL)

    messages = _trim_history(list(history or []))
    messages.append({"role": "user", "content": user_message})

    try:
        client = Anthropic(api_key=api_key)
        # MATH VERIFIER (2026-08-03): generated AND refereed -- see _create_verified.
        reply = _create_verified(
            client, model,
            _cacheable_system(build_topic_prompt(student, topic, course)),
            messages, " [topic]",
            meta={"code": code, "course": course, "mode": "topic"},
        ) or "(Sorry, I lost my train of thought. Could you say that again?)"
        return ensure_board(reply, user_message, history)
    except Exception as exc:  # noqa: BLE001
        print(f"[topic] Claude API error: {exc}")
        return ("(I'm having trouble thinking right now -- give me a moment and "
                "try again.)")


# I did no harm and this file is not truncated.
