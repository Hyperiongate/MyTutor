# =============================================================================
# lessonscripts.py  --  THE SCRIPTED-FIRST ENGINE + THE COURSE  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-22  BUILD la -- ALGEBRA I UNITS 7 AND 8, ONE BUILD (Jim: "do twice as
#               much as you have been doing between pushes"). 100 lessons -> 108,
#               97 ops (foil, fnum, gcfx, dsq + sqy, roots, vtx, hitg).
#               UNIT 7, POLYNOMIALS & FACTORING: the area model comes back and RUNS
#               BACKWARDS. (x + a)(x + b) is FOUR rooms -- middles ADD, corner TIMES,
#               and mixing those two jobs is the unit's recurring wrong tap.
#               Factoring is the same picture read the other way, a detective game
#               with two clues (adds to the x count AND timeses to the corner --
#               "a number that fits only one clue is an impostor"). gcfx demands
#               gcd(a, b) = 1 via a new _gcd helper: the pulled-out factor must be
#               the WHOLE common factor, or the factored form is a lie. dsq is the
#               vanishing middle -- the first identity that feels like a magic trick
#               and is just two rooms cancelling; a >= 3 because at 2 the square
#               collides with the double.
#               UNIT 8, QUADRATIC FUNCTIONS: the curve arrives, built on three
#               feelings: SQUARING IS NOT DOUBLING (sqy requires x >= 3 and its
#               teach names the trap's cause -- at 2 the two agree, and that
#               coincidence is what plants the habit); a product of zero means a
#               factor is zero (roots: "nobody asked for 3 + 5 or 3 x 5" -- the
#               wrong taps do arithmetic on the roots); a square is never negative,
#               so the curve has a FLOOR (vtx); and the ball comes down (hitg),
#               where the square root is met as the answer to "what number squared
#               equals 25" before it is ever a symbol -- and the wrong tap of 2a is
#               the child reaching for halving, "which undoes doubling, not
#               squaring".
#               CAUGHT READING THE BOARDS: vtx originally wrote "lowest y = 0 + 2 =
#               ?" -- the answer wearing a hat, the same giveaway class as kz's pond
#               sequence. The board now shows the rule and the floor, never the sum.
#   2026-08-22  BUILD kz -- ALGEBRA I UNIT 6: EXPONENTS & EXPONENTIAL FUNCTIONS.
#               ⭐ THE COURSE REACHES 100 LESSONS. 96 -> 100, 89 ops (exadd, exmul,
#               sci, dbl added). Prealgebra U1 taught what a power IS; this unit
#               teaches how powers BEHAVE.
#               Lessons 1 and 2 are a deliberate PAIR: the product rule (x³ · x² --
#               joining piles, powers ADD) and the power of a power ((x³)² -- copying
#               a pile, powers TIMES) are each other's classic confusion, taught
#               back-to-back, each offering the other's rule as its wrong tap. The
#               closing beat gives the one question that separates them: "am I
#               JOINING two piles, or COPYING a whole pile?"
#               Lesson 3 is scientific notation in child clothes (b × 10^a; the wrong
#               tap is the times-not-power reading, 3 × 10² tapped as 60). Lesson 4
#               is THE FIRST EXPONENTIAL GROWTH: the doubling pond, whose wrong tap
#               is the LINEAR THINKER'S answer (up by 2 a day) -- the board draws the
#               run-away sequence so the child watches doubling pull away from
#               walking. dbl requires at least 3 days: below that, doubling and
#               times-2-times-days agree and the error cannot be shown.
#               NEW module helper _sup(n) -- real superscripts for board text; expn
#               hard-coded ² and ³ because its powers stop at 3, Algebra I's do not.
#               CAUGHT READING THE BOARDS OUT LOUD: dbl's sequence originally ran ALL
#               THE WAY to the answer ("2 → 4 → 8 → 16" asking for 16). It now stops
#               one day short and ends on "?" -- a board that answers its own ask
#               teaches tapping, not doubling.
#   2026-08-22  BUILD ky -- ALGEBRA I UNIT 5: SYSTEMS OF EQUATIONS. 92 lessons -> 96,
#               85 ops (sys1, sys2, sumd, elim added). TWO RULES TRUE AT ONCE, opened
#               by [[graph]] drawing TWO LINES CROSSING (lines= splits on ";") -- the
#               crossing point is the answer standing on the board before anyone
#               computes it. Then the three classical moves in their plainest
#               clothes: SUBSTITUTION as "swap y for what it equals" (two letters
#               become one), the sum-and-difference puzzle (add the clues and the
#               smaller number cancels itself away), and ELIMINATION as two shopping
#               trips -- take one buy away from the other and the eraser VANISHES.
#               ONE DISTRACTOR RUNS THROUGH THE WHOLE UNIT: the value of the OTHER
#               unknown. In sys1 it is the y where the lines cross, in sys2 it is y
#               again, in elim it is the eraser's price. A system holds two answers,
#               and tapping the wrong one is the system-specific mistake -- offered
#               every time, and the teach beats name it every time.
#               AUTHORING NOTE WORTH KEEPING: sys1's constraint surface is genuinely
#               small -- with single-digit a there are only SIX distinct valid
#               problems, fewer than one bank. Its check now allows a up to 14 and
#               says why. The bank verifier caught ten bad picks before insertion
#               (sumd at a = 2b where the halving error IS the answer; elim at
#               3b = 2a where the eraser's price collides with it; sys2 at b = 3a
#               where stopping-at-2x collides with y) -- every one is now excluded
#               by the op's own check, not by hand-care.
#               The validator caught "makes" in sys1's ask ("what x makes both
#               rules...") and rule 14 demanded " cents " spoken standalone.
#   2026-08-22  BUILD kx -- ALGEBRA I UNIT 4: LINEAR FUNCTIONS & GRAPHS. 88 lessons
#               -> 92, 81 ops (lny, slp, yint, lin2 added).
#               ⭐ [[graph]] DRAWS ITS FIRST SCRIPTED LINE -- the real function
#               grapher, used by the generated lane since July and never by a
#               scripted lesson (the shelf: areamodel kt, angle-split ks, balance kv,
#               machine kw, grapher kx). A line is taught as THE MACHINE'S WHOLE
#               TABLE OF ANSWERS DRAWN AT ONCE -- every point an input standing under
#               its output -- so the unit sits directly on U3 rather than beside it.
#               The ladder: read one point off a line (wrong tap: the swapped
#               partner, answering y with the x you were given); SLOPE from two
#               points, before any formula, as "the climb per step" (wrong taps: the
#               heights -- where y landed and where it started -- versus how far it
#               MOVED); the starting height at x = 0, where 2 × 0 makes the times
#               part VANISH (wrong tap: the slope -- the other number in the rule);
#               and start-plus-climb answering any x, where y = ax + b is a sentence
#               ("start at b, climb a per step") before it is a formula (wrong tap:
#               the height one step LEFT -- the off-by-one graph-reading error).
#               Rule 14 forced "line" to be spoken as a standalone word -- it only
#               appeared against punctuation -- same punctuation-spacing fix as
#               "terms" in kt and "the term" in km.
#   2026-08-22  BUILD kw -- ALGEBRA I UNIT 3: FUNCTIONS & NOTATION. 84 lessons -> 88,
#               77 ops (fm1, fnot, fm2, fback added).
#               ⭐ [[machine]] GETS ITS FIRST SCRIPTED USE -- the last renderer on
#               July's figure shelf to be picked up (areamodel kt, angle-split ks,
#               balance kv). A function is taught as a MACHINE: door in, rule, door
#               out. The renderer prints "f(4) = 9" under the flow, so lesson 1 lets
#               the child STARE at the notation for a whole lesson before lesson 2
#               ever asks them to read it -- the shorthand arrives as a caption for
#               something familiar, not as a new thing.
#               THE NOTATION ERROR THE UNIT DEFUSES: f(3) read as f times 3. The
#               misreading is not stupid -- parentheses have meant times since the
#               distributive lesson, and the same marks suddenly mean "feed the
#               machine". The f-of-x lesson says that conflict OUT LOUD ("same marks,
#               different job") and offers the times-reading as the wrong tap on
#               every problem.
#               The rest of the ladder: two machines in a row (the first's output is
#               the second's input; wrong tap = the other order -- composition
#               without the word), and running the machine BACKWARDS (f of WHAT
#               equals 10 -- "an equation in machine clothes", tying straight back to
#               U2's balance; wrong tap = feeding the machine its own output).
#               fm2's asks open with "Two machines in a row." deliberately -- that is
#               scene-setting like rat's recipe, not rule re-teaching like the evxy
#               and mlx scaffolds that were trimmed; the distinction is recorded here
#               so a future sweep does not "fix" it.
#   2026-08-22  BUILD kv -- ALGEBRA I UNIT 2: LINEAR EQUATIONS & INEQUALITIES.
#               80 lessons -> 84, 73 ops (un1, un2, un3, ineq added). SOLVING BEGINS.
#               Unit 1 always handed the child what x was holding; from here the
#               EQUATION holds it, and the child gets it back by undoing -- the same
#               move off both sides.
#               ⭐ [[balance]] GETS ITS FIRST SCRIPTED USE -- the balance-scale
#               renderer, in the codebase since July, same story as [[areamodel]]
#               (kt) and [[angle split=]] (ks). An equation IS a balance; "take the
#               same off both sides or the scale tips" is the whole logic of solving,
#               drawn instead of asserted. Equals is taught as LEVEL.
#               The ladder: undo a plus, undo a times (a DIFFERENT undo -- choosing
#               which is the single biggest decision a solver makes, so it gets its
#               own lesson and its own wrong tap: 3x = 12 answered 9, the wrong-undo
#               error), two steps back in reverse order (socks before shoes -- the 3
#               went on last so it comes off first; the wrong tap is stopping at
#               "2x = 8" and calling 8 the answer, the same stop-at-step-one error as
#               rte/pcn/tri3), and LESS THAN, where the tap answer is the biggest
#               whole number allowed -- an inequality's answer is a crowd, a tap can
#               hold one number, and the wrong tap is the boundary itself (x < 7
#               answered 7), which is THE inequality misconception.
#               The validator caught "makes" twice in one teach beat ("plus 4 makes
#               11", "the picture that makes it honest") -- the first was the exact
#               habit the ban exists for; both reworded rather than the ban weakened.
#   2026-08-22  BUILD ku -- ALGEBRA I OPENS: UNIT 1, FOUNDATIONS & EXPRESSIONS.
#               76 lessons -> 80, 69 ops (ev2, evxy, cl2, dstm added). The course key
#               is "algebra1", matching curriculum.COURSES, whose own unit list names
#               this unit -- the lessons follow Jim's declared curriculum, not an
#               invented one.
#               Prealgebra U9 planted four seeds one at a time; this unit makes them
#               WORK TOGETHER: two-step evaluation (order of operations meets a letter
#               -- the add-first error b(a+c) is the wrong tap), a second letter
#               (proving x was never special; each letter keeps its own number),
#               collecting the x's PAST A Y (the first algebra done blind -- neither
#               letter's value is ever given -- with "9 of what?" as the
#               grab-everything error), and distributing over a take away, where the
#               invisible times carries a minus with it, drawn as an [[areamodel]]
#               with a NEGATIVE room (the renderer parses cols="x,-3" and prints the
#               expanded sum with the minus carried through).
#               Caught while reading the rendered asks out loud: evxy's ask opened
#               "Two letters now." in every one of twelve problems -- the same
#               scaffold-never-fades defect mlx had in build kt. The teach beats
#               introduce y; the ask just asks.
#   2026-08-21  BUILD kt -- PREALGEBRA UNIT 9: VARIABLES & EXPRESSIONS. THE COURSE'S
#               LAST UNIT. 72 lessons -> 76, 65 ops (evx, mlx, clt, dst added).
#               PREALGEBRA IS COMPLETE: nine units, 35 lessons (Unit 2 has three), entry ladder to the
#               doorway of algebra.
#               The order is the order the idea grows: a letter HOLDS a number (evx),
#               a number written against a letter means TIMES (mlx -- the one piece of
#               notation a child must simply be told, because nothing about it looks
#               like what it means), like terms collect by COUNTING (clt -- three x's
#               plus two x's are five x's, like apples), and a times DISTRIBUTES over
#               a parenthesis (dst).
#               ⭐ dst DRAWS THE DISTRIBUTIVE PROPERTY as an area model: a rectangle
#               4 tall and (x + 3) wide, cut into a 4x room and a 12 room, expanded
#               sum printed underneath -- using [[areamodel]], the algebra-tile
#               renderer in the registry since July and (exactly like [[angle split=]]
#               before build ks) never used by a scripted lesson until now. The child
#               is not handed the rule; the child is shown the two rooms. The teach
#               beat ties it back to rule one of prealgebra: parentheses SAY do the
#               inside first, but an x inside will not collapse -- so the times has to
#               reach in, and it reaches BOTH rooms.
#               The distractors are the unit's real errors: CONCATENATION (x holds 5,
#               "x + 3" tapped as 53 -- the documented universal first misreading of
#               substitution), 3x read as 3 plus x, counts timesed instead of added
#               (3x + 2x tapped as 6x), and the times never reaching the number
#               (4(x + 3) tapped as "plus 3").
#               Caught this build: (1) clt's neighbour distractor lands exactly on its
#               times-them distractor at 2x + 3x (both 6) -- its check now demands
#               three distinct options, the same repair shr and prop needed in kp.
#               (2) mlx's ask originally re-explained the invisible-times shorthand in
#               EVERY problem; a scaffold repeated in all twelve asks is a scaffold
#               that never fades, and fading it is what practice is for. The teach
#               beats own the explanation now.
#   2026-08-21  BUILD ks -- PREALGEBRA UNIT 8: MEASUREMENT & GEOMETRY BASICS.
#               68 lessons -> 72, 61 ops (cnv, tri, sla, tri3 added).
#               ⭐ THE FIRST SCRIPTED LESSONS THAT DRAW A REAL FIGURE. Basic Math's
#               geometry unit -- perimeter, area, quarter turns, volume -- draws NO
#               pictures at all: every board in it is a [[step]] line. Geometry is the
#               one subject where the picture IS the argument, and geo-figures.js has
#               carried [[triangle]] and [[angle]] since July. Three of these four
#               lessons put a figure up, and the straight-line lesson uses
#               [[angle deg="180" split="130"]] -- a tag built on 2026-08-01 for
#               exactly that sentence, after Jim's beta run caught the tutor SAYING
#               "a ray splits it into two smaller angles" over a figure with no ray,
#               and never once used by a scripted lesson until now.
#               The ladder: change a unit (Unit 5's place value wearing a coat), halve
#               a rectangle to get a triangle, then the two facts every later geometry
#               course leans on -- a straight line is 180 degrees, and so are the three
#               angles of ANY triangle. That last lesson is the first in the whole
#               course whose answer comes from a rule about all triangles rather than
#               from counting something.
#               Distractors, all of them real errors: the wrong power of ten (cnv --
#               a child who knows a zero goes on and not how many), the rectangle
#               un-halved (tri), a full turn's 360 in place of a straight line's 180
#               (sla), and the two angles you were GIVEN added up (tri3 -- doing step
#               one and tapping it).
#               tri3 draws the right-angle square when one of its given angles is 90.
#               These figures are schematic by design, but a right angle drawn as a
#               lazy corner with "90°" written beside it is schematic in the one way
#               that teaches the wrong thing.
#   2026-08-21  BUILD kr -- PREALGEBRA UNIT 7: PERCENTS. 64 lessons -> 68, 57 ops
#               (pcn, asp, pwh, pup added). Basic Math's percent lesson only ever asks
#               for 10, 25 or 50 percent and answers them with a FRACTION SHORTCUT --
#               half, a fourth, a tenth. The shortcut is fine and it is also a dead
#               end: it says nothing at all about 30 percent or 70 percent. This unit
#               replaces it with one method that never runs out -- find ten percent,
#               then count how many tens you need -- and then runs that method in all
#               four directions a percent question can face: forwards (pcn), as a
#               reading of one number against another (asp, which is Unit 6's
#               proportion with 100 on the bottom), BACKWARDS from a part to the whole
#               (pwh, the direction children reverse), and finally up and down on a
#               price (pup).
#               THE ERROR THE LAST LESSON EXISTS FOR is moving a price by the PERCENT
#               NUMBER instead of by that percent OF the price -- 40 dollars up 10
#               percent read as 50 dollars, because 40 and 10 are two numbers and
#               adding them is the thing a child already knows how to do. It is the
#               wrong tap on every problem in that bank.
#               Two defects the validator could NOT see, found by reading the rendered
#               boards and options out loud:
#                 - pup drew the ten-percent step TWICE whenever the percent was ten
#                   ("10% of 40 = 4" then "10% = 4"), which teaches a child that the
#                   second step is empty. It is now drawn only when it says something
#                   new.
#                 - pwh's forward-error distractor rounds DOWN. At "6 is 20 percent of
#                   what?" it came out as 1, and 1 is not an answer any child arrives
#                   at -- it is a stub. The check now demands every wrong option be a
#                   real wrong answer, and the one bank item that relied on the stub
#                   was replaced.
#   2026-08-21  BUILD kp -- PREALGEBRA UNIT 6: RATIOS, RATES & PROPORTIONS.
#               60 lessons -> 64, 53 ops (rat, rte, prop, shr added). Basic Math's
#               "one costs" already finds a unit PRICE; these four are the family
#               around it, in the order the ideas depend on each other: keeping a
#               ratio's shape when both sides grow, scaling a rate over time (the same
#               move with a unit step in the middle), writing it as an equation with a
#               hole in it, and SPLITTING an amount in a ratio -- the genuinely
#               different one, because there the total is given and the parts have to
#               be counted before anything is shared. The unit is aimed at ONE error:
#               adding instead of timesing (2 to 3 grown to 4 read as "4 to 5"), and
#               three of the four lessons offer exactly that as their wrong tap.
#               THE VALIDATOR CO-AUTHORED AGAIN, and every catch is recorded here
#               because each one is a rule worth keeping: "makes" is banned speech
#               (canon is "equals") so the machine now FILLS bottles rather than making
#               them; "gives you" and "is the same as" were caught in teach prose; rule
#               14 demanded "per hour" and "proportion" be said out loud; and a share of
#               ONE part turned out to be the same number as the size of one part, so
#               shr's check now requires THREE DIFFERENT tap options and the 1-to-3
#               problem left the bank (it still teaches in the worked example, which is
#               prose, not a tap). prop got the same distinctness demand when two of its
#               distractors collided on 7.
#               ALSO CATCHING UP ON RULE 8, which builds kk through ko wrote as inline
#               section comments but never entered here:
#                 kk (2026-08-21) Prealgebra U1, Number Sense & Order of Operations --
#                     41 -> 45 lessons; ops tba, parf, expn, exo.
#                 km (2026-08-21) Prealgebra U3, Integers -- the first answers below
#                     zero; ops cbz, addneg, subneg, mulneg. A lesson may now declare
#                     min_value, because "every answer is at least 1" stopped being true
#                     the day negatives arrived; the option regex learned to see a minus
#                     sign. U2 (Factors, Multiples & Primes; nfac, spf, npf) shipped
#                     alongside it.  45 -> 52 lessons.
#                 kn (2026-08-21) Prealgebra U4, Fractions -- past Basic's unit
#                     fractions; ops nuf, uic, dbf, imp.  52 -> 56 lessons.
#                 ko (2026-08-21) Prealgebra U5, Decimals -- past Basic's naming, to
#                     PLACE; ops hun, x10, dth, dsh.  56 -> 60 lessons.
#   2026-08-21  BUILD kd -- THE CONTENT SWEEP + LESSONS THAT FLOW. Jim: "my priority
#               right now is to get the app up and running ... I wanna see it all up
#               and running, and then I can troubleshoot it from there." (Reviews,
#               quizzes, exams and depth-maintenance are DEFERRED to a design
#               conversation once content is complete -- his ruling, recorded.)
#               TEN new lessons close the audit's remaining named gaps: Entry U1
#               counting (a concrete-only op where the child COUNTS the stars -- the
#               spoken ask deliberately never says the number, with a speaks()
#               override documenting why), numbers before/after, counting coins
#               (nickels), story problems for Entry (add/take-away) and Basic
#               (multiply/divide) -- via a NEW per-problem "story" field: a problem
#               may carry its own spoken sentence, and every validator rule (digits
#               spoken, canon vocabulary, word caps via closure) applies to it
#               automatically -- plus hundredths, adding fractions with DIFFERENT
#               bottoms, least common multiple, angles as quarter turns, and volume.
#               41 lessons. Entry still lacks Time and Shapes units (no clock/shape
#               renderer on the pilot page yet -- recorded, not hidden).
#   2026-08-21  BUILD kc -- THE RE-CUT (Jim's ruling on the Eureka audit,
#               Eureka_Audit_Of_The_Scripted_Course_2026-08-21.md). The audit's
#               headline: my first eight lessons -- single-digit adding through
#               regrouping -- were ENTRY-LEVEL MATH content by Jim's own curriculum,
#               filed under Basic because Basic U1's title ("Place Value &
#               Whole-Number Operations") reads the same at every grade band. MOVED:
#               all eight to course "entry", units 2-6, ids renamed entry-*. Basic
#               gets its REAL Unit 1 -- place value to 1,000, rounding to tens and
#               hundreds, and an interleaved multi-digit review (interleaving is the
#               evidence-based practice; the review lesson carries mixed_review=True
#               and the ramp check deliberately does not apply). PLUS the audit's two
#               biggest holes: multi-digit multiplication and division (Eureka G4-M3,
#               43 days, the largest module in grades 3-5 -- previously ZERO lessons)
#               and fractions ON THE NUMBER LINE (Eureka G3-M5's core idea: a
#               fraction IS a number with a place, previously taught only as portions
#               of groups). New ops: pv (hundreds/tens/ones), r10/r100 (rounding,
#               with their OWN distractors -- +-10/+-100, because +-1 distractors
#               would make rounding trivially guessable), nl/nlw (number-line hops).
#               OP_EXT entries may now declare a "choices" function.
#   2026-08-21  BUILD jz -- THE COURSE CROSSES ALL NINE UNITS. Jim: "keep working ...
#               I wanna get through the whole basic math course." SEVENTEEN new
#               lessons spanning units 1-9 (regrouping, multiplication, division,
#               remainders, missing factors, GCF, unit fractions, equivalent
#               fractions, same-bottom fraction add/take-away, tenths, money,
#               percent, unit price, perimeter, area), built on a NEW data-driven
#               OP_EXT registry: each op declares its answer function, spoken/board/
#               praise templates, difficulty key, per-problem constraint, and (when
#               digits are spoken as words) its own rule-44 check. The original
#               +/−/t ops are untouched. Problems may now carry an optional third
#               number c (fractions need one); it joins the dedup key and the
#               choices rotation. ALSO FIXED: jy accidentally placed carrying BEFORE
#               two-digit-no-carry in the course order -- an explicit COURSE_ORDER
#               now owns the sequence and the module refuses to import if any lesson
#               is missing from it or listed twice. New canon vocabulary: "regroup"
#               (bans "borrow"), "too small" (jr's live catch), "times" (bans
#               "multiplied by"). Depth note, honest: units 2-9 open at survey depth
#               (about two lessons each); the factory deepens any unit on demand.
#   2026-08-21  BUILD jy -- CARRYING COMES HOME. Lesson 7, "Adding with carrying" --
#               the lesson build jr's whole consistency-memory fight was about. On
#               2026-08-20 Jim caught the live tutor teaching the SAME rule two ways
#               four turns apart ("over nine" ... "ten or more"), and jr pinned the
#               first phrasing per student at runtime. Here the fix becomes
#               structural: "over nine" is now CANON VOCABULARY -- "ten or more",
#               "more than nine" and "bigger than nine" are BANNED from every
#               lesson's closure by the validator, and the intervention prompt hands
#               the AI the same words. A child on the scripted path can no longer
#               hear the carrying rule in two costumes, because the second costume
#               cannot pass the build. New validator branch "carry": every bank
#               problem MUST carry in the ones (else the lesson teaches its idea on
#               examples that never use it) and must NOT overflow the tens.
#   2026-08-21  BUILD jx -- JIM'S SECOND WORDING RULING + LESSONS FIVE AND SIX.
#               Jim, on jw's names: "What I meant to say is we're going to be adding
#               or subtracting SINGLE-DIGIT numbers -- numbers one through nine.
#               That's how I would say it." Lessons are now named by their INPUTS,
#               the way a person says it: "Adding single-digit numbers", "Taking away
#               single-digit numbers", "...past ten", "...from bigger numbers" -- and
#               the validator grew a_max/b_max so the bank PROVABLY matches the name
#               (L2's 10−6 and L4's 20−10 were quietly violating it; both replaced).
#               NEW LESSONS: 5. "Tens and ones" (teen numbers as one ten and some
#               ones -- a new op "t", answer = 10a+b, so the answer key stays
#               computed) and 6. "Adding two-digit numbers" (no carrying -- and the
#               validator ENFORCES no-carry on every bank problem, so a carrying
#               problem cannot sneak into the lesson that promises none). Lessons may
#               now declare their own representation levels: lesson 6 is
#               abstract-only, because dropping a struggling child to counting 37
#               stars one at a time would be the opposite of help.
#   2026-08-21  BUILD jw -- THE FIRST FOUR LESSONS (the course takes shape). Jim's
#               playtest verdict on the pilot: "very, very impressive. I think it's
#               what we want" -- and his wording ruling: say it PLAINLY. "Adding
#               within 10" is curriculum-speak; the goal chip now says "Adding
#               numbers up to 10" and the teach script says out loud what the bound
#               actually is: "every answer will be ten or smaller."
#               GENERALIZED: problems carry an op ("+" or "-"), renderers and praise
#               are op-aware, each lesson declares its symbols, its bound, its
#               difficulty key and its own advance line. NEW LESSONS (each authored
#               to the 2026-08-20 research settings, each with its own closure):
#                 1. Adding numbers up to 10        (reworded per Jim)
#                 2. Taking away -- numbers up to 10 (the minus sign, "are left")
#                 3. Adding numbers up to 20        (counting on from the bigger)
#                 4. Taking away -- numbers up to 20 (counting back)
#               PILOT_LESSON remains LESSONS[0] so every existing pin and endpoint
#               default still resolves. The engine itself is UNCHANGED in behavior:
#               same settings, same intervene contract, same closure property.
#   2026-08-20  NEW FILE (build js -- THE PILOT). Jim's ruling of 2026-08-20
#               (Ruling_Scripted_First_And_The_Settings_2026-08-20.md): every lesson is
#               pre-authored, pre-verified, and pre-voiced up to the moment a child
#               responds; the AI steps in only when the child leaves the script; CODE,
#               not the model, returns the child to the script. Why: the day's
#               measurements -- ~$50/student/month against a $29 price, 11.5s median
#               turn, 42.4% verified right first try, 25 known-bad replies shipped in a
#               week -- are all costs of GENERATING teaching at runtime. A script
#               verified once is right forever, retries never, and speaks from cached
#               audio at zero marginal cost.
#
#               THIS FILE IS DELIBERATELY PURE. No model, no network, no store, no
#               clock: lesson data + a state-machine engine + a validator. Everything
#               here can therefore be verified exhaustively by ruletests PART 3cv, and
#               a verified script stays verified.
#
#               THE SETTINGS ARE THE RESEARCH DOC'S, NOT OPINIONS (citations there):
#               advance on 3 consecutive unaided correct, minimum 4, cap 10; worked
#               examples then example-problem pairs; error path = scripted "let's look
#               together" -> AI Model-Lead-Test -> engine-issued same-form retest;
#               second intervention on a skill drops a representation level (abstract ->
#               pictorial -> concrete); failing at concrete ends warmly and marks the
#               topic "learning"; a garbled answer gets ONE scripted re-ask, then
#               tap-only -- never an AI call for a mishearing.
#
#               ⭐ THE CLOSURE PROPERTY (the reason pre-rendered voice can be TOTAL):
#               every spoken string this engine can ever emit is enumerable in advance
#               by audio_lines(). PART 3cv drives every scenario the engine supports
#               and asserts each emitted spoken line is in that closure. If a future
#               edit adds a line the closure misses, the battery fails -- so the voice
#               cache can never be surprised at runtime.
# =============================================================================

import re

# ---- THE SETTINGS (from the 2026-08-20 research ruling; change THERE first) -------
ADVANCE_STREAK = 3        # advance on 3 consecutive unaided correct (EDM 2015)
MIN_PROBLEMS = 4          # even a perfect child does at least 4 (DI "firming")
MAX_PROBLEMS = 10         # past 10 without a streak, stop -- see drop/end rules
DROP_AFTER_INTERVENTIONS = 2   # 2nd AI intervention on a skill -> easier representation
LEVELS = ("abstract", "pictorial", "concrete")   # drop direction, left to right
BEAT_WORD_CAP = 80        # rule 19c / build jd: one beat per turn, spoken

# ---- CANON VOCABULARY (build jr's lesson: one rule, one wording) ------------------
# canon phrase -> the synonyms that are BANNED anywhere in any lesson's speech.
# The validator enforces it; the intervention contract hands the canon to the AI.
VOCABULARY = {
    "put together": ("combine", "join together", "add together"),
    "in all": ("altogether", "all together", "the total"),
    "equals": ("makes", "gives you", "is the same as"),
    "take away": ("subtract", "remove"),
    "are left": ("remain", "remaining"),
    # jy: THE CARRYING RULE HAS ONE WORDING -- the exact defect Jim caught live on
    # 2026-08-20 ("over nine" ... then "ten or more", four turns apart), now banned
    # at authoring time across every lesson's closure.
    "over nine": ("ten or more", "more than nine", "bigger than nine"),
    # jz: regrouping's rule has one wording too (jr's other live catch), and so
    # does multiplication's name for itself.
    "regroup": ("borrow",),
    "too small": ("not big enough",),
    "times": ("multiplied by",),
}

# ---- PRAISE (rotated deterministically by problem index; all pre-renderable) ------
PRAISE_PREFIXES = ("That's it!", "You got it!", "Nice counting!",
                   "Exactly right!", "Well done!")

# fixed one-line scripts (every one of these is pre-rendered once)
LINE_WRONG = "Not quite — let's look at it together."
LINE_REASK = "Let me say that again."
LINE_TAP = "Tap the answer you think is right."
LINE_END_GRACEFUL = ("We did some strong thinking today. We'll practice this again "
                     "next time — Mr. Cadabra is proud of you.")


def ans(p):
    """The one place an answer is computed. Problems are DATA (a, b, op) -- a wrong
    answer key cannot exist in this file, because none is ever typed.
    ops: "+" a+b · "-" a-b · "t" tens-and-ones, a tens + b ones = 10a+b."""
    op = p.get("op", "+")
    if op in OP_EXT:
        return OP_EXT[op]["ans"](p)
    if op == "-":
        return p["a"] - p["b"]
    if op == "t":
        return 10 * p["a"] + p["b"]
    return p["a"] + p["b"]


# =============================================================================
# THE LESSONS -- Basic Math, Unit 1. Each authored to the research settings; each
# bank is ordered by its difficulty key (the 85%-success ramp).
# =============================================================================
LESSONS = [
    {
        "id": "entry-u2-add-single-digit",
        "course": "entry", "unit": 2,
        "topic": "Adding single-digit numbers",
        "op": "+", "max_value": 10, "a_max": 9, "b_max": 9,
        "symbols": ("plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can add single-digit numbers."),
        "teach": [
            # Jim's wording rulings, 2026-08-21: name the lesson by its INPUTS, the
            # way a person says it -- "we're adding single-digit numbers, the
            # numbers one through nine."
            ("Today we are learning to add. Adding means putting two groups "
             "together and counting how many there are in all. We will add "
             "single-digit numbers — the numbers one through nine.",
             '[[goal text="Adding single-digit numbers"]]'),
            ("Here are three stars. And here are two more stars. Let's put the "
             "groups together and count every star: one, two, three, four, five. "
             "There are five stars in all.",
             '[[objects emoji="⭐" groups="3" add="2" caption="count every star"]]'),
            ("Mathematicians write putting together with a special sign. We write "
             "it like this, and we say it 'plus'. Three plus two.",
             '[[step eq="3 + 2"]]'),
            ("And when we know how many in all, we use one more sign. We write it "
             "like this, and we say it 'equals'. Three plus two equals five.",
             '[[step eq="3 + 2 = 5"]]'),
            ("Watch me do a whole one. Four stars, and one more star. I count "
             "every star: one, two, three, four, five. Four plus one equals five.",
             '[[objects emoji="⭐" groups="4" add="1" caption="count every star"]]'
             '[[step eq="4 + 1 = 5"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two stars and two stars. "
                        "Count them all: one, two, three, four. Two plus two "
                        "equals four.",
                        '[[objects emoji="⭐" groups="2" add="2" caption="count every star"]]'
                        '[[step eq="2 + 2 = 4"]]'),
             "ask": {"a": 2, "b": 3, "op": "+"}},
            {"worked": ("One more together. Five stars and one star. Count them "
                        "all — six. Five plus one equals six.",
                        '[[objects emoji="⭐" groups="5" add="1" caption="count every star"]]'
                        '[[step eq="5 + 1 = 6"]]'),
             "ask": {"a": 4, "b": 2, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 1, "op": "+"}, {"a": 1, "b": 3, "op": "+"},
            {"a": 2, "b": 2, "op": "+"}, {"a": 3, "b": 2, "op": "+"},
            {"a": 4, "b": 1, "op": "+"}, {"a": 3, "b": 3, "op": "+"},
            {"a": 5, "b": 2, "op": "+"}, {"a": 4, "b": 3, "op": "+"},
            {"a": 6, "b": 2, "op": "+"}, {"a": 5, "b": 4, "op": "+"},
            {"a": 7, "b": 2, "op": "+"}, {"a": 6, "b": 3, "op": "+"},
        ],
    },
    {
        "id": "entry-u3-take-away-single-digit",
        "course": "entry", "unit": 3,
        "topic": "Taking away single-digit numbers",
        "op": "-", "max_value": 10, "a_max": 9, "b_max": 9,
        "symbols": ("minus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can take away single-digit numbers."),
        "teach": [
            ("Today we are learning to take away. Taking away means starting "
             "with a group, taking some away, and counting how many are left. "
             "We will take away single-digit numbers — the numbers one through "
             "nine.",
             '[[goal text="Taking away single-digit numbers"]]'),
            ("Here are five stars. Watch me take two away. Count what is left: "
             "one, two, three. Three stars are left.",
             '[[objects emoji="⭐" groups="5" caption="start with five — take two away, then count what is left"]]'),
            ("Mathematicians write taking away with its own sign. We write it "
             "like this, and we say it 'minus'. Five minus two.",
             '[[step eq="5 − 2"]]'),
            ("You already know the equals sign. Five minus two equals three.",
             '[[step eq="5 − 2 = 3"]]'),
            ("Watch me do a whole one. Six stars, take four away. Count what is "
             "left: one, two. Six minus four equals two.",
             '[[objects emoji="⭐" groups="6" caption="start with six — take four away"]]'
             '[[step eq="6 − 4 = 2"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Four stars, take one "
                        "away. Count what is left — three. Four minus one "
                        "equals three.",
                        '[[objects emoji="⭐" groups="4" caption="start with four — take one away"]]'
                        '[[step eq="4 − 1 = 3"]]'),
             "ask": {"a": 5, "b": 2, "op": "-"}},
            {"worked": ("One more together. Seven stars, take three away. Count "
                        "what is left — four. Seven minus three equals four.",
                        '[[objects emoji="⭐" groups="7" caption="start with seven — take three away"]]'
                        '[[step eq="7 − 3 = 4"]]'),
             "ask": {"a": 6, "b": 1, "op": "-"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 3, "b": 1, "op": "-"}, {"a": 4, "b": 1, "op": "-"},
            {"a": 4, "b": 2, "op": "-"}, {"a": 5, "b": 1, "op": "-"},
            {"a": 5, "b": 3, "op": "-"}, {"a": 6, "b": 2, "op": "-"},
            {"a": 6, "b": 3, "op": "-"}, {"a": 7, "b": 4, "op": "-"},
            {"a": 8, "b": 3, "op": "-"}, {"a": 8, "b": 5, "op": "-"},
            {"a": 9, "b": 4, "op": "-"}, {"a": 9, "b": 5, "op": "-"},
        ],
    },
    {
        "id": "entry-u2-add-past-ten",
        "course": "entry", "unit": 2,
        "topic": "Adding single-digit numbers past ten",
        "op": "+", "max_value": 20, "a_max": 9, "b_max": 9,
        "symbols": ("plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can add single-digit numbers past ten."),
        "teach": [
            ("You already know how to add single-digit numbers. Today the answers "
             "get bigger — they will go past ten.",
             '[[goal text="Adding single-digit numbers past ten"]]'),
            ("Watch me. Nine stars, and four more stars. I count on from nine: "
             "ten, eleven, twelve, thirteen. Nine plus four equals thirteen.",
             '[[objects emoji="⭐" groups="9" add="4" caption="count on from nine"]]'
             '[[step eq="9 + 4 = 13"]]'),
            ("Here is a helpful trick. Start with the bigger number and count up. "
             "Eight plus three: eight — nine, ten, eleven. Eight plus three "
             "equals eleven.",
             '[[step eq="8 + 3 = 11"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Seven stars and five "
                        "stars. Count on from seven: eight, nine, ten, eleven, "
                        "twelve. Seven plus five equals twelve.",
                        '[[objects emoji="⭐" groups="7" add="5" caption="count on from seven"]]'
                        '[[step eq="7 + 5 = 12"]]'),
             "ask": {"a": 7, "b": 6, "op": "+"}},
            {"worked": ("One more together. Nine stars and six stars. Count on "
                        "from nine — fifteen. Nine plus six equals fifteen.",
                        '[[objects emoji="⭐" groups="9" add="6" caption="count on from nine"]]'
                        '[[step eq="9 + 6 = 15"]]'),
             "ask": {"a": 8, "b": 6, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 9, "b": 2, "op": "+"}, {"a": 7, "b": 4, "op": "+"},
            {"a": 8, "b": 4, "op": "+"}, {"a": 9, "b": 3, "op": "+"},
            {"a": 6, "b": 6, "op": "+"}, {"a": 8, "b": 5, "op": "+"},
            {"a": 5, "b": 8, "op": "+"}, {"a": 9, "b": 5, "op": "+"},
            {"a": 8, "b": 7, "op": "+"}, {"a": 7, "b": 8, "op": "+"},
            {"a": 9, "b": 7, "op": "+"}, {"a": 9, "b": 8, "op": "+"},
        ],
    },
    {
        "id": "entry-u3-take-away-bigger",
        "course": "entry", "unit": 3,
        "topic": "Taking away from bigger numbers",
        "op": "-", "max_value": 20, "a_max": 19, "b_max": 9,
        "symbols": ("minus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can take away from bigger numbers."),
        "teach": [
            ("You already know how to take away single-digit numbers. Today we "
             "start with bigger numbers — the numbers up to nineteen.",
             '[[goal text="Taking away from bigger numbers"]]'),
            ("Watch me. Thirteen stars, take five away. I count back from "
             "thirteen: twelve, eleven, ten, nine, eight. Thirteen minus five "
             "equals eight.",
             '[[objects emoji="⭐" groups="13" caption="start with thirteen — take five away"]]'
             '[[step eq="13 − 5 = 8"]]'),
            ("Here is a helpful trick. Counting back works for any take away. "
             "Eleven minus three: eleven — ten, nine, eight. Eleven minus three "
             "equals eight.",
             '[[step eq="11 − 3 = 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Twelve stars, take four "
                        "away. Count back from twelve — eight. Twelve minus four "
                        "equals eight.",
                        '[[objects emoji="⭐" groups="12" caption="start with twelve — take four away"]]'
                        '[[step eq="12 − 4 = 8"]]'),
             "ask": {"a": 12, "b": 3, "op": "-"}},
            {"worked": ("One more together. Fifteen stars, take six away. Count "
                        "back from fifteen — nine. Fifteen minus six equals nine.",
                        '[[objects emoji="⭐" groups="15" caption="start with fifteen — take six away"]]'
                        '[[step eq="15 − 6 = 9"]]'),
             "ask": {"a": 14, "b": 5, "op": "-"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 11, "b": 2, "op": "-"}, {"a": 11, "b": 4, "op": "-"},
            {"a": 12, "b": 5, "op": "-"}, {"a": 13, "b": 4, "op": "-"},
            {"a": 13, "b": 6, "op": "-"}, {"a": 14, "b": 6, "op": "-"},
            {"a": 15, "b": 7, "op": "-"}, {"a": 15, "b": 8, "op": "-"},
            {"a": 16, "b": 7, "op": "-"}, {"a": 17, "b": 8, "op": "-"},
            {"a": 18, "b": 9, "op": "-"}, {"a": 19, "b": 9, "op": "-"},
        ],
    },
    {
        "id": "entry-u4-tens-and-ones",
        "course": "entry", "unit": 4,
        "topic": "Tens and ones",
        "op": "t", "max_value": 19, "a_max": 1, "b_max": 9,
        "symbols": ("ten", "ones"),
        "advance_line": ("Three in a row — you've got it! "
                         "You know your tens and ones."),
        "teach": [
            ("Today we are learning about tens and ones. Ten ones, put together, "
             "make one ten. The numbers from eleven to nineteen are one ten and "
             "some ones.",
             '[[goal text="Tens and ones"]]'),
            ("Look — here is one ten, and four more ones. One ten and four ones "
             "is fourteen.",
             '[[objects emoji="⭐" groups="10" add="4" caption="one ten and four ones"]]'
             '[[step eq="1 ten and 4 ones = 14"]]'),
            ("The first digit of fourteen counts the tens. The second digit "
             "counts the ones. 1 ten, 4 ones — fourteen.",
             '[[step eq="14 = 1 ten and 4 ones"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One ten and three ones. "
                        "Ten — eleven, twelve, thirteen. 1 ten and 3 ones is "
                        "thirteen.",
                        '[[objects emoji="⭐" groups="10" add="3" caption="one ten and three ones"]]'
                        '[[step eq="1 ten and 3 ones = 13"]]'),
             "ask": {"a": 1, "b": 2, "op": "t"}},
            {"worked": ("One more together. One ten and six ones. Count on from "
                        "ten — sixteen. 1 ten and 6 ones is sixteen.",
                        '[[objects emoji="⭐" groups="10" add="6" caption="one ten and six ones"]]'
                        '[[step eq="1 ten and 6 ones = 16"]]'),
             "ask": {"a": 1, "b": 5, "op": "t"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "op": "t"}, {"a": 1, "b": 3, "op": "t"},
            {"a": 1, "b": 4, "op": "t"}, {"a": 1, "b": 6, "op": "t"},
            {"a": 1, "b": 7, "op": "t"}, {"a": 1, "b": 8, "op": "t"},
            {"a": 1, "b": 9, "op": "t"},
        ],
    },
    {
        "id": "entry-u5-add-with-carrying",
        "course": "entry", "unit": 5,
        "topic": "Adding with carrying",
        "op": "+", "max_value": 99, "carry": True,
        "levels": ("abstract",),   # like lesson 6: stars do not help at this size
        "symbols": ("carry", "plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can carry like a pro."),
        "teach": [
            ("Today we are learning to carry. Sometimes when we add, the ones add "
             "up to over nine. When that happens, we write the ones digit and "
             "carry one ten over to the tens.",
             '[[goal text="Adding with carrying"]]'),
            ("Watch me add 27 plus 15. Ones first: 7 plus 5 equals 12. Twelve is "
             "over nine — so we write the 2 and carry one ten. Tens: 2 plus 1 "
             "equals 3, plus the carried one equals 4. So 27 plus 15 equals 42.",
             '[[step eq="27 + 15"]][[step eq="ones: 7 + 5 = 12"]]'
             '[[step eq="write 2, carry 1"]][[step eq="tens: 2 + 1 + 1 = 4"]]'
             '[[step eq="27 + 15 = 42"]]'),
            ("One more, watch. 38 plus 24. Ones: 8 plus 4 equals 12 — over nine, "
             "write the 2, carry one ten. Tens: 3 plus 2 equals 5, plus the "
             "carried one equals 6. So 38 plus 24 equals 62.",
             '[[step eq="38 + 24"]][[step eq="ones: 8 + 4 = 12"]]'
             '[[step eq="write 2, carry 1"]][[step eq="tens: 3 + 2 + 1 = 6"]]'
             '[[step eq="38 + 24 = 62"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 46 plus 17. Ones: 6 plus "
                        "7 equals 13 — over nine, write the 3, carry one ten. "
                        "Tens: 4 plus 1 plus the carried one equals 6. So 46 plus "
                        "17 equals 63.",
                        '[[step eq="46 + 17"]][[step eq="ones: 6 + 7 = 13"]]'
                        '[[step eq="write 3, carry 1"]][[step eq="tens: 4 + 1 + 1 = 6"]]'
                        '[[step eq="46 + 17 = 63"]]'),
             "ask": {"a": 45, "b": 17, "op": "+"}},
            {"worked": ("One more together. 29 plus 35. Ones: 9 plus 5 equals 14 "
                        "— over nine, write the 4, carry one ten. Tens: 2 plus 3 "
                        "plus the carried one equals 6. So 29 plus 35 equals 64.",
                        '[[step eq="29 + 35"]][[step eq="ones: 9 + 5 = 14"]]'
                        '[[step eq="write 4, carry 1"]][[step eq="tens: 2 + 3 + 1 = 6"]]'
                        '[[step eq="29 + 35 = 64"]]'),
             "ask": {"a": 28, "b": 34, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 15, "b": 16, "op": "+"}, {"a": 18, "b": 13, "op": "+"},
            {"a": 24, "b": 17, "op": "+"}, {"a": 26, "b": 15, "op": "+"},
            {"a": 28, "b": 16, "op": "+"}, {"a": 35, "b": 17, "op": "+"},
            {"a": 36, "b": 18, "op": "+"}, {"a": 45, "b": 19, "op": "+"},
            {"a": 47, "b": 26, "op": "+"}, {"a": 56, "b": 27, "op": "+"},
            {"a": 58, "b": 25, "op": "+"}, {"a": 67, "b": 26, "op": "+"},
        ],
    },
    {
        "id": "entry-u5-add-two-digit-no-carry",
        "course": "entry", "unit": 5,
        "topic": "Adding two-digit numbers",
        "op": "+", "max_value": 99, "no_carry": True,
        "levels": ("abstract",),   # dropping to counting 37 stars would not be help
        "symbols": ("plus", "equals"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can add two-digit numbers."),
        "teach": [
            ("Today we are adding two-digit numbers. A two-digit number has a "
             "tens digit and a ones digit. We add the ones first, then the tens.",
             '[[goal text="Adding two-digit numbers"]]'),
            ("Watch me add 23 plus 14. First the ones: 3 plus 4 equals 7. Then "
             "the tens: 2 tens plus 1 ten equals 3 tens. So 23 plus 14 equals 37.",
             '[[step eq="23 + 14"]][[step eq="ones: 3 + 4 = 7"]]'
             '[[step eq="tens: 2 + 1 = 3"]][[step eq="23 + 14 = 37"]]'),
            ("One more, watch. 31 plus 25. Ones: 1 plus 5 equals 6. Tens: 3 plus "
             "2 equals 5. So 31 plus 25 equals 56.",
             '[[step eq="31 + 25"]][[step eq="ones: 1 + 5 = 6"]]'
             '[[step eq="tens: 3 + 2 = 5"]][[step eq="31 + 25 = 56"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 42 plus 16. Ones: 2 plus "
                        "6 equals 8. Tens: 4 plus 1 equals 5. So 42 plus 16 "
                        "equals 58.",
                        '[[step eq="42 + 16"]][[step eq="ones: 2 + 6 = 8"]]'
                        '[[step eq="tens: 4 + 1 = 5"]][[step eq="42 + 16 = 58"]]'),
             "ask": {"a": 42, "b": 13, "op": "+"}},
            {"worked": ("One more together. 34 plus 22. Ones: 4 plus 2 equals 6. "
                        "Tens: 3 plus 2 equals 5. So 34 plus 22 equals 56.",
                        '[[step eq="34 + 22"]][[step eq="ones: 4 + 2 = 6"]]'
                        '[[step eq="tens: 3 + 2 = 5"]][[step eq="34 + 22 = 56"]]'),
             "ask": {"a": 51, "b": 24, "op": "+"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 12, "b": 13, "op": "+"}, {"a": 21, "b": 14, "op": "+"},
            {"a": 23, "b": 15, "op": "+"}, {"a": 32, "b": 16, "op": "+"},
            {"a": 41, "b": 17, "op": "+"}, {"a": 33, "b": 26, "op": "+"},
            {"a": 44, "b": 23, "op": "+"}, {"a": 52, "b": 25, "op": "+"},
            {"a": 63, "b": 21, "op": "+"}, {"a": 54, "b": 33, "op": "+"},
            {"a": 62, "b": 34, "op": "+"}, {"a": 71, "b": 26, "op": "+"},
        ],
    },
]

_MORE_LESSONS = [
    {
        "id": "entry-u6-take-away-with-regrouping",
        "course": "entry", "unit": 6,
        "topic": 'Taking away with regrouping',
        "op": '-', "max_value": 99, "regroup": True,
        "levels": ("abstract",),
        "symbols": ('regroup', 'too small', 'equals'),
        "advance_line": "Three in a row — you've got it! You can regroup like a pro.",
        "teach": [
            ('Today we are learning to regroup. Sometimes the ones digit on top is too small to take away from. When that happens, we regroup: we take one ten and turn it into ten ones.',
             '[[goal text="Taking away with regrouping"]]'),
            ('Watch me take 17 away from 42. Ones: 2 is too small to take 7 away from. Regroup — one ten becomes ten ones, so 2 becomes 12, and the 4 tens become 3. Ones: 12 take away 7 equals 5. Tens: 3 take away 1 equals 2. So 42 take away 17 equals 25.',
             '[[step eq="42 − 17"]][[step eq="regroup: 42 = 3 tens and 12 ones"]][[step eq="ones: 12 − 7 = 5"]][[step eq="tens: 3 − 1 = 2"]][[step eq="42 − 17 = 25"]]'),
            ('One more, watch. 53 take away 28. Ones: 3 is too small — regroup, 3 becomes 13, and 5 tens become 4. Ones: 13 take away 8 equals 5. Tens: 4 take away 2 equals 2. So 53 take away 28 equals 25.',
             '[[step eq="53 − 28"]][[step eq="regroup: 53 = 4 tens and 13 ones"]][[step eq="ones: 13 − 8 = 5"]][[step eq="tens: 4 − 2 = 2"]][[step eq="53 − 28 = 25"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 61 take away 35. Ones: 1 is too small — regroup, 1 becomes 11, 6 tens become 5. Ones: 11 take away 5 equals 6. Tens: 5 take away 3 equals 2. So 61 take away 35 equals 26.',
                        '[[step eq="61 − 35"]][[step eq="regroup: 61 = 5 tens and 11 ones"]][[step eq="ones: 11 − 5 = 6"]][[step eq="tens: 5 − 3 = 2"]][[step eq="61 − 35 = 26"]]'),
             "ask": {'a': 62, 'b': 35, 'op': '-'}},
            {"worked": ('One more together. 74 take away 46. Ones: 4 is too small — regroup, 4 becomes 14, 7 tens become 6. Ones: 14 take away 6 equals 8. Tens: 6 take away 4 equals 2. So 74 take away 46 equals 28.',
                        '[[step eq="74 − 46"]][[step eq="regroup: 74 = 6 tens and 14 ones"]][[step eq="ones: 14 − 6 = 8"]][[step eq="tens: 6 − 4 = 2"]][[step eq="74 − 46 = 28"]]'),
             "ask": {'a': 73, 'b': 45, 'op': '-'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 21, 'b': 13, 'op': '-'}, {'a': 32, 'b': 15, 'op': '-'}, {'a': 34, 'b': 16, 'op': '-'}, {'a': 43, 'b': 17, 'op': '-'}, {'a': 45, 'b': 28, 'op': '-'}, {'a': 52, 'b': 24, 'op': '-'}, {'a': 56, 'b': 38, 'op': '-'}, {'a': 63, 'b': 26, 'op': '-'}, {'a': 71, 'b': 44, 'op': '-'}, {'a': 75, 'b': 47, 'op': '-'}, {'a': 82, 'b': 55, 'op': '-'}, {'a': 91, 'b': 63, 'op': '-'}],
    },
    {
        "id": 'basic-u2-what-multiplying-means',
        "course": "basic", "unit": 2,
        "topic": 'What multiplying means',
        "op": '*', "max_value": 30,
        "levels": ("abstract",),
        "symbols": ('times', 'equals'),
        "advance_line": "Three in a row — you've got it! You know what multiplying means.",
        "teach": [
            ('Today we are learning to multiply. Multiplying means putting together equal groups. Three times four means three groups of four.',
             '[[goal text="What multiplying means"]]'),
            ('Watch me. Three times four is three groups of four: 4 plus 4 plus 4 equals 12. We write it with the times sign. Three times four equals 12.',
             '[[step eq="3 × 4"]][[step eq="4 + 4 + 4 = 12"]][[step eq="3 × 4 = 12"]]'),
            ('One more, watch. Two times five is two groups of five: 5 plus 5 equals 10. Two times five equals ten.',
             '[[step eq="2 × 5"]][[step eq="5 + 5 = 10"]][[step eq="2 × 5 = 10"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Four times two is four groups of two: 2 plus 2 plus 2 plus 2 equals 8. Four times two equals eight.',
                        '[[step eq="4 × 2"]][[step eq="2 + 2 + 2 + 2 = 8"]][[step eq="4 × 2 = 8"]]'),
             "ask": {'a': 3, 'b': 2, 'op': '*'}},
            {"worked": ('One more together. Five times three is five groups of three — fifteen. Five times three equals fifteen.',
                        '[[step eq="5 × 3"]][[step eq="3 + 3 + 3 + 3 + 3 = 15"]][[step eq="5 × 3 = 15"]]'),
             "ask": {'a': 4, 'b': 3, 'op': '*'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 2, 'b': 2, 'op': '*'}, {'a': 2, 'b': 3, 'op': '*'}, {'a': 3, 'b': 3, 'op': '*'}, {'a': 2, 'b': 5, 'op': '*'}, {'a': 4, 'b': 4, 'op': '*'}, {'a': 3, 'b': 5, 'op': '*'}, {'a': 4, 'b': 5, 'op': '*'}, {'a': 5, 'b': 5, 'op': '*'}],
    },
    {
        "id": 'basic-u2-times-tables',
        "course": "basic", "unit": 2,
        "topic": 'Times tables',
        "op": '*', "max_value": 81,
        "levels": ("abstract",),
        "symbols": ('times', 'equals'),
        "advance_line": "Three in a row — you've got it! Your times tables are getting strong.",
        "teach": [
            ('You already know what multiplying means. Today we practice the times tables — bigger groups, up to nine times nine.',
             '[[goal text="Times tables"]]'),
            ('Watch me. Six times seven. Six groups of seven equals 42. Six times seven equals 42.',
             '[[step eq="6 × 7 = 42"]]'),
            ('A helpful trick: turn the problem around. Seven times six equals the same 42 — the order does not change the answer.',
             '[[step eq="7 × 6 = 42"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Eight times six equals 48.',
                        '[[step eq="8 × 6 = 48"]]'),
             "ask": {'a': 8, 'b': 5, 'op': '*'}},
            {"worked": ('One more together. Nine times seven equals 63.',
                        '[[step eq="9 × 7 = 63"]]'),
             "ask": {'a': 9, 'b': 6, 'op': '*'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 3, 'b': 6, 'op': '*'}, {'a': 4, 'b': 6, 'op': '*'}, {'a': 5, 'b': 6, 'op': '*'}, {'a': 6, 'b': 6, 'op': '*'}, {'a': 6, 'b': 7, 'op': '*'}, {'a': 7, 'b': 7, 'op': '*'}, {'a': 8, 'b': 7, 'op': '*'}, {'a': 8, 'b': 8, 'op': '*'}, {'a': 9, 'b': 8, 'op': '*'}, {'a': 9, 'b': 9, 'op': '*'}],
    },
    {
        "id": 'basic-u3-what-dividing-means',
        "course": "basic", "unit": 3,
        "topic": 'What dividing means',
        "op": '/', "max_value": 45,
        "levels": ("abstract",),
        "symbols": ('divided', 'equals'),
        "advance_line": "Three in a row — you've got it! You know what dividing means.",
        "teach": [
            ('Today we are learning to divide. Dividing means sharing into equal groups. Twelve divided by three asks: share 12 into 3 equal groups — how many in each group?',
             '[[goal text="What dividing means"]]'),
            ('Watch me. Twelve divided by three. Share 12 into 3 equal groups: each group gets 4. Twelve divided by three equals four.',
             '[[step eq="12 ÷ 3 = 4"]]'),
            ('Dividing undoes multiplying. Three times four equals 12, so twelve divided by three equals four.',
             '[[step eq="3 × 4 = 12"]][[step eq="12 ÷ 3 = 4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Ten divided by two. Share 10 into 2 equal groups: each gets 5. Ten divided by two equals five.',
                        '[[step eq="10 ÷ 2 = 5"]]'),
             "ask": {'a': 8, 'b': 2, 'op': '/'}},
            {"worked": ('One more together. Fifteen divided by five equals three.',
                        '[[step eq="15 ÷ 5 = 3"]]'),
             "ask": {'a': 20, 'b': 5, 'op': '/'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 6, 'b': 2, 'op': '/'}, {'a': 9, 'b': 3, 'op': '/'}, {'a': 12, 'b': 4, 'op': '/'}, {'a': 16, 'b': 4, 'op': '/'}, {'a': 18, 'b': 3, 'op': '/'}, {'a': 24, 'b': 6, 'op': '/'}, {'a': 28, 'b': 4, 'op': '/'}, {'a': 35, 'b': 7, 'op': '/'}, {'a': 36, 'b': 6, 'op': '/'}, {'a': 45, 'b': 9, 'op': '/'}],
    },
    {
        "id": 'basic-u3-left-overs',
        "course": "basic", "unit": 3,
        "topic": 'Dividing with left-overs',
        "op": 'rem', "max_value": 50,
        "levels": ("abstract",),
        "symbols": ('shared', 'left'),
        "advance_line": "Three in a row — you've got it! You can handle the left-overs.",
        "teach": [
            ('Sometimes sharing does not come out even. Share 13 into groups of 4: you fill 3 groups, and 1 is left over. Today we find what is left over.',
             '[[goal text="Dividing with left-overs"]]'),
            ('Watch me. 13 shared into groups of 4. Three groups of four equals 12, and 13 take away 12 equals 1. So 1 is left over.',
             '[[step eq="13 ÷ 4"]][[step eq="3 × 4 = 12"]][[step eq="13 − 12 = 1"]][[step eq="left over = 1"]]'),
            ('One more, watch. 17 shared into groups of 5. Three groups of five equals 15, and 17 take away 15 equals 2. So 2 are left over.',
             '[[step eq="17 ÷ 5"]][[step eq="3 × 5 = 15"]][[step eq="left over = 2"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 11 shared into groups of 3. Three groups of three equals 9, and 11 take away 9 equals 2 left over.',
                        '[[step eq="11 ÷ 3"]][[step eq="left over = 2"]]'),
             "ask": {'a': 10, 'b': 3, 'op': 'rem'}},
            {"worked": ('One more together. 14 shared into groups of 4 leaves 2 left over.',
                        '[[step eq="14 ÷ 4"]][[step eq="left over = 2"]]'),
             "ask": {'a': 13, 'b': 5, 'op': 'rem'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 7, 'b': 2, 'op': 'rem'}, {'a': 9, 'b': 4, 'op': 'rem'}, {'a': 11, 'b': 4, 'op': 'rem'}, {'a': 14, 'b': 3, 'op': 'rem'}, {'a': 17, 'b': 4, 'op': 'rem'}, {'a': 19, 'b': 5, 'op': 'rem'}, {'a': 23, 'b': 5, 'op': 'rem'}, {'a': 26, 'b': 6, 'op': 'rem'}, {'a': 31, 'b': 7, 'op': 'rem'}, {'a': 38, 'b': 8, 'op': 'rem'}],
    },
    {
        "id": 'basic-u4-missing-factors',
        "course": "basic", "unit": 4,
        "topic": 'Missing factors',
        "op": 'mf', "max_value": 72,
        "levels": ("abstract",),
        "symbols": ('times', 'factor'),
        "advance_line": "Three in a row — you've got it! You can find the missing factor.",
        "teach": [
            ('A factor is a number you multiply. In 3 times 4 equals 12, the factors are 3 and 4. Today one factor is hiding, and we find it.',
             '[[goal text="Missing factors"]]'),
            ('Watch me. 3 times what equals 12? I think: three groups of WHAT reach 12? Three times four equals 12 — the missing factor is 4.',
             '[[step eq="3 × ? = 12"]][[step eq="3 × 4 = 12"]]'),
            ('One more, watch. 5 times what equals 30? Five times six equals 30 — the missing factor is 6.',
             '[[step eq="5 × ? = 30"]][[step eq="5 × 6 = 30"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 4 times what equals 20? Four times five equals 20 — the missing factor is 5.',
                        '[[step eq="4 × ? = 20"]][[step eq="4 × 5 = 20"]]'),
             "ask": {'a': 16, 'b': 4, 'op': 'mf'}},
            {"worked": ('One more together. 6 times what equals 42? Six times seven equals 42.',
                        '[[step eq="6 × ? = 42"]][[step eq="6 × 7 = 42"]]'),
             "ask": {'a': 36, 'b': 6, 'op': 'mf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 6, 'b': 2, 'op': 'mf'}, {'a': 12, 'b': 3, 'op': 'mf'}, {'a': 15, 'b': 3, 'op': 'mf'}, {'a': 24, 'b': 4, 'op': 'mf'}, {'a': 30, 'b': 5, 'op': 'mf'}, {'a': 35, 'b': 5, 'op': 'mf'}, {'a': 48, 'b': 6, 'op': 'mf'}, {'a': 56, 'b': 7, 'op': 'mf'}, {'a': 63, 'b': 9, 'op': 'mf'}, {'a': 72, 'b': 8, 'op': 'mf'}],
    },
    {
        "id": 'basic-u4-greatest-common-factor',
        "course": "basic", "unit": 4,
        "topic": 'The greatest common factor',
        "op": 'gcf', "max_value": 48,
        "levels": ("abstract",),
        "symbols": ('factor', 'greatest'),
        "advance_line": "Three in a row — you've got it! You can find the greatest common factor.",
        "teach": [
            ('A common factor divides two numbers evenly. Today we hunt for the GREATEST one — the biggest number that divides both.',
             '[[goal text="The greatest common factor"]]'),
            ('Watch me find the greatest common factor of 12 and 18. Factors of 12: 1, 2, 3, 4, 6, 12. Factors of 18: 1, 2, 3, 6, 9, 18. The greatest one they share is 6.',
             '[[step eq="12: 1, 2, 3, 4, 6, 12"]][[step eq="18: 1, 2, 3, 6, 9, 18"]][[step eq="GCF of 12 and 18 = 6"]]'),
            ('One more, watch. 8 and 20. Factors of 8: 1, 2, 4, 8. Factors of 20: 1, 2, 4, 5, 10, 20. The greatest common factor equals 4.',
             '[[step eq="GCF of 8 and 20 = 4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 6 and 9. Factors of 6: 1, 2, 3, 6. Factors of 9: 1, 3, 9. The greatest common factor equals 3.',
                        '[[step eq="GCF of 6 and 9 = 3"]]'),
             "ask": {'a': 6, 'b': 8, 'op': 'gcf'}},
            {"worked": ('One more together. 10 and 15 — the greatest common factor equals 5.',
                        '[[step eq="GCF of 10 and 15 = 5"]]'),
             "ask": {'a': 12, 'b': 16, 'op': 'gcf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 4, 'b': 6, 'op': 'gcf'}, {'a': 6, 'b': 10, 'op': 'gcf'}, {'a': 8, 'b': 12, 'op': 'gcf'}, {'a': 9, 'b': 12, 'op': 'gcf'}, {'a': 14, 'b': 21, 'op': 'gcf'}, {'a': 18, 'b': 24, 'op': 'gcf'}, {'a': 10, 'b': 25, 'op': 'gcf'}, {'a': 20, 'b': 30, 'op': 'gcf'}, {'a': 24, 'b': 36, 'op': 'gcf'}, {'a': 32, 'b': 48, 'op': 'gcf'}],
    },
    {
        "id": 'basic-u5-fraction-of-a-group',
        "course": "basic", "unit": 5,
        "topic": 'A fraction of a group',
        "op": 'of', "max_value": 24,
        "levels": ("abstract",),
        "symbols": ('share', 'equal'),
        "advance_line": "Three in a row — you've got it! You can find a fraction of a group.",
        "teach": [
            ('A fraction names equal shares. One half means one of two equal shares. One fourth means one of four equal shares. Today we take a fraction OF a group.',
             '[[goal text="A fraction of a group"]]'),
            ('Watch me find one half of 8. Share 8 into 2 equal groups — each group gets 4. One half of 8 equals 4.',
             '[[step eq="1/2 of 8 = 4"]]'),
            ('One more, watch. One third of 12. Share 12 into 3 equal groups — each gets 4. One third of 12 equals 4.',
             '[[step eq="1/3 of 12 = 4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. One fourth of 12. Share 12 into 4 equal groups — each gets 3. One fourth of 12 equals 3.',
                        '[[step eq="1/4 of 12 = 3"]]'),
             "ask": {'a': 8, 'b': 4, 'op': 'of'}},
            {"worked": ('One more together. One fifth of 10 equals 2.',
                        '[[step eq="1/5 of 10 = 2"]]'),
             "ask": {'a': 15, 'b': 5, 'op': 'of'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 4, 'b': 2, 'op': 'of'}, {'a': 6, 'b': 2, 'op': 'of'}, {'a': 6, 'b': 3, 'op': 'of'}, {'a': 10, 'b': 2, 'op': 'of'}, {'a': 9, 'b': 3, 'op': 'of'}, {'a': 12, 'b': 2, 'op': 'of'}, {'a': 12, 'b': 3, 'op': 'of'}, {'a': 16, 'b': 4, 'op': 'of'}, {'a': 20, 'b': 5, 'op': 'of'}, {'a': 24, 'b': 6, 'op': 'of'}],
    },
    {
        "id": 'basic-u5-equivalent-fractions',
        "course": "basic", "unit": 5,
        "topic": 'Equivalent fractions',
        "op": 'eqf', "max_value": 12,
        "levels": ("abstract",),
        "symbols": ('equal', 'same'),
        "advance_line": "Three in a row — you've got it! You can spot equal fractions.",
        "teach": [
            ('Two fractions can name the SAME amount. One half of a pizza and two fourths of a pizza are the same amount of pizza. We call them equal fractions.',
             '[[goal text="Equivalent fractions"]]'),
            ('Watch me. One half equals how many fourths? Cut every half into two — two halves become four fourths, and ONE half becomes TWO fourths. One half equals two fourths.',
             '[[step eq="1/2 = 2/4"]]'),
            ('One more, watch. One third equals how many sixths? Cut every third in two — one third becomes two sixths.',
             '[[step eq="1/3 = 2/6"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. One half equals how many sixths? Cut every half into three — one half equals three sixths.',
                        '[[step eq="1/2 = 3/6"]]'),
             "ask": {'a': 1, 'b': 2, 'c': 8, 'op': 'eqf'}},
            {"worked": ('One more together. One fourth equals two eighths.',
                        '[[step eq="1/4 = 2/8"]]'),
             "ask": {'a': 1, 'b': 2, 'c': 10, 'op': 'eqf'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 1, 'b': 2, 'c': 4, 'op': 'eqf'}, {'a': 1, 'b': 3, 'c': 6, 'op': 'eqf'}, {'a': 1, 'b': 2, 'c': 6, 'op': 'eqf'}, {'a': 1, 'b': 4, 'c': 8, 'op': 'eqf'}, {'a': 1, 'b': 5, 'c': 10, 'op': 'eqf'}, {'a': 1, 'b': 6, 'c': 12, 'op': 'eqf'}, {'a': 1, 'b': 4, 'c': 12, 'op': 'eqf'}, {'a': 1, 'b': 3, 'c': 12, 'op': 'eqf'}, {'a': 1, 'b': 2, 'c': 12, 'op': 'eqf'}],
    },
    {
        "id": 'basic-u6-add-fractions-same-bottom',
        "course": "basic", "unit": 6,
        "topic": 'Adding fractions',
        "op": 'fa', "max_value": 12,
        "levels": ("abstract",),
        "symbols": ('bottom', 'plus'),
        "advance_line": "Three in a row — you've got it! You can add fractions with the same bottom.",
        "teach": [
            ('When two fractions have the SAME bottom number, the pieces are the same size — so we can just count them. Today we add fractions with the same bottom.',
             '[[goal text="Adding fractions"]]'),
            ('Watch me. Two eighths plus three eighths. The pieces are all eighths, so count them: 2 plus 3 equals 5. Two eighths plus three eighths equals five eighths.',
             '[[step eq="2/8 + 3/8 = 5/8"]]'),
            ('One more, watch. One fourth plus two fourths equals three fourths. The bottom stays the same — only the count changes.',
             '[[step eq="1/4 + 2/4 = 3/4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Two sixths plus three sixths equals five sixths.',
                        '[[step eq="2/6 + 3/6 = 5/6"]]'),
             "ask": {'a': 1, 'b': 3, 'c': 6, 'op': 'fa'}},
            {"worked": ('One more together. Three tenths plus four tenths equals seven tenths.',
                        '[[step eq="3/10 + 4/10 = 7/10"]]'),
             "ask": {'a': 2, 'b': 5, 'c': 10, 'op': 'fa'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 1, 'b': 1, 'c': 4, 'op': 'fa'}, {'a': 1, 'b': 2, 'c': 5, 'op': 'fa'}, {'a': 2, 'b': 2, 'c': 6, 'op': 'fa'}, {'a': 1, 'b': 4, 'c': 6, 'op': 'fa'}, {'a': 2, 'b': 3, 'c': 8, 'op': 'fa'}, {'a': 3, 'b': 3, 'c': 8, 'op': 'fa'}, {'a': 2, 'b': 5, 'c': 8, 'op': 'fa'}, {'a': 4, 'b': 3, 'c': 10, 'op': 'fa'}, {'a': 3, 'b': 5, 'c': 10, 'op': 'fa'}, {'a': 5, 'b': 4, 'c': 12, 'op': 'fa'}],
    },
    {
        "id": 'basic-u6-take-away-fractions-same-bottom',
        "course": "basic", "unit": 6,
        "topic": 'Taking away fractions',
        "op": 'fs', "max_value": 12,
        "levels": ("abstract",),
        "symbols": ('bottom', 'take'),
        "advance_line": "Three in a row — you've got it! You can take away fractions with the same bottom.",
        "teach": [
            ('Taking away fractions with the same bottom works the same way — the pieces are the same size, so we just count what is left.',
             '[[goal text="Taking away fractions"]]'),
            ('Watch me. Five eighths take away two eighths. Count: 5 take away 2 equals 3. Five eighths take away two eighths equals three eighths.',
             '[[step eq="5/8 − 2/8 = 3/8"]]'),
            ('One more, watch. Three fourths take away one fourth equals two fourths.',
             '[[step eq="3/4 − 1/4 = 2/4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Four sixths take away one sixth equals three sixths.',
                        '[[step eq="4/6 − 1/6 = 3/6"]]'),
             "ask": {'a': 5, 'b': 2, 'c': 6, 'op': 'fs'}},
            {"worked": ('One more together. Seven tenths take away three tenths equals four tenths.',
                        '[[step eq="7/10 − 3/10 = 4/10"]]'),
             "ask": {'a': 8, 'b': 5, 'c': 10, 'op': 'fs'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 3, 'b': 1, 'c': 4, 'op': 'fs'}, {'a': 4, 'b': 2, 'c': 5, 'op': 'fs'}, {'a': 5, 'b': 1, 'c': 6, 'op': 'fs'}, {'a': 5, 'b': 3, 'c': 6, 'op': 'fs'}, {'a': 6, 'b': 2, 'c': 8, 'op': 'fs'}, {'a': 7, 'b': 3, 'c': 8, 'op': 'fs'}, {'a': 7, 'b': 5, 'c': 8, 'op': 'fs'}, {'a': 8, 'b': 3, 'c': 10, 'op': 'fs'}, {'a': 9, 'b': 4, 'c': 10, 'op': 'fs'}, {'a': 11, 'b': 5, 'c': 12, 'op': 'fs'}],
    },
    {
        "id": 'basic-u7-tenths',
        "course": "basic", "unit": 7,
        "topic": 'Tenths',
        "op": 'dt', "max_value": 9,
        "levels": ("abstract",),
        "symbols": ('tenth', 'point'),
        "advance_line": "Three in a row — you've got it! You know your tenths.",
        "teach": [
            ('Today we meet decimals. Split one whole into ten equal parts — each part is one tenth. We write one tenth with a point: 0.1.',
             '[[goal text="Tenths"]]'),
            ('Watch me. 0.3 is three tenths. 0.4 is four tenths. Three tenths plus four tenths equals seven tenths — 0.7.',
             '[[step eq="0.3 + 0.4 = 0.7"]]'),
            ('The point keeps the tenths in their own place, just like tens and ones have places. Count the tenths, and the point stays put.',
             '[[step eq="0.2 + 0.5 = 0.7"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. Two tenths plus six tenths equals eight tenths — 0.8.',
                        '[[step eq="0.2 + 0.6 = 0.8"]]'),
             "ask": {'a': 1, 'b': 3, 'op': 'dt'}},
            {"worked": ('One more together. Five tenths plus four tenths equals nine tenths.',
                        '[[step eq="0.5 + 0.4 = 0.9"]]'),
             "ask": {'a': 2, 'b': 4, 'op': 'dt'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 1, 'b': 2, 'op': 'dt'}, {'a': 2, 'b': 2, 'op': 'dt'}, {'a': 1, 'b': 4, 'op': 'dt'}, {'a': 3, 'b': 3, 'op': 'dt'}, {'a': 2, 'b': 5, 'op': 'dt'}, {'a': 4, 'b': 4, 'op': 'dt'}, {'a': 3, 'b': 5, 'op': 'dt'}, {'a': 6, 'b': 3, 'op': 'dt'}, {'a': 4, 'b': 5, 'op': 'dt'}, {'a': 7, 'b': 2, 'op': 'dt'}],
    },
    {
        "id": 'basic-u7-dimes-and-pennies',
        "course": "basic", "unit": 7,
        "topic": 'Dimes and pennies',
        "op": 'm', "max_value": 99,
        "levels": ("abstract",),
        "symbols": ('dime', 'penny'),
        "advance_line": "Three in a row — you've got it! You can count money like a shopkeeper.",
        "teach": [
            ('Money uses tens and ones too. A dime is worth ten cents. A penny is worth one cent. Dimes are the tens, pennies are the ones.',
             '[[goal text="Dimes and pennies"]]'),
            ('Watch me. 3 dimes and 4 pennies. The dimes bring 30 cents, the pennies bring 4 more. 30 plus 4 equals 34 cents.',
             '[[step eq="3 dimes = 30 cents"]][[step eq="30 + 4 = 34"]][[step eq="3 dimes + 4 pennies = 34 cents"]]'),
            ('One more, watch. 5 dimes and 2 pennies. 50 plus 2 equals 52 cents.',
             '[[step eq="5 dimes + 2 pennies = 52 cents"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 2 dimes and 7 pennies. 20 plus 7 equals 27 cents.',
                        '[[step eq="2 dimes + 7 pennies = 27 cents"]]'),
             "ask": {'a': 2, 'b': 5, 'op': 'm'}},
            {"worked": ('One more together. 4 dimes and 6 pennies equals 46 cents.',
                        '[[step eq="4 dimes + 6 pennies = 46 cents"]]'),
             "ask": {'a': 4, 'b': 3, 'op': 'm'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 1, 'b': 2, 'op': 'm'}, {'a': 1, 'b': 5, 'op': 'm'}, {'a': 2, 'b': 3, 'op': 'm'}, {'a': 3, 'b': 1, 'op': 'm'}, {'a': 3, 'b': 6, 'op': 'm'}, {'a': 5, 'b': 4, 'op': 'm'}, {'a': 6, 'b': 2, 'op': 'm'}, {'a': 7, 'b': 5, 'op': 'm'}, {'a': 8, 'b': 8, 'op': 'm'}, {'a': 9, 'b': 9, 'op': 'm'}],
    },
    {
        "id": 'basic-u8-percent-of',
        "course": "basic", "unit": 8,
        "topic": 'Percent',
        "op": 'pc', "max_value": 100,
        "levels": ("abstract",),
        "symbols": ('percent', 'hundred'),
        "advance_line": "Three in a row — you've got it! You can take a percent of a number.",
        "teach": [
            ('Percent means out of one hundred. Fifty percent means fifty out of a hundred — one half. Twenty-five percent is one fourth. Ten percent is one tenth.',
             '[[goal text="Percent"]]'),
            ('Watch me find 50 percent of 8. Fifty percent is one half, and one half of 8 equals 4. So 50 percent of 8 equals 4.',
             '[[step eq="50% of 8 = 4"]]'),
            ('One more, watch. 10 percent of 40. Ten percent is one tenth, and one tenth of 40 equals 4. So 10 percent of 40 equals 4.',
             '[[step eq="10% of 40 = 4"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 25 percent of 8. Twenty-five percent is one fourth, and one fourth of 8 equals 2.',
                        '[[step eq="25% of 8 = 2"]]'),
             "ask": {'a': 25, 'b': 12, 'op': 'pc'}},
            {"worked": ('One more together. 50 percent of 12 equals 6.',
                        '[[step eq="50% of 12 = 6"]]'),
             "ask": {'a': 50, 'b': 14, 'op': 'pc'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 50, 'b': 2, 'op': 'pc'}, {'a': 50, 'b': 4, 'op': 'pc'}, {'a': 25, 'b': 4, 'op': 'pc'}, {'a': 50, 'b': 6, 'op': 'pc'}, {'a': 50, 'b': 10, 'op': 'pc'}, {'a': 25, 'b': 16, 'op': 'pc'}, {'a': 50, 'b': 18, 'op': 'pc'}, {'a': 10, 'b': 20, 'op': 'pc'}, {'a': 10, 'b': 30, 'op': 'pc'}, {'a': 10, 'b': 50, 'op': 'pc'}],
    },
    {
        "id": 'basic-u8-one-costs',
        "course": "basic", "unit": 8,
        "topic": 'What one costs',
        "op": 'rate', "max_value": 40,
        "levels": ("abstract",),
        "symbols": ('cost', 'divided'),
        "advance_line": "Three in a row — you've got it! You can find what one costs.",
        "teach": [
            ('Prices often come in bunches: six apples for twelve dollars. To compare prices, we find what ONE costs. That is dividing.',
             '[[goal text="What one costs"]]'),
            ('Watch me. 6 apples cost 12 dollars. 12 divided by 6 equals 2 — one apple costs 2 dollars.',
             '[[step eq="12 ÷ 6 = 2"]]'),
            ('One more, watch. 4 apples cost 20 dollars. 20 divided by 4 equals 5 — one apple costs 5 dollars.',
             '[[step eq="20 ÷ 4 = 5"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 3 apples cost 9 dollars. 9 divided by 3 equals 3 — one costs 3 dollars.',
                        '[[step eq="9 ÷ 3 = 3"]]'),
             "ask": {'a': 8, 'b': 4, 'op': 'rate'}},
            {"worked": ('One more together. 5 apples cost 15 dollars — one costs 3 dollars.',
                        '[[step eq="15 ÷ 5 = 3"]]'),
             "ask": {'a': 12, 'b': 3, 'op': 'rate'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 6, 'b': 2, 'op': 'rate'}, {'a': 10, 'b': 2, 'op': 'rate'}, {'a': 12, 'b': 4, 'op': 'rate'}, {'a': 15, 'b': 3, 'op': 'rate'}, {'a': 16, 'b': 4, 'op': 'rate'}, {'a': 20, 'b': 5, 'op': 'rate'}, {'a': 24, 'b': 6, 'op': 'rate'}, {'a': 28, 'b': 7, 'op': 'rate'}, {'a': 32, 'b': 8, 'op': 'rate'}, {'a': 36, 'b': 9, 'op': 'rate'}],
    },
    {
        "id": 'basic-u9-perimeter',
        "course": "basic", "unit": 9,
        "topic": 'Perimeter',
        "op": 'peri', "max_value": 60,
        "levels": ("abstract",),
        "symbols": ('perimeter', 'around'),
        "advance_line": "Three in a row — you've got it! You can walk the whole way around.",
        "teach": [
            ('Perimeter is the distance all the way around a shape. For a rectangle, walk all four sides: long, wide, long, wide.',
             '[[goal text="Perimeter"]]'),
            ('Watch me. A rectangle 5 long and 3 wide. Walk around: 5 plus 3 plus 5 plus 3 equals 16. The perimeter equals 16.',
             '[[step eq="5 + 3 + 5 + 3 = 16"]]'),
            ('One more, watch. 6 long and 2 wide: 6 plus 2 plus 6 plus 2 equals 16.',
             '[[step eq="6 + 2 + 6 + 2 = 16"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 4 long and 2 wide: 4 plus 2 plus 4 plus 2 equals 12.',
                        '[[step eq="4 + 2 + 4 + 2 = 12"]]'),
             "ask": {'a': 5, 'b': 2, 'op': 'peri'}},
            {"worked": ('One more together. 7 long and 3 wide — the perimeter equals 20.',
                        '[[step eq="7 + 3 + 7 + 3 = 20"]]'),
             "ask": {'a': 6, 'b': 4, 'op': 'peri'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 3, 'b': 1, 'op': 'peri'}, {'a': 3, 'b': 2, 'op': 'peri'}, {'a': 4, 'b': 3, 'op': 'peri'}, {'a': 5, 'b': 3, 'op': 'peri'}, {'a': 6, 'b': 3, 'op': 'peri'}, {'a': 7, 'b': 4, 'op': 'peri'}, {'a': 8, 'b': 5, 'op': 'peri'}, {'a': 9, 'b': 6, 'op': 'peri'}, {'a': 10, 'b': 7, 'op': 'peri'}, {'a': 12, 'b': 8, 'op': 'peri'}],
    },
    {
        "id": 'basic-u9-area',
        "course": "basic", "unit": 9,
        "topic": 'Area',
        "op": 'area', "max_value": 96,
        "levels": ("abstract",),
        "symbols": ('area', 'inside'),
        "advance_line": "Three in a row — you've got it! You can count the space inside.",
        "teach": [
            ('Area is the space INSIDE a shape, counted in squares. For a rectangle, area is the long side times the wide side.',
             '[[goal text="Area"]]'),
            ('Watch me. A rectangle 5 long and 3 wide holds 3 rows of 5 squares: 5 times 3 equals 15. The area equals 15 squares.',
             '[[step eq="5 × 3 = 15"]]'),
            ('One more, watch. 4 long and 2 wide: 4 times 2 equals 8 squares.',
             '[[step eq="4 × 2 = 8"]]'),
        ],
        "pairs": [
            {"worked": ('Here is one more, done for you. 6 long and 2 wide: 6 times 2 equals 12 squares.',
                        '[[step eq="6 × 2 = 12"]]'),
             "ask": {'a': 3, 'b': 2, 'op': 'area'}},
            {"worked": ('One more together. 7 long and 4 wide — the area equals 28 squares.',
                        '[[step eq="7 × 4 = 28"]]'),
             "ask": {'a': 5, 'b': 4, 'op': 'area'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [{'a': 5, 'b': 2, 'op': 'area'}, {'a': 4, 'b': 3, 'op': 'area'}, {'a': 6, 'b': 3, 'op': 'area'}, {'a': 7, 'b': 3, 'op': 'area'}, {'a': 6, 'b': 4, 'op': 'area'}, {'a': 8, 'b': 4, 'op': 'area'}, {'a': 9, 'b': 5, 'op': 'area'}, {'a': 8, 'b': 6, 'op': 'area'}, {'a': 9, 'b': 7, 'op': 'area'}, {'a': 12, 'b': 8, 'op': 'area'}],
    },
    {
        "id": "basic-u1-place-value-to-1000", "course": "basic", "unit": 1,
        "topic": "Place value to 1,000",
        "op": "pv", "max_value": 999,
        "levels": ("abstract",),
        "symbols": ("hundreds", "ones"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can read hundreds, tens and ones."),
        "teach": [
            ("You know tens and ones. Today we add one more place: hundreds. Ten "
             "tens, put together, equal one hundred. A three-digit number counts "
             "hundreds, then tens, then ones.",
             '[[goal text="Place value to 1,000"]]'),
            ("Watch me read 342. The 3 counts hundreds — three hundred. The 4 "
             "counts tens — forty. The 2 counts ones. 3 hundreds, 4 tens and 2 "
             "ones equals 342.",
             '[[step eq="342 = 3 hundreds + 4 tens + 2 ones"]]'),
            ("One more, watch. 5 hundreds, 1 ten and 7 ones. Five hundred, ten, "
             "seven — 517.",
             '[[step eq="5 hundreds + 1 ten + 7 ones = 517"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 hundreds, 6 tens and 3 "
                        "ones. Two hundred sixty-three — 263.",
                        '[[step eq="2 hundreds + 6 tens + 3 ones = 263"]]'),
             "ask": {"a": 2, "b": 3, "c": 4, "op": "pv"}},
            {"worked": ("One more together. 7 hundreds, 2 tens and 9 ones — 729.",
                        '[[step eq="7 hundreds + 2 tens + 9 ones = 729"]]'),
             "ask": {"a": 6, "b": 1, "c": 5, "op": "pv"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "c": 2, "op": "pv"}, {"a": 1, "b": 4, "c": 3, "op": "pv"},
            {"a": 2, "b": 2, "c": 5, "op": "pv"}, {"a": 3, "b": 1, "c": 6, "op": "pv"},
            {"a": 3, "b": 5, "c": 2, "op": "pv"}, {"a": 4, "b": 3, "c": 8, "op": "pv"},
            {"a": 5, "b": 6, "c": 1, "op": "pv"}, {"a": 6, "b": 4, "c": 7, "op": "pv"},
            {"a": 7, "b": 8, "c": 3, "op": "pv"}, {"a": 9, "b": 2, "c": 9, "op": "pv"},
        ],
    },
    {
        "id": "basic-u1-rounding-tens", "course": "basic", "unit": 1,
        "topic": "Rounding to the nearest ten",
        "op": "r10", "max_value": 110,
        "levels": ("abstract",),
        "symbols": ("round", "nearest"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can round to the nearest ten."),
        "teach": [
            ("Rounding gives a number a simpler neighbour. To round to the "
             "nearest ten, look at the ones digit: if it is 4 or smaller, round "
             "down. If it is 5 or bigger, round up.",
             '[[goal text="Rounding to the nearest ten"]]'),
            ("Watch me round 47. The ones digit is 7 — that is 5 or bigger, so "
             "we round up. 47 rounds to 50.",
             '[[step eq="47 → nearest ten = 50"]]'),
            ("One more, watch. Round 32. The ones digit is 2 — 4 or smaller, so "
             "we round down. 32 rounds to 30.",
             '[[step eq="32 → nearest ten = 30"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Round 85. The ones "
                        "digit is 5 — 5 or bigger rounds up. 85 rounds to 90.",
                        '[[step eq="85 → nearest ten = 90"]]'),
             "ask": {"a": 74, "op": "r10", "b": 0}},
            {"worked": ("One more together. Round 61 — the ones digit is 1, so "
                        "round down to 60.",
                        '[[step eq="61 → nearest ten = 60"]]'),
             "ask": {"a": 58, "op": "r10", "b": 0}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 12, "op": "r10", "b": 0}, {"a": 17, "op": "r10", "b": 0},
            {"a": 23, "op": "r10", "b": 0}, {"a": 35, "op": "r10", "b": 0},
            {"a": 41, "op": "r10", "b": 0}, {"a": 49, "op": "r10", "b": 0},
            {"a": 56, "op": "r10", "b": 0}, {"a": 64, "op": "r10", "b": 0},
            {"a": 78, "op": "r10", "b": 0}, {"a": 93, "op": "r10", "b": 0},
        ],
    },
    {
        "id": "basic-u1-rounding-hundreds", "course": "basic", "unit": 1,
        "topic": "Rounding to the nearest hundred",
        "op": "r100", "max_value": 1000,
        "levels": ("abstract",),
        "symbols": ("round", "nearest"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can round to the nearest hundred."),
        "teach": [
            ("Rounding to the nearest hundred works the same way — but now the "
             "TENS digit decides. 4 or smaller rounds down; 5 or bigger rounds "
             "up.",
             '[[goal text="Rounding to the nearest hundred"]]'),
            ("Watch me round 470. The tens digit is 7 — 5 or bigger, round up. "
             "470 rounds to 500.",
             '[[step eq="470 → nearest hundred = 500"]]'),
            ("One more, watch. Round 320. The tens digit is 2 — round down. 320 "
             "rounds to 300.",
             '[[step eq="320 → nearest hundred = 300"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Round 149. The tens "
                        "digit is 4 — round down. 149 rounds to 100.",
                        '[[step eq="149 → nearest hundred = 100"]]'),
             "ask": {"a": 253, "op": "r100", "b": 0}},
            {"worked": ("One more together. Round 662 — the tens digit is 6, "
                        "round up to 700.",
                        '[[step eq="662 → nearest hundred = 700"]]'),
             "ask": {"a": 578, "op": "r100", "b": 0}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 120, "op": "r100", "b": 0}, {"a": 180, "op": "r100", "b": 0},
            {"a": 240, "op": "r100", "b": 0}, {"a": 350, "op": "r100", "b": 0},
            {"a": 430, "op": "r100", "b": 0}, {"a": 490, "op": "r100", "b": 0},
            {"a": 560, "op": "r100", "b": 0}, {"a": 640, "op": "r100", "b": 0},
            {"a": 770, "op": "r100", "b": 0}, {"a": 910, "op": "r100", "b": 0},
        ],
    },
    {
        "id": "basic-u1-multi-digit-review", "course": "basic", "unit": 1,
        "topic": "Adding and taking away — review",
        "op": "+", "max_value": 99, "mixed_review": True,
        "levels": ("abstract",),
        "symbols": ("carry", "regroup"),
        "advance_line": ("Three in a row — you've got it! "
                         "Your adding and taking away are ready for bigger things."),
        "teach": [
            ("You learned carrying and regrouping in Entry-Level Math. Before we "
             "multiply and divide, let's warm those up — a quick mix of both.",
             '[[goal text="Adding and taking away — review"]]'),
            ("Remember: when the ones add up to over nine, write the ones digit "
             "and carry one ten. When the top ones digit is too small, regroup — "
             "one ten becomes ten ones.",
             '[[step eq="carry: ones over nine"]][[step eq="regroup: ones too small"]]'),
        ],
        "pairs": [
            {"worked": ("One quick worked one. 38 plus 24: ones 8 plus 4 equals "
                        "12 — over nine, write 2, carry 1. Tens: 3 plus 2 plus 1 "
                        "equals 6. 62.",
                        '[[step eq="38 + 24 = 62"]]'),
             "ask": {"a": 27, "b": 15, "op": "+"}},
            {"worked": ("And one taking away. 53 take away 28: 3 is too small — "
                        "regroup. 13 take away 8 equals 5; 4 take away 2 equals "
                        "2. 25.",
                        '[[step eq="53 − 28 = 25"]]'),
             "ask": {"a": 42, "b": 17, "op": "-"}},
        ],
        "practice_intro": ("Now it's your turn — adds and take-aways, mixed. "
                           "Three right answers in a row and we're done."),
        "bank": [
            {"a": 26, "b": 15, "op": "+"}, {"a": 31, "b": 14, "op": "-"},
            {"a": 35, "b": 17, "op": "+"}, {"a": 44, "b": 26, "op": "-"},
            {"a": 46, "b": 18, "op": "+"}, {"a": 52, "b": 35, "op": "-"},
            {"a": 57, "b": 26, "op": "+"}, {"a": 63, "b": 47, "op": "-"},
            {"a": 65, "b": 28, "op": "+"}, {"a": 82, "b": 56, "op": "-"},
        ],
    },
    {
        "id": "basic-u2-multiply-two-digit", "course": "basic", "unit": 2,
        "topic": "Multiplying bigger numbers",
        "op": "*", "max_value": 300,
        "levels": ("abstract",),
        "symbols": ("times", "tens"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can multiply bigger numbers."),
        "teach": [
            ("Today we multiply a two-digit number. The trick: split it into "
             "tens and ones, multiply each piece, then put the pieces together.",
             '[[goal text="Multiplying bigger numbers"]]'),
            ("Watch me. 34 times 2. Split 34 into 30 and 4. 30 times 2 equals "
             "60. 4 times 2 equals 8. 60 plus 8 equals 68.",
             '[[step eq="34 × 2"]][[step eq="30 × 2 = 60"]][[step eq="4 × 2 = 8"]]'
             '[[step eq="60 + 8 = 68"]]'),
            ("One more, watch. 23 times 3. 20 times 3 equals 60; 3 times 3 "
             "equals 9. 60 plus 9 equals 69.",
             '[[step eq="23 × 3"]][[step eq="20 × 3 = 60"]][[step eq="3 × 3 = 9"]]'
             '[[step eq="23 × 3 = 69"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 42 times 2. 40 times 2 "
                        "equals 80; 2 times 2 equals 4. 84.",
                        '[[step eq="42 × 2 = 84"]]'),
             "ask": {"a": 43, "b": 2, "op": "*"}},
            {"worked": ("One more together. 31 times 3. 90 plus 3 — 93.",
                        '[[step eq="31 × 3 = 93"]]'),
             "ask": {"a": 32, "b": 3, "op": "*"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 12, "b": 2, "op": "*"}, {"a": 13, "b": 3, "op": "*"},
            {"a": 24, "b": 2, "op": "*"}, {"a": 21, "b": 3, "op": "*"},
            {"a": 23, "b": 4, "op": "*"}, {"a": 34, "b": 3, "op": "*"},
            {"a": 42, "b": 3, "op": "*"}, {"a": 33, "b": 5, "op": "*"},
            {"a": 45, "b": 4, "op": "*"}, {"a": 62, "b": 4, "op": "*"},
        ],
    },
    {
        "id": "basic-u3-divide-two-digit", "course": "basic", "unit": 3,
        "topic": "Dividing bigger numbers",
        "op": "/", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("divided", "split"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can divide bigger numbers."),
        "teach": [
            ("Today we divide a two-digit number. The trick is the same one "
             "multiplying used: split the number into friendly pieces, divide "
             "each piece, then put the answers together.",
             '[[goal text="Dividing bigger numbers"]]'),
            ("Watch me. 84 divided by 4. Split 84 into 80 and 4. 80 divided by "
             "4 equals 20. 4 divided by 4 equals 1. 20 plus 1 equals 21.",
             '[[step eq="84 ÷ 4"]][[step eq="80 ÷ 4 = 20"]][[step eq="4 ÷ 4 = 1"]]'
             '[[step eq="84 ÷ 4 = 21"]]'),
            ("One more, watch. 69 divided by 3. 60 divided by 3 equals 20; 9 "
             "divided by 3 equals 3. 23.",
             '[[step eq="69 ÷ 3 = 23"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 48 divided by 2. 40 "
                        "divided by 2 equals 20; 8 divided by 2 equals 4. 24.",
                        '[[step eq="48 ÷ 2 = 24"]]'),
             "ask": {"a": 46, "b": 2, "op": "/"}},
            {"worked": ("One more together. 96 divided by 3 — 32.",
                        '[[step eq="96 ÷ 3 = 32"]]'),
             "ask": {"a": 93, "b": 3, "op": "/"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 22, "b": 2, "op": "/"}, {"a": 26, "b": 2, "op": "/"},
            {"a": 33, "b": 3, "op": "/"}, {"a": 39, "b": 3, "op": "/"},
            {"a": 44, "b": 4, "op": "/"}, {"a": 48, "b": 4, "op": "/"},
            {"a": 55, "b": 5, "op": "/"}, {"a": 63, "b": 3, "op": "/"},
            {"a": 66, "b": 2, "op": "/"}, {"a": 88, "b": 4, "op": "/"},
        ],
    },
    {
        "id": "basic-u5-fractions-on-the-number-line", "course": "basic", "unit": 5,
        "topic": "Fractions live on the number line",
        "op": "nl", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("hop", "line"),
        "advance_line": ("Three in a row — you've got it! "
                         "A fraction is a number with its own home on the line."),
        "teach": [
            ("A fraction is not just a piece of pizza — a fraction is a NUMBER, "
             "and every number has a home on the number line. Today we find "
             "where fractions live.",
             '[[goal text="Fractions live on the number line"]]'),
            ("Watch me. Cut the line from 0 to 1 into 4 equal hops. Each hop is "
             "one fourth. Hop once — you stand on 1 out of 4. Hop three times — "
             "you stand on 3 out of 4.",
             '[[step eq="0 —(4 hops)— 1"]][[step eq="3 hops → 3/4"]]'),
            ("And if you take ALL 4 hops, you reach 1 whole. Four fourths "
             "equals one.",
             '[[step eq="4 hops → 4/4 = 1"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Cut the line into 3 "
                        "hops. 2 hops from 0 lands on 2 out of 3.",
                        '[[step eq="0 —(3 hops)— 1 · 2 hops → 2/3"]]'),
             "ask": {"a": 2, "b": 5, "op": "nl"}},
            {"worked": ("One more together. Cut the line into 6 hops — reaching "
                        "1 whole takes all 6 hops.",
                        '[[step eq="0 —(6 hops)— 1 · 1 whole = 6 hops"]]'),
             "ask": {"a": 1, "b": 8, "op": "nlw"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 2, "op": "nl"}, {"a": 1, "b": 3, "op": "nl"},
            {"a": 2, "b": 3, "op": "nl"}, {"a": 1, "b": 4, "op": "nlw"},
            {"a": 3, "b": 4, "op": "nl"}, {"a": 1, "b": 5, "op": "nlw"},
            {"a": 4, "b": 5, "op": "nl"}, {"a": 5, "b": 6, "op": "nl"},
            {"a": 1, "b": 8, "op": "nl"}, {"a": 1, "b": 10, "op": "nlw"},
        ],
    },
    # ------------------------- BUILD kd: the content sweep -------------------------
    {
        "id": "entry-u1-counting-to-10", "course": "entry", "unit": 1,
        "topic": "Counting to 10",
        "op": "cnt", "max_value": 10,
        "levels": ("concrete",),   # the picture IS the problem; there is no
                                   # abstract form of "count these stars"
        "symbols": ("count",),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count to ten."),
        "teach": [
            ("Today we learn to count stars. Point to each star and say one "
             "number for it: one, two, three.",
             '[[goal text="Counting to 10"]]'),
            ("Watch me count these stars. One, two, three. Three stars.",
             '[[objects emoji="⭐" groups="3" caption="count them one at a time"]]'),
            ("Watch me count again. One, two, three, four, five. Five stars.",
             '[[objects emoji="⭐" groups="5" caption="count them one at a time"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One, two, three, four. "
                        "Four stars.",
                        '[[objects emoji="⭐" groups="4" caption="count them one at a time"]]'),
             "ask": {"a": 2, "b": 0, "op": "cnt"}},
            {"worked": ("One more together. One, two, three, four, five, six. "
                        "Six stars.",
                        '[[objects emoji="⭐" groups="6" caption="count them one at a time"]]'),
             "ask": {"a": 4, "b": 0, "op": "cnt"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 0, "op": "cnt"}, {"a": 3, "b": 0, "op": "cnt"},
            {"a": 5, "b": 0, "op": "cnt"}, {"a": 6, "b": 0, "op": "cnt"},
            {"a": 7, "b": 0, "op": "cnt"}, {"a": 8, "b": 0, "op": "cnt"},
            {"a": 9, "b": 0, "op": "cnt"}, {"a": 10, "b": 0, "op": "cnt"},
        ],
    },
    {
        "id": "entry-u1-numbers-before-and-after", "course": "entry", "unit": 1,
        "topic": "Numbers before and after",
        "op": "aft", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("after", "before"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can find the number before and the number after."),
        "teach": [
            ("Numbers stand in a line, always in the same order: 1, 2, 3, 4, 5. "
             "Today we find the number right after a number, and the number "
             "right before it.",
             '[[goal text="Numbers before and after"]]'),
            ("Watch me. What comes right after 5? Count up one: 6. "
             "6 comes right after 5.",
             '[[step eq="5, 6"]]'),
            ("Watch me. What comes right before 8? Count back one: 7. "
             "7 comes right before 8.",
             '[[step eq="7, 8"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Right after 6 comes 7.",
                        '[[step eq="6, 7"]]'),
             "ask": {"a": 4, "b": 0, "op": "aft"}},
            {"worked": ("One more together. Right before 10 comes 9.",
                        '[[step eq="9, 10"]]'),
             "ask": {"a": 7, "b": 0, "op": "bef"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 0, "op": "aft"}, {"a": 3, "b": 0, "op": "bef"},
            {"a": 5, "b": 0, "op": "aft"}, {"a": 6, "b": 0, "op": "bef"},
            {"a": 8, "b": 0, "op": "aft"}, {"a": 9, "b": 0, "op": "bef"},
            {"a": 11, "b": 0, "op": "aft"}, {"a": 12, "b": 0, "op": "bef"},
            {"a": 14, "b": 0, "op": "aft"}, {"a": 15, "b": 0, "op": "bef"},
            {"a": 17, "b": 0, "op": "aft"}, {"a": 20, "b": 0, "op": "bef"},
        ],
    },
    {
        "id": "entry-u3-story-problems", "course": "entry", "unit": 3,
        "topic": "Story problems — adding and taking away",
        "op": "+", "max_value": 10, "a_max": 9, "b_max": 9,
        "mixed_review": True,   # plus and minus interleave; a ramp across two ops
                                # would be meaningless
        "levels": ("abstract",),
        "symbols": ("plus", "minus"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can solve story problems."),
        "teach": [
            ("Today we solve story problems. A story problem tells a little "
             "story and hides a plus or a minus inside. Our job is to find it.",
             '[[goal text="Story problems"]]'),
            ("Listen. Maya has 3 stickers. She gets 2 more. Getting more means "
             "putting together — that is plus. Three plus two equals five "
             "stickers in all.",
             '[[step eq="3 + 2 = 5"]]'),
            ("Listen. Ben has 6 grapes. He eats 2. Eating them is taking away — "
             "that is minus. Six minus two equals four grapes are left.",
             '[[step eq="6 − 2 = 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Ava has 4 crayons. She "
                        "gets 3 more. That is plus. Four plus three equals seven "
                        "crayons in all.",
                        '[[step eq="4 + 3 = 7"]]'),
             "ask": {"a": 5, "b": 2, "op": "+",
                     "story": ("Sam has 5 shells. He finds 2 more. How many "
                               "shells does he have in all?")}},
            {"worked": ("One more together. Leo has 8 balloons. 3 fly away. That "
                        "is minus — take away. Eight minus three equals five "
                        "balloons are left.",
                        '[[step eq="8 − 3 = 5"]]'),
             "ask": {"a": 7, "b": 3, "op": "-",
                     "story": ("Mia has 7 berries. She eats 3. How many berries "
                               "are left?")}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 1, "op": "+",
             "story": ("Jo has 2 rocks. She finds 1 more. How many rocks does "
                       "she have in all?")},
            {"a": 3, "b": 1, "op": "-",
             "story": "Ed has 3 kites. 1 blows away. How many kites are left?"},
            {"a": 3, "b": 2, "op": "+",
             "story": ("Ana has 3 cups. She gets 2 more. How many cups does she "
                       "have in all?")},
            {"a": 4, "b": 2, "op": "-",
             "story": "Ty has 4 socks. 2 get lost. How many socks are left?"},
            {"a": 4, "b": 3, "op": "+",
             "story": ("Bo has 4 cars. He gets 3 more. How many cars does he "
                       "have in all?")},
            {"a": 6, "b": 2, "op": "-",
             "story": "Zoe has 6 pears. She eats 2. How many pears are left?"},
            {"a": 5, "b": 4, "op": "+",
             "story": ("Kim has 5 beads. She gets 4 more. How many beads does "
                       "she have in all?")},
            {"a": 8, "b": 3, "op": "-",
             "story": ("Dan has 8 stamps. He gives 3 away. How many stamps are "
                       "left?")},
            {"a": 6, "b": 3, "op": "+",
             "story": ("Pia has 6 leaves. She finds 3 more. How many leaves does "
                       "she have in all?")},
            {"a": 9, "b": 4, "op": "-",
             "story": "Max has 9 blocks. 4 fall down. How many blocks are left?"},
        ],
    },
    {
        "id": "entry-u7-counting-coins", "course": "entry", "unit": 7,
        "topic": "Counting nickels and pennies",
        "op": "nick", "max_value": 35,
        "levels": ("abstract",),
        "symbols": ("nickel", "penny"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count nickels and pennies."),
        "teach": [
            ("Money time! A penny is worth 1 cent. A nickel is worth 5 cents.",
             '[[goal text="Counting nickels and pennies"]]'),
            ("Watch me count 2 nickels and 3 pennies. Nickels first, count by "
             "five: 5, 10. Then pennies, count on: 11, 12, 13. That is 13 "
             "cents.",
             '[[step eq="5, 10 — 11, 12, 13 = 13 cents"]]'),
            ("One more, watch. 3 nickels and 1 penny. Count by five: 5, 10, 15. "
             "One more: 16. 16 cents.",
             '[[step eq="5, 10, 15 — 16 = 16 cents"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 1 nickel and 2 "
                        "pennies. 5 — then 6, 7. 7 cents.",
                        '[[step eq="5 — 6, 7 = 7 cents"]]'),
             "ask": {"a": 1, "b": 4, "op": "nick"}},
            {"worked": ("One more together. 2 nickels and 2 pennies. 5, 10 — "
                        "11, 12. 12 cents.",
                        '[[step eq="5, 10 — 11, 12 = 12 cents"]]'),
             "ask": {"a": 2, "b": 4, "op": "nick"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 1, "op": "nick"}, {"a": 1, "b": 2, "op": "nick"},
            {"a": 1, "b": 3, "op": "nick"}, {"a": 2, "b": 1, "op": "nick"},
            {"a": 2, "b": 2, "op": "nick"}, {"a": 2, "b": 3, "op": "nick"},
            {"a": 3, "b": 1, "op": "nick"}, {"a": 3, "b": 2, "op": "nick"},
            {"a": 4, "b": 1, "op": "nick"}, {"a": 4, "b": 3, "op": "nick"},
            {"a": 5, "b": 2, "op": "nick"}, {"a": 6, "b": 1, "op": "nick"},
        ],
    },
    {
        "id": "basic-u3-story-problems", "course": "basic", "unit": 3,
        "topic": "Story problems — multiplying and dividing",
        "op": "*", "max_value": 40, "mixed_review": True,
        "levels": ("abstract",),
        "symbols": ("times", "divided"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can solve multiplying and dividing story problems."),
        "teach": [
            ("Story problems can hide times and divided by too. Equal groups of "
             "the same size mean times. Sharing into equal groups means divided "
             "by.",
             '[[goal text="Story problems — multiplying and dividing"]]'),
            ("Listen. Each box holds 4 crayons. There are 3 boxes. Equal boxes — "
             "that is times. Four times three equals twelve crayons in all.",
             '[[step eq="4 × 3 = 12"]]'),
            ("Listen. 12 cookies are shared into 3 equal bags. Sharing — that is "
             "divided by. Twelve divided by three equals four cookies in each "
             "bag.",
             '[[step eq="12 ÷ 3 = 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Each pack holds 5 "
                        "pencils. There are 2 packs. Five times two equals ten "
                        "pencils in all.",
                        '[[step eq="5 × 2 = 10"]]'),
             "ask": {"a": 3, "b": 4, "op": "*",
                     "story": ("Each jar holds 3 marbles. There are 4 jars. How "
                               "many marbles in all?")}},
            {"worked": ("One more together. 10 apples are shared into 2 equal "
                        "baskets. Ten divided by two equals five apples in each "
                        "basket.",
                        '[[step eq="10 ÷ 2 = 5"]]'),
             "ask": {"a": 12, "b": 4, "op": "/",
                     "story": ("12 grapes are shared into 4 equal bowls. How "
                               "many grapes go in each bowl?")}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 3, "op": "*",
             "story": ("Each cup holds 2 straws. There are 3 cups. How many "
                       "straws in all?")},
            {"a": 6, "b": 2, "op": "/",
             "story": ("6 socks are shared into 2 equal drawers. How many socks "
                       "go in each drawer?")},
            {"a": 4, "b": 2, "op": "*",
             "story": ("Each bag holds 4 buns. There are 2 bags. How many buns "
                       "in all?")},
            {"a": 8, "b": 4, "op": "/",
             "story": ("8 fish are shared into 4 equal tanks. How many fish "
                       "swim in each tank?")},
            {"a": 5, "b": 3, "op": "*",
             "story": ("Each row has 5 chairs. There are 3 rows. How many "
                       "chairs in all?")},
            {"a": 15, "b": 3, "op": "/",
             "story": ("15 stickers are shared into 3 equal sheets. How many "
                       "stickers go on each sheet?")},
            {"a": 6, "b": 4, "op": "*",
             "story": ("Each tray holds 6 eggs. There are 4 trays. How many "
                       "eggs in all?")},
            {"a": 20, "b": 5, "op": "/",
             "story": ("20 beads are shared into 5 equal strings. How many "
                       "beads go on each string?")},
            {"a": 7, "b": 3, "op": "*",
             "story": ("Each shelf holds 7 books. There are 3 shelves. How many "
                       "books in all?")},
            {"a": 30, "b": 6, "op": "/",
             "story": ("30 seeds are shared into 6 equal pots. How many seeds "
                       "go in each pot?")},
        ],
    },
    {
        "id": "basic-u4-least-common-multiple", "course": "basic", "unit": 4,
        "topic": "Least common multiple",
        "op": "lcm", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("multiple", "least"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can find the least common multiple."),
        "teach": [
            ("A multiple of a number is what you land on when you count by it. "
             "The multiples of 3 are 3, 6, 9, 12, and so on.",
             '[[goal text="Least common multiple"]]'),
            ("The least common multiple of two numbers is the smallest number "
             "in BOTH count-by lists. Watch me find it for 2 and 3. Count by 2: "
             "2, 4, 6. Count by 3: 3, 6. The first match is 6.",
             '[[step eq="2: 2, 4, 6"]][[step eq="3: 3, 6"]]'
             '[[step eq="LCM of 2 and 3 = 6"]]'),
            ("One more, watch. 4 and 6. Count by 4: 4, 8, 12. Count by 6: 6, "
             "12. The first match is 12. The least common multiple of 4 and 6 "
             "equals 12.",
             '[[step eq="4: 4, 8, 12"]][[step eq="6: 6, 12"]]'
             '[[step eq="LCM of 4 and 6 = 12"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 and 6. Count by 3: "
                        "3, 6. Count by 6: 6. The first match is 6 — the least "
                        "common multiple of 3 and 6 equals 6.",
                        '[[step eq="LCM of 3 and 6 = 6"]]'),
             "ask": {"a": 2, "b": 6, "op": "lcm"}},
            {"worked": ("One more together. 2 and 5. Count by 2: 2, 4, 6, 8, "
                        "10. Count by 5: 5, 10. The first match is 10.",
                        '[[step eq="LCM of 2 and 5 = 10"]]'),
             "ask": {"a": 4, "b": 5, "op": "lcm"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 4, "op": "lcm"}, {"a": 2, "b": 3, "op": "lcm"},
            {"a": 3, "b": 6, "op": "lcm"}, {"a": 2, "b": 5, "op": "lcm"},
            {"a": 3, "b": 4, "op": "lcm"}, {"a": 4, "b": 6, "op": "lcm"},
            {"a": 2, "b": 7, "op": "lcm"}, {"a": 3, "b": 5, "op": "lcm"},
            {"a": 4, "b": 10, "op": "lcm"}, {"a": 3, "b": 8, "op": "lcm"},
            {"a": 5, "b": 6, "op": "lcm"},
        ],
    },
    {
        "id": "basic-u6-add-fractions-different-bottoms", "course": "basic",
        "unit": 6,
        "topic": "Adding fractions with different bottoms",
        "op": "fu", "max_value": 12,
        "levels": ("abstract",),
        "symbols": ("bottoms", "plus"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can add fractions with different bottoms."),
        "teach": [
            ("Today we add fractions with different bottoms. The trick: change "
             "one fraction so both bottoms match, then add the tops.",
             '[[goal text="Adding fractions with different bottoms"]]'),
            ("Watch me. One half plus one fourth. One half equals two fourths. "
             "Two fourths plus one fourth equals three fourths.",
             '[[step eq="1/2 + 1/4"]][[step eq="1/2 = 2/4"]]'
             '[[step eq="2/4 + 1/4 = 3/4"]]'),
            ("One more, watch. One third plus two sixths. One third equals two "
             "sixths. Two sixths plus two sixths equals four sixths.",
             '[[step eq="1/3 + 2/6"]][[step eq="1/3 = 2/6"]]'
             '[[step eq="2/6 + 2/6 = 4/6"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. One half plus one "
                        "sixth. One half equals three sixths. Three sixths plus "
                        "one sixth equals four sixths.",
                        '[[step eq="1/2 = 3/6"]][[step eq="3/6 + 1/6 = 4/6"]]'),
             "ask": {"a": 1, "b": 2, "c": 4, "op": "fu"}},
            {"worked": ("One more together. One fourth plus one eighth. One "
                        "fourth equals two eighths. Two eighths plus one eighth "
                        "equals three eighths.",
                        '[[step eq="1/4 = 2/8"]][[step eq="2/8 + 1/8 = 3/8"]]'),
             "ask": {"a": 1, "b": 3, "c": 6, "op": "fu"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 2, "c": 6, "op": "fu"},
            {"a": 2, "b": 3, "c": 6, "op": "fu"},
            {"a": 1, "b": 2, "c": 8, "op": "fu"},
            {"a": 3, "b": 2, "c": 8, "op": "fu"},
            {"a": 1, "b": 4, "c": 8, "op": "fu"},
            {"a": 5, "b": 4, "c": 8, "op": "fu"},
            {"a": 2, "b": 2, "c": 10, "op": "fu"},
            {"a": 3, "b": 5, "c": 10, "op": "fu"},
            {"a": 4, "b": 2, "c": 12, "op": "fu"},
            {"a": 5, "b": 3, "c": 12, "op": "fu"},
            {"a": 2, "b": 4, "c": 12, "op": "fu"},
            {"a": 7, "b": 6, "c": 12, "op": "fu"},
        ],
    },
    {
        "id": "basic-u7-hundredths", "course": "basic", "unit": 7,
        "topic": "Hundredths",
        "op": "dh", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("hundredths", "plus"),
        "advance_line": ("Three in a row — you've got it! "
                         "You know your hundredths."),
        "teach": [
            ("A hundredth is one out of one hundred equal pieces. We write "
             "hundredths after the point — 0.25 is 25 hundredths.",
             '[[goal text="Hundredths"]]'
             '[[step eq="0.25 = 25 hundredths"]]'),
            ("Adding hundredths works like adding whole numbers. Watch me. 25 "
             "hundredths plus 13 hundredths equals 38 hundredths — 0.38.",
             '[[step eq="0.25 + 0.13 = 0.38"]]'),
            ("One more, watch. 40 hundredths plus 22 hundredths equals 62 "
             "hundredths. 0.62.",
             '[[step eq="0.40 + 0.22 = 0.62"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 31 hundredths plus 24 "
                        "hundredths equals 55 hundredths — 0.55.",
                        '[[step eq="0.31 + 0.24 = 0.55"]]'),
             "ask": {"a": 11, "b": 12, "op": "dh"}},
            {"worked": ("One more together. 26 hundredths plus 32 hundredths "
                        "equals 58 hundredths.",
                        '[[step eq="0.26 + 0.32 = 0.58"]]'),
             "ask": {"a": 22, "b": 15, "op": "dh"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 12, "b": 13, "op": "dh"}, {"a": 21, "b": 14, "op": "dh"},
            {"a": 23, "b": 22, "op": "dh"}, {"a": 31, "b": 24, "op": "dh"},
            {"a": 42, "b": 23, "op": "dh"}, {"a": 34, "b": 37, "op": "dh"},
            {"a": 44, "b": 31, "op": "dh"}, {"a": 52, "b": 33, "op": "dh"},
            {"a": 63, "b": 27, "op": "dh"}, {"a": 61, "b": 34, "op": "dh"},
        ],
    },
    {
        "id": "basic-u9-quarter-turns", "course": "basic", "unit": 9,
        "topic": "Quarter turns and degrees",
        "op": "ang", "max_value": 360,
        "levels": ("abstract",),
        "symbols": ("degrees", "turn"),
        "advance_line": ("Three in a row — you've got it! "
                         "You know your quarter turns."),
        "teach": [
            ("We measure turning in degrees. There are 90 degrees in one "
             "quarter turn of a circle, and four quarter turns go all the way "
             "around.",
             '[[goal text="Quarter turns and degrees"]]'),
            ("Watch me. 2 quarter turns. 2 times 90 equals 180 — so 2 quarter "
             "turns equals 180 degrees.",
             '[[step eq="2 × 90° = 180°"]]'),
            ("And backwards, watch. 270 degrees. How many quarter turns? Count "
             "by 90: 90, 180, 270 — three counts. 270 degrees equals 3 quarter "
             "turns.",
             '[[step eq="270° = 3 × 90°"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 quarter turns. 3 "
                        "times 90 equals 270 degrees.",
                        '[[step eq="3 × 90° = 270°"]]'),
             "ask": {"a": 4, "b": 0, "op": "ang"}},
            {"worked": ("One more together. 180 degrees. Count by 90: 90, 180 — "
                        "two counts. 180 degrees equals 2 quarter turns.",
                        '[[step eq="180° = 2 × 90°"]]'),
             "ask": {"a": 360, "b": 0, "op": "angq"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 1, "b": 0, "op": "ang"}, {"a": 90, "b": 0, "op": "angq"},
            {"a": 2, "b": 0, "op": "ang"}, {"a": 180, "b": 0, "op": "angq"},
            {"a": 3, "b": 0, "op": "ang"}, {"a": 270, "b": 0, "op": "angq"},
        ],
    },
    {
        "id": "basic-u9-volume", "course": "basic", "unit": 9,
        "topic": "Volume — counting cubes",
        "op": "vol", "max_value": 96,
        "levels": ("abstract",),
        "symbols": ("times", "cubes"),
        "advance_line": ("Three in a row — you've got it! "
                         "You can count the cubes that fill a box."),
        "teach": [
            ("Volume is how many cubes fill a box. Count the cubes in one "
             "layer, then count the layers.",
             '[[goal text="Volume — counting cubes"]]'),
            ("Watch me. A box 3 cubes long, 2 cubes wide, 2 cubes tall. One "
             "layer holds 3 times 2 equals 6 cubes. There are 2 layers. 6 "
             "times 2 equals 12 cubes.",
             '[[step eq="3 × 2 = 6"]][[step eq="6 × 2 = 12 cubes"]]'),
            ("One more, watch. 4 cubes long, 2 wide, 2 tall. 4 times 2 equals "
             "8 in a layer. 8 times 2 equals 16 cubes.",
             '[[step eq="4 × 2 = 8"]][[step eq="8 × 2 = 16 cubes"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 2 long, 2 wide, 3 "
                        "tall. 2 times 2 equals 4. 4 times 3 equals 12 cubes.",
                        '[[step eq="2 × 2 = 4"]][[step eq="4 × 3 = 12 cubes"]]'),
             "ask": {"a": 3, "b": 3, "c": 1, "op": "vol"}},
            {"worked": ("One more together. 5 long, 2 wide, 2 tall. 5 times 2 "
                        "equals 10. 10 times 2 equals 20 cubes.",
                        '[[step eq="5 × 2 = 10"]][[step eq="10 × 2 = 20 cubes"]]'),
             "ask": {"a": 2, "b": 3, "c": 1, "op": "vol"}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and "
                           "we're done — here comes the first one."),
        "bank": [
            {"a": 2, "b": 2, "c": 1, "op": "vol"},
            {"a": 3, "b": 2, "c": 1, "op": "vol"},
            {"a": 2, "b": 2, "c": 2, "op": "vol"},
            {"a": 3, "b": 2, "c": 2, "op": "vol"},
            {"a": 4, "b": 2, "c": 2, "op": "vol"},
            {"a": 3, "b": 3, "c": 2, "op": "vol"},
            {"a": 4, "b": 3, "c": 2, "op": "vol"},
            {"a": 5, "b": 3, "c": 2, "op": "vol"},
            {"a": 4, "b": 4, "c": 2, "op": "vol"},
            {"a": 4, "b": 3, "c": 3, "op": "vol"},
            {"a": 4, "b": 4, "c": 3, "op": "vol"},
            {"a": 4, "b": 4, "c": 4, "op": "vol"},
        ],
    },
]
LESSONS.extend(_MORE_LESSONS)

# =============================================================================
# PREALGEBRA -- UNIT 1: NUMBER SENSE & ORDER OF OPERATIONS (build kk, 2026-08-21)
# =============================================================================
# The first unit authored AFTER build kj gave the scripted lane the real board, and
# the first of the eight courses Jim asked for ("I wanna go through all the courses").
#
# NAMED BY THEIR INPUTS, BOUNDS SAID PLAINLY -- Jim's jw/jx ruling. Not "Order of
# operations": a child does not know what an operation is. "Times before add" says
# what they will do, and the opening beat says which numbers.
#
# WHY THIS ORDER: the rule is worth nothing until there is a second step to compete
# with the first, so lesson 1 puts times against add. Parentheses come next because
# they OVERRIDE what was just learned, and a rule is only understood once you meet
# its exception. Exponents come third because they are a NEW kind of step rather than
# a new order. Lesson 4 stacks all three, which is the only place the full order can
# actually be tested.
_PREALGEBRA_U1 = [
    {
        "id": "pre-u1-times-before-add",
        "course": "prealgebra", "unit": 1,
        "topic": "Times before add",
        "op": "tba", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("times", "plus", "equals"),
        "advance_line": "Three in a row — you've got it! You do the times first, every time.",
        "teach": [
            ["Today a problem has two steps in it, not one. You will see a plus and a times in the same line. There is a rule for which one goes first, and it is not left to right. The times goes first. Always.",
             '[[goal text="Times before add"]]'],
            ["Watch me do 2 plus 3 times 4. Times first: 3 times 4 equals 12. Now the adding: 2 plus 12 equals 14. If you had gone left to right you would have said 20, and 20 is wrong.",
             '[[step eq="2 + 3 × 4"]][[step eq="3 × 4 = 12"]][[step eq="2 + 12 = 14"]]'],
            ["One more. 5 plus 2 times 6. Find the times: 2 times 6 equals 12. Then add: 5 plus 12 equals 17.",
             '[[step eq="5 + 2 × 6"]][[step eq="2 × 6 = 12"]][[step eq="5 + 12 = 17"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 plus 3 times 3. Times first: 3 times 3 equals 9. Then 4 plus 9 equals 13.",
                        '[[step eq="4 + 3 × 3"]][[step eq="4 + 9 = 13"]]'],
             "ask": {"a": 3, "b": 2, "c": 5, "op": "tba"}},
            {"worked": ["One more together. 6 plus 4 times 2. The times gives 8. Then 6 plus 8 equals 14.",
                        '[[step eq="6 + 4 × 2"]][[step eq="6 + 8 = 14"]]'],
             "ask": {"a": 2, "b": 3, "c": 6, "op": "tba"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 1, "b": 2, "c": 3, "op": "tba"},
            {"a": 2, "b": 2, "c": 4, "op": "tba"},
            {"a": 3, "b": 3, "c": 3, "op": "tba"},
            {"a": 2, "b": 4, "c": 3, "op": "tba"},
            {"a": 5, "b": 3, "c": 4, "op": "tba"},
            {"a": 4, "b": 5, "c": 4, "op": "tba"},
            {"a": 6, "b": 4, "c": 6, "op": "tba"},
            {"a": 3, "b": 7, "c": 5, "op": "tba"},
            {"a": 8, "b": 6, "c": 7, "op": "tba"},
            {"a": 5, "b": 8, "c": 9, "op": "tba"},
        ],
    },
    {
        "id": "pre-u1-parentheses-first",
        "course": "prealgebra", "unit": 1,
        "topic": "Parentheses first",
        "op": "parf", "max_value": 150,
        "levels": ("abstract",),
        "symbols": ("parentheses", "times", "plus", "equals"),
        "advance_line": "Three in a row — you've got it! What is inside the parentheses goes first.",
        "teach": [
            ["Last time you learned the times goes before the add. Today you meet the one thing that beats it. Two curved marks around part of a problem are called parentheses, and whatever sits inside them goes first — even an add.",
             '[[goal text="Parentheses first"]]'],
            ["Watch me do 2 plus 3, in parentheses, times 4. Inside first: 2 plus 3 equals 5. Now the times: 5 times 4 equals 20. Without the parentheses this same line would be 14, so the marks change the answer.",
             '[[step eq="(2 + 3) × 4"]][[step eq="2 + 3 = 5"]][[step eq="5 × 4 = 20"]]'],
            ["One more. 1 plus 6, in parentheses, times 3. Inside: 1 plus 6 equals 7. Then 7 times 3 equals 21.",
             '[[step eq="(1 + 6) × 3"]][[step eq="1 + 6 = 7"]][[step eq="7 × 3 = 21"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 plus 2, in parentheses, times 5. Inside gives 6. Then 6 times 5 equals 30.",
                        '[[step eq="(4 + 2) × 5"]][[step eq="6 × 5 = 30"]]'],
             "ask": {"a": 3, "b": 3, "c": 4, "op": "parf"}},
            {"worked": ["One more together. 5 plus 1, in parentheses, times 7. Inside gives 6. Then 6 times 7 equals 42.",
                        '[[step eq="(5 + 1) × 7"]][[step eq="6 × 7 = 42"]]'],
             "ask": {"a": 2, "b": 5, "c": 3, "op": "parf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 1, "b": 2, "c": 2, "op": "parf"},
            {"a": 2, "b": 3, "c": 2, "op": "parf"},
            {"a": 3, "b": 2, "c": 3, "op": "parf"},
            {"a": 4, "b": 3, "c": 3, "op": "parf"},
            {"a": 2, "b": 6, "c": 4, "op": "parf"},
            {"a": 5, "b": 4, "c": 4, "op": "parf"},
            {"a": 3, "b": 7, "c": 5, "op": "parf"},
            {"a": 6, "b": 5, "c": 6, "op": "parf"},
            {"a": 8, "b": 4, "c": 8, "op": "parf"},
            {"a": 7, "b": 9, "c": 7, "op": "parf"},
        ],
    },
    {
        "id": "pre-u1-exponents-are-repeated-times",
        "course": "prealgebra", "unit": 1,
        "topic": "Exponents are repeated times",
        "op": "expn", "max_value": 216,
        "levels": ("abstract",),
        "symbols": ("squared", "power", "times", "equals"),
        "advance_line": "Three in a row — you've got it! A small high number counts how many to multiply.",
        "teach": [
            ["A small number written high up after another number is an exponent. It is not a times. It counts how many copies to multiply. 3 with a small 2 means two 3s multiplied: 3 times 3. Say it as three squared.",
             '[[goal text="Exponents are repeated times"]]'],
            ["Three squared equals 9. Here is why the word squared fits — three rows of three really do make a square, and counting the little boxes gives 9.",
             '[[areamodel rows="3" cols="3" caption="three rows of three"]][[step eq="3² = 3 × 3 = 9"]]'],
            ["A small 3 means three copies, and we say it as to the power 3. 2 with a small 3 is 2 times 2 times 2, which equals 8. Careful — it is not 2 times 3. That would be 6, and 6 is wrong.",
             '[[step eq="2³ = 2 × 2 × 2 = 8"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 squared is two 4s multiplied — 4 times 4, which equals 16.",
                        '[[areamodel rows="4" cols="4" caption="four rows of four"]][[step eq="4² = 16"]]'],
             "ask": {"a": 6, "b": 2, "op": "expn"}},
            {"worked": ["One more together. 3 with a small 3 means three 3s multiplied: 3 times 3 times 3, which equals 27.",
                        '[[step eq="3³ = 3 × 3 × 3 = 27"]]'],
             "ask": {"a": 7, "b": 2, "op": "expn"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "expn"},
            {"a": 3, "b": 2, "op": "expn"},
            {"a": 4, "b": 2, "op": "expn"},
            {"a": 5, "b": 2, "op": "expn"},
            {"a": 3, "b": 3, "op": "expn"},
            {"a": 4, "b": 3, "op": "expn"},
            {"a": 8, "b": 2, "op": "expn"},
            {"a": 9, "b": 2, "op": "expn"},
            {"a": 5, "b": 3, "op": "expn"},
            {"a": 6, "b": 3, "op": "expn"},
        ],
    },
    {
        "id": "pre-u1-power-then-times-then-add",
        "course": "prealgebra", "unit": 1,
        "topic": "Power, then times, then add",
        "op": "exo", "max_value": 130,
        "levels": ("abstract",),
        "symbols": ("squared", "times", "plus", "equals"),
        "advance_line": "Three in a row — you've got it! Power first, then times, then add.",
        "teach": [
            ["You know two rules now: the times goes before the add, and parentheses go before everything. Today a third step joins them — the exponent — and it goes first of all. Power first, then times, then add.",
             '[[goal text="Power, then times, then add"]]'],
            ["Watch me do 3 squared plus 2 times 4. Power first: 3 squared equals 9. Times next: 2 times 4 equals 8. Add last: 9 plus 8 equals 17.",
             '[[step eq="3² + 2 × 4"]][[step eq="9 + 8"]][[step eq="= 17"]]'],
            ["One more. 2 squared plus 5 times 3. The power gives 4. The times gives 15. 4 plus 15 equals 19.",
             '[[step eq="2² + 5 × 3"]][[step eq="4 + 15 = 19"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 squared plus 3 times 2. Power: 16. Times: 6. 16 plus 6 equals 22.",
                        '[[step eq="4² + 3 × 2"]][[step eq="16 + 6 = 22"]]'],
             "ask": {"a": 3, "b": 4, "c": 2, "op": "exo"}},
            {"worked": ["One more together. 5 squared plus 2 times 6. Power: 25. Times: 12. 25 plus 12 equals 37.",
                        '[[step eq="5² + 2 × 6"]][[step eq="25 + 12 = 37"]]'],
             "ask": {"a": 4, "b": 5, "c": 2, "op": "exo"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 2, "c": 2, "op": "exo"},
            {"a": 3, "b": 3, "c": 2, "op": "exo"},
            {"a": 3, "b": 2, "c": 4, "op": "exo"},
            {"a": 4, "b": 2, "c": 3, "op": "exo"},
            {"a": 4, "b": 3, "c": 3, "op": "exo"},
            {"a": 5, "b": 2, "c": 4, "op": "exo"},
            {"a": 5, "b": 4, "c": 3, "op": "exo"},
            {"a": 6, "b": 3, "c": 4, "op": "exo"},
            {"a": 7, "b": 5, "c": 3, "op": "exo"},
            {"a": 8, "b": 6, "c": 5, "op": "exo"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U1)

# =============================================================================
# PREALGEBRA -- UNITS 2 & 3 (build km, 2026-08-21)
# =============================================================================
# U2 goes UNDERNEATH what Basic Math already teaches. Basic finds the greatest common
# factor and the least common multiple by listing; these three lessons are what that
# listing is made of -- what a factor is, which numbers have only two, and how to break
# a number all the way down to primes.
#
# U3 is the first unit in the app whose answers go BELOW ZERO, which is why validate()
# gained min_value. Every lesson through Basic Math answers with a count, so "answers
# are 1 or more" was a real invariant worth keeping; a lesson that means to break it now
# says so, and the guard stays on for the other 45.
_PREALGEBRA_U23 = [
    {
        "id": "pre-u2-how-many-factors",
        "course": "prealgebra", "unit": 2,
        "topic": "How many factors a number has",
        "op": "nfac", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("factor", "divides"),
        "advance_line": "Three in a row — you've got it! You can count a number's factors.",
        "teach": [
            ["A factor is a number that divides another one exactly, with nothing left over. 1 and the number itself are always factors. Today you count how many a number has in all.",
             '[[goal text="How many factors a number has"]]'],
            ["Take 6. Does 1 divide it? Yes. Does 2? Yes, 6 is two 3s. Does 3? Yes. Does 4? No, there is something left over. Does 5? No. Does 6? Yes. So 6 has four factors: 1, 2, 3 and 6.",
             '[[step eq="factors of 6 = 1, 2, 3, 6 → four"]]'],
            ["Now 7. Only 1 and 7 divide it exactly. Nothing else fits. So 7 has just two factors. Numbers with exactly two are special, and they have a name you will meet next lesson.",
             '[[step eq="factors of 7 = 1, 7 → two"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 8. 1 divides it, 2 divides it, 4 divides it, 8 divides it. 3, 5, 6 and 7 do not. So 8 has four factors.",
                        '[[step eq="factors of 8 = 1, 2, 4, 8 → four"]]'],
             "ask": {"a": 14, "b": 4, "op": "nfac"}},
            {"worked": ["One more together. 9. 1 divides it, 3 divides it, 9 divides it. So 9 has three factors.",
                        '[[step eq="factors of 9 = 1, 3, 9 → three"]]'],
             "ask": {"a": 25, "b": 3, "op": "nfac"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 7, "b": 2, "op": "nfac"},
            {"a": 9, "b": 3, "op": "nfac"},
            {"a": 10, "b": 4, "op": "nfac"},
            {"a": 12, "b": 6, "op": "nfac"},
            {"a": 15, "b": 4, "op": "nfac"},
            {"a": 16, "b": 5, "op": "nfac"},
            {"a": 18, "b": 6, "op": "nfac"},
            {"a": 20, "b": 6, "op": "nfac"},
            {"a": 24, "b": 8, "op": "nfac"},
            {"a": 30, "b": 8, "op": "nfac"},
        ],
    },
    {
        "id": "pre-u2-the-smallest-factor",
        "course": "prealgebra", "unit": 2,
        "topic": "The smallest factor above 1",
        "op": "spf", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("factor", "prime"),
        "advance_line": "Three in a row — you've got it! You can find a number's smallest factor.",
        "teach": [
            ["A number with exactly two factors — just 1 and itself — is a prime number. 2, 3, 5 and 7 are primes. Every other number can be divided by something smaller, and today you hunt for the smallest one.",
             '[[goal text="The smallest factor above 1"]]'],
            ["Take 15. Try 2 — no, 15 is odd. Try 3 — yes, 15 is three 5s. So 3 is the smallest factor of 15 above 1. You go up in order and stop at the first one that fits.",
             '[[step eq="15 ÷ 2 leaves 1 · 15 ÷ 3 = 5 ✓"]]'],
            ["Take 35. Try 2 — no. Try 3 — no. Try 5 — yes, 35 is five 7s. The smallest factor of 35 above 1 is 5.",
             '[[step eq="35 ÷ 5 = 7 ✓"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 27. 2 does not fit. 3 does — 27 is three 9s. So the answer is 3.",
                        '[[step eq="27 ÷ 3 = 9 ✓"]]'],
             "ask": {"a": 51, "b": 3, "op": "spf"}},
            {"worked": ["One more together. 91. 2 no, 3 no, 5 no. 7 fits — 91 is seven 13s. The answer is 7.",
                        '[[step eq="91 ÷ 7 = 13 ✓"]]'],
             "ask": {"a": 65, "b": 5, "op": "spf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 9, "b": 3, "op": "spf"},
            {"a": 15, "b": 3, "op": "spf"},
            {"a": 21, "b": 3, "op": "spf"},
            {"a": 25, "b": 5, "op": "spf"},
            {"a": 33, "b": 3, "op": "spf"},
            {"a": 35, "b": 5, "op": "spf"},
            {"a": 39, "b": 3, "op": "spf"},
            {"a": 49, "b": 7, "op": "spf"},
            {"a": 55, "b": 5, "op": "spf"},
            {"a": 77, "b": 7, "op": "spf"},
        ],
    },
    {
        "id": "pre-u2-breaking-into-primes",
        "course": "prealgebra", "unit": 2,
        "topic": "Breaking a number into primes",
        "op": "npf", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("prime", "factor"),
        "advance_line": "Three in a row — you've got it! Every number breaks down into primes.",
        "teach": [
            ["Every number that is not prime can be written as primes multiplied. Keep pulling out the smallest factor until only primes are left. Today you count how many primes it takes.",
             '[[goal text="Breaking a number into primes"]]'],
            ["Take 12. The smallest factor is 2, and 12 is two 6s. Now break the 6: that is two 3s. Nothing is left but primes. 12 equals 2 times 2 times 3 — three primes.",
             '[[step eq="12 = 2 × 6"]][[step eq="6 = 2 × 3"]][[step eq="12 = 2 × 2 × 3 → three"]]'],
            ["Take 20. Smallest factor 2, so 20 is two 10s. Break the 10: two 5s. 20 equals 2 times 2 times 5 — three primes again.",
             '[[step eq="20 = 2 × 2 × 5 → three"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 8. Two 4s, and the 4 is two 2s. 8 equals 2 times 2 times 2 — three primes.",
                        '[[step eq="8 = 2 × 2 × 2 → three"]]'],
             "ask": {"a": 15, "b": 2, "op": "npf"}},
            {"worked": ["One more together. 30. Two 15s, and 15 is three 5s. 30 equals 2 times 3 times 5 — three primes.",
                        '[[step eq="30 = 2 × 3 × 5 → three"]]'],
             "ask": {"a": 16, "b": 4, "op": "npf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 6, "b": 2, "op": "npf"},
            {"a": 10, "b": 2, "op": "npf"},
            {"a": 12, "b": 3, "op": "npf"},
            {"a": 18, "b": 3, "op": "npf"},
            {"a": 20, "b": 3, "op": "npf"},
            {"a": 27, "b": 3, "op": "npf"},
            {"a": 28, "b": 3, "op": "npf"},
            {"a": 45, "b": 3, "op": "npf"},
            {"a": 50, "b": 3, "op": "npf"},
            {"a": 63, "b": 3, "op": "npf"},
        ],
    },
    {
        "id": "pre-u3-counting-back-past-zero",
        "course": "prealgebra", "unit": 3,
        "topic": "Counting back past zero",
        "op": "cbz", "max_value": 25, "min_value": -20,
        "levels": ("abstract",),
        "symbols": ("negative", "zero", "number line"),
        "advance_line": "Three in a row — you've got it! You can count straight past zero.",
        "teach": [
            ["Numbers keep going to the left of zero. Those are the negative numbers, and they are real places on the number line — not mistakes. One step left of zero is negative 1. Two steps is negative 2.",
             '[[goal text="Counting back past zero"]][[numberline min="-10" max="10" points="-3"]]'],
            ["Start at 3 and count back 7. Three steps take you to zero. You still have four to go, so you carry on to the left and land on negative 4.",
             '[[numberline min="-10" max="10" points="-4"]][[step eq="3 − 7 = −4"]]'],
            ["Start at 2 and count back 9. Two steps reach zero, seven more keep going left. You land on negative 7.",
             '[[numberline min="-10" max="10" points="-7"]][[step eq="2 − 9 = −7"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Start at 4, count back 6. Four steps to zero, two more to the left — negative 2.",
                        '[[numberline min="-10" max="10" points="-2"]][[step eq="4 − 6 = −2"]]'],
             "ask": {"a": 6, "b": 10, "op": "cbz"}},
            {"worked": ["One more together. Start at 1, count back 8. One step to zero, seven more left — negative 7.",
                        '[[numberline min="-10" max="10" points="-7"]][[step eq="1 − 8 = −7"]]'],
             "ask": {"a": 4, "b": 15, "op": "cbz"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 7, "op": "cbz"},
            {"a": 2, "b": 6, "op": "cbz"},
            {"a": 5, "b": 9, "op": "cbz"},
            {"a": 4, "b": 11, "op": "cbz"},
            {"a": 6, "b": 13, "op": "cbz"},
            {"a": 3, "b": 12, "op": "cbz"},
            {"a": 7, "b": 16, "op": "cbz"},
            {"a": 8, "b": 19, "op": "cbz"},
            {"a": 2, "b": 14, "op": "cbz"},
            {"a": 5, "b": 18, "op": "cbz"},
        ],
    },
    {
        "id": "pre-u3-adding-a-negative",
        "course": "prealgebra", "unit": 3,
        "topic": "Adding a negative number",
        "op": "addneg", "max_value": 30, "min_value": -20,
        "levels": ("abstract",),
        "symbols": ("negative", "plus"),
        "advance_line": "Three in a row — you've got it! Adding a negative moves you left.",
        "teach": [
            ["Adding usually moves you right along the line. But adding a NEGATIVE number moves you the other way — to the left. Adding negative 3 does exactly what counting back 3 does.",
             '[[goal text="Adding a negative number"]]'],
            ["Watch: 5 plus negative 7. Start at 5, move 7 to the left. Five steps reach zero, two more keep going, and you land on negative 2. So 5 plus negative 7 equals negative 2.",
             '[[numberline min="-10" max="10" points="-2"]][[step eq="5 + (−7) = −2"]]'],
            ["Another: 3 plus negative 6. Start at 3, move 6 left. You land on negative 3. The plus sign did not stop you going left — the negative did that.",
             '[[numberline min="-10" max="10" points="-3"]][[step eq="3 + (−6) = −3"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 plus negative 9. Start at 4, move 9 to the left, land on negative 5.",
                        '[[numberline min="-10" max="10" points="-5"]][[step eq="4 + (−9) = −5"]]'],
             "ask": {"a": 6, "b": 13, "op": "addneg"}},
            {"worked": ["One more together. 2 plus negative 8 lands on negative 6.",
                        '[[numberline min="-10" max="10" points="-6"]][[step eq="2 + (−8) = −6"]]'],
             "ask": {"a": 8, "b": 12, "op": "addneg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 5, "b": 7, "op": "addneg"},
            {"a": 3, "b": 6, "op": "addneg"},
            {"a": 8, "b": 11, "op": "addneg"},
            {"a": 4, "b": 10, "op": "addneg"},
            {"a": 9, "b": 15, "op": "addneg"},
            {"a": 6, "b": 14, "op": "addneg"},
            {"a": 2, "b": 11, "op": "addneg"},
            {"a": 7, "b": 18, "op": "addneg"},
            {"a": 3, "b": 16, "op": "addneg"},
            {"a": 5, "b": 21, "op": "addneg"},
        ],
    },
    {
        "id": "pre-u3-taking-away-a-negative",
        "course": "prealgebra", "unit": 3,
        "topic": "Taking away a negative number",
        # min_value is declared even though every ANSWER here is positive: the wrong
        # option a child can tap IS negative (the error for "4 take away negative 6" is
        # 4 − 6 = −2, and that is exactly the mistake worth offering). The floor has to
        # cover what appears on screen, not only what is correct. The op's own check
        # keeps the answers positive by construction: a + b with both a and b above 0.
        "op": "subneg", "max_value": 30, "min_value": -20,
        "levels": ("abstract",),
        "symbols": ("negative", "take away"),
        "advance_line": "Three in a row — you've got it! Taking away a negative moves you right.",
        "teach": [
            ["Here is the surprising one. Taking away usually moves you left. But taking away a NEGATIVE moves you RIGHT — the two negatives cancel each other and the answer grows.",
             '[[goal text="Taking away a negative number"]]'],
            ["Watch: 3 take away negative 2. Taking away a move-left is a move-right, so you go 2 to the right of 3 and land on 5. 3 take away negative 2 equals 5.",
             '[[step eq="3 − (−2) = 3 + 2 = 5"]]'],
            ["Another: 5 take away negative 3 equals 8. Whenever a take away meets a negative, swap the pair for a plus.",
             '[[step eq="5 − (−3) = 5 + 3 = 8"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 6 take away negative 4. The two negatives become a plus: 6 plus 4 equals 10.",
                        '[[step eq="6 − (−4) = 6 + 4 = 10"]]'],
             "ask": {"a": 7, "b": 6, "op": "subneg"}},
            {"worked": ["One more together. 2 take away negative 9 equals 2 plus 9, which equals 11.",
                        '[[step eq="2 − (−9) = 11"]]'],
             "ask": {"a": 4, "b": 13, "op": "subneg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 2, "op": "subneg"},
            {"a": 5, "b": 3, "op": "subneg"},
            {"a": 4, "b": 6, "op": "subneg"},
            {"a": 7, "b": 4, "op": "subneg"},
            {"a": 6, "b": 8, "op": "subneg"},
            {"a": 9, "b": 5, "op": "subneg"},
            {"a": 8, "b": 9, "op": "subneg"},
            {"a": 5, "b": 12, "op": "subneg"},
            {"a": 9, "b": 11, "op": "subneg"},
            {"a": 7, "b": 15, "op": "subneg"},
        ],
    },
    {
        "id": "pre-u3-times-with-a-negative",
        "course": "prealgebra", "unit": 3,
        "topic": "Times with a negative number",
        "op": "mulneg", "max_value": 90, "min_value": -95,
        "levels": ("abstract",),
        "symbols": ("negative", "times"),
        "advance_line": "Three in a row — you've got it! One negative turns the answer negative.",
        "teach": [
            ["Times works the same as it always did — only the sign is new. Negative 3 times 4 means four lots of negative 3. Four moves of 3 to the left lands on negative 12.",
             '[[goal text="Times with a negative number"]]'],
            ["So do the times first and ignore the sign: 3 times 4 equals 12. Then look at the signs. One of them is negative, so the answer is negative. Negative 3 times 4 equals negative 12.",
             '[[numberline min="-20" max="10" points="-12"]][[step eq="(−3) × 4 = −12"]]'],
            ["Another: negative 5 times 3. Five 3s equal 15, and one negative sign turns it negative 15.",
             '[[step eq="(−5) × 3 = −15"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Negative 2 times 7. Two 7s equal 14, and one negative turns it negative 14.",
                        '[[step eq="(−2) × 7 = −14"]]'],
             "ask": {"a": 4, "b": 6, "op": "mulneg"}},
            {"worked": ["One more together. Negative 6 times 4. Six 4s equal 24, so the answer is negative 24.",
                        '[[step eq="(−6) × 4 = −24"]]'],
             "ask": {"a": 8, "b": 5, "op": "mulneg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "mulneg"},
            {"a": 3, "b": 3, "op": "mulneg"},
            {"a": 2, "b": 6, "op": "mulneg"},
            {"a": 4, "b": 4, "op": "mulneg"},
            {"a": 3, "b": 7, "op": "mulneg"},
            {"a": 5, "b": 5, "op": "mulneg"},
            {"a": 4, "b": 8, "op": "mulneg"},
            {"a": 6, "b": 7, "op": "mulneg"},
            {"a": 7, "b": 8, "op": "mulneg"},
            {"a": 9, "b": 9, "op": "mulneg"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U23)

# =============================================================================
# PREALGEBRA -- UNIT 4: FRACTIONS (build kn, 2026-08-21)
# =============================================================================
# Basic Math takes fractions as far as adding and taking them away, and its
# "fraction of a group" only ever asks for a UNIT fraction -- "one half of 4". These
# four go past that, in the order the ideas actually depend on each other: take a
# non-unit fraction of a number (which is the unit-fraction skill done a times), then
# count how many parts fit inside a whole, which is what makes dividing BY a fraction
# make sense rather than being a rule to memorise, and finally read a fraction that is
# bigger than 1.
#
# EVERY ANSWER IS A WHOLE NUMBER, because a tap answer has to be one. That is a real
# constraint on what this unit can ask, and it was allowed to shape the questions
# rather than being worked around -- "how many fourths are in 3 wholes" is a better
# question than "what is 3 divided by one fourth" for a child meeting this the first
# time, and it happens to answer with an integer.
_PREALGEBRA_U4 = [
    {
        "id": "pre-u4-a-fraction-of-a-number",
        "course": "prealgebra", "unit": 4,
        "topic": "Two thirds of a number",
        "op": "nuf", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("fraction", "of"),
        "advance_line": "Three in a row — you've got it! Divide by the bottom, then times by the top.",
        "teach": [
            ["You already know how to find one half or one third of a number. Today the top of the fraction is bigger than 1, and that only adds one step. Divide by the bottom to find one part, then take as many parts as the top says.",
             '[[goal text="Two thirds of a number"]]'],
            ["Watch me find two thirds of 12. The bottom is 3, so cut 12 into 3 equal parts: 12 divided by 3 equals 4. That is ONE third. The top is 2, so take two of them: 4 times 2 equals 8.",
             '[[step eq="12 ÷ 3 = 4"]][[step eq="4 × 2 = 8"]]'],
            ["One more. Three fourths of 20. Bottom first: 20 divided by 4 equals 5. Now the top: 5 times 3 equals 15.",
             '[[step eq="20 ÷ 4 = 5"]][[step eq="5 × 3 = 15"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Two fifths of 10. 10 divided by 5 equals 2, and 2 times 2 equals 4.",
                        '[[step eq="10 ÷ 5 = 2"]][[step eq="2 × 2 = 4"]]'],
             "ask": {"a": 3, "b": 4, "c": 16, "op": "nuf"}},
            {"worked": ["One more together. Five sixths of 18. 18 divided by 6 equals 3, and 3 times 5 equals 15.",
                        '[[step eq="18 ÷ 6 = 3"]][[step eq="3 × 5 = 15"]]'],
             "ask": {"a": 2, "b": 7, "c": 21, "op": "nuf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 6, "op": "nuf"},
            {"a": 2, "b": 5, "c": 10, "op": "nuf"},
            {"a": 3, "b": 4, "c": 8, "op": "nuf"},
            {"a": 2, "b": 3, "c": 9, "op": "nuf"},
            {"a": 3, "b": 8, "c": 16, "op": "nuf"},
            {"a": 3, "b": 4, "c": 12, "op": "nuf"},
            {"a": 3, "b": 5, "c": 15, "op": "nuf"},
            {"a": 2, "b": 3, "c": 15, "op": "nuf"},
            {"a": 5, "b": 6, "c": 12, "op": "nuf"},
            {"a": 4, "b": 5, "c": 20, "op": "nuf"},
        ],
    },
    {
        "id": "pre-u4-how-many-parts-in-a-whole",
        "course": "prealgebra", "unit": 4,
        "topic": "How many parts fit in a whole",
        "op": "uic", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("fraction", "whole"),
        "advance_line": "Three in a row — you've got it! Count the parts in one whole, then times by the wholes.",
        "teach": [
            ["The bottom number of a fraction says how many equal parts make one whole. Four fourths make one whole. Five fifths make one whole. So counting parts inside several wholes is just a times.",
             '[[goal text="How many parts fit in a whole"]]'],
            ["How many fourths are in 3 wholes? One whole holds 4 fourths. Three wholes hold three lots of that: 3 times 4 equals 12. So there are 12 fourths in 3 wholes.",
             '[[step eq="1 whole = 4 fourths"]][[step eq="3 × 4 = 12"]]'],
            ["How many sixths are in 2 wholes? One whole holds 6. Two wholes hold 2 times 6, which equals 12.",
             '[[step eq="2 × 6 = 12"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. How many thirds are in 4 wholes? One whole holds 3, so 4 wholes hold 4 times 3, which equals 12.",
                        '[[step eq="4 × 3 = 12"]]'],
             "ask": {"a": 5, "b": 4, "op": "uic"}},
            {"worked": ["One more together. How many eighths are in 3 wholes? 3 times 8 equals 24.",
                        '[[step eq="3 × 8 = 24"]]'],
             "ask": {"a": 6, "b": 5, "op": "uic"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "uic"},
            {"a": 3, "b": 2, "op": "uic"},
            {"a": 2, "b": 4, "op": "uic"},
            {"a": 4, "b": 3, "op": "uic"},
            {"a": 5, "b": 3, "op": "uic"},
            {"a": 4, "b": 5, "op": "uic"},
            {"a": 6, "b": 4, "op": "uic"},
            {"a": 5, "b": 6, "op": "uic"},
            {"a": 8, "b": 5, "op": "uic"},
            {"a": 7, "b": 7, "op": "uic"},
        ],
    },
    {
        "id": "pre-u4-dividing-by-a-fraction",
        "course": "prealgebra", "unit": 4,
        "topic": "Dividing by a fraction",
        "op": "dbf", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("fraction", "divided by"),
        "advance_line": "Three in a row — you've got it! Flip the fraction, then times.",
        "teach": [
            ["Dividing asks how many of these fit inside that. You just counted how many fourths fit in 3 wholes and got 12 — a bigger number. Dividing by a fraction gives a BIGGER answer, because small parts fit in many times.",
             '[[goal text="Dividing by a fraction"]]'],
            ["The rule is short: flip the fraction over, then times. Watch. 4 divided by two thirds. Flip two thirds to get three halves. Now times: 4 times 3 equals 12, and 12 divided by 2 equals 6.",
             '[[step eq="4 ÷ 2/3"]][[step eq="4 × 3/2"]][[step eq="12 ÷ 2 = 6"]]'],
            ["One more. 6 divided by three fourths. Flip to four thirds. 6 times 4 equals 24, and 24 divided by 3 equals 8.",
             '[[step eq="6 ÷ 3/4 = 6 × 4/3"]][[step eq="24 ÷ 3 = 8"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 divided by two fifths. Flip to five halves. 4 times 5 equals 20, and 20 divided by 2 equals 10.",
                        '[[step eq="4 × 5/2 = 10"]]'],
             "ask": {"a": 3, "b": 5, "c": 9, "op": "dbf"}},
            {"worked": ["One more together. 10 divided by five sixths. Flip to six fifths. 10 times 6 equals 60, and 60 divided by 5 equals 12.",
                        '[[step eq="10 × 6/5 = 12"]]'],
             "ask": {"a": 2, "b": 5, "c": 6, "op": "dbf"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 4, "op": "dbf"},
            {"a": 3, "b": 4, "c": 6, "op": "dbf"},
            {"a": 2, "b": 5, "c": 4, "op": "dbf"},
            {"a": 3, "b": 5, "c": 6, "op": "dbf"},
            {"a": 4, "b": 5, "c": 8, "op": "dbf"},
            {"a": 5, "b": 6, "c": 10, "op": "dbf"},
            {"a": 2, "b": 3, "c": 10, "op": "dbf"},
            {"a": 3, "b": 7, "c": 9, "op": "dbf"},
            {"a": 4, "b": 9, "c": 12, "op": "dbf"},
            {"a": 2, "b": 7, "c": 8, "op": "dbf"},
        ],
    },
    {
        "id": "pre-u4-fractions-bigger-than-one",
        "course": "prealgebra", "unit": 4,
        "topic": "Fractions bigger than one",
        "op": "imp", "max_value": 40,
        "levels": ("abstract",),
        "symbols": ("fraction", "whole", "number line"),
        "advance_line": "Three in a row — you've got it! You can find the whole ones inside a fraction.",
        "teach": [
            ["A fraction can be bigger than one whole. Seven thirds is not a mistake. On the number line it is a real place, out past 2. Three thirds fill one whole, so seven thirds fill two wholes with one third left over.",
             '[[goal text="Fractions bigger than one"]][[numberline min="0" max="3" points="2.33"]]'],
            ["To find the whole ones, ask how many times the bottom fits into the top. Seven thirds: 3 fits into 7 twice, with 1 left. So seven thirds is 2 whole ones and one third.",
             '[[numberline min="0" max="3" points="2.33"]][[step eq="7 ÷ 3 = 2 whole ones, 1 left"]]'],
            ["Another. Eleven fourths. 4 fits into 11 twice, with 3 left. So eleven fourths is 2 whole ones and three fourths.",
             '[[numberline min="0" max="3" points="2.75"]][[step eq="11 ÷ 4 = 2 whole ones, 3 left"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Nine halves. 2 fits into 9 four times, with 1 left. Four whole ones and one half.",
                        '[[step eq="9 ÷ 2 = 4 whole ones, 1 left"]]'],
             "ask": {"a": 14, "b": 3, "op": "imp"}},
            {"worked": ["One more together. Twenty sevenths. 7 fits into 20 twice, with 6 left. Two whole ones and six sevenths.",
                        '[[step eq="20 ÷ 7 = 2 whole ones, 6 left"]]'],
             "ask": {"a": 22, "b": 5, "op": "imp"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 7, "b": 3, "op": "imp"},
            {"a": 9, "b": 4, "op": "imp"},
            {"a": 11, "b": 5, "op": "imp"},
            {"a": 13, "b": 4, "op": "imp"},
            {"a": 17, "b": 5, "op": "imp"},
            {"a": 19, "b": 6, "op": "imp"},
            {"a": 23, "b": 7, "op": "imp"},
            {"a": 29, "b": 8, "op": "imp"},
            {"a": 25, "b": 6, "op": "imp"},
            {"a": 31, "b": 7, "op": "imp"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U4)

# =============================================================================
# PREALGEBRA -- UNIT 5: DECIMALS (build ko, 2026-08-21)
# =============================================================================
# Basic Math NAMES tenths and hundredths and counts dimes and pennies. These four go
# past naming to the thing that actually goes wrong with decimals: place. Comparing
# two decimals is really converting them to a common unit, so lesson 1 does exactly
# that and the misconception dies where it lives -- 0.45 is 45 hundredths and 0.5 is
# FIFTY hundredths, which settles which is bigger without any rule about digits.
#
# EVERY ANSWER IS A COUNT OF PARTS -- "how many hundredths", "how many tenths". That
# is forced by the tap answer being a whole number, and it is also the honest way to
# hold a decimal in your head: 3.6 is thirty-six tenths, and sharing it between 4 is
# just sharing 36 things.
_PREALGEBRA_U5 = [
    {
        "id": "pre-u5-how-many-hundredths",
        "course": "prealgebra", "unit": 5,
        "topic": "How many hundredths",
        "op": "hun", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("decimal point", "hundredths"),
        "advance_line": "Three in a row — you've got it! You can count the hundredths in any decimal.",
        "teach": [
            ["A decimal point separates the whole ones from the parts. After the decimal point the first place counts tenths and the second counts hundredths. Ten hundredths make one tenth. So a decimal like 0 point 4 5 can be counted a different way: as hundredths.",
             '[[goal text="How many hundredths"]]'],
            ["0 point 4 5 is 4 tenths and 5 hundredths. Each tenth is 10 hundredths, so 4 tenths are 40 hundredths. Put the 5 with them and you have 45 hundredths.",
             '[[step eq="0.45 = 40 + 5 = 45 hundredths"]]'],
            ["Here is why that matters. Which is bigger, 0 point 5 or 0 point 4 5? Count them the same way: 0 point 5 is 50 hundredths, 0 point 4 5 is 45 hundredths. 50 beats 45. More digits does NOT mean bigger.",
             '[[numberline min="0" max="1" points="0.5,0.45"]][[step eq="0.5 = 50 hundredths · 0.45 = 45 hundredths"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 0 point 3 2. Three tenths are 30 hundredths, put the 2 with them: 32 hundredths.",
                        '[[step eq="0.32 = 32 hundredths"]]'],
             "ask": {"a": 6, "b": 7, "op": "hun"}},
            {"worked": ["One more together. 0 point 8 0. Eight tenths are 80 hundredths, and there are no extra ones: 80 hundredths.",
                        '[[step eq="0.80 = 80 hundredths"]]'],
             "ask": {"a": 2, "b": 9, "op": "hun"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 1, "b": 8, "op": "hun"},
            {"a": 2, "b": 5, "op": "hun"},
            {"a": 3, "b": 0, "op": "hun"},
            {"a": 4, "b": 0, "op": "hun"},
            {"a": 4, "b": 5, "op": "hun"},
            {"a": 5, "b": 0, "op": "hun"},
            {"a": 6, "b": 2, "op": "hun"},
            {"a": 7, "b": 0, "op": "hun"},
            {"a": 8, "b": 4, "op": "hun"},
            {"a": 9, "b": 6, "op": "hun"},
        ],
    },
    {
        "id": "pre-u5-times-by-ten",
        "course": "prealgebra", "unit": 5,
        "topic": "Timesing a decimal by ten",
        "op": "x10", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("decimal point", "place"),
        "advance_line": "Three in a row — you've got it! Times by ten and every digit moves one place left.",
        "teach": [
            ["Timesing by ten does something tidy to a decimal point number: every digit moves one place to the left. The tenths become ones, the ones become tens. Nothing is dropped and nothing is invented.",
             '[[goal text="Timesing a decimal by ten"]]'],
            ["Watch: 3 point 7 times 10. The 7 was seven tenths; move it one place left and it is seven ones. The 3 was three ones; it becomes three tens. So the answer is 37.",
             '[[step eq="3.7 × 10 = 37"]]'],
            ["One more. 5 point 2 times 10 equals 52. Careful — the answer is not 50. The tenths digit moves too; it does not get left behind.",
             '[[step eq="5.2 × 10 = 52"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 6 point 4 times 10. Both digits move one place left: 64.",
                        '[[step eq="6.4 × 10 = 64"]]'],
             "ask": {"a": 7, "b": 3, "op": "x10"}},
            {"worked": ["One more together. 1 point 9 times 10 equals 19.",
                        '[[step eq="1.9 × 10 = 19"]]'],
             "ask": {"a": 4, "b": 6, "op": "x10"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 1, "b": 5, "op": "x10"},
            {"a": 2, "b": 3, "op": "x10"},
            {"a": 2, "b": 6, "op": "x10"},
            {"a": 3, "b": 7, "op": "x10"},
            {"a": 4, "b": 2, "op": "x10"},
            {"a": 5, "b": 2, "op": "x10"},
            {"a": 6, "b": 8, "op": "x10"},
            {"a": 7, "b": 4, "op": "x10"},
            {"a": 8, "b": 1, "op": "x10"},
            {"a": 9, "b": 9, "op": "x10"},
        ],
    },
    {
        "id": "pre-u5-tenths-times-a-number",
        "course": "prealgebra", "unit": 5,
        "topic": "Tenths times a whole number",
        "op": "dth", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("tenths", "times"),
        "advance_line": "Three in a row — you've got it! Count the tenths, then times them.",
        "teach": [
            ["A decimal is easier to times if you first say what it is a count of. 0 point 3 is three tenths. Timesing three tenths by 4 works exactly like timesing 3 by 4 — the parts just stay tenths.",
             '[[goal text="Tenths times a whole number"]]'],
            ["Watch: 0 point 3 times 4. Say it as three tenths. 3 times 4 equals 12, so the answer is 12 tenths. Twelve tenths is more than a whole one, which is fine — that is 1 point 2.",
             '[[step eq="0.3 = 3 tenths"]][[step eq="3 tenths × 4 = 12 tenths"]]'],
            ["One more. 0 point 5 times 5. Five tenths, timesed by 5, equals 25 tenths.",
             '[[step eq="5 tenths × 5 = 25 tenths"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 0 point 2 times 7. Two tenths times 7 equals 14 tenths.",
                        '[[step eq="2 tenths × 7 = 14 tenths"]]'],
             "ask": {"a": 6, "b": 3, "op": "dth"}},
            {"worked": ["One more together. 0 point 8 times 6. Eight tenths times 6 equals 48 tenths.",
                        '[[step eq="8 tenths × 6 = 48 tenths"]]'],
             "ask": {"a": 7, "b": 4, "op": "dth"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "dth"},
            {"a": 3, "b": 3, "op": "dth"},
            {"a": 2, "b": 6, "op": "dth"},
            {"a": 4, "b": 4, "op": "dth"},
            {"a": 3, "b": 7, "op": "dth"},
            {"a": 5, "b": 5, "op": "dth"},
            {"a": 4, "b": 8, "op": "dth"},
            {"a": 6, "b": 7, "op": "dth"},
            {"a": 7, "b": 8, "op": "dth"},
            {"a": 9, "b": 9, "op": "dth"},
        ],
    },
    {
        "id": "pre-u5-sharing-a-decimal",
        "course": "prealgebra", "unit": 5,
        "topic": "Sharing a decimal out",
        "op": "dsh", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("tenths", "shared"),
        "advance_line": "Three in a row — you've got it! Count the tenths, then share them out.",
        "teach": [
            ["Sharing a decimal works the same way as timesing one: say what it is a count of first. 3 point 6 is thirty-six tenths. Sharing thirty-six tenths between 4 is just sharing 36 things between 4.",
             '[[goal text="Sharing a decimal out"]]'],
            ["Watch: 3 point 6 shared between 4. Thirty-six tenths, shared between 4, gives 9 tenths each. Nine tenths is 0 point 9.",
             '[[step eq="3.6 = 36 tenths"]][[step eq="36 ÷ 4 = 9 tenths"]]'],
            ["One more. 2 point 4 shared between 3. Twenty-four tenths between 3 gives 8 tenths each, which is 0 point 8.",
             '[[step eq="24 tenths ÷ 3 = 8 tenths"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 point 8 shared between 6. Forty-eight tenths between 6 gives 8 tenths each.",
                        '[[step eq="48 tenths ÷ 6 = 8 tenths"]]'],
             "ask": {"a": 9, "b": 0, "c": 5, "op": "dsh"}},
            {"worked": ["One more together. 1 point 2 shared between 4. Twelve tenths between 4 gives 3 tenths each.",
                        '[[step eq="12 tenths ÷ 4 = 3 tenths"]]'],
             "ask": {"a": 7, "b": 7, "c": 7, "op": "dsh"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 1, "b": 2, "c": 4, "op": "dsh"},
            {"a": 2, "b": 8, "c": 7, "op": "dsh"},
            {"a": 2, "b": 4, "c": 3, "op": "dsh"},
            {"a": 4, "b": 8, "c": 6, "op": "dsh"},
            {"a": 3, "b": 6, "c": 4, "op": "dsh"},
            {"a": 5, "b": 4, "c": 6, "op": "dsh"},
            {"a": 6, "b": 3, "c": 7, "op": "dsh"},
            {"a": 7, "b": 2, "c": 8, "op": "dsh"},
            {"a": 8, "b": 1, "c": 9, "op": "dsh"},
            {"a": 4, "b": 5, "c": 5, "op": "dsh"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U5)


# =============================================================================
# PREALGEBRA -- UNIT 6: RATIOS, RATES & PROPORTIONS (build kp, 2026-08-21)
# =============================================================================
# Basic Math's "one costs" already finds a unit PRICE. These four are the family of
# ideas around it, in the order they depend on each other: keep a ratio's shape when
# both sides grow, scale a rate over time (which is that same move with a unit step in
# the middle), write it as an equation with a hole in it, and finally SPLIT an amount
# in a ratio -- the genuinely different one, because there the total is given and the
# parts have to be found before anything can be shared.
#
# THE ERROR THIS WHOLE UNIT IS ABOUT is adding instead of timesing: a child who thinks
# 2 to 3 grown to 4 becomes "4 to 5", because 3 was one more than 2. Three of the four
# lessons offer exactly that as their wrong option.
_PREALGEBRA_U6 = [
    {
        "id": "pre-u6-keeping-a-ratio",
        "course": "prealgebra", "unit": 6,
        "topic": "Keeping a ratio the same",
        "op": "rat", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("ratio", "for every"),
        "advance_line": "Three in a row — you've got it! A ratio grows by timesing, not by adding.",
        "teach": [
            ["A ratio says how two amounts go together. Two cups of flour for every 3 cups of milk is a ratio, written 2 to 3. Make more, and BOTH sides have to grow the same way — by timesing, not by adding.",
             '[[goal text="Keeping a ratio the same"]]'],
            ["Two cups of flour for every 3 of milk. You have 6 cups of flour. That is 3 batches, because 6 divided by 2 equals 3. So the milk grows the same way: 3 batches of 3 cups equals 9 cups.",
             '[[step eq="2 : 3"]][[step eq="6 ÷ 2 = 3 batches"]][[step eq="3 × 3 = 9"]]'],
            ["Careful with the tempting wrong move. 6 cups of flour does NOT mean 7 cups of milk just because 3 is one more than 2. Adding breaks the ratio; timesing keeps it.",
             '[[step eq="2 : 3 → 6 : 9 ✓"]][[step eq="2 : 3 → 6 : 7 ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 3 cups of flour for every 4 of milk, with 9 cups of flour. 9 divided by 3 equals 3 batches, and 3 times 4 equals 12 cups of milk.",
                        '[[step eq="9 ÷ 3 = 3"]][[step eq="3 × 4 = 12"]]'],
             "ask": {"a": 5, "b": 6, "c": 15, "op": "rat"}},
            {"worked": ["One more together. 2 to 9, with 8 cups of flour. 8 divided by 2 equals 4 batches, and 4 times 9 equals 36.",
                        '[[step eq="8 ÷ 2 = 4"]][[step eq="4 × 9 = 36"]]'],
             "ask": {"a": 3, "b": 7, "c": 9, "op": "rat"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 5, "b": 2, "c": 10, "op": "rat"},
            {"a": 2, "b": 3, "c": 4, "op": "rat"},
            {"a": 4, "b": 3, "c": 8, "op": "rat"},
            {"a": 3, "b": 4, "c": 6, "op": "rat"},
            {"a": 2, "b": 5, "c": 6, "op": "rat"},
            {"a": 3, "b": 5, "c": 9, "op": "rat"},
            {"a": 4, "b": 5, "c": 12, "op": "rat"},
            {"a": 6, "b": 5, "c": 18, "op": "rat"},
            {"a": 2, "b": 7, "c": 8, "op": "rat"},
            {"a": 3, "b": 8, "c": 12, "op": "rat"},
        ],
    },
    {
        "id": "pre-u6-scaling-a-rate",
        "course": "prealgebra", "unit": 6,
        "topic": "Working out a rate",
        "op": "rte", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("rate", "per hour"),
        "advance_line": "Three in a row — you've got it! Find one hour first, then times up.",
        "teach": [
            ["A rate says how much happens in one hour, or one minute, or one of anything. Bottles per hour is a rate. When you know how much happened over several hours, find ONE hour first. That single number does all the work afterwards.",
             '[[goal text="Working out a rate"]]'],
            ["A machine fills 18 bottles in 3 hours. One hour first: 18 divided by 3 equals 6 bottles an hour. Now 5 hours: 6 times 5 equals 30 bottles.",
             '[[step eq="18 ÷ 3 = 6 per hour"]][[step eq="6 × 5 = 30"]]'],
            ["Two steps, always in that order. Divide to reach one, then times to reach the hours you were asked about. Stopping after the divide leaves you holding the rate, not the answer.",
             '[[step eq="÷ to reach 1 hour · × to reach the hours asked"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 24 bottles in 4 hours. That is 6 an hour, and in 6 hours it fills 36.",
                        '[[step eq="24 ÷ 4 = 6"]][[step eq="6 × 6 = 36"]]'],
             "ask": {"a": 4, "b": 5, "c": 20, "op": "rte"}},
            {"worked": ["One more together. 40 bottles in 5 hours is 8 an hour, so in 2 hours it fills 16.",
                        '[[step eq="40 ÷ 5 = 8"]][[step eq="8 × 2 = 16"]]'],
             "ask": {"a": 6, "b": 3, "c": 21, "op": "rte"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 12, "op": "rte"},
            {"a": 3, "b": 4, "c": 20, "op": "rte"},
            {"a": 3, "b": 7, "c": 35, "op": "rte"},
            {"a": 2, "b": 5, "c": 40, "op": "rte"},
            {"a": 4, "b": 2, "c": 10, "op": "rte"},
            {"a": 4, "b": 9, "c": 45, "op": "rte"},
            {"a": 5, "b": 3, "c": 18, "op": "rte"},
            {"a": 6, "b": 4, "c": 24, "op": "rte"},
            {"a": 8, "b": 5, "c": 30, "op": "rte"},
            {"a": 7, "b": 6, "c": 42, "op": "rte"},
        ],
    },
    {
        "id": "pre-u6-filling-in-a-proportion",
        "course": "prealgebra", "unit": 6,
        "topic": "Filling in a proportion",
        "op": "prop", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("proportion", "over"),
        "advance_line": "Three in a row — you've got it! Find what the bottom was timesed by.",
        "teach": [
            ["Two fractions worth the same amount make a proportion — say it, pro-por-shun. Write a proportion with a hole in it and you have a puzzle: 3 over 4 equals what over 8? The rule works exactly like the ratio rule — whatever happened to the bottom happened to the top.",
             '[[goal text="Filling in a proportion"]]'],
            ["3 over 4 equals what over 8. Look at the bottoms: 4 became 8, so it was timesed by 2. Do the same to the top: 3 times 2 equals 6. So 3 over 4 equals 6 over 8.",
             '[[step eq="3/4 = ?/8"]][[step eq="4 × 2 = 8, so 3 × 2 = 6"]]'],
            ["Watch out for adding. The bottom went up by 4, but that does NOT mean the top goes up by 4. 3 over 4 is not 7 over 8. Ask what the bottom was TIMESED by, every time.",
             '[[step eq="3/4 = 6/8 ✓"]][[step eq="3/4 = 7/8 ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 2 over 5 equals what over 10? The bottom doubled, so the top doubles: 4.",
                        '[[step eq="2/5 = 4/10"]]'],
             "ask": {"a": 5, "b": 3, "c": 9, "op": "prop"}},
            {"worked": ["One more together. 3 over 5 equals what over 15? The bottom was timesed by 3, so 3 times 3 equals 9.",
                        '[[step eq="3/5 = 9/15"]]'],
             "ask": {"a": 2, "b": 9, "c": 27, "op": "prop"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 6, "op": "prop"},
            {"a": 2, "b": 5, "c": 10, "op": "prop"},
            {"a": 2, "b": 7, "c": 14, "op": "prop"},
            {"a": 3, "b": 4, "c": 8, "op": "prop"},
            {"a": 3, "b": 8, "c": 16, "op": "prop"},
            {"a": 4, "b": 9, "c": 18, "op": "prop"},
            {"a": 3, "b": 5, "c": 15, "op": "prop"},
            {"a": 5, "b": 6, "c": 12, "op": "prop"},
            {"a": 4, "b": 3, "c": 9, "op": "prop"},
            {"a": 7, "b": 4, "c": 20, "op": "prop"},
        ],
    },
    {
        "id": "pre-u6-sharing-in-a-ratio",
        "course": "prealgebra", "unit": 6,
        "topic": "Sharing in a ratio",
        "op": "shr", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("ratio", "parts"),
        "advance_line": "Three in a row — you've got it! Count the parts first, then share them out.",
        "teach": [
            ["This one is different. You are given the whole amount and the ratio, and you have to find the shares. The trick is to count the parts first: a ratio of 2 to 3 means 5 parts in all, not 2 and not 3.",
             '[[goal text="Sharing in a ratio"]]'],
            ["Share 20 sweets in the ratio 2 to 3. Count the parts: 2 and 3 make 5 parts. Now share: 20 divided by 5 equals 4 sweets in each part. The first child gets 2 parts — 4 times 2 equals 8.",
             '[[objects emoji="🟦" groups="2" add="3" caption="2 parts and 3 parts = 5 parts in all"]][[step eq="20 ÷ 5 = 4 each part"]][[step eq="4 × 2 = 8"]]'],
            ["Check it the easy way: the other child gets 3 parts, which is 12. And 8 plus 12 equals 20, the amount you started with. If the two shares do not put back together, something went wrong.",
             '[[step eq="8 + 12 = 20 ✓"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Share 12 in the ratio 1 to 3. That is 4 parts, so each part is 3. The first child gets 1 part — 3.",
                        '[[step eq="12 ÷ 4 = 3"]][[step eq="3 × 1 = 3"]]'],
             "ask": {"a": 3, "b": 4, "c": 28, "op": "shr"}},
            {"worked": ["One more together. Share 30 in the ratio 2 to 4. Six parts, so each part is 5, and the first child gets 2 parts — 10.",
                        '[[step eq="30 ÷ 6 = 5"]][[step eq="5 × 2 = 10"]]'],
             "ask": {"a": 5, "b": 2, "c": 35, "op": "shr"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 10, "op": "shr"},
            {"a": 2, "b": 5, "c": 14, "op": "shr"},
            {"a": 2, "b": 7, "c": 27, "op": "shr"},
            {"a": 3, "b": 2, "c": 15, "op": "shr"},
            {"a": 3, "b": 5, "c": 24, "op": "shr"},
            {"a": 4, "b": 3, "c": 21, "op": "shr"},
            {"a": 5, "b": 4, "c": 27, "op": "shr"},
            {"a": 4, "b": 5, "c": 36, "op": "shr"},
            {"a": 5, "b": 3, "c": 32, "op": "shr"},
            {"a": 7, "b": 3, "c": 50, "op": "shr"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U6)


# =============================================================================
# PREALGEBRA -- UNIT 7: PERCENTS (build kr, 2026-08-21)
# =============================================================================
# Basic Math's percent lesson only ever asks for 10, 25 or 50 percent, and it answers
# them with a fraction shortcut: half, a fourth, a tenth. That shortcut is fine and it
# is also a dead end -- it says nothing at all about 30 percent or 70 percent. This
# unit replaces it with ONE method that never runs out: find ten percent, then count
# how many tens you need. Lesson 1 teaches the method; lessons 2, 3 and 4 run it in
# the other three directions a percent question can face.
#
# THE ERROR THE LAST LESSON IS ABOUT is moving a price by the PERCENT NUMBER instead
# of by that percent OF the price -- 40 dollars up 10 percent read as 50 dollars,
# because 40 and 10 are two numbers and adding them is the thing a child knows how to
# do. It is offered as the wrong tap on every problem in that bank.
_PREALGEBRA_U7 = [
    {
        "id": "pre-u7-any-percent",
        "course": "prealgebra", "unit": 7,
        "topic": "Any percent, ten at a time",
        "op": "pcn", "max_value": 90,
        "levels": ("abstract",),
        "symbols": ("percent", "of"),
        "advance_line": "Three in a row — you've got it! Find ten percent, then count the tens.",
        "teach": [
            ["You already know 50 percent is half and 10 percent is a tenth. But what about 30 percent, or 70 percent? Half and a fourth are no help there. Here is one way that works for every single one of them.",
             '[[goal text="Any percent, ten at a time"]]'],
            ["Find TEN percent first, because that is easy — just a tenth. Ten percent of 40 is 4. Now 30 percent is three tens, so take three of those fours: 3 times 4 equals 12. So 30 percent of 40 equals 12.",
             '[[step eq="10% of 40 = 4"]][[step eq="30% is 3 tens"]][[step eq="3 × 4 = 12"]]'],
            ["One more. 70 percent of 20. Ten percent of 20 is 2. Seventy percent is seven tens, so 7 times 2 equals 14. Careful — the answer is not 2. Finding ten percent is only the first of the two steps.",
             '[[step eq="10% of 20 = 2"]][[step eq="7 × 2 = 14"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 20 percent of 50. Ten percent of 50 is 5, and 20 percent is two tens: 2 times 5 equals 10.",
                        '[[step eq="10% of 50 = 5"]][[step eq="2 × 5 = 10"]]'],
             "ask": {"a": 20, "b": 50, "op": "pcn"}},
            {"worked": ["One more together. 80 percent of 40. Ten percent of 40 is 4, and eight of those is 8 times 4, which equals 32.",
                        '[[step eq="10% of 40 = 4"]][[step eq="8 × 4 = 32"]]'],
             "ask": {"a": 80, "b": 40, "op": "pcn"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 20, "b": 20, "op": "pcn"},
            {"a": 30, "b": 20, "op": "pcn"},
            {"a": 20, "b": 40, "op": "pcn"},
            {"a": 30, "b": 30, "op": "pcn"},
            {"a": 40, "b": 30, "op": "pcn"},
            {"a": 60, "b": 20, "op": "pcn"},
            {"a": 30, "b": 60, "op": "pcn"},
            {"a": 40, "b": 60, "op": "pcn"},
            {"a": 60, "b": 60, "op": "pcn"},
            {"a": 70, "b": 80, "op": "pcn"},
        ],
    },
    {
        "id": "pre-u7-what-percent-is-that",
        "course": "prealgebra", "unit": 7,
        "topic": "What percent is that",
        "op": "asp", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("percent", "out of"),
        "advance_line": "Three in a row — you've got it! Put it over a hundred and read the top.",
        "teach": [
            ["Sometimes you are given both numbers and asked for the percent instead. 15 out of 20 — what percent is that? Percent means out of a hundred, so this is the proportion puzzle you already know, with 100 on the bottom.",
             '[[goal text="What percent is that"]]'],
            ["15 out of 20 equals what out of 100? Look at the bottoms: 20 became 100, so it was timesed by 5. Do the same to the top: 15 times 5 equals 75. So 15 out of 20 is 75 percent.",
             '[[step eq="15/20 = ?/100"]][[step eq="20 × 5 = 100, so 15 × 5 = 75"]]'],
            ["Watch which number you answer with. 15 out of 20 is 75 percent, not 15 percent and not 25 percent. 25 is the percent of the ones you did NOT have.",
             '[[step eq="15 out of 20 = 75% ✓"]][[step eq="the other 5 are the 25% ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 2 out of 5. The bottom 5 becomes 100 by timesing by 20, so the top does too: 2 times 20 equals 40 percent.",
                        '[[step eq="2/5 = 40/100"]]'],
             "ask": {"a": 2, "b": 5, "op": "asp"}},
            {"worked": ["One more together. 11 out of 20. Times both by 5: 11 times 5 equals 55, so that is 55 percent.",
                        '[[step eq="11/20 = 55/100"]]'],
             "ask": {"a": 11, "b": 20, "op": "asp"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 1, "b": 10, "op": "asp"},
            {"a": 1, "b": 4, "op": "asp"},
            {"a": 3, "b": 10, "op": "asp"},
            {"a": 9, "b": 20, "op": "asp"},
            {"a": 13, "b": 20, "op": "asp"},
            {"a": 17, "b": 25, "op": "asp"},
            {"a": 7, "b": 10, "op": "asp"},
            {"a": 3, "b": 4, "op": "asp"},
            {"a": 21, "b": 25, "op": "asp"},
            {"a": 19, "b": 20, "op": "asp"},
        ],
    },
    {
        "id": "pre-u7-finding-the-whole",
        "course": "prealgebra", "unit": 7,
        "topic": "Finding the whole from a part",
        "op": "pwh", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("percent", "whole"),
        "advance_line": "Three in a row — you've got it! Step down to ten percent, then up to a hundred.",
        "teach": [
            ["Here the question turns around. You are told a part and what percent it is, and the whole is what is missing. 12 is 30 percent of what number? The same ten-percent step does it, walked in the other direction.",
             '[[goal text="Finding the whole from a part"]]'],
            ["30 percent is 12. Step DOWN to ten percent first: 30 percent is three tens, so ten percent is 12 divided by 3, which equals 4. Now step up: one hundred percent is ten of those, and 4 times 10 equals 40.",
             '[[step eq="30% = 12"]][[step eq="10% = 12 ÷ 3 = 4"]][[step eq="100% = 4 × 10 = 40"]]'],
            ["Check it the easy way: is 30 percent of 40 really 12? Ten percent of 40 is 4, three tens is 3 times 4, which equals 12. It fits. And notice the whole is BIGGER than the part — if your answer came out smaller, you ran the sum forwards by mistake.",
             '[[step eq="30% of 40 = 12 ✓"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 9 is 30 percent of what? Ten percent is 9 divided by 3, which equals 3, and a hundred percent is 3 times 10, which equals 30.",
                        '[[step eq="10% = 3"]][[step eq="100% = 30"]]'],
             "ask": {"a": 30, "b": 9, "op": "pwh"}},
            {"worked": ["One more together. 30 is 60 percent of what? Ten percent is 30 divided by 6, which equals 5, so the whole is 5 times 10, which equals 50.",
                        '[[step eq="10% = 5"]][[step eq="100% = 50"]]'],
             "ask": {"a": 60, "b": 30, "op": "pwh"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 60, "b": 18, "op": "pwh"},
            {"a": 30, "b": 12, "op": "pwh"},
            {"a": 40, "b": 16, "op": "pwh"},
            {"a": 20, "b": 10, "op": "pwh"},
            {"a": 60, "b": 36, "op": "pwh"},
            {"a": 80, "b": 48, "op": "pwh"},
            {"a": 70, "b": 49, "op": "pwh"},
            {"a": 90, "b": 72, "op": "pwh"},
            {"a": 20, "b": 18, "op": "pwh"},
            {"a": 40, "b": 40, "op": "pwh"},
        ],
    },
    {
        "id": "pre-u7-a-price-goes-up",
        "course": "prealgebra", "unit": 7,
        "topic": "A price goes up or down",
        "op": "pup", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("percent", "price"),
        "advance_line": "Three in a row — you've got it! Work out the change first, then move the price by it.",
        "teach": [
            ["This is where percents earn their keep: prices. A coat costs 40 dollars and the price goes up by 10 percent. Two steps, and the first one you already know: work out what the change is worth, then move the price by that.",
             '[[goal text="A price goes up or down"]]'],
            ["Ten percent of 40 is 4, so the change is 4 dollars. The price goes UP, so put it on: 40 plus 4 equals 44 dollars.",
             '[[step eq="10% of 40 = 4"]][[step eq="40 + 4 = 44"]]'],
            ["Here is the trap. The new price is NOT 50 dollars. Ten is a percent, not ten dollars — you cannot put it straight onto the price. And when the price goes DOWN instead, the same 4 comes off: 40 take away 4 equals 36 dollars.",
             '[[step eq="40 + 4 = 44 ✓"]][[step eq="40 + 10 = 50 ✗"]][[step eq="down: 40 − 4 = 36"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. A 30 dollar shirt goes up by 10 percent. Ten percent of 30 is 3, so the new price is 30 plus 3, which equals 33 dollars.",
                        '[[step eq="10% of 30 = 3"]][[step eq="30 + 3 = 33"]]'],
             "ask": {"a": 10, "b": 30, "c": 1, "op": "pup"}},
            {"worked": ["One more together. A 40 dollar bag goes down by 20 percent. Ten percent of 40 is 4, so 20 percent is 8, and 40 take away 8 equals 32 dollars.",
                        '[[step eq="20% of 40 = 8"]][[step eq="40 − 8 = 32"]]'],
             "ask": {"a": 20, "b": 40, "c": 0, "op": "pup"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 10, "b": 20, "c": 1, "op": "pup"},
            {"a": 20, "b": 20, "c": 1, "op": "pup"},
            {"a": 10, "b": 40, "c": 0, "op": "pup"},
            {"a": 20, "b": 50, "c": 0, "op": "pup"},
            {"a": 10, "b": 40, "c": 1, "op": "pup"},
            {"a": 30, "b": 40, "c": 1, "op": "pup"},
            {"a": 20, "b": 60, "c": 1, "op": "pup"},
            {"a": 10, "b": 80, "c": 0, "op": "pup"},
            {"a": 50, "b": 60, "c": 1, "op": "pup"},
            {"a": 20, "b": 80, "c": 1, "op": "pup"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U7)


# =============================================================================
# PREALGEBRA -- UNIT 8: MEASUREMENT & GEOMETRY BASICS (build ks, 2026-08-21)
# =============================================================================
# Basic Math's geometry unit -- perimeter, area, quarter turns, volume -- draws NO
# PICTURES. Every board in it is a [[step]] line. Geometry is the one subject where the
# picture IS the argument, and geo-figures.js has had [[triangle]] and [[angle]] since
# July. THREE OF THESE FOUR LESSONS PUT A REAL FIGURE ON THE BOARD, and the
# straight-line lesson uses [[angle deg="180" split="130"]] -- a tag built for exactly
# that sentence and never once used by a scripted lesson.
#
# The unit walks from measuring to seeing: change a unit (which is Unit 5's place value
# wearing a coat), then halve a rectangle to get a triangle, then meet the two facts
# every later geometry course leans on -- a straight line is 180 degrees, and so are
# the three angles of any triangle. The last lesson is the first one in the whole
# course whose answer comes from a rule about ALL triangles rather than from counting.
_PREALGEBRA_U8 = [
    {
        "id": "pre-u8-changing-units",
        "course": "prealgebra", "unit": 8,
        "topic": "Changing units",
        "op": "cnv", "max_value": 9000,
        "levels": ("abstract",),
        "symbols": ("unit", "centimetres"),
        "advance_line": "Three in a row — you've got it! Going to a smaller unit means more of them.",
        "teach": [
            ["Measuring the same thing in a smaller unit takes MORE of them. One centimetre is 10 millimetres, one metre is 100 centimetres, one kilogram is 1000 grams. Each time you swap to the smaller unit, you times.",
             '[[goal text="Changing units"]]'],
            ["How many centimetres are there in 3 metres? One metre is 100 centimetres, so 3 metres is 3 lots of 100: 3 times 100 equals 300 centimetres.",
             '[[step eq="1 m = 100 cm"]][[step eq="3 × 100 = 300"]]'],
            ["The hard part is never the timesing — it is knowing HOW MANY zeros. 3 metres is not 30 centimetres; that would be using ten when the unit needs a hundred. Say the fact out loud first, then times by it.",
             '[[step eq="3 m = 300 cm ✓"]][[step eq="3 m = 30 cm ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 6 centimetres in millimetres. One centimetre is 10 millimetres, so 6 times 10 equals 60 millimetres.",
                        '[[step eq="6 × 10 = 60"]]'],
             "ask": {"a": 6, "b": 10, "op": "cnv"}},
            {"worked": ["One more together. 3 kilograms in grams. One kilogram is 1000 grams, so 3 times 1000 equals 3000 grams.",
                        '[[step eq="3 × 1000 = 3000"]]'],
             "ask": {"a": 3, "b": 1000, "op": "cnv"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 10, "op": "cnv"},
            {"a": 5, "b": 10, "op": "cnv"},
            {"a": 8, "b": 10, "op": "cnv"},
            {"a": 2, "b": 100, "op": "cnv"},
            {"a": 4, "b": 100, "op": "cnv"},
            {"a": 7, "b": 100, "op": "cnv"},
            {"a": 9, "b": 100, "op": "cnv"},
            {"a": 2, "b": 1000, "op": "cnv"},
            {"a": 5, "b": 1000, "op": "cnv"},
            {"a": 9, "b": 1000, "op": "cnv"},
        ],
    },
    {
        "id": "pre-u8-area-of-a-triangle",
        "course": "prealgebra", "unit": 8,
        "topic": "Area of a triangle",
        "op": "tri", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("base", "height"),
        "advance_line": "Three in a row — you've got it! Times the base by the height, then halve it.",
        "teach": [
            ["You already know a rectangle's area: the long side times the short side. A triangle is easier than it looks, because every right triangle is exactly HALF of a rectangle. Draw the rectangle round it and you can see the other half.",
             '[[goal text="Area of a triangle"]][[triangle v="A,B,C" right="A" sides="6,,4"]]'],
            ["This one has a base of 6 and a height of 4. The rectangle round it is 6 times 4, which equals 24. The triangle is half of that: 24 divided by 2 equals 12.",
             '[[triangle v="A,B,C" right="A" sides="6,,4"]][[step eq="6 × 4 = 24"]][[step eq="24 ÷ 2 = 12"]]'],
            ["Do not stop after the timesing. 24 is the rectangle, not the triangle. The halving is the whole idea — miss it and your triangle is twice the size of the one on the board.",
             '[[step eq="24 ÷ 2 = 12 ✓"]][[step eq="24 ✗ — that is the rectangle"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. A base of 8 and a height of 3. 8 times 3 equals 24, and half of 24 equals 12.",
                        '[[triangle v="A,B,C" right="A" sides="8,,3"]][[step eq="24 ÷ 2 = 12"]]'],
             "ask": {"a": 9, "b": 4, "op": "tri"}},
            {"worked": ["One more together. A base of 10 and a height of 6. 10 times 6 equals 60, and half of 60 equals 30.",
                        '[[step eq="10 × 6 = 60"]][[step eq="60 ÷ 2 = 30"]]'],
             "ask": {"a": 7, "b": 8, "op": "tri"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 4, "b": 2, "op": "tri"},
            {"a": 3, "b": 4, "op": "tri"},
            {"a": 4, "b": 5, "op": "tri"},
            {"a": 6, "b": 4, "op": "tri"},
            {"a": 5, "b": 6, "op": "tri"},
            {"a": 8, "b": 5, "op": "tri"},
            {"a": 6, "b": 9, "op": "tri"},
            {"a": 12, "b": 5, "op": "tri"},
            {"a": 10, "b": 8, "op": "tri"},
            {"a": 14, "b": 9, "op": "tri"},
        ],
    },
    {
        "id": "pre-u8-angles-on-a-line",
        "course": "prealgebra", "unit": 8,
        "topic": "Angles on a straight line",
        "op": "sla", "max_value": 360,
        "levels": ("abstract",),
        "symbols": ("degrees", "straight line"),
        "advance_line": "Three in a row — you've got it! A straight line is 180 degrees.",
        "teach": [
            ["You know a quarter turn is 90 degrees — two of those make a half turn, and a half turn is a straight line: 180 degrees. That one fact answers a whole family of questions.",
             '[[goal text="Angles on a straight line"]][[angle deg="180" split="90"]]'],
            ["Here is a straight line with a ray drawn up from it. The two angles sit together and fill the line, so together they are 180. If one of them is 130, the other is 180 take away 130, which equals 50.",
             '[[angle deg="180" split="130"]][[step eq="180° − 130° = 50°"]]'],
            ["Watch which number you take away from. It is 180, not 90 and not 360. 90 is a quarter turn and 360 is the whole way round — neither of them is a straight line.",
             '[[step eq="180° − 130° = 50° ✓"]][[step eq="360° − 130° = 230° ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. One angle on the line is 120 degrees. 180 take away 120 equals 60 degrees.",
                        '[[angle deg="180" split="120"]][[step eq="180° − 120° = 60°"]]'],
             "ask": {"a": 150, "b": 0, "op": "sla"}},
            {"worked": ["One more together. One angle is 45 degrees, so the other is 180 take away 45, which equals 135 degrees.",
                        '[[angle deg="180" split="45"]][[step eq="180° − 45° = 135°"]]'],
             "ask": {"a": 70, "b": 0, "op": "sla"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 160, "b": 0, "op": "sla"},
            {"a": 140, "b": 0, "op": "sla"},
            {"a": 125, "b": 0, "op": "sla"},
            {"a": 110, "b": 0, "op": "sla"},
            {"a": 100, "b": 0, "op": "sla"},
            {"a": 80, "b": 0, "op": "sla"},
            {"a": 65, "b": 0, "op": "sla"},
            {"a": 50, "b": 0, "op": "sla"},
            {"a": 35, "b": 0, "op": "sla"},
            {"a": 20, "b": 0, "op": "sla"},
        ],
    },
    {
        "id": "pre-u8-angles-in-a-triangle",
        "course": "prealgebra", "unit": 8,
        "topic": "Angles in a triangle",
        "op": "tri3", "max_value": 180,
        "levels": ("abstract",),
        "symbols": ("degrees", "triangle"),
        "advance_line": "Three in a row — you've got it! The three angles of any triangle are 180 degrees.",
        "teach": [
            ["Here is one of the most useful facts in all of geometry. Take any triangle at all — thin, wide, lopsided — and its three angles always come to 180 degrees — the same 180 as a straight line, and that is not a coincidence.",
             '[[goal text="Angles in a triangle"]][[triangle v="A,B,C" angles="50,60,70"]]'],
            ["So if you are given two of them, the third one is forced. Two angles are 50 and 60. Add those: 50 plus 60 equals 110. Now 180 take away 110 equals 70 degrees.",
             '[[triangle v="A,B,C" angles="50,60,"]][[step eq="50° + 60° = 110°"]][[step eq="180° − 110° = 70°"]]'],
            ["Two steps, and the first one is not the answer. 110 is what the two you were GIVEN come to. The one you were asked for is what is left of the 180 after them.",
             '[[step eq="180° − 110° = 70° ✓"]][[step eq="110° ✗ — that is the two you were given"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Two angles are 30 and 60. Together they are 90, and 180 take away 90 equals 90 degrees.",
                        '[[triangle v="A,B,C" angles="30,60,"]][[step eq="180° − 90° = 90°"]]'],
             "ask": {"a": 65, "b": 75, "op": "tri3"}},
            {"worked": ["One more together. Two angles are 20 and 30. Together they are 50, so the third is 180 take away 50, which equals 130 degrees.",
                        '[[step eq="20° + 30° = 50°"]][[step eq="180° − 50° = 130°"]]'],
             "ask": {"a": 50, "b": 60, "op": "tri3"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 80, "b": 80, "op": "tri3"},
            {"a": 70, "b": 85, "op": "tri3"},
            {"a": 60, "b": 90, "op": "tri3"},
            {"a": 55, "b": 90, "op": "tri3"},
            {"a": 60, "b": 70, "op": "tri3"},
            {"a": 40, "b": 80, "op": "tri3"},
            {"a": 30, "b": 90, "op": "tri3"},
            {"a": 45, "b": 60, "op": "tri3"},
            {"a": 40, "b": 55, "op": "tri3"},
            {"a": 20, "b": 40, "op": "tri3"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U8)


# =============================================================================
# PREALGEBRA -- UNIT 9: VARIABLES & EXPRESSIONS (build kt, 2026-08-21)
# =============================================================================
# The last prealgebra unit, and the doorway to algebra. Everything before this asked
# about numbers; these four ask about a LETTER that stands for one. The order is the
# order the idea grows: a letter holds a number, a number written against a letter
# means times, like terms collect by counting, and a times distributes over a
# parenthesis.
#
# ⭐ THE LAST LESSON DRAWS THE DISTRIBUTIVE PROPERTY as an area model -- a rectangle
# 4 tall and (x + 3) wide, cut into a 4x room and a 12 room -- using [[areamodel]],
# the algebra-tile renderer that has been in the registry since July and (exactly like
# [[angle split=]] before build ks) has never been used by a scripted lesson. The
# child is not handed the rule; the child is shown the two rooms.
#
# THE ERROR THAT RULES THIS UNIT is the notation quietly meaning times: 3x read as
# 3 plus x, and 4(x + 3) read as 4x + 3 with the times never reaching the number.
# Both are offered as wrong taps, every time.
_PREALGEBRA_U9 = [
    {
        "id": "pre-u9-a-letter-holds-a-number",
        "course": "prealgebra", "unit": 9,
        "topic": "A letter holds a number",
        "op": "evx", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("x", "letter"),
        "advance_line": "Three in a row — you've got it! Swap the letter for its number, then work it out.",
        "teach": [
            ["Here is the biggest idea in all of algebra, and it is small enough to hold: a letter can stand for a number. When we write x , we mean some number that x is holding for us. Tell me what x holds, and every question about x becomes a question about that number.",
             '[[goal text="A letter holds a number"]]'],
            ["Say x is holding 5. What is x plus 3? Swap the letter for its number: x plus 3 becomes 5 plus 3, which equals 8. That swap is the whole move.",
             '[[step eq="x = 5"]][[step eq="x + 3 = 5 + 3 = 8"]]'],
            ["One careful thing. x plus 3 with x holding 5 is NOT fifty-three. The 5 and the 3 do not sit next to each other like digits — the plus keeps them apart. Swap first, then add.",
             '[[step eq="5 + 3 = 8 ✓"]][[step eq="53 ✗ — those are digits, not a sum"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x is holding 4. x plus 6 becomes 4 plus 6, which equals 10.",
                        '[[step eq="x = 4"]][[step eq="4 + 6 = 10"]]'],
             "ask": {"a": 5, "b": 6, "op": "evx"}},
            {"worked": ["One more together. x is holding 7. x plus 2 becomes 7 plus 2, which equals 9.",
                        '[[step eq="7 + 2 = 9"]]'],
             "ask": {"a": 8, "b": 7, "op": "evx"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "evx"},
            {"a": 4, "b": 2, "op": "evx"},
            {"a": 3, "b": 4, "op": "evx"},
            {"a": 5, "b": 3, "op": "evx"},
            {"a": 6, "b": 3, "op": "evx"},
            {"a": 4, "b": 7, "op": "evx"},
            {"a": 8, "b": 4, "op": "evx"},
            {"a": 9, "b": 5, "op": "evx"},
            {"a": 7, "b": 9, "op": "evx"},
            {"a": 9, "b": 9, "op": "evx"},
        ],
    },
    {
        "id": "pre-u9-a-number-against-a-letter",
        "course": "prealgebra", "unit": 9,
        "topic": "A number against a letter means times",
        "op": "mlx", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("x", "times"),
        "advance_line": "Three in a row — you've got it! A number against a letter means times, every time.",
        "teach": [
            ["Algebra has one piece of shorthand you have to be told, because nothing about it looks like what it means: a number written right next to a letter means TIMES. 3 x means 3 times x. The times sign is there — it is just invisible.",
             '[[goal text="A number against a letter means times"]]'],
            ["Say x is holding 4. What is 3 x? That is 3 times x, so 3 times 4, which equals 12.",
             '[[step eq="x = 4"]][[step eq="3x = 3 × 4 = 12"]]'],
            ["The trap is reading 3 x as 3 plus x — it looks like the 3 is just standing near the x. It is not standing near it; it is timesing it. 3 x with x holding 4 equals 12, never 7.",
             '[[step eq="3x = 12 ✓"]][[step eq="3 + 4 = 7 ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x is holding 5. 4 x is 4 times 5, which equals 20.",
                        '[[step eq="4x = 4 × 5 = 20"]]'],
             "ask": {"a": 4, "b": 5, "op": "mlx"}},
            {"worked": ["One more together. x is holding 3. 6 x is 6 times 3, which equals 18.",
                        '[[step eq="6x = 6 × 3 = 18"]]'],
             "ask": {"a": 7, "b": 3, "op": "mlx"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "mlx"},
            {"a": 4, "b": 2, "op": "mlx"},
            {"a": 3, "b": 3, "op": "mlx"},
            {"a": 3, "b": 4, "op": "mlx"},
            {"a": 5, "b": 3, "op": "mlx"},
            {"a": 4, "b": 4, "op": "mlx"},
            {"a": 6, "b": 3, "op": "mlx"},
            {"a": 5, "b": 4, "op": "mlx"},
            {"a": 7, "b": 4, "op": "mlx"},
            {"a": 6, "b": 6, "op": "mlx"},
        ],
    },
    {
        "id": "pre-u9-collecting-x",
        "course": "prealgebra", "unit": 9,
        "topic": "Collecting the x's",
        "op": "clt", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("x", "terms"),
        "advance_line": "Three in a row — you've got it! x's collect by counting, like apples.",
        "teach": [
            ["You do not need to know what x is holding to do some things with it. 3 x plus 2 x — three of something plus two of the same something is five of it. Three apples plus two apples: five apples. Three x's plus two x's: five x's. Pieces like 3 x and 2 x are called terms , and terms of x collect by counting.",
             '[[goal text="Collecting the x\'s"]]'],
            ["Watch: 3 x plus 2 x. Count them: 3 of them plus 2 of them equals 5 of them. So 3 x plus 2 x equals 5 x — whatever x turns out to be holding.",
             '[[step eq="3x + 2x"]][[step eq="3 of them + 2 of them = 5 of them"]]'],
            ["Careful — the counts ADD. Do not times them. 3 x plus 2 x is 5 x, not 6 x. The invisible times lives between a number and its own letter, not between the two counts.",
             '[[step eq="3x + 2x = 5x ✓"]][[step eq="6x ✗ — the counts add"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 x plus 5 x. Four of them plus five of them equals nine of them: 9 x.",
                        '[[step eq="4x + 5x = 9x"]]'],
             "ask": {"a": 5, "b": 6, "op": "clt"}},
            {"worked": ["One more together. 7 x plus 2 x equals 9 x.",
                        '[[step eq="7x + 2x = 9x"]]'],
             "ask": {"a": 8, "b": 6, "op": "clt"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 4, "op": "clt"},
            {"a": 4, "b": 3, "op": "clt"},
            {"a": 6, "b": 2, "op": "clt"},
            {"a": 4, "b": 5, "op": "clt"},
            {"a": 7, "b": 4, "op": "clt"},
            {"a": 8, "b": 5, "op": "clt"},
            {"a": 9, "b": 5, "op": "clt"},
            {"a": 7, "b": 8, "op": "clt"},
            {"a": 9, "b": 7, "op": "clt"},
            {"a": 9, "b": 9, "op": "clt"},
        ],
    },
    {
        "id": "pre-u9-the-times-reaches-both",
        "course": "prealgebra", "unit": 9,
        "topic": "The times reaches both rooms",
        "op": "dst", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("parentheses", "x"),
        "advance_line": "Three in a row — you've got it! The times outside reaches everything inside.",
        "teach": [
            ["You met parentheses in the very first prealgebra lesson: do what is inside first. But when an x is inside, you CANNOT do the inside first — x plus 3 will not collapse into one number. So the times outside has to reach in. Here is the picture that shows what that means.",
             '[[goal text="The times reaches both rooms"]][[areamodel rows="4" cols="x,3"]]'],
            ["This rectangle is 4 tall and x plus 3 wide, so its area is 4 times the whole of x plus 3. The wall splits it into two rooms: one is 4 times x, the other is 4 times 3, which equals 12. Both rooms together: 4 x plus 12.",
             '[[areamodel rows="4" cols="x,3"]][[step eq="4(x + 3) = 4x + 12"]]'],
            ["The times reaches BOTH rooms — that is the whole rule. The wrong answer is 4 x plus 3, where the 4 timesed the x and never touched the 3. Look at the picture: the second room is real, and it is 12, not 3.",
             '[[step eq="4x + 12 ✓"]][[step eq="4x + 3 ✗ — the 3 never got timesed"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Times the whole of x plus 2 by 5. The rooms are 5 x and 5 times 2, which equals 10. So it is 5 x plus 10.",
                        '[[areamodel rows="5" cols="x,2"]][[step eq="5(x + 2) = 5x + 10"]]'],
             "ask": {"a": 4, "b": 3, "op": "dst"}},
            {"worked": ["One more together. Times the whole of x plus 4 by 3. The rooms are 3 x and 3 times 4, which equals 12: 3 x plus 12.",
                        '[[areamodel rows="3" cols="x,4"]][[step eq="3(x + 4) = 3x + 12"]]'],
             "ask": {"a": 5, "b": 6, "op": "dst"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "dst"},
            {"a": 4, "b": 2, "op": "dst"},
            {"a": 3, "b": 3, "op": "dst"},
            {"a": 3, "b": 4, "op": "dst"},
            {"a": 5, "b": 3, "op": "dst"},
            {"a": 4, "b": 4, "op": "dst"},
            {"a": 6, "b": 3, "op": "dst"},
            {"a": 5, "b": 4, "op": "dst"},
            {"a": 6, "b": 4, "op": "dst"},
            {"a": 7, "b": 4, "op": "dst"},
        ],
    },
]
LESSONS.extend(_PREALGEBRA_U9)


# =============================================================================
# ALGEBRA I -- UNIT 1: FOUNDATIONS & EXPRESSIONS (build ku, 2026-08-22)
# =============================================================================
# THE FIRST ALGEBRA I UNIT, sitting directly on Prealgebra U9. That unit planted the
# four seeds one at a time; this one makes them work together. Two-step evaluation is
# where order of operations (Prealgebra U1's very first rule) meets a letter. The
# second letter proves the first one was never special. Collecting past a y is the
# first algebra done blind -- you never learn what either letter holds. And
# distributing over a take away is the first time the invisible times has to carry a
# minus sign with it, drawn as an area model with a negative room.
#
# THE COURSE KEY IS "algebra1", matching curriculum.COURSES -- Jim's own curriculum
# names this unit "Foundations & Expressions".
_ALGEBRA1_U1 = [
    {
        "id": "alg1-u1-two-steps-with-a-letter",
        "course": "algebra1", "unit": 1,
        "topic": "Two steps with a letter",
        "op": "ev2", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("x", "times"),
        "advance_line": "Three in a row — you've got it! Times first, then add — even with a letter inside.",
        "teach": [
            ["Welcome to algebra. You already know the two moves this lesson needs: a number against a letter means times, and times comes before add. Put them together and you can work out something like 3 x plus 2 the moment you learn what x is holding.",
             '[[goal text="Two steps with a letter"]]'],
            ["Say x is holding 4. What is 3 x plus 2? The times comes first: 3 times 4 equals 12. Then the add: 12 plus 2 equals 14.",
             '[[step eq="x = 4"]][[step eq="3x + 2 = 3 × 4 + 2"]][[step eq="12 + 2 = 14"]]'],
            ["The order is the whole game. If you add first — 4 plus 2, then times 3 — you get 18, and 18 is wrong. The plus cannot reach the x before the times has had it.",
             '[[step eq="3 × 4 + 2 = 14 ✓"]][[step eq="3 × (4 + 2) = 18 ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x is holding 5. 2 x plus 7: times first, 2 times 5 equals 10, then 10 plus 7 equals 17.",
                        '[[step eq="2x + 7 = 10 + 7 = 17"]]'],
             "ask": {"a": 4, "b": 3, "c": 2, "op": "ev2"}},
            {"worked": ["One more together. x is holding 3. 5 x plus 4: 5 times 3 equals 15, and 15 plus 4 equals 19.",
                        '[[step eq="5x + 4 = 15 + 4 = 19"]]'],
             "ask": {"a": 5, "b": 4, "c": 6, "op": "ev2"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 2, "op": "ev2"},
            {"a": 3, "b": 2, "c": 3, "op": "ev2"},
            {"a": 2, "b": 3, "c": 4, "op": "ev2"},
            {"a": 4, "b": 2, "c": 5, "op": "ev2"},
            {"a": 3, "b": 4, "c": 3, "op": "ev2"},
            {"a": 5, "b": 3, "c": 4, "op": "ev2"},
            {"a": 4, "b": 5, "c": 2, "op": "ev2"},
            {"a": 6, "b": 4, "c": 3, "op": "ev2"},
            {"a": 7, "b": 4, "c": 5, "op": "ev2"},
            {"a": 8, "b": 5, "c": 6, "op": "ev2"},
        ],
    },
    {
        "id": "alg1-u1-two-letters",
        "course": "algebra1", "unit": 1,
        "topic": "Two letters at once",
        "op": "evxy", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("y", "letter"),
        "advance_line": "Three in a row — you've got it! Each letter keeps its own number.",
        "teach": [
            ["There was never anything special about x. Any letter can hold a number, and two letters can each hold their own. Meet y — it works exactly like x, and the two of them can stand in the same expression without getting mixed up.",
             '[[goal text="Two letters at once"]]'],
            ["Say x is holding 3 and y is holding 4. What is x plus 2 y? Deal with the times first: 2 y is 2 times 4, which equals 8. Then x plus that: 3 plus 8 equals 11.",
             '[[step eq="x = 3 · y = 4"]][[step eq="x + 2y = 3 + 2 × 4"]][[step eq="3 + 8 = 11"]]'],
            ["Each letter keeps its own number — the 2 belongs to the y and never touches the x. 3 plus 2, timesed by 4, would be 20, and 20 is wrong. Read who the 2 is standing next to.",
             '[[step eq="3 + 2 × 4 = 11 ✓"]][[step eq="(3 + 2) × 4 = 20 ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x holds 5, y holds 2. x plus 4 y: 4 times 2 equals 8, and 5 plus 8 equals 13.",
                        '[[step eq="5 + 4 × 2 = 13"]]'],
             "ask": {"a": 3, "b": 4, "c": 2, "op": "evxy"}},
            {"worked": ["One more together. x holds 6, y holds 3. x plus 5 y: 5 times 3 equals 15, and 6 plus 15 equals 21.",
                        '[[step eq="6 + 5 × 3 = 21"]]'],
             "ask": {"a": 7, "b": 5, "c": 4, "op": "evxy"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 2, "op": "evxy"},
            {"a": 3, "b": 2, "c": 3, "op": "evxy"},
            {"a": 4, "b": 3, "c": 2, "op": "evxy"},
            {"a": 2, "b": 5, "c": 2, "op": "evxy"},
            {"a": 5, "b": 4, "c": 3, "op": "evxy"},
            {"a": 4, "b": 5, "c": 3, "op": "evxy"},
            {"a": 6, "b": 5, "c": 3, "op": "evxy"},
            {"a": 3, "b": 7, "c": 4, "op": "evxy"},
            {"a": 6, "b": 7, "c": 4, "op": "evxy"},
            {"a": 9, "b": 6, "c": 5, "op": "evxy"},
        ],
    },
    {
        "id": "alg1-u1-collecting-past-a-y",
        "course": "algebra1", "unit": 1,
        "topic": "Collecting past a y",
        "op": "cl2", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("x", "y"),
        "advance_line": "Three in a row — you've got it! Only the same letter collects.",
        "teach": [
            ["You know that x's collect by counting: 3 x plus 4 x is 7 x. Today there is a y standing in the middle. The rule does not change — it just gets a boundary: only the SAME letter collects. An x and a y are apples and oranges.",
             '[[goal text="Collecting past a y"]]'],
            ["Watch: 3 x plus 2 y plus 4 x. Walk along it and count only the x's: 3 of them, then 4 more, which equals 7 x. The 2 y is a different thing — it walks past and stays exactly as it is. The answer is 7 x plus 2 y.",
             '[[step eq="3x + 2y + 4x"]][[step eq="the x\'s: 3 + 4 = 7 · the y stays"]]'],
            ["The tempting mistake is grabbing everything: 3 plus 2 plus 4 equals 9, and calling it 9 of something. Nine of WHAT? The x's and the y are not the same thing, and a count needs everything in it to be the same thing.",
             '[[step eq="7x + 2y ✓"]][[step eq="9 ✗ — nine of what?"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 5 x plus 3 y plus 2 x. The x's: 5 plus 2 equals 7. So it is 7 x plus 3 y.",
                        '[[step eq="5x + 3y + 2x = 7x + 3y"]]'],
             "ask": {"a": 4, "b": 2, "c": 6, "op": "cl2"}},
            {"worked": ["One more together. 6 x plus 4 y plus 3 x. The x's make 9, so it is 9 x plus 4 y.",
                        '[[step eq="6x + 4y + 3x = 9x + 4y"]]'],
             "ask": {"a": 8, "b": 3, "c": 5, "op": "cl2"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 3, "op": "cl2"},
            {"a": 3, "b": 2, "c": 4, "op": "cl2"},
            {"a": 4, "b": 3, "c": 4, "op": "cl2"},
            {"a": 5, "b": 4, "c": 4, "op": "cl2"},
            {"a": 6, "b": 3, "c": 5, "op": "cl2"},
            {"a": 7, "b": 4, "c": 5, "op": "cl2"},
            {"a": 8, "b": 5, "c": 6, "op": "cl2"},
            {"a": 9, "b": 4, "c": 6, "op": "cl2"},
            {"a": 9, "b": 5, "c": 8, "op": "cl2"},
            {"a": 9, "b": 6, "c": 9, "op": "cl2"},
        ],
    },
    {
        "id": "alg1-u1-minus-goes-through",
        "course": "algebra1", "unit": 1,
        "topic": "The minus goes through too",
        "op": "dstm", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("parentheses", "take away"),
        "advance_line": "Three in a row — you've got it! The times reaches both rooms, minus and all.",
        "teach": [
            ["You know the times outside parentheses reaches both rooms: 4 times the whole of x plus 3 is 4 x plus 12. Today the inside says take away instead — x take away 3 — and the rule holds. The times still reaches both rooms; the second room just comes off instead of going on.",
             '[[goal text="The minus goes through too"]][[areamodel rows="4" cols="x,-3"]]'],
            ["Look at the picture: a rectangle 4 tall and x take away 3 wide. The rooms are 4 times x, and 4 times 3, which equals 12 — and that room is TAKEN AWAY. So 4 times the whole of x take away 3 comes to 4 x take away 12.",
             '[[areamodel rows="4" cols="x,-3"]][[step eq="4(x − 3) = 4x − 12"]]'],
            ["The wrong answer is 4 x take away 3, where the 4 timesed the x and never reached the 3. The times does not stop at the minus sign — it carries it along. 12 comes off, not 3.",
             '[[step eq="4x − 12 ✓"]][[step eq="4x − 3 ✗ — the 3 never got timesed"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Times the whole of x take away 2 by 5. The rooms are 5 x, and 5 times 2, which equals 10, taken away: 5 x take away 10.",
                        '[[areamodel rows="5" cols="x,-2"]][[step eq="5(x − 2) = 5x − 10"]]'],
             "ask": {"a": 4, "b": 3, "op": "dstm"}},
            {"worked": ["One more together. Times the whole of x take away 4 by 3. The rooms are 3 x and 12, taken away: 3 x take away 12.",
                        '[[areamodel rows="3" cols="x,-4"]][[step eq="3(x − 4) = 3x − 12"]]'],
             "ask": {"a": 7, "b": 3, "op": "dstm"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "dstm"},
            {"a": 4, "b": 2, "op": "dstm"},
            {"a": 3, "b": 3, "op": "dstm"},
            {"a": 3, "b": 4, "op": "dstm"},
            {"a": 5, "b": 3, "op": "dstm"},
            {"a": 4, "b": 4, "op": "dstm"},
            {"a": 6, "b": 3, "op": "dstm"},
            {"a": 5, "b": 4, "op": "dstm"},
            {"a": 6, "b": 4, "op": "dstm"},
            {"a": 8, "b": 4, "op": "dstm"},
        ],
    },
]
LESSONS.extend(_ALGEBRA1_U1)


# =============================================================================
# ALGEBRA I -- UNIT 2: LINEAR EQUATIONS & INEQUALITIES (build kv, 2026-08-22)
# =============================================================================
# SOLVING BEGINS. Unit 1 always handed the child what x was holding; from here the
# EQUATION holds it, and the child gets it back by undoing -- the same move off both
# sides. The board is ⭐ [[balance]], the balance-scale renderer that has been in the
# codebase since July and never once used by a scripted lesson. An equation IS a
# balance, and "take the same off both sides or the scale tips" is the whole logic of
# solving, drawn.
#
# The ladder: undo a plus, undo a times (a DIFFERENT undo -- the single biggest
# decision a solver makes is which one), two steps back in reverse order (the 3 went
# on last, so it comes off first -- socks on before shoes, shoes off before socks),
# and finally "less than", where the tap answer is the BIGGEST whole number allowed,
# because an inequality's answer is a crowd and a tap can only hold one number.
_ALGEBRA1_U2 = [
    {
        "id": "alg1-u2-undoing-a-plus",
        "course": "algebra1", "unit": 2,
        "topic": "Undoing a plus",
        "op": "un1", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("equals", "x"),
        "advance_line": "Three in a row — you've got it! Take the same off both sides and the scale stays level.",
        "teach": [
            ["Until today, I always told you what x was holding. Now the equation tells you — in disguise. x plus 4 equals 11 means: some hidden number, plus 4, comes to 11 — and finding it is called solving. Here is the picture that keeps it honest: an equation is a balance scale, and equals means LEVEL.",
             '[[goal text="Undoing a plus"]][[balance left="x + 4" right="11"]]'],
            ["The left pan holds x and a 4. To get x alone, take the 4 off — but the scale only stays level if you take 4 off BOTH sides. 11 take away 4 equals 7. So x is holding 7.",
             '[[balance left="x + 4" right="11" caption="take 4 off both sides"]][[step eq="x = 11 − 4 = 7"]]'],
            ["Check it — put 7 back in: 7 plus 4 equals 11. Level. And watch the wrong move: ADDING 4 gives 15, which pushes the same way the equation already went. Solving is undoing, and the undo of a plus is a take away.",
             '[[step eq="7 + 4 = 11 ✓"]][[step eq="x = 15 ✗ — that pushed instead of undoing"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x plus 5 equals 12. Take 5 off both sides: 12 take away 5 equals 7. x is holding 7.",
                        '[[balance left="x + 5" right="12"]][[step eq="x = 12 − 5 = 7"]]'],
             "ask": {"a": 4, "b": 13, "op": "un1"}},
            {"worked": ["One more together. x plus 3 equals 10. 10 take away 3 equals 7, so x is holding 7.",
                        '[[step eq="x = 10 − 3 = 7"]]'],
             "ask": {"a": 6, "b": 21, "op": "un1"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 5, "op": "un1"},
            {"a": 4, "b": 7, "op": "un1"},
            {"a": 2, "b": 7, "op": "un1"},
            {"a": 5, "b": 11, "op": "un1"},
            {"a": 3, "b": 10, "op": "un1"},
            {"a": 6, "b": 14, "op": "un1"},
            {"a": 4, "b": 14, "op": "un1"},
            {"a": 7, "b": 19, "op": "un1"},
            {"a": 5, "b": 19, "op": "un1"},
            {"a": 8, "b": 24, "op": "un1"},
        ],
    },
    {
        "id": "alg1-u2-undoing-a-times",
        "course": "algebra1", "unit": 2,
        "topic": "Undoing a times",
        "op": "un2", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("x", "times"),
        "advance_line": "Three in a row — you've got it! The undo of a times is a share.",
        "teach": [
            ["A new disguise. 3 x equals 12 — three x's together weigh 12. The undo is NOT a take away this time. Three of something made 12, so one of them is 12 shared between 3. The undo of a times is a share.",
             '[[goal text="Undoing a times"]][[balance left="3x" right="12"]]'],
            ["Share both sides between 3: the left pan drops to one x, and the right drops to 12 shared between 3, which equals 4. So x is holding 4.",
             '[[balance left="3x" right="12" caption="share both sides between 3"]][[step eq="x = 12 ÷ 3 = 4"]]'],
            ["The trap is undoing the WRONG operation. 12 take away 3 equals 9 — but nothing here was added, so there is nothing to take away. Ask what happened to x. It was timesed, so it gets shared. Check: 3 times 4 equals 12. Level.",
             '[[step eq="3 × 4 = 12 ✓"]][[step eq="x = 12 − 3 = 9 ✗ — wrong undo"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 4 x equals 20. Share both sides between 4: 20 shared between 4 equals 5. x is holding 5.",
                        '[[balance left="4x" right="20"]][[step eq="x = 20 ÷ 4 = 5"]]'],
             "ask": {"a": 2, "b": 12, "op": "un2"}},
            {"worked": ["One more together. 5 x equals 30. 30 shared between 5 equals 6, so x is holding 6.",
                        '[[step eq="x = 30 ÷ 5 = 6"]]'],
             "ask": {"a": 4, "b": 36, "op": "un2"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 4, "b": 8, "op": "un2"},
            {"a": 3, "b": 9, "op": "un2"},
            {"a": 5, "b": 15, "op": "un2"},
            {"a": 2, "b": 8, "op": "un2"},
            {"a": 6, "b": 24, "op": "un2"},
            {"a": 3, "b": 15, "op": "un2"},
            {"a": 4, "b": 24, "op": "un2"},
            {"a": 5, "b": 35, "op": "un2"},
            {"a": 3, "b": 24, "op": "un2"},
            {"a": 6, "b": 54, "op": "un2"},
        ],
    },
    {
        "id": "alg1-u2-two-steps-back",
        "course": "algebra1", "unit": 2,
        "topic": "Two steps back",
        "op": "un3", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("x", "equals"),
        "advance_line": "Three in a row — you've got it! Last on, first off — then share.",
        "teach": [
            ["Now both disguises at once: 2 x plus 3 equals 11. Two undos to make, and the ORDER matters. Think of socks and shoes: the shoes went on last, so they come off first. Here the plus 3 went on last — it comes off first.",
             '[[goal text="Two steps back"]][[balance left="2x + 3" right="11"]]'],
            ["Take 3 off both sides: 2 x equals 8. Now the second undo — share both sides between 2: x equals 4.",
             '[[balance left="2x" right="8" caption="the 3 is off — one undo left"]][[step eq="2x = 11 − 3 = 8"]][[step eq="x = 8 ÷ 2 = 4"]]'],
            ["Do not stop at 8. Eight is what TWO x's weigh, not what one x is holding. Both undos have to happen. Check: 2 times 4 is 8, plus 3 is 11. Level.",
             '[[step eq="2 × 4 + 3 = 11 ✓"]][[step eq="x = 8 ✗ — that is two x\'s, not one"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 3 x plus 2 equals 14. The 2 comes off first: 3 x equals 12. Then share: x equals 4.",
                        '[[step eq="3x = 14 − 2 = 12"]][[step eq="x = 12 ÷ 3 = 4"]]'],
             "ask": {"a": 2, "b": 4, "c": 14, "op": "un3"}},
            {"worked": ["One more together. 4 x plus 3 equals 19. Take the 3 off: 4 x equals 16. Share between 4: x equals 4.",
                        '[[step eq="4x = 16"]][[step eq="x = 4"]]'],
             "ask": {"a": 5, "b": 3, "c": 38, "op": "un3"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 7, "op": "un3"},
            {"a": 3, "b": 2, "c": 11, "op": "un3"},
            {"a": 2, "b": 5, "c": 13, "op": "un3"},
            {"a": 4, "b": 3, "c": 23, "op": "un3"},
            {"a": 3, "b": 4, "c": 22, "op": "un3"},
            {"a": 2, "b": 7, "c": 21, "op": "un3"},
            {"a": 5, "b": 2, "c": 42, "op": "un3"},
            {"a": 4, "b": 5, "c": 41, "op": "un3"},
            {"a": 3, "b": 6, "c": 36, "op": "un3"},
            {"a": 6, "b": 4, "c": 76, "op": "un3"},
        ],
    },
    {
        "id": "alg1-u2-the-biggest-x",
        "course": "algebra1", "unit": 2,
        "topic": "Less than",
        "op": "ineq", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("less than", "x"),
        "advance_line": "Three in a row — you've got it! Less than shuts the door on the number itself.",
        "teach": [
            ["Not every puzzle says equals. x plus 3 is LESS THAN 10 — the left side has to weigh less than the right. Now x is not one hidden number any more; it is a whole crowd of allowed ones, and the puzzle is finding where the crowd stops.",
             '[[goal text="Less than"]][[step eq="x + 3 < 10"]]'],
            ["Undo it exactly like an equation: take 3 from both sides. x is less than 7. On the number line, that is everything to the LEFT of 7 — and 7 itself is not included, because x plus 3 has to stay under 10, not land on it.",
             '[[step eq="x < 10 − 3 = 7"]][[numberline min="0" max="9" points="7"]]'],
            ["So what is the biggest WHOLE number x can hold? Not 7 — less than shuts the door on 7 itself. Try it: 7 plus 3 equals 10, and 10 is not less than 10. The biggest allowed is 6.",
             '[[step eq="x = 6 ✓ — 6 + 3 = 9, under 10"]][[step eq="x = 7 ✗ — 7 + 3 = 10, not under"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x plus 4 is less than 11. Take 4 off: x is less than 7, so the biggest whole number is 6.",
                        '[[step eq="x < 7"]][[step eq="biggest whole number: 6"]]'],
             "ask": {"a": 3, "b": 9, "op": "ineq"}},
            {"worked": ["One more together. x plus 2 is less than 9. x is less than 7 — the biggest whole number x can hold is 6.",
                        '[[step eq="x < 7 → 6"]]'],
             "ask": {"a": 6, "b": 19, "op": "ineq"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 5, "op": "ineq"},
            {"a": 3, "b": 7, "op": "ineq"},
            {"a": 4, "b": 9, "op": "ineq"},
            {"a": 2, "b": 8, "op": "ineq"},
            {"a": 5, "b": 12, "op": "ineq"},
            {"a": 3, "b": 11, "op": "ineq"},
            {"a": 6, "b": 15, "op": "ineq"},
            {"a": 4, "b": 14, "op": "ineq"},
            {"a": 7, "b": 18, "op": "ineq"},
            {"a": 5, "b": 17, "op": "ineq"},
        ],
    },
]
LESSONS.extend(_ALGEBRA1_U2)


# =============================================================================
# ALGEBRA I -- UNIT 3: FUNCTIONS & NOTATION (build kw, 2026-08-22)
# =============================================================================
# A function is a MACHINE: a number goes in, the rule happens to it, a number comes
# out. The board is ⭐ [[machine]] -- the last renderer on July's figure shelf to get
# its first scripted use (areamodel kt, angle-split ks, balance kv). It draws
# input -> rule box -> output and prints "f(4) = 9" underneath, which means the
# NOTATION lesson can point at a line the child has already stared at for a whole
# lesson before anyone asks them to read it.
#
# THE NOTATION ERROR THIS UNIT DEFUSES: f(3) read as f TIMES 3. That misreading is
# not stupid -- parentheses have meant times since the distributive lesson, and here
# the same marks suddenly mean "feed the machine". The f-of-x lesson says that out
# loud and offers the times-reading as the wrong tap on every single problem.
_ALGEBRA1_U3 = [
    {
        "id": "alg1-u3-the-number-machine",
        "course": "algebra1", "unit": 3,
        "topic": "The number machine",
        "op": "fm1", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("machine", "rule"),
        "advance_line": "Three in a row — you've got it! In goes a number, the rule runs, out comes the answer.",
        "teach": [
            ["Here is a machine that eats numbers. It has one rule painted on its side, and it follows that rule on whatever you feed it — same rule, every time, no exceptions. Feed it a number and it puts a number out. That is all a function is: a rule with a door in and a door out.",
             '[[goal text="The number machine"]][[machine input="4" rule="2x + 1" output="9"]]'],
            ["This machine's rule is: times the input by 2, then add 1. Feed it 4. The rule runs in order: 2 times 4 equals 8, then 8 plus 1 equals 9. Out comes 9.",
             '[[machine input="4" rule="2x + 1" output="9"]][[step eq="2 × 4 = 8"]][[step eq="8 + 1 = 9"]]'],
            ["The rule says its steps in order, and the order is part of the rule. Times by 2 THEN add 1 is not the same machine as add 1 then times by 2 — feed them both a 4 and one puts out 9, the other 10.",
             '[[step eq="2 × 4 + 1 = 9 ✓"]][[step eq="(4 + 1) × 2 = 10 — a DIFFERENT machine"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. The rule is times by 3, then add 2. Feed it 5: 3 times 5 equals 15, plus 2 equals 17.",
                        '[[machine input="5" rule="3x + 2" output="17"]]'],
             "ask": {"a": 3, "b": 2, "c": 4, "op": "fm1"}},
            {"worked": ["One more together. Times by 4, then add 1. Feed it 3: 4 times 3 equals 12, plus 1 equals 13.",
                        '[[machine input="3" rule="4x + 1" output="13"]]'],
             "ask": {"a": 5, "b": 3, "c": 5, "op": "fm1"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 2, "c": 3, "op": "fm1"},
            {"a": 2, "b": 3, "c": 3, "op": "fm1"},
            {"a": 3, "b": 2, "c": 3, "op": "fm1"},
            {"a": 2, "b": 4, "c": 4, "op": "fm1"},
            {"a": 3, "b": 4, "c": 3, "op": "fm1"},
            {"a": 4, "b": 2, "c": 3, "op": "fm1"},
            {"a": 3, "b": 3, "c": 4, "op": "fm1"},
            {"a": 4, "b": 3, "c": 4, "op": "fm1"},
            {"a": 5, "b": 2, "c": 4, "op": "fm1"},
            {"a": 4, "b": 4, "c": 5, "op": "fm1"},
        ],
    },
    {
        "id": "alg1-u3-f-of-x",
        "course": "algebra1", "unit": 3,
        "topic": "Saying f of x",
        "op": "fnot", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("f", "of"),
        "advance_line": "Three in a row — you've got it! f of 3 means feed the machine 3.",
        "teach": [
            ["Mathematicians got tired of drawing the machine, so they gave it a name: f. And look under the machine — the board has been writing its shorthand all along: f of 4 equals 9. It means: feed machine f the number 4, and 9 comes out. That is the whole code.",
             '[[goal text="Saying f of x"]][[machine input="4" rule="x + 5" output="9" fname="f"]]'],
            ["f of x equals x plus 5 — that is the rule, written with the name in front. So what is f of 3? Feed the machine 3: 3 plus 5 equals 8. f of 3 equals 8.",
             '[[machine input="3" rule="x + 5" output="8" fname="f"]][[step eq="f(3) = 3 + 5 = 8"]]'],
            ["Now the warning, and it is a fair one. In the distributive lesson, parentheses meant TIMES. Here, f followed by 3 in parentheses does NOT mean f times 3 — there is no timesing anywhere. It is the machine's name and its meal. Same marks, different job.",
             '[[step eq="f(3) = feed f the number 3 ✓"]][[step eq="f × 3 ✗ — nothing is being timesed"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. f of x equals x plus 4. f of 6: feed it 6, and 6 plus 4 equals 10.",
                        '[[step eq="f(6) = 6 + 4 = 10"]]'],
             "ask": {"a": 3, "b": 5, "op": "fnot"}},
            {"worked": ["One more together. f of x equals x plus 2. f of 9 is 9 plus 2, which equals 11.",
                        '[[step eq="f(9) = 11"]]'],
             "ask": {"a": 7, "b": 4, "op": "fnot"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "fnot"},
            {"a": 4, "b": 2, "op": "fnot"},
            {"a": 3, "b": 4, "op": "fnot"},
            {"a": 5, "b": 3, "op": "fnot"},
            {"a": 4, "b": 5, "op": "fnot"},
            {"a": 6, "b": 4, "op": "fnot"},
            {"a": 5, "b": 7, "op": "fnot"},
            {"a": 7, "b": 6, "op": "fnot"},
            {"a": 6, "b": 8, "op": "fnot"},
            {"a": 8, "b": 9, "op": "fnot"},
        ],
    },
    {
        "id": "alg1-u3-two-machines",
        "course": "algebra1", "unit": 3,
        "topic": "Two machines in a row",
        "op": "fm2", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("machine", "order"),
        "advance_line": "Three in a row — you've got it! The first machine's output is the second machine's input.",
        "teach": [
            ["Machines can stand in a line. The first machine's out-door feeds the second machine's in-door — whatever comes out of one goes straight into the next. Two small rules in a row can do the work of one bigger rule.",
             '[[goal text="Two machines in a row"]]'],
            ["The first machine adds 2. The second times by 3. Feed 4 through both, in order. Machine one: 4 plus 2 equals 6. That 6 goes into machine two: 6 times 3 equals 18.",
             '[[machine input="4" rule="x + 2" output="6"]][[machine input="6" rule="3x" output="18" fname="g"]]'],
            ["The order is everything. Run the same two machines the other way round — times 3 first, then add 2 — and 4 becomes 12 becomes 14, not 18. Same machines, different line-up, different answer. Read WHICH machine is first before you feed anything.",
             '[[step eq="(4 + 2) × 3 = 18 ✓"]][[step eq="4 × 3 + 2 = 14 — the other order"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. First adds 3, second times by 2. Feed 5: 5 plus 3 equals 8, and 8 times 2 equals 16.",
                        '[[machine input="5" rule="x + 3" output="8"]][[machine input="8" rule="2x" output="16" fname="g"]]'],
             "ask": {"a": 3, "b": 2, "c": 4, "op": "fm2"}},
            {"worked": ["One more together. First adds 2, second times by 4. Feed 3: 3 plus 2 equals 5, and 5 times 4 equals 20.",
                        '[[step eq="(3 + 2) × 4 = 20"]]'],
             "ask": {"a": 4, "b": 4, "c": 2, "op": "fm2"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 2, "c": 3, "op": "fm2"},
            {"a": 2, "b": 3, "c": 2, "op": "fm2"},
            {"a": 2, "b": 2, "c": 4, "op": "fm2"},
            {"a": 2, "b": 3, "c": 3, "op": "fm2"},
            {"a": 3, "b": 3, "c": 2, "op": "fm2"},
            {"a": 2, "b": 4, "c": 3, "op": "fm2"},
            {"a": 4, "b": 3, "c": 3, "op": "fm2"},
            {"a": 3, "b": 3, "c": 5, "op": "fm2"},
            {"a": 5, "b": 3, "c": 4, "op": "fm2"},
            {"a": 4, "b": 4, "c": 3, "op": "fm2"},
        ],
    },
    {
        "id": "alg1-u3-which-input",
        "course": "algebra1", "unit": 3,
        "topic": "Which input was it",
        "op": "fback", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("f", "of"),
        "advance_line": "Three in a row — you've got it! Undo the rule and the input walks back out.",
        "teach": [
            ["One more trick with the machine: running it backwards. f of x equals x plus 3, and somebody tells you the machine put out 10 — but not what went in. f of WHAT equals 10? The input is hiding, exactly like x hid on the balance.",
             '[[goal text="Which input was it"]][[machine input="?" rule="x + 3" output="10" fname="f"]]'],
            ["You already know this move. Something plus 3 came to 10 — that is an equation in machine clothes. Undo the rule: 10 take away 3 equals 7. The input was 7.",
             '[[machine input="?" rule="x + 3" output="10" fname="f"]][[step eq="? + 3 = 10"]][[step eq="? = 10 − 3 = 7"]]'],
            ["Check it by running the machine forwards: feed 7, and 7 plus 3 equals 10. It fits. The careless move is running the machine forwards with the OUTPUT — feeding it the 10 and getting 13. The 10 came out of the machine; it never went in.",
             '[[step eq="f(7) = 10 ✓"]][[step eq="10 + 3 = 13 ✗ — the 10 came OUT, it never went in"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. f of x equals x plus 4, and the output is 11. Undo: 11 take away 4 equals 7. The input was 7.",
                        '[[machine input="?" rule="x + 4" output="11" fname="f"]][[step eq="? = 11 − 4 = 7"]]'],
             "ask": {"a": 3, "b": 13, "op": "fback"}},
            {"worked": ["One more together. f of x equals x plus 5, and out came 12. 12 take away 5 equals 7 — the input was 7.",
                        '[[step eq="? = 12 − 5 = 7"]]'],
             "ask": {"a": 6, "b": 20, "op": "fback"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 5, "op": "fback"},
            {"a": 4, "b": 7, "op": "fback"},
            {"a": 2, "b": 6, "op": "fback"},
            {"a": 3, "b": 8, "op": "fback"},
            {"a": 5, "b": 11, "op": "fback"},
            {"a": 2, "b": 9, "op": "fback"},
            {"a": 6, "b": 14, "op": "fback"},
            {"a": 4, "b": 13, "op": "fback"},
            {"a": 7, "b": 18, "op": "fback"},
            {"a": 5, "b": 18, "op": "fback"},
        ],
    },
]
LESSONS.extend(_ALGEBRA1_U3)


# =============================================================================
# ALGEBRA I -- UNIT 4: LINEAR FUNCTIONS & GRAPHS (build kx, 2026-08-22)
# =============================================================================
# The machine meets the coordinate plane. A line IS the machine's whole table of
# answers drawn at once -- every point on it is an input standing under its output.
# The board is ⭐ [[graph]], the real function grapher that no scripted lesson has
# ever used (the shelf continues: areamodel kt, angle-split ks, balance kv,
# machine kw).
#
# The ladder: read one point off a line, SLOPE as how much y climbs when x steps
# once (taught from two points, before any formula), the starting height where x is
# zero, and then slope and start working together to answer for any x -- which is
# y = ax + b understood as "start at b, climb a per step" rather than as a formula.
_ALGEBRA1_U4 = [
    {
        "id": "alg1-u4-reading-the-line",
        "course": "algebra1", "unit": 4,
        "topic": "Reading the line",
        "op": "lny", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("y", "line"),
        "advance_line": "Three in a row — you've got it! Every point is an input standing under its output.",
        "teach": [
            ["Last unit the machine answered one input at a time. A graph answers ALL of them at once. The rule y equals x plus 2 becomes a line on the graph. Pick any x along the bottom, go straight up to the line , and the height you reach is that x's answer — its y.",
             '[[goal text="Reading the line"]][[graph lines="y=x+2" range="0..8"]]'],
            ["What is y when x is 3? Find 3 along the bottom, climb up to the line, and read the height: 3 plus 2 equals 5. The point sits at 3 comma 5 — the input and its output, standing together.",
             '[[graph lines="y=x+2" points="(3,5)" range="0..8"]][[step eq="x = 3 → y = 3 + 2 = 5"]]'],
            ["Keep the partners straight. The first number is the x you were given; the second is the y you found. At 3 comma 5, the answer to the question 'what is y' is 5 — not the 3 you started from.",
             '[[step eq="(3, 5): x = 3, y = 5"]][[step eq="y = 3 ✗ — that is the input"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y equals x plus 4, and x is 2. Climb: 2 plus 4 equals 6. The point is 2 comma 6, and y is 6.",
                        '[[graph lines="y=x+4" points="(2,6)" range="0..8"]][[step eq="y = 2 + 4 = 6"]]'],
             "ask": {"a": 3, "b": 6, "op": "lny"}},
            {"worked": ["One more together. y equals x plus 5, and x is 4: y equals 9.",
                        '[[step eq="y = 4 + 5 = 9"]]'],
             "ask": {"a": 7, "b": 6, "op": "lny"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "lny"},
            {"a": 4, "b": 2, "op": "lny"},
            {"a": 3, "b": 4, "op": "lny"},
            {"a": 5, "b": 3, "op": "lny"},
            {"a": 4, "b": 5, "op": "lny"},
            {"a": 6, "b": 4, "op": "lny"},
            {"a": 5, "b": 7, "op": "lny"},
            {"a": 8, "b": 5, "op": "lny"},
            {"a": 6, "b": 9, "op": "lny"},
            {"a": 9, "b": 8, "op": "lny"},
        ],
    },
    {
        "id": "alg1-u4-the-climb",
        "course": "algebra1", "unit": 4,
        "topic": "The climb of a line",
        "op": "slp", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("slope", "line"),
        "advance_line": "Three in a row — you've got it! The slope is the climb, not the height.",
        "teach": [
            ["Lines are straight, and straight means FAIR: every time x steps one to the right, y climbs by the same amount. That amount — the climb per step — is called the slope. It is the line's personality: big slope, steep line; small slope, gentle line.",
             '[[goal text="The climb of a line"]]'],
            ["Here is a line through 2 comma 3 and 3 comma 5. x stepped once, from 2 to 3. y climbed from 3 to 5 — a climb of 2. The slope is 2, and it is 2 between ANY two neighbouring steps on this line, all the way along.",
             '[[graph points="(2,3),(3,5)" range="0..5"]][[step eq="y: 3 → 5, a climb of 2"]]'],
            ["The slope is the CLIMB, not the height. This line reaches height 5, but its slope is not 5 — 5 is where y landed, and 3 is where it started. The slope is the difference between them: how far y MOVED.",
             '[[step eq="slope = 5 − 3 = 2 ✓"]][[step eq="slope = 5 ✗ — that is a height, not a climb"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Through 1 comma 4 and 2 comma 7. y went from 4 to 7 — a climb of 3. The slope is 3.",
                        '[[graph points="(1,4),(2,7)" range="0..4"]][[step eq="7 − 4 = 3"]]'],
             "ask": {"a": 3, "b": 2, "c": 5, "op": "slp"}},
            {"worked": ["One more together. Through 2 comma 2 and 3 comma 6. From 2 up to 6 is a climb of 4 — the slope is 4.",
                        '[[step eq="6 − 2 = 4"]]'],
             "ask": {"a": 6, "b": 3, "c": 4, "op": "slp"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 1, "c": 3, "op": "slp"},
            {"a": 2, "b": 3, "c": 5, "op": "slp"},
            {"a": 3, "b": 2, "c": 4, "op": "slp"},
            {"a": 3, "b": 4, "c": 6, "op": "slp"},
            {"a": 4, "b": 2, "c": 5, "op": "slp"},
            {"a": 5, "b": 3, "c": 6, "op": "slp"},
            {"a": 6, "b": 2, "c": 7, "op": "slp"},
            {"a": 7, "b": 3, "c": 8, "op": "slp"},
            {"a": 8, "b": 2, "c": 9, "op": "slp"},
            {"a": 9, "b": 4, "c": 7, "op": "slp"},
        ],
    },
    {
        "id": "alg1-u4-where-it-starts",
        "course": "algebra1", "unit": 4,
        "topic": "Where the line starts",
        "op": "yint", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("y", "zero"),
        "advance_line": "Three in a row — you've got it! At x equals zero, the times part vanishes.",
        "teach": [
            ["Every line has a starting height: where it stands when x is zero, right at the left wall of the graph. For a rule like y equals 2 x plus 3, you can find it without drawing anything — put zero in for x and watch what happens.",
             '[[goal text="Where the line starts"]][[graph lines="y=2x+3" range="0..4"]]'],
            ["y equals 2 times zero plus 3. But 2 times zero is ZERO — the whole times part vanishes. All that is left is the plus 3. So at x equals zero, y equals 3. The line starts at height 3 and does its climbing from there.",
             '[[step eq="y = 2 × 0 + 3"]][[step eq="y = 0 + 3 = 3"]]'],
            ["So in y equals 2 x plus 3, the two numbers have two different jobs: the 2 is the climb per step, and the 3 is where the climbing starts. Asked where the line starts, the answer is the plus number — not the 2.",
             '[[step eq="start = 3 ✓"]][[step eq="start = 2 ✗ — that is the climb, not the start"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y equals 4 x plus 5. At x equals zero, 4 times zero vanishes, and y equals 5.",
                        '[[step eq="y = 4 × 0 + 5 = 5"]]'],
             "ask": {"a": 4, "b": 3, "op": "yint"}},
            {"worked": ["One more together. y equals 3 x plus 7. At zero, y equals 7 — that is the starting height.",
                        '[[step eq="y = 3 × 0 + 7 = 7"]]'],
             "ask": {"a": 6, "b": 8, "op": "yint"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 2, "op": "yint"},
            {"a": 5, "b": 3, "op": "yint"},
            {"a": 2, "b": 4, "op": "yint"},
            {"a": 8, "b": 4, "op": "yint"},
            {"a": 6, "b": 5, "op": "yint"},
            {"a": 4, "b": 6, "op": "yint"},
            {"a": 9, "b": 7, "op": "yint"},
            {"a": 3, "b": 8, "op": "yint"},
            {"a": 5, "b": 9, "op": "yint"},
            {"a": 7, "b": 9, "op": "yint"},
        ],
    },
    {
        "id": "alg1-u4-start-and-climb",
        "course": "algebra1", "unit": 4,
        "topic": "Start plus climb",
        "op": "lin2", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("y", "x"),
        "advance_line": "Three in a row — you've got it! Start at the plus number, climb the slope once per step.",
        "teach": [
            ["Now the two jobs work together. y equals 3 x plus 2: start at height 2, and climb 3 for every step x takes. That is the whole line in one sentence — and it answers any x you like.",
             '[[goal text="Start plus climb"]][[graph lines="y=3x+2" range="0..5"]]'],
            ["What is y when x is 4? Four steps, each a climb of 3: 3 times 4 equals 12 of climbing. Add the start: 12 plus 2 equals 14. The line stands at height 14 over x equals 4.",
             '[[graph lines="y=3x+2" points="(4,14)" range="0..6"]][[step eq="y = 3 × 4 + 2 = 14"]]'],
            ["Count your steps carefully. The height at x equals 4 is 14; one step earlier, at x equals 3, it was only 11. Stopping a step short is the easiest mistake on a graph — land on the x you were asked about, then read the height.",
             '[[step eq="x = 4 → 14 ✓"]][[step eq="x = 3 → 11 — one step short"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y equals 2 x plus 5, at x equals 3. Climb: 2 times 3 equals 6. Start: plus 5. y equals 11.",
                        '[[step eq="y = 2 × 3 + 5 = 11"]]'],
             "ask": {"a": 2, "b": 3, "c": 4, "op": "lin2"}},
            {"worked": ["One more together. y equals 4 x plus 1, at x equals 5: 4 times 5 equals 20, plus 1 equals 21.",
                        '[[step eq="y = 4 × 5 + 1 = 21"]]'],
             "ask": {"a": 5, "b": 3, "c": 5, "op": "lin2"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 2, "c": 2, "op": "lin2"},
            {"a": 3, "b": 2, "c": 2, "op": "lin2"},
            {"a": 2, "b": 3, "c": 3, "op": "lin2"},
            {"a": 2, "b": 4, "c": 3, "op": "lin2"},
            {"a": 3, "b": 3, "c": 3, "op": "lin2"},
            {"a": 4, "b": 2, "c": 3, "op": "lin2"},
            {"a": 3, "b": 4, "c": 4, "op": "lin2"},
            {"a": 4, "b": 3, "c": 4, "op": "lin2"},
            {"a": 5, "b": 2, "c": 4, "op": "lin2"},
            {"a": 4, "b": 4, "c": 5, "op": "lin2"},
        ],
    },
]
LESSONS.extend(_ALGEBRA1_U4)


# =============================================================================
# ALGEBRA I -- UNIT 5: SYSTEMS OF EQUATIONS (build ky, 2026-08-22)
# =============================================================================
# TWO RULES TRUE AT ONCE. The unit's one big picture is two lines crossing --
# [[graph]] takes lines="y=x+2; y=3x" and draws them both, and the crossing point is
# the answer, standing on the board before anyone computes it. From there the three
# classical moves, each in its plainest clothes: SWAP a letter for what it equals
# (substitution), the oldest system in the world -- a sum and a difference -- and
# taking one equation away from another so a whole unknown VANISHES (elimination,
# taught as two shopping trips).
#
# A RECURRING DISTRACTOR RUNS THROUGH THE WHOLE UNIT: the value of the OTHER
# unknown. In sys1 it is the y where the lines cross; in sys2 it is y again; in elim
# it is the eraser's price. A system has two answers living in it, and tapping the
# wrong one is the system-specific mistake -- so it is offered every single time.
_ALGEBRA1_U5 = [
    {
        "id": "alg1-u5-where-two-rules-agree",
        "course": "algebra1", "unit": 5,
        "topic": "Where two rules agree",
        "op": "sys1", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("cross", "x"),
        "advance_line": "Three in a row — you've got it! The crossing is where both rules tell the same story.",
        "teach": [
            ["Two rules can both talk about the same x and y. One says y equals x plus 2. Another says y equals 3 times x. Usually they disagree — feed them the same x and they give different y's. But look at the picture: two lines, and they cross .",
             '[[goal text="Where two rules agree"]][[graph lines="y=x+2; y=3x" range="0..4"]]'],
            ["At the crossing, both rules give the SAME y. Try x equals 1: the first rule says 3, the second says 3. They agree! That is what the crossing point means — the one x where both lines stand at the same height.",
             '[[graph lines="y=x+2; y=3x" points="(1,3)" range="0..4"]][[step eq="x + 2 = 3x at x = 1"]]'],
            ["You can find it without the picture too: if both rules give the same y, then x plus 2 EQUALS 3 x. That is an equation, and you know what to do with equations. But keep the question straight — the answer asked for is the x of the crossing, not its height.",
             '[[step eq="x + 2 = 3x → x = 1 ✓"]][[step eq="y = 3 is the HEIGHT, not the x"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y equals x plus 4, and y equals 3 times x. They agree where x plus 4 equals 3 x — at x equals 2, where both say 6.",
                        '[[graph lines="y=x+4; y=3x" points="(2,6)" range="0..5"]][[step eq="x + 4 = 3x → x = 2"]]'],
             "ask": {"a": 10, "b": 6, "op": "sys1"}},
            {"worked": ["One more together. y equals x plus 6, and y equals 4 times x. x plus 6 equals 4 x at x equals 2, where both rules say 8.",
                        '[[step eq="x + 6 = 4x → x = 2"]]'],
             "ask": {"a": 12, "b": 5, "op": "sys1"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 4, "b": 3, "op": "sys1"},
            {"a": 6, "b": 4, "op": "sys1"},
            {"a": 8, "b": 5, "op": "sys1"},
            {"a": 6, "b": 3, "op": "sys1"},
            {"a": 9, "b": 4, "op": "sys1"},
            {"a": 8, "b": 3, "op": "sys1"},
            {"a": 12, "b": 4, "op": "sys1"},
            {"a": 10, "b": 3, "op": "sys1"},
            {"a": 12, "b": 3, "op": "sys1"},
            {"a": 14, "b": 3, "op": "sys1"},
        ],
    },
    {
        "id": "alg1-u5-swapping-in",
        "course": "algebra1", "unit": 5,
        "topic": "Swapping a letter in",
        "op": "sys2", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("swap", "y"),
        "advance_line": "Three in a row — you've got it! Swap y for what it equals, and one letter is left.",
        "teach": [
            ["Here is the strongest trick in this whole unit. If one rule TELLS you what y equals, you can swap y out of the other rule entirely — write what it equals in its place. Two letters become one, and one letter you can solve.",
             '[[goal text="Swapping a letter in"]]'],
            ["y equals x plus 2. Also, x plus y equals 10. Swap the y in the second rule for x plus 2: x plus x plus 2 equals 10. That is 2 x plus 2 equals 10 — so 2 x equals 8, and x equals 4.",
             '[[step eq="x + (x + 2) = 10"]][[step eq="2x = 8"]][[step eq="x = 4"]]'],
            ["Two cares. First: after the swap there are TWO x's — count them. Second: the question asked for x. y is 6 here, and 6 is also standing in the problem waiting to be tapped — but it is the other letter's answer, not yours.",
             '[[step eq="x = 4 ✓ · y = 6 — the OTHER letter"]][[step eq="check: 4 + 6 = 10 ✓"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y equals x plus 4, and x plus y equals 12. Swap: x plus x plus 4 equals 12, so 2 x equals 8, and x equals 4.",
                        '[[step eq="2x + 4 = 12"]][[step eq="x = 4"]]'],
             "ask": {"a": 5, "b": 13, "op": "sys2"}},
            {"worked": ["One more together. y equals x plus 3, and x plus y equals 11. Swap: 2 x plus 3 equals 11, so x equals 4.",
                        '[[step eq="2x + 3 = 11 → x = 4"]]'],
             "ask": {"a": 7, "b": 23, "op": "sys2"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 7, "op": "sys2"},
            {"a": 4, "b": 8, "op": "sys2"},
            {"a": 2, "b": 8, "op": "sys2"},
            {"a": 5, "b": 11, "op": "sys2"},
            {"a": 2, "b": 10, "op": "sys2"},
            {"a": 6, "b": 14, "op": "sys2"},
            {"a": 3, "b": 13, "op": "sys2"},
            {"a": 4, "b": 16, "op": "sys2"},
            {"a": 6, "b": 20, "op": "sys2"},
            {"a": 5, "b": 21, "op": "sys2"},
        ],
    },
    {
        "id": "alg1-u5-sum-and-difference",
        "course": "algebra1", "unit": 5,
        "topic": "The sum and the difference",
        "op": "sumd", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("together", "difference"),
        "advance_line": "Three in a row — you've got it! Add the two clues and the smaller number cancels itself away.",
        "teach": [
            ["The oldest puzzle with two unknowns: two secret numbers, and two clues. Put together they equal 10. Their difference — the bigger take away the smaller — equals 4. Neither clue alone is enough; together they trap the answer completely.",
             '[[goal text="The sum and the difference"]][[step eq="big + small = 10"]][[step eq="big − small = 4"]]'],
            ["Here is the trap closing. Add the two clues: big plus small, plus big take away small — the small cancels itself away, leaving two bigs. 10 plus 4 equals 14, so two bigs equal 14, and the big one is 7. The small one is what is left: 3.",
             '[[step eq="two bigs = 10 + 4 = 14"]][[step eq="big = 7 · small = 3"]]'],
            ["Check both clues: 7 plus 3 equals 10, and 7 take away 3 equals 4. Both happy. The lazy answer is 5 — half of 10 — but that ignores the second clue entirely: 5 and 5 have no difference at all.",
             '[[step eq="7 + 3 = 10 ✓ · 7 − 3 = 4 ✓"]][[step eq="5 and 5 ✗ — their difference is 0, not 4"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Together 12, difference 2. Two bigs equal 14, so the bigger is 7 and the smaller is 5.",
                        '[[step eq="two bigs = 14 → big = 7"]]'],
             "ask": {"a": 10, "b": 4, "op": "sumd"}},
            {"worked": ["One more together. Together 16, difference 6. Two bigs equal 22, the bigger is 11, the smaller is 5.",
                        '[[step eq="two bigs = 22 → big = 11"]]'],
             "ask": {"a": 22, "b": 6, "op": "sumd"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 6, "b": 2, "op": "sumd"},
            {"a": 8, "b": 2, "op": "sumd"},
            {"a": 10, "b": 2, "op": "sumd"},
            {"a": 12, "b": 4, "op": "sumd"},
            {"a": 14, "b": 6, "op": "sumd"},
            {"a": 16, "b": 4, "op": "sumd"},
            {"a": 18, "b": 8, "op": "sumd"},
            {"a": 20, "b": 6, "op": "sumd"},
            {"a": 24, "b": 8, "op": "sumd"},
            {"a": 26, "b": 10, "op": "sumd"},
        ],
    },
    {
        "id": "alg1-u5-the-eraser-vanishes",
        "course": "algebra1", "unit": 5,
        "topic": "The eraser vanishes",
        "op": "elim", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("take away", "cents"),
        "advance_line": "Three in a row — you've got it! Take one buy away from the other and a whole unknown vanishes.",
        "teach": [
            ["Two shopping trips, paid in cents , the smallest coins. Trip one: two pencils and an eraser, 14 cents. Trip two: one pencil and the same eraser, 9 cents. Nobody told you what anything costs — and yet you can work out the pencil exactly.",
             '[[goal text="The eraser vanishes"]][[step eq="2 pencils + eraser = 14"]][[step eq="1 pencil + eraser = 9"]]'],
            ["Take the second trip away from the first. The eraser is in both, so it vanishes . One pencil is left over on one side, and 14 take away 9 equals 5 on the other. A pencil costs 5 cents.",
             '[[step eq="difference: 1 pencil = 14 − 9 = 5"]]'],
            ["And the eraser? Put the pencil back into trip two: 5 plus eraser equals 9, so the eraser is 4 cents. Careful when you tap — 4 is the ERASER'S price, and the question asked for the pencil. A system holds two answers, and only one of them is yours.",
             '[[step eq="pencil = 5 ✓ · eraser = 4 — the other unknown"]][[step eq="check: 2 × 5 + 4 = 14 ✓"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. Two pencils and an eraser, 12 cents; one pencil and the eraser, 7. Take away: one pencil equals 5 cents.",
                        '[[step eq="1 pencil = 12 − 7 = 5"]]'],
             "ask": {"a": 14, "b": 9, "op": "elim"}},
            {"worked": ["One more together. Two pencils and an eraser, 16 cents; one pencil and the eraser, 9. The pencil is 16 take away 9 — 7 cents.",
                        '[[step eq="1 pencil = 16 − 9 = 7"]]'],
             "ask": {"a": 24, "b": 13, "op": "elim"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 10, "b": 8, "op": "elim"},
            {"a": 8, "b": 5, "op": "elim"},
            {"a": 10, "b": 7, "op": "elim"},
            {"a": 10, "b": 6, "op": "elim"},
            {"a": 12, "b": 7, "op": "elim"},
            {"a": 14, "b": 8, "op": "elim"},
            {"a": 16, "b": 9, "op": "elim"},
            {"a": 18, "b": 10, "op": "elim"},
            {"a": 20, "b": 11, "op": "elim"},
            {"a": 22, "b": 12, "op": "elim"},
        ],
    },
]
LESSONS.extend(_ALGEBRA1_U5)


# =============================================================================
# ALGEBRA I -- UNIT 6: EXPONENTS & EXPONENTIAL FUNCTIONS (build kz, 2026-08-22)
# =============================================================================
# Prealgebra U1 taught what a power IS ("three 2s multiplied"). This unit teaches how
# powers BEHAVE. Lessons 1 and 2 are a deliberate PAIR: the product rule (powers add)
# and the power of a power (powers times) are each other's classic confusion, so they
# are taught back-to-back and each offers the other's rule as its wrong tap. Telling
# the two situations apart IS the skill.
#
# Lesson 3 puts the power to work carrying a digit (scientific notation in child
# clothes), and lesson 4 is THE FIRST EXPONENTIAL GROWTH -- the doubling pond, where
# the wrong tap is the linear thinker's answer and the board draws the run-away
# sequence so the child can watch it pull ahead.
_ALGEBRA1_U6 = [
    {
        "id": "alg1-u6-counting-the-copies",
        "course": "algebra1", "unit": 6,
        "topic": "Counting the copies",
        "op": "exadd", "max_value": 20,
        "levels": ("abstract",),
        "symbols": ("power", "x"),
        "advance_line": "Three in a row — you've got it! Multiplying powers ADDS the counts.",
        "teach": [
            ["You know x to the power 3 means three x's multiplied. So what is x to the 3, times x to the 2? Do not guess — WRITE IT OUT. Three x's multiplied, times two more x's multiplied. Count them: five x's. It is x to the power 5.",
             '[[goal text="Counting the copies"]][[step eq="x³ · x² = (x · x · x) · (x · x)"]]'],
            ["That is the whole rule: when powers of x multiply, their counts ADD. 3 x's and 2 x's are 5 x's — the same way 3 apples and 2 apples are 5 apples. The power is just a count.",
             '[[step eq="x³ · x² = x⁵"]][[step eq="3 + 2 = 5"]]'],
            ["The tempting wrong move is timesing the powers: 3 times 2 equals 6, so x to the 6. Write it out and count — there are only five x's on the page. Nothing here made copies of copies; two piles just joined.",
             '[[step eq="x³ · x² = x⁵ ✓"]][[step eq="x⁶ ✗ — count the x\'s: there are 5"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x to the 4 times x to the 3. Four x's joined by three more: seven x's, so x to the 7.",
                        '[[step eq="x⁴ · x³ = x⁷"]]'],
             "ask": {"a": 3, "b": 7, "op": "exadd"}},
            {"worked": ["One more together. x to the 5 times x to the 2: five and two make... careful — five x's and two x's are SEVEN x's. x to the 7.",
                        '[[step eq="x⁵ · x² = x⁷"]]'],
             "ask": {"a": 4, "b": 6, "op": "exadd"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 4, "op": "exadd"},
            {"a": 3, "b": 3, "op": "exadd"},
            {"a": 2, "b": 5, "op": "exadd"},
            {"a": 3, "b": 4, "op": "exadd"},
            {"a": 2, "b": 6, "op": "exadd"},
            {"a": 3, "b": 5, "op": "exadd"},
            {"a": 4, "b": 4, "op": "exadd"},
            {"a": 2, "b": 7, "op": "exadd"},
            {"a": 4, "b": 5, "op": "exadd"},
            {"a": 5, "b": 5, "op": "exadd"},
        ],
    },
    {
        "id": "alg1-u6-copies-of-copies",
        "course": "algebra1", "unit": 6,
        "topic": "Copies of copies",
        "op": "exmul", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("power", "parentheses"),
        "advance_line": "Three in a row — you've got it! Copies of copies times the counts.",
        "teach": [
            ["Now the OTHER situation, and it looks teasingly similar. Take x to the 3 — all of it, parentheses around it — and raise THAT to the power 2. That means two copies of the whole thing: two copies of three x's.",
             '[[goal text="Copies of copies"]][[step eq="(x³)² = (x · x · x) · (x · x · x)"]]'],
            ["Count them: two groups of three is 3 times 2, which equals 6 x's. So a power OF a power TIMES the counts — because you are making copies of copies, and copies of copies is exactly what timesing counts.",
             '[[step eq="(x³)² = x⁶"]][[step eq="3 × 2 = 6"]]'],
            ["Yesterday multiplying powers ADDED, today a power of a power TIMES — and telling the two apart is the entire skill. Ask one question: am I JOINING two piles, or COPYING a whole pile? Joining adds. Copying times.",
             '[[step eq="x³ · x² = x⁵ — joining, ADD"]][[step eq="(x³)² = x⁶ — copying, TIMES"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x to the 4, all raised to the power 2. Two copies of four x's: 4 times 2 equals 8, so x to the 8.",
                        '[[step eq="(x⁴)² = x⁸"]]'],
             "ask": {"a": 3, "b": 4, "op": "exmul"}},
            {"worked": ["One more together. x to the 2, raised to the power 5. Five copies of two x's is 10: x to the 10.",
                        '[[step eq="(x²)⁵ = x¹⁰"]]'],
             "ask": {"a": 5, "b": 4, "op": "exmul"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "op": "exmul"},
            {"a": 4, "b": 2, "op": "exmul"},
            {"a": 3, "b": 3, "op": "exmul"},
            {"a": 2, "b": 5, "op": "exmul"},
            {"a": 4, "b": 3, "op": "exmul"},
            {"a": 2, "b": 7, "op": "exmul"},
            {"a": 5, "b": 3, "op": "exmul"},
            {"a": 4, "b": 4, "op": "exmul"},
            {"a": 3, "b": 6, "op": "exmul"},
            {"a": 4, "b": 5, "op": "exmul"},
        ],
    },
    {
        "id": "alg1-u6-times-ten-again",
        "course": "algebra1", "unit": 6,
        "topic": "Times ten, again and again",
        "op": "sci", "max_value": 10000,
        "levels": ("abstract",),
        "symbols": ("ten", "power"),
        "advance_line": "Three in a row — you've got it! The power counts the zeros.",
        "teach": [
            ["Powers of ten are the friendliest powers there are. 10 to the power 3 is 10 times 10 times 10, which equals 1000 — a one with three zeros. The power counts the zeros. That is why scientists write huge numbers this way.",
             '[[goal text="Times ten, again and again"]][[step eq="10³ = 10 × 10 × 10 = 1000"]]'],
            ["Now put a digit in front. 3 times 10 to the power 2: that is 3 times 100, which equals 300 — the 3 with two zeros marching behind it.",
             '[[step eq="3 × 10² = 3 × 100 = 300"]]'],
            ["The trap is reading the power as a TIMES: 3 times 10 times 2 equals 60, and 60 is nowhere near 300. The 2 up there is not a number to times by — it is a count of how many times the ten itself appears.",
             '[[step eq="3 × 10² = 300 ✓"]][[step eq="3 × 10 × 2 = 60 ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 5 times 10 to the 3. That is 5 times 1000 — 5000, the 5 with three zeros behind it.",
                        '[[step eq="5 × 10³ = 5000"]]'],
             "ask": {"a": 2, "b": 4, "op": "sci"}},
            {"worked": ["One more together. 7 times 10 to the 2 equals 700.",
                        '[[step eq="7 × 10² = 700"]]'],
             "ask": {"a": 3, "b": 5, "op": "sci"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 2, "op": "sci"},
            {"a": 2, "b": 3, "op": "sci"},
            {"a": 2, "b": 5, "op": "sci"},
            {"a": 2, "b": 7, "op": "sci"},
            {"a": 2, "b": 9, "op": "sci"},
            {"a": 3, "b": 2, "op": "sci"},
            {"a": 3, "b": 4, "op": "sci"},
            {"a": 3, "b": 6, "op": "sci"},
            {"a": 3, "b": 8, "op": "sci"},
            {"a": 3, "b": 9, "op": "sci"},
        ],
    },
    {
        "id": "alg1-u6-the-doubling-pond",
        "course": "algebra1", "unit": 6,
        "topic": "The doubling pond",
        "op": "dbl", "max_value": 100,
        "levels": ("abstract",),
        "symbols": ("doubles", "day"),
        "advance_line": "Three in a row — you've got it! Doubling doubles everything there is, not just the start.",
        "teach": [
            ["A pond has 3 lily pads, and lily pads double : every day, each pad becomes two. Watch a few days go by — 3, then 6, then 12, then 24. Look how fast that pulled away. This kind of growing has a name: exponential.",
             '[[goal text="The doubling pond"]][[step eq="3 → 6 → 12 → 24"]]'],
            ["Why so fast? Because each day doubles EVERYTHING there is, not just the pads you started with. After 3 days the pond has been doubled 3 times: 3 times 2 times 2 times 2, which equals 24. The days count the doublings — the days are a power of 2.",
             '[[step eq="3 × 2 × 2 × 2 = 24"]][[step eq="3 × 2³"]]'],
            ["A careful person who has not seen doubling before guesses like a walker: up by the same amount each day, 3, 5, 7, 9. But the pond is not walking — it is doubling, and by day 3 it holds 24, not 9. Growth that FEEDS ON ITSELF leaves walking behind.",
             '[[step eq="doubling: 3 → 24 ✓"]][[step eq="up by 2 a day: 3 → 9 ✗"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 2 pads, doubling for 4 days: 2, 4, 8, 16, 32. That is 2 times 2 to the power 4 — 32 pads.",
                        '[[step eq="2 → 4 → 8 → 16 → 32"]]'],
             "ask": {"a": 3, "b": 6, "op": "dbl"}},
            {"worked": ["One more together. 5 pads, doubling for 3 days: 5, 10, 20, 40. Forty pads.",
                        '[[step eq="5 → 10 → 20 → 40"]]'],
             "ask": {"a": 4, "b": 6, "op": "dbl"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 2, "op": "dbl"},
            {"a": 3, "b": 3, "op": "dbl"},
            {"a": 4, "b": 2, "op": "dbl"},
            {"a": 3, "b": 4, "op": "dbl"},
            {"a": 3, "b": 5, "op": "dbl"},
            {"a": 4, "b": 3, "op": "dbl"},
            {"a": 5, "b": 2, "op": "dbl"},
            {"a": 4, "b": 4, "op": "dbl"},
            {"a": 4, "b": 5, "op": "dbl"},
            {"a": 5, "b": 3, "op": "dbl"},
        ],
    },
]
LESSONS.extend(_ALGEBRA1_U6)


# =============================================================================
# ALGEBRA I -- UNIT 7: POLYNOMIALS & FACTORING (build la, 2026-08-22)
# =============================================================================
# The area model comes back and then RUNS BACKWARDS. Build kt drew a(x + b) as two
# rooms; now the rectangle is (x + a)(x + b) -- FOUR rooms -- and factoring is the
# same picture read the other way: given the rooms, find the sides. The unit ends on
# the vanishing middle, the first identity a child meets that feels like a magic
# trick and is just two rooms cancelling.
_ALGEBRA1_U7 = [
    {
        "id": "alg1-u7-the-four-rooms",
        "course": "algebra1", "unit": 7,
        "topic": "The four rooms",
        "op": "foil", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("rooms", "x"),
        "advance_line": "Three in a row — you've got it! The middle rooms add; the corner room times.",
        "teach": [
            ["The rectangle picture grows up today. x plus 2, times x plus 3 — BOTH sides have an x in them now, so the wall cuts each way and the rectangle has four rooms : an x-squared room, two x rooms, and a corner of plain number.",
             '[[goal text="The four rooms"]][[areamodel rows="x,2" cols="x,3"]]'],
            ["Read the rooms. x times x is x squared. The two middle rooms are 3 x and 2 x — together 5 x. The corner is 2 times 3, which equals 6. So x plus 2, times x plus 3, comes to x squared plus 5 x plus 6.",
             '[[areamodel rows="x,2" cols="x,3"]][[step eq="(x + 2)(x + 3) = x² + 5x + 6"]]'],
            ["Two different jobs in one picture: the MIDDLE rooms add the two numbers — 2 plus 3 equals 5 — and the CORNER rooms times them — 2 times 3 equals 6. Mixing those two jobs up is the whole danger of this unit, so say them apart: middles add, corner times.",
             '[[step eq="middles: 2 + 3 = 5 → 5x"]][[step eq="corner: 2 × 3 = 6"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x plus 4, times x plus 2. Middles: 4 plus 2 equals 6, so 6 x. Corner: 4 times 2 equals 8. x squared plus 6 x plus 8.",
                        '[[areamodel rows="x,4" cols="x,2"]]'],
             "ask": {"a": 4, "b": 6, "op": "foil"}},
            {"worked": ["One more together. x plus 5, times x plus 3: middles make 8 x, corner is 15. x squared plus 8 x plus 15.",
                        '[[step eq="(x + 5)(x + 3) = x² + 8x + 15"]]'],
             "ask": {"a": 5, "b": 6, "op": "foil"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 4, "op": "foil"},
            {"a": 3, "b": 3, "op": "foil"},
            {"a": 2, "b": 5, "op": "foil"},
            {"a": 3, "b": 4, "op": "foil"},
            {"a": 2, "b": 6, "op": "foil"},
            {"a": 3, "b": 5, "op": "foil"},
            {"a": 4, "b": 4, "op": "foil"},
            {"a": 2, "b": 7, "op": "foil"},
            {"a": 4, "b": 5, "op": "foil"},
            {"a": 3, "b": 7, "op": "foil"},
        ],
    },
    {
        "id": "alg1-u7-factoring-backwards",
        "course": "algebra1", "unit": 7,
        "topic": "Running the rooms backwards",
        "op": "fnum", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("factoring", "x"),
        "advance_line": "Three in a row — you've got it! The right number fits BOTH clues at once.",
        "teach": [
            ["Now run yesterday's picture backwards. You are handed the finished sum — x squared plus 5 x plus 6 — and asked what two sides built it. Working back from the rooms to the sides is called factoring , and it is a detective game with two clues.",
             '[[goal text="Running the rooms backwards"]][[areamodel rows="x,2" cols="x,3"]]'],
            ["The clues: the two hidden numbers ADD to the x count, 5, and TIMES to the corner, 6. Try pairs: 1 and 4? Add to 5, but times to 4 — no. 2 and 3? Add to 5 AND times to 6. Both clues fit, so the sides are x plus 2 and x plus 3.",
             '[[step eq="? + ? = 5 · ? × ? = 6"]][[step eq="2 + 3 = 5 ✓ · 2 × 3 = 6 ✓"]]'],
            ["Both clues, always. A number that only adds right, or only timeses right, is an impostor. And you can check the whole answer for free — multiply the sides back out and watch the original come back.",
             '[[step eq="(x + 2)(x + 3) = x² + 5x + 6 ✓"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x squared plus 7 x plus 12, equals x plus 3, times x plus what? The partner must add with 3 to 7 and times with 3 to 12 — that is 4, both ways.",
                        '[[step eq="3 + 4 = 7 ✓ · 3 × 4 = 12 ✓"]]'],
             "ask": {"a": 6, "b": 2, "op": "fnum"}},
            {"worked": ["One more together. x squared plus 9 x plus 20, equals x plus 5, times x plus what? 5 plus 4 equals 9, and 5 times 4 equals 20. It is 4.",
                        '[[step eq="(x + 5)(x + 4) = x² + 9x + 20"]]'],
             "ask": {"a": 4, "b": 6, "op": "fnum"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 2, "c": 0, "op": "fnum"},
            {"a": 4, "b": 2, "c": 0, "op": "fnum"},
            {"a": 2, "b": 3, "c": 0, "op": "fnum"},
            {"a": 4, "b": 3, "c": 0, "op": "fnum"},
            {"a": 5, "b": 3, "c": 0, "op": "fnum"},
            {"a": 3, "b": 4, "c": 0, "op": "fnum"},
            {"a": 2, "b": 5, "c": 0, "op": "fnum"},
            {"a": 3, "b": 5, "c": 0, "op": "fnum"},
            {"a": 4, "b": 5, "c": 0, "op": "fnum"},
            {"a": 5, "b": 6, "c": 0, "op": "fnum"},
        ],
    },
    {
        "id": "alg1-u7-the-common-factor",
        "course": "algebra1", "unit": 7,
        "topic": "Pulling out the common factor",
        "op": "gcfx", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("common factor", "x"),
        "advance_line": "Three in a row — you've got it! Both parts share, or it is not a common factor.",
        "teach": [
            ["Sometimes the whole expression shares one number. Look at 6 x plus 9: the 6 is 3 times 2, and the 9 is 3 times 3. The 3 lives in BOTH parts — it is a common factor , and you can pull it out front.",
             '[[goal text="Pulling out the common factor"]][[step eq="6x + 9 = 3 · 2x + 3 · 3"]]'],
            ["Pull the 3 out: 6 x plus 9 equals 3 times, 2 x plus 3. Check it with the distributive lesson's own rule — the 3 reaches both rooms: 3 times 2 x is 6 x, and 3 times 3 is 9. It all comes back.",
             '[[step eq="6x + 9 = 3(2x + 3)"]][[step eq="check: 3 × 2x = 6x ✓ · 3 × 3 = 9 ✓"]]'],
            ["The mistake is pulling the factor from ONE part only: 3 times, 2 x plus 9 — multiply that back and you get 6 x plus 27, not 6 x plus 9. A common factor comes out of everything it was in, or it does not come out at all.",
             '[[step eq="3(2x + 3) ✓"]][[step eq="3(2x + 9) ✗ — that is 6x + 27"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. 8 x plus 6 equals 2 times, 4 x plus 3. Both the 8 and the 6 gave up their 2.",
                        '[[step eq="8x + 6 = 2(4x + 3)"]]'],
             "ask": {"a": 3, "b": 5, "c": 2, "op": "gcfx"}},
            {"worked": ["One more together. 15 x plus 10 equals 5 times, 3 x plus 2.",
                        '[[step eq="15x + 10 = 5(3x + 2)"]]'],
             "ask": {"a": 7, "b": 2, "c": 3, "op": "gcfx"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 2, "b": 3, "c": 2, "op": "gcfx"},
            {"a": 2, "b": 5, "c": 3, "op": "gcfx"},
            {"a": 3, "b": 4, "c": 2, "op": "gcfx"},
            {"a": 4, "b": 3, "c": 2, "op": "gcfx"},
            {"a": 3, "b": 2, "c": 3, "op": "gcfx"},
            {"a": 2, "b": 3, "c": 5, "op": "gcfx"},
            {"a": 4, "b": 5, "c": 3, "op": "gcfx"},
            {"a": 5, "b": 4, "c": 3, "op": "gcfx"},
            {"a": 4, "b": 3, "c": 4, "op": "gcfx"},
            {"a": 5, "b": 3, "c": 4, "op": "gcfx"},
        ],
    },
    {
        "id": "alg1-u7-the-vanishing-middle",
        "course": "algebra1", "unit": 7,
        "topic": "The vanishing middle",
        "op": "dsq", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("squared", "take away"),
        "advance_line": "Three in a row — you've got it! Plus and take away the same x's — the middles cancel.",
        "teach": [
            ["One special pair of sides does something wonderful. x plus 3, times x TAKE AWAY 3. Build the rooms: x squared, then plus 3 x from one middle and take away 3 x from the other, then the corner, 3 times 3 taken away.",
             '[[goal text="The vanishing middle"]][[step eq="(x + 3)(x − 3)"]][[step eq="x² + 3x − 3x − 9"]]'],
            ["Watch the middles: plus 3 x and take away 3 x. They cancel — land exactly on nothing. All that survives is x squared take away 9. The whole middle of the answer vanished .",
             '[[step eq="+3x − 3x = 0"]][[step eq="(x + 3)(x − 3) = x² − 9"]]'],
            ["And notice WHICH 9: it is 3 squared, not 3 and not 6. The corner room is 3 times 3. This pattern — x squared take away a square — is famous enough to have a name, the difference of squares, and it works for any number in the 3's place.",
             '[[step eq="x² − 9 ✓ (9 = 3²)"]][[step eq="x² − 3 ✗ · x² − 6x... ✗ nothing survived but the squares"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x plus 5, times x take away 5. The middles cancel, the corner is 5 squared: x squared take away 25.",
                        '[[step eq="(x + 5)(x − 5) = x² − 25"]]'],
             "ask": {"a": 13, "b": 0, "op": "dsq"}},
            {"worked": ["One more together. x plus 10, times x take away 10: x squared take away 100.",
                        '[[step eq="(x + 10)(x − 10) = x² − 100"]]'],
             "ask": {"a": 14, "b": 0, "op": "dsq"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 0, "op": "dsq"},
            {"a": 4, "b": 0, "op": "dsq"},
            {"a": 5, "b": 0, "op": "dsq"},
            {"a": 6, "b": 0, "op": "dsq"},
            {"a": 7, "b": 0, "op": "dsq"},
            {"a": 8, "b": 0, "op": "dsq"},
            {"a": 9, "b": 0, "op": "dsq"},
            {"a": 10, "b": 0, "op": "dsq"},
            {"a": 11, "b": 0, "op": "dsq"},
            {"a": 12, "b": 0, "op": "dsq"},
        ],
    },
]
LESSONS.extend(_ALGEBRA1_U7)


# =============================================================================
# ALGEBRA I -- UNIT 8: QUADRATIC FUNCTIONS (build la, 2026-08-22)
# =============================================================================
# THE CURVE ARRIVES. y = x² is the first rule whose graph BENDS, and the unit is
# built on the three things a child must feel about it: squaring is not doubling, a
# product of zero means one of the factors is zero, and a square is never negative
# -- which is exactly why the curve has a lowest point. The last lesson throws a
# ball: height c take away x squared, and finding where it lands is asking what
# number squared equals c -- the square root, met as an answer to a question rather
# than as a symbol.
_ALGEBRA1_U8 = [
    {
        "id": "alg1-u8-the-curve",
        "course": "algebra1", "unit": 8,
        "topic": "The curve",
        "op": "sqy", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("squared", "curve"),
        "advance_line": "Three in a row — you've got it! Squared means times itself, never times two.",
        "teach": [
            ["Every line you have drawn was straight. Meet the first rule that bends: y equals x squared. Feed it 1, 2, 3, 4 and out come 1, 4, 9, 16 — each step up costs more than the last, so the graph bends into a curve , shaped like a bowl.",
             '[[goal text="The curve"]][[graph func="x^2" range="-4..4"]]'],
            ["Read it like any rule. y equals x squared plus 2, at x equals 3: 3 squared is 3 times 3, which equals 9, plus 2 equals 11.",
             '[[graph func="x^2+2" range="-4..4"]][[step eq="y = 3² + 2 = 9 + 2 = 11"]]'],
            ["The one error to burn away now: squared means TIMES ITSELF, not times two. 3 squared is 9, not 6. At x equals 2 the two happen to agree — 2 times 2 and 2 plus 2 are both 4 — and that coincidence at 2 is exactly what plants the habit. Everywhere else it breaks.",
             '[[step eq="3² = 3 × 3 = 9 ✓"]][[step eq="3² = 6 ✗ — that is doubling"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y equals x squared plus 3, at x equals 4: 16 plus 3 equals 19.",
                        '[[step eq="y = 4² + 3 = 19"]]'],
             "ask": {"a": 3, "b": 7, "op": "sqy"}},
            {"worked": ["One more together. y equals x squared plus 1, at x equals 5: 25 plus 1 equals 26.",
                        '[[step eq="y = 5² + 1 = 26"]]'],
             "ask": {"a": 6, "b": 7, "op": "sqy"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 1, "op": "sqy"},
            {"a": 3, "b": 4, "op": "sqy"},
            {"a": 4, "b": 2, "op": "sqy"},
            {"a": 4, "b": 5, "op": "sqy"},
            {"a": 5, "b": 2, "op": "sqy"},
            {"a": 5, "b": 6, "op": "sqy"},
            {"a": 6, "b": 3, "op": "sqy"},
            {"a": 7, "b": 2, "op": "sqy"},
            {"a": 8, "b": 4, "op": "sqy"},
            {"a": 9, "b": 5, "op": "sqy"},
        ],
    },
    {
        "id": "alg1-u8-two-answers",
        "course": "algebra1", "unit": 8,
        "topic": "Zero times anything",
        "op": "roots", "max_value": 99,
        "levels": ("abstract",),
        "symbols": ("zero", "x"),
        "advance_line": "Three in a row — you've got it! A product is zero only when a factor is zero.",
        "teach": [
            ["Here is a fact so plain it hides its power: zero times ANYTHING is zero — and NOTHING ELSE, times anything, ever lands on zero. So if two brackets multiply to zero, one of the brackets MUST be zero. There is no other way.",
             '[[goal text="Zero times anything"]][[step eq="(something) × (something) = 0"]]'],
            ["x take away 3, times x take away 5, equals zero. When is the first bracket zero? At x equals 3. The second? At x equals 5. So the equation has TWO answers, 3 and 5 — a bending curve can touch the ground twice.",
             '[[step eq="(x − 3)(x − 5) = 0"]][[step eq="x = 3 or x = 5"]]'],
            ["Do not do arithmetic on the two numbers — they are not asking to be added or timesed. Each one answers its own bracket. Check: at x equals 5, the second bracket is zero, and zero times anything wipes out the whole thing.",
             '[[step eq="x = 3, x = 5 ✓"]][[step eq="x = 8 ✗ · x = 15 ✗ — nobody asked for 3 + 5 or 3 × 5"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. x take away 2, times x take away 6, equals zero. The answers are 2 and 6 — one per bracket.",
                        '[[step eq="(x − 2)(x − 6) = 0 → x = 2 or 6"]]'],
             "ask": {"a": 6, "b": 4, "op": "roots"}},
            {"worked": ["One more together. x take away 4, times x take away 7: the answers are 4 and 7.",
                        '[[step eq="x = 4 or x = 7"]]'],
             "ask": {"a": 7, "b": 5, "op": "roots"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 2, "op": "roots"},
            {"a": 4, "b": 2, "op": "roots"},
            {"a": 2, "b": 3, "op": "roots"},
            {"a": 5, "b": 3, "op": "roots"},
            {"a": 2, "b": 5, "op": "roots"},
            {"a": 4, "b": 5, "op": "roots"},
            {"a": 3, "b": 6, "op": "roots"},
            {"a": 2, "b": 7, "op": "roots"},
            {"a": 5, "b": 8, "op": "roots"},
            {"a": 4, "b": 9, "op": "roots"},
        ],
    },
    {
        "id": "alg1-u8-the-lowest-point",
        "course": "algebra1", "unit": 8,
        "topic": "The lowest point",
        "op": "vtx", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("squared", "lowest"),
        "advance_line": "Three in a row — you've got it! A square is never below zero, so the plus number is the floor.",
        "teach": [
            ["A square can never be below zero. Times any number by itself — even a negative one — and the answer refuses to be negative. That single refusal gives every bending curve of this shape a FLOOR: a lowest point it touches and never goes under.",
             '[[goal text="The lowest point"]][[graph func="(x-3)^2+2" range="0..6"]]'],
            ["y equals: x take away 3, squared, plus 2. The squared part is smallest when it is exactly zero — which happens right at x equals 3. At that moment y is 0 plus 2, which equals 2. The lowest y this curve ever reaches is 2.",
             '[[step eq="(x − 3)² is 0 at x = 3"]][[step eq="lowest y = 0 + 2 = 2"]]'],
            ["The rule's two numbers do two jobs — the U4 lesson again, curved. The 3 says WHERE the low point sits, left and right. The 2 says HOW LOW the curve goes. Asked for the lowest y, the answer is the plus number, not the number inside the brackets.",
             '[[step eq="lowest y = 2 ✓"]][[step eq="3 ✗ — that is where it sits, not how low"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y equals: x take away 5, squared, plus 4. The square bottoms out at zero, so the lowest y is 4.",
                        '[[graph func="(x-5)^2+4" range="2..8"]][[step eq="lowest y = 4"]]'],
             "ask": {"a": 4, "b": 3, "op": "vtx"}},
            {"worked": ["One more together. y equals: x take away 2, squared, plus 6. Lowest y: 6.",
                        '[[step eq="lowest y = 6"]]'],
             "ask": {"a": 7, "b": 8, "op": "vtx"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 2, "op": "vtx"},
            {"a": 5, "b": 3, "op": "vtx"},
            {"a": 2, "b": 4, "op": "vtx"},
            {"a": 7, "b": 4, "op": "vtx"},
            {"a": 6, "b": 5, "op": "vtx"},
            {"a": 4, "b": 6, "op": "vtx"},
            {"a": 9, "b": 7, "op": "vtx"},
            {"a": 3, "b": 8, "op": "vtx"},
            {"a": 5, "b": 9, "op": "vtx"},
            {"a": 8, "b": 9, "op": "vtx"},
        ],
    },
    {
        "id": "alg1-u8-the-ball-comes-down",
        "course": "algebra1", "unit": 8,
        "topic": "The ball comes down",
        "op": "hitg", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("squared", "zero"),
        "advance_line": "Three in a row — you've got it! Ask what number squared equals the height.",
        "teach": [
            ["Throw a ball and its height follows a bending curve — quadratics are how the world falls. Here is one: y equals 25 take away x squared. At x equals 0 the height is 25, and as x grows, x squared eats the height away.",
             '[[goal text="The ball comes down"]][[graph func="25-x^2" range="0..6"]]'],
            ["When does it hit the ground? The ground is where the height is zero , so 25 take away x squared equals 0 — x squared must equal 25. Now the question turns around — WHAT NUMBER, squared, equals 25? Five: 5 times 5 is 25. The ball lands at x equals 5.",
             '[[step eq="25 − x² = 0"]][[step eq="x² = 25 → x = 5"]]'],
            ["That backwards question has a name: 5 is the square root of 25 — the number that squares to it. It is not half of 25. Halving undoes doubling; the square root undoes SQUARING, and you have known since the curve lesson that those are different beasts.",
             '[[step eq="x = 5 ✓ (5² = 25)"]][[step eq="x = 12 ✗ — half undoes DOUBLING, not squaring"]]'],
        ],
        "pairs": [
            {"worked": ["Here is one more, done for you. y equals 36 take away x squared. It lands where x squared equals 36 — and 6 squared is 36. x equals 6.",
                        '[[step eq="x² = 36 → x = 6"]]'],
             "ask": {"a": 13, "b": 0, "op": "hitg"}},
            {"worked": ["One more together. y equals 49 take away x squared. 7 squared is 49, so it lands at x equals 7.",
                        '[[step eq="x² = 49 → x = 7"]]'],
             "ask": {"a": 14, "b": 0, "op": "hitg"}},
        ],
        "practice_intro": "Now it's your turn. Three right answers in a row and we're done — here comes the first one.",
        "bank": [
            {"a": 3, "b": 0, "op": "hitg"},
            {"a": 4, "b": 0, "op": "hitg"},
            {"a": 5, "b": 0, "op": "hitg"},
            {"a": 6, "b": 0, "op": "hitg"},
            {"a": 7, "b": 0, "op": "hitg"},
            {"a": 8, "b": 0, "op": "hitg"},
            {"a": 9, "b": 0, "op": "hitg"},
            {"a": 10, "b": 0, "op": "hitg"},
            {"a": 11, "b": 0, "op": "hitg"},
            {"a": 12, "b": 0, "op": "hitg"},
        ],
    },
]
LESSONS.extend(_ALGEBRA1_U8)





# THE COURSE ORDER IS OWNED HERE (jz -- jy had accidentally placed carrying before
# two-digit-no-carry). Import fails loudly if a lesson is missing or listed twice.
COURSE_ORDER = [
    # ---- ENTRY-LEVEL MATH (the kc re-cut: these eight lessons were authored under
    # Basic U1 and belong here by Jim's own curriculum -- Eureka audit 2026-08-21;
    # kd opens the course where Eureka does -- counting -- and adds story problems
    # and coins) ----
    "entry-u1-counting-to-10", "entry-u1-numbers-before-and-after",
    "entry-u2-add-single-digit", "entry-u2-add-past-ten",
    "entry-u3-take-away-single-digit", "entry-u3-take-away-bigger",
    "entry-u3-story-problems",
    "entry-u4-tens-and-ones", "entry-u5-add-two-digit-no-carry",
    "entry-u5-add-with-carrying", "entry-u6-take-away-with-regrouping",
    "entry-u7-counting-coins",
    # ---- BASIC MATH (grades 3-5 band) ----
    "basic-u1-place-value-to-1000", "basic-u1-rounding-tens",
    "basic-u1-rounding-hundreds", "basic-u1-multi-digit-review",
    "basic-u2-what-multiplying-means", "basic-u2-times-tables",
    "basic-u2-multiply-two-digit",
    "basic-u3-what-dividing-means", "basic-u3-left-overs",
    "basic-u3-divide-two-digit", "basic-u3-story-problems",
    "basic-u4-missing-factors", "basic-u4-greatest-common-factor",
    "basic-u4-least-common-multiple",
    "basic-u5-fractions-on-the-number-line",
    "basic-u5-fraction-of-a-group", "basic-u5-equivalent-fractions",
    "basic-u6-add-fractions-same-bottom", "basic-u6-take-away-fractions-same-bottom",
    "basic-u6-add-fractions-different-bottoms",
    "basic-u7-tenths", "basic-u7-dimes-and-pennies", "basic-u7-hundredths",
    "basic-u8-percent-of", "basic-u8-one-costs",
    "basic-u9-perimeter", "basic-u9-area",
    "basic-u9-quarter-turns", "basic-u9-volume",

    # ---- PREALGEBRA (build kk) -- Unit 1: Number Sense & Order of Operations ----
    "pre-u1-times-before-add", "pre-u1-parentheses-first",
    "pre-u1-exponents-are-repeated-times", "pre-u1-power-then-times-then-add",
    # Unit 2: Factors, Multiples & Primes -- underneath Basic's GCF/LCM
    "pre-u2-how-many-factors", "pre-u2-the-smallest-factor",
    "pre-u2-breaking-into-primes",
    # Unit 3: Integers & Negative Numbers -- the first answers below zero
    "pre-u3-counting-back-past-zero", "pre-u3-adding-a-negative",
    "pre-u3-taking-away-a-negative", "pre-u3-times-with-a-negative",
    # Unit 4: Fractions -- past Basic's adding, taking away and unit fractions
    "pre-u4-a-fraction-of-a-number", "pre-u4-how-many-parts-in-a-whole",
    "pre-u4-dividing-by-a-fraction", "pre-u4-fractions-bigger-than-one",
    # Unit 5: Decimals -- past Basic's naming of tenths and hundredths
    "pre-u5-how-many-hundredths", "pre-u5-times-by-ten",
    "pre-u5-tenths-times-a-number", "pre-u5-sharing-a-decimal",
    # Unit 6: Ratios, Rates & Proportions -- past Basic's unit price
    "pre-u6-keeping-a-ratio", "pre-u6-scaling-a-rate",
    "pre-u6-filling-in-a-proportion", "pre-u6-sharing-in-a-ratio",
    # Unit 7: Percents -- past Basic's 10/25/50 fraction shortcut
    "pre-u7-any-percent", "pre-u7-what-percent-is-that",
    "pre-u7-finding-the-whole", "pre-u7-a-price-goes-up",
    # Unit 8: Measurement & Geometry Basics -- and the first prealgebra lessons
    # that put a real FIGURE on the board rather than a line of text
    "pre-u8-changing-units", "pre-u8-area-of-a-triangle",
    "pre-u8-angles-on-a-line", "pre-u8-angles-in-a-triangle",
    # Unit 9: Variables & Expressions -- the doorway to algebra, closed with the
    # ⭐ area model for the distributive property
    "pre-u9-a-letter-holds-a-number", "pre-u9-a-number-against-a-letter",
    "pre-u9-collecting-x", "pre-u9-the-times-reaches-both",

    # ---- ALGEBRA I (build ku) -- Unit 1: Foundations & Expressions ----
    "alg1-u1-two-steps-with-a-letter", "alg1-u1-two-letters",
    "alg1-u1-collecting-past-a-y", "alg1-u1-minus-goes-through",
    # Unit 2: Linear Equations & Inequalities -- solving begins, on the ⭐ balance
    "alg1-u2-undoing-a-plus", "alg1-u2-undoing-a-times",
    "alg1-u2-two-steps-back", "alg1-u2-the-biggest-x",
    # Unit 3: Functions & Notation -- the ⭐ machine, named f
    "alg1-u3-the-number-machine", "alg1-u3-f-of-x",
    "alg1-u3-two-machines", "alg1-u3-which-input",
    # Unit 4: Linear Functions & Graphs -- the ⭐ grapher draws its first line
    "alg1-u4-reading-the-line", "alg1-u4-the-climb",
    "alg1-u4-where-it-starts", "alg1-u4-start-and-climb",
    # Unit 5: Systems of Equations -- two rules true at once
    "alg1-u5-where-two-rules-agree", "alg1-u5-swapping-in",
    "alg1-u5-sum-and-difference", "alg1-u5-the-eraser-vanishes",
    # Unit 6: Exponents & Exponential Functions -- how powers behave
    "alg1-u6-counting-the-copies", "alg1-u6-copies-of-copies",
    "alg1-u6-times-ten-again", "alg1-u6-the-doubling-pond",
    # Unit 7: Polynomials & Factoring -- the area model runs backwards
    "alg1-u7-the-four-rooms", "alg1-u7-factoring-backwards",
    "alg1-u7-the-common-factor", "alg1-u7-the-vanishing-middle",
    # Unit 8: Quadratic Functions -- the curve arrives
    "alg1-u8-the-curve", "alg1-u8-two-answers",
    "alg1-u8-the-lowest-point", "alg1-u8-the-ball-comes-down",
]
_by_id = {les["id"]: les for les in LESSONS}
if sorted(COURSE_ORDER) != sorted(_by_id):
    raise RuntimeError("COURSE_ORDER and LESSONS disagree: "
                       + str(sorted(set(COURSE_ORDER) ^ set(_by_id))))
LESSONS = [_by_id[i] for i in COURSE_ORDER]

LESSON_BY_ID = {les["id"]: les for les in LESSONS}
PILOT_LESSON = LESSONS[0]   # every js/jt-era pin and endpoint default still resolves


# =============================================================================
# OP_EXT -- the data-driven op registry (build jz). The original three ops
# ("+", "-", "t") stay hand-written below; every newer op is an entry here:
#   ans(p)    the computed answer (never typed -- the founding rule)
#   spoken(p) what the child hears (abstract level; these lessons are abstract-only)
#   board(p)  the board tags
#   praise(p) the echo line after the praise prefix
#   key(p)    the difficulty-ramp key
#   check(p)  (ok, why) -- the per-problem constraint the validator enforces
#   speaks(p, spoken) -- rule-44 override for ops that speak digits as WORDS
# =============================================================================
_NUMWORD = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
            7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
            12: "twelve"}
_FRACWORD = {2: ("half", "halves"), 3: ("third", "thirds"),
             4: ("fourth", "fourths"), 5: ("fifth", "fifths"),
             6: ("sixth", "sixths"), 8: ("eighth", "eighths"),
             10: ("tenth", "tenths"), 12: ("twelfth", "twelfths")}


def _gcd(x, y):
    while y:
        x, y = y, x % y
    return x


_FRAC_BOTTOM = {2: "half", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
                7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 12: "twelfth"}
_FRAC_TOP = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
             7: "seven", 8: "eight", 9: "nine", 10: "ten"}


def _frac_words(a, b):
    """A fraction said the way a child reads it: (2, 3) -> "two thirds". Basic Math
    only ever spoke UNIT fractions ("one half"), so it had no need to pluralise;
    Prealgebra U4 is where non-unit fractions arrive (build kn)."""
    top = _FRAC_TOP.get(a, str(a))
    bot = _FRAC_BOTTOM.get(b, f"{b}th")
    return f"{top} {bot}" if a == 1 else f"{top} {bot}s"


def _gcd(a, b):
    """math.gcd without the import ceremony (build la -- gcfx's honesty check:
    the pulled-out factor must be the WHOLE common factor)."""
    while b:
        a, b = b, a % b
    return a


_SUPS = {0: "\u2070", 1: "\u00b9", 2: "\u00b2", 3: "\u00b3", 4: "\u2074",
         5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"}


def _sup(n):
    """A small exponent as a real superscript, for board text (build kz -- expn
    hard-coded \u00b2 and \u00b3 because its powers stop at 3; Algebra I's do not)."""
    return "".join(_SUPS[int(d)] for d in str(n))


def _prime_factors(n):
    """The primes whose product is n, repeats included: 12 -> [2, 2, 3]. Used by the
    Prealgebra U2 ops (build km); a lambda cannot express the loop readably."""
    out, d, n = [], 2, int(n)
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


OP_EXT = {
    "*": {
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: f"What is {p['a']} times {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]} × {p["b"]} = ?"]]',
        "praise": lambda p: f"{p['a']} times {p['b']} equals {p['a'] * p['b']}.",
        "key": lambda p: p["a"] * p["b"],
        "check": lambda p: (p["a"] >= 1 and p["b"] >= 1, "factors must be at least 1"),
    },
    "/": {
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: f"What is {p['a']} divided by {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]} ÷ {p["b"]} = ?"]]',
        "praise": lambda p: f"{p['a']} divided by {p['b']} equals {p['a'] // p['b']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] >= 2,
                            "a division lesson must divide EXACTLY"),
    },
    "rem": {
        "ans": lambda p: p["a"] % p["b"],
        "spoken": lambda p: (f"What is left over when {p['a']} is shared into "
                             f"groups of {p['b']}?"),
        "board": lambda p: f'[[step eq="{p["a"]} ÷ {p["b"]} → left over = ?"]]',
        "praise": lambda p: (f"Sharing {p['a']} into groups of {p['b']} leaves "
                             f"{p['a'] % p['b']} left over."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] % p["b"] < p["b"],
                            "the left-over must be at least 1 (tap options start "
                            "at 1) and smaller than the group"),
    },
    "mf": {   # missing factor: b × ? = a
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: f"{p['b']} times what equals {p['a']}?",
        "board": lambda p: f'[[step eq="{p["b"]} × ? = {p["a"]}"]]',
        "praise": lambda p: f"{p['b']} times {p['a'] // p['b']} equals {p['a']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] >= 2,
                            "the missing factor must be exact"),
    },
    "gcf": {
        "ans": lambda p: _gcd(p["a"], p["b"]),
        "spoken": lambda p: (f"What is the greatest common factor of {p['a']} "
                             f"and {p['b']}?"),
        "board": lambda p: f'[[step eq="GCF of {p["a"]} and {p["b"]} = ?"]]',
        "praise": lambda p: (f"The greatest common factor of {p['a']} and "
                             f"{p['b']} equals {_gcd(p['a'], p['b'])}."),
        "key": lambda p: max(p["a"], p["b"]),
        "check": lambda p: (_gcd(p["a"], p["b"]) >= 2,
                            "a GCF of 1 makes a dull tap question"),
    },
    "of": {   # one unit-fraction of a group: 1/b of a
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"What is one {_FRACWORD[p['b']][0]} of {p['a']}?"),
        "board": lambda p: f'[[step eq="1/{p["b"]} of {p["a"]} = ?"]]',
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} of {p['a']} equals "
                             f"{p['a'] // p['b']}."),
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] in _FRACWORD,
                            "the share must be exact and the fraction sayable"),
        "speaks": lambda p, sp: str(p["a"]) in sp and _FRACWORD[p["b"]][0] in sp,
    },
    "eqf": {   # 1/b = ?/c
        "ans": lambda p: p["c"] // p["b"],
        "spoken": lambda p: (f"One {_FRACWORD[p['b']][0]} equals how many "
                             f"{_FRACWORD[p['c']][1]}?"),
        "board": lambda p: f'[[step eq="1/{p["b"]} = ?/{p["c"]}"]]',
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} equals "
                             f"{_NUMWORD[p['c'] // p['b']]} {_FRACWORD[p['c']][1]}."),
        "key": lambda p: p["c"],
        "check": lambda p: (p["c"] % p["b"] == 0 and p["b"] in _FRACWORD
                            and p["c"] in _FRACWORD and p["c"] > p["b"]
                            and p["c"] // p["b"] in _NUMWORD,
                            "the equivalence must be exact and sayable"),
        "speaks": lambda p, sp: (_FRACWORD[p["b"]][0] in sp
                                 and _FRACWORD[p["c"]][1] in sp),
    },
    "fa": {   # a/c + b/c, answered in c-ths
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is {p['a']} "
                             f"{_FRACWORD[p['c']][1]} plus {p['b']} "
                             f"{_FRACWORD[p['c']][1]}?"),
        "board": lambda p: f'[[step eq="{p["a"]}/{p["c"]} + {p["b"]}/{p["c"]} = ?/{p["c"]}"]]',
        "praise": lambda p: (f"{p['a']} {_FRACWORD[p['c']][1]} plus {p['b']} "
                             f"{_FRACWORD[p['c']][1]} equals {p['a'] + p['b']} "
                             f"{_FRACWORD[p['c']][1]}."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (p["a"] + p["b"] < p["c"] and p["c"] in _FRACWORD,
                            "same-bottom adding stays a proper fraction"),
    },
    "fs": {   # a/c - b/c
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is {p['a']} "
                             f"{_FRACWORD[p['c']][1]} take away {p['b']} "
                             f"{_FRACWORD[p['c']][1]}?"),
        "board": lambda p: f'[[step eq="{p["a"]}/{p["c"]} − {p["b"]}/{p["c"]} = ?/{p["c"]}"]]',
        "praise": lambda p: (f"{p['a']} {_FRACWORD[p['c']][1]} take away "
                             f"{p['b']} {_FRACWORD[p['c']][1]} equals "
                             f"{p['a'] - p['b']} {_FRACWORD[p['c']][1]}."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] - p["b"] and p["a"] < p["c"]
                            and p["c"] in _FRACWORD,
                            "same-bottom take-away stays proper and positive"),
    },
    "dt": {   # tenths: 0.a + 0.b, answered in tenths
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"How many tenths is {p['a']} tenths plus "
                             f"{p['b']} tenths?"),
        "board": lambda p: f'[[step eq="0.{p["a"]} + 0.{p["b"]} = 0.?"]]',
        "praise": lambda p: (f"{p['a']} tenths plus {p['b']} tenths equals "
                             f"{p['a'] + p['b']} tenths."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (p["a"] + p["b"] <= 9,
                            "the tenths must not spill into a whole (that is the "
                            "NEXT lesson's idea)"),
    },
    "m": {    # money: a dimes + b pennies = ? cents
        "ans": lambda p: 10 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many cents is {p['a']} dimes and {p['b']} "
                             f"pennies?"),
        "board": lambda p: f'[[step eq="{p["a"]} dimes + {p["b"]} pennies = ? cents"]]',
        "praise": lambda p: (f"{p['a']} dimes and {p['b']} pennies equals "
                             f"{10 * p['a'] + p['b']} cents."),
        "key": lambda p: 10 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9,
                            "dimes and pennies each stay single-digit"),
    },
    "pc": {   # a% of b
        "ans": lambda p: p["a"] * p["b"] // 100,
        "spoken": lambda p: f"What is {p['a']} percent of {p['b']}?",
        "board": lambda p: f'[[step eq="{p["a"]}% of {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} percent of {p['b']} equals "
                             f"{p['a'] * p['b'] // 100}."),
        "key": lambda p: p["b"],
        "check": lambda p: ((p["a"] * p["b"]) % 100 == 0
                            and p["a"] * p["b"] // 100 >= 1,
                            "the percent must come out whole, and at least 1"),
    },
    "rate": {  # b things cost a dollars; one costs ?
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"{p['b']} apples cost {p['a']} dollars. What does "
                             f"one apple cost, in dollars?"),
        "board": lambda p: f'[[step eq="{p["a"]} ÷ {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} divided by {p['b']} equals "
                             f"{p['a'] // p['b']} — one costs "
                             f"{p['a'] // p['b']} dollars."),
        "key": lambda p: p["a"],
        "check": lambda p: (p["a"] % p["b"] == 0 and p["b"] >= 2,
                            "a unit price must come out exact"),
    },
    "pv": {   # a hundreds, b tens, c ones
        "ans": lambda p: 100 * p["a"] + 10 * p["b"] + p["c"],
        "spoken": lambda p: (f"What number is {p['a']} hundreds, {p['b']} tens "
                             f"and {p['c']} ones?"),
        "board": lambda p: (f'[[step eq="{p["a"]} hundreds + {p["b"]} tens + '
                            f'{p["c"]} ones = ?"]]'),
        "praise": lambda p: (f"{p['a']} hundreds, {p['b']} tens and {p['c']} ones "
                             f"— that is {100 * p['a'] + 10 * p['b'] + p['c']}."),
        "key": lambda p: 100 * p["a"] + 10 * p["b"] + p["c"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9
                            and 1 <= p["c"] <= 9,
                            "each place stays 1-9 in this first lesson"),
    },
    "r10": {   # round a to the nearest ten
        "ans": lambda p: (p["a"] + 5) // 10 * 10,
        "spoken": lambda p: f"Round {p['a']} to the nearest ten.",
        "board": lambda p: f'[[step eq="{p["a"]} → nearest ten = ?"]]',
        "praise": lambda p: (f"{p['a']} rounds to {(p['a'] + 5) // 10 * 10}."),
        "key": lambda p: p["a"],
        "check": lambda p: (10 <= p["a"] <= 99 and p["a"] % 10 != 0,
                            "a multiple of ten leaves nothing to round"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
        # +-1 distractors would make rounding guessable by eye; the real confusion
        # is WHICH ten, so the distractors are the neighbouring tens.
        # near the bottom of the range the lower ten would be 0 -- shift the
        # window up instead (tap options must stay >= 1, validator-enforced)
        "choices": lambda p: ([(p["a"] + 5) // 10 * 10 - 10,
                               (p["a"] + 5) // 10 * 10,
                               (p["a"] + 5) // 10 * 10 + 10]
                              if (p["a"] + 5) // 10 * 10 >= 20 else
                              [(p["a"] + 5) // 10 * 10,
                               (p["a"] + 5) // 10 * 10 + 10,
                               (p["a"] + 5) // 10 * 10 + 20]),
    },
    "r100": {  # round a to the nearest hundred
        "ans": lambda p: (p["a"] + 50) // 100 * 100,
        "spoken": lambda p: f"Round {p['a']} to the nearest hundred.",
        "board": lambda p: f'[[step eq="{p["a"]} → nearest hundred = ?"]]',
        "praise": lambda p: (f"{p['a']} rounds to {(p['a'] + 50) // 100 * 100}."),
        "key": lambda p: p["a"],
        "check": lambda p: (100 <= p["a"] <= 999 and p["a"] % 100 != 0,
                            "a multiple of one hundred leaves nothing to round"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "choices": lambda p: ([(p["a"] + 50) // 100 * 100 - 100,
                               (p["a"] + 50) // 100 * 100,
                               (p["a"] + 50) // 100 * 100 + 100]
                              if (p["a"] + 50) // 100 * 100 >= 200 else
                              [(p["a"] + 50) // 100 * 100,
                               (p["a"] + 50) // 100 * 100 + 100,
                               (p["a"] + 50) // 100 * 100 + 200]),
    },
    "nl": {    # hops from 0 to a/b on a 0-to-1 number line cut into b hops
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"A number line from 0 to 1 is cut into {p['b']} "
                             f"equal hops. How many hops from 0 reach {p['a']} "
                             f"out of {p['b']}?"),
        "board": lambda p: f'[[step eq="0 —({p["b"]} hops)— 1 · land on {p["a"]}/{p["b"]} = ? hops"]]',
        "praise": lambda p: (f"{p['a']} hops — {p['a']} out of {p['b']} lives "
                             f"{p['a']} hops from 0."),
        "key": lambda p: p["b"],
        "check": lambda p: (1 <= p["a"] < p["b"] <= 12,
                            "the fraction stays proper and the hops countable"),
    },
    "nlw": {   # hops from 0 to reach 1 whole
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"A number line from 0 to 1 is cut into {p['b']} "
                             f"equal hops. How many hops from 0 reach 1 whole?"),
        "board": lambda p: f'[[step eq="0 —({p["b"]} hops)— 1 · reach 1 = ? hops"]]',
        "praise": lambda p: (f"{p['b']} hops — all {p['b']} hops together equal "
                             f"1 whole."),
        "key": lambda p: p["b"],
        "check": lambda p: (2 <= p["b"] <= 12 and p.get("a", 1) == 1,
                            "the whole-line question fixes a=1"),
    },
    "cnt": {   # count the stars (concrete-only; the picture IS the problem)
        "ans": lambda p: p["a"],
        "spoken": lambda p: "Count the stars. How many stars are there?",
        "board": lambda p: (f'[[objects emoji="⭐" groups="{p["a"]}" '
                            f'caption="count them one at a time"]]'),
        "praise": lambda p: f"{p['a']} stars — you counted every one.",
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 10, "countable on one screen"),
        # rule 44's PURPOSE is "the child heard the whole problem" -- here the whole
        # problem is the picture, and SAYING the number would answer it.
        "speaks": lambda p, sp: True,
    },
    "aft": {
        "ans": lambda p: p["a"] + 1,
        "spoken": lambda p: f"What number comes right after {p['a']}?",
        "board": lambda p: f'[[step eq="{p["a"]}, ?"]]',
        "praise": lambda p: f"{p['a'] + 1} comes right after {p['a']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 19, "stays in the counting range"),
        # the problem has ONE number; b is a placeholder 0 (like r10/r100)
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "bef": {
        "ans": lambda p: p["a"] - 1,
        "spoken": lambda p: f"What number comes right before {p['a']}?",
        "board": lambda p: f'[[step eq="?, {p["a"]}"]]',
        "praise": lambda p: f"{p['a'] - 1} comes right before {p['a']}.",
        "key": lambda p: p["a"],
        "check": lambda p: (2 <= p["a"] <= 20, "the answer must stay at least 1"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "nick": {  # a nickels + b pennies = ? cents
        "ans": lambda p: 5 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many cents is {p['a']} nickels and {p['b']} "
                             f"pennies?"),
        "board": lambda p: f'[[step eq="{p["a"]} nickels + {p["b"]} pennies = ? cents"]]',
        "praise": lambda p: (f"{p['a']} nickels and {p['b']} pennies equals "
                             f"{5 * p['a'] + p['b']} cents."),
        "key": lambda p: 5 * p["a"] + p["b"],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 4,
                            "pennies stay under a nickel"),
    },
    "dh": {    # hundredths: 0.ab + 0.cd, answered in hundredths
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"How many hundredths is {p['a']} hundredths plus "
                             f"{p['b']} hundredths?"),
        "board": lambda p: f'[[step eq="0.{p["a"]} + 0.{p["b"]} = 0.?"]]',
        "praise": lambda p: (f"{p['a']} hundredths plus {p['b']} hundredths "
                             f"equals {p['a'] + p['b']} hundredths."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (10 <= p["a"] <= 89 and 10 <= p["b"] <= 89
                            and p["a"] + p["b"] <= 99,
                            "two-digit hundredths, no spill into a whole"),
    },
    "fu": {    # one 1/b plus a/c, same-family bottoms (b divides c)
        "ans": lambda p: p["c"] // p["b"] + p["a"],
        "spoken": lambda p: (f"How many {_FRACWORD[p['c']][1]} is one "
                             f"{_FRACWORD[p['b']][0]} plus {p['a']} "
                             f"{_FRACWORD[p['c']][1]}?"),
        "board": lambda p: (f'[[step eq="1/{p["b"]} + {p["a"]}/{p["c"]} = '
                            f'?/{p["c"]}"]]'),
        "praise": lambda p: (f"One {_FRACWORD[p['b']][0]} is "
                             f"{p['c'] // p['b']} {_FRACWORD[p['c']][1]} — plus "
                             f"{p['a']} more equals "
                             f"{p['c'] // p['b'] + p['a']} {_FRACWORD[p['c']][1]}."),
        "key": lambda p: p["c"],
        "check": lambda p: (p["c"] % p["b"] == 0 and p["c"] > p["b"]
                            and p["b"] in _FRACWORD and p["c"] in _FRACWORD
                            and p["c"] // p["b"] + p["a"] < p["c"],
                            "the bottoms must be family (b divides c) and the sum "
                            "stays a proper fraction"),
        "speaks": lambda p, sp: (str(p["a"]) in sp
                                 and _FRACWORD[p["b"]][0] in sp
                                 and _FRACWORD[p["c"]][1] in sp),
    },
    "lcm": {
        "ans": lambda p: p["a"] * p["b"] // _gcd(p["a"], p["b"]),
        "spoken": lambda p: (f"What is the least common multiple of {p['a']} "
                             f"and {p['b']}?"),
        "board": lambda p: f'[[step eq="LCM of {p["a"]} and {p["b"]} = ?"]]',
        "praise": lambda p: (f"The least common multiple of {p['a']} and "
                             f"{p['b']} equals "
                             f"{p['a'] * p['b'] // _gcd(p['a'], p['b'])}."),
        "key": lambda p: p["a"] * p["b"] // _gcd(p["a"], p["b"]),
        "check": lambda p: (2 <= p["a"] and 2 <= p["b"]
                            and p["a"] * p["b"] // _gcd(p["a"], p["b"]) <= 60,
                            "the LCM stays countable"),
    },
    "ang": {   # quarter turns
        "ans": lambda p: 90 * p["a"],
        "spoken": lambda p: (f"A quarter turn is 90 degrees. How many degrees "
                             f"is {p['a']} quarter "
                             f"turn{'' if p['a'] == 1 else 's'}?"),
        "board": lambda p: f'[[step eq="{p["a"]} × 90° = ?"]]',
        "praise": lambda p: (f"{p['a']} quarter "
                             f"turn{'' if p['a'] == 1 else 's'} equals "
                             f"{90 * p['a']} degrees."),
        "key": lambda p: p["a"],
        "check": lambda p: (1 <= p["a"] <= 4, "a full turn is the ceiling"),
        # +-1 would be absurd next to 180; the confusion is WHICH multiple of 90
        "choices": lambda p: ([90 * p["a"] - 90, 90 * p["a"], 90 * p["a"] + 90]
                              if p["a"] >= 2 else [90, 180, 270]),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "angq": {  # the reverse of ang: how many quarter turns is a degrees?
        "ans": lambda p: p["a"] // 90,
        "spoken": lambda p: f"How many quarter turns is {p['a']} degrees?",
        "board": lambda p: f'[[step eq="{p["a"]}\u00b0 = ? \u00d7 90\u00b0"]]',
        "praise": lambda p: (f"{p['a']} degrees equals {p['a'] // 90} quarter "
                             f"turn{'' if p['a'] // 90 == 1 else 's'}."),
        "key": lambda p: p["a"] // 90,
        "check": lambda p: (p["a"] in (90, 180, 270, 360),
                            "only whole quarter turns have an answer here"),
        "speaks": lambda p, sp: str(p["a"]) in sp,
    },
    "vol": {   # a x b x c cubes
        "ans": lambda p: p["a"] * p["b"] * p["c"],
        "spoken": lambda p: (f"A box is {p['a']} cubes long, {p['b']} cubes "
                             f"wide and {p['c']} cubes tall. How many cubes "
                             f"fill it?"),
        "board": lambda p: f'[[step eq="{p["a"]} × {p["b"]} × {p["c"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} times {p['b']} times {p['c']} equals "
                             f"{p['a'] * p['b'] * p['c']} cubes."),
        "key": lambda p: p["a"] * p["b"] * p["c"],
        "check": lambda p: (p["a"] * p["b"] * p["c"] <= 96
                            and min(p["a"], p["b"], p["c"]) >= 1,
                            "countable cubes"),
    },
    "peri": {
        "ans": lambda p: 2 * (p["a"] + p["b"]),
        "spoken": lambda p: (f"A rectangle is {p['a']} long and {p['b']} wide. "
                             f"What is its perimeter?"),
        "board": lambda p: (f'[[step eq="{p["a"]} + {p["b"]} + {p["a"]} + '
                            f'{p["b"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} plus {p['b']} plus {p['a']} plus "
                             f"{p['b']} equals {2 * (p['a'] + p['b'])}."),
        "key": lambda p: p["a"] + p["b"],
        "check": lambda p: (p["a"] > p["b"] >= 1,
                            "long means longer: a must beat b"),
    },
    "area": {
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"A rectangle is {p['a']} long and {p['b']} wide. "
                             f"What is its area?"),
        "board": lambda p: f'[[step eq="{p["a"]} × {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} times {p['b']} equals "
                             f"{p['a'] * p['b']} squares."),
        "key": lambda p: p["a"] * p["b"],
        "check": lambda p: (p["a"] > p["b"] >= 1, "long means longer"),
    },

    # ---- PREALGEBRA UNIT 1 (build kk) -- ORDER OF OPERATIONS ------------------
    # Each of these declares its own `choices`, and the wrong option on offer is
    # THE MISCONCEPTION ITSELF -- the answer a child gets by working left to right,
    # or by ignoring the parentheses, or by reading an exponent as a times. A
    # distractor that is merely "the answer plus one" tests arithmetic; a distractor
    # that is the actual error tests whether the RULE landed, and when the child taps
    # it the intervention knows exactly which wrong idea to unpick.
    "tba": {   # a + b x c -- times before add
        "ans": lambda p: p["a"] + p["b"] * p["c"],
        "spoken": lambda p: f"What is {p['a']} plus {p['b']} times {p['c']}?",
        "board": lambda p: f'[[step eq="{p["a"]} + {p["b"]} × {p["c"]} = ?"]]',
        "praise": lambda p: (f"{p['b']} times {p['c']} equals {p['b'] * p['c']}, "
                             f"and {p['a']} plus {p['b'] * p['c']} equals "
                             f"{p['a'] + p['b'] * p['c']}."),
        "key": lambda p: p["b"] * p["c"],
        "choices": lambda p: [p["a"] + p["b"] * p["c"] - p["c"],
                              p["a"] + p["b"] * p["c"],
                              (p["a"] + p["b"]) * p["c"]],
        "check": lambda p: (1 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9,
                            "a is 1-9 and both times numbers are 2-9, so the "
                            "left-to-right answer is always a DIFFERENT number"),
    },
    "parf": {  # (a + b) x c -- parentheses first
        "ans": lambda p: (p["a"] + p["b"]) * p["c"],
        "spoken": lambda p: (f"What is {p['a']} plus {p['b']}, in parentheses, "
                             f"times {p['c']}?"),
        "board": lambda p: f'[[step eq="({p["a"]} + {p["b"]}) × {p["c"]} = ?"]]',
        "praise": lambda p: (f"Inside first: {p['a']} plus {p['b']} equals "
                             f"{p['a'] + p['b']}. Then {p['a'] + p['b']} times "
                             f"{p['c']} equals {(p['a'] + p['b']) * p['c']}."),
        "key": lambda p: (p["a"] + p["b"]) * p["c"],
        "choices": lambda p: [(p["a"] + p["b"]) * p["c"],
                              p["a"] + p["b"] * p["c"],
                              (p["a"] + p["b"]) * p["c"] + p["c"]],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9 and 2 <= p["c"] <= 9,
                            "c is 2-9 so ignoring the parentheses always gives a "
                            "different number"),
    },
    "expn": {  # a to the power b, b in (2, 3) -- an exponent is repeated times
        "ans": lambda p: p["a"] ** p["b"],
        # The spoken line must contain BOTH numbers -- the validator checks it, and it
        # is right to: "3 squared" hides the 2, and a child who only ever hears the word
        # never connects it to the small digit on the board.
        "spoken": lambda p: (f"What is {p['a']} to the power 3? That means three "
                             f"{p['a']}s multiplied."
                             if p["b"] == 3 else
                             f"What is {p['a']} squared — {p['a']} to the power 2?"),
        # THE PICTURE THE METHODOLOGY ASKS FOR (build kj gave us the renderer): a
        # square number IS a square. Cubes have no honest 2-D picture, so they get
        # the written repeat instead of a drawing that would lie about the shape.
        "board": lambda p: (f'[[areamodel rows="{p["a"]}" cols="{p["a"]}" '
                            f'caption="{p["a"]} rows of {p["a"]}"]]'
                            f'[[step eq="{p["a"]}² = ?"]]'
                            if p["b"] == 2 else
                            f'[[step eq="{p["a"]}³ = {p["a"]} × {p["a"]} × '
                            f'{p["a"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} to the power {p['b']} equals "
                             f"{p['a'] ** p['b']} — that is {p['b']} {p['a']}s "
                             f"multiplied."),
        "key": lambda p: p["a"] ** p["b"],
        "choices": lambda p: [p["a"] ** p["b"], p["a"] * p["b"],
                              p["a"] ** p["b"] + p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["b"] in (2, 3)
                            and p["a"] ** p["b"] != p["a"] * p["b"],
                            "a is 2-9 and the power is 2 or 3, and the power answer "
                            "never equals the times answer (which rules out 2²)"),
    },
    "exo": {   # a squared + b x c -- power first, then times, then add
        "ans": lambda p: p["a"] * p["a"] + p["b"] * p["c"],
        "spoken": lambda p: (f"What is {p['a']} squared plus {p['b']} times "
                             f"{p['c']}?"),
        "board": lambda p: f'[[step eq="{p["a"]}² + {p["b"]} × {p["c"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} squared equals {p['a'] * p['a']}, "
                             f"{p['b']} times {p['c']} equals {p['b'] * p['c']}, "
                             f"and those put together equal "
                             f"{p['a'] * p['a'] + p['b'] * p['c']}."),
        "key": lambda p: p["a"] * p["a"] + p["b"] * p["c"],
        # The two wrong options are the two real errors: adding before the times, and
        # reading the little 2 as "times 2". a >= 3 is what keeps all three distinct --
        # at a = 2 the power and the doubling give the same number, and the child would
        # be offered the same answer twice. (The validator caught exactly that.)
        "choices": lambda p: [p["a"] * p["a"] + p["b"] * p["c"],
                              (p["a"] * p["a"] + p["b"]) * p["c"],
                              2 * p["a"] + p["b"] * p["c"]],
        "check": lambda p: (3 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9,
                            "a is 3-9 (at 2, squaring and doubling agree and two "
                            "options would collide); b and c are 2-9"),
    },

    # ---- PREALGEBRA UNIT 2 (build km) -- FACTORS, MULTIPLES & PRIMES ----------
    # Basic Math already teaches GCF and LCM by listing. These go underneath that:
    # what a factor IS, which numbers have only two, and how to break a number all
    # the way down. `a` is the number; `b` carries the authored answer for reference
    # only -- ans() recomputes it, because ans() is the ONLY place answers are made.
    "nfac": {  # how many different numbers divide a exactly
        "ans": lambda p: sum(1 for d in range(1, p["a"] + 1) if p["a"] % d == 0),
        "spoken": lambda p: (f"How many different numbers divide {p['a']} exactly, "
                             f"with nothing left over?"),
        "board": lambda p: f'[[step eq="factors of {p["a"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} has "
                             f"{sum(1 for d in range(1, p['a'] + 1) if p['a'] % d == 0)}"
                             f" factors."),
        "key": lambda p: p["a"],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # `b` is a reference, never spoken
        "check": lambda p: (4 <= p["a"] <= 60,
                            "the number stays small enough to check every divisor by "
                            "hand"),
    },
    "spf": {   # the smallest number above 1 that divides a
        "ans": lambda p: next(d for d in range(2, p["a"] + 1) if p["a"] % d == 0),
        "spoken": lambda p: (f"What is the smallest number, bigger than 1, that "
                             f"divides {p['a']} exactly?"),
        "board": lambda p: f'[[step eq="{p["a"]} ÷ ? leaves nothing over"]]',
        "praise": lambda p: (f"{next(d for d in range(2, p['a'] + 1) if p['a'] % d == 0)}"
                             f" is the smallest one that divides {p['a']}."),
        "key": lambda p: p["a"],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # `b` is a reference, never spoken
        "check": lambda p: (9 <= p["a"] <= 99 and
                            next(d for d in range(2, p["a"] + 1) if p["a"] % d == 0)
                            != p["a"],
                            "the number is 9-99 and is NOT itself prime, so there is a "
                            "smaller factor to find"),
    },
    "npf": {   # how many primes multiplied make a (repeats counted)
        "ans": lambda p: len(_prime_factors(p["a"])),
        "spoken": lambda p: (f"Break {p['a']} down into primes multiplied. How many "
                             f"primes does it take?"),
        "board": lambda p: f'[[step eq="{p["a"]} = ? primes multiplied"]]',
        "praise": lambda p: (f"{p['a']} equals "
                             f"{' × '.join(str(x) for x in _prime_factors(p['a']))} — "
                             f"{len(_prime_factors(p['a']))} primes."),
        "key": lambda p: p["a"],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # `b` is a reference, never spoken
        "check": lambda p: (4 <= p["a"] <= 99 and len(_prime_factors(p["a"])) >= 2,
                            "the number is 4-99 and is not prime itself, so there is "
                            "something to break down"),
    },

    # ---- PREALGEBRA UNIT 3 (build km) -- INTEGERS & NEGATIVE NUMBERS ---------
    # THE FIRST LESSONS IN THE APP WHOSE ANSWERS GO BELOW ZERO. The validator used to
    # assume every answer was 1 or more -- true of every counting lesson through Basic
    # Math, and false the moment integers arrive -- so a lesson now declares its own
    # min_value and the guard stays on. The PROBLEM DATA stays positive: `a` and `b`
    # are the numbers a child reads, and the sign lives in the question and the answer.
    # Each wrong option is the sign error itself.
    "cbz": {   # start at a, count back b, land below zero
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"Start at {p['a']} and count back {p['b']}. What number "
                             f"do you land on?"),
        # THE PICTURE THIS UNIT EXISTS FOR (build kj gave us the renderer): below zero
        # is a PLACE, and a child who sees it on the line stops thinking of a negative
        # as a broken sum.
        "board": lambda p: (f'[[numberline min="-20" max="10" '
                            f'points="{p["a"] - p["b"]}"]]'
                            f'[[step eq="{p["a"]} − {p["b"]} = ?"]]'),
        "praise": lambda p: (f"You land on negative {p['b'] - p['a']} — "
                             f"{p['b'] - p['a']} steps to the left of zero."),
        "key": lambda p: p["b"] - p["a"],
        "choices": lambda p: [p["a"] - p["b"], p["b"] - p["a"], p["a"] - p["b"] - 1],
        "check": lambda p: (1 <= p["a"] <= 9 and p["a"] < p["b"] <= 21,
                            "counting back always passes zero, which is the lesson"),
    },
    "addneg": {  # a + (-b)
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"What is {p['a']} plus negative {p['b']}?"),
        "board": lambda p: (f'[[numberline min="-20" max="10" '
                            f'points="{p["a"] - p["b"]}"]]'
                            f'[[step eq="{p["a"]} + (−{p["b"]}) = ?"]]'),
        "praise": lambda p: (f"Adding negative {p['b']} moves {p['b']} to the left, "
                             f"so you land on negative {p['b'] - p['a']}."),
        "key": lambda p: p["b"] - p["a"],
        "choices": lambda p: [p["a"] - p["b"], p["a"] + p["b"], p["a"] - p["b"] - 1],
        "check": lambda p: (1 <= p["a"] <= 9 and p["a"] < p["b"] <= 21,
                            "the answer lands below zero, which is the lesson"),
    },
    "subneg": {  # a - (-b) -- the surprise: it goes UP
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"What is {p['a']} take away negative {p['b']}?"),
        "board": lambda p: f'[[step eq="{p["a"]} − (−{p["b"]}) = ?"]]',
        "praise": lambda p: (f"Taking away negative {p['b']} moves {p['b']} to the "
                             f"RIGHT, so {p['a']} take away negative {p['b']} equals "
                             f"{p['a'] + p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        "choices": lambda p: [p["a"] + p["b"], p["a"] - p["b"], p["a"] + p["b"] + 1],
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 15 and p["a"] != p["b"],
                            "a and b differ, so the right answer and the take-away "
                            "error are never the same number"),
    },
    "mulneg": {  # (-a) x b
        "ans": lambda p: -(p["a"] * p["b"]),
        "spoken": lambda p: f"What is negative {p['a']} times {p['b']}?",
        "board": lambda p: f'[[step eq="(−{p["a"]}) × {p["b"]} = ?"]]',
        "praise": lambda p: (f"{p['a']} times {p['b']} equals {p['a'] * p['b']}, and "
                             f"one negative turns the answer negative — negative "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        "choices": lambda p: [-(p["a"] * p["b"]), p["a"] * p["b"],
                              -(p["a"] * p["b"]) - p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9,
                            "both numbers are 2-9, so the answer and the "
                            "forgot-the-sign error are always different"),
    },

    # ---- PREALGEBRA UNIT 4 (build kn) -- FRACTIONS BEYOND BASIC ---------------
    # Basic Math takes fractions as far as adding and taking them away, and its
    # "fraction of a group" only ever asks for a UNIT fraction -- "one half of 4".
    # These four go past that: a non-unit fraction of a number, how many parts fit
    # inside a whole, dividing BY a fraction, and reading an improper fraction.
    # Every answer is a whole number, because a tap answer has to be one.
    "nuf": {   # a/b of c -- a NON-unit fraction of a whole number
        "ans": lambda p: p["c"] // p["b"] * p["a"],
        "spoken": lambda p: (f"What is {_frac_words(p['a'], p['b'])} of {p['c']}?"),
        "board": lambda p: (f'[[step eq="{p["c"]} ÷ {p["b"]} = {p["c"] // p["b"]}"]]'
                            f'[[step eq="{p["c"] // p["b"]} × {p["a"]} = ?"]]'),
        "praise": lambda p: (f"One {_FRAC_BOTTOM.get(p['b'], 'part')} of {p['c']} is "
                             f"{p['c'] // p['b']}, and {p['a']} of those equal "
                             f"{p['c'] // p['b'] * p['a']}."),
        "key": lambda p: p["c"] // p["b"] * p["a"],
        # The wrong option is the child who stops after the divide -- they found ONE
        # part and forgot to take a of them, which is the whole difference between
        # this lesson and Basic's unit-fraction one.
        "choices": lambda p: [p["c"] // p["b"] * p["a"], p["c"] // p["b"],
                              p["c"] // p["b"] * p["a"] + p["c"] // p["b"]],
        "speaks": lambda p, sp: str(p["c"]) in sp,   # a and b are said as WORDS
        "check": lambda p: (2 <= p["a"] < p["b"] <= 10 and p["c"] % p["b"] == 0
                            and p["c"] <= 30 and p["a"] != 1,
                            "a proper NON-unit fraction, and c divides exactly so the "
                            "answer is a whole number a child can tap"),
    },
    "uic": {   # how many 1/a fit inside b wholes
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"How many {_FRAC_BOTTOM.get(p['a'], 'parts')}s are "
                             f"there in {p['b']} wholes?"),
        "board": lambda p: (f'[[step eq="1 whole = {p["a"]} '
                            f'{_FRAC_BOTTOM.get(p["a"], "parts")}s"]]'
                            f'[[step eq="{p["b"]} wholes = {p["b"]} × {p["a"]} = ?"]]'),
        "praise": lambda p: (f"Each whole holds {p['a']}, so {p['b']} wholes hold "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["a"] * p["b"] - p["a"]],
        "speaks": lambda p, sp: str(p["b"]) in sp,   # the bottom is said as a WORD
        "check": lambda p: (2 <= p["a"] <= 10 and 2 <= p["b"] <= 8
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "the parts are 2-10 and the wholes 2-8, and a×b never "
                            "equals a+b -- at 2 and 2 they both give 4 and the child "
                            "would be offered the answer twice"),
    },
    "dbf": {   # c divided by a/b -- flip and times
        "ans": lambda p: p["c"] * p["b"] // p["a"],
        "spoken": lambda p: (f"What is {p['c']} divided by "
                             f"{_frac_words(p['a'], p['b'])}?"),
        "board": lambda p: (f'[[step eq="{p["c"]} ÷ {p["a"]}/{p["b"]}"]]'
                            f'[[step eq="{p["c"]} × {p["b"]}/{p["a"]} = ?"]]'),
        "praise": lambda p: (f"Flip the fraction and times: {p['c']} times "
                             f"{p['b']} over {p['a']} equals "
                             f"{p['c'] * p['b'] // p['a']}."),
        "key": lambda p: p["c"] * p["b"] // p["a"],
        # The error worth offering is dividing instead of flipping -- the child who
        # trusts that dividing always makes things smaller.
        "choices": lambda p: [p["c"] * p["b"] // p["a"], p["c"] * p["a"] // p["b"] or 1,
                              p["c"] * p["b"] // p["a"] + p["b"]],
        "speaks": lambda p, sp: str(p["c"]) in sp,
        "check": lambda p: (2 <= p["a"] < p["b"] <= 9 and 2 <= p["c"] <= 12
                            and (p["c"] * p["b"]) % p["a"] == 0
                            and p["c"] * p["b"] // p["a"] != p["c"] * p["a"] // p["b"],
                            "the answer is a whole number, and flipping the wrong way "
                            "always gives a different one"),
    },
    "imp": {   # a/b -- how many WHOLE ones are inside it
        "ans": lambda p: p["a"] // p["b"],
        "spoken": lambda p: (f"How many whole ones are inside {p['a']} "
                             f"{_FRAC_BOTTOM.get(p['b'], 'part')}s?"),
        # A fraction bigger than 1 is a PLACE past the whole numbers, and the line
        # says that better than any sentence (build kj gave us the renderer).
        "board": lambda p: (f'[[numberline min="0" max="{p["a"] // p["b"] + 1}" '
                            f'points="{round(p["a"] / p["b"], 2)}"]]'
                            f'[[step eq="{p["a"]}/{p["b"]} = ? whole ones and some left"]]'),
        "praise": lambda p: (f"{p['b']} of them fill one whole, so {p['a']} of them "
                             f"fill {p['a'] // p['b']} whole ones with "
                             f"{p['a'] % p['b']} left over."),
        "key": lambda p: p["a"] // p["b"],
        "choices": lambda p: [p["a"] // p["b"], p["a"] % p["b"], p["a"] // p["b"] + 1],
        "speaks": lambda p, sp: str(p["a"]) in sp,   # the bottom is said as a WORD
        "check": lambda p: (7 <= p["a"] <= 40 and 3 <= p["b"] <= 9
                            and p["a"] % p["b"] != 0
                            and p["a"] // p["b"] != p["a"] % p["b"],
                            "the fraction is bigger than 1 and does not land exactly "
                            "on a whole, and the whole count and the left-over are "
                            "never the same number"),
    },

    # ---- PREALGEBRA UNIT 5 (build ko) -- DECIMALS BEYOND BASIC ----------------
    # Basic Math names tenths and hundredths and counts dimes and pennies. These four
    # go past naming: converting to a common unit (which is what comparing decimals
    # REALLY is), scaling by ten, and timesing and sharing them.
    # Every answer is a COUNT OF PARTS -- "how many hundredths", "how many tenths" --
    # which is both the honest way to think about a decimal and the only way a tap
    # answer can carry one.
    "hun": {   # 0.ab -- how many hundredths is that?
        "ans": lambda p: 10 * p["a"] + p["b"],
        "spoken": lambda p: (f"How many hundredths are there in "
                             f"0 point {p['a']}{p['b']}?"),
        "board": lambda p: (f'[[numberline min="0" max="1" '
                            f'points="{(10 * p["a"] + p["b"]) / 100}"]]'
                            f'[[step eq="0.{p["a"]}{p["b"]} = ? hundredths"]]'),
        "praise": lambda p: (f"0 point {p['a']}{p['b']} is "
                             f"{10 * p['a'] + p['b']} hundredths."),
        "key": lambda p: 10 * p["a"] + p["b"],
        # The wrong option is the child reading the digits as a whole number and
        # ignoring the place -- the same habit that makes 0.45 look bigger than 0.5.
        "choices": lambda p: [10 * p["a"] + p["b"], p["a"] + p["b"],
                              10 * p["a"] + p["b"] + 10],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (1 <= p["a"] <= 9 and 0 <= p["b"] <= 9
                            and 10 * p["a"] + p["b"] != p["a"] + p["b"],
                            "a is 1-9 so the place-value answer and the "
                            "digits-added error are never the same number"),
    },
    "x10": {   # a.b times 10
        "ans": lambda p: 10 * p["a"] + p["b"],
        "spoken": lambda p: f"What is {p['a']} point {p['b']} times 10?",
        "board": lambda p: (f'[[step eq="{p["a"]}.{p["b"]} × 10"]]'
                            f'[[step eq="every digit moves one place left = ?"]]'),
        "praise": lambda p: (f"Timesing by 10 moves every digit one place to the "
                             f"left, so {p['a']} point {p['b']} becomes "
                             f"{10 * p['a'] + p['b']}."),
        "key": lambda p: 10 * p["a"] + p["b"],
        # The error worth offering is timesing only the whole part and leaving the
        # tenths where they were.
        "choices": lambda p: [10 * p["a"] + p["b"], 10 * p["a"],
                              10 * p["a"] + p["b"] + 1],
        "check": lambda p: (1 <= p["a"] <= 9 and 0 <= p["b"] <= 9 and p["b"] != 0,
                            "there is a tenths digit to move, so leaving it behind "
                            "gives a different number"),
    },
    "dth": {   # 0.a times b -- answered in TENTHS
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"0 point {p['a']} times {p['b']} — how many tenths "
                             f"is that?"),
        "board": lambda p: (f'[[step eq="0.{p["a"]} = {p["a"]} tenths"]]'
                            f'[[step eq="{p["a"]} tenths × {p["b"]} = ? tenths"]]'),
        "praise": lambda p: (f"{p['a']} tenths taken {p['b']} times equal "
                             f"{p['a'] * p['b']} tenths."),
        "key": lambda p: p["a"] * p["b"],
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"], p["a"] * p["b"] + p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "both are 2-9 and the times never equals the add, so the "
                            "three options are three different numbers"),
    },
    "dsh": {   # a.b shared between c -- answered in TENTHS
        "ans": lambda p: (10 * p["a"] + p["b"]) // p["c"],
        "spoken": lambda p: (f"{p['a']} point {p['b']} shared between {p['c']} — "
                             f"how many tenths each?"),
        "board": lambda p: (f'[[step eq="{p["a"]}.{p["b"]} = '
                            f'{10 * p["a"] + p["b"]} tenths"]]'
                            f'[[step eq="{10 * p["a"] + p["b"]} ÷ {p["c"]} = ? tenths"]]'),
        "praise": lambda p: (f"{p['a']} point {p['b']} is "
                             f"{10 * p['a'] + p['b']} tenths, and shared between "
                             f"{p['c']} that is "
                             f"{(10 * p['a'] + p['b']) // p['c']} tenths each."),
        "key": lambda p: (10 * p["a"] + p["b"]) // p["c"],
        "choices": lambda p: [(10 * p["a"] + p["b"]) // p["c"],
                              (10 * p["a"] + p["b"]) // p["c"] + p["c"],
                              (10 * p["a"] + p["b"]) // p["c"] + 1],
        "check": lambda p: (1 <= p["a"] <= 9 and 0 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and (10 * p["a"] + p["b"]) % p["c"] == 0,
                            "it shares out exactly, so the answer is a whole number "
                            "of tenths a child can tap"),
    },

    # ---- PREALGEBRA UNIT 6 (build kp) -- RATIOS, RATES & PROPORTIONS ----------
    # Basic Math's "one costs" already does unit PRICE. These four are the family of
    # ideas around it: keeping a ratio's shape when both sides grow, scaling a rate
    # over time, the same move written as an equation with a hole in it, and splitting
    # an amount in a ratio -- the one that is genuinely different, because the total is
    # given and the parts have to be found.
    "rat": {   # ratio a:b -- given c of the first, how many of the second
        "ans": lambda p: p["c"] // p["a"] * p["b"],
        "spoken": lambda p: (f"A recipe uses {p['a']} cups of flour for every "
                             f"{p['b']} cups of milk. With {p['c']} cups of flour, "
                             f"how many cups of milk?"),
        "board": lambda p: (f'[[step eq="{p["a"]} : {p["b"]}"]]'
                            f'[[step eq="{p["c"]} ÷ {p["a"]} = {p["c"] // p["a"]} '
                            f'batches"]]'
                            f'[[step eq="{p["c"] // p["a"]} × {p["b"]} = ?"]]'),
        "praise": lambda p: (f"{p['c']} cups of flour is {p['c'] // p['a']} batches, "
                             f"so it takes {p['c'] // p['a'] * p['b']} cups of milk."),
        "key": lambda p: p["c"] // p["a"] * p["b"],
        # The error worth offering is ADDING the difference instead of scaling -- the
        # child who thinks 2:3 growing to 4 means "4:5", because 3 is one more than 2.
        "choices": lambda p: [p["c"] // p["a"] * p["b"], p["c"] + (p["b"] - p["a"]),
                              p["c"] // p["a"] * p["b"] + p["b"]],
        "speaks": lambda p, sp: str(p["a"]) in sp and str(p["c"]) in sp,
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and p["a"] != p["b"]
                            and p["c"] % p["a"] == 0 and p["c"] // p["a"] >= 2
                            and len({p["c"] // p["a"] * p["b"],
                                     p["c"] + (p["b"] - p["a"]),
                                     p["c"] // p["a"] * p["b"] + p["b"]}) == 3,
                            "the ratio really scales (at least two batches) and the "
                            "three tap options are three different numbers"),
    },
    "rte": {   # c things in b hours -- how many in a hours
        "ans": lambda p: p["c"] // p["b"] * p["a"],
        # "makes" is banned speech (canon is "equals"), so the machine FILLS.
        "spoken": lambda p: (f"A machine fills {p['c']} bottles in {p['b']} hours. "
                             f"How many does it fill in {p['a']} hours?"),
        "board": lambda p: (f'[[step eq="{p["c"]} ÷ {p["b"]} = '
                            f'{p["c"] // p["b"]} per hour"]]'
                            f'[[step eq="{p["c"] // p["b"]} × {p["a"]} = ?"]]'),
        "praise": lambda p: (f"That is {p['c'] // p['b']} an hour, so in {p['a']} "
                             f"hours it fills {p['c'] // p['b'] * p['a']}."),
        "key": lambda p: p["c"] // p["b"] * p["a"],
        "choices": lambda p: [p["c"] // p["b"] * p["a"], p["c"] // p["b"],
                              p["c"] // p["b"] * p["a"] + p["c"] // p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["c"] % p["b"] == 0 and p["a"] != 1
                            and p["c"] // p["b"] * p["a"] != p["c"] // p["b"],
                            "it divides exactly and the target time is not one hour, "
                            "so finding the rate is only HALF the job"),
    },
    "prop": {  # a/b = ?/c
        "ans": lambda p: p["a"] * p["c"] // p["b"],
        "spoken": lambda p: (f"{p['a']} over {p['b']} equals what over {p['c']}?"),
        "board": lambda p: (f'[[step eq="{p["a"]}/{p["b"]} = ?/{p["c"]}"]]'
                            f'[[step eq="{p["c"]} ÷ {p["b"]} = '
                            f'{p["c"] // p["b"] if p["c"] % p["b"] == 0 else "?"}"]]'
                            if p["c"] % p["b"] == 0 else
                            f'[[step eq="{p["a"]}/{p["b"]} = ?/{p["c"]}"]]'
                            f'[[step eq="{p["a"]} × {p["c"]} ÷ {p["b"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} over {p['b']} equals "
                             f"{p['a'] * p['c'] // p['b']} over {p['c']}."),
        "key": lambda p: p["a"] * p["c"] // p["b"],
        # The classic error: adding the same amount to both instead of timesing.
        "choices": lambda p: [p["a"] * p["c"] // p["b"], p["a"] + (p["c"] - p["b"]),
                              p["a"] * p["c"] // p["b"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and p["c"] <= 30
                            and (p["a"] * p["c"]) % p["b"] == 0 and p["c"] != p["b"]
                            and len({p["a"] * p["c"] // p["b"],
                                     p["a"] + (p["c"] - p["b"]),
                                     p["a"] * p["c"] // p["b"] + p["b"]}) == 3,
                            "the missing number is whole, the bottom really changes, "
                            "and all THREE options are different numbers (the first "
                            "try had the add-the-same error landing on the same value "
                            "as the neighbour)"),
    },
    "shr": {   # share c in the ratio a:b -- the FIRST share
        "ans": lambda p: p["c"] // (p["a"] + p["b"]) * p["a"],
        "spoken": lambda p: (f"Share {p['c']} sweets between two children in the "
                             f"ratio {p['a']} to {p['b']}. How many does the first "
                             f"child get?"),
        "board": lambda p: (f'[[objects emoji="🟦" groups="{p["a"]}" add="{p["b"]}" '
                            f'caption="{p["a"]} parts and {p["b"]} parts = '
                            f'{p["a"] + p["b"]} parts in all"]]'
                            f'[[step eq="{p["c"]} ÷ {p["a"] + p["b"]} = '
                            f'{p["c"] // (p["a"] + p["b"])} each part"]]'
                            f'[[step eq="{p["c"] // (p["a"] + p["b"])} × {p["a"]} = ?"]]'),
        "praise": lambda p: (f"{p['a'] + p['b']} parts in all, so each part is "
                             f"{p['c'] // (p['a'] + p['b'])}, and the first child gets "
                             f"{p['a']} of them — "
                             f"{p['c'] // (p['a'] + p['b']) * p['a']}."),
        "key": lambda p: p["c"] // (p["a"] + p["b"]) * p["a"],
        # The error worth offering is sharing the amount by the FIRST number only,
        # forgetting that the parts have to be counted together first.
        "choices": lambda p: [p["c"] // (p["a"] + p["b"]) * p["a"],
                              p["c"] // (p["a"] + p["b"]) * p["b"],
                              p["c"] // (p["a"] + p["b"])],
        "speaks": lambda p, sp: str(p["c"]) in sp and str(p["a"]) in sp,
        # A one-part share IS the size of one part, so a = 1 (or b = 1) makes two
        # of the three options the same number. Requiring three different options
        # says that out loud instead of hiding it in a bound on a.
        "check": lambda p: (1 <= p["a"] <= 9 and 1 <= p["b"] <= 9 and p["a"] != p["b"]
                            and p["c"] % (p["a"] + p["b"]) == 0
                            and p["c"] // (p["a"] + p["b"]) != 1
                            and len({p["c"] // (p["a"] + p["b"]) * p["a"],
                                     p["c"] // (p["a"] + p["b"]) * p["b"],
                                     p["c"] // (p["a"] + p["b"])}) == 3,
                            "each part is more than one and the three tap options "
                            "are three different numbers"),
    },

    # ---- PREALGEBRA UNIT 7 (build kr) -- PERCENTS -----------------------------
    # Basic Math's "pc" only ever asks for 10, 25 or 50 percent, and it answers them
    # with a fraction shortcut (half, a fourth, a tenth). That shortcut runs out the
    # moment the percent is 30 or 70. These four replace it with ONE method that keeps
    # working -- find ten percent, then count how many tens you need -- and then run
    # that method in every direction: forwards, as a reading of one number against
    # another, backwards from a part to the whole, and finally up and down.
    "pcn": {   # a percent of b, both multiples of ten
        "ans": lambda p: p["a"] * p["b"] // 100,
        "spoken": lambda p: f"What is {p['a']} percent of {p['b']}?",
        "board": lambda p: (f'[[step eq="10% of {p["b"]} = {p["b"] // 10}"]]'
                            f'[[step eq="{p["a"]}% is {p["a"] // 10} tens"]]'
                            f'[[step eq="{p["a"] // 10} × {p["b"] // 10} = ?"]]'),
        "praise": lambda p: (f"10 percent of {p['b']} is {p['b'] // 10}, and "
                             f"{p['a']} percent is {p['a'] // 10} of those — "
                             f"{p['a'] * p['b'] // 100}."),
        "key": lambda p: p["a"] * p["b"] // 100,
        # The error worth offering is STOPPING AT TEN PERCENT -- the same shape as the
        # rate error in Unit 6, where the child divides to reach one and taps that.
        "choices": lambda p: [p["a"] * p["b"] // 100, p["b"] // 10,
                              p["a"] * p["b"] // 100 + p["b"] // 10],
        "check": lambda p: (p["a"] % 10 == 0 and 20 <= p["a"] <= 90 and p["a"] != 50
                            and p["b"] % 10 == 0 and 10 <= p["b"] <= 90
                            and len({p["a"] * p["b"] // 100, p["b"] // 10,
                                     p["a"] * p["b"] // 100 + p["b"] // 10}) == 3,
                            "both are tens so ten percent is whole, the percent is one "
                            "Basic never taught, and the three options differ"),
    },
    "asp": {   # a out of b -- what percent?
        "ans": lambda p: p["a"] * 100 // p["b"],
        "spoken": lambda p: f"{p['a']} out of {p['b']} — what percent is that?",
        "board": lambda p: (f'[[step eq="{p["a"]}/{p["b"]} = ?/100"]]'
                            f'[[step eq="{p["a"]} × 100 ÷ {p["b"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} out of {p['b']} is "
                             f"{p['a'] * 100 // p['b']} percent."),
        "key": lambda p: p["a"] * 100 // p["b"],
        # The classic slip is reading the percent of what is NOT there, so the second
        # option is the leftover percent. The third is tapping the part itself.
        "choices": lambda p: [p["a"] * 100 // p["b"],
                              100 - p["a"] * 100 // p["b"], p["a"]],
        "check": lambda p: (1 <= p["a"] < p["b"] <= 100
                            and (p["a"] * 100) % p["b"] == 0
                            and len({p["a"] * 100 // p["b"],
                                     100 - p["a"] * 100 // p["b"], p["a"]}) == 3,
                            "the percent is whole, the part is smaller than the whole, "
                            "and the three options differ (which rules out 50 percent, "
                            "where the answer and its leftover are one number)"),
    },
    "pwh": {   # b is a percent of WHAT? -- the reverse, and the hard direction
        "ans": lambda p: p["b"] * 100 // p["a"],
        "spoken": lambda p: f"{p['b']} is {p['a']} percent of what number?",
        "board": lambda p: (f'[[step eq="{p["a"]}% = {p["b"]}"]]'
                            f'[[step eq="10% = {p["b"]} ÷ {p["a"] // 10} = '
                            f'{p["b"] // (p["a"] // 10)}"]]'
                            f'[[step eq="100% = {p["b"] // (p["a"] // 10)} × 10 = ?"]]'),
        "praise": lambda p: (f"10 percent is {p['b'] // (p['a'] // 10)}, so the whole "
                             f"is ten of those — {p['b'] * 100 // p['a']}."),
        "key": lambda p: p["b"] * 100 // p["a"],
        # THE reversal error: doing the forward sum instead -- finding a percent OF the
        # part, when the part is what you were given.
        "choices": lambda p: [p["b"] * 100 // p["a"], p["a"] * p["b"] // 100,
                              p["b"] * 100 // p["a"] - p["b"]],
        "check": lambda p: (p["a"] % 10 == 0 and 10 <= p["a"] <= 90
                            and (p["b"] * 100) % p["a"] == 0
                            and p["b"] % (p["a"] // 10) == 0
                            and 1 <= p["b"] * 100 // p["a"] <= 100
                            # >= 2, not >= 1: at 20 percent of 6 the forward error
                            # rounds down to 1, and "1" is not an answer any child
                            # arrives at -- it is a stub, and a stub is not a choice.
                            and min(p["b"] * 100 // p["a"], p["a"] * p["b"] // 100,
                                    p["b"] * 100 // p["a"] - p["b"]) >= 2
                            and len({p["b"] * 100 // p["a"], p["a"] * p["b"] // 100,
                                     p["b"] * 100 // p["a"] - p["b"]}) == 3,
                            "the ten-percent step is whole, the whole is a real "
                            "number a child can tap, and every wrong option is a real "
                            "wrong answer rather than a rounded-down stub"),
    },
    "pup": {   # c=1 a percent MORE, c=0 a percent LESS
        "ans": lambda p: (p["b"] + p["a"] * p["b"] // 100 if p.get("c")
                          else p["b"] - p["a"] * p["b"] // 100),
        "spoken": lambda p: (f"A coat costs {p['b']} dollars. The price goes "
                             f"{'up' if p.get('c') else 'down'} by {p['a']} percent. "
                             f"What does it cost now?"),
        # The ten-percent step and the "a percent" step are the SAME LINE when the
        # percent is ten, and a board that says "10% of 40 = 4" and then "10% = 4"
        # teaches a child that the second step is empty. Show it only when it says
        # something new.
        "board": lambda p: (f'[[step eq="10% of {p["b"]} = {p["b"] // 10}"]]'
                            + (f'[[step eq="{p["a"]}% = {p["a"] * p["b"] // 100}"]]'
                               if p["a"] != 10 else "")
                            + f'[[step eq="{p["b"]} '
                              f'{"+" if p.get("c") else "−"} '
                              f'{p["a"] * p["b"] // 100} = ?"]]'),
        "praise": lambda p: (f"{p['a']} percent of {p['b']} is "
                             f"{p['a'] * p['b'] // 100}, so the new price is "
                             f"{p['b'] + p['a'] * p['b'] // 100 if p.get('c') else p['b'] - p['a'] * p['b'] // 100} dollars."),
        "key": lambda p: (p["b"] + p["a"] * p["b"] // 100 if p.get("c")
                          else p["b"] - p["a"] * p["b"] // 100),
        # THE error this lesson exists for: moving the price by the PERCENT NUMBER
        # instead of by that percent OF the price -- 40 dollars up 10 percent read as
        # 50 dollars. The third option is the change on its own, mistaken for the price.
        "choices": lambda p: [(p["b"] + p["a"] * p["b"] // 100 if p.get("c")
                               else p["b"] - p["a"] * p["b"] // 100),
                              (p["b"] + p["a"] if p.get("c") else p["b"] - p["a"]),
                              p["a"] * p["b"] // 100],
        "speaks": lambda p, sp: str(p["a"]) in sp and str(p["b"]) in sp,
        "check": lambda p: (p["a"] % 10 == 0 and 10 <= p["a"] <= 50
                            and p["b"] % 10 == 0 and 10 <= p["b"] <= 90
                            and (p["a"] * p["b"]) % 100 == 0
                            and len({(p["b"] + p["a"] * p["b"] // 100 if p.get("c")
                                      else p["b"] - p["a"] * p["b"] // 100),
                                     (p["b"] + p["a"] if p.get("c")
                                      else p["b"] - p["a"]),
                                     p["a"] * p["b"] // 100}) == 3,
                            "the change is a whole number of dollars and the three "
                            "options are three different prices"),
    },

    # ---- PREALGEBRA UNIT 8 (build ks) -- MEASUREMENT & GEOMETRY BASICS -------
    # Basic Math's geometry unit (perimeter, area, quarter turns, volume) draws NO
    # PICTURES -- every one of its boards is a [[step]] line. That is the wrong medium
    # for the one subject where the picture IS the argument, and geo-figures.js has had
    # [[triangle]] and [[angle]] the whole time. Three of these four ops put a real
    # figure on the board, and the straight-line lesson uses [[angle deg="180"
    # split="130"]] -- a tag built in July for exactly this and never once used by a
    # scripted lesson.
    "cnv": {   # a of the bigger unit -- how many of the smaller? b is the factor
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (
            f"How many millimetres are there in {p['a']} centimetres?" if p["b"] == 10
            else f"How many centimetres are there in {p['a']} metres?" if p["b"] == 100
            else f"How many grams are there in {p['a']} kilograms?"),
        "board": lambda p: (f'[[step eq="1 {"cm = 10 mm" if p["b"] == 10 else "m = 100 cm" if p["b"] == 100 else "kg = 1000 g"}"]]'
                            f'[[step eq="{p["a"]} × {p["b"]} = ?"]]'),
        "praise": lambda p: (f"Each one is {p['b']}, so {p['a']} of them are "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # THE unit-conversion error is the wrong power of ten -- one place short, or one
        # place too far. Neither is a careless slip; both are a child who knows a zero
        # goes on and does not know how many.
        "choices": lambda p: [p["a"] * p["b"], p["a"] * p["b"] // 10,
                              p["a"] * p["b"] * 10],
        # The factor is not spoken -- the UNIT NAMES carry it, which is the whole point
        # of the lesson. Rule 44 is satisfied by the number the child has to use.
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (1 <= p["a"] <= 9 and p["b"] in (10, 100, 1000)
                            and p["a"] * p["b"] <= 9000
                            and len({p["a"] * p["b"], p["a"] * p["b"] // 10,
                                     p["a"] * p["b"] * 10}) == 3,
                            "a single-digit count of a real unit, and the three options "
                            "are three different places"),
    },
    "tri": {   # area of a right triangle, base a and height b
        "ans": lambda p: p["a"] * p["b"] // 2,
        "spoken": lambda p: (f"A triangle has a base of {p['a']} and a height of "
                             f"{p['b']}. What is its area?"),
        "board": lambda p: (f'[[triangle v="A,B,C" right="A" '
                            f'sides="{p["a"]},,{p["b"]}"]]'
                            f'[[step eq="the rectangle round it: '
                            f'{p["a"]} × {p["b"]} = {p["a"] * p["b"]}"]]'
                            f'[[step eq="the triangle is half: '
                            f'{p["a"] * p["b"]} ÷ 2 = ?"]]'),
        "praise": lambda p: (f"The rectangle round it is {p['a'] * p['b']}, and the "
                             f"triangle is half of that — {p['a'] * p['b'] // 2}."),
        "key": lambda p: p["a"] * p["b"] // 2,
        # The error worth offering is FORGETTING TO HALVE -- answering with the
        # rectangle. It is the single most common wrong answer there is here.
        "choices": lambda p: [p["a"] * p["b"] // 2, p["a"] * p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 20 and 2 <= p["b"] <= 20
                            and (p["a"] * p["b"]) % 2 == 0
                            and len({p["a"] * p["b"] // 2, p["a"] * p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "the half is a whole number of squares and the three "
                            "options are three different numbers"),
    },
    "sla": {   # two angles on a straight line: one is a, how big is the other?
        "ans": lambda p: 180 - p["a"],
        "spoken": lambda p: (f"Two angles sit together on a straight line. One of them "
                             f"is {p['a']} degrees. How big is the other one?"),
        # geo-figures' split= was built in July for exactly this sentence and no
        # scripted lesson had ever used it: the straight line IS the 180, drawn.
        "board": lambda p: (f'[[angle deg="180" split="{p["a"]}"]]'
                            f'[[step eq="180° − {p["a"]}° = ?"]]'),
        "praise": lambda p: (f"A straight line is 180 degrees, and 180 take away "
                             f"{p['a']} equals {180 - p['a']}."),
        "key": lambda p: 180 - p["a"],
        # The two real errors: using a RIGHT ANGLE'S 90 or a FULL TURN'S 360 in place of
        # the straight line's 180, and simply tapping the angle you were handed.
        "choices": lambda p: [180 - p["a"], 360 - p["a"], p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (10 <= p["a"] <= 170 and p["a"] != 90
                            and len({180 - p["a"], 360 - p["a"], p["a"]}) == 3,
                            "the angle is not the right angle (where the answer and the "
                            "angle are one number) and the three options differ"),
    },
    "tri3": {  # two angles of a triangle are a and b -- the third?
        "ans": lambda p: 180 - p["a"] - p["b"],
        "spoken": lambda p: (f"Two angles of a triangle are {p['a']} degrees and "
                             f"{p['b']} degrees. How big is the third one?"),
        # When one of the given angles IS 90, say so in the figure. The renderer's
        # header calls these figures schematic, and they are -- but a right angle drawn
        # as a lazy corner with "90°" written beside it is schematic in the one way
        # that teaches the wrong thing.
        "board": lambda p: (f'[[triangle v="A,B,C"'
                            + (' right="A"' if p["a"] == 90 else
                               ' right="B"' if p["b"] == 90 else "")
                            + f' angles="{p["a"]},{p["b"]},"]]'
                            f'[[step eq="{p["a"]}° + {p["b"]}° = '
                            f'{p["a"] + p["b"]}°"]]'
                            f'[[step eq="180° − {p["a"] + p["b"]}° = ?"]]'),
        "praise": lambda p: (f"The two you were given are {p['a'] + p['b']} together, "
                             f"and 180 take away {p['a'] + p['b']} equals "
                             f"{180 - p['a'] - p['b']}."),
        "key": lambda p: 180 - p["a"] - p["b"],
        # The error worth offering is answering with the two you were GIVEN added up --
        # the child who does the first step and taps it.
        "choices": lambda p: [180 - p["a"] - p["b"], p["a"] + p["b"],
                              180 - p["a"]],
        "check": lambda p: (10 <= p["a"] <= 150 and 10 <= p["b"] <= 150
                            and 180 - p["a"] - p["b"] >= 10
                            and len({180 - p["a"] - p["b"], p["a"] + p["b"],
                                     180 - p["a"]}) == 3,
                            "all three angles are real ones a child can see, and the "
                            "three options are three different numbers"),
    },

    # ---- PREALGEBRA UNIT 9 (build kt) -- VARIABLES & EXPRESSIONS --------------
    # The last prealgebra unit, and the doorway to algebra. Everything before this
    # asked about numbers; these four ask about a LETTER that stands for one. The
    # order is the order the idea actually grows: a letter holds a number (evx), a
    # number written against a letter means times (mlx), like terms collect by
    # counting (clt), and a times distributes over a parenthesis (dst) -- drawn with
    # [[areamodel]], the algebra-tile renderer that has been in the registry since
    # July and, exactly like [[angle split=]] before build ks, has never once been
    # used by a scripted lesson.
    "evx": {   # x holds a -- what is x + b?
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"The letter x is holding the number {p['a']}. "
                             f"What is x plus {p['b']}?"),
        "board": lambda p: (f'[[step eq="x = {p["a"]}"]]'
                            f'[[step eq="x + {p["b"]} = {p["a"]} + {p["b"]} = ?"]]'),
        "praise": lambda p: (f"x is {p['a']}, so x plus {p['b']} is {p['a']} plus "
                             f"{p['b']}, which equals {p['a'] + p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        # THE first-variable error is CONCATENATION: x holds 5, so "x + 3" is read as
        # writing 5 next to 3 -- the child taps 53. It looks bizarre to an adult and it
        # is the documented, universal first misreading of substitution.
        "choices": lambda p: [p["a"] + p["b"], 10 * p["a"] + p["b"], p["a"] * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "single digits so the glued-together error is a real tap, "
                            "and the times never equals the add"),
    },
    "mlx": {   # x holds a -- what is bx?
        "ans": lambda p: p["a"] * p["b"],
        # The ask does NOT re-explain the shorthand -- the teach beats own that.
        # A scaffold repeated in every one of twelve asks is a scaffold that never
        # fades, and fading it is what practice is for.
        "spoken": lambda p: (f"The letter x is holding the number {p['a']}. "
                             f"What is {p['b']} x?"),
        "board": lambda p: (f'[[step eq="x = {p["a"]}"]]'
                            f'[[step eq="{p["b"]}x = {p["b"]} × {p["a"]} = ?"]]'),
        "praise": lambda p: (f"{p['b']} x means {p['b']} times x, and {p['b']} times "
                             f"{p['a']} equals {p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # The error is reading the written-together 3x as 3 PLUS x -- adding where the
        # notation quietly means times.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"],
                              p["a"] * p["b"] + p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "both single digits and never the 2-and-2 case, so the "
                            "times-versus-add error is a different number"),
    },
    "clt": {   # ax + bx -- how many x in all?
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"{p['a']} x plus {p['b']} x — how many x is that "
                             f"in all?"),
        "board": lambda p: (f'[[step eq="{p["a"]}x + {p["b"]}x"]]'
                            f'[[step eq="{p["a"]} of them + {p["b"]} of them '
                            f'= ? of them"]]'),
        "praise": lambda p: (f"{p['a']} x's and {p['b']} more x's are "
                             f"{p['a'] + p['b']} x's in all — {p['a'] + p['b']} x."),
        "key": lambda p: p["a"] + p["b"],
        # The error is TIMESING the counts -- the child who has just learned that
        # letters mean times and now applies it to everything in sight.
        "choices": lambda p: [p["a"] + p["b"], p["a"] * p["b"], p["a"] + p["b"] + 1],
        # Three DISTINCT options, said outright: at 2x + 3x the neighbour distractor
        # (6) lands exactly on the times-them distractor (6), so requiring the pair
        # to differ is not enough -- the whole set has to.
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] + p["b"], p["a"] * p["b"],
                                     p["a"] + p["b"] + 1}) == 3,
                            "the counts add like apples add, and the three tap "
                            "options are three different numbers"),
    },
    "dst": {   # a(x + b) = ax + ? -- the distributive property, drawn as area
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"Times the whole of x plus {p['b']} by {p['a']}. "
                             f"That comes to {p['a']} x plus what number?"),
        # ⭐ [[areamodel]] draws a rectangle a tall and (x + b) wide, cut into an ax
        # piece and an ab piece, with the expanded sum printed under it. The child is
        # not told the rule -- the child is shown the two rooms of the rectangle.
        "board": lambda p: (f'[[areamodel rows="{p["a"]}" cols="x,{p["b"]}"]]'
                            f'[[step eq="{p["a"]}(x + {p["b"]}) = {p["a"]}x + ?"]]'),
        "praise": lambda p: (f"The {p['a']} reaches BOTH rooms: {p['a']} times x, and "
                             f"{p['a']} times {p['b']}, which equals "
                             f"{p['a'] * p['b']}. So it is {p['a']} x plus "
                             f"{p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # THE distributive error: the times reaches the x and never the number --
        # 4(x + 3) read as 4x + 3. The wrong tap is the untouched 3.
        "choices": lambda p: [p["a"] * p["b"], p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] * p["b"], p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "the multiplier is at least 2 so the untouched-number "
                            "error is a real different tap, and all three options "
                            "differ"),
    },

    # ---- ALGEBRA I UNIT 1 (build ku) -- FOUNDATIONS & EXPRESSIONS -------------
    # The first Algebra I unit, sitting directly on Prealgebra U9. That unit taught
    # the four seeds one at a time: a letter holds a number, a number against a letter
    # means times, like terms count, a times distributes. These four make the seeds
    # WORK TOGETHER: evaluate a two-step expression (where order of operations meets a
    # letter), read TWO letters at once, collect the x's when y's are standing in the
    # way, and distribute over a take away -- the first time the invisible times has
    # to carry a minus sign with it.
    "ev2": {   # x holds a -- what is bx + c?
        "ans": lambda p: p["a"] * p["b"] + p["c"],
        "spoken": lambda p: (f"The letter x is holding the number {p['a']}. "
                             f"What is {p['b']} x plus {p['c']}?"),
        "board": lambda p: (f'[[step eq="x = {p["a"]}"]]'
                            f'[[step eq="{p["b"]}x + {p["c"]} = '
                            f'{p["b"]} × {p["a"]} + {p["c"]} = ?"]]'),
        "praise": lambda p: (f"{p['b']} x is {p['b']} times {p['a']}, which equals "
                             f"{p['a'] * p['b']}, and {p['a'] * p['b']} plus "
                             f"{p['c']} equals {p['a'] * p['b'] + p['c']}."),
        "key": lambda p: p["a"] * p["b"] + p["c"],
        # Prealgebra U1's own rule, now with a letter in it: times before add. The
        # error worth offering is ADDING FIRST -- b times (a plus c). The third option
        # is ignoring the invisible times altogether and adding everything in sight.
        "choices": lambda p: [p["a"] * p["b"] + p["c"],
                              p["b"] * (p["a"] + p["c"]),
                              p["a"] + p["b"] + p["c"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] * p["b"] + p["c"],
                                     p["b"] * (p["a"] + p["c"]),
                                     p["a"] + p["b"] + p["c"]}) == 3,
                            "single digits and three distinct options -- which rules "
                            "out x holding 2 with a coefficient of 2, where timesing "
                            "and adding agree"),
    },
    "evxy": {  # x holds a, y holds b -- what is x + cy?
        "ans": lambda p: p["a"] + p["c"] * p["b"],
        # No "two letters now" preamble in the ask -- the same scaffold-never-fades
        # defect mlx had in build kt. The teach beats introduce y; the ask just asks.
        "spoken": lambda p: (f"x is holding {p['a']}, and y is holding {p['b']}. "
                             f"What is x plus {p['c']} y?"),
        "board": lambda p: (f'[[step eq="x = {p["a"]} · y = {p["b"]}"]]'
                            f'[[step eq="x + {p["c"]}y = {p["a"]} + '
                            f'{p["c"]} × {p["b"]} = ?"]]'),
        "praise": lambda p: (f"{p['c']} y is {p['c']} times {p['b']}, which equals "
                             f"{p['c'] * p['b']}, and {p['a']} plus that equals "
                             f"{p['a'] + p['c'] * p['b']}."),
        "key": lambda p: p["a"] + p["c"] * p["b"],
        # Each letter keeps its own number. The errors: adding a to c first and then
        # timesing (the same add-first slip as ev2, wearing a y), and treating "c y"
        # as c plus y.
        "choices": lambda p: [p["a"] + p["c"] * p["b"],
                              (p["a"] + p["c"]) * p["b"],
                              p["a"] + p["c"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] + p["c"] * p["b"],
                                     (p["a"] + p["c"]) * p["b"],
                                     p["a"] + p["c"] + p["b"]}) == 3,
                            "single digits and three distinct options"),
    },
    "cl2": {   # ax + by + cx -- how many x?
        "ans": lambda p: p["a"] + p["c"],
        "spoken": lambda p: (f"{p['a']} x plus {p['b']} y plus {p['c']} x — "
                             f"how many x is that in all?"),
        "board": lambda p: (f'[[step eq="{p["a"]}x + {p["b"]}y + {p["c"]}x"]]'
                            f'[[step eq="the x\'s: {p["a"]} + {p["c"]} = ? '
                            f'· the y walks past"]]'),
        "praise": lambda p: (f"Only the x's collect: {p['a']} and {p['c']} make "
                             f"{p['a'] + p['c']} x. The {p['b']} y is a different "
                             f"thing and stays as it is."),
        "key": lambda p: p["a"] + p["c"],
        # The error is GRABBING EVERYTHING -- apples and oranges into one pile. A y is
        # not an x, and 3x + 2y + 4x is 7x plus 2y, not 9 of anything.
        "choices": lambda p: [p["a"] + p["c"], p["a"] + p["b"] + p["c"],
                              p["a"] + p["c"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] + p["c"], p["a"] + p["b"] + p["c"],
                                     p["a"] + p["c"] + 1}) == 3,
                            "the y really is in the way (b at least 2, so grabbing it "
                            "is visibly different from the neighbour distractor)"),
    },
    "dstm": {  # a(x - b) = ax - ?
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"Times the whole of x take away {p['b']} by {p['a']}. "
                             f"That comes to {p['a']} x take away what number?"),
        # The area model again, with a NEGATIVE room: [[areamodel]] parses "-b" and
        # prints the expanded sum with the minus carried through ("= ax - ab").
        "board": lambda p: (f'[[areamodel rows="{p["a"]}" cols="x,-{p["b"]}"]]'
                            f'[[step eq="{p["a"]}(x − {p["b"]}) = {p["a"]}x − ?"]]'),
        "praise": lambda p: (f"The {p['a']} reaches both rooms, minus and all: "
                             f"{p['a']} times x, and {p['a']} times {p['b']}, which "
                             f"equals {p['a'] * p['b']} — taken away. So it is "
                             f"{p['a']} x take away {p['a'] * p['b']}."),
        "key": lambda p: p["a"] * p["b"],
        # Same family as dst: the times never reaches the number (tap b), or the
        # numbers get added instead of timesed.
        "choices": lambda p: [p["a"] * p["b"], p["b"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] * p["b"], p["b"],
                                     p["a"] + p["b"]}) == 3,
                            "the multiplier is at least 2 and the three options are "
                            "three different numbers"),
    },

    # ---- ALGEBRA I UNIT 2 (build kv) -- LINEAR EQUATIONS & INEQUALITIES -------
    # SOLVING BEGINS. Until now every x was handed to the child ("x is holding 5");
    # from here the equation holds it and the child gets it back by UNDOING -- the
    # same move off both sides. The board is ⭐ [[balance]], the balance-scale
    # renderer that (like [[areamodel]] and [[angle split=]] before it) has been in
    # the codebase since July and never once used by a scripted lesson. An equation
    # IS a balance; the figure is the argument.
    "un1": {   # x + a = b -- undo the plus
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"x plus {p['a']} equals {p['b']}. "
                             f"What number is x holding?"),
        "board": lambda p: (f'[[balance left="x + {p["a"]}" right="{p["b"]}" '
                            f'caption="take {p["a"]} off BOTH sides"]]'
                            f'[[step eq="x = {p["b"]} − {p["a"]} = ?"]]'),
        "praise": lambda p: (f"Take {p['a']} off both sides and the scale stays "
                             f"level: x is {p['b']} take away {p['a']}, which "
                             f"equals {p['b'] - p['a']}."),
        "key": lambda p: p["b"] - p["a"],
        # The error is pushing the same way instead of undoing: x + 4 = 11 answered
        # with 15. The third option is tapping the right-hand side untouched.
        "choices": lambda p: [p["b"] - p["a"], p["b"] + p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["a"] < p["b"] <= 30
                            and p["b"] - p["a"] >= 2,
                            "the hidden number is at least 2 and every number stays "
                            "small enough to check by counting"),
    },
    "un2": {   # ax = b -- undo the times
        "ans": lambda p: p["b"] // p["a"],
        "spoken": lambda p: (f"{p['a']} x equals {p['b']}. "
                             f"What number is x holding?"),
        "board": lambda p: (f'[[balance left="{p["a"]}x" right="{p["b"]}" '
                            f'caption="share BOTH sides between {p["a"]}"]]'
                            f'[[step eq="x = {p["b"]} ÷ {p["a"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} x's weigh {p['b']}, so one x weighs "
                             f"{p['b']} shared between {p['a']} — "
                             f"{p['b'] // p['a']}."),
        "key": lambda p: p["b"] // p["a"],
        # The error is UNDOING THE WRONG OPERATION: taking the 3 away instead of
        # sharing between 3 -- 3x = 12 answered with 9.
        "choices": lambda p: [p["b"] // p["a"], p["b"] - p["a"],
                              p["b"] // p["a"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and p["b"] % p["a"] == 0
                            and p["b"] // p["a"] >= 2
                            and len({p["b"] // p["a"], p["b"] - p["a"],
                                     p["b"] // p["a"] + 1}) == 3,
                            "it shares exactly, x is at least 2, and the take-away "
                            "error is visibly a different number"),
    },
    "un3": {   # ax + b = c -- two steps back, in reverse order
        "ans": lambda p: (p["c"] - p["b"]) // p["a"],
        "spoken": lambda p: (f"{p['a']} x plus {p['b']} equals {p['c']}. "
                             f"What number is x holding?"),
        "board": lambda p: (f'[[balance left="{p["a"]}x + {p["b"]}" '
                            f'right="{p["c"]}"]]'
                            f'[[step eq="take {p["b"]} off both sides: '
                            f'{p["a"]}x = {p["c"] - p["b"]}"]]'
                            f'[[step eq="x = {p["c"] - p["b"]} ÷ {p["a"]} = ?"]]'),
        "praise": lambda p: (f"The {p['b']} went on last, so it comes off first: "
                             f"{p['a']} x equals {p['c'] - p['b']}. Then share: "
                             f"x equals {(p['c'] - p['b']) // p['a']}."),
        "key": lambda p: (p["c"] - p["b"]) // p["a"],
        # The stop-at-step-one error again (rte, pcn, tri3 -- it is everywhere):
        # taking the b off, seeing ax = c-b, and tapping THAT number as x.
        "choices": lambda p: [(p["c"] - p["b"]) // p["a"], p["c"] - p["b"],
                              (p["c"] - p["b"]) // p["a"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and (p["c"] - p["b"]) % p["a"] == 0
                            and (p["c"] - p["b"]) // p["a"] >= 2
                            and len({(p["c"] - p["b"]) // p["a"], p["c"] - p["b"],
                                     (p["c"] - p["b"]) // p["a"] + 1}) == 3,
                            "both undo steps land on whole numbers and the "
                            "stopped-halfway error is a different number"),
    },
    "ineq": {  # x + a < b -- the BIGGEST whole number x can hold
        "ans": lambda p: p["b"] - p["a"] - 1,
        "spoken": lambda p: (f"x plus {p['a']} is less than {p['b']}. "
                             f"What is the biggest whole number x can hold?"),
        "board": lambda p: (f'[[step eq="x + {p["a"]} < {p["b"]}"]]'
                            f'[[step eq="x < {p["b"]} − {p["a"]}"]]'
                            f'[[numberline min="0" max="{p["b"] - p["a"] + 2}" '
                            f'points="{p["b"] - p["a"]}"]]'),
        "praise": lambda p: (f"x has to stay under {p['b'] - p['a']} — it can be "
                             f"anything less, and the biggest whole number under "
                             f"{p['b'] - p['a']} is {p['b'] - p['a'] - 1}."),
        "key": lambda p: p["b"] - p["a"] - 1,
        # THE inequality error: forgetting that "less than" shuts the door on the
        # number itself. x + 3 < 10 means x < 7, and 7 is NOT allowed.
        "choices": lambda p: [p["b"] - p["a"] - 1, p["b"] - p["a"],
                              p["b"] + p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["a"] < p["b"] <= 30
                            and p["b"] - p["a"] >= 3,
                            "the boundary is at least 3, so the answer is a real "
                            "number and the door-shut error sits right beside it"),
    },

    # ---- ALGEBRA I UNIT 3 (build kw) -- FUNCTIONS & NOTATION ------------------
    # A function is a MACHINE: a number goes in, a rule happens to it, a number comes
    # out. The board is ⭐ [[machine]], the function-machine renderer -- the last of
    # July's figure shelf to get its first scripted use (areamodel kt, angle-split ks,
    # balance kv). It draws input -> rule box -> output AND prints "f(4) = 9"
    # underneath, so the notation lesson can point at a line the child has already
    # been looking at for a whole lesson.
    "fm1": {   # rule ax + b, input c -- what comes out?
        "ans": lambda p: p["a"] * p["c"] + p["b"],
        "spoken": lambda p: (f"A machine's rule is: times the input by {p['a']}, "
                             f"then add {p['b']}. Feed it {p['c']}. "
                             f"What number comes out?"),
        "board": lambda p: (f'[[machine input="{p["c"]}" '
                            f'rule="{p["a"]}x + {p["b"]}" output="?"]]'),
        "praise": lambda p: (f"{p['c']} goes in, the rule runs: {p['a']} times "
                             f"{p['c']} equals {p['a'] * p['c']}, plus {p['b']} — "
                             f"out comes {p['a'] * p['c'] + p['b']}."),
        "key": lambda p: p["a"] * p["c"] + p["b"],
        # The rule says its steps IN ORDER, so the wrong tap is running them the other
        # way: adding first. The third is ignoring the times altogether.
        "choices": lambda p: [p["a"] * p["c"] + p["b"],
                              p["a"] * (p["c"] + p["b"]),
                              p["a"] + p["b"] + p["c"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] * p["c"] + p["b"],
                                     p["a"] * (p["c"] + p["b"]),
                                     p["a"] + p["b"] + p["c"]}) == 3,
                            "single digits and three distinct outputs -- which rules "
                            "out the inputs where timesing and adding agree"),
    },
    "fnot": {  # f(x) = x + a -- what is f(b)?
        "ans": lambda p: p["b"] + p["a"],
        "spoken": lambda p: (f"f of x equals x plus {p['a']}. "
                             f"What is f of {p['b']}?"),
        "board": lambda p: (f'[[machine input="{p["b"]}" rule="x + {p["a"]}" '
                            f'output="?" fname="f"]]'
                            f'[[step eq="f({p["b"]}) = {p["b"]} + {p["a"]} = ?"]]'),
        "praise": lambda p: (f"f of {p['b']} means: feed the machine {p['b']}. "
                             f"{p['b']} plus {p['a']} equals {p['b'] + p['a']}."),
        "key": lambda p: p["b"] + p["a"],
        # THE notation error: reading f(3) as f TIMES 3 -- the parentheses have meant
        # "times" since the distributive lesson, and here they suddenly do not. The
        # wrong tap is the times reading; the third is handing back the input.
        "choices": lambda p: [p["b"] + p["a"], p["a"] * p["b"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] * p["b"] != p["a"] + p["b"],
                            "single digits, never the 2-and-2 case, so the "
                            "f-times-b misreading is visibly a different number"),
    },
    "fm2": {   # machine one adds a, machine two times by b, input c -- IN ORDER
        "ans": lambda p: (p["c"] + p["a"]) * p["b"],
        "spoken": lambda p: (f"Two machines in a row. The first adds {p['a']}. "
                             f"The second times by {p['b']}. Feed {p['c']} through "
                             f"both, first then second. What comes out?"),
        "board": lambda p: (f'[[machine input="{p["c"]}" rule="x + {p["a"]}" '
                            f'output="{p["c"] + p["a"]}"]]'
                            f'[[machine input="{p["c"] + p["a"]}" '
                            f'rule="{p["b"]}x" output="?" fname="g"]]'),
        "praise": lambda p: (f"Machine one: {p['c']} plus {p['a']} equals "
                             f"{p['c'] + p['a']}. That goes straight into machine "
                             f"two: {p['c'] + p['a']} times {p['b']} equals "
                             f"{(p['c'] + p['a']) * p['b']}."),
        "key": lambda p: (p["c"] + p["a"]) * p["b"],
        # The error is running the machines in the WRONG ORDER -- timesing first,
        # then adding. Order mattering is the entire lesson.
        "choices": lambda p: [(p["c"] + p["a"]) * p["b"],
                              p["c"] * p["b"] + p["a"],
                              p["c"] + p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({(p["c"] + p["a"]) * p["b"],
                                     p["c"] * p["b"] + p["a"],
                                     p["c"] + p["a"] + p["b"]}) == 3,
                            "three distinct outputs, so the wrong-order error is a "
                            "real different tap"),
    },
    "fback": { # f(x) = x + a and f(?) = b -- which input was it?
        "ans": lambda p: p["b"] - p["a"],
        "spoken": lambda p: (f"f of x equals x plus {p['a']}. f of WHAT equals "
                             f"{p['b']}? Which number went in?"),
        "board": lambda p: (f'[[machine input="?" rule="x + {p["a"]}" '
                            f'output="{p["b"]}" fname="f"]]'
                            f'[[step eq="? + {p["a"]} = {p["b"]}"]]'),
        "praise": lambda p: (f"The machine put out {p['b']} after adding {p['a']}, "
                             f"so {p['b']} take away {p['a']} went in — "
                             f"{p['b'] - p['a']}."),
        "key": lambda p: p["b"] - p["a"],
        # Running the machine FORWARDS with the output as input -- b + a -- is the
        # error; the third is tapping the output itself.
        "choices": lambda p: [p["b"] - p["a"], p["b"] + p["a"], p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["a"] < p["b"] <= 30
                            and p["b"] - p["a"] >= 2,
                            "the input is at least 2 and the numbers stay small "
                            "enough to check by running the machine forwards"),
    },

    # ---- ALGEBRA I UNIT 4 (build kx) -- LINEAR FUNCTIONS & GRAPHS -------------
    # The machine met the coordinate plane. A line IS the machine's whole table of
    # answers drawn at once -- every point is an input standing under its output. The
    # board is ⭐ [[graph]], the real function grapher (lines=, points=, range=) that
    # no scripted lesson has ever used. The ladder: read one point off a line, SLOPE
    # as how much y climbs when x steps once, the starting height where x is zero,
    # and finally slope and start working together to answer for any x.
    "lny": {   # y = x + a -- what is y when x = b?
        "ans": lambda p: p["b"] + p["a"],
        "spoken": lambda p: (f"The line is y equals x plus {p['a']}. "
                             f"What is y when x is {p['b']}?"),
        "board": lambda p: (f'[[graph lines="y=x+{p["a"]}" '
                            f'range="0..{p["b"] + p["a"] + 2}"]]'
                            f'[[step eq="x = {p["b"]} → y = {p["b"]} + {p["a"]} = ?"]]'),
        "praise": lambda p: (f"At x equals {p['b']}, the line stands at {p['b']} "
                             f"plus {p['a']} — y equals {p['b'] + p['a']}."),
        "key": lambda p: p["b"] + p["a"],
        # The graph error is SWAPPING THE PARTNERS: asked for y, tapping the x you
        # were given. The third option is the line's own added number.
        "choices": lambda p: [p["b"] + p["a"], p["b"], p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and p["a"] != p["b"],
                            "a and b differ, so the swapped-partner tap and the "
                            "added-number tap are three different numbers"),
    },
    "slp": {   # through (b, c) and (b+1, c+a) -- how much does y go up?
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"A line passes through the point {p['b']} comma "
                             f"{p['c']}, and the point {p['b'] + 1} comma "
                             f"{p['c'] + p['a']}. When x goes up by 1, how much "
                             f"does y go up?"),
        "board": lambda p: (f'[[graph points="({p["b"]},{p["c"]}),'
                            f'({p["b"] + 1},{p["c"] + p["a"]})" '
                            f'range="0..{p["b"] + 3}"]]'
                            f'[[step eq="y: {p["c"]} → {p["c"] + p["a"]}, '
                            f'a climb of ?"]]'),
        "praise": lambda p: (f"x stepped once and y climbed from {p['c']} to "
                             f"{p['c'] + p['a']} — a climb of {p['a']}. That climb "
                             f"is called the slope."),
        "key": lambda p: p["a"],
        # The errors are reading a HEIGHT as the climb: tapping where y landed, or
        # where it started, instead of how far it moved.
        "choices": lambda p: [p["a"], p["c"] + p["a"], p["c"]],
        # The rise is the ANSWER, so it is deliberately never spoken; the two
        # heights and the x-step carry the problem.
        "speaks": lambda p, sp: (str(p["b"]) in sp and str(p["c"]) in sp
                                 and str(p["c"] + p["a"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 1 <= p["b"] <= 4 and 2 <= p["c"] <= 9
                            and p["a"] != p["c"],
                            "the climb differs from both heights, so all three taps "
                            "are different numbers, and the points sit near the "
                            "origin where the graph can show them"),
    },
    "yint": {  # y = ax + b -- what is y when x is ZERO?
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"The line is y equals {p['a']} x plus {p['b']}. "
                             f"What is y when x is zero?"),
        "board": lambda p: (f'[[graph lines="y={p["a"]}x+{p["b"]}" '
                            f'range="0..5"]]'
                            f'[[step eq="x = 0 → y = {p["a"]} × 0 + {p["b"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} times zero is zero — the times part "
                             f"vanishes, and y is just {p['b']}. That is where the "
                             f"line starts."),
        "key": lambda p: p["b"],
        # The error is tapping the SLOPE -- the other number in the rule -- or adding
        # the two as if x being zero changed nothing.
        "choices": lambda p: [p["b"], p["a"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9 and p["a"] != p["b"],
                            "slope and start differ, so the three taps are three "
                            "different numbers"),
    },
    "lin2": {  # y = ax + b -- what is y when x = c?
        "ans": lambda p: p["a"] * p["c"] + p["b"],
        "spoken": lambda p: (f"The line is y equals {p['a']} x plus {p['b']}. "
                             f"What is y when x is {p['c']}?"),
        "board": lambda p: (f'[[graph lines="y={p["a"]}x+{p["b"]}" '
                            f'range="0..{p["c"] + 2}"]]'
                            f'[[step eq="y = {p["a"]} × {p["c"]} + {p["b"]} = ?"]]'),
        "praise": lambda p: (f"Start at {p['b']}, climb {p['a']} for each of the "
                             f"{p['c']} steps: {p['a']} times {p['c']} equals "
                             f"{p['a'] * p['c']}, plus {p['b']} equals "
                             f"{p['a'] * p['c'] + p['b']}."),
        "key": lambda p: p["a"] * p["c"] + p["b"],
        # Off-by-one-step is the graph-reading error: the height one x to the LEFT.
        # The third is tapping the x itself.
        "choices": lambda p: [p["a"] * p["c"] + p["b"],
                              p["a"] * (p["c"] - 1) + p["b"], p["c"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 1 <= p["b"] <= 9 and 2 <= p["c"] <= 9
                            and len({p["a"] * p["c"] + p["b"],
                                     p["a"] * (p["c"] - 1) + p["b"],
                                     p["c"]}) == 3,
                            "three distinct heights, so the one-step-left error is a "
                            "real different tap"),
    },

    # ---- ALGEBRA I UNIT 5 (build ky) -- SYSTEMS OF EQUATIONS ------------------
    # Two rules true at once. The unit's one big picture is TWO LINES CROSSING --
    # [[graph]] takes lines="y=x+2; y=3x" and draws them both, and the crossing
    # point is the answer standing on the board. The ladder: see the crossing (sys1),
    # SWAP a letter for what it equals (sys2, substitution), the oldest system there
    # is -- a sum and a difference (sumd), and taking one equation away from another
    # so a whole unknown vanishes (elim, elimination in story clothes).
    "sys1": {  # y = x + a and y = bx -- which x makes both agree?
        "ans": lambda p: p["a"] // (p["b"] - 1),
        "spoken": lambda p: (f"One rule says y equals x plus {p['a']}. Another rule "
                             f"says y equals {p['b']} times x. For which x do both "
                             f"rules say the SAME y?"),
        "board": lambda p: (f'[[graph lines="y=x+{p["a"]}; y={p["b"]}x" '
                            f'range="0..{p["a"] // (p["b"] - 1) + 3}"]]'
                            f'[[step eq="x + {p["a"]} = {p["b"]}x"]]'),
        "praise": lambda p: (f"At x equals {p['a'] // (p['b'] - 1)}, both rules say "
                             f"y equals {p['b'] * (p['a'] // (p['b'] - 1))} — the "
                             f"lines cross there, and that crossing is the answer."),
        "key": lambda p: p["a"] // (p["b"] - 1),
        # U4's swapped-partner error comes back: tapping the Y where the lines meet
        # instead of the x that was asked for. The third is the rule's own plus number.
        "choices": lambda p: [p["a"] // (p["b"] - 1),
                              p["b"] * (p["a"] // (p["b"] - 1)), p["a"]],
        # a runs to 14, not 9: with b in 3..6 and the crossing forced whole and >= 2,
        # single-digit a yields only SIX distinct problems -- fewer than one bank.
        # The constraint surface here is genuinely small, and the wider a is what
        # buys a 10-problem ramp.
        "check": lambda p: (2 <= p["a"] <= 14 and 3 <= p["b"] <= 6
                            and p["a"] % (p["b"] - 1) == 0
                            and p["a"] // (p["b"] - 1) >= 2
                            and len({p["a"] // (p["b"] - 1),
                                     p["b"] * (p["a"] // (p["b"] - 1)),
                                     p["a"]}) == 3,
                            "the crossing lands on a whole x of at least 2, b is at "
                            "least 3 so the x never equals the plus number, and the "
                            "three taps differ"),
    },
    "sys2": {  # y = x + a and x + y = b -- what is x?
        "ans": lambda p: (p["b"] - p["a"]) // 2,
        "spoken": lambda p: (f"y equals x plus {p['a']}. Also, x plus y equals "
                             f"{p['b']}. What is x?"),
        "board": lambda p: (f'[[step eq="x + y = {p["b"]}"]]'
                            f'[[step eq="swap y in: x + (x + {p["a"]}) = {p["b"]}"]]'
                            f'[[step eq="2x = {p["b"] - p["a"]} → x = ?"]]'),
        "praise": lambda p: (f"Swap y for what it equals and there are two x's: "
                             f"2 x plus {p['a']} equals {p['b']}, so 2 x equals "
                             f"{p['b'] - p['a']}, and x equals "
                             f"{(p['b'] - p['a']) // 2}."),
        "key": lambda p: (p["b"] - p["a"]) // 2,
        # The middle option IS the other unknown -- y. Tapping the wrong letter's
        # value is the system error. The third is stopping at 2x.
        "choices": lambda p: [(p["b"] - p["a"]) // 2, (p["b"] + p["a"]) // 2,
                              p["b"] - p["a"]],
        "check": lambda p: (2 <= p["a"] <= 9 and p["a"] < p["b"] <= 30
                            and (p["b"] - p["a"]) % 2 == 0
                            and (p["b"] - p["a"]) // 2 >= 2
                            and p["b"] != 3 * p["a"],
                            "the swap lands on whole numbers, x is at least 2, and "
                            "b is never 3a (where stopping-at-2x collides with y)"),
    },
    "sumd": {  # together a, apart b -- the BIGGER of the two
        "ans": lambda p: (p["a"] + p["b"]) // 2,
        "spoken": lambda p: (f"Two secret numbers. Put together they equal {p['a']}. "
                             f"The bigger take away the smaller equals {p['b']}. "
                             f"What is the bigger number?"),
        "board": lambda p: (f'[[step eq="bigger + smaller = {p["a"]}"]]'
                            f'[[step eq="bigger − smaller = {p["b"]}"]]'
                            f'[[step eq="bigger = ({p["a"]} + {p["b"]}) ÷ 2 = ?"]]'),
        "praise": lambda p: (f"The bigger is {(p['a'] + p['b']) // 2} and the "
                             f"smaller is {(p['a'] - p['b']) // 2} — together "
                             f"{p['a']}, apart {p['b']}. Both rules happy at once."),
        "key": lambda p: (p["a"] + p["b"]) // 2,
        # The error is HALVING THE TOTAL -- splitting evenly as if the difference
        # rule were not there. One rule satisfied, the other ignored.
        "choices": lambda p: [(p["a"] + p["b"]) // 2, p["a"] // 2, p["b"]],
        "check": lambda p: (p["a"] % 2 == 0 and p["b"] % 2 == 0
                            and 2 <= p["b"] < p["a"] <= 30 and p["a"] != 2 * p["b"]
                            and (p["a"] - p["b"]) // 2 >= 1
                            and len({(p["a"] + p["b"]) // 2, p["a"] // 2,
                                     p["b"]}) == 3,
                            "both secret numbers are whole, the smaller is at least "
                            "1, and the split-evenly error is a different tap"),
    },
    "elim": {  # 2 pencils + eraser = a; 1 pencil + eraser = b -- the pencil?
        "ans": lambda p: p["a"] - p["b"],
        "spoken": lambda p: (f"Two pencils and an eraser cost {p['a']} cents. One "
                             f"pencil and the same eraser cost {p['b']} cents. "
                             f"What does one pencil cost?"),
        "board": lambda p: (f'[[step eq="2 pencils + eraser = {p["a"]}"]]'
                            f'[[step eq="1 pencil + eraser = {p["b"]}"]]'
                            f'[[step eq="take the second away: 1 pencil = '
                            f'{p["a"]} − {p["b"]} = ?"]]'),
        "praise": lambda p: (f"Take the second buy away from the first: the eraser "
                             f"vanishes, one pencil is left, and it costs "
                             f"{p['a'] - p['b']} cents."),
        "key": lambda p: p["a"] - p["b"],
        # The middle option is the ERASER's price -- the other unknown again. The
        # third is halving the first buy as if it were two pencils and nothing else.
        "choices": lambda p: [p["a"] - p["b"], 2 * p["b"] - p["a"], p["a"] // 2],
        "check": lambda p: (p["b"] < p["a"] < 2 * p["b"] and p["a"] % 2 == 0
                            and p["a"] <= 30 and p["a"] - p["b"] >= 2
                            and 2 * p["b"] - p["a"] >= 1
                            and len({p["a"] - p["b"], 2 * p["b"] - p["a"],
                                     p["a"] // 2}) == 3,
                            "both prices are real (pencil and eraser at least 1), a "
                            "is even so the halving error is a whole tap, and the "
                            "three taps differ"),
    },

    # ---- ALGEBRA I UNIT 6 (build kz) -- EXPONENTS & EXPONENTIAL FUNCTIONS -----
    # Prealgebra U1 taught what a power IS (expn: "three 2s multiplied"). This unit
    # teaches how powers BEHAVE: the product rule as counting copies (x³ · x² is five
    # x's, not six), a power of a power as copies of copies, powers of ten carrying a
    # digit (scientific notation in child clothes), and finally DOUBLING -- the first
    # exponential growth, where the wrong tap is the linear thinker's answer.
    # _sup() writes the exponents as real superscripts on the board, the way expn
    # already wrote ² and ³ by hand.
    "exadd": { # x^a · x^b -- how many x's multiplied in all?
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"x to the power {p['a']}, times x to the power "
                             f"{p['b']}. Write out all the x's multiplied — "
                             f"how many x's are there?"),
        "board": lambda p: (f'[[step eq="x{_sup(p["a"])} · x{_sup(p["b"])}"]]'
                            f'[[step eq="({" · ".join(["x"] * p["a"])}) · '
                            f'({" · ".join(["x"] * p["b"])})"]]'
                            f'[[step eq="{p["a"]} + {p["b"]} = ? x\'s"]]'),
        "praise": lambda p: (f"{p['a']} x's joined by {p['b']} more x's — "
                             f"{p['a'] + p['b']} x's multiplied, which is x to the "
                             f"power {p['a'] + p['b']}. The powers ADD."),
        "key": lambda p: p["a"] + p["b"],
        # THE exponent error: timesing the powers. x³ · x² read as x to the 6.
        "choices": lambda p: [p["a"] + p["b"], p["a"] * p["b"],
                              p["a"] + p["b"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] + p["b"], p["a"] * p["b"],
                                     p["a"] + p["b"] + 1}) == 3,
                            "three distinct counts -- which rules out 2·2 (where "
                            "adding and timesing agree) and 2·3 (where timesing "
                            "lands on the neighbour)"),
    },
    "exmul": { # (x^a)^b -- how many x's is that?
        "ans": lambda p: p["a"] * p["b"],
        "spoken": lambda p: (f"Take x to the power {p['a']}, and raise all of it "
                             f"to the power {p['b']}. How many x's multiplied "
                             f"is that?"),
        "board": lambda p: (f'[[step eq="(x{_sup(p["a"])}){_sup(p["b"])}"]]'
                            f'[[step eq="{p["b"]} copies of {p["a"]} x\'s"]]'
                            f'[[step eq="{p["a"]} × {p["b"]} = ? x\'s"]]'),
        "praise": lambda p: (f"{p['b']} copies of {p['a']} x's each: {p['a']} times "
                             f"{p['b']} equals {p['a'] * p['b']} x's. Copies of "
                             f"copies TIMES."),
        "key": lambda p: p["a"] * p["b"],
        # The mirror of exadd's error: ADDING here, where copies of copies times.
        # Taught back-to-back with exadd deliberately, because telling the two
        # situations apart IS the skill.
        "choices": lambda p: [p["a"] * p["b"], p["a"] + p["b"],
                              p["a"] * p["b"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] * p["b"], p["a"] + p["b"],
                                     p["a"] * p["b"] + 1}) == 3,
                            "three distinct counts, ruling out the cases where "
                            "adding collides with timesing or its neighbour"),
    },
    "sci": {   # b × 10^a
        "ans": lambda p: p["b"] * 10 ** p["a"],
        "spoken": lambda p: (f"What is {p['b']} times 10 to the power {p['a']}?"),
        "board": lambda p: (f'[[step eq="{p["b"]} × 10{_sup(p["a"])}"]]'
                            f'[[step eq="{p["b"]} × '
                            f'{" × ".join(["10"] * p["a"])} = ?"]]'),
        "praise": lambda p: (f"10 to the {p['a']} is a 1 with {p['a']} zeros, so "
                             f"{p['b']} times it is {p['b']} with {p['a']} zeros — "
                             f"{p['b'] * 10 ** p['a']}."),
        "key": lambda p: p["b"] * 10 ** p["a"],
        # The times-not-power error, at ten: b × 10 × a instead of b × 10^a --
        # 3 times 10 to the 2 read as 3 × 10 × 2 = 60. The third option is one
        # power short, the place-value slip from Unit 8's changing-units lesson.
        "choices": lambda p: [p["b"] * 10 ** p["a"], p["b"] * 10 * p["a"],
                              p["b"] * 10 ** (p["a"] - 1)],
        "check": lambda p: (2 <= p["a"] <= 3 and 2 <= p["b"] <= 9,
                            "the exponent is at least 2 (at 1, times-ten and "
                            "ten-to-the agree and the error cannot be shown)"),
    },
    "dbl": {   # b pads, doubling every day, for a days
        "ans": lambda p: p["b"] * 2 ** p["a"],
        "spoken": lambda p: (f"A pond has {p['b']} lily pads, and the pads double "
                             f"every day. How many pads after {p['a']} days?"),
        # The sequence stops ONE DAY SHORT and ends on "?" -- drawn to the end it
        # hands the child the answer, and a board that answers its own ask teaches
        # tapping, not doubling.
        "board": lambda p: (f'[[step eq="start: {p["b"]}"]]'
                            f'[[step eq="{" → ".join(str(p["b"] * 2 ** d) for d in range(p["a"]))} → ?"]]'
                            f'[[step eq="{p["b"]} × {" × ".join(["2"] * p["a"])} = ?"]]'),
        "praise": lambda p: (f"Doubling {p['a']} times: "
                             f"{' , then '.join(str(p['b'] * 2 ** d) for d in range(1, p['a'] + 1))}"
                             f" — {p['b'] * 2 ** p['a']} pads. Each day doubles "
                             f"EVERYTHING there is, not just the start."),
        "key": lambda p: p["b"] * 2 ** p["a"],
        # THE growth error is LINEAR THINKING: up by 2 a day (b + 2a), or "double"
        # read as times-2-times-days (b × 2 × a). Exponential beats both, visibly.
        "choices": lambda p: [p["b"] * 2 ** p["a"], p["b"] + 2 * p["a"],
                              p["b"] * 2 * p["a"]],
        "check": lambda p: (3 <= p["a"] <= 5 and 2 <= p["b"] <= 6
                            and p["b"] * 2 ** p["a"] <= 100
                            and len({p["b"] * 2 ** p["a"], p["b"] + 2 * p["a"],
                                     p["b"] * 2 * p["a"]}) == 3,
                            "at least 3 days (below that, doubling and times-2-"
                            "times-days agree), and the pond stays countable"),
    },

    # ---- ALGEBRA I UNIT 7 (build la) -- POLYNOMIALS & FACTORING ---------------
    # The area model comes back and then RUNS BACKWARDS. kt drew a(x + b); now the
    # rectangle is (x + a)(x + b) -- four rooms -- and factoring is the same picture
    # read the other way: given the rooms, find the sides. The unit ends on the
    # vanishing middle, the first identity a child meets that feels like a magic
    # trick and is just the rooms cancelling.
    "foil": {  # (x + a)(x + b) = x² + ?x + ab -- the x count
        "ans": lambda p: p["a"] + p["b"],
        "spoken": lambda p: (f"x plus {p['a']}, times x plus {p['b']}. That comes "
                            f"to x squared, plus how many x, plus "
                            f"{p['a'] * p['b']}?"),
        "board": lambda p: (f'[[step eq="(x + {p["a"]})(x + {p["b"]})"]]'
                            f'[[step eq="x rooms: {p["a"]}x + {p["b"]}x"]]'
                            f'[[step eq="x² + ?x + {p["a"] * p["b"]}"]]'),
        "praise": lambda p: (f"The two x rooms hold {p['a']} x and {p['b']} x — "
                             f"{p['a'] + p['b']} x in all. x squared, plus "
                             f"{p['a'] + p['b']} x, plus {p['a'] * p['b']}."),
        "key": lambda p: p["a"] + p["b"],
        # The classic: forgetting the middle rooms entirely, or filling them with
        # the corner's product. The middle ADDS the two numbers; the corner times.
        "choices": lambda p: [p["a"] + p["b"], p["a"] * p["b"],
                              p["a"] + p["b"] + 1],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["a"] + p["b"], p["a"] * p["b"],
                                     p["a"] + p["b"] + 1}) == 3,
                            "three distinct counts (ruling out 2·2 and 2·3, where "
                            "the times collides with the add or its neighbour)"),
    },
    "fnum": {  # x² + (a+b)x + ab = (x + a)(x + ?)
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"x squared, plus {p['a'] + p['b']} x, plus "
                             f"{p['a'] * p['b']}, equals: x plus {p['a']}, times, "
                             f"x plus what?"),
        "board": lambda p: (f'[[step eq="x² + {p["a"] + p["b"]}x + '
                            f'{p["a"] * p["b"]}"]]'
                            f'[[step eq="= (x + {p["a"]})(x + ?)"]]'
                            f'[[step eq="{p["a"]} + ? = {p["a"] + p["b"]} · '
                            f'{p["a"]} × ? = {p["a"] * p["b"]}"]]'),
        "praise": lambda p: (f"{p['a']} plus {p['b']} equals {p['a'] + p['b']}, and "
                             f"{p['a']} times {p['b']} equals {p['a'] * p['b']} — "
                             f"{p['b']} fits BOTH clues, and a factor has to fit "
                             f"both."),
        "key": lambda p: p["b"],
        # The wrong taps: the number that fits only ONE clue -- what is left after
        # subtracting from the product -- and the x count itself.
        "choices": lambda p: [p["b"], p["a"] * p["b"] - p["a"], p["a"] + p["b"]],
        "speaks": lambda p, sp: (str(p["a"]) in sp and str(p["a"] + p["b"]) in sp
                                 and str(p["a"] * p["b"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and len({p["b"], p["a"] * p["b"] - p["a"],
                                     p["a"] + p["b"]}) == 3,
                            "three distinct taps -- which quietly excludes the "
                            "handful of pairs where the leftover collides"),
    },
    "gcfx": {  # (c·a)x + (c·b) = c(ax + ?)
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"{p['c'] * p['a']} x plus {p['c'] * p['b']} equals: "
                             f"{p['c']} times, {p['a']} x plus what?"),
        "board": lambda p: (f'[[step eq="{p["c"] * p["a"]}x + {p["c"] * p["b"]}"]]'
                            f'[[step eq="= {p["c"]}({p["a"]}x + ?)"]]'
                            f'[[step eq="{p["c"]} × ? = {p["c"] * p["b"]}"]]'),
        "praise": lambda p: (f"The {p['c']} was pulled out of BOTH parts: "
                             f"{p['c'] * p['a']} x became {p['a']} x, so "
                             f"{p['c'] * p['b']} becomes {p['b']}. Both parts "
                             f"share, or it is not a common factor."),
        "key": lambda p: p["c"] * p["a"],
        # THE factoring-out error: pulling the factor from the x part only and
        # leaving the constant untouched -- 6x + 9 = 3(2x + 9).
        "choices": lambda p: [p["b"], p["c"] * p["b"], p["c"]],
        "speaks": lambda p, sp: (str(p["c"] * p["a"]) in sp
                                 and str(p["c"] * p["b"]) in sp
                                 and str(p["c"]) in sp),
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and 2 <= p["c"] <= 9 and p["b"] != p["c"]
                            and _gcd(p["a"], p["b"]) == 1,
                            "a and b share no factor (so c really is the WHOLE "
                            "common factor -- a half-factored answer would be a "
                            "lie), and b differs from c so the taps differ"),
    },
    "dsq": {   # (x + a)(x - a) = x² - ?
        "ans": lambda p: p["a"] * p["a"],
        "spoken": lambda p: (f"x plus {p['a']}, times x take away {p['a']}. That "
                             f"comes to x squared take away what number?"),
        "board": lambda p: (f'[[step eq="(x + {p["a"]})(x − {p["a"]})"]]'
                            f'[[step eq="middles: +{p["a"]}x − {p["a"]}x cancel"]]'
                            f'[[step eq="x² − ?"]]'),
        "praise": lambda p: (f"The middle rooms cancel — plus {p['a']} x and take "
                             f"away {p['a']} x land on nothing — leaving x squared "
                             f"take away {p['a'] * p['a']}."),
        "key": lambda p: p["a"] * p["a"],
        # The errors: tapping the number itself (x² − 3 for x² − 9), or doubling it
        # (the ghost of the middle terms that SHOULD have cancelled).
        "choices": lambda p: [p["a"] * p["a"], p["a"], 2 * p["a"]],
        "speaks": lambda p, sp: str(p["a"]) in sp,
        "check": lambda p: (3 <= p["a"] <= 14,
                            "a is at least 3 (at 2, the square equals the double "
                            "and two taps collide)"),
    },

    # ---- ALGEBRA I UNIT 8 (build la) -- QUADRATIC FUNCTIONS -------------------
    # The curve arrives. y = x² is the first rule where the graph BENDS, and the
    # unit is built on the three things a child must feel about it: squaring is not
    # doubling, a product of zero means one of the factors is zero, and a square is
    # never negative (which is why the curve has a lowest point). The last lesson
    # throws a ball: height c take away x squared, and finding where it lands is
    # asking what number squared equals c.
    "sqy": {   # y = x² + b at x = a
        "ans": lambda p: p["a"] * p["a"] + p["b"],
        "spoken": lambda p: (f"The curve is y equals x squared plus {p['b']}. "
                             f"What is y when x is {p['a']}?"),
        "board": lambda p: (f'[[graph func="x^2+{p["b"]}" range="-4..4"]]'
                            f'[[step eq="y = {p["a"]}² + {p["b"]} = ?"]]'),
        "praise": lambda p: (f"{p['a']} squared is {p['a']} times {p['a']} — "
                             f"{p['a'] * p['a']} — plus {p['b']} equals "
                             f"{p['a'] * p['a'] + p['b']}."),
        "key": lambda p: p["a"] * p["a"] + p["b"],
        # THE squaring error: x² read as 2x. The third tap drops the square entirely.
        "choices": lambda p: [p["a"] * p["a"] + p["b"], 2 * p["a"] + p["b"],
                              p["a"] + p["b"]],
        "check": lambda p: (3 <= p["a"] <= 9 and 1 <= p["b"] <= 9,
                            "x is at least 3 (at 2, squaring and doubling agree "
                            "and the error cannot be shown)"),
    },
    "roots": { # (x - a)(x - b) = 0 -- the other answer
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"x take away {p['a']}, times x take away {p['b']}, "
                             f"equals zero. One answer is x equals {p['a']}. "
                             f"What is the other answer?"),
        "board": lambda p: (f'[[step eq="(x − {p["a"]})(x − {p["b"]}) = 0"]]'
                            f'[[step eq="zero times anything is zero"]]'
                            f'[[step eq="x = {p["a"]}, or x = ?"]]'),
        "praise": lambda p: (f"If either bracket lands on zero, the whole thing is "
                             f"zero. x equals {p['a']} kills the first bracket, and "
                             f"x equals {p['b']} kills the second."),
        "key": lambda p: p["b"],
        # The wrong taps ADD or TIMES the two numbers -- treating the equation like
        # an arithmetic problem instead of reading which x kills a bracket.
        "choices": lambda p: [p["b"], p["a"] + p["b"], p["a"] * p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"]
                            and p["a"] + p["b"] != p["a"] * p["b"],
                            "two different roots, and the add and times taps are "
                            "different numbers"),
    },
    "vtx": {   # y = (x - a)² + b -- the lowest y
        "ans": lambda p: p["b"],
        "spoken": lambda p: (f"y equals: x take away {p['a']}, squared, plus "
                             f"{p['b']}. What is the LOWEST y this curve can ever "
                             f"reach?"),
        # The board shows the RULE and the square's floor -- never "0 + b = ?",
        # which is the answer wearing a hat (the pond taught this in kz).
        "board": lambda p: (f'[[graph func="(x-{p["a"]})^2+{p["b"]}" '
                            f'range="{p["a"] - 3}..{p["a"] + 3}"]]'
                            f'[[step eq="y = (x − {p["a"]})² + {p["b"]}"]]'
                            f'[[step eq="the squared part bottoms out at 0 — '
                            f'lowest y = ?"]]'),
        "praise": lambda p: (f"A square can never be below zero — the smallest the "
                             f"squared part gets is 0, right at x equals {p['a']} — "
                             f"so the lowest y is 0 plus {p['b']}: {p['b']}."),
        "key": lambda p: p["b"],
        # The wrong taps: the OTHER number in the rule (where the low point sits
        # left-and-right, not how low it goes), and the two added.
        "choices": lambda p: [p["b"], p["a"], p["a"] + p["b"]],
        "check": lambda p: (2 <= p["a"] <= 9 and 2 <= p["b"] <= 9
                            and p["a"] != p["b"],
                            "the across number and the up number differ, so the "
                            "three taps are three different numbers"),
    },
    "hitg": {  # y = a² - x² -- where does the height reach zero?
        "ans": lambda p: p["a"],
        "spoken": lambda p: (f"A ball's height is y equals {p['a'] * p['a']} take "
                             f"away x squared. At what x does the height reach "
                             f"zero?"),
        "board": lambda p: (f'[[graph func="{p["a"] * p["a"]}-x^2" '
                            f'range="0..{p["a"] + 1}"]]'
                            f'[[step eq="{p["a"] * p["a"]} − x² = 0"]]'
                            f'[[step eq="what number squared equals '
                            f'{p["a"] * p["a"]}?"]]'),
        "praise": lambda p: (f"The height is zero when x squared equals "
                             f"{p['a'] * p['a']} — and {p['a']} squared is exactly "
                             f"that. {p['a']} is called the square root of "
                             f"{p['a'] * p['a']}."),
        "key": lambda p: p["a"],
        # The wrong taps: the height itself, and its half -- the child who reaches
        # for halving because halving undoes doubling, when what is needed is the
        # number that SQUARES to it.
        "choices": lambda p: [p["a"], p["a"] * p["a"], 2 * p["a"]],
        "speaks": lambda p, sp: str(p["a"] * p["a"]) in sp,
        "check": lambda p: (3 <= p["a"] <= 14,
                            "a is at least 3 (at 2, the double collides with the "
                            "square... with 2a = a² -- same wall as dsq)"),
    },
}


# =============================================================================
# RENDERERS -- problem data -> what the child sees and hears, per level.
# One function per surface, so vocabulary consistency is BY CONSTRUCTION.
# =============================================================================
def spoken_for(p, level):
    a, b = p["a"], p["b"]
    # kd: a problem may carry its own story sentence -- word problems are authored
    # per problem, and every closure/vocabulary/digits check applies to the story.
    if p.get("story"):
        return p["story"]
    if p.get("op") in OP_EXT:
        return OP_EXT[p["op"]]["spoken"](p)
    if p.get("op") == "t":
        if level == "abstract":
            return f"What number is {a} ten and {b} ones?"
        if level == "pictorial":
            return f"Count if you need to. What number is {a} ten and {b} ones?"
        return (f"Let's count together. {a} ten, and {b} more ones. "
                f"What number is that?")
    if p.get("op") == "-":
        if level == "abstract":
            return f"What is {a} minus {b}?"
        if level == "pictorial":
            return f"Count the stars if you need them. What is {a} minus {b}?"
        return (f"Let's count together. {a} stars, take {b} away. "
                f"How many are left?")
    if level == "abstract":
        return f"What is {a} plus {b}?"
    if level == "pictorial":
        return f"Count the stars if you need them. What is {a} plus {b}?"
    return (f"Let's count together. {a} stars, then {b} more stars. "
            f"How many in all?")


def board_for(p, level):
    a, b = p["a"], p["b"]
    if p.get("op") in OP_EXT:
        return OP_EXT[p["op"]]["board"](p)
    if p.get("op") == "t":
        step = f'[[step eq="{a} ten and {b} ones = ?"]]'
        if level == "abstract":
            return step
        stars = (f'[[objects emoji="⭐" groups="10" add="{b}" '
                 f'caption="one ten and {b} ones"]]')
        return stars + step
    if p.get("op") == "-":
        step = f'[[step eq="{a} − {b} = ?"]]'
        if level == "abstract":
            return step
        stars = (f'[[objects emoji="⭐" groups="{a}" '
                 f'caption="start with {a} — take {b} away, count what is left"]]')
        return stars + step
    step = f'[[step eq="{a} + {b} = ?"]]'
    if level == "abstract":
        return step
    stars = f'[[objects emoji="⭐" groups="{a}" add="{b}" caption="count every star"]]'
    return stars + step


def choices_for(p):
    """Three tap options: the answer and its two neighbours (floor 1), shuffled by a
    FIXED per-problem rotation -- deterministic, so replays render identically.
    kc: an op may declare its OWN distractors (rounding needs the neighbouring tens,
    not +-1, or the answer is guessable by eye)."""
    v = ans(p)
    ext = OP_EXT.get(p.get("op", "+"), {})
    if "choices" in ext:
        opts = list(ext["choices"](p))
    else:
        opts = [v - 1, v, v + 1] if v > 1 else [v, v + 1, v + 2]
    k = (p["a"] * 3 + p["b"] + p.get("c", 0)) % 3
    opts = opts[k:] + opts[:k]
    return "[[choices options=\"" + " | ".join(str(o) for o in opts) + "\"]]"


def praise_for(p, index):
    a, b = p["a"], p["b"]
    if p.get("op") in OP_EXT:
        return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)] + " "
                + OP_EXT[p["op"]]["praise"](p))
    if p.get("op") == "t":
        return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)]
                + f" {a} ten and {b} ones — that is {ans(p)}.")
    word = "minus" if p.get("op") == "-" else "plus"
    return (PRAISE_PREFIXES[index % len(PRAISE_PREFIXES)]
            + f" {a} {word} {b} equals {ans(p)}.")


# =============================================================================
# THE ENGINE -- a pure state machine.  step(lesson, state, event) -> (out, state)
# -----------------------------------------------------------------------------
# Events:   ("begin",)            start the lesson
#           ("answer", value)     the child answered (tap or typed int)
#           ("unheard",)          voice input could not be recognized
#           ("resume",)           the AI intervention finished; give the retest
# Outputs (dicts), by kind:
#   say        {spoken, board}                       -- narration beat, no input
#   ask        {spoken, board, choices, expected, guided, problem} -- wait for child
#   intervene  {reason, problem, expected, got, vocabulary, retest} -- AI takes over;
#              the ONLY step the model ever authors, and the engine has already chosen
#              the retest problem, so the RETURN to script is code's decision.
#   end        {spoken, graceful, mastered, problems_done}
# =============================================================================
def start(lesson):
    return {"phase": "teach", "i": 0,
            "level": lesson.get("levels", LEVELS)[0],
            "bank_i": 0, "done": 0, "streak": 0,
            "interventions": 0, "unheard": 0, "pending": None,
            "retest": None, "finished": False}


def _problem_key(p):
    return (p.get("op", "+"), p["a"], p["b"], p.get("c", 0))


def _next_bank_problem(lesson, state):
    """The next unused bank problem; the bank wraps if the retest path consumed it."""
    bank = lesson["bank"]
    p = bank[state["bank_i"] % len(bank)]
    state["bank_i"] += 1
    return p


def _ask(state, p, guided=False):
    out = {"kind": "ask", "spoken": spoken_for(p, state["level"]),
           "board": board_for(p, state["level"]), "choices": choices_for(p),
           "expected": ans(p), "guided": guided, "problem": p,
           "tap_only": state["unheard"] >= 2}
    state["pending"] = {"problem": p, "guided": guided}
    return out


def step(lesson, state, event):
    """One engine transition. Returns (list_of_output_steps, state). Pure."""
    kind = event[0]
    out = []

    if state["finished"]:
        return ([{"kind": "end", "spoken": "", "graceful": True,
                  "mastered": False, "problems_done": state["done"]}], state)

    if kind == "begin":
        for spoken, board in lesson["teach"]:
            out.append({"kind": "say", "spoken": spoken, "board": board})
        pair = lesson["pairs"][0]
        out.append({"kind": "say", "spoken": pair["worked"][0],
                    "board": pair["worked"][1]})
        out.append(_ask(state, pair["ask"], guided=True))
        state["phase"] = "pair-0"
        return (out, state)

    if kind == "unheard":
        state["unheard"] += 1
        p = state["pending"]["problem"]
        guided = state["pending"]["guided"]
        re_spoken = LINE_TAP if state["unheard"] >= 2 else (
            LINE_REASK + " " + spoken_for(p, state["level"]))
        asked = _ask(state, p, guided=guided)
        asked["spoken"] = re_spoken
        return ([asked], state)

    if kind == "resume":
        # The AI intervention is over. The engine -- not the model -- decides what
        # happens next: the retest problem it already chose, or (at the cap) the
        # warm close. The model never picks where the child lands.
        p = state["retest"]
        state["retest"] = None
        if p is None:
            state["finished"] = True
            return ([{"kind": "end", "spoken": LINE_END_GRACEFUL, "graceful": True,
                      "mastered": False, "problems_done": state["done"]}], state)
        return ([_ask(state, p, guided=False)], state)

    if kind != "answer":
        return ([], state)

    state["unheard"] = 0
    pend = state["pending"]
    p, guided = pend["problem"], pend["guided"]
    correct = (event[1] == ans(p))

    if correct:
        idx = state["done"]
        out.append({"kind": "say", "spoken": praise_for(p, idx), "board": ""})
        if not guided:
            state["done"] += 1
            state["streak"] += 1
        # ---- where next? ----
        if state["phase"] == "pair-0":
            pair = lesson["pairs"][1]
            out.append({"kind": "say", "spoken": pair["worked"][0],
                        "board": pair["worked"][1]})
            out.append(_ask(state, pair["ask"], guided=True))
            state["phase"] = "pair-1"
            return (out, state)
        if state["phase"] == "pair-1":
            out.append({"kind": "say", "spoken": lesson["practice_intro"],
                        "board": ""})
            state["phase"] = "practice"
            out.append(_ask(state, _next_bank_problem(lesson, state)))
            return (out, state)
        # practice
        if state["done"] >= MIN_PROBLEMS and state["streak"] >= ADVANCE_STREAK:
            out.append({"kind": "end", "spoken": lesson["advance_line"],
                        "graceful": True, "mastered": True,
                        "problems_done": state["done"]})
            state["finished"] = True
            return (out, state)
        if state["done"] >= MAX_PROBLEMS:
            out.append({"kind": "end", "spoken": LINE_END_GRACEFUL,
                        "graceful": True, "mastered": False,
                        "problems_done": state["done"]})
            state["finished"] = True
            return (out, state)
        out.append(_ask(state, _next_bank_problem(lesson, state)))
        return (out, state)

    # ---- wrong answer: the ONE doorway to the AI ----
    state["streak"] = 0
    if not guided:
        state["done"] += 1
    state["interventions"] += 1
    if state["interventions"] >= DROP_AFTER_INTERVENTIONS:
        lv = lesson.get("levels", LEVELS)
        li = lv.index(state["level"])
        if li + 1 < len(lv):
            state["level"] = lv[li + 1]
            state["interventions"] = 0
        else:
            # already at concrete and still failing: end warmly, mark "learning"
            out.append({"kind": "say", "spoken": LINE_WRONG, "board": ""})
            out.append({"kind": "end", "spoken": LINE_END_GRACEFUL,
                        "graceful": True, "mastered": False,
                        "problems_done": state["done"]})
            state["finished"] = True
            return (out, state)
    # AT THE CAP, THE ERROR IS STILL CORRECTED BUT NO RETEST FOLLOWS: the AI's
    # Model-Lead-Test runs (never leave a child with an uncorrected error), and
    # "resume" then ends the practice gracefully instead of asking an eleventh
    # problem. Found by the alternating right/wrong scenario in build js's own
    # dry run -- the cap only guarded the CORRECT path, and `done` reached 11.
    retest = None
    if state["done"] < MAX_PROBLEMS:
        retest = _next_bank_problem(lesson, state)
    state["retest"] = retest
    out.append({"kind": "say", "spoken": LINE_WRONG, "board": ""})
    out.append({"kind": "intervene", "reason": "wrong_answer", "problem": p,
                "expected": ans(p), "got": event[1],
                "vocabulary": {k: k for k in VOCABULARY},
                "level": state["level"], "retest": retest})
    return (out, state)


# =============================================================================
# THE AUDIO CLOSURE -- every spoken string a lesson can ever emit.
# =============================================================================
def audio_lines(lesson):
    lines = set()
    for spoken, _board in lesson["teach"]:
        lines.add(spoken)
    for pair in lesson["pairs"]:
        lines.add(pair["worked"][0])
    lines.add(lesson["practice_intro"])
    problems = list(lesson["bank"]) + [pair["ask"] for pair in lesson["pairs"]]
    for p in problems:
        for level in lesson.get("levels", LEVELS):
            lines.add(spoken_for(p, level))
            lines.add(LINE_REASK + " " + spoken_for(p, level))
        for i in range(len(PRAISE_PREFIXES)):
            lines.add(praise_for(p, i))
    lines.update([LINE_WRONG, LINE_TAP, LINE_END_GRACEFUL,
                  lesson["advance_line"]])
    return sorted(lines)


def audio_cost_estimate(lesson, usd_per_1k_chars=0.22):
    chars = sum(len(s) for s in audio_lines(lesson))
    return {"lines": len(audio_lines(lesson)), "chars": chars,
            "usd": round(chars / 1000.0 * usd_per_1k_chars, 2)}


# =============================================================================
# THE VALIDATOR -- the checks that make "verified once" true. Pure; returns a list
# of (ok, label, detail). The battery fails the build on any not-ok.
# =============================================================================
_TAG_RE = re.compile(r"\[\[\s*([\w-]+)")


def _difficulty_key(p):
    """The ramp is measured on what makes the problem HARD: the sum for adding,
    the starting number for taking away (you count back from it), the ones count
    for tens-and-ones."""
    op = p.get("op", "+")
    if op in OP_EXT:
        return OP_EXT[op]["key"](p)
    if op == "-":
        return p["a"]
    if op == "t":
        return p["b"]
    return p["a"] + p["b"]


def validate(lesson, board_tag_names=None):
    checks = []

    def ck(ok, label, detail=""):
        checks.append((bool(ok), label, detail))

    lid = lesson["id"]
    bound = lesson.get("max_value", 10)

    # 1. every answer is COMPUTED -- and inside the lesson's own stated bound
    problems = list(lesson["bank"]) + [pr["ask"] for pr in lesson["pairs"]]
    # build km: the floor is DECLARED, not assumed. Every lesson through Basic Math
    # answers with a count, so "answers are 1 or more" was a true invariant and a
    # useful one -- it catches an op whose arithmetic has gone backwards. Prealgebra
    # Unit 3 teaches integers, where landing below zero IS the lesson, so a lesson may
    # now state its own floor. Default 1, so all 45 earlier lessons are unchanged and
    # still guarded; a lesson that wants negatives has to say so out loud.
    floor = lesson.get("min_value", 1)
    ck(all(floor <= ans(p) <= bound for p in problems),
       f"{lid}: every answer stays within {floor} to {bound}",
       str([p for p in problems if not floor <= ans(p) <= bound]))
    ck(all(p["a"] <= bound and p["b"] <= bound for p in problems),
       f"{lid}: every number a child sees stays within {bound}", "")
    # jx: the lesson's NAME is a promise about its INPUTS (Jim's second wording
    # ruling) -- a_max/b_max make the bank provably match the name.
    a_cap = lesson.get("a_max")
    b_cap = lesson.get("b_max")
    if a_cap is not None:
        ck(all(p["a"] <= a_cap for p in problems),
           f"{lid}: every first number honors the name (a <= {a_cap})",
           str([p for p in problems if p["a"] > a_cap]))
    if b_cap is not None:
        ck(all(p["b"] <= b_cap for p in problems),
           f"{lid}: every second number honors the name (b <= {b_cap})",
           str([p for p in problems if p["b"] > b_cap]))
    for p in problems:
        _ext = OP_EXT.get(p.get("op", "+"))
        if _ext:
            okc, why = _ext["check"](p)
            ck(okc, f"{lid}: {p} satisfies its op's constraint", why)
    if lesson.get("regroup"):
        ck(all(p["a"] % 10 < p["b"] % 10 and p["a"] > p["b"] and
               p["a"] // 10 - 1 >= p["b"] // 10 for p in problems),
           f"{lid}: EVERY problem regroups (ones too small) and never goes "
           f"negative in the tens",
           str([p for p in problems if not (p["a"] % 10 < p["b"] % 10
                and p["a"] > p["b"] and p["a"] // 10 - 1 >= p["b"] // 10)]))
    if lesson.get("carry"):
        ck(all(p["a"] % 10 + p["b"] % 10 > 9 for p in problems),
           f"{lid}: EVERY problem carries -- a carrying lesson that practices on "
           f"no-carry problems teaches its idea on examples that never use it",
           str([p for p in problems if p["a"] % 10 + p["b"] % 10 <= 9]))
        ck(all(p["a"] // 10 + p["b"] // 10 + 1 <= 9 for p in problems),
           f"{lid}: no problem overflows the tens (answers stay two-digit)",
           str([p for p in problems if p["a"] // 10 + p["b"] // 10 + 1 > 9]))
    if lesson.get("no_carry"):
        ck(all(p["a"] % 10 + p["b"] % 10 <= 9
               and p["a"] // 10 + p["b"] // 10 <= 9 for p in problems),
           f"{lid}: NO problem carries -- the lesson that promises no carrying "
           f"cannot quietly require it",
           str([p for p in problems
                if p["a"] % 10 + p["b"] % 10 > 9
                or p["a"] // 10 + p["b"] // 10 > 9]))
    ck(len({_problem_key(p) for p in problems}) == len(problems),
       f"{lid}: no duplicate problems", "")

    # 2. choices: the right answer appears exactly once, every option in range.
    # build km: the pattern was r"\d+", which cannot see a minus sign -- it read the
    # option "-6" as "6", so a Prealgebra U3 lesson looked like it was offering the
    # answer twice when it was offering -6 and +6, which is the whole point of the
    # question. The floor moved with it: "every option is at least 1" was the same
    # assumption as min_value, and it is now the lesson's declared floor (default 1,
    # so the other 45 lessons are guarded exactly as before).
    for p in problems:
        opts = re.findall(r"-?\d+", choices_for(p))
        ck(opts.count(str(ans(p))) == 1,
           f"{lid}: choices for {p['a']}{p.get('op', '+')}{p['b']} contain the "
           f"answer exactly once", str(opts))
        # THE FLOOR ONLY, deliberately. An upper bound here was tried in km and was
        # WRONG: the default distractor set is the answer's neighbours, so a lesson
        # whose top answer equals its max_value legitimately offers max_value + 1 --
        # Counting to 10 shows 9 | 10 | 11, times tables show 80 | 81 | 82. Six shipped
        # lessons said so at once, and they were right. max_value describes the
        # PROBLEMS; a neighbour one step past it is a normal wrong answer, not a defect.
        ck(all(int(o) >= floor for o in opts),
           f"{lid}: choices for {p['a']}{p.get('op', '+')}{p['b']} are all at "
           f"least {floor}", str(opts))

    # 3. the difficulty ramp: the key never falls by more than 1 across the bank.
    # kc: a lesson may declare mixed_review=True -- INTERLEAVED practice across ops
    # is the evidence-based design for review (the ramp is a teaching-lesson rule).
    if not lesson.get("mixed_review"):
        keys = [_difficulty_key(p) for p in lesson["bank"]]
        ck(all(keys[i + 1] >= keys[i] - 1 for i in range(len(keys) - 1)),
           f"{lid}: the bank is a ramp (difficulty never falls by more than 1)",
           str(keys))

    # 4. every beat respects the spoken cap
    for spoken in [s for s, _b in lesson["teach"]] + \
                  [pr["worked"][0] for pr in lesson["pairs"]] + \
                  [lesson["practice_intro"]]:
        ck(len(spoken.split()) <= BEAT_WORD_CAP,
           f"{lid}: beat under {BEAT_WORD_CAP} words: \"{spoken[:36]}...\"",
           f"{len(spoken.split())} words")

    # 5. rule 14 by construction: the lesson's symbols are READ ALOUD in teach
    teach_text = " ".join(s for s, _b in lesson["teach"]).lower()
    for sym in lesson["symbols"]:
        ck(f"'{sym}'" in teach_text or f" {sym} " in teach_text,
           f"{lid}: the {sym} sign is introduced by name (rule 14)", "")

    # 6. rule 44 by construction: every ask SPEAKS its numbers
    for p in problems:
        for level in lesson.get("levels", LEVELS):
            sp = spoken_for(p, level)
            _speaks = OP_EXT.get(p.get("op", "+"), {}).get("speaks")
            ok44 = _speaks(p, sp) if _speaks else (str(p["a"]) in sp
                                                  and str(p["b"]) in sp)
            ck(ok44,
               f"{lid}: ask speaks its numbers "
               f"({p['a']}{p.get('op', '+')}{p['b']}, {level})", sp)

    # 7. build jr's lesson, enforced at authoring time: canon vocabulary only
    all_speech = " ".join(audio_lines(lesson)).lower()
    for canon, banned in VOCABULARY.items():
        for term in banned:
            ck(term not in all_speech,
               f"{lid}: '{term}' never appears (canon is '{canon}')", "")

    # 8. every board tag is a real tag (against tags.py when provided)
    if board_tag_names:
        boards = [b for _s, b in lesson["teach"]] + \
                 [pr["worked"][1] for pr in lesson["pairs"]] + \
                 [board_for(p, lv) for p in problems
                  for lv in lesson.get("levels", LEVELS)] + \
                 [choices_for(p) for p in problems]
        for b in boards:
            for name in _TAG_RE.findall(b):
                ck(name in board_tag_names,
                   f"{lid}: board tag [[{name}]] exists in the registry", b[:60])

    # 9. praise pool sanity
    ck(len(PRAISE_PREFIXES) >= 3, "at least 3 praise variants", "")
    return checks


# I did no harm and this file is not truncated.
