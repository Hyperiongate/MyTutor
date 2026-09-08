# CHANGELOG -- tutor.py  (notes rolled out of the file's header)

Moved out of `tutor.py` on 2026-09-08 (build ui): every CHANGE NOTE dated before 2026-09-01 -- 191 entries, VERBATIM, in the order they sat in the file (newest first). The 27 notes from 2026-09-01 on stay at the top of `tutor.py` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
#   2026-08-31  BUILD rc -- THE STAR FALLS WHEN THE CHILD SLIPS: code's own grade. Jim's
#               ruling: a miss is ANY WRONG TAP. The prompt's new [[miss]] tag asks the
#               model to report a mid-problem slip, but a tag is a nudge, not a
#               guarantee (the qw lesson), so NEW answer_slip()/expected_answer_for()/
#               child_answer_token() are the code floor: when the previous tutor turn
#               left a question whose answer CODE CAN COMPUTE (the same qw/ra parsers --
#               one grammar, two consumers) and the child's message is a BARE answer
#               that disagrees, main.py's chat handler resets the today-streak without
#               waiting for the model. Cautious by design: sentences, uncomputable asks,
#               non-comparative words, and same-direction synonyms ("bigger" for
#               "greater") are never slips -- a wrongly fallen star is worse than a late
#               one. Grading accepts negative truths the repair refuses to OFFER.
#   2026-08-31  BUILD ra -- THE LEFTOVER GETS ITS BUTTONS. Jim, live on entry/basic the
#               same evening qw deployed: "some of the times it's missing bubbles."
#               Measured first: referee 58's detector FIRES on every shape he saw, and
#               repair_missing_buttons answered "unrepairable" to all of them -- it only
#               knew plain a-op-b arithmetic, so the youngest courses' bread-and-butter
#               asks (comparisons, one-more/one-less, comes-after/before) shipped
#               bubble-less as counted pass_through residue. NEW _rb_counting_shapes():
#               four classes, still computed-never-guessed (the build-pt law), FINAL
#               SPOKEN ASK ONLY -- (A) "which is bigger, X or Y?" offers the question's
#               own pair, the true answer present BY CONSTRUCTION; (B) "is X greater or
#               less than Y?" offers its own two relation words; (C) one more/less than
#               N and (D) comes after/before N compute N±1 into the arithmetic repair's
#               exact row shape (floored, rotated). Refusals: X == Y, one-less-than-zero,
#               before-zero, and every word problem -- a repair that reads stories is a
#               repair that guesses. The arithmetic branch is BYTE-UNTOUCHED and still
#               runs first; its own refusals still refuse. Events unchanged
#               (code_repair / pass_through · elembuttons). PART 3hb proves each class
#               failable and re-proves the pt grid law over the new rows.
#   2026-08-31  BUILD qx -- THE 08-29 REVIEW'S LAST TWO ITEMS (R7, R8), plus the qask
#               measurement pinned. ① R7: rule 15's referee learns the COMMAND ASK.
#               Measured first: "Simplify eight twelfths?" AND "Simplify 8/12?" BOTH
#               slipped (one number, no operator word -- the verb IS the operator). A
#               closed verb list (simplify/reduce/convert/evaluate/solve/factor/expand/
#               round/work out) plus one number now qualifies, FINAL SENTENCE ONLY --
#               the canon sweep caught precalc's mid-turn "how many angles solve it?"
#               (teaching, answered in the next breath) and the scope takes it out. Net
#               new canon hits: 0. ② R8, measurement only: changed_expression_probe
#               (rule 64 -- the child's "3 + 2 x 4" silently worked as "2 + 3 x 4").
#               Fires probe · expressionswap with "reordered" vs "replaced" in the
#               detail; the counts decide whether a referee is worth its false-positive
#               risk, which is the design question R8 left open. No behaviour changes.
#   2026-08-31  BUILD qw -- THE BUTTONS GUARANTEE. Referee 58 could only NUDGE: three
#               failed attempts and _settle shipped the least-bad draft anyway, which in
#               Entry-Level and Basic is a question a child who cannot type has no way
#               to answer (the watch counted 84 replies/week shipped with a standing
#               finding). NEW repair_missing_buttons() runs at the moment of shipping,
#               on EVERY exit of _create_verified (the accepted draft, the settled
#               pass-through, the degraded no-verifier path -- one _shipped() door): if
#               referee 58's own test still fires, it reads the pending problem off the
#               reply's OWN board ("4 + 3 = ?", or the spoken "what is four plus
#               three?"), COMPUTES the answer, and appends the scripted lane's exact
#               choices row (answer + neighbours, floored, per-problem rotation).
#               ⚠️ COMPUTED, NEVER GUESSED (the build-pt law: the answer must be among
#               the choices): plain + − × ÷ on small whole numbers only, division only
#               when even, take-away only when non-negative. Anything else ships as
#               today and logs pass_through · elembuttons so the night watch counts the
#               leftover. Events: code_repair · elembuttons on every repair. The nudges
#               still run first -- the model's child-slip distractors beat code's
#               neighbours; this is the floor under the floor.
#   2026-08-31  BUILD qv -- THE WATCH'S THREE REFEREE-SHAPED FINDINGS, measured first:
#               ① REFEREE 67, fraction_orientation_conflict (rule 63): "the TOP number
#               is the numerator" spoken over a board showing 1/4 with a SLASH -- the
#               child sees left and right, not top and bottom. Fires only when the
#               top/bottom sentence also says fraction/numerator/denominator (so column
#               addition's honest "add the top number" never fires) and the prose never
#               says "slash", the one word that bridges the notations. notation.py has
#               carried that exact bridge since build dk; now it has teeth.
#               ② REFEREE 68, second_triangle_conflict (rule 26): a second, DIFFERENT
#               [[triangle]] drawn with no [[clear]] while the first still stands --
#               every triangle is A,B,C/a,b,c, so the child sees two conflicting
#               definitions of the same names. Referee 56 only fires on NUMBERED
#               questions; the watch's unnumbered new problem slipped past it. The
#               board's contents = the conversation since its last [[clear]], which is
#               exactly how the board is designed to persist. Re-drawing the SAME
#               triangle stays silent.
#               ③ funcrule's NOT-NEW gate became NOT-YET-READ: the watch shipped
#               g(x) = 3x - 2 written and never read, and the old gate makes that
#               reachable in two turns (introduce without a question: silent; ask
#               later: "not new", silent). A rule seen before now buys silence only if
#               its READING ("g of x") was heard too. The existing silence for a rule
#               both written AND read before is pinned and unchanged.
#   2026-08-31  BUILD qu -- TWO ROWS FROM THE FIRST HEALTHY NIGHT WATCH. The 2026-08-31
#               watch (the first on the Anthropic seat since the DeepSeek trial ended)
#               confirmed two false wordings in live lessons, and both are exactly what
#               KNOWN_FALSEHOODS was built for -- no new referee, one row each:
#                 * division-always-makes-smaller ("division -- that's when we split a
#                   group of things into equal smaller groups", basic course, rule 61).
#                   Dividing by 1 leaves the group the same size; the condition -- MORE
#                   THAN ONE group -- is the escape, and the true form carries it.
#                 * symbol-read-as-expression ('that little "÷" is the division sign,
#                   read "two divided by two"', prealgebra, rule 48/61). A symbol's
#                   name never holds a number: the sign is read "divided by", the
#                   EXPRESSION 2 ÷ 2 is read "two divided by two". The escape is the
#                   correct short reading appearing anywhere in the reply, which the
#                   right sentence always carries -- so teaching both readings in one
#                   sentence stays silent.
#               FIRES + SILENT lines ride PART 3ge as its design demands; the table's
#               canon sweep covers the new rows automatically (0 hits).
#   2026-08-30  BUILD qs -- COUNT OUT LOUD WITH ME, AND THE REFEREE THAT KEEPS IT HONEST.
#               Jim, on the Entry-Level turn he read on 2026-08-30: Mr. Cadabra had said
#               "point to each one and count out loud with me" -- a line nobody asked him
#               for -- over a board that had drawn every star in the same instant. "I
#               liked it... maybe he could have said one star with a check over, two stars
#               with a check over, three stars with a check over."
#               board.js's [[objects]] tag now takes count="1": the things land ONE AT A
#               TIME, each with its own ✓ and number, paced to voice.js's new
#               "mt:speaking" event -- his real voice, not a timer racing it.
#               ⚠️ THAT PRINTS THE COUNT, and this board otherwise never does ("counting
#               them is the child's job"). So THE SIXTY-SIXTH REFEREE, counted_drawing_
#               conflict: a reply whose last spoken thing is a QUESTION and whose LAST
#               [[objects]] tag carries count= is rejected, because the picture answers
#               the question before the child counts anything (rule 17). The LAST tag is
#               the one deliberately: an earlier counted drawing in the same reply is the
#               MODEL, which is exactly where the attribute belongs -- so the
#               Model-Lead-Test turn this was built for passes untouched.
#               _SCRIPT_INTERVENE_SYSTEM's MODEL step now asks for count="1" and says in
#               so many words that step 3 draws plain. Canon swept clean.
#   2026-08-30  BUILD qm -- EVERY QUIZ ANSWER GETS A VERDICT (the SIXTY-FIFTH referee).
#               Jim, live in a Geometry quiz: "Question one, correct. Two, correct.
#               Three, correct. Question four, I answer it, and it goes right to question
#               five ... we need to be consistent." Rule 47(i) already SAID it ("'Correct'
#               or 'not quite', next question") and prompt words alone did not hold it.
#               quiz_verdict_conflict: previous turn asked a numbered question, the
#               student answered, this reply asks the next one with no verdict before it.
#               A score line or a [[mark]] counts as a verdict; one that lands after the
#               next question does not. Canon swept 0 of 2,109. PART 3gp.
#   2026-08-30  BUILD ql -- THE DEEPSEEK TRIAL ENDED (Jim's call). Nothing about the seat
#               machinery is removed -- it is env-gated and inert with TUTOR_PROVIDER
#               unset -- but _privacy_page_names now STRIPS HTML COMMENTS before it
#               reads the page. ql's own change note in privacy.html explains at length
#               why DeepSeek was removed, and on a raw substring check that note would
#               have RE-OPENED the gate it was written to close. A processor is "named"
#               only where a parent can read it. (ruletests' code_only() exists for this
#               exact trap; build ki says it fired five times in one evening.)
#   2026-08-30  BUILD qi -- REACHED, OR REFUSED. Jim on the outage: "somehow the
#               DeepSeek wasn't being called." A call that NEVER GOT THERE (DNS,
#               egress, proxy, TLS) and a vendor that answered and refused (401 / 404 /
#               400) look identical from the child's seat and have nothing in common as
#               problems. NEW BrainUnreachable names the first, with the host and URL in
#               its words, so /api/admin/seat-check can report `reached` from the TYPE
#               instead of sniffing a string. PART 3gm.
#   2026-08-30  BUILD qh -- THE SEAT THAT CANNOT TEACH HANDS THE CLASS BACK. The first
#               night on qg's DeepSeek seat: 120 teaching-path fail-opens, every turn of
#               every lesson, and the child got "(I'm having trouble thinking right
#               now)". The catch-all in _reply_pipeline was written for a ONE-BRAIN
#               world; qg added a challenger seat and left it alone, so one wrong env
#               value took the live lane down for a night. Now a non-Anthropic seat that
#               raises hands THIS TURN to Anthropic and is marked down STICKY
#               (_SEAT_DOWN / _seat_down / _seat_is_down) so the next child does not pay
#               the same failed lookup; the failopen event carries provider/model; the
#               apology survives for both-brains-down. active_brain reports a downed
#               seat. PART 3gl.
#   2026-08-29  BUILD qg -- THE DEEPSEEK BRAIN. Jim: "we're gonna use DeepSeek instead of
#               Opus ... until I say different." TUTOR_PROVIDER=deepseek seats DeepSeek
#               (deepseek-v4-pro; DEEPSEEK_REASONING_EFFORT off|low|high|max, default
#               low) on _OpenAIBrain, now an OpenAI-COMPATIBLE adapter (url, extra body,
#               vendor). The critic seat can sit there too (thinking off). Every referee,
#               nudge and usage line is untouched. THE LAW: _deepseek_teaching_allowed
#               reads static/privacy.html -- no DeepSeek named on the page, no DeepSeek
#               seat (loud fallback, privacy_gate event), because DeepSeek stores data in
#               the People's Republic of China and parents were promised a named list.
#               active_brain() reports the live seat to /health and /admin. PART 3gk.
#   2026-08-29  BUILD qf -- TWO THOUGHTS ON ONE LINE (the SIXTY-FOURTH referee). Jim's
#               screenshot: "4x² + 3x² = 7x²   4x² + 7x stays as it is" -- "more than one
#               idea on a line." board_two_thoughts_conflict: a board line that
#               finishes one equation and then starts another expression (a TERM then
#               an OPERATOR after "= result"). Its canon sweep found the line itself in
#               the algebra1 like-terms foundation card, plus three more authored cards
#               using runs of spaces as separators -- all split in foundations.py.
#               Sweep after: 0 of 2,109 cards + 3,699 bank boards. PART 3gj.
#   2026-08-29  BUILD qd -- THE INTERVENTION TEACHES THE PROBLEM THAT WAS ASKED. Jim's
#               screenshots: an Algebra II absolute-value miss (|6 − 9|, he said "Two")
#               became "let's count every star: 6 + 9 = 15". script_intervention
#               reduced EVERY op to + or − (pv fixed one character of this; every
#               OP_EXT op still fell through to "+"). The note is now built by the
#               engine that asked the question -- lessonscripts.spoken_for, board_for,
#               ans, and OP_EXT's praise line -- and _SCRIPT_INTERVENE_SYSTEM scopes the
#               star recipe to plain adding/taking away of small numbers, with "never
#               swap the problem" said outright. Still < 2500 chars. PART 3gi. (The
#               companion client bug -- the redo going to the live tutor -- is in
#               static/session.html.)
#   2026-08-29  BUILD qb -- THE CHECK THAT CAN BE FAILED. The watch's rule-39 finding:
#               "Does that difference make sense?" cannot be failed. New _BARE_CHECK_RE
#               in finite_answer_conflict: a bare comprehension ask ending the turn is
#               nudged to rule 39(d)'s OWN required form ("Does that click, or should I
#               show it a different way?" + It clicks | Show me another way) -- checked
#               before the plain yes/no so "Got it?" is caught. Also _EITHER_OR_RE now
#               takes NUMERIC alternatives ("Which is bigger, 3 or 5?"), final sentence
#               only (3 canon worked-example hits before the scope, 0 after). PART 3gg.
#   2026-08-29  BUILD qa -- ONE ENTRY PER FUNCTION LETTER (rule 48). The 2026-08-29 watch:
#               g(2) = 8 written after f(x), "g of two" never said. The notation
#               referee's entry held f/g/h in ONE class (f in the history made g
#               "known") and required a letter argument (g(2) was never seen). Three
#               entries now, each its own first use, numeric arguments included; the
#               nudge quotes "g of two". Lenient canon sweep 0; strict ceiling 12
#               recorded in PART 3gf. This is Jim's 2026-08-09 "flipped over to g of x".
#   2026-08-29  BUILD pz -- THE NAMED LIST OF FALSEHOODS (the SIXTY-THIRD referee).
#               The 2026-08-29 watch confirmed three false universals ("the hypotenuse
#               always gets the letter c"; "division is sharing until nothing's left
#               over"; "every digit's in the ones place"). Rule 61 was enforced live for
#               two topics only; everything else was prompt words. NEW KNOWN_FALSEHOODS
#               table + known_falsehood_conflict: each entry is the false sentence
#               itself, its escape condition, and the true form the nudge dictates.
#               PART 3w's ten authored bans join it live (precedence excluded -- the
#               37th owns it). True absolutes untouched. Canon swept 0 of 2,109. PART 3ge.
#   2026-08-29  BUILD py -- THE PLAIN YES/NO GETS ITS BUTTONS. Jim, restating a standing
#               rule: "whenever there's a yes or no or a binary answer, we should have
#               bubbles -- throughout." finite_answer_conflict knew six shapes, each
#               from one screenshot; the 2026-08-29 watch's "Does that difference make
#               sense?" matched none. New _PLAIN_YESNO_RE: the FINAL sentence opens
#               with an auxiliary verb, holds no "or" and no wh-word, ends in "?".
#               Check-ins get "Yes | Not yet" (Jim's pick), factual yes/no gets
#               "Yes | No". Canon swept 0 of 2,109 cards. PART 3gd, both directions.
#   2026-08-29  BUILD px -- SHIP THE BEST DRAFT, AND READ THE CRITIC'S VERDICT. The
#               2026-08-29 night watch finally printed the livecritic crash REASONS
#               (build pq's eyes): "Extra data: line 6 column 1" -- json.loads refusing
#               a verdict the critic kept talking after, because the parse sliced from
#               the first brace to the LAST one. New _critic_verdict reads ONE object
#               with raw_decode; trailing chatter is counted as referee_soft, not a
#               crash. (The other reason, "claude-haiku-4.5 not found", is the 08-26
#               typo incident still inside the 7-day window; Render is correct.) And
#               the bigger number: 66 replies shipped WITH a known finding in 7 days --
#               every one from _create_verified shipping the THIRD draft, whatever it
#               was. New _best_draft ranks the kept drafts (critic < prose < mathcheck,
#               newest wins a tie) and ONE _settle path ships the least-bad one, logging
#               WHICH attempt shipped. Zero extra model calls. PART 3gb, both directions.
#               Also NEW rule_titles(): the rule registry as a function (the battery's
#               own RULES.md extraction), so nightwatch's reviewer renders its conduct
#               list from it instead of a hand list that drifted three times. PART 3gc.
#   2026-08-28  BUILD pv -- THE INTERVENTION WAS TOLD TO TEACH THE WRONG OPERATION.
#               script_intervention's note names the real operator ("The problem was
#               90 - 29") and then said, hardcoded, "Teach Model-Lead-Test on {a} + {b}
#               now" -- a PLUS for every problem, subtraction included. That is how
#               Jim's Geometry angle lesson ended up teaching place value. It now
#               teaches {a} {op} {b}. One line, from a screenshot.
#   2026-08-28  BUILD pt -- THE CHILD CANNOT BE RIGHT (referees 60, 61, 62), from
#               Jim's flag queue. A prealgebra reply asked "1 + 2 = ?" and offered
#               9 | 4 | 7 -- the answer absent, every tap marked wrong, recorded as a
#               maths failure the child did not earn. MEASURED: all 59 referees silent,
#               mathcheck "ok", because every equation the board STATES is true. We
#               checked the teacher's arithmetic and never asked whether the CHILD
#               could be right. The same reply also wrote "1 + 2 = 3" above the
#               question (rule 17), and a third flag asked for "the first move on the
#               left side" with no board at all (rule 15). All three swept clean over
#               2,829 cards. A FOURTH flag ("plus negative 2 plus 3") was NOT made a
#               referee -- 4 canon hits, all in pre-u3-adding-a-negative -- and became
#               a HOW YOU SPEAK clause instead. See ruletests PART 3fx.
#   2026-08-28  BUILD ps -- RULE 61'S SECOND ENFORCED SLICE (the FIFTY-NINTH referee).
#               Two night-watch falsehoods in one limits-hole lesson: "a hole never
#               just appears... it comes from dividing by zero" and "cancelling always
#               leaves a hole". Both false -- (x-1)/(x-1)² cancels and is still an
#               ASYMPTOTE. ⚠️ RULE 61(c) ALREADY NAMED THIS CASE with the true form
#               written out, and the model said the false thing anyway: a rule held by
#               prompt words alone is a wish, so the case was PROMOTED rather than
#               re-worded. Narrow, sentence-scoped, always satisfiable (one mention of
#               asymptote/simplified/survives buys silence). ⚠️ The canon sweep fired on
#               OUR OWN calculus foundation card ("a hole never simply appears") -- see
#               foundations.py, same build. One shape CUT: 'we always say "f of 6"'.
#   2026-08-28  BUILD pr -- RULE 44'S THIRD PHANTOM: A FRAGMENT OF AN UNSPOKEN WHOLE.
#               The night watch's order-of-operations turn drew "4 + 5 x 2", asked
#               "5 x 2 = ?", and never said the problem. Rule 44's referee was silent
#               for TWO measured reasons: the whole line carries no "?" so it was never
#               a candidate, AND _pq_spoken_covers passes on one spoken number. Two
#               repairs CUT by canon sweep: strict coverage newly condemns 169 authored
#               cards (58 -> 227), and even gated behind an announcement it hits 29,
#               because it counts "÷ 2" as a quantity where a teacher says "halved".
#               What shipped is narrower -- a pending question that is a FRAGMENT of a
#               larger board expression whose extra numbers were never spoken. Zero
#               hits in 2,109 cards. Inside rule 44's existing seat: still 58 referees.
#   2026-08-28  BUILD pq -- RULE 42'S TWO OPEN DOORS. The night watch caught three
#               comparison-to-others lines in one run. MEASURED, not assumed: two were
#               detector misses ("a lot of PEOPLE", bare "EVERYONE") and the third
#               ("lots of kids") FIRED and shipped anyway -- a pass_through, not a
#               hole. _CMP_SHAPES gains "a lot of" + the people-nouns. The canon sweep
#               CUT "most people" (probstat says it legitimately) and the entire
#               everyone/everybody family (17 canon hits; no regex spares real
#               teaching). See ruletests PART 3fu.
#   2026-08-27  BUILD oq -- THE RAISED HAND. NEW script_question() +
#               _SCRIPT_QUESTION_SYSTEM: one bounded spoken answer to a child's
#               mid-script question (60 words, no board tags -- stripped if any
#               slip -- the pending problem's answer explicitly fenced, ends by
#               handing the lesson back). Rides _reply_pipeline like every model
#               turn, mode="script", fails open to "" so the caller's authored
#               hold line takes over.
#   2026-08-27  BUILD on -- THREE REFEREES CORRECTED BY THE PHASE-1 CANON AUDIT
#               (holding 1,989 authored cards to the live standard exposed
#               referee defects no live traffic ever had): (1) student_compare's
#               probstat percentile exemption skipped only the FIRST mention and
#               convicted the second -- it now loops; (2) skipped_result
#               demanded a literal "x = 225" from a board that honestly wrote
#               "x = 15² = 225" -- chained equalities now count; (3) angle_piece
#               convicted "pieces of the rim" and "an answer in pieces, not in
#               degrees" -- narrowed to a piece WITH a degree measure. All three
#               reduce false fires on live replies too.
#   2026-08-26  BUILD ol -- THE SIXTH FLAG HARVEST (six probstat flags, 23:23-
#               23:32). (1) finite_answer: _EITHER_OR_RE allows one trailing noun
#               ("categorical or quantitative DATA?"); _OFFER_FORK_RE learns "or
#               want another"; NEW _CLAUSE_FORK_RE (", or is it harder...?"); and
#               the quiz exemption is NARROWED per Jim's ruling -- a named-binary
#               quiz question ships its buttons (the words already gave the whole
#               answer space), while forks/ready-checks stay quiz-exempt and open
#               quiz questions keep free answers. (2) NEW opener_grade_conflict
#               (the FIFTY-THIRD): an opener never grades -- server-gated via
#               meta["opener"] (main.py sets it on __open__ turns); greeting
#               first exempts recap praise. (3) NEW spoken_time_collision_
#               conflict (the FIFTY-FOURTH): "Question 3: 20 students" is a
#               clock time in the ear; ratios written 3:20 untouched. All
#               patterns canon-swept 0 (including the quiz flip: 0 canon cards
#               affected). The tiny-bar-chart flag is math-figures.js (400 ->
#               720 display cap) and the sign-in fast-forward also gets a
#               dangling-answer note in main.py's opener branch.
#   2026-08-26  BUILD ok -- GRADE WHAT THEY SAID, EARN WHAT YOU SCORE. Jim's live
#               probstat catch: student tapped "Spring" (right!) and the reply
#               opened "Pie chart -- correct! That's question 1 done" -- wrong
#               answer graded, quiz declared mid-stream, question 1 credited
#               though never asked. (1) tapped_answer_conflict's iy digit gate
#               was the hole: word answers (Spring, Pie chart -- the buttons
#               39(e) ships everywhere) were exempt with the request taps. A
#               wordy tap now counts as an answer whenever the reply GRADES
#               (_TA_GRADING_RE, narrow verbs); request taps stay exempt because
#               their replies do the thing instead of grading it. (2) NEW
#               quiz_credit_conflict (the FIFTY-SECOND referee): "question N
#               done" is rejected unless the conversation actually asked a
#               question N (heard-gated). Rule 18(c) and new 47(k) are the
#               prompt-side twins.
#   2026-08-27  BUILD ow -- THE FIFTY-FIFTH REFEREE: he says "step one, step two"
#               and the board shows one unlabelled column. Jim, live in geometry
#               with os ALREADY DEPLOYED (/health said 2026-08-27ot): "it's not
#               putting side by side problems as we progress, and it's not saying
#               step one, step two, step three." The [[stepcard]] tag existed and
#               went unused -- a rule the model ignored once earns a referee.
#               spoken_steps_conflict fires only when the tutor's own words name
#               two or more numbered stages with no [[stepcard]] anywhere: a
#               prose-versus-board mismatch, not a style opinion. A SECOND, LOOSER
#               ARM ("first ... then ... then") was designed, swept against the
#               canon, and CUT -- eleven hits, all false ("first ones, then tens,
#               then hundreds"). The narrow arm swept clean at zero.
#   2026-08-27  BUILD os -- THE BOARD READS ONE, TWO, THREE (one word here). The
#               new [[stepcard]] board tag (board.js + rule 58e: labeled Step-N
#               cards side by side) joins _LEAK_SHAPES' tag-name list -- ahead of
#               "step" in the alternation, so "a stepcard tag" spoken to a child
#               is caught whole. No referee added, no behavior changed.
#   2026-08-26  BUILD oj -- SIDE BY SIDE ON PURPOSE (one word here). The new
#               [[beside]] board tag (board.js + rule 58d) joins _LEAK_SHAPES'
#               tag-name list so "I'll send a beside tag" spoken to a child is
#               caught like its siblings. No referee added, no behavior changed.
#   2026-08-26  BUILD oi -- THE FIFTH FLAG HARVEST (five geometry flags, 22:45-22:52).
#               (1) finite_answer_conflict learns the LEADING fork: "Want X, or Y?"
#               (_LEAD_FORK_RE) -- nu's shape needed the offer verb after the "or";
#               two flags carried it up front. (2) NEW paper_drawing_conflict (the
#               FIFTIETH referee): "grab your paper and draw two lines crossing"
#               outsources the board's own job; fires only when NO figure exists in
#               the reply or the conversation (heard-gated, nv's law). (3) NEW
#               vertical_angles_conflict (the FIFTY-FIRST): a vertical-angles
#               question asked with no crossing lines anywhere -- pairs with
#               geo-figures.js's new [[angle cross="?"]] X. All three patterns
#               canon-swept 0 before enforcement. The congruent-in-a-recap and
#               long-turn flags are prompt work (prompts.py rule 37/19c) -- no
#               referee change.
#   2026-08-21  BUILD jy -- the intervention prompt learns CARRYING, with jr's canon
#               words baked in: two-digit adds are modeled as step lines (ones, the
#               carry when the ones go over nine, tens, answer), and the rule is
#               "over nine" -- NEVER "ten or more", the exact two-costume defect Jim
#               caught live on 2026-08-20. Still under the 2,500-char pin.
#   2026-08-21  BUILD jw -- the intervention prompt learns TAKING AWAY: the course
#               grew to four lessons (lessonscripts.py) and two of them subtract, so
#               _SCRIPT_INTERVENE_SYSTEM now covers both ops with the canon words for
#               each ("take away", "are left", "minus") and script_intervention's note
#               states the problem with its real sign. Still under the 2,500-char pin.
#   2026-08-21  BUILD jt -- script_intervention(): the scripted lesson's one doorway
#               to the model. A ~1,600-char system prompt (vs ~183,000 for the lesson
#               lane) because an intervention already knows the problem, the child's
#               answer, the level and the canon words; Model-Lead-Test on that ONE
#               problem; at most 60 spoken words; ends with the engine-supplied
#               choices tag so CODE grades the redo. Rides _reply_pipeline unchanged,
#               so mathcheck and all 37 referees still check the reply. Returns "" on
#               any failure -- the server falls back to the scripted retest, because
#               the model must never brick a scripted lesson.
#   2026-08-20  BUILD jr -- CONSISTENCY MEMORY. From Jim's live Basic Math lesson: the
#               tutor said "since that's OVER NINE, carry" and, four turns later in the
#               SAME lesson, "since that's TEN OR MORE, carry" -- identical to us, two
#               rules to a seven-year-old. NEW detect_phrasings / remember_phrasings /
#               phrasing_note. What is pinned is the PHRASE THAT NAMES THE RULE, never
#               the sentence: "write the three" vs "write the zero" is correct variation
#               (different columns), "over nine" vs "ten or more" is not. Delivered
#               PRE-HOC on turn_note -- never the system prompt, so the 71k cached
#               prefix is untouched -- because today's measurement says a turn is 16s,
#               30% of turns already retry, and a 38th referee would buy a wording fix
#               with another whole model call. A contradicting phrasing fires a PROBE,
#               not a rejection, so "did pre-hoc hold?" is answered by evidence.
#   2026-08-20  BUILD jq -- WHAT THE TURN WRITES. NEW _measure_output(): the accepted
#               reply's whole size, the part the child HEARS (tags stripped) and how
#               many board tags it carries, all recorded on the turn's usage row. From
#               jm/jp's decomposition -- 12.3s of a 16s turn is the teaching model
#               generating ~875 tokens at a normal ~71/second, so the wait is LENGTH,
#               and rule 19c's cap governs only the spoken part. Measured on the
#               ACCEPTED draft (a discarded one is counted by ms_retry; letting it in
#               would describe a reply no child ever saw) and in CHARACTERS (the API's
#               token count spans all attempts and cannot be split). A reply past
#               OUTSIZE_CHARS (env, default 3000) also fires ONE probe naming its five
#               biggest tags -- every turn would be ~9,000 telemetry rows a week, and
#               the outliers are where the seconds are.
#   2026-08-20  BUILD jp -- THE SECOND OPINION IS TIMED. LIVE_CRITIC is seated with
#               claude-opus-5 in production, so an entire extra model reads every draft
#               the regex referees accept, before the child sees anything. jm's ms_model
#               wrapped only the teaching call, so those seconds were being reported as
#               "referees and our own work" -- overhead, rather than what they are.
#               _live_critic_review now takes the turn's `tokens` dict and charges its
#               own wall time to ms_critic in a finally block (so a crashed or
#               empty-seat call is still counted honestly), and _turn_ms returns a
#               fourth number. Nothing about the critic's BEHAVIOUR changed.
#   2026-08-20  BUILD jo -- THE SECOND PHANTOM IS DEAD. Measured from the first real
#               /admin reading (206 retries on 692 turns = 29.8%): rule 44's referee
#               fired on 4.3% of turns and caused most of the replies that shipped WITH
#               an unresolved finding, because _pq_spoken_covers could only hear numbers
#               0-20 and the round tens. "three hundred", "twenty five" and "one hundred
#               forty four" were invisible, and a decimal only counted when read
#               digit-wise -- so "ten percent of eighty" over a board of "0.10 x 80"
#               failed every single time. The tutor read the problem aloud exactly as
#               rule 48 demands and the referee could not hear it: unresolvable by
#               construction, iz's phantom in a second costume. NEW _spoken_numbers()
#               parses compound number words (runs break at any non-number token, so
#               "three plus one" can never become 31; "and" continues a run only after a
#               scale word); the decimal branch gains ONE narrow door for a percent
#               reading that still requires the word "percent". The fraction branch is
#               untouched. Builds gk and gw are re-pinned in PART 3cr and still reject
#               exactly what they were written to reject.
#   2026-08-20  BUILD jm -- THE TURN CLOCK. A refereed turn now records how long it
#               took: ms_total (wall clock for the whole of _create_verified), ms_model
#               (cumulative time inside model calls, all attempts and all continuation
#               hops) and ms_retry (everything after the first draft was rejected).
#               NEW: _timed_create_full (a wrapper, so _create_full is untouched) and
#               _turn_ms. No new plumbing -- the clock rides the `tokens` dict that
#               already carries the token counts to store.log_usage. ms_total minus
#               ms_model is referees plus our own work; ms_retry gives Lever 1 of the
#               2026-08-20 responsiveness proposal a NUMBER instead of an argument.
#               Every read is wrapped and every failure yields 0: a clock that throws
#               must never cost a lesson, and store drops a 0 rather than averaging it
#               in as an instant turn. The assessment call (get_assessment) is
#               deliberately NOT clocked -- it is not a teaching turn and shares none of
#               this path; its rows carry 0 and are excluded from every average.
#   2026-08-20  BUILD jl -- RULE 61 GOES LIVE: the THIRTY-SEVENTH referee,
#               overgeneralized_precedence_conflict. The night watch's only confirmed
#               finding of 2026-08-20 was the tutor telling a prealgebra student
#               "Multiplying and dividing always happen before adding and subtracting"
#               -- false, and stage one of the rule being taught. Rule 61(c) already
#               carried that exact NOT/BUT pair, so the tutor was TOLD and said it in a
#               new costume: the gap was enforcement, not words. Three conditions, all
#               required (spoken prose only; a universality marker in the same sentence;
#               no grouping symbol anywhere in the reply), so a legitimate "here we
#               multiply before we add" is untouched and the fix the nudge dictates is
#               always reachable -- the property build iz's phantom lacked. PART 3w
#               gains the live pins and the new costume joins its authored-content ban
#               list. Rule 61 stops being prompt-covered for live replies.
#   2026-08-19  BUILD jh -- REFEREE 36, THE COLUMN PLACE. Jim resuming a session on
#               24368 + 8175: the board carried "43" under the line (ones and tens
#               done, HUNDREDS next) and the tutor announced "ten-thousands: 2 + 1 =
#               ?", skipping two columns. The board knows where the work stands; the
#               tutor's memory of it does not -- and partial= makes that objective, so
#               it is refereeable. Companion prompt rule: a half-finished problem is
#               RESTARTED on resume, never resumed mid-column.
#   2026-08-19  BUILD jg -- REFEREE 35, THE ORPHAN STEP. Jim, solving 3(x-2)=2x+5:
#               "it actually put a bubble between those, and the original equation was
#               out of sight up high... it feels like it doesn't understand what is on
#               the screen." THE PROMPT CAUSED IT -- five places said "because the
#               board STACKS, you never re-state the whole solution", which was true
#               when the worklist was one permanent visible column and became FALSE
#               once turns scroll (and build ir anchors each new bubble at the top,
#               pushing earlier lines off-screen entirely). orphan_step_conflict
#               rejects a reply that draws an operation with no line in that SAME reply
#               to operate on. The five prompt sites now teach the opposite: write the
#               line you are acting on, then the op, then the result, together.
#   2026-08-19  BUILD jd -- REFEREE 34, THE SPOKEN-LENGTH CEILING. Jim's [voiceclip]
#               probe measured a live turn at 126 spoken words = FORTY-SIX SECONDS of
#               unbroken speech at a child ("Mr. Cadabra is very slow today"), on a
#               welcome-back opener that taught nothing new. That is build ja's bill:
#               ja lifted the 1-3 sentence cap so a new idea could be taught properly,
#               Jim ruled "long, but IN BEATS", and the rule bounded nothing -- so the
#               permission leaked into every turn. spoken_length_conflict rejects a
#               reply whose SPOKEN prose (tags excluded -- a turn is never punished for
#               what it draws) runs past _SPOKEN_WORD_CEILING=110, and tells it to land
#               one beat, board it, and end on a continue-check. A word count is
#               objective, which is what makes this refereeable where rule 19's shape
#               is not; the ceiling sits ABOVE the ~80-word teaching guidance so a
#               generous demonstration never trips it.
#   2026-08-19  BUILD iz -- THE PHANTOM FOUND, AND THE CRITIC HELD TO JSON.
#               (1) iy's line-naming exposed why the "absolute-value unresolved"
#               nudge could never be satisfied: the referee was reading the PIPE
#               SEPARATORS of [[choices]]/[[card]] option lists ("3/4 | 2/4 |
#               4/8") as absolute-value bars -- a phantom notation no retry could
#               explain. Real bars hug their contents; the pattern now demands a
#               non-space just inside both bars (|x|, |−5|, |x - 3| still fire).
#               This also un-skews the model comparison: arms that used MORE
#               answer buttons (good pedagogy) were being punished hardest.
#               (2) The Anthropic live critic returned non-JSON verdicts 4x in
#               one audited arm (each a silently wasted check) -- it is now held
#               to JSON by assistant prefill of the opening brace, with the
#               plain-shape fallback on the known intermittent refusal.
#   2026-08-19  BUILD iy -- TWO CATCHES FROM THE ARM-1 RERUN. (1) Referee 33
#               demanded the tutor "say 'Quiz me!' back and tell them whether it
#               is right" -- a REQUEST button is not a graded answer; the referee
#               now enforces only QUANTITATIVE taps (the option contains a
#               digit). (2) The rule-14 absolute-value nudge went unresolved
#               3-for-3 even WITH the quoted ready sentence -- so the nudge now
#               NAMES THE LINE THAT DOES IT (the exact board value), which both
#               points the model at the accused line and finally shows us, in
#               the server log, what keeps writing bars nobody reads aloud.
#   2026-08-19  BUILD iw -- THE TAPPED FRACTION IS SPOKEN (caught LIVE by Jim's
#               very first Opus audit run, same night referee 33 shipped): the
#               audit student answered "3/4", the reply said "three fourths"
#               back, and tapped_answer_conflict objected three times -- a FALSE
#               fire that burned two retries on a correct reply and handicapped
#               that arm's score. _ta_option_pattern now gives a pure-fraction
#               option its spoken forms: "three fourths", "three quarters",
#               "three over four", and the literal. (The gk lesson a third time:
#               a fraction's spoken form is its ordinal, not its digits.)
#               Companion in lessonaudit.py: the lineup line and the report
#               FILENAME carry the resolved models (CLAUDE_MODEL=claude-opus-5
#               is an arm, and it overwrote the sonnet arm's report).
#   2026-08-19  BUILDS iu/iv -- THE BRAIN IS PLUGGABLE + THE LIVE CRITIC SEAT
#               (Jim's A/B ruling; challenger model his explicit call: gpt-5.6).
#               iu: TUTOR_PROVIDER=anthropic (default, byte-identical)|openai picks
#               the author; _OpenAIBrain adapts OpenAI's chat API to the exact
#               client.messages.create(...) call _create_full already makes --
#               same .content/.stop_reason/.usage shape, token-parameter and
#               room-to-think negotiation inherited from lessonaudit's transport,
#               prefill refused with the NAMED words _create_full's negotiation
#               already listens for (so continuations fall back to the nudge on
#               their own). Pipeline, referees, retries: untouched, vendor-blind.
#               iv: LIVE_CRITIC=off (default)|anthropic|openai seats a SECOND
#               model that reads every draft the regex referees accept -- the
#               judgment moles (the "Eleven is the answer" thread-jump class)
#               caught without a new build per mole. A confident objection is a
#               retry through the same loop (_CRITIC_NUDGE); pass-unless-confident,
#               fail open everywhere, usage logged kind="critic". Off = production
#               behavior byte-identical. Pinned in ruletests PART 3cf.
#   2026-08-19  BUILDS is/it -- REFEREE 33 + THE NUDGE THAT FINALLY SAYS HOW. is:
#               tapped_answer_conflict (rule 18a's runtime half, from Jim live in
#               Entry Level Math: he TAPPED "32" answering "which is bigger,
#               thirty-two or twenty-nine?" and the reply graded the lesson's
#               OTHER thread -- "Eleven is the answer -- you jumped one step past
#               ten!" -- engaging neither 32 nor 29). When the student's message
#               is EXACTLY one of the previous turn's [[choices]] options and the
#               reply touches neither their answer nor any option of that
#               question (digits or words -- "thirty-two" counts for 32), the
#               reply is regenerated. Narrow: typed/spoken answers and "I'm not
#               sure" are exempt; emoji-only options never judged; fail open.
#               it: the rule-14 notation nudge goes PRESCRIPTIVE -- five straight
#               unresolved retries (four lessonaudit runs + Jim's Render log,
#               absolute-value bars every time) proved a described defect stays
#               unfixed. Each _NOTATIONS entry now carries the ready sentence,
#               and the referee message QUOTES it, so a retry only has to
#               include it. Pinned in ruletests PART 3ce.
#   2026-08-25  BUILD np -- THE FIRST PRODUCTION WEEK'S THREE ROOT FIXES, from
#               Jim's telemetry panel (560 turns, 274 fires, 37 pass-throughs).
#               ① pendcheck (13%% of turns, the #1 firer) was firing on rule
#               39(d)'s REQUIRED comprehension check-ins whenever they mentioned
#               numbers ("does that 'zero over zero' make sense... or should I
#               slow down?") -- an unsatisfiable nudge, the iz phantom signature.
#               _PQ_CHECKIN exempts the check-in shapes. ② spokenlen's nudge said
#               "keep every word" while demanding fewer -- unsatisfiable by
#               construction; it now prescribes the first beat only, ~60 words,
#               cut by stopping earlier. ③ _CRITIC_NUDGE puts the fix in a place:
#               THE FIRST SENTENCE grades the ungraded answer / honors the skipped
#               request -- the commonest of the 11 unresolved critic objections.
#   2026-08-25  BUILD nn -- REFEREE 42: A SMALL ANSWER SPACE SHIPS ITS BUTTONS
#               (rule 39e). The either-or / yes-or-no question shapes must carry
#               [[choices]]; quiz moments exempt; rule 39(d)'s required check-in
#               wording deliberately unmatched (whole-clause alternatives). Canon
#               swept to zero before shipping. PART 3dx.
#   2026-08-25  BUILD nl -- REFEREE 41: AN ANGLE IS CALLED AN ANGLE. From Jim's
#               live "one piece measuring 130 degrees". Course-gated to geometry/
#               precalc (fractions live on pieces; a pie chart's piece may fairly
#               be 90 degrees). Root cause was the geometry TEMPLATE modelling the
#               word -- fixed in prompts.py the same build. PART 3dv.
#   2026-08-25  BUILD nk -- REFEREE 40: NO LAYOUT WORDS FOR THE BOARD. From Jim's
#               live "points up there" (they were below). Noun+phrase shape only;
#               the math senses of below/down-there and the numerator's "up top"
#               stay untouched. PART 3du, both directions + canonical sweep.
#   2026-08-25  BUILD nj -- REFEREES 38 AND 39, THE ONES THAT GOT AWAY. ①
#               function_ask_rewrite_conflict (rule 16's function-notation shape):
#               "what would f(4) be?" must find f(4) or f(x)= on THIS reply's board;
#               a worked f(3) is neither. ② func_rule_spoken_conflict (rule 44's
#               definition shape): a NEW rule written and questioned must be READ --
#               name and numbers, prose or in-tag, heard-gated. Both swept to zero
#               on the canon; the sweep caught algebra1/domain as a real authored
#               gap (fixed in foundations.py). ⚠️ TOOLING SCAR, KEPT ON PURPOSE:
#               the first cut of these regexes reached this file with LITERAL
#               BACKSPACE BYTES where \b belonged -- an escaping layer ate them,
#               the file PARSED fine, and only failing directional cases caught it.
#               PART 3dt now greps this file for \x08. Never trust a pattern you
#               have not watched match.
#   2026-08-25  BUILD ni -- THE NIGHT WATCH'S DETERMINISTIC HALF. Two changes here:
#               ① _NOTATIONS grows ÷, the TIGHT multiplication dot, and subscripts --
#               "8 ÷ 2 = ?" reached a beginner unread, and the three-forms card
#               handed an Algebra II student r₁, r₂ and · with no reading. The dot
#               demands no surrounding space (a spaced dot is a separator -- the iz
#               pipe phantom's second verse, caught in THIS build's sweep before it
#               shipped). ② _note_tag_vals replaces the old one-value regex, which
#               captured only the FIRST quoted attribute per tag -- the caught card
#               showed this referee nothing but its TITLE. Titles, items, captions:
#               drawn means read. Both directions + separator phantoms pinned in
#               PART 3ds; mathcheck.py gained the board-equation checker the same
#               night (see its notes).
#   2026-08-18  BUILDS ih/ii/ij -- REFEREES 30-32, THE TIER-B REMAINDER. ih:
#               notation_intro_conflict (rule 14's runtime half) -- a reply whose
#               BOARD tags carry a symbol new to this conversation (√, π, ^, |x|,
#               f(x)) while the prose never reads it aloud is rejected; stored
#               history keeps tags, so `heard` genuinely knows which symbols the
#               student has met. ii: repeat_question_conflict (rule 22) -- a
#               question of six words or more re-asked WORD FOR WORD from the
#               previous tutor turn is rejected; _create_verified now also extracts
#               prev_tutor from the ORIGINAL messages. ij: back_reference_conflict
#               (rule 62's caught shape) -- "the <X> we did a minute ago/earlier"
#               when <X> appears nowhere in the conversation; generic tokens and
#               real work exempt. Rule 19 (worked-example-first) deliberately
#               DEFERRED -- the audit judged it too fuzzy for an honest pattern.
#               PARTs 3by/3bz/3ca.
#   2026-08-18  BUILD ig -- THE TWENTY-NINTH REFEREE: THE QUIZ VOCABULARY GATE
#               (rule 37's quiz-facing half; the promotion audit's Tier-B
#               flagship). ia generalized from three hardcoded words to the whole
#               course glossary: quiz_vocab_conflict rejects a NUMBERED quiz
#               question offering a choice between foundations glossary terms the
#               student was never DELIVERED (terms_known -- the store's
#               [[learned]]-tracked scripts via main._foundations_heard, durable
#               across sessions and history caps) nor HEARD (conversation) nor
#               taught in this reply. Built conservatively with ZERO [termgap]
#               calibration data (Jim checked: the log has none yet): choice shape
#               only, numbered questions only, silent unless BOTH facts supplied;
#               the what-is-the-<term> shape is deferred on purpose. get_tutor_reply
#               meta gains "terms_known"; the sweep signature gains
#               terms_known/course. PART 3bx.
#   2026-08-18  BUILDS id/ie/if -- THE PROMOTION BATCH: REFEREES 25-28, from the
#               promotion audit's Tier A (Jim: "we're still in whack-a-mole mode";
#               the audit showed every recent miss came from the thirty rules held
#               by prompt words alone). id: student_compare_conflict (rule 42 --
#               "most kids find this hard" and every other measurement against a
#               room the student cannot see) + spotlight_count_conflict (rule 60c
#               -- a second line/board spotlight; tour page-stops exempt). ie:
#               substitution_rewrite_conflict (rule 16, both 2026-08-07 live
#               catches -- a plug-in/check ask with no REAL equation written, where
#               a bare "x = 4" is not one and the tags' quoted VALUES are judged,
#               never the attribute syntax's own '='). if: instruction_leak_conflict
#               (rule 4 -- "my instructions", "rule 47 says", "step tag", "I'm not
#               allowed"; the math forms "you're not allowed to divide by zero" and
#               "the rule for adding fractions" stay untouched). All reply-only,
#               fail open, both directions + canonical sweep in PARTs 3bu-3bw.
#   2026-08-18  BUILDS ia + ib -- THE TWENTY-THIRD AND TWENTY-FOURTH REFEREES, both
#               from ONE live quiz run of Jim's. ia: quiz_term_conflict (rule 47e) --
#               a question offering the acute/right/obtuse choice when the
#               conversation never taught those words is rejected. First referee fed
#               the conversation itself: _create_verified now computes `heard` (the
#               ORIGINAL messages' text, never the retry msgs -- a rejected draft
#               plus its nudge must not teach the checker its own vocabulary) and
#               prose_board_conflict passes it down; silent when the caller cannot
#               know. The reply's own prose outside the question counts as heard, so
#               teach-then-quiz in one reply stays legal. ib:
#               question_self_contained_conflict (rule 47g) -- a NUMBERED quiz
#               question ("Question 5:") that states "the vertex ... at Y" and then
#               asks "what is the vertex" is rejected; outside a numbered quiz the
#               shape stays legal (rule 47's say-it-back move). PARTs 3br/3bs.
#   2026-08-18  BUILD hz -- THE TWENTY-SECOND REFEREE: THE PROMISED COMPARISON.
#               Jim's live catch (geometry, angle sizes): "Here's our angle again,
#               fifty degrees, next to a right angle for comparison" -- and the board
#               showed ONLY the fifty. The promised-picture referee stayed quiet
#               because a figure WAS drawn; the content referees only know triangles.
#               NEW angle_compare_conflict(reply): fires when the prose places the
#               angle next to / beside / alongside a right angle (or says "right
#               angle ... for comparison") and no [[angle]] tag in the reply carries
#               deg="90". A bare comparison QUESTION ("compared to ninety, is fifty
#               bigger?") never fires -- asking needs no second picture; claiming one
#               is on the board does. The fix it teaches: draw the piece INSIDE the
#               right angle ([[angle deg="90" split="50"]]) or drop the claim. Rule
#               63(e) carries the words (prompts.py); fail open; both directions +
#               canonical sweep in PART 3bq.
#   2026-08-18  BUILD ht -- THE UPSTREAM CALL IS BOUNDED (Phase 5, review Class F).
#               Every Anthropic client is now constructed with
#               timeout=ANTHROPIC_TIMEOUT_S (env, default 60s) and max_retries=1 --
#               the SDK default was ~600s with 2 retries, so a hung upstream could
#               freeze a child for ten minutes while the page said "thinking". A
#               slow-but-working reply still lands; a hung one becomes the friendly
#               try-again message; the pages' own 90s fetch abort (same build) is
#               the outer guarantee.
#   2026-08-18  BUILD hr -- THE TWENTY-FIRST REFEREE: THE STORY-UNITS CHECK. The
#               night watch's first confirmed catch on the live Phase-4 build
#               (08:44 UTC report): 4 + 3 × 2 modeled as "4 dollars, plus 3 bags of
#               2 candies each" -- dollars added to candies, the numbers as
#               decoration. NEW story_units_conflict(reply): fires when one sentence
#               adds a money amount to grouped NON-money objects with no price
#               resolution ("...that cost 1 dollar each" stays a fine shopping
#               story; "and" merely lists facts and never fires). The rule-27
#               precedent: narrow enforcement of the caught shape, while rule 32's
#               new one-unit clause (prompts.py) covers the class in words.
#   2026-08-18  BUILD ho -- THE TWENTIETH REFEREE: THE RECORD-CLAIM CHECK (the
#               count-claim probe's promotion; Phase 4, Class D). The audit's most
#               corrosive shape -- a child refused a demonstration on the invented
#               evidence "you've now watched this move twice" -- is now vetoed like
#               arithmetic. NEW record_claim_conflict(reply, record): SCORE claims
#               must name a score the record holds (exempt when the reply carries
#               its own [[quiz]]/[[check]]/[[finalexam]] tag -- rule 45's referee
#               owns in-reply results); "you've mastered Unit N" / "Unit N is in
#               progress" are checked against the record's mastered/touched sets
#               (future conditionals exempt); WATCH-COUNT claims are refused
#               outright -- no record stores per-event counts, so the number can
#               never be a memory (rule 65d's principle, enforced). Armed via
#               meta["record"] (main._claim_record, lesson lane); silent where the
#               caller cannot know; fail open, canonical-swept, tested in both
#               directions on the audit's own transcript shapes.
#   2026-08-18  BUILD hm -- THE NINETEENTH REFEREE: THE UNITPLAN CHECK (Phase 4 of the
#               full-app review begins -- Class D, the model's word becoming truth).
#               A hallucinated [[unitplan unit="N"]] used to sail through the sweep,
#               get filed into topic_progress by main.py, and come back as the rail's
#               truth on the next resume (the likeliest phantom-Unit-5 mechanism).
#               New unitplan_conflict(reply, allowed_units): the server computes which
#               units the RECORD can justify (main._unit_allowed_set -- resolved,
#               focus, touched, mastered, next-in-progression, or asked-for-by-the-
#               student THIS turn) and a declaration outside that set is regenerated,
#               exactly as [[verify]]/SymPy vetoes arithmetic. Wired via
#               meta["allowed_units"] (lesson lane only; silent where the caller
#               cannot know). The pattern for reading the tag's unit now lives in
#               tags.UNITPLAN_UNIT_PATTERN -- one grammar source, two consumers.
#   2026-08-17  BUILD hj -- THE UNIT ARRIVES AS A FIELD. build_system_prompt and
#               _lesson_unit (the fourteenth referee) now read
#               student["current_unit"] -- the value main._resolve_unit derived ONCE
#               -- before any older path. The regex-the-prose fallback
#               (_unit_from_progress) survives only for callers that predate the
#               field (nightwatch drives get_tutor_reply directly with synthetic
#               students); when the field is present, no prose is parsed at all.
#               Referee and prompt still cannot disagree -- same field, one owner.
#   2026-08-17  BUILD hh -- THE TAG GRAMMAR HAS ONE SOURCE (tags.py; the last Phase 2
#               build). FIGURE_TAGS, _BOARD_TAGS and _PQ_BOARD_TAGS now DERIVE from
#               the registry; the rule-18b sweep's inline step|write|solve regex
#               became _STEP_TAG_RE, compiled once from tags.STEP_TAGS; and
#               _FIGURE_TAGS -- which turned out to be a LITERAL RE-DECLARATION of
#               FIGURE_TAGS, the same 22 members re-typed by hand in a different
#               order in the same file -- is now simply FIGURE_TAGS. The tags import
#               is deliberately NOT defensive: tags.py is pure data, and "the
#               referees silently forgot what a tag is" must stop a deploy at boot,
#               not degrade in the dark. ruletests PART 3ay guards the derivations.
#   2026-08-17  BUILD hg -- ONE REPLY PIPELINE (Phase 2's backend half). The three
#               reply getters were hand-copied variants of one sequence -- key check,
#               model, history trim, client, _create_verified, fallback, post-nets,
#               graceful catch-all -- and the copies had already cost real coverage
#               twice: practice/topic ran for weeks with the fourteenth referee
#               silently disarmed (re-armed in hb), and only lessons ran the TODAY
#               net. NEW _reply_pipeline() is the single sequence; the getters are
#               thin CONFIGURATIONS naming exactly what differs per lane: the prompt
#               builder (passed as a CALLABLE so a prompt crash still degrades to the
#               friendly message inside the try, never a 500 at a child), the
#               referee's unit, the log tag, the telemetry name, the turn-note
#               (lesson only, build cm) and the post-net (TODAY bar, lesson only).
#               Every future referee/net/probe now lands in every lane by
#               construction. Verified: the no-key path returns the identical message
#               on all three lanes; one _create_verified call site; no getter builds
#               its own client; ruletests PART 3ax guards all of it (mutation-tested:
#               an eagerly-built prompt escaping the try is caught).
#   2026-08-17  BUILD hb -- THE FOURTEENTH REFEREE IS RE-ARMED ON PRACTICE AND TOPIC.
#               The full-app review found unit_claim_conflict silently DISARMED in both
#               side-trip modes since build gn: they passed no "unit" in meta, and the
#               referee stays mute without one -- so "welcome back to Unit 7" was caught
#               in a lesson and unguarded on two thirds of the teaching surface.
#               WHICH unit it is armed with matters more than the arming. NOT the
#               student's placed unit: a practice problem is a side trip and may come
#               from any unit, so that would fire on correct teaching and regenerate
#               good replies. It is the unit of the PROBLEM (or topic) -- exactly what
#               build_practice_prompt / build_topic_prompt already use to pick the
#               playbook, so the referee and the prompt cannot disagree (the gn
#               property). Unclassifiable text yields None and the referee stays silent.
#               WITH IT, _UNIT_CLAIM_RE WIDENED FOR CONTRACTIONS: "you're in the middle
#               of Unit 7" walked past the pattern while "you are ..." was caught -- an
#               apostrophe was the entire difference. Now we're/you're/you've/been.
#               Verified both directions (6 must-fire, 6 must-stay-silent) and swept
#               over all 1,014 canonical foundation strings x 9 units: 0 false alarms.
#               ruletests PART 3av.
#   2026-08-17  BUILD ha -- EYES (Phase 1 of the full-app review). The review's
#               meta-finding: this file applied fail-open ~19 times with print-only
#               reporting, so a crashed referee and a healthy one emitted identical
#               signals -- store.record_error was unreachable from the teaching path
#               because get_tutor_reply converts every exception to a friendly string.
#               A referee here once corrupted authored foundation scripts for FOUR
#               BUILDS unreported (gl -> gw). Now: a tiny _event() helper writes one
#               row to store.system_events (never raises, no-ops when the store is
#               off) and EVERYTHING counts itself -- every referee FIRE (all 19 paths
#               in prose_board_conflict, by name), every referee CRASH (all 19 fail-open
#               handlers + mathcheck's), every PASS-THROUGH (a reply shipped with a
#               known finding, mathcheck or prosecheck), every probe observation
#               (countclaim, markcheck), both [promptsize] alarms, and the three
#               teaching-path catch-alls (failopen). A dead check is now a visible
#               zero on /admin instead of a silence.
#   2026-08-17  BUILD gz -- THE PROMPT CEILING IS ENFORCED WHERE THE PROMPT IS BUILT.
#               Full-app review, Phase 0. The 180,000-char ceiling lived only in a
#               ruletests measurement taken with a FRESH student; a returning student who
#               had heard every foundation script assembled to 186,890-194,284 chars ON
#               EVERY COURSE (measured in a clean container against this exact code) and
#               nothing at runtime noticed. Second shipping of this miss class (gf's
#               185,595 was the first). Now: PROMPT_CEILING is defined HERE (ruletests
#               imports it -- one definition, per the review's "facts without owners"
#               class); build_system_prompt checks every assembly; an over-ceiling prompt
#               is reassembled with heard-script wording DEFERRED -- the cl mechanism cn
#               kept dormant for exactly this day ("it becomes the right answer if the
#               library ever grows to where it does not fit"). Refresher turns carry the
#               words regardless (foundations_force_verbatim, set by main.py from
#               foundations.wants_refresher) so rule 40's promise -- the exact script is
#               restored the moment they ask -- stays true. Under-ceiling students get a
#               byte-identical prompt to before: the cache stays warm, nothing changes.
#               Every remaining overflow prints [promptsize] OVER CEILING, loudly.
#   2026-08-17  BUILD gy -- A RULE SPOKEN AS A LAW: rule 54 widened, rule 61's fraction
#               case born enforced (the EIGHTEENTH referee). The last of the six causes
#               from the day's audit triage.
#               RULE 54: "'of' means multiply" (the percents lesson). The banned list was
#               story-cue words only, and "of" belongs there by that list's own logic --
#               "sum" and "difference" NAME their operations and rule 37 requires teaching
#               them, while "of" merely CORRELATES inside one problem type. A child taught
#               it as a rule applies it to "3 out of 4". Added with it: the rest of the
#               classic bad mnemonic ("is means equals, of means times"), plus per and each.
#               RULE 61: "the bottom number never changes, we just add the top numbers" (the
#               fractions lesson). Rule 61 is generally UNENFORCEABLE -- "always" and "never"
#               are frequently true, including in rule 64's own "a length is never negative".
#               What makes this case decidable is that THE SAME LESSON SAYS IT CORRECTLY
#               THREE TIMES ("since the denominators match", "same-bottom-number fractions",
#               "since the slices are the same size"). The tutor knows the condition and
#               drops it, so the check is only: is the condition in the sentence? 0 false
#               alarms across 1,015 canonical scripts, which is the test that matters --
#               the fraction library states this rule many times over.
#   2026-08-17  BUILD gx -- THE REFUSED-DEMONSTRATION REFEREE (rule 65), the SEVENTEENTH,
#               and the worst thing the day's audit found. Twice in one geometry lesson a
#               child asked to be SHOWN and was turned down:
#                 "Can you show me taking the square root of 169?"
#                   -> "You've now watched this move twice -- let's flip it." (new triangle)
#                 "Can you show me 8 squared and 15 squared first?"
#                   -> "You've watched this exact move twice now... let's see you try it."
#               Both counts were FALSE; the move had been shown once. So the refusal rested
#               on invented evidence, and the child was told they should already know it --
#               which they cannot correct, because they cannot see the transcript.
#               A student saying "show me" is handing over the exact information a tutor
#               spends a lesson trying to get: they are not ready alone. Withdrawing the
#               scaffold is right when their WORK says so, never as the answer to this.
#               THE DISCRIMINATOR CAME OUT OF THE LESSON ITSELF, which is why it can be
#               trusted: earlier in the same transcript the same student asked the same kind
#               of question and was answered properly -- and every compliant reply carries a
#               COMPLETED board line ("5^2 = 25"), while the refusals carry only pending
#               ones. All three conditions required: asked to be shown, nothing worked out,
#               work handed back. 0 false alarms on 1,015 scripts x 6 phrasings -- after the
#               sweep caught two over-broad conditions in an early draft (a card TITLE
#               ending in "?", and the VARIABLE x read as a multiplication sign).
#   2026-08-17  BUILD gw -- THE BARE ANSWER-DEMAND, THE DECIMAL, AND A REFEREE THAT HAD
#               BEEN FIGHTING US. Three fixes from one thread of the day's audit.
#               (1) The decimal-alignment lesson raised a rule 15 and a rule 44 finding
#               that turned out to be ONE defect: board [[step eq="2.6 + 1.35"]] with no
#               "?", prose "...add column by column. What do you get?". Rule 15's referee
#               needs the numbers to be IN the asking sentence; rule 44's referee only
#               inspects board values containing "?". THE MISSING "?" HID THE PROBLEM FROM
#               BOTH AT ONCE. A bare demand for an answer now counts as an ask when the
#               board is holding a real computation for it to be about.
#               (2) Underneath it, gk's fraction bug wearing a decimal point: the
#               digit-scatter fallback found the "1" of 1.35 inside the word "one" in
#               "let's try ONE with a similar setup" and called the problem spoken. A
#               decimal now counts as read only when its whole part is said beside "point"
#               -- or "dollars", because "three dollars and ninety seven cents" IS reading
#               3.97 aloud.
#               (3) ⭐ NOT FROM THE AUDIT AT ALL -- the canonical sweep found it. gl's
#               self-correction referee read "hold on" as the tutor changing its mind, and
#               TWO foundation scripts say "so hold on to this" / "the one to hold on to".
#               It has been REGENERATING AUTHORED CONTENT. A referee that fights the
#               foundation library is worse than no referee: it burns a model call and can
#               cost the student the good draft (dg). "hold on TO something" is a teaching
#               instruction, not a wobble.
#   2026-08-17  BUILD gv -- THE INVENTED HISTORY: one referee widened, one probe added.
#               The day's audit found SEVEN claims about what had already happened that
#               were untrue, and they split on whether a referee can CHECK them.
#               ENFORCED: "you completed the square start to finish on your own", said to a
#               student who answered two sub-steps of a procedure the tutor wrote every
#               line of. gm's gates all let it through correctly by their own terms -- the
#               student DID show working -- because gm asks "did they show A method?" and
#               this sentence begs "did they do THE WHOLE THING?". narrated_method_conflict
#               gains a TOTALITY branch that runs first: a totality phrase plus a NAMED
#               procedure over a fragment. Warmth about a problem they did answer ("you
#               solved it all by yourself", to an eight-year-old) is deliberately untouched.
#               MEASURED: "you've now watched this move twice" (said twice, both false),
#               "all three conversions under your belt", "your last score was 85%", "Unit 9
#               is also still in progress". Every one is a claim about the whole
#               conversation or about a record this function has never seen, so
#               count_claim_probe LOGS and changes nothing. ⚠️ The false count is the ENGINE
#               of the worst behaviour in the audit: a student asked "can you show me
#               taking the square root of 169?" and was refused with "you've now watched
#               this move twice". A child asking to be shown, turned down on invented
#               evidence. Enforcement waits for the probe's data -- two diagnoses this week
#               were guesses, and this one will not be a third.
#   2026-08-17  BUILD gu -- THE COLD-QUIZ REFEREE (rule 47(d)), the SIXTEENTH, and it is
#               six days late. Two lines, side by side:
#                 2026-08-11 audit:  "let's do it -- five questions, all on finding the
#                                     percent of a number"
#                 2026-08-17 audit:  "Let's do it - five questions, all on finding the
#                                     percent of a number."
#               WORD FOR WORD. Rule 47(d) was written FROM the first one; it fixes the
#               instrument at TEN questions and forbids a smaller one wearing the Unit
#               Quiz's name into a child's record. The tutor said it again unchanged
#               because rule 47 was COVERED and nothing watched it. gm's lesson, twice
#               over: a rule written from a real incident that fails again is a wish.
#               Enforceable precisely BECAUSE 47(d) already fixed the number and already
#               sanctioned the smaller instrument on one condition -- that the tutor says
#               which one it is. So the check is the rule: a quiz is starting, the stated
#               count is not ten, and the reply never names the instrument. 11 cases both
#               directions; 0 false alarms on 1,015 canonical scripts. Note the negative
#               lookahead in _CQ_NAMED -- 47(d)'s remedy REQUIRES mentioning the unit quiz
#               ("the Unit 7 quiz also covers..."), so a bare mention test would have
#               rejected the very sentence the rule asks for.
#   2026-08-17  BUILD gt -- BOARD NOTATION LEARNS THREE MORE SHAPES, and the way they were
#               found is the point. Five lesson-audit runs (ten lessons, 27 findings) turned
#               up three malformed board lines that board_notation_conflict ALREADY EXISTED
#               to catch and walked straight past:
#                 [[step eq="1 + 2 = 3 -> 3/4"]]        an arrow AFTER the equals sign, so
#                                                       the line asserts 3 -> 3/4 and a child
#                                                       can read "three equals three fourths"
#                 [[step eq="12: which digit is the ones? = ?"]]   a QUESTION inside an
#                                                       equation tag -- not maths at all
#                 [[step eq="(x+4)^2 = (x+4)^2"]]       a TAUTOLOGY where the factoring
#                                                       belonged; it records no step
#               None of the three needs judgement, which is what makes the miss instructive:
#               the audit's real product was not the bad turns, it was THE SHAPE OF OUR OWN
#               BLINDNESS. Scoped to eq= deliberately -- a [[write text]] may carry an arrow
#               ("f(x) <- say it out loud") and a [[step check]] may repeat a value ("6 = 6,
#               so the limit is 6"); only an eq= claims to BE an equation.
#               Verified against 76 real board lines from those same five transcripts: it
#               fires on exactly the three the auditor flagged and is silent on the other
#               73. 0 false alarms across 1,015 canonical scripts.
#   2026-08-17  BUILD gr -- THE SIGNED-ANSWER REFEREE (rule 64), the FIFTEENTH. Jim
#               answered "minus five" to "what times itself gives twenty five?" and the
#               tutor said "That is correct", then taught on using 5. Two failures: the
#               affirmation was untrue (a length is never negative) and the reply used a
#               number the student never gave. mathcheck cannot see it -- every number in
#               that reply is arithmetically sound. answer_sign_conflict needs all three:
#               an explicitly signed student answer, an affirmation, and the unsigned
#               magnitude used WITHOUT the sign ever being mentioned. 14 cases both ways;
#               0 false alarms on 1,015 canonical scripts x 7 signed utterances. Two bugs
#               in its own patterns were found by running the real exchange rather than
#               trusting them: a lookahead that rejected "5." at a sentence end, and a bare
#               "exactly"/"correct" that matched ordinary prose ("exactly one output").
#   2026-08-16  BUILD gn -- THE UNIT-CLAIM REFEREE (rule 0's recap clause), the FOURTEENTH,
#               and the first that judges a reply against a fact from OUTSIDE it. Jim read
#               his rail saying Unit 1 under an opener saying Unit 5 and asked which was
#               broken. The RAIL was right: Maya's record says "New to this course... start
#               at the beginning", nothing was mastered, and the next quiz was a Unit 1
#               topic -- "Two days ago we started Unit 5: Right Triangles" was invented,
#               two-day shared past and all. A child cannot correct a grown-up's memory;
#               told they spent a lesson on the Pythagorean theorem, they conclude they
#               forgot it. _lesson_unit() derives the unit from exactly the two inputs
#               build_system_prompt uses, so prompt and referee cannot drift, and the
#               referee stands SILENT when neither input says. 9 cases both directions,
#               0 false alarms on 1,015 canonical strings.
#   2026-08-16  BUILD gn -- THE TRIANGLE-LETTER REFEREE (rule 63(d), born ENFORCED), the
#               THIRTEENTH. Jim, from one live Geometry lesson: "a, b, and c are supposed
#               to be legs of a right triangle, and instead they're shown as the angles. So
#               when you say a squared plus b squared equals c squared, it makes no sense."
#               v= letters the CORNERS and sides= letters the SIDES, so a tag reading
#               v="A,B,C" sides="3,?,4" leaves nothing on the picture called a, b or c --
#               and with the right angle at A the convention makes side a the HYPOTENUSE,
#               the exact opposite of what the board said. Sibling of triangle_side_conflict
#               (fe): same tag, same AB/BC/CA contract, wired immediately after it. Proved
#               in both directions on 8 cases, silent on all 1,015 canonical foundation
#               strings and on every existing 63c case.
#   2026-08-16  BUILD gm -- NEVER CREDIT A METHOD THE STUDENT DID NOT SHOW (twelfth referee).
#               Rule 43 already said this, in these words, written from a live catch on
#               2026-08-13 -- and on 2026-08-16 the audits caught it again: the student typed
#               "1 1/2. Next." and the tutor replied "that regrouping is exactly the move
#               that trips people up, and you nailed it clean." A rule written from a real
#               incident that fails again the same month is a wish, not a rule; this is the
#               enforcement. Narrow: it fires only when the student showed NO working AND the
#               reply claims a NAMED procedure. Praising the answer is untouched, and a reply
#               that ASKS "how did you get that?" is never flagged.
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
```

I did no harm and this file is not truncated.
