# CHANGELOG -- prompts.py  (notes rolled out of the file's header)

Moved out of `prompts.py` on 2026-09-08 (build ui): every CHANGE NOTE dated before 2026-09-01 -- 49 entries, VERBATIM, in the order they sat in the file (newest first). The 4 notes from 2026-09-01 on stay at the top of `prompts.py` itself, and new notes keep going there. Nothing below was edited; grep this file for a build letter or a date. When the header is rolled out again, the newer block is added ABOVE this one.

```text
#   2026-08-31  BUILD rc -- THE STAR FALLS WHEN THE CHILD SLIPS (text only, as always).
#               NEW [[miss]] tag joins the hidden-tags contract in EVERY copy (10 tag
#               blocks, 9 companion paragraphs, 9 intros "Two -> Three hidden tags"):
#               the mirror of [[nice]], REQUIRED the moment a reply tells the student
#               their answer was wrong, even when the problem keeps going -- Jim's
#               ruling: a miss is ANY wrong tap, and the today-streak resets on it.
#               Never with [[nice]]; never on a FINISHED problem ([[mark correct="0"]]
#               already counts that). Code floor lives in tutor.answer_slip (build rc).
#   2026-08-30  BUILD qs -- COUNT OUT LOUD WITH ME. The model invented the line "point
#               to each one and count out loud with me" on a live Entry-Level turn, Jim
#               liked it, and the board could not honour it: [[objects]] drew every star
#               in the same instant. board.js's new count="1" lands them one at a time,
#               each with its own ✓ and number, paced to his voice. Three text changes
#               here, no code (this file is TEXT ONLY and the battery enforces it):
#                 * the elementary objects doc teaches the attribute AND its one ban;
#                 * GROUND_RULES 7's "the count is deliberately not printed" gains the
#                   single exception, with a pointer to where the ban lives;
#                 * rule 17's counting clause (rule (e)) states the ban itself -- a
#                   counted drawing under a question is the answer in another channel.
#               ⚑ Referee 66 rejects that reply, so the exception cannot leak.
#   2026-08-29  BUILD py -- RULE 39(e) NAMES THE PLAIN YES/NO. Jim, 2026-08-29: "whenever
#               there's a yes or no or a binary answer, we should have bubbles." The
#               rule's example labels now split the CHECK-IN ("Does that make sense?"
#               -> Yes | Not yet -- Jim's pick, the dignified way out) from the FACTUAL
#               yes/no ("Is 7 prime?" -> Yes | No). The referee that holds it is
#               tutor.finite_answer_conflict's new _PLAIN_YESNO_RE. One copy of 39(e).
#   2026-08-28  BUILD pt -- WHEN THE OPERATION MEETS THE SIGN, SAY THE PLAIN THING.
#               Jim flagged "the left side becomes 2X, plus negative 2 plus 3": "minus
#               2 and negative 2 are the same...but a novice may be confused by this".
#               The tutor was OBEYING the existing rule (a negative value is "negative
#               two", never "minus two") -- and reading both signs literally is correct
#               and unhelpful, because a novice hears two opposite words in a row. All
#               ELEVEN copies of HOW YOU SPEAK now say: 2x + (-2) + 3 is "two x take
#               away two, plus three". The exception is named in the same breath -- a
#               lesson TEACHING that adding a negative is subtracting says both and
#               names the equivalence, which is what pre-u3-adding-a-negative does.
#               Not a referee: "plus negative" has 4 canon hits, all in that lesson.
#   2026-08-27  BUILD ox -- THE SEVENTH FLAG HARVEST (seven live flags). NEW 47(l):
#               a new numbered question starts on a CLEAN board (Jim flagged the
#               same stale-answer board three times in one geometry quiz). NEW
#               48(d3): never point a spoken colon at a board tag ("that's:" is
#               silence in the ear). ELEMENTARY TEMPLATE: the "only skip the tag
#               when the question is genuinely open-ended" loophole is CLOSED --
#               every turn-ending question in entry/basic ships its buttons, with
#               honest distractors when the answer space is not small. Referees
#               56, 57 and 58 enforce. The elementary rule is course-local on
#               purpose: it costs the shared ceiling nothing.
#   2026-08-27  BUILD ow -- USE THE WHOLE BOARD, AND MEAN IT. Rule 58(e) gains the
#               HARD clause: if the words say "step one" and "step two", the board
#               must carry [[stepcard]]s -- refereed now (the 55th), because Jim
#               watched a live geometry lesson with the tag already deployed and
#               got none of it. 58(e) also picks up the width reminder ([[beside]],
#               58d) from the same sentence of his, and the explicit carve-out that
#               naming an ORDER is not a staged demonstration.
#   2026-08-27  BUILD ot -- THE FIGURE SHELF GROWS (Jim: "I want all the graphics
#               that math teaches to be available"). New figure docs, placed in
#               the course templates that teach with them (never the shared
#               ceiling): GEOMETRY gains [[transversal]] (parallel lines cut by
#               a transversal, ask= names the related angle), [[polygon]] and
#               [[solid]]; ELEMENTARY gains [[clock]], [[tape]] and numberline
#               hops=; PREALGEBRA gains [[venn]] (GCF/LCM live in the overlap),
#               [[tape]] and hops=; PROBSTAT gains [[venn]]. Renderers in
#               geo-figures.js / math-figures.js, registry in tags.py.
#   2026-08-27  BUILD os -- THE BOARD READS ONE, TWO, THREE. Rule 58 grows (e):
#               the NEW [[stepcard n= title=]] tag (board.js) opens a labeled
#               Step-N card; following blocks land inside it, cards fill the
#               board side by side. For staged demonstrations (2-4 cards), every
#               card drawn-in, step numbers spoken as they open. Documented ONCE
#               in the shared rules, per the oj precedent.
#   2026-08-26  BUILD ol -- THE SIXTH FLAG HARVEST (six probstat flags). 39(e)'s
#               quiz exemption gains Jim's carve-out (a quiz question that NAMES
#               its two alternatives still ships buttons); 48(d2) the voice reads
#               "Question 3: 20" as a clock time -- period after the question
#               number, spell the leading count; SESSION_OPENER_RULES rule 0
#               gains AN OPENER NEVER GRADES (the dangling stale answer from a
#               previous session is re-posed after the greeting, never graded).
#               Referees 53 (openergrade) + 54 (timecollision) enforce.
#   2026-08-26  BUILD ok -- GRADE WHAT THEY SAID, EARN WHAT YOU SCORE (Jim's live
#               probstat catch: "Spring" answered, "Pie chart -- correct! That's
#               question 1 done" replied). 18(c) grows THE FIRST WORDS AFTER
#               THEIR ANSWER NAME THEIR ANSWER; NEW 47(k) QUIZ CREDIT IS EARNED,
#               NEVER NARRATED (a quiz begins by asking question 1, not scoring
#               it). Referees 33-widened and 52 enforce.
#   2026-08-26  BUILD oj -- SIDE BY SIDE ON PURPOSE. Jim: "the whiteboard is
#               underutilized... put the other equation right next to this one."
#               Rule 58 grows (d): the NEW [[beside]] tag (board.js) puts the next
#               board block NEXT TO the previous one -- say the move, use it when
#               comparing, keep pointing by content (phones stack the columns).
#               Documented ONCE in the shared rules, not per template.
#   2026-08-26  BUILD oi -- THE FIFTH FLAG HARVEST (five geometry flags). (1) 39(e)
#               names the LEADING fork ("Want X, or Y?" is the same fork; referee
#               enforces). (2) Geometry template: [[angle]] documents cross="?"
#               (the vertical-angles X, new in geo-figures.js) and the sketch-along
#               clause is REWRITTEN -- the old wording asked for a paper sketch
#               without saying the board draws FIRST, and the tutor obeyed it
#               ("grab your paper and draw two lines crossing", flagged live).
#               Board first, paper optional, referee 50 enforces. (3) 37 grows
#               A RECAP IS A FIRST TIME TOO: every term this conversation hasn't
#               taught gets its three-word gloss even in recaps ("congruent" flag).
#   2026-08-25  BUILD nl -- AN ANGLE IS CALLED AN ANGLE. Jim's live catch: "one
#               piece measuring 130 degrees... what does the other piece have to
#               be?" in the vocabulary lesson itself. ROOT CAUSE: the geometry
#               template's own [[angle]] tag instructions said "the 60° piece...
#               labels both pieces" -- the tutor echoed its own prompt's word.
#               Template reworded (area decomposition keeps its pieces), explicit
#               vocabulary rule added (geometry-local: no shared-ceiling cost),
#               and referee 41 enforces the degree-measured shape.
#   2026-08-26  BUILD oe -- THE WEEK-OLD MEMORY AND THE CHECK-CRAM (Jim's two
#               flags from one resumed algebra1 session). 40(i): after a gap, a
#               mid-flight problem is RE-DERIVED, never resumed at its last step
#               ("we had x = 11" is the tutor's memory, not the student's);
#               main.py's gap note carries the same law dynamically. 15(a): a
#               label never shares a line with an equation (referee 49 holds the
#               check-cram shape).
#   2026-08-26  BUILD oc -- NEVER FAST-FORWARD THE BOARD. Jim's flag: student
#               answered "+3 to each side" (one step) and the next reply said
#               "We got X equals 5 -- nice work isolating it" -- 3X = 15 never
#               drawn, the divide-by-3 never drawn or asked, x = 5 on no board,
#               and the student praised for work done invisibly FOR them. 15(a)
#               gains the clause; referee 48 holds the announced-unseen-result
#               shape (heard-gated).
#   2026-08-26  BUILD nz -- THE THIRD FLAG HARVEST (a basic-course session).
#               ① 29(c) SCOPED: nu's keep-going/stop fork was being offered after
#               EVERY problem (Jim: "I have only done 1 problem and it's asking
#               me if I want to stop") -- the fork now belongs only at real
#               boundaries; mid-topic the ask is "ready for another?". An honest
#               regression from this morning's rule, owned and fixed same-day.
#               ② COUNT YOUR OWN DRAWING added to the elementary objects
#               guidance (referee 47 enforces: "four bundles" over a board that
#               drew three, then the child's correct 3 graded wrong).
#               ③ referee 45 learned the "what number did you build?" ask shape.
#   2026-08-26  BUILD nw -- THE SECOND FLAG HARVEST + THE PLACEMENT GAP. Four
#               fresh flags from a live Entry session, plus Jim's design insight:
#               "if a placement exam puts me in unit three, it feels fair to talk
#               about terms that weren't brought up yet... it might be worthwhile
#               to first spend a few minutes reviewing... so people aren't caught
#               off guard" (he hit exactly this: 'fact families' assumed known).
#               15(a) ONE EQUATION PER LINE; 40(g2) PLACEMENT VALIDATES SKILLS,
#               NOT VOCABULARY; 48(h) never hang "too" after a number (say "as
#               well"); the elementary template names techniques as tricks ("the
#               counting-on trick"), never verb-stacks ("count on to add"). The
#               placed-student note in main.py carries the first-session review
#               opener; the number line's size fix lives in math-figures.js.
#   2026-08-26  BUILD nv -- THE NIGHT WATCH'S THIRTEEN (2026-08-26 run). Six
#               tight clauses: 15(a) the pending line asks YOUR question (x+2=0
#               then x=?, never x+2=?); 17 the total ends "= ?" until they answer
#               (referee 45 holds the shape); 40(g) no record means ask, not
#               choose (referee 46); 48(g) read the whole line, "= ?" included;
#               50(h) name the whole gate (review never unlocks, a passed quiz
#               does); 63(f) say the stack as drawn (first term on top). The
#               catalogue grew slash/arrow/hug entries in tutor.py; "lots of
#               kids" joined rule 42's shapes.
#   2026-08-26  BUILD nu -- THE FIRST FLAG HARVEST (four rules from Jim's new
#               in-app flag queue, one live Pre-Algebra evening). 29(c) finishing
#               a topic is not finishing the day (referee 43 holds the sign-off
#               shape); 47(e) grows its second law -- operations and notation may
#               not debut inside a quiz (the 3-squared-in-an-order-of-operations-
#               quiz flag); 39(e) grows the two-way OFFER clause (referee 42 now
#               holds the offer-fork shape: "...or would you like a quick
#               refresher?" ships buttons); 48(f) a power is never typed as two
#               digits (the '"32" is read as "three squared"' flag; referee 44
#               holds board paren balance, its sibling defect).
#   2026-08-25  BUILD nn -- RULE 39(e): A SMALL ANSWER SPACE SHIPS ITS BUTTONS,
#               EVERY COURSE. Jim's UI review items 2+3: yes/no/confused as taps,
#               and finite-answer questions ("supplementary or complementary?") as
#               bubbles. The client has been universal since 2026-08-03 (board.js
#               showChoices + the auto "I'm not sure" button); only the two
#               youngest courses' prompts ever ASKED for choices. Quizzes exempt --
#               mastery is never a one-in-three guess. Referee 42 enforces the
#               either-or shape.
#   2026-08-25  BUILD nk -- NO LAYOUT WORDS FOR THE BOARD. Jim's live catch: "those
#               three points up there" while the points sat BELOW his words. The
#               board-usage block now bans pointing by screen direction outright;
#               the narrow noun+phrase shape is ENFORCED by referee 40.
#   2026-08-25  BUILD nj -- RULE 15 LEARNS COLUMN ARITHMETIC. "What do you get
#               adding the hundredths column?" now writes the pending computation
#               itself first (hundredths: 0 + 5 = ?) -- the decimal-alignment
#               finding's shape, held at prompt tier because a referee cannot know
#               which questions need a written computation without guessing.
#   2026-08-25  BUILD ni -- THE QUIZ-EIGHTY CLUSTER, WRITTEN INTO THE RULES. From
#               the 2026-08-25 night watch: 47(h) nothing taught between the two
#               qualifying answers; 47(i) a no-hints quiz means no teaching until it
#               ends; 47(j) never promise a quiz you already know you must refuse;
#               59(e) a bare number earns no method claim; 61(c) gains the division-
#               makes-smaller and roots-cross-the-axis catalogue entries. Anchored
#               verbatim by PART 3ds.
#   2026-08-19  BUILD io -- THE ANECDOTE DIET, BATCH 1 (the consolidation pass Jim
#               approved, backed by the prompt-size experiment: the giant prompt
#               taught WORSE, 9 findings vs 6-7). Every dated citation and
#               narrative framing ("Live catch, 2026-08-12: ...", "first full
#               audit, 2026-08-11: ...") removed from the RULE PROSE -- the stories
#               live forever in these change notes and the build records; the
#               rules keep every principle, every prescription, and every teaching
#               example verbatim. Zero dates remain in the rulebook. Deep trims on
#               49(f)/(g), 47(d)/(e)/(g), 15, 16, 17, 48, 61's framing.
#               GRAPH_TOOL_NOTE 105,253 -> 101,407 (-3,846 in every turn of every
#               course). One battery anchor updated deliberately (49f's date pin
#               now holds the prescription). Batches 2-3 (the merge clusters) are
#               queued in Rule_Consolidation_Proposal_2026-08-19.md.
#   2026-08-18  BUILD il -- THE TODAY BAR: SIZING + TRUST-THE-SERVER. The PROGRESS
#               BARS section teaches Jim's ruling: each today item is a genuine
#               10-15 minute piece of work (2-3 items = an honest half-hour, no
#               two-minute padding, plan said aloud), and the SERVER now ticks
#               items too (completed results + ~15-minute worked ticks) -- the
#               model trusts those ticks, never contradicts the bar, and marks a
#               noticed one with a single warm sentence.
#   2026-08-18  BUILDS ih/ii/ij -- RULES 14, 22 AND 62 GAIN THEIR REFEREE NOTES:
#               board notation new to the conversation is read aloud or the draft
#               dies (14, 30th referee) · a question re-asked word for word from
#               the previous turn dies (22, 31st) · "the <thing> we did a minute
#               ago" for a thing this conversation never held dies (62, 32nd).
#   2026-08-18  BUILD ig -- RULE 37 GAINS ITS REFEREE NOTE (the quiz vocabulary
#               gate): a numbered quiz question offering a choice between key terms
#               the student was never taught or heard is now rejected -- "teaching
#               may introduce a word; a quiz may not." Enforced by tutor's
#               twenty-ninth referee, fed the store's delivered-scripts fact.
#   2026-08-18  BUILDS id/ie/if (the promotion batch) -- FOUR WISHES BECOME WATCHED.
#               From the promotion audit (Jim: "we're still in whack-a-mole mode"):
#               every recent live miss came from rules held by words alone. Rule 42
#               gains (d) and rules 4/16/60(c) gain one-line "a referee now..."
#               notes: comparisons to other students (42, kind-sounding forms
#               included), instruction leaks (4), substitution asks with no written
#               equation (16), and a second spotlight (60c) are now REJECTED, not
#               requested. Referees 25-28 in tutor.py.
#   2026-08-18  BUILDS ia/ib/ic -- RULE 47 GROWS THREE QUIZ-HONESTY CLAUSES, all from
#               ONE live quiz run of Jim's (four catches in five questions): (e) THE
#               QUIZ ASKS ONLY WHAT WAS TAUGHT (question one asked acute/right/obtuse
#               untaught, and the restarted quiz asked it again -- teach the missing
#               term in its OWN turn, then quiz; enforced by tutor's twenty-third
#               referee); (f) AN ANGLE QUESTION DRAWS ITS ANGLE (angle M's complement
#               was asked with no picture -- the split right angle IS the complement
#               picture); (g) THE QUESTION MUST NOT CONTAIN ITS ANSWER ("with the
#               vertex at Y... what is the vertex?" -- enforced by the twenty-fourth
#               referee).
#   2026-08-18  BUILD hz -- RULE 63(e): A COMPARISON YOU SPEAK IS A COMPARISON YOU
#               DRAW. Jim's live catch: "here's our angle again, fifty degrees, next
#               to a right angle for comparison" over a board holding ONLY the fifty.
#               Rule 63 gains (d) (the triangle-letter contract, enforced since gn
#               but never written into the rule body) and (e) (the promised
#               comparison); the [[angle]] bullet now teaches the honest compare
#               move -- deg="90" split="50" draws the piece INSIDE the right angle.
#               Enforced for the caught shape by tutor's twenty-second referee.
#   2026-08-18  BUILD hr -- RULE 32(b): THE STORY KEEPS ONE UNIT. Written from the
#               night watch's first confirmed catch on the live Phase-4 build ("4
#               dollars, plus 3 bags of 2 candies each" as a picture of 4 + 3 × 2).
#               A story that MODELS an expression uses one kind of quantity
#               throughout; mixing kinds is licensed only when the mixing IS the
#               math (conversion, prices×quantities) and is said out loud.
#               Collision check (per the hp discipline): rules 1 (real-world
#               problems welcome) and 38 (concrete first) push toward rich stories
#               -- no conflict; a one-unit story is still concrete. Enforced for
#               the caught shape by tutor's twenty-first referee.
#   2026-08-18  BUILD hp -- THE ORDER OF AUTHORITY (Phase 4's precedence lattice).
#               The review found TWO blocks claiming supremacy -- GROUND_RULES
#               ("override anything said later") and SESSION_OPENER_RULES ("override
#               anything above") -- so every collision was resolved by whichever
#               claim the model happened to weight, and several audited "violations"
#               were actually one rule obeyed against another (23-vs-64's silent
#               trade, 65-vs-6/17/38c's refused demonstration). NEW section at the
#               end of GROUND_RULES: WHEN INSTRUCTIONS COLLIDE -- five named levels
#               (ground rules > the server's facts > session mechanics > teaching
#               rules > style), specific-beats-general within a level, and the
#               known cross-pulls stated by number (65 over fading; 64 over 23; 59
#               first; 56 over flow). SESSION_OPENER_RULES' header is re-scoped to
#               level 3 -- it outranks the course template for how a session OPENS,
#               never the Ground Rules and never the record. Reaches every lane
#               (the block rides GROUND_RULES). RULES.md regenerated; the battery
#               now fails when RULES.md is stale (it was two builds stale with
#               nothing checking it).
#   2026-08-18  BUILD hm -- THE RECORD OUTRANKS THE CONVERSATION (Phase 4, Class D).
#               Two word-level cuts matching main.py's honest opener:
#               (1) Rule 0's recap clause no longer licenses "this conversation" as a
#               source of progress facts. The old text let a previously INVENTED
#               recap, stored verbatim in history, count as memory next session (the
#               review's likeliest phantom-Unit-5 mechanism). Now: facts come from
#               the notes/server record; the conversation refreshes tone and recent
#               wording; when they disagree, the record wins.
#               (2) PROGRESS_TAGS_NOTE's unit-bar section says outright that the unit
#               a [[unitplan]] declares must be one the record supports (the notes'
#               unit, a touched/mastered unit, the next one, or the unit the student
#               just asked for) -- the server now checks this (the 19th referee), so
#               the words tell the model what the machinery enforces.
#   2026-08-17  BUILD gs -- THE UNIT BAR INSTRUCTION GETS TEETH (lesson-only, in
#               PROGRESS_TAGS_NOTE, not the shared block -- [[unitplan]] is machinery the
#               practice and topic pages cannot draw, and ruletests enforces that boundary).
#               Jim, twice: "it still says unit one when we are talking about unit five."
#               The tag must now be emitted the moment the work MOVES units, and the unit it
#               names must be the unit actually being taught -- where the teaching is IS
#               where the student is. main.py tracks that declaration instead of placement.
#   2026-08-17  BUILD gx -- NEW RULE 65 (shared block, all ten courses): WHEN A STUDENT
#               ASKS TO BE SHOWN, SHOW THEM. THE ASKING IS THE ANSWER. From the 2026-08-17
#               audit, twice in one geometry lesson. (d) is the half that matters most and
#               cannot be enforced yet: never justify the refusal with a COUNT -- both
#               counts in that lesson were false. Enforced by refused_demonstration_conflict;
#               (d) is measured by the [countclaim] probe.
#   2026-08-17  BUILD gr -- NEW RULE 64 (shared block, all ten courses): NEVER TRADE THE
#               STUDENT'S NUMBER FOR A DIFFERENT ONE, AND A LENGTH IS NEVER NEGATIVE. From
#               Jim's lesson: "minus five" -> "That is correct" -> taught on with 5. The
#               rule says what to do instead, in one sentence the tutor can actually speak:
#               name what is true of BOTH values, then let the context rule one out aloud.
#               Extends to counts, probabilities, ages, distances and prices.
#   2026-08-16  BUILD gn -- RULE 0 GAINS ITS RECAP CLAUSE. "A recap is a memory, not a
#               guess." The tutor may say it was in the middle of a unit or topic ONLY if
#               the notes or this conversation say so; with nothing to go on it welcomes
#               the student back WITHOUT naming a place. From Jim's 2026-08-16 lesson,
#               where a brand-new Geometry student was told "two days ago we started Unit
#               5: Right Triangles". Enforced by tutor.unit_claim_conflict.
#   2026-08-16  BUILD gn -- THE GEOMETRY [[triangle]] DOC LEARNS TO LETTER ITS SIDES. Jim
#               caught a figure whose words named sides a, b, c while v= put A, B, C on the
#               CORNERS and sides= held bare numbers, so the theorem pointed at nothing.
#               The doc now says: if your words name a side by letter, put the letter IN the
#               side slot (sides="c = 3, a = ?, b = 4"); a side's letter is the lowercase of
#               the vertex OPPOSITE it; and for the Pythagorean theorem put the right angle
#               at C so the hypotenuse is c. Enforced by tutor.triangle_letter_conflict.
#   2026-08-13  BUILD fe -- THE 2026-08-13 LESSON-AUDIT FINDINGS BECOME RULES (every one
#               read against its quoted transcript before this was written; ruletests
#               PART 3ah pins each anchor, PART 3w bans the new false universals):
#               - NEW rule 63: THE WORDS AND THE PICTURE ARE THE SAME FIGURE. (a) one
#                 figure, one name -- the Functions lesson called the drawn circle "a
#                 sideways-opening curve" and "that circle" in one breath; (b) a
#                 sharing story draws the SHARES -- 14 cookies for 4 friends is
#                 3|3|3|3 with 2 apart, never 4|4|4|2; (c) the triangle sides list is
#                 a contract (AB, BC, CA -- right="C" makes AB the hypotenuse slot),
#                 now machine-checked by tutor.triangle_side_conflict.
#               - rule 61(c) grows five -> nine corrected forms: the fraction
#                 "always", multiplication-first with no grouping-symbol condition,
#                 sides-don't-match-means-jump, plus-or-minus-means-two-answers.
#               - rule 17 gains ask-first-confirm-after and the no-escape-hatch
#                 clause; rule 26(a) gains A WRONG PICTURE IS A WRONG LINE; rule 41
#                 gains the question-figure caption carve-out (the caption carries
#                 the TASK, never the answer the question wants); rule 43 gains the
#                 bare-answer-shows-no-method clause; rule 14 gains abbreviations
#                 (DNE) and goals-card symbols (i); rule 13 gains the ten-percent
#                 direction and the nonnegative-root traps; rule 4 gains A SEPARATE
#                 EXAMPLE ANNOUNCES ITSELF. Geometry's [[triangle]] doc now names the
#                 hypotenuse's slot where the tag is taught.
#               Three audit findings were REJECTED, reasons recorded in ruletests
#               PART 3ah's header (rule 52d, rule 47, rule 15/[[column]]).
#   2026-08-13  BUILD ey -- THE [[bye]] TAG: THE FIRST MECHANICAL END-OF-SESSION SIGNAL.
#               PROGRESS_TAGS_NOTE gains section 3 (lesson mode only, alongside the
#               today/unit bars -- deliberately NOT the shared block, which practice and
#               topic also receive and which have no bye handler). Until now a goodbye
#               existed ONLY as prose, so the app could not tell a wrap-up turn from any
#               other turn; the alternative was sniffing his words for "see you", which
#               misfires on "see you next Tuesday we'll do fractions". The tag draws
#               NOTHING and the student never hears it -- its whole job is to mark the
#               turn rule 29(a) already requires, so the app can close the session warmly
#               (build ey plays his goodbye clip AFTER that reply's live words).
#               GUARD RAILS IN THE TEXT, because a tag that fires early would end sessions
#               that were not ending: emitted ONLY when the student has clearly said they
#               are going, never because a lesson merely feels finished or the hour is
#               late, at most once a session, and it ends nothing by itself -- "one more"
#               afterwards just carries on.
#   2026-08-13  BUILD ex -- THE SEVEN VERIFIED TEACHING DEFECTS FROM THE 2026-08-12
#               AUDITS, CLOSED IN ONE BUILD (all verified against the transcripts
#               before this was written; ruletests PART 3ab pins every one):
#               - rule 19 gains (e): A NEW MOVE INSIDE A FAMILIAR TOPIC COUNTS AS NEW.
#                 A regrouping subtraction was ASKED before one had ever been modelled;
#                 now any never-watched move (regrouping, a carry, a negative result, a
#                 fraction answer) gets the (a)-(c) demo first, even mid-topic.
#               - rule 27 gains (c): A STORY MODEL HOLDS ONE UNIT. A board model wrote
#                 "3 dollars + 8 tickets = 11"; rule 27 covered only the FINAL answer's
#                 unit. Now the model keeps one unit line to line; two quantities stay
#                 on separate lines until a real relationship (price, rate) converts,
#                 spoken out loud.
#               - rule 49 gains (g): THE DIAGNOSIS IS SPOKEN. 0.82 was corrected with
#                 a clean re-walk and "place value" was never said; now the KIND of
#                 error is named in words the student can keep (rule 42 still holds:
#                 the error, never the student).
#               - rule 50 gains (g): AT THE LOCKED DOOR, THE OFFER IS AUTOMATIC. The
#                 retake path came up only when the student asked; now the reply that
#                 delivers "locked" also names the nearest unit, its best score, and
#                 the review-then-retake plan, unprompted.
#               - rule 51 gains (f): A LIMIT NAMES ITS APPROACH, AND EACH SIDE IS ITS
#                 OWN CLAIM. Covers both calculus catches: bare "lim f(x)" with no
#                 "as x -> a" (an incomplete sentence), and the caption calling
#                 1/(x-2) infinite "on both sides" when the left side is MINUS
#                 infinity -- each side is tested before it is described.
#               - rule 52 gains (e): THE VERDICT OPENS THE REPLY. "No -- it's 11"
#                 comes FIRST when the moment to tell them has arrived, then the why;
#                 deliberately does not override rule 22's ladder (an early miss still
#                 gets "not quite" + a hint, not the answer).
#               - NEW RULE 62: YOU MAY ONLY POINT AT WORK THAT HAPPENED. "The way we
#                 did a minute ago" for factoring that never happened; now every
#                 back-reference is checked against the board and the notes -- point
#                 at real work (rule 60's spotlight), or teach it now (rule 19), or
#                 drop the reference. 62 rules total; RULES.md regenerated.
#   2026-08-13  BUILD ew -- THE FINAL NOTES STOP COUNTING TO NINE. FINAL_PREP_NOTE and
#               FINAL_EXAM_NOTE said "MASTERED ALL NINE UNITS" / "18 questions... all
#               nine units" -- true for every course today only because all ten happen
#               to have nine units, and these two notes are SHARED overlays appended for
#               any course whose (now-derived, main.py build ew) gate opens. Reworded
#               count-neutral: "every unit of this course", "two questions per unit",
#               "after the last question". The per-course "THE NINE UNITS" curriculum
#               headers are untouched on purpose -- each lives inside one course's own
#               prompt and is factual for that course; if a course's unit list ever
#               changes, its own section changes with it.
#   2026-08-12  BUILD en -- RULE 49 GAINS (f): WHEN THEY TELL YOU THEIR RULE, ANSWER
#               THAT RULE. From the 2026-08-12 audit: a student said "we do 5 plus 3
#               first, so that's 8" -- naming a left-to-right rule out loud -- and the
#               tutor replied that three times two is not three plus two, correcting a
#               misconception the student never had while their real one survived. Rule
#               49 already said to check the hypothesis (d) and not to force the nearest
#               catalogued rule (e); it never said what to do when the student HANDS you
#               the rule. Now it does: their sentence is evidence, not a guess -- say it
#               back, name when it IS true, and show the one case where it breaks.
#   2026-08-12  BUILD em -- THE FRACTION PIE IS COUNTABLE NOW. The board-tools section
#               teaches the new equal-parts form [[pie parts="4" shaded="3"]] and says
#               plainly why the proportional data= form is wrong for a fraction: it
#               draws one wedge per entry, so "four equal parts" arrived as two lumps
#               with a percentage legend that answers the question the tutor is about
#               to ask. data= stays correct for unequal categories (spinners, surveys).
#   2026-08-12  BUILD el -- NEW RULE 61 (shared block, once): A GENERALIZATION CARRIES
#               ITS CONDITION. From the 2026-08-12 lesson audits, which caught FIVE
#               instances across calculus, algebra1 and algebra2 of the same failure --
#               a helpful heuristic stated as a universal law ("0/0 means there's a
#               hidden common factor", "a letter with parentheses after it is function
#               notation", "taking a square root always gives two answers", "always
#               half the middle coefficient squared", "the discriminant tells you how
#               many solutions"). Every one is false as stated and every one is the
#               kind a student carries into a test. Rule 13 requires true sentences but
#               MATHCHECK CANNOT SEE THESE -- there is no arithmetic in "always" -- so
#               the rule carries the five real catches with their true forms, and part
#               (d) forbids the obvious overcorrection: true absolutes (a length is
#               never negative; the hypotenuse is always the longest side) must stay
#               crisp, because a tutor who hedges everything teaches nothing.
#               Same build: the algebra1 function-notation FOUNDATION SCRIPT, which was
#               the actual source of one of the five, is corrected in foundations.py.
#               Prompt budget: +~2.7k shared characters; largest prompt still under the
#               160k ceiling (measured after).
#   2026-08-12  BUILD ee -- THE FIVE TEACHING UPGRADES (shared block, once): rules 56-60.
#               The prompt-lane queue from the Four-Lens/evidence-base work, all five in
#               one build (claude/Teaching_Evidence_Base_2026-08-10.md is the source):
#               56 FIND THE ERROR (WWC g20 r1) -- a complete solution with ONE realistic,
#                  catalogued mistake, announced as a spot-the-mistake game up front (the
#                  board's first line says so), analyzed line by line ("how could you SHOW
#                  it's wrong?"), then cleared and re-solved correctly BY THE STUDENT
#                  (rules 13/26 respected: wrong work is presented as suspect, never
#                  asserted, never left standing). Includes the incomplete-solution cousin.
#               57 TEACH THE STUDENT TO CHECK THEMSELVES (WWC g16 r2; EEF r5) -- the
#                  panel's self-monitoring questions (before/during/after), one at a
#                  time, in his own words, handed over to the student across weeks.
#               58 TWO WAYS, ONE BOARD (WWC g16 r4 + g20 r3) -- a second legitimate
#                  method for the SAME problem on the SAME board (the board stacks),
#                  then the research's comparison questions; the student's choice of
#                  method is respected afterward.
#               59 RIGHT ANSWER, WRONG METHOD (MAA IPG) -- rule 49 wakes on wrong
#                  answers; this covers its blind spot. Accept the right answer first
#                  (tally untouched, rule 45), ask "how did you get that?", and if the
#                  method is broken, show the one case where it betrays them.
#               60 THE SPOTLIGHT TAG (signaling) -- [[highlight id="line"|"board"]] now
#                  glows board work on the teaching pages (same-build page change:
#                  session/practice/topic). Words say the where; the glow points at it;
#                  at most one per reply; it never replaces rule 41's caption.
#               Prompt budget: +~8.2k shared characters (largest built prompt measured
#               156,515 after); the 150k tripwire is RAISED to 160k in ruletests.py per
#               Jim's standing decision (2026-08-11: "if you need to raise it, you
#               raise it"), with its own change note there.
#   2026-08-11  BUILD dt -- NEW RULE 55 (shared block, once): A MISSED QUIZ PROBLEM
#               COMES BACK -- ONCE, FRESH, AND KINDLY. (a) the tag half: [[quiz]],
#               [[check]], and [[finalexam]] carry a missed="question => their answer
#               | ..." attribute whenever questions were missed -- the tutor is the
#               only one who knows what was asked, so the tutor reports it; the app
#               stores it (store.quiz_misses, swept to 200/student). (b) the spaced-
#               review half: mastery notes hand back RECENT MISSED PROBLEMS and the
#               tutor revisits exactly ONE, early, as a fresh similar problem --
#               never a re-test, never a scold. Evidence: retrieval practice /
#               spaced review; closes Four-Lens student item 1. Prompt budget:
#               +~1,150 shared characters (measured after: max course lesson prompt
#               ~148.3k of the 150k ceiling; Jim authorized raising it if ever
#               needed).
#   2026-08-11  BUILD dr -- THE FIRST WORDING CHANGE IN THIS FILE, and it's exactly the
#               kind the split was built for: one paragraph, zero code risk. Jim: "it's
#               okay for the youngest to have a way to talk as well." GRAPH_TOOL_NOTE's
#               how-they-answer paragraph now tells the tutor that elementary students
#               (entry/basic) can SPEAK as well as tap -- tap, talk, and type all equally
#               good -- and that young readers' transcriptions deserve EXTRA charity
#               ("free" for three, "ate" for eight). Matches the same-build page change
#               (session/practice/topic: canRecord no longer excludes IS_ELEM). Prompt
#               budget: +~190 characters, still under the 150,000 ceiling (Jim, 08-11:
#               the ceiling may be raised when needed; not needed here).
#   2026-08-11  BORN (build do -- the tutor.py split). tutor.py had grown to 539 KB,
#               and about two thirds of it was not code at all: it was the WORDS --
#               eleven course/mode system-prompt templates, the shared GROUND RULES
#               and teaching-rules block, the session/progress/final-exam overlays,
#               the per-course practice+topic scopes, and the two assessment-writer
#               voices. Every one of those moved HERE, VERBATIM -- extracted by line
#               range from tutor.py, never retyped, and the whole move was proven
#               byte-identical: 52 built prompts (every course x lesson/first-meeting/
#               practice/topic, plus final prep/exam, focus-unit, and the standalone
#               constants) hashed before and after the split -- 52 of 52 equal.
#               tutor.py keeps the ENGINE (API calls, referees, verification pipeline)
#               and imports these names, so tutor.<NAME> still works everywhere.
```

I did no harm and this file is not truncated.
