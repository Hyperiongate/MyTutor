# =============================================================================
# misconceptions.py  --  WHY THE ANSWER WAS WRONG  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-10  NEW FILE (build ck, Jim: "I want to pursue the misconception box").
#               Proactive audit #2, item 2 -- the highest-leverage teaching item left.
#
#               WHAT WAS MISSING. Rules 20-22 tell the tutor what to DO about a wrong
#               answer: credit the correct part, change the representation, never re-ask
#               the same way twice. Nothing told him to work out WHY it was wrong. So a
#               student who says 3 + 2 x 4 = 20 and a student who says 21 got the same
#               response, when they need opposite things: the first is running
#               left-to-right evaluation and needs THAT rule fixed; the second made a
#               slip. Re-explaining the whole topic to the first one wastes the lesson
#               and leaves the broken rule intact, so it fires again next week.
#
#               WHAT THIS IS. 148 catalogued wrong RULES -- not mistakes, RULES: the
#               systematic, repeatable procedures students actually run. Each entry
#               names the broken rule, the giveaway answer it produces, why an
#               intelligent child lands there (it is nearly always over-generalising
#               something they were taught correctly), the concrete move that dislodges
#               it, and words the tutor can say almost verbatim. Grounded in the error-
#               pattern literature: Ashlock's buggy algorithms, the whole-number bias
#               work on fractions, Kuchemann and MacGregor on letter-as-object, van
#               Hiele levels for geometry, Tall and Vinner on limits, and Kahneman and
#               Tversky on base rates and the gambler's fallacy.
#
#               TWO WAYS IT REACHES A LESSON.
#                 1. tutor.py appends this course's catalogue to every prompt, so rule
#                    49 ("diagnose the rule, then fix THAT") is followable.
#                 2. main.py runs `match()` over what the student just said. A hit adds
#                    a note NAMING the likely misconception. The note is always framed
#                    as a possibility the tutor may ignore -- a matcher that overrode
#                    his judgement would be worse than no matcher.
#
#               THE `detect` STRINGS ARE EVIDENCE, NOT ANSWERS. Any string that could
#               plausibly appear in a CORRECT answer was stripped at build time: 68 bare
#               numbers went, because "seven" is not evidence of anything. Two entries
#               ended up with no usable tell and are prompt-only, which is the honest
#               outcome -- a wrong match is far more damaging than a missed one.
# -----------------------------------------------------------------------------
# ADDING ONE
#   Append to the course's list. `say` is spoken aloud, so it carries no symbols
#   (see tutor.py "HOW YOU SPEAK") and must not open by telling the student they are
#   wrong -- lead with what they got right, or with a check they can run themselves.
#   ruletests.py PART 3g enforces all of that.
# =============================================================================

import re

# course id -> the wrong rules students actually run in it.
#   id      : stable slug
#   name    : how a teacher would name the error
#   topic   : the curriculum topic where it bites
#   tell    : a concrete problem and the exact wrong answer it produces
#   detect  : distinctive strings that suggest the student is running this rule
#   rule    : the broken rule itself -- the heart of the entry
#   why     : why an intelligent student lands there
#   fix     : the concrete move that dislodges it
#   say     : words the tutor can use almost verbatim
MISCONCEPTIONS = {
    "entrymath": [
        {"id": "decade-back-drops-a-ten", "name": "one less takes away a whole ten",
         "topic": "One more & one less",
         "tell": "one less than 70 answered as 60",
         "detect": [],
         "rule": "When the ones digit is 0, they take one away from the TENS digit instead of counting"
                 " back across the decade, so one less than 70 becomes 60 and one less than 40 becomes"
                 " 30.",
         "why": "Every 'one less' they have practised had a ones digit to shrink. With a 0 in the ones"
                " place there is nothing there to take one from, so the only digit left to change is the"
                " tens digit.",
         "fix": "Put them on a hundred chart or a number line and have them physically step backwards"
                " one square from 70. They land on 69, not 60. Then do 69, 68, 67 so they feel that the"
                " count goes back through the whole row before the tens digit is allowed to change."
                " Repeat at 40 and 30.",
         "say": "Good instinct that the tens digit has to move eventually. Put your finger on seventy"
                " on the chart and take exactly one step backwards. Where did you land? That is the"
                " number just before seventy. The tens digit only changes after you walk back through"
                " every number in the row.",
        },
        {"id": "compare-by-ones-digit", "name": "comparing using only the ones digit",
         "topic": "Comparing numbers",
         "tell": "asked which is bigger, 19 or 21, answers 19",
         "detect": ["19 is bigger", "nineteen is bigger", "19 is more"],
         "rule": "They compare two-digit numbers by looking only at the ones digits, so 19 beats 21"
                 " because 9 beats 1. The tens digit is treated as decoration rather than as the digit"
                 " that decides.",
         "why": "For a whole year the only numbers they compared were single digits, and the ones digit"
                " is the one they know best. Nobody has yet told them that the digits are not equal"
                " partners.",
         "fix": "Build both numbers in ten-sticks and loose cubes. Nineteen is one stick and nine"
                " loose; twenty-one is two sticks and one loose. Line them up side by side and let them"
                " see that the second pile is taller even though its loose cubes are fewer. Then state"
                " the rule: check the tens first, and only look at the ones when the tens are the same.",
         "say": "You read those ones digits exactly right, nine really is more than one. Now build both"
                " numbers with ten sticks and loose cubes and stand them next to each other. Which pile"
                " is taller? The tens get checked first, and the ones only settle a tie.",
        },
        {"id": "count-on-from-first", "name": "counting the first number again",
         "topic": "Counting on",
         "tell": "8 + 3 answered as 10",
         "detect": [],
         "rule": "When counting on they say the first number as the first count, so 8 + 3 comes out as"
                 " 8, 9, 10 and the answer is always exactly one less than it should be.",
         "why": "Counting objects taught them that the first thing you point at gets the word 'one'."
                " Counting on asks them to start the count at the next number instead, which contradicts"
                " the habit that made them successful.",
         "fix": "Give them 8 counters in a covered cup and 3 loose. Tap the cup and say 'eight is"
                " already in here' — the cup is not counted, it is where you START. Then count the loose"
                " ones on top: nine, ten, eleven. Have them raise three fingers and count those fingers,"
                " not the cup.",
         "say": "Your counting was perfectly steady, and you stopped after exactly three words. Here is"
                " the one thing to move. The eight is already inside the cup, so eight is where you"
                " start, not something you count. Tap the cup, then count the three loose ones on top.",
        },
        {"id": "make-ten-double-counts", "name": "making a ten then adding it all again",
         "topic": "Make-a-ten",
         "tell": "8 + 5 answered as 15",
         "detect": [],
         "rule": "They break 8 up to 10 by borrowing 2 from the 5, then add the whole original 5 to the"
                 " ten anyway, so the 2 they already used gets counted a second time.",
         "why": "The make-a-ten move has two halves and only the first half is exciting. Getting to a"
                " round ten feels like the work is done, and the leftover 3 looks like an accident"
                " rather than the point.",
         "fix": "Use a ten-frame. Put 8 counters in and hold 5 in their hand. Slide counters in one at"
                " a time and count out loud how many actually leave the hand: two go in to fill the"
                " frame, so only three are still in the hand. Say it as a sentence: eight and two makes"
                " ten, and three are left.",
         "say": "Filling the frame to ten was smart, that is exactly the move. Now look at your hand."
                " You had five counters, and two of them went in to finish the ten. How many are still"
                " sitting in your hand? Those are the ones that go on top of the ten.",
        },
        {"id": "missing-addend-adds-both", "name": "adding the two numbers you can see",
         "topic": "Missing addends",
         "tell": "5 + __ = 12 answered as 17",
         "detect": [],
         "rule": "They see two numbers and a plus sign and add them, ignoring the fact that one of those"
                 " numbers is the TOTAL and the blank is a part.",
         "why": "In every problem so far the two numbers were both parts and the answer went in the"
                " blank. The plus sign has come to mean 'add the numbers on this page', not 'these two"
                " parts join to make that total'.",
         "fix": "Draw a part-part-whole bar: one long bar labelled 12 on top, split underneath into a 5"
                " and an empty box. Point at 12 and ask whether the answer can be bigger than the whole"
                " bar. Then have them count up from 5 to 12 on their fingers to fill the box.",
         "say": "You added carefully and got those two numbers right. Look at the twelve for a second."
                " Twelve is the whole bar, and the box is only a piece of it. Can a piece be bigger than"
                " the whole bar? Count up from five until you reach twelve, and count how many steps"
                " that took.",
        },
        {"id": "equals-means-answer-next", "name": "the equals sign means answer goes here",
         "topic": "Fact families",
         "tell": "4 + 3 = __ + 2 answered as 7",
         "detect": [],
         "rule": "They read the equals sign as an instruction meaning 'write the total now', so they add"
                 " whatever is on the left and stop, never noticing the plus 2 sitting on the right.",
         "why": "Every problem they have ever seen had the equals sign followed by an empty space, so"
                " equals has been taught by accident to mean 'and the answer is' rather than 'the same"
                " amount as'.",
         "fix": "Use a balance scale or two piles of counters. Build 4 and 3 on the left, and 2 on the"
                " right, and ask what has to go with the 2 to make the sides balance. Rename the equals"
                " sign out loud as 'is the same amount as' every single time you read a problem for a"
                " week.",
         "say": "Four and three really is seven, that part is solid. Now read the sign in the middle as"
                " the words is the same amount as. The left side holds seven. The right side already has"
                " two on it. What has to join the two so both sides hold the same amount?",
        },
        {"id": "write-number-as-you-say-it", "name": "writing the number the way it sounds",
         "topic": "Reading & writing numbers",
         "tell": "three hundred five written as 3005",
         "detect": [],
         "rule": "They write each spoken chunk as its own numeral and stick the chunks together, so"
                 " 'three hundred' becomes 300 and 'five' becomes 5, written side by side as 3005.",
         "why": "This is a completely logical transcription of what they hear, and it even works for"
                " numbers like fifty-six. Nobody has told them that a zero has a job, which is holding"
                " an empty column open.",
         "fix": "Draw three labelled boxes: hundreds, tens, ones. Fill in 3 and 5 where they belong and"
                " ask what to write in the tens box when there are no tens. Leaving it blank slides the"
                " 5 over, so a 0 has to stand in that box as a placeholder. Then have them read 3005"
                " back and hear that it says three thousand five.",
         "say": "You heard the number exactly right, three hundred and then five. Read back what you"
                " wrote though. That one says three thousand five. Draw hundreds, tens and ones boxes."
                " The five goes in ones, the three in hundreds, and something has to hold the tens box"
                " open.",
        },
        {"id": "drops-the-carried-ten", "name": "writing the ones and dropping the ten",
         "topic": "Carrying (regrouping)",
         "tell": "27 + 15 answered as 32",
         "detect": [],
         "rule": "They add each column and write only the last digit of each column's answer, so the ten"
                 " that 7 + 5 makes is simply thrown away rather than carried into the tens column.",
         "why": "The rule they were given is 'one digit per column', and it is a real rule. The carry"
                " is an extra step that has nothing to do with the column they are looking at, so it"
                " feels like it belongs to nobody.",
         "fix": "Estimate first: 27 and 15 are close to 30 and 15, so the answer must be over 40, and"
                " 32 is too small. Then build it with ten-sticks and cubes. Twelve loose cubes will not"
                " fit in the ones column, so bundle ten of them into a stick and physically move that"
                " stick over.",
         "say": "Both of your columns were added correctly, so your facts are solid. Check the size"
                " first though. Twenty seven is nearly thirty, and you added fifteen more. Should the"
                " answer be in the thirties? Those twelve loose cubes will not fit in one column, so"
                " bundle ten and move them.",
        },
        {"id": "smaller-from-larger", "name": "always take the smaller from the larger",
         "topic": "Borrowing (regrouping)",
         "tell": "52 - 27 answered as 35",
         "detect": [],
         "rule": "In each column they subtract the smaller digit from the larger one no matter which is"
                 " on top, so 2 minus 7 is done as 7 minus 2 and borrowing never has to happen.",
         "why": "They were taught, truthfully, that you cannot take 7 from 2. So when a column looks"
                " impossible they flip it, which keeps the algorithm running. It is a repair, not"
                " carelessness.",
         "fix": "Check by adding back: 35 plus 27 is 62, not 52, so the answer is too big. Then build"
                " 52 as five ten-sticks and two cubes and try to hand over 27. There are not enough"
                " loose cubes, so break one stick into ten cubes first. Twelve cubes minus seven is what"
                " the ones column really says.",
         "say": "Your subtracting inside each column was accurate. Let us check it the way a cashier"
                " would. Add your answer back to twenty seven and see whether you get fifty two. Then"
                " build fifty two out of sticks and try to hand me seven single cubes. You will need to"
                " break a stick first.",
        },
        {"id": "bigger-coin-more-value", "name": "the bigger coin is worth more",
         "topic": "Coin & bill values",
         "tell": "asked whether a nickel or a dime is worth more, says the nickel",
         "detect": ["nickel is worth more", "nickel is bigger", "the nickel"],
         "rule": "They rank coins by physical size, so a nickel beats a dime and a quarter beats a"
                 " dollar bill, because in every other part of life a bigger object means a bigger"
                 " amount.",
         "why": "Size has been a reliable guide to quantity their whole life: the bigger cup holds more"
                " juice. Coin value is a pure convention that actually contradicts the evidence in their"
                " hand.",
         "fix": "Trade physically. Put out ten pennies and let them swap the pile for one dime, then"
                " swap five pennies for one nickel. Line up the penny piles under each coin so the value"
                " is visible as a length rather than as a fact to memorise. Leave those labelled piles"
                " on the table.",
         "say": "You are right that the nickel is the bigger piece of metal, that is a fair thing to"
                " notice. Coins are strange this way. Count out how many pennies I will trade you for"
                " each one. The dime buys a taller stack of pennies, and the stack is what tells you the"
                " value.",
        },
        {"id": "minute-hand-read-literally", "name": "reading the minute hand as its number",
         "topic": "Minutes by 5s",
         "tell": "a clock with hands on 3 and 9 read as three oh nine",
         "detect": ["three oh nine"],
         "rule": "They read whichever number the minute hand points at as the number of minutes, so a"
                 " hand on the 9 means 9 minutes instead of 45.",
         "why": "One hand pointing at a 3 does mean 3 o'clock, so applying the same reading to the"
                " other hand is consistent, not careless. The clock face carries two different scales"
                " printed on top of each other.",
         "fix": "Write the minute numbers 5, 10, 15 and so on in a second ring outside the printed"
                " numbers, or lay a paper ring over the clock. Then have them skip-count by fives around"
                " to the 9 while touching each number: five, ten, fifteen, all the way to forty five.",
         "say": "You spotted both hands and read the hour perfectly. The clock plays a trick, though."
                " The numbers around the edge are for the little hand. For the big hand, skip count by"
                " fives and touch each number as you go. How many do you reach when you get to the nine?",
        },
        {"id": "tilted-square-is-a-diamond", "name": "a tilted square stops being a square",
         "topic": "2-D shapes & their parts",
         "tell": "a square rotated onto its corner is called a diamond, not a square",
         "detect": ["diamond", "not a square", "rhombus"],
         "rule": "They treat orientation as part of a shape's definition, so a shape only counts as a"
                 " square when it sits flat on a side, and a triangle only counts when it has a"
                 " horizontal bottom.",
         "why": "Every square in every book they have seen sits flat. With that many examples all"
                " sharing a feature, deciding the feature is part of the definition is genuinely good"
                " reasoning from the evidence they have.",
         "fix": "Cut a square out of card, name it together, then slowly turn it in their hands and ask"
                " at what moment it stopped being a square. Nothing was cut or added, so nothing"
                " changed. Then check the definition with their fingers: four straight sides the same"
                " length, four square corners.",
         "say": "Diamond is exactly what that looks like, and lots of people call it that. Watch my"
                " hands. I am turning the card, not cutting it. Tell me the moment it stopped being a"
                " square. Now check with your fingers, four equal sides and four square corners. Still"
                " true?",
        },
    ],
    "basicmath": [
        {"id": "borrow-across-zero", "name": "borrowing from a zero without paying it back",
         "topic": "Multi-digit subtraction",
         "tell": "500 - 236 answered as 364",
         "detect": [],
         "rule": "When they need to borrow and the next column holds a 0, they change the 0 into a 9 but"
                 " never take the 1 from the column beyond it, so the number silently gains a hundred.",
         "why": "They have learned the true shortcut that a 0 becomes 9 when you borrow through it, but"
                " the reason for the 9 was never unpacked, so the second half of the trade has nothing"
                " holding it in place.",
         "fix": "Estimate first: 500 minus roughly 240 has to be around 260, so 364 is far too big."
                " Then do the trade in two visible steps on paper: 500 becomes 4 hundreds and 10 tens,"
                " then 4 hundreds, 9 tens and 10 ones. Write each new number above the old one so the"
                " hundreds digit is seen dropping to 4.",
         "say": "Your columns are all subtracted correctly, so the hard part is fine. Estimate with me"
                " first. Five hundred take away about two hundred forty should land near two sixty. Your"
                " answer is a hundred above that. Where did the extra hundred come from when you changed"
                " the zero?",
        },
        {"id": "chain-rounding", "name": "rounding twice up the number",
         "topic": "Rounding & estimating",
         "tell": "3,548 rounded to the nearest hundred answered as 3,600",
         "detect": [],
         "rule": "They round from the right in stages: 48 rounds the tens up to 5, and that new 5 then"
                 " rounds the hundreds up, so a number below the halfway point still gets rounded up.",
         "why": "Rounding was practised one place at a time, and doing several small correct roundings"
                " in a row looks exactly like careful work. Nobody said the digits to the right must be"
                " read as they stand, once.",
         "fix": "Draw a number line from 3,500 to 3,600 with 3,550 marked in the middle. Put 3,548 on"
                " it and let them see it sits just left of the midpoint, so the nearer end is 3,500."
                " State the rule as one look: cover everything right of the rounding digit and read only"
                " the single digit next door.",
         "say": "Each of those little roundings was done right, which is why this one is sneaky. Draw a"
                " line from thirty five hundred to thirty six hundred and mark the middle. Where does"
                " three thousand five hundred forty eight sit? Which end is it closer to?",
        },
        {"id": "no-placeholder-zero", "name": "second row written without its zero",
         "topic": "Multi-digit multiplication",
         "tell": "23 x 45 answered as 207",
         "detect": ["two oh seven"],
         "rule": "In the second partial product they multiply by the 4 and write 92 starting in the ones"
                 " column, instead of recording that the 4 means 40 and the row is worth 920.",
         "why": "In the tens digit they see a 4, and multiplying by 4 is what they were trained to do."
                " The placeholder zero was taught as a ritual step rather than as the thing that says"
                " this row is forty of them.",
         "fix": "Estimate: 23 times 45 is roughly 20 times 45, about 900, so 207 cannot be right. Then"
                " rebuild it as an area model with four boxes: 20 times 40, 20 times 5, 3 times 40 and 3"
                " times 5. The 800 box makes it obvious the tens row is worth hundreds, not tens.",
         "say": "Both of your multiplications were right, so your facts are strong. Estimate it with"
                " me. Twenty three is about twenty, and twenty groups of forty five is around nine"
                " hundred. Your answer is much smaller, so look at the second row. Is that four really a"
                " four, or forty?",
        },
        {"id": "times-zero-gives-the-number", "name": "multiplying by zero leaves it alone",
         "topic": "Multiplication facts",
         "tell": "6 x 0 answered as 6",
         "detect": [],
         "rule": "They treat 0 in multiplication the way it behaves in addition, as a do-nothing number,"
                 " so any number times zero comes back unchanged.",
         "why": "Adding zero really does leave a number alone, and that is a rule they were taught and"
                " rewarded for. Zero looks like the same character in both settings, so carrying the"
                " behaviour across is reasonable.",
         "fix": "Read it as a story instead of a fact: six groups with zero things in each group. Draw"
                " six empty circles and count what is inside them. Then run the pattern down: six times"
                " three is 18, six times two is 12, six times one is 6, six times zero is what comes"
                " next.",
         "say": "You are thinking of adding zero, and there you would be exactly right, zero really"
                " does leave a number alone. Multiplying tells a different story. Draw six circles with"
                " nothing inside any of them, then count everything you drew. How many things are there"
                " altogether?",
        },
        {"id": "quotient-missing-zero", "name": "skipping the zero in the quotient",
         "topic": "Long division",
         "tell": "618 divided by 6 answered as 13",
         "detect": [],
         "rule": "When a step divides into a number too small to hold the divisor, they move on to the"
                 " next digit without writing a 0 above, so the quotient loses a place and comes out ten"
                 " times too small.",
         "why": "Writing a 0 feels like writing nothing, and they were taught to only record real"
                " answers. The columns above the bar have never been presented as place value that must"
                " stay lined up.",
         "fix": "Estimate: 618 shared among 6 is about 100 each, so 13 is far too small. Then require"
                " one digit above the bar for every digit inside it, checking alignment after each step."
                " Multiply back at the end: 13 times 6 is 78, nowhere near 618.",
         "say": "Every division step you did was correct, which is why this is easy to miss. Check the"
                " size first. Six hundred eighteen shared between six people is about a hundred each."
                " Then count digits. Six hundred eighteen has three, so how many spaces belong above the"
                " bar?",
        },
        {"id": "remainder-as-decimal", "name": "the remainder written after a point",
         "topic": "Interpreting remainders",
         "tell": "17 divided by 5 answered as 3.2",
         "detect": [],
         "rule": "They compute 3 remainder 2 correctly and then write the remainder after a decimal"
                 " point, as though the leftover 2 named tenths rather than 2 out of the 5 needed to make"
                 " another whole.",
         "why": "Both notations are ways of writing what is left over, and nobody has shown that the"
                " digit after the point is measured against ten while a remainder is measured against"
                " the divisor.",
         "fix": "Do it with money: 17 dollars shared by 5 people gives 3 dollars each with 2 dollars"
                " left, and those 2 dollars split five ways is 40 cents, so each person gets 3 dollars"
                " 40. Then check by multiplying: 3.2 times 5 is 16, which is not 17, but 3.4 times 5 is"
                " 17.",
         "say": "Your division is right, three each with two left over. The question is what those two"
                " leftovers are worth. Share seventeen dollars between five people, then split the two"
                " dollars that are left. How much extra does each person get? Now check by multiplying"
                " back.",
        },
        {"id": "factors-multiples-swap", "name": "listing multiples when asked for factors",
         "topic": "Factors vs. multiples",
         "tell": "asked for the factors of 6, answers 6, 12, 18, 24",
         "detect": [],
         "rule": "They treat factor and multiple as the same idea, and default to the one they practised"
                 " more, so a request for factors produces the times table of the number instead of the"
                 " numbers that divide into it.",
         "why": "Both words arrive in the same week, both are about multiplication, and both live in"
                " the same sentence: 3 times 4 is 12. The words label different roles in that sentence,"
                " and the roles are easy to lose.",
         "fix": "Anchor each word to a picture. Factors are the rectangles you can build with exactly 6"
                " tiles: 1 by 6 and 2 by 3, so the factors are the side lengths and there are only a"
                " few. Multiples are the stops you land on counting by 6 forever. Say aloud: factors fit"
                " inside, multiples run outside.",
         "say": "That list is perfectly correct for a different question, those are the multiples of"
                " six. Try this. Take six tiles and build every rectangle you can with all of them. Tell"
                " me the side lengths you used. Factors fit inside the number, and multiples go past it.",
        },
        {"id": "bigger-denominator-bigger-fraction", "name": "the bigger bottom number wins",
         "topic": "Comparing fractions",
         "tell": "asked which is larger, 1/3 or 1/8, answers 1/8",
         "detect": ["1/8 is bigger", "one eighth is bigger", "eight is bigger than three"],
         "rule": "They compare fractions by comparing the denominators as whole numbers, so 1/8 beats"
                 " 1/3 because 8 beats 3, ignoring that a bigger denominator means the whole was cut into"
                 " more and therefore smaller pieces.",
         "why": "This is the whole-number rule working exactly as trained: for four years bigger digits"
                " have meant bigger amounts. The denominator is the first number they ever meet where"
                " growing makes the value shrink.",
         "fix": "Fold two identical paper strips, one into 3 equal parts and one into 8, and shade one"
                " piece of each. Lay them on top of each other. Then say it as sharing: would you rather"
                " split one pizza with two friends or with seven? More people means a smaller slice.",
         "say": "Eight is definitely bigger than three, so I can see the road you took. Try it as"
                " pizza. Would you rather share one pizza with two friends, or with seven friends? More"
                " people cutting means each slice gets smaller, so the bigger bottom number makes the"
                " tinier piece.",
        },
        {"id": "counts-ticks-not-gaps", "name": "counting the marks instead of the spaces",
         "topic": "Fractions on a number line",
         "tell": "on a 0-to-1 line cut into 4 equal parts, the third mark is named 3/5",
         "detect": ["three fifths", "5 parts"],
         "rule": "They count the tick marks on the number line, including the 0 and 1 at the ends, to"
                 " get the denominator, so a line in 4 equal parts gets read as fifths because there are"
                 " 5 marks to count.",
         "why": "Counting objects is exactly what they have been rewarded for since kindergarten, and"
                " tick marks are the only things on the line that look like objects. The intervals are"
                " empty space, which does not look countable.",
         "fix": "Have them colour each gap a different colour before naming anything, then count the"
                " coloured strips, not the lines. Ask what the whole is worth: 0 to 1, split into how"
                " many painted pieces? Then check the answer for sense, since 3/5 and 3/4 cannot both"
                " name the same point.",
         "say": "You counted every mark on that line and did not miss one. Fractions count the spaces"
                " between the marks, not the marks. Colour in each gap from zero to one, using a"
                " different colour for each. Now how many coloured pieces make the whole, and how many"
                " are shaded?",
        },
        {"id": "add-across-fractions", "name": "adding across, top and bottom",
         "topic": "Adding & subtracting fractions",
         "tell": "1/2 + 1/3 answered as 2/5",
         "detect": ["two fifths"],
         "rule": "They add the numerators together and the denominators together, treating a fraction as"
                 " two separate whole numbers stacked up rather than as one quantity.",
         "why": "Column addition is the only addition procedure they own, and nothing about the way a"
                " fraction is written announces that the bottom number is a different KIND of thing from"
                " the top one.",
         "fix": "Draw both fractions on the same whole. One half is a big piece and one third is"
                " smaller, and two fifths comes out smaller than the half they started with, so the"
                " answer cannot be right. Then rebuild: the denominator names the SIZE of the piece, so"
                " the pieces have to match before you are allowed to count them together.",
         "say": "Look at what your answer says. You started with half a pizza and added more, and you"
                " ended up holding less than half. So your counting is fine. It is the pieces that are"
                " not the same size yet, and the bottom number is what tells you the size.",
        },
        {"id": "multiplying-makes-bigger", "name": "multiplying always makes it bigger",
         "topic": "Multiplying fractions",
         "tell": "6 x 1/2 answered as 12",
         "detect": [],
         "rule": "They believe multiplying must produce a larger result, so when a fraction is involved"
                 " they reach for whichever operation grows the number, doubling instead of halving.",
         "why": "Every multiplication they have ever done did make the number bigger, because every"
                " factor was a whole number of at least 2. The belief is an honest generalisation from a"
                " hundred true examples.",
         "fix": "Read the times sign as the words 'groups of' and then as 'of': six groups of one half,"
                " or one half OF six. Draw six circles and cut each in half, then gather the halves."
                " Follow the pattern down: 6 times 3, 6 times 2, 6 times 1, 6 times a half, so the"
                " answers keep shrinking.",
         "say": "That rule has held true for every multiplication you have done so far, so I understand"
                " it. Read the sign as the word of. One half of six. If I have six cookies and take half"
                " of them, do I end up with more cookies or fewer? Draw the six and cut each one.",
        },
        {"id": "divide-fractions-across", "name": "dividing straight across the fractions",
         "topic": "Dividing & mixed numbers",
         "tell": "1/2 divided by 1/4 answered as 1/8",
         "detect": ["one eighth"],
         "rule": "They apply the multiplying-fractions procedure to division, or multiply straight"
                 " across without flipping, because they also expect dividing to make the answer smaller.",
         "why": "Multiplying across is the one fraction procedure that actually works the easy way, so"
                " it becomes the default. And division has always made numbers smaller, so an answer of"
                " 2 looks impossible.",
         "fix": "Ask the question in words: how many quarters fit inside one half? Draw a half and lay"
                " quarter pieces on it until it is covered. Two fit, so the answer is 2, and 1/8 is"
                " smaller than what they started with, which cannot happen when you count how many"
                " pieces fit.",
         "say": "You multiplied across neatly, and that move is right for multiplying. Division asks"
                " something else. How many quarter pieces fit inside one half? Draw the half and lay"
                " quarters on top until it is covered. Count the quarters you used, and that is your"
                " answer.",
        },
        {"id": "longer-decimal-is-bigger", "name": "more digits means a bigger decimal",
         "topic": "Comparing & rounding decimals",
         "tell": "asked which is larger, 0.45 or 0.7, answers 0.45",
         "detect": ["0.45 is bigger", "point four five is bigger", ".45 is bigger"],
         "rule": "They compare the digits after the point as if they were a whole number, so 45 beats 7"
                 " and the longer decimal wins, ignoring that the first digit after the point counts"
                 " tenths.",
         "why": "For whole numbers, more digits genuinely does mean a bigger number, and that rule has"
                " never failed them. The decimal point looks like a separator rather than a change of"
                " scale.",
         "fix": "Turn both into money: 0.45 is 45 cents and 0.7 is 70 cents, and 70 cents is clearly"
                " more. Or line them up in a place-value chart, writing 0.7 as 0.70 so both have two"
                " places. Then compare tenths first, the way you compare tens before ones.",
         "say": "Forty five is bigger than seven, so I see exactly what you did. Try it as money. Forty"
                " five cents, or seventy cents. Which would you rather have in your pocket? The first"
                " spot after the point is dimes, so write them both with two places and compare the"
                " dimes first.",
        },
        {"id": "decimals-lined-up-right", "name": "lining up the last digits instead of the points",
         "topic": "Adding & subtracting decimals",
         "tell": "3.4 + 0.25 answered as 5.9",
         "detect": [],
         "rule": "They stack the numbers so the rightmost digits line up, the way they always have with"
                 " whole numbers, so tenths get added to hundredths and the decimal point is placed by"
                 " copying.",
         "why": "Right-alignment is the rule that made whole-number addition work every time, and it is"
                " a rule about where the last digit goes. The idea that the point, not the edge, marks"
                " the place values is new.",
         "fix": "Estimate first: 3.4 plus a quarter is a bit more than 3, so 5.9 is impossible. Then"
                " write both with the same number of decimal places, 3.40 and 0.25, and stack the points"
                " in a straight vertical line. Money makes it concrete: 3 dollars 40 plus 25 cents.",
         "say": "Your digits are added correctly, so the arithmetic is not the issue. Estimate it"
                " first. Three point four is a bit over three, and you added about a quarter, so the"
                " answer should still be near three. Write them as money and line the points up"
                " underneath each other.",
        },
        {"id": "unit-rate-inverted", "name": "dividing the unit rate upside down",
         "topic": "Ratios & unit rates",
         "tell": "12 apples cost 3 dollars, cost per apple answered as 4 dollars",
         "detect": ["4 dollars", "four dollars each"],
         "rule": "They always divide the larger number by the smaller one, so the division gets set up"
                 " upside down and the answer describes apples per dollar while the question asked"
                 " dollars per apple.",
         "why": "Division has always been presented big number first, and a decimal answer looks like a"
                " mistake at this age. Dividing 3 by 12 feels backwards even though it is exactly what"
                " per apple means.",
         "fix": "Have them write the units into the division: dollars per apple means dollars divided"
                " by apples. Then sanity check against the story: if one apple cost 4 dollars, twelve"
                " apples would cost 48 dollars, not 3. Estimating first also helps, since 12 apples for"
                " 3 dollars is clearly cheap.",
         "say": "You picked the right two numbers, so the setup is nearly there. Test your answer"
                " against the story. If one apple costs four dollars, what would twelve apples cost?"
                " Compare that to three dollars. The word per tells you which number gets shared out.",
        },
        {"id": "area-perimeter-swap", "name": "adding the sides to find area",
         "topic": "Perimeter & area",
         "tell": "area of a 4 by 6 rectangle answered as 20",
         "detect": ["added the sides"],
         "rule": "They use one formula for both questions, usually adding the side lengths, so area gets"
                 " answered with the perimeter and the two words point at the same procedure.",
         "why": "Both questions arrive in the same lesson with the same picture and the same two"
                " numbers, and both words are long and new. Nothing in the picture forces them to be"
                " different until units are taken seriously.",
         "fix": "Make them different jobs. Perimeter is the fence you walk around the outside; area is"
                " the carpet that covers the inside. Have them draw the rectangle on grid paper, trace"
                " the fence with a finger, then count the squares inside. Attach units: feet for the"
                " fence, square feet for the carpet.",
         "say": "Adding the sides is the right move for one of these two questions. Draw the rectangle"
                " on grid paper. Now trace all the way around the outside with your finger, that is the"
                " fence. Then count every square inside it, that is the carpet. Which one did the"
                " question ask for?",
        },
    ],
    "prealgebra": [
        {"id": "left-to-right-arithmetic", "name": "working strictly left to right",
         "topic": "Order of operations (PEMDAS)",
         "tell": "3 + 4 x 5 answered as 35",
         "detect": [],
         "rule": "They evaluate the expression in reading order, so 3 plus 4 is done first and the 7 is"
                 " then multiplied by 5, ignoring that multiplication is settled before addition.",
         "why": "Reading left to right is how every sentence, every number and every calculator key"
                " press has worked for them. Order of operations is the first place where written order"
                " is not doing order.",
         "fix": "Have them circle the multiplication first, in pen, before writing anything else, so 4"
                " x 5 becomes a single object of 20 sitting next to the 3. A context helps: 3 dollars"
                " plus 4 tickets at 5 dollars each. The tickets have to be totalled before anything is"
                " added on.",
         "say": "Your arithmetic is right in both steps, so this is about order only. Picture three"
                " dollars in your pocket plus four tickets that cost five dollars each. You have to work"
                " out the tickets before you add your three. Circle the multiplying part first, then"
                " add.",
        },
        {"id": "multiply-before-divide", "name": "doing all multiplying before dividing",
         "topic": "Order of operations (PEMDAS)",
         "tell": "24 divided by 6 x 2 answered as 2",
         "detect": [],
         "rule": "They read PEMDAS as a strict six-step ladder, so every multiplication is completed"
                 " before any division, and 6 times 2 is done first even though the division came earlier"
                 " in the line.",
         "why": "The mnemonic really does list M before D, and treating a memorised list as an ordered"
                " sequence is exactly how mnemonics usually work. Nobody flagged that two of the letters"
                " are a tie.",
         "fix": "Rewrite the mnemonic in two levels on paper, with multiplication and division sharing"
                " one rung and addition and subtraction sharing the next, then work each rung left to"
                " right. Show a counterexample they can check another way: 24 divided by 6, times 2, is"
                " 4 groups doubled.",
         "say": "You applied the mnemonic exactly as it is written, which is fair, the letters really"
                " do go in that order. Multiplying and dividing are actually a tie, and so are adding"
                " and subtracting. When two tie, you take them left to right. Try the line again that"
                " way.",
        },
        {"id": "gcf-lcm-swap", "name": "giving the multiple when asked for the factor",
         "topic": "GCF & LCM",
         "tell": "greatest common factor of 4 and 6 answered as 12",
         "detect": [],
         "rule": "They run one procedure for both questions and pick the answer that is larger, because"
                 " the word 'greatest' pulls them toward a big number, so the least common multiple is"
                 " offered as the greatest common factor.",
         "why": "The two phrases share three words and both are computed from the same pair of numbers"
                " in the same lesson. The word greatest genuinely does mean biggest, and 12 is bigger"
                " than 2.",
         "fix": "Bound each one before computing. A common FACTOR has to divide both, so it can never"
                " be larger than the smaller number, which caps it at 4 here. A common MULTIPLE has to"
                " be at least as large as the bigger number. Have them state the ceiling or floor out"
                " loud before working.",
         "say": "Twelve is a genuinely important number for this pair, it is the least common multiple."
                " A factor has to divide into both numbers, so it can never be bigger than the smaller"
                " one. That caps you at four here. Which numbers divide into both four and six?",
        },
        {"id": "negatives-ranked-by-size", "name": "the bigger negative is the bigger number",
         "topic": "The number line & comparing",
         "tell": "asked which is greater, -8 or -3, answers -8",
         "detect": ["-8 is bigger", "negative eight is bigger", "-8 is greater"],
         "rule": "They compare negatives by comparing the digits and ignoring the sign, so -8 beats -3"
                 " because 8 beats 3, treating the minus sign as a label rather than as a direction on"
                 " the line.",
         "why": "Digit size has decided every comparison they have ever made. And -8 IS bigger in one"
                " real sense, as a distance from zero, which is exactly what absolute value will measure"
                " next week.",
         "fix": "Put both on a number line and use the rule that the number further right is greater."
                " Then attach money or temperature: owing 8 dollars against owing 3 dollars, or 8 below"
                " zero against 3 below zero. Which would you rather have? The bigger debt is the worse"
                " position.",
         "say": "You are right that eight is the bigger amount, and that idea gets its own name later,"
                " absolute value. For greater than, think of debt. Would you rather owe eight dollars or"
                " three dollars? On the number line the one further to the right is always the greater"
                " one.",
        },
        {"id": "sum-keeps-the-first-sign", "name": "add the digits keep the first sign",
         "topic": "Adding & subtracting integers",
         "tell": "-5 + 3 answered as -8",
         "detect": [],
         "rule": "They add the two digits regardless of sign and then attach the sign of whichever"
                 " number came first, so a negative plus a positive still moves further into the"
                 " negatives.",
         "why": "Adding has always meant combining and growing, and the plus sign says add. The idea"
                " that one of the two numbers pushes in the opposite direction is genuinely new, and the"
                " signs look like labels, not arrows.",
         "fix": "Walk it on a number line: start at -5 and take 3 steps toward the positive side,"
                " landing on -2. Or use money: 5 dollars of debt and then 3 dollars earned leaves 2"
                " dollars of debt. Have them say which direction each number pushes before they combine"
                " anything.",
         "say": "You kept careful track of that negative sign, which many people drop. Try it as money."
                " You owe five dollars, then you earn three. Are you further into debt, or closer to"
                " even? Start at negative five on the line and take three steps toward zero.",
        },
        {"id": "minus-a-negative-stays-negative", "name": "two minus signs still mean subtract",
         "topic": "Adding & subtracting integers",
         "tell": "5 - (-3) answered as 2",
         "detect": [],
         "rule": "They see a subtraction sign and take away, treating the second minus as decoration, so"
                 " subtracting a negative gives the same answer as subtracting a positive.",
         "why": "Every minus sign they have met so far meant take away, and there is no everyday"
                " sentence in which removing something makes you better off. The double sign looks like"
                " emphasis rather than a second instruction.",
         "fix": "Use debt: if I take away a 3 dollar debt from you, you are 3 dollars better off, so 5"
                " becomes 8. Or run the pattern and let it force the answer: 5 minus 2, 5 minus 1, 5"
                " minus 0, 5 minus negative 1. The answers climb by one each time, so the next one has"
                " to be 6.",
         "say": "You spotted the subtraction correctly, and the second sign is doing something extra."
                " Imagine I erase a three dollar debt of yours. Are you better off or worse off? Now run"
                " the pattern, five minus two, five minus one, five minus zero. Which way are the"
                " answers heading?",
        },
        {"id": "mixed-number-smaller-fraction-first", "name": "flipping the fraction part to subtract",
         "topic": "Mixed numbers",
         "tell": "5 1/4 - 2 3/4 answered as 3 2/4",
         "detect": ["three and two fourths"],
         "rule": "They subtract the whole numbers, then subtract the smaller fraction from the larger"
                 " one whichever way round they appear, so 1/4 minus 3/4 is done as 3/4 minus 1/4 and no"
                 " regrouping is needed.",
         "why": "This is the whole-number smaller-from-larger repair applied to a new column. Faced"
                " with an impossible-looking subtraction they flip it, which keeps the procedure moving,"
                " and the whole numbers are untouched.",
         "fix": "Estimate: 5 and a bit minus nearly 3 is about 2 and a half, so an answer above 3 is"
                " too big. Then regroup visibly, rewriting 5 1/4 as 4 5/4 by trading one whole for four"
                " quarters, exactly like borrowing a ten. Drawing quarter-circles makes the trade"
                " concrete.",
         "say": "Your whole numbers and your quarters were each subtracted accurately. Estimate first"
                " though. Five and a bit, take away almost three, should land close to two and a half."
                " Your answer is over three. Trade one of those wholes for four quarters and try again.",
        },
        {"id": "flip-the-first-fraction", "name": "flipping the wrong fraction when dividing",
         "topic": "Multiplying & dividing fractions",
         "tell": "1/2 divided by 3/4 answered as 1 1/2",
         "detect": ["one and a half"],
         "rule": "They remember to invert and multiply but flip the first fraction instead of the"
                 " second, so the dividend gets reciprocated and the answer comes out as the reciprocal"
                 " of the truth.",
         "why": "Keep, change, flip is memorised as three moves without an anchor for WHICH one flips,"
                " and the first fraction is the one their eye reaches first. The rule was given as a"
                " ritual, not as a reason.",
         "fix": "Sense-check the size: dividing by 3/4, a number less than 1, must give an answer"
                " bigger than 1/2, but not bigger than 1/2 doubled. Then reground the rule in meaning:"
                " how many three-quarter pieces fit into a half? Less than one of them fits, so the"
                " answer has to be below 1.",
         "say": "You remembered to flip and multiply, which is the right family of moves. Check the"
                " size before you trust it. How many three quarter pieces fit inside one half? Not even"
                " one whole piece fits, so should your answer be above one or below one?",
        },
        {"id": "dividing-makes-smaller", "name": "dividing always makes it smaller",
         "topic": "Multiplying & dividing decimals",
         "tell": "6 divided by 0.5 answered as 3",
         "detect": [],
         "rule": "They believe division must shrink a number, so when the divisor is less than 1 they"
                 " halve or otherwise reduce instead of asking how many of the divisor fit inside.",
         "why": "Every divisor they have used has been a whole number of at least 2, so division has"
                " always shrunk things. Also, 0.5 is read as half and half is strongly linked to the"
                " action of halving.",
         "fix": "Say it as a counting question: how many half-dollars are in 6 dollars? Lay out six"
                " circles and cut each in half, then count the pieces. Twelve. Then run the pattern: 6"
                " divided by 4, by 2, by 1, by 0.5, so the answers grow as the divisor shrinks.",
         "say": "The word half is doing the work there, and halving six really does give three."
                " Division asks a different question. How many half dollar coins make six dollars? Cut"
                " six circles in half and count the pieces. When the divider gets smaller, the answer"
                " grows.",
        },
        {"id": "percent-decimal-one-shift", "name": "moving the point only one place",
         "topic": "Decimals, fractions & percents",
         "tell": "7% written as a decimal answered as 0.7",
         "detect": [],
         "rule": "They convert a percent to a decimal by moving the point one place, or by simply"
                 " putting the digits after a point, rather than dividing by 100 which moves it two"
                 " places.",
         "why": "One shift is what dividing by 10 does, and the shifting rule was learned as an action"
                " rather than as a division. With a one-digit percent there is only one digit to move"
                " past, so one hop feels complete.",
         "fix": "Anchor with a known pair: 50 percent is 0.5 and 5 percent is 0.05, and have them see"
                " those cannot be the same. Then say what percent means, out of 100, so 7 percent is"
                " 7/100, and 7 divided by 100 needs two hops. Writing 7 as 07 first gives the second"
                " digit to hop over.",
         "say": "Moving the point is exactly the right action, it is the number of hops we need to"
                " settle. Percent means out of one hundred, so seven percent is seven hundredths."
                " Compare it with fifty percent, which is zero point five. Can seven percent and seventy"
                " percent both be point seven?",
        },
        {"id": "scale-by-adding", "name": "scaling a recipe by adding the difference",
         "topic": "Scaling recipes & maps",
         "tell": "6 cups serves 4 people, so 8 people answered as 10 cups",
         "detect": ["10 cups", "ten cups", "added 4"],
         "rule": "They keep the DIFFERENCE between the two quantities constant instead of the ratio, so"
                 " if people go up by 4 then cups go up by 4 as well.",
         "why": "Additive reasoning is older, safer and works for many real patterns such as ages and"
                " temperatures. Nothing in the wording of a recipe problem announces that this"
                " relationship is multiplicative.",
         "fix": "Build a ratio table with the halfway rung in it: 4 people and 6 cups, 2 people and 3"
                " cups, 8 people and 12 cups. Then check with the doubling story: 8 people is exactly"
                " twice 4 people, so everything on the recipe card doubles. Ask what 10 cups would mean"
                " for 40 people.",
         "say": "You kept the numbers moving together, which is the right instinct. Ask how many times"
                " bigger, not how much bigger. Eight people is exactly double four people, so every"
                " ingredient on the card doubles too. What does six cups become when the whole recipe"
                " doubles?",
        },
        {"id": "ratio-written-backwards", "name": "writing the ratio in the wrong order",
         "topic": "Ratios",
         "tell": "3 cats and 5 dogs, ratio of cats to dogs answered as 5 to 3",
         "detect": ["5 to 3", "five to three"],
         "rule": "They write the two numbers in the order they appear in the picture or the sentence, or"
                 " put the larger one first out of habit, instead of following the order named by the"
                 " words to and colon.",
         "why": "Order has rarely mattered before: 3 and 5 add and multiply the same either way. A"
                " ratio is one of the first notations where swapping the numbers gives a different"
                " answer entirely.",
         "fix": "Have them write the labels above the numbers before writing any digits: cats first,"
                " dogs second, because that is the order the question said. Then test the reversed one"
                " out loud, 5 cats to 3 dogs, and check it against the picture.",
         "say": "You found both numbers correctly, so only the order is in play. Write the two words"
                " down first, in the order the question says them, then put a number under each word."
                " Now read your answer back as a sentence and check it against the picture.",
        },
        {"id": "discount-is-the-price", "name": "giving the discount as the new price",
         "topic": "Percent increase & decrease",
         "tell": "a 40 dollar coat at 25% off, final price answered as 10 dollars",
         "detect": ["10 dollars", "ten dollars"],
         "rule": "They compute the percent OF the number correctly and stop there, reporting the amount"
                 " saved as the amount paid, because the last procedure they practised ended at that"
                 " step.",
         "why": "Percent of a number was the whole skill last week, and 10 is the correct answer to a"
                " question just next door to this one. The word off quietly adds a subtraction the"
                " procedure does not contain.",
         "fix": "Make them label the 10 before doing anything else: is this the money saved or the"
                " money paid? Then draw a 40 dollar bar, shade the 25 percent taken off, and label the"
                " unshaded part. A reality check helps too, since a quarter off should still leave most"
                " of the price.",
         "say": "Ten dollars is exactly right, and now name it. Is that the money you save, or the"
                " money you hand over? A quarter off means you still pay for three quarters of the coat."
                " Draw the forty dollar bar, shade the part that comes off, and read the rest.",
        },
        {"id": "median-without-sorting", "name": "taking the middle of the unsorted list",
         "topic": "Mean & median",
         "tell": "median of 7, 2, 9, 3, 5 answered as 9",
         "detect": [],
         "rule": "They take the value physically in the middle of the list as written, without putting"
                 " the numbers in order first, so the median depends on the order the data happened to be"
                 " typed in.",
         "why": "Median is defined as the middle value, and the middle of a written list is a real,"
                " visible thing. Ordering is a hidden first step that the definition does not mention"
                " out loud.",
         "fix": "Write each number on a separate card and have them physically line the cards up"
                " smallest to largest, then pull the middle card out. Then reshuffle the original list"
                " into a different order and ask whether the middle of the list changed, and whether the"
                " true middle value should.",
         "say": "Nine is sitting right in the middle of that list, so I can see why you picked it."
                " Median means the middle after you line them up in order, smallest to largest. Write"
                " the numbers on cards, sort them, then pull out the one standing in the centre.",
        },
        {"id": "conjoining-unlike-terms", "name": "sticking a number onto the variable",
         "topic": "Combining like terms",
         "tell": "3x + 2 simplified to 5x",
         "detect": ["5x", "five x"],
         "rule": "They add every number in sight and reattach the letter, treating x as a unit label"
                 " rather than an unknown quantity, so 3x and 2 are combined even though one counts x's"
                 " and the other counts ones.",
         "why": "Every expression so far has collapsed into a single answer, and a leftover plus sign"
                " feels unfinished. Combining like terms was taught right before, so combining is the"
                " move currently loaded.",
         "fix": "Make the letter a thing: x is a box of pencils, and the 2 is 2 loose pencils, so 3"
                " boxes and 2 loose cannot be 5 boxes. Then test with numbers: put x as 10 and compute"
                " both expressions, getting 32 and 50, which proves they are not the same expression.",
         "say": "Adding like terms is exactly the right skill here, so let us check which terms are"
                " alike. Say x means a box of pencils. You have three boxes and two loose pencils. Is"
                " that five boxes? Now try x as ten in both versions and compare what you get.",
        },
        {"id": "solve-by-repeating-the-operation", "name": "repeating the operation instead of undoing it",
         "topic": "One-step equations",
         "tell": "x + 5 = 12 answered as x is 17",
         "detect": [],
         "rule": "They perform whichever operation is written in the equation on the two numbers they"
                 " can see, so a plus sign means add, rather than undoing the plus 5 by subtracting it"
                 " from both sides.",
         "why": "For years the operation sign has been an instruction to carry out, and a page of plus"
                " signs meant a page of adding. Reading a sign as something that has already happened"
                " and must be reversed is new.",
         "fix": "Use the scales picture: x and 5 on one pan, 12 on the other, and ask what to take off"
                " both pans to leave x alone. Then always substitute back, since 17 plus 5 is 22, not"
                " 12. Have them say out loud what has been DONE to x before choosing what to do about"
                " it.",
         "say": "You spotted the plus sign and acted on it, and that sign is telling you something"
                " important. Test your answer first. Put seventeen in for x and add five. Do you land on"
                " twelve? The five has already been added to x, so what takes it back off?",
        },
    ],
    "algebra1": [
        {"id": "distribute-one-term-only", "name": "distributing to the first term only",
         "topic": "the distributive property",
         "tell": "3(x + 4) answered as 3x + 4",
         "detect": ["3x + 4", "three x plus four"],
         "rule": "They multiply the outside factor by the FIRST term inside the parentheses and copy the"
                 " rest down unchanged.",
         "why": "Left-to-right reading habits make the first term feel like 'the' term, and in 3(x) + 4"
                " — which looks almost identical — copying the 4 IS right.",
         "fix": "Draw it as one rectangle 3 tall and x + 4 wide, then cut it down the middle: two"
                " rectangles, 3 by x and 3 by 4. The 3 touches BOTH pieces because it is the height of"
                " the whole thing. Then re-do their problem on the picture before doing it in symbols.",
         "say": "Good — you got the three times x part exactly right. Let me draw what the parentheses"
                " mean, because there is a second piece that the three also has to reach, and the"
                " picture makes it obvious.",
        },
        {"id": "combine-unlike-powers", "name": "adding terms with different exponents",
         "topic": "Combining like terms",
         "tell": "3x + 2x^2 answered as 5x^2",
         "detect": ["5x^2", "5x squared", "five x squared"],
         "rule": "They read 'like terms' as 'terms containing the same letter', so any two terms with an"
                 " x in them get their coefficients added, and the bigger exponent is carried along for"
                 " the ride.",
         "why": "3x + 2x = 5x works exactly this way, and the little 2 looks like a decoration attached"
                " to the x rather than part of what the term IS.",
         "fix": "Have them put x = 10 into both: 3(10) + 2(100) is 230, but 5(100) is 500, so the rule"
                " visibly breaks. Then rename the pieces — x^2 is a square tile and x is a stick — and"
                " lay them on the desk. Three sticks and two squares cannot be five of any one thing.",
         "say": "Your instinct to collect the x pieces together is the right instinct, and your"
                " arithmetic is clean. Try putting ten in for x on both your version and mine and see"
                " whether they land on the same number. That test tells us which pieces are allowed to"
                " combine.",
        },
        {"id": "letter-as-object", "name": "reading the letter as an object",
         "topic": "Variables, terms & coefficients",
         "tell": "2a + 3b simplified to 5ab",
         "detect": ["5ab", "five a b", "5 ab"],
         "rule": "They read a as 'apples' and b as 'bananas', so 2a + 3b becomes five pieces of fruit,"
                 " with the letters glued together as a label on one count.",
         "why": "Letters are usually introduced as abbreviations — 3m means three metres — and that"
                " reading is genuinely correct for units, so it survives long past the point where a"
                " letter starts meaning an unknown number.",
         "fix": "Let a be 10 and b be 2. Their expression gives 100; the real one gives 26. Then"
                " rewrite the letters out loud as 'the number of apples' and 'the number of bananas' and"
                " ask what 2a + 3b counts. The letters stand for how many, not for what.",
         "say": "You spotted that there are five somethings in there, and that is a real feature of the"
                " problem. Let me have you test it: let a be ten and b be two, work out both versions,"
                " and tell me what you notice about the two answers.",
        },
        {"id": "subtract-parens-first-term-only", "name": "subtracting only the first term in parentheses",
         "topic": "Combining like terms",
         "tell": "8 - (3x - 5) answered as 8 - 3x - 5",
         "detect": ["8 - 3x - 5", "eight minus three x minus five", "minus 3x minus 5"],
         "rule": "The minus sign in front of the parentheses is applied only to the first term inside;"
                 " every other term is copied down with the sign it already had.",
         "why": "The minus really does mean 'take away', and taking away the visible 3x is the part"
                " they can see; the minus five already looks negative, so it feels like it has already"
                " been dealt with.",
         "fix": "Rewrite the subtraction as adding negative one times the quantity, then distribute —"
                " now it is the distributive property they already trust. Confirm with x = 1: the"
                " original is 8 minus negative 2, which is 10, while their version gives 0.",
         "say": "Nice job carrying that first piece across correctly. Put one in for x and work out the"
                " original and your version separately, and we will see whether the minus sign out front"
                " reached everything inside the parentheses or stopped partway.",
        },
        {"id": "term-moved-without-sign-change", "name": "moving a term without changing its sign",
         "topic": "One-, two- & multi-step equations",
         "tell": "x + 7 = 12 answered as x = 19",
         "detect": ["x = 19", "x equals 19", "x equals nineteen"],
         "rule": "They move a term across the equals sign and copy it exactly as written, so the plus"
                 " seven arrives on the other side still as plus seven.",
         "why": "'Move it to the other side' is a real shortcut they were taught; what got dropped is"
                " that moving is shorthand for undoing — doing the same operation to both sides.",
         "fix": "Put a balance scale on the board with x and seven blocks on the left and twelve on the"
                " right, and ask what has to happen to BOTH pans. Then have them substitute 19 into the"
                " original and hear 26 come out. Write the 'minus seven from both sides' line"
                " explicitly.",
         "say": "You knew the seven had to get out of the way, and that is exactly the right plan. Try"
                " putting nineteen back into the original problem and tell me what the left side comes"
                " out to. Then we will decide what the seven should look like once it moves.",
        },
        {"id": "inequality-sign-not-flipped", "name": "keeping the inequality direction after a negative divide",
         "topic": "Solving & graphing inequalities",
         "tell": "-2x > 6 answered as x > -3",
         "detect": ["x > -3", "x greater than -3", "x is greater than negative 3"],
         "rule": "They solve an inequality with exactly the same moves as an equation, so dividing both"
                 " sides by a negative number leaves the inequality symbol pointing the same way.",
         "why": "Transferring equation moves to inequalities is correct for every other step, and"
                " equations have no direction to preserve, so nothing in that well-built habit warns"
                " them that this one operation is different.",
         "fix": "Test x = -10 in the original: negative two times negative ten is 20, which is bigger"
                " than 6, yet negative ten is not in their answer. Then show the number line: two sits"
                " left of five, but negative two sits RIGHT of negative five, so multiplying by a"
                " negative reflects the order.",
         "say": "Your steps are clean and you divided correctly. Test negative ten in the original"
                " problem for me and tell me whether it works. Then check whether negative ten is inside"
                " the answer you wrote. What that comparison shows us is worth more than any rule I"
                " could state.",
        },
        {"id": "equals-as-produces", "name": "using equals to mean and then I get",
         "topic": "One-, two- & multi-step equations",
         "tell": "asked to double the sum of 5 and 3, they write 5 + 3 = 8 x 2 = 16",
         "detect": ["8 x 2 = 16", "= 8 x 2 =", "and then that equals"],
         "rule": "The equals sign is read as a one-way instruction meaning 'here comes the answer', so"
                 " they chain it, each new equals announcing the next result rather than claiming two"
                 " quantities are the same.",
         "why": "Years of worksheets put the answer box right after the equals sign, and a calculator's"
                " equals key behaves exactly like that — press it and something new appears.",
         "fix": "Point at their own chain and ask whether five plus three is really the same number as"
                " sixteen. Then re-stage it as a balance: whatever is written on each side of an equals"
                " must weigh the same. Have them rewrite the work as separate lines, one true statement"
                " per line.",
         "say": "Your arithmetic in that chain is all correct, every step of it. Read the middle of it"
                " back to me as a sentence, out loud: does five plus three equal sixteen? Let me show"
                " you what that little bar is actually promising, because it changes how we write the"
                " work.",
        },
        {"id": "function-notation-as-multiplication", "name": "reading f of x as f times x",
         "topic": "Function notation f(x)",
         "tell": "with f(x) = 2x + 1, f(3) answered as 3f",
         "detect": ["f times 3", "3f", "f times x"],
         "rule": "They read f(x) as a product of f and x, so f(3) means f multiplied by three, and f is"
                 " an unknown factor rather than the name of a rule.",
         "why": "Everywhere else in algebra a symbol pressed against a parenthesis means multiply — 3(x"
                " + 4) taught them precisely that — and f(x) is the first place that pattern stops"
                " holding.",
         "fix": "Say it aloud as 'f of three' every single time. Draw the function as a machine with a"
                " chute: three goes in the top, the rule 2x + 1 runs, and seven falls out. Build a small"
                " input-output table so f(3) is visibly one number, not two things multiplied.",
         "say": "You are reading the notation the way it is written everywhere else, and that is a fair"
                " reading. This one is a special case. Read it aloud with me as f of three, then feed"
                " three into the machine and tell me the number that comes out the bottom.",
        },
        {"id": "function-of-a-sum-split", "name": "splitting a function across a sum",
         "topic": "Function notation f(x)",
         "tell": "with f(x) = x^2, f(x + 3) answered as x^2 + 3",
         "detect": ["x^2 + 3", "x squared plus 3", "f(x) + f(3)"],
         "rule": "They treat the f as something that distributes over what is inside, so f(x + 3)"
                 " becomes f(x) plus 3 instead of substituting the whole quantity x + 3 wherever x"
                 " appears.",
         "why": "Distribution is the dominant move of the whole year and f(x + 3) has the same shape on"
                " the page as 3(x + 4), so the eye files it under a rule that has never let them down.",
         "fix": "Rewrite the rule with an empty box instead of a letter: f of box equals box squared."
                " Then drop the entire quantity x + 3 into the box and let them see the whole thing get"
                " squared. Confirm numerically: f(2 + 3) is 25, while their version gives 7.",
         "say": "Substituting is exactly the right idea, and you kept everything tidy. Let me rewrite"
                " the rule with an empty box in place of the letter, and then you tell me what goes into"
                " the box when the input is x plus three. The box makes the grouping visible.",
        },
        {"id": "slope-run-over-rise", "name": "computing slope as run over rise",
         "topic": "Slope as rate of change",
         "tell": "through (1, 2) and (3, 8), slope answered as 1/3",
         "detect": ["run over rise", "one third"],
         "rule": "They compute slope as horizontal change divided by vertical change, because ordered"
                 " pairs list x first, so the x difference goes on top.",
         "why": "Every other convention this year puts x before y, so leading with the x difference is"
                " a consistent and thoughtful habit rather than carelessness.",
         "fix": "Anchor it in a rate they already say out loud: dollars PER hour, miles PER gallon. The"
                " thing after 'per' is what sits on the bottom, and slope is rise per one step across."
                " Then walk the staircase between the two points on the grid, counting up first and"
                " across second.",
         "say": "You found both changes correctly, six and two, which is the hard part. Say the slope"
                " out loud as a rate for me, like miles per hour. Whatever word comes after per is the"
                " one that belongs on the bottom of the fraction. Now which of your two numbers is that?",
        },
        {"id": "perpendicular-negate-not-reciprocal", "name": "negating the slope without flipping it",
         "topic": "Parallel & perpendicular lines",
         "tell": "a line perpendicular to y = 4x + 1 given slope -4",
         "detect": [],
         "rule": "They remember the perpendicular slope as 'the negative of the original' and stop"
                 " there, dropping the reciprocal half of negative reciprocal.",
         "why": "The word negative carries the emphasis in the phrase, and for slopes of one and"
                " negative one the shortcut gives the right answer, so it passes every quick self-check"
                " they make.",
         "fix": "Graph y = 4x and y = -4x on the same axes. Both are steep and they cross in a narrow"
                " X, obviously not a square corner. Then graph y equal to negative one fourth x and see"
                " the corner turn square. Steep and shallow have to pair up.",
         "say": "Flipping the sign is half of it, and you did that half correctly. Graph your line and"
                " the original on the same axes and look at the corner where they cross. Does that look"
                " like a square corner to you, or something sharper? That tells us what is still"
                " missing.",
        },
        {"id": "substitution-into-same-equation", "name": "substituting back into the same equation",
         "topic": "Substitution",
         "tell": "solving for y in the first equation, then putting it back into that same first equation and getting 0 = 0",
         "detect": ["zero equals zero", "everything cancelled"],
         "rule": "They substitute the rearranged expression into the equation it came from, so the"
                 " statement collapses into an identity, which they then report as infinitely many"
                 " solutions or no solution.",
         "why": "The instruction is 'substitute it in', and the equation they just worked on is the one"
                " in front of them; nothing in the wording says the expression has to travel to the"
                " OTHER equation.",
         "fix": "Colour the two equations differently and draw an arrow from the first to the second,"
                " so the expression visibly travels. Then link it to the graph: one equation alone is a"
                " whole line of solutions, which is why it says nothing new — the second line is what"
                " pins down the single crossing point.",
         "say": "That collapse to zero equals zero is real information, not a mistake, and your algebra"
                " got there correctly. It happens when an expression goes home into the equation it came"
                " from. Watch what happens when we send it into the other equation instead.",
        },
        {"id": "product-rule-multiply-exponents", "name": "multiplying exponents when multiplying powers",
         "topic": "Laws of exponents",
         "tell": "x^2 times x^3 answered as x^6",
         "detect": ["x^6", "x to the sixth", "x to the 6"],
         "rule": "They use one exponent rule for every situation: whenever two powers meet, multiply the"
                 " exponents — the move that is genuinely correct for a power raised to a power.",
         "why": "Both rules were taught in the same lesson and look nearly identical on the page, and"
                " multiplying the bases feels like it ought to mean multiplying the exponents too.",
         "fix": "Expand both sides with no rules at all: x times x, then x times x times x. Have them"
                " count the x's — five. Then expand a power of a power the same way and count six."
                " Seeing the two expansions side by side separates the two rules permanently.",
         "say": "You are working from a real exponent rule, and you applied it consistently. Write both"
                " powers out the long way for me, just x's in a row, and count how many you end up with."
                " The count settles which rule belongs to which situation.",
        },
        {"id": "square-of-a-binomial-linear", "name": "squaring each term of a sum",
         "topic": "Adding & multiplying polynomials",
         "tell": "(x + 3)^2 answered as x^2 + 9",
         "detect": ["x^2 + 9", "x squared plus 9", "x squared plus nine"],
         "rule": "They treat squaring as an operation that reaches each term separately, so the square"
                 " of x plus three becomes x squared plus three squared, with no middle term at all.",
         "why": "Exponents genuinely do distribute over multiplication — the square of 3x really is 9x"
                " squared — and nothing in that correct rule announces that addition behaves"
                " differently.",
         "fix": "Draw a square with side x + 3 and cut it into four regions: x by x, x by 3, 3 by x,"
                " and 3 by 3. Their answer accounts for the two corner squares and loses the two"
                " rectangles, which together are the missing 6x. Check with x = 2: the real answer is"
                " 25, theirs is 13.",
         "say": "Both of the pieces you wrote are genuinely in the answer, so you are partway there."
                " Let me draw the square with side x plus three and chop it up. There are four regions"
                " in that picture and you have found two of them. Look at what is left over.",
        },
        {"id": "zero-product-applied-to-nonzero", "name": "setting each factor equal to any number",
         "topic": "Solving by factoring",
         "tell": "(x - 2)(x + 5) = 8 solved by setting x - 2 = 8 and x + 5 = 8",
         "detect": ["x - 2 = 8", "set each factor equal to 8", "x = 10 and x = 3"],
         "rule": "They split a factored product and set each factor equal to whatever number is on the"
                 " right-hand side, rather than using the fact that only zero forces one of the factors"
                 " to be zero.",
         "why": "The procedure they practised was 'split the factors and solve each one', and in every"
                " worked example the right side happened to be zero, so the zero never looked like the"
                " load-bearing part.",
         "fix": "Ask for two numbers whose product is eight: four and two work, and neither is eight,"
                " so knowing the product tells you nothing about the pieces. Then ask for two numbers"
                " whose product is zero and watch that one of them MUST be zero. Multiply out, move the"
                " eight over, factor again.",
         "say": "Splitting a factored expression into two smaller equations is a genuinely powerful"
                " move, and you set it up cleanly. Give me two numbers that multiply to eight. Now two"
                " numbers that multiply to zero. Notice how much more the second question forces on us."
                " That is why zero is special.",
        },
        {"id": "correlation-read-as-cause", "name": "reading a strong correlation as a cause",
         "topic": "Correlation vs. causation",
         "tell": "ice cream sales and drownings correlate strongly, answered as ice cream causing the drownings",
         "detect": ["causes the", "so it must cause", "proves that"],
         "rule": "They treat a correlation coefficient near one as evidence of a mechanism: if the"
                 " points line up, the explanatory variable is producing the response variable.",
         "why": "Most classroom scatter plots are built from genuinely causal pairs, and the line of"
                " best fit is used to predict, which sounds a great deal like control.",
         "fix": "Ask them to hunt for a third thing that could drive both columns — here, hot weather."
                " Then ask whether reversing the arrow sounds equally sensible, since the correlation is"
                " identical either way. A correlation is symmetric; a cause is not, and that asymmetry"
                " is the test.",
         "say": "You read the scatter plot correctly and the association is genuinely strong. Before we"
                " name a cause, hunt with me for a third thing that pushes both columns up at once. If"
                " you can find one, the story changes. What is going on outside on the days both numbers"
                " are high?",
        },
    ],
    "geometry": [
        {"id": "complement-supplement-swapped", "name": "swapping complementary and supplementary",
         "topic": "Complementary, supplementary & vertical angles",
         "tell": "the complement of 50 degrees given as 130 degrees",
         "detect": ["130 degrees"],
         "rule": "They pair the two words with the two totals by feel rather than by meaning, so"
                 " complementary gets matched with 180 and supplementary with 90.",
         "why": "Neither word carries a numerical hint on its face, and both are ordinary English words"
                " about completing or adding to something, so the pairing has to be memorised with no"
                " logic underneath it to fall back on.",
         "fix": "Give the pairing a structure they can rebuild: C for corner, which is the square"
                " corner of 90; S for straight, which is the straight line of 180. Draw both pictures"
                " beside the words. Then have them re-answer using the drawing rather than the memory.",
         "say": "You knew this was one of the two big totals, and your subtraction was right. Let me"
                " draw both pictures. C for corner, the square corner; S for straight, the flat line."
                " Now look at your problem and tell me which picture the word complement is pointing at.",
        },
        {"id": "angle-size-from-ray-length", "name": "judging angle size by ray length",
         "topic": "Naming & measuring angles",
         "tell": "two angles both measuring 40 degrees, the one drawn with longer rays called the bigger angle",
         "detect": ["the rays are longer", "it looks bigger", "bigger because it is longer"],
         "rule": "They measure an angle by how much of it is drawn — the length of the rays or the gap"
                 " between the endpoints — rather than by the amount of turn between the two rays.",
         "why": "Every measurement before this one, length and perimeter and area, genuinely does grow"
                " when the drawing grows, so 'bigger drawing means bigger number' has never failed them"
                " until now.",
         "fix": "Pin two paper strips at a vertex and open them to a fixed angle. Slide the strips out"
                " longer without touching the opening and re-measure with the protractor: same reading."
                " The rays are really infinite; only the turn between them is being measured.",
         "say": "You are comparing carefully and describing what you see accurately. Watch these two"
                " pinned strips. I am making the arms longer without changing how far open they are."
                " Read the protractor before and after and tell me what the number does.",
        },
        {"id": "reflect-wrong-coordinate", "name": "reflecting by changing the named axis",
         "topic": "Reflections",
         "tell": "reflecting the point (3, 5) over the y-axis answered as (3, -5)",
         "detect": ["3, negative 5", "change the y"],
         "rule": "They read 'reflect over the y-axis' as an instruction to change the y-coordinate,"
                 " since the y is the letter named in the instruction.",
         "why": "In almost every other piece of notation, the label tells you which thing to operate"
                " on, so treating the named axis as the target rather than as the mirror is a reasonable"
                " transfer.",
         "fix": "Plot the point, then physically fold the paper along the y-axis and see where the"
                " point lands. The axis is the crease, not the target. Measure the distance from the"
                " point to the crease before and after: that distance is what gets mirrored, so the"
                " coordinate that changes is the across one.",
         "say": "You made exactly one coordinate change, which is right, and you kept the other one,"
                " which is also right. Fold the paper along the y-axis with me and watch where your"
                " point lands. The axis is the crease we fold on, not the number we change.",
        },
        {"id": "congruent-requires-same-orientation", "name": "congruent only if positioned the same",
         "topic": "Congruence from rigid motions",
         "tell": "two identical triangles, one turned a quarter turn, called not congruent",
         "detect": ["not congruent", "it is turned", "facing the wrong way"],
         "rule": "They require congruent figures to sit the same way up on the page, so a figure that"
                 " has been rotated or flipped is judged a different shape.",
         "why": "Their earliest matching tasks rewarded exact visual overlap, and congruence is nearly"
                " always first illustrated with pictures drawn in identical orientation, so orientation"
                " quietly joins the definition.",
         "fix": "Trace one triangle onto tracing paper and physically slide, turn, and flip it onto the"
                " other until it sits on top. Those three moves are the whole definition: anything you"
                " can reach by sliding, turning or flipping is congruent, because none of those moves"
                " changes a single length or angle.",
         "say": "You are right that something about these two is different, and naming that difference"
                " matters. Trace the first one for me and then turn your tracing paper until it lands on"
                " the second. If it fits perfectly, tell me which lengths or angles the turning changed.",
        },
        {"id": "ssa-treated-as-congruence", "name": "treating side side angle as a shortcut",
         "topic": "SSS, SAS, ASA, AAS, HL",
         "tell": "two triangles matching in two sides and a non-included angle declared congruent by SSA",
         "detect": ["ssa", "side side angle", "s s a"],
         "rule": "They treat any three matching parts as sufficient for congruence, so two sides and any"
                 " angle counts; the word 'included' is heard as descriptive detail rather than as the"
                 " condition itself.",
         "why": "Four of the five real shortcuts are three-letter strings, so the mind stores the rule"
                " as 'three matching parts' and the letters as bookkeeping, which is an efficient and"
                " usually accurate summary.",
         "fix": "Build the counterexample with straws or a compass: fix the angle and the side beside"
                " it, then swing the third side so it can reach the base in two different places. Two"
                " genuinely different triangles come from the same three measurements, so those three"
                " measurements cannot determine a triangle.",
         "say": "You matched three parts and named them in order, which is exactly the method. Let me"
                " build this one with straws. I am going to keep your three measurements and make two"
                " triangles that are not the same shape. Watch where the swinging side can land.",
        },
        {"id": "diagram-assumed-to-scale", "name": "reading facts off the picture",
         "topic": "Two-column proofs",
         "tell": "in a proof, claiming two segments are equal because they look the same length in the diagram",
         "detect": ["it looks", "they look equal", "you can see it in the picture"],
         "rule": "They accept the appearance of the diagram as a legitimate given, so anything that"
                 " looks equal, parallel, or square becomes a statement in the proof without a reason.",
         "why": "Diagrams are usually drawn accurately, so the eye is nearly always right, and every"
                " earlier year of geometry actively rewarded measuring the picture to answer the"
                " question.",
         "fix": "Show a deliberately distorted diagram where two segments look equal and are not, and"
                " let the ruler settle it. Then set the standing rule for proofs: only tick marks,"
                " stated givens, and previously proven facts may appear as reasons. For each claimed"
                " line, ask which mark tells us that.",
         "say": "Your eye is sharp and in this drawing you are probably right. In a proof we need a"
                " reason a blind person could check. Show me the tick mark or the given that says those"
                " two are equal. If there is not one, we have found the next thing to prove.",
        },
        {"id": "area-scales-linearly", "name": "scaling area by the scale factor",
         "topic": "How area scales",
         "tell": "a figure dilated by scale factor 3 said to have 3 times the area",
         "detect": ["3 times the area", "three times the area", "times 3"],
         "rule": "They apply the scale factor once to every measurement of the figure, so area is"
                 " multiplied by k in the same way that each length is.",
         "why": "For every length in the figure that rule is exactly right, and nothing in the phrase"
                " 'scale factor three' hints that area is built from two lengths multiplied together and"
                " therefore takes the factor twice.",
         "fix": "On grid paper, draw a one by one square and its scale factor three copy, then count"
                " the little squares inside: nine, not three. Repeat with a two by three rectangle to"
                " confirm. Then let them predict what a cube's volume does before you show them.",
         "say": "You applied the scale factor faithfully, and for the sides that is exactly correct."
                " Draw me the unit square and its tripled copy on grid paper, then count the little"
                " squares that fit inside the big one. The count will tell you how area really grows.",
        },
        {"id": "dilation-by-adding", "name": "dilating by adding to the coordinates",
         "topic": "Dilations & scale factor",
         "tell": "dilating (2, 3) by scale factor 2 answered as (4, 5)",
         "detect": ["add 2 to each"],
         "rule": "They apply the scale factor as an amount to add to each coordinate instead of a number"
                 " to multiply by, so the dilation behaves like a translation.",
         "why": "Translations came first in the unit and are performed by adding to coordinates, and in"
                " ordinary English 'make it bigger by two' really does mean add two.",
         "fix": "Plot the original figure, their image, and rays drawn from the centre through each"
                " original point. Under a true dilation every image point sits on its ray, twice as far"
                " out; the added version drifts off the rays and the shape visibly distorts rather than"
                " growing.",
         "say": "You changed both coordinates by the same amount, which keeps things consistent, and"
                " consistency is the right instinct. Draw rays from the origin through your original"
                " points and plot your new points. Tell me whether your new points sit on those rays or"
                " slide off them.",
        },
        {"id": "pythagoras-on-any-triangle", "name": "using Pythagoras on a non-right triangle",
         "topic": "Pythagorean theorem & its converse",
         "tell": "a triangle with sides 5 and 6 and no right angle, third side given as the square root of 61",
         "detect": ["square root of 61", "sqrt(61)"],
         "rule": "They treat a squared plus b squared equals c squared as a general relationship among"
                 " any triangle's three sides, applying it whenever two sides are known and the angle is"
                 " not checked.",
         "why": "It is the first formula that ties a triangle's three sides together, and every"
                " practice problem for a week is a right triangle, so the right angle stops registering"
                " as a condition and becomes background scenery.",
         "fix": "Pin two straws of length 5 and 6 at a vertex and open and close the angle between"
                " them. The third side visibly changes length while the two given sides never do, so no"
                " formula in the two given sides alone can predict it. The right angle is what pins the"
                " opening.",
         "say": "You picked the right formula for the shape of the information you were given, and your"
                " arithmetic is clean. Hold these two straws and open the angle between them wider."
                " Watch the third side while you do it. Now tell me what the formula would have to know"
                " to give one answer.",
        },
        {"id": "leg-found-by-adding", "name": "adding when solving for a leg",
         "topic": "Pythagorean theorem & its converse",
         "tell": "hypotenuse 13 and one leg 5, the other leg given as the square root of 194",
         "detect": ["square root of 194", "sqrt(194)"],
         "rule": "They square the two numbers they were given and add, regardless of which one is the"
                 " hypotenuse, because the remembered form of the theorem is 'square the two you have and"
                 " add them'.",
         "why": "Nearly every practice problem asks for the hypotenuse, so a, b and c become 'first,"
                " second, answer' rather than 'leg, leg, hypotenuse' — a sensible compression that only"
                " fails when the missing side is a leg.",
         "fix": "Make labelling the hypotenuse the required first step: it sits opposite the right"
                " angle and is always the longest side. Then run the sanity check on their answer, about"
                " 13.9, against a hypotenuse of 13. A leg cannot be longer than the hypotenuse, so the"
                " operation must be subtraction.",
         "say": "You set up the theorem correctly and squared both numbers accurately. Look at your"
                " answer next to the thirteen. You have found a side about thirteen point nine long"
                " inside a triangle whose longest side is thirteen. What does that tell us about which"
                " number was the hypotenuse?",
        },
        {"id": "inscribed-angle-equals-arc", "name": "inscribed angle equal to its arc",
         "topic": "Central & inscribed angles",
         "tell": "an inscribed angle on an 80 degree arc answered as 80 degrees",
         "detect": ["80 degrees", "same as the arc", "equal to the arc"],
         "rule": "They apply the central angle relationship to every angle in the circle: the angle"
                 " equals the arc it opens onto, whether its vertex sits at the centre or out on the"
                 " circle.",
         "why": "The central angle case is taught first and is beautifully simple, and vertex position"
                " looks like a detail of where the picture was drawn rather than the thing the whole"
                " rule depends on.",
         "fix": "Draw both angles on the same arc in one circle and measure them with a protractor: the"
                " one with its vertex on the circle reads half. Then slide that vertex around the circle"
                " and re-measure — it stays half, no matter where it goes, which is the surprising and"
                " memorable part.",
         "say": "You connected the angle to its arc, and that link is the whole idea of this unit. Let"
                " me draw the other angle on the same arc, the one with its point at the centre. Measure"
                " both with the protractor and tell me how the two numbers are related.",
        },
        {"id": "midpoint-by-subtracting", "name": "subtracting coordinates to find a midpoint",
         "topic": "Distance & midpoint formulas",
         "tell": "the midpoint of (2, 3) and (8, 7) answered as (6, 4)",
         "detect": ["subtract the coordinates"],
         "rule": "They use the subtract-the-coordinates move from distance and slope for the midpoint as"
                 " well, producing the difference between the two points instead of their average.",
         "why": "Three formulas in one short unit all begin by pairing up the x's and the y's, and two"
                " of the three genuinely start with subtraction, so subtraction becomes the default"
                " opening move.",
         "fix": "Plot both points and their answer: it does not even land on the segment. Then strip"
                " the formula away and ask the plain question — what number is halfway between 2 and 8?"
                " Halfway is an average, so add and halve. Plot the result and see it sit dead centre.",
         "say": "You paired the x's with the x's and the y's with the y's, which is the part students"
                " most often get tangled. Plot your answer on the grid with the two original points. Is"
                " it sitting between them? Now tell me what number is halfway between two and eight.",
        },
        {"id": "area-perimeter-confused", "name": "computing perimeter when asked for area",
         "topic": "Area of polygons & circles",
         "tell": "the area of a 5 by 3 rectangle answered as 16",
         "detect": ["added the sides"],
         "rule": "They choose between adding the sides and multiplying them based on the shape in front"
                 " of them rather than on the question asked, so whichever operation they used most"
                 " recently is the one that fires.",
         "why": "Both are single numbers attached to the same figure, both get called the size of it,"
                " and the two words are introduced in the same lesson with the same picture, so nothing"
                " separates them in memory.",
         "fix": "Insist on units before numbers: sixteen what? Tile the rectangle with unit squares and"
                " count fifteen squares covering it; then lay string around the outside and measure"
                " sixteen units of string. Area covers the inside, perimeter fences the outside, and the"
                " units say which is which.",
         "say": "Your arithmetic on the sides is right, so this is about which question we are"
                " answering. Tell me sixteen what. Then count with me how many little squares it takes"
                " to cover the whole rectangle. One of those numbers fences it, the other one covers it.",
        },
        {"id": "disjoint-called-independent", "name": "treating mutually exclusive as independent",
         "topic": "Independence",
         "tell": "two events that cannot both happen, such as rolling a 2 and rolling a 5 on one die, called independent",
         "detect": ["they cannot both happen", "they do not overlap", "mutually exclusive so independent"],
         "rule": "They read independent as separate, so any two events with no outcomes in common are"
                 " declared independent, and the Venn diagram with no overlap becomes the picture of"
                 " independence.",
         "why": "In everyday English independent does mean unconnected, and two circles drawn apart"
                " look exactly like the picture of unconnectedness, so the word and the diagram"
                " reinforce each other.",
         "fix": "Take the single die: rolling a 2 and rolling a 5 cannot both happen. Now ask what the"
                " chance of a 5 becomes once you know it was not a 2 — it rises from one sixth to one"
                " fifth. Knowing one changed the other, so they are the opposite of independent. Then"
                " check by multiplying the probabilities.",
         "say": "Your reading of the Venn diagram is accurate, those events really do not overlap. Try"
                " this with me. On one die, I tell you the roll was not a two. What is the chance it was"
                " a five now? If that number moved, the two events are talking to each other.",
        },
    ],
    "algebra2": [
        {"id": "absolute-value-one-case-only", "name": "solving an absolute value equation once",
         "topic": "Absolute-value equations & inequalities",
         "tell": "the absolute value of x minus 3 equals 5 answered as x = 8 only",
         "detect": ["just 8", "only 8", "8 is the answer"],
         "rule": "They strip the absolute value bars as if they were parentheses and solve the single"
                 " remaining equation, so only the positive case is ever produced.",
         "why": "The bars look like grouping symbols, and when the quantity inside is positive,"
                " dropping them genuinely changes nothing, so the shortcut is correct in about half of"
                " all the examples they meet.",
         "fix": "Read the bars aloud as distance: how far is x from 3 on the number line? Mark 3 and"
                " step 5 units in each direction, landing on 8 and on negative 2. Two points, so two"
                " answers. Make the number line sketch the required first step before any algebra"
                " happens.",
         "say": "The eight is genuinely one of the answers and your solving was clean. Draw a number"
                " line with me and mark three. Now step five units away from it. How many places did you"
                " land? Distance does not care which direction you walk, and that is the whole idea"
                " here.",
        },
        {"id": "absolute-value-inequality-direction", "name": "using the and form for a greater than",
         "topic": "Absolute-value equations & inequalities",
         "tell": "the absolute value of x is greater than 5 answered as x between -5 and 5",
         "detect": ["between -5 and 5", "-5 < x < 5", "between negative 5 and 5"],
         "rule": "They convert every absolute value inequality into the same sandwich form, with the"
                 " variable trapped between the negative and positive of the number, because that is the"
                 " pattern they practised first.",
         "why": "The less-than case is taught first and its compact double inequality is visually"
                " memorable as THE answer shape for absolute value, so it gets applied to the whole"
                " family.",
         "fix": "Go back to distance: absolute value of x more than 5 asks which numbers sit further"
                " than 5 from zero. Shade a number line and test a specific value like 10 in the"
                " original, then check whether their answer contains it. Greater than gives the two"
                " outside pieces, less than gives the middle.",
         "say": "You produced a clean interval and your endpoints are the right two numbers. Test ten"
                " in the original for me. Does it work? Now check whether ten is inside the interval you"
                " wrote. That mismatch will tell you which part of the number line we actually want.",
        },
        {"id": "completing-square-one-side", "name": "completing the square on one side only",
         "topic": "Completing the square",
         "tell": "x^2 + 6x = 7 rewritten as (x + 3)^2 = 7",
         "detect": ["(x + 3)^2 = 7", "x plus 3 squared equals 7", "still equals 7"],
         "rule": "They add the square of half the middle coefficient to the left side to manufacture the"
                 " perfect square and leave the right side untouched, treating the addition as a"
                 " rewriting step rather than an operation on an equation.",
         "why": "Every earlier factoring move genuinely was a rewrite of one side that left its value"
                " alone; completing the square looks like factoring but is the one step where the"
                " expression's value actually changes.",
         "fix": "Put the balance scale back up: they have dropped nine units into the left pan only."
                " Then check numerically — the solutions of their version do not satisfy the original."
                " Require the words 'add nine to both sides' as a separate visible line before the"
                " factored form is written.",
         "say": "Recognizing that nine is the number that completes the square is the hard part, and"
                " you found it instantly. Now picture the equation as a balance. You just set nine units"
                " into the left pan. What does the right pan need before we go on?",
        },
        {"id": "root-of-negative-as-negative-root", "name": "pulling the minus out from under the radical",
         "topic": "Imaginary & complex numbers",
         "tell": "the square root of negative nine answered as -3",
         "detect": [],
         "rule": "They move the minus sign out from under the radical, so the square root of negative"
                 " nine becomes the negative of the square root of nine.",
         "why": "A minus sign is portable almost everywhere else in algebra, and the answer negative"
                " three does contain both a three and a minus, so it looks like everything in the"
                " problem has been accounted for.",
         "fix": "Check by squaring: negative three times negative three is positive nine, not negative"
                " nine, so it fails its own test. Then ask for ANY real number whose square is negative"
                " and let them come up empty. That emptiness is exactly what the imaginary unit was"
                " invented to fill, giving three i.",
         "say": "You handled the minus sign the way it behaves nearly everywhere else, and your square"
                " root of nine is right. Square your answer and tell me what you get. Then hunt for any"
                " number at all whose square comes out negative. What you find is why this unit exists.",
        },
        {"id": "factor-theorem-sign-flipped", "name": "testing a factor at the wrong value",
         "topic": "Remainder & Factor theorems",
         "tell": "to test whether x + 3 is a factor of a polynomial, they evaluate f(3)",
         "detect": ["f(3)", "plug in 3", "f of 3"],
         "rule": "They substitute the number they can see inside the factor, so x plus 3 gets tested at"
                 " 3, rather than at the value that makes the factor equal zero.",
         "why": "Reading the visible number is an efficient habit that works everywhere else, and for a"
                " factor written with a minus sign the shortcut gives the correct value, which covers"
                " most of the worked examples.",
         "fix": "Ask the one question the theorem is built on: what value of x makes x plus 3 equal"
                " zero? Then test on something already factored, like x^2 + 5x + 6, which is (x + 2)(x +"
                " 3): f(-3) is 0 while f(3) is 30. The zero is the signal, so you have to feed it the"
                " number that produces zero.",
         "say": "You went straight to substitution, which is exactly what the theorem asks for. One"
                " question first: what number would you have to put in for x to make x plus three come"
                " out to zero? Feed the polynomial that number instead and see what happens.",
        },
        {"id": "synthetic-division-skip-missing-term", "name": "omitting missing degrees in division",
         "topic": "Long & synthetic division",
         "tell": "dividing x^3 - 2x + 1 with the coefficient row written as 1, -2, 1",
         "detect": ["there is no x squared", "skip that one"],
         "rule": "They write down only the coefficients that are visible, so a polynomial with a missing"
                 " degree loses a column and every later coefficient shifts into the wrong place.",
         "why": "The instruction really is 'write the coefficients', and a term that is not on the page"
                " does not feel like a coefficient of zero, in the same way that we never write the"
                " missing hundreds in a number.",
         "fix": "Rewrite the polynomial in full with the missing term shown as zero x squared, so every"
                " degree has a column. Compare with place value in ordinary numbers: 105 and 15 are not"
                " the same number, and the zero is doing the work. Then multiply the quotient back to"
                " confirm.",
         "say": "Your setup and your signs are both right, so this is one small bookkeeping point."
                " Write the polynomial out with every power from the highest down to the constant, even"
                " the ones with nothing in front of them. Tell me which power has no term, and what its"
                " coefficient must be.",
        },
        {"id": "cancel-terms-not-factors", "name": "cancelling across a plus sign",
         "topic": "Simplifying & operations",
         "tell": "the quantity x plus 3, all over 3, simplified to x",
         "detect": ["just x", "the 3s cancel", "the threes cancel"],
         "rule": "They cancel any symbol that appears on the top and on the bottom, treating"
                 " cancellation as crossing out matching things rather than dividing a common factor out"
                 " of the entire numerator.",
         "why": "Cancelling genuinely does work that way for factors — 3x over 3 really is x — and the"
                " classroom demonstration is literally the act of crossing out identical symbols, which"
                " is what gets remembered.",
         "fix": "Numbers settle it: 2 plus 3, over 3, is five thirds, not 2. Then define the test out"
                " loud — you may only cancel something that multiplies the WHOLE top. Have them factor"
                " the numerator first every time; if the common piece will not factor out, it may not be"
                " crossed out.",
         "say": "You spotted a three on the top and a three on the bottom, and that pattern really is"
                " worth spotting. Try it with numbers: put two in for x and work out both your version"
                " and the original. Whichever way those two land will tell us when crossing out is"
                " allowed.",
        },
        {"id": "hole-called-asymptote", "name": "calling every denominator zero an asymptote",
         "topic": "Asymptotes & holes",
         "tell": "for (x^2 - 4)/(x - 2), a vertical asymptote reported at x = 2",
         "detect": ["asymptote at x = 2", "vertical asymptote at 2", "asymptote at 2"],
         "rule": "They locate vertical asymptotes by setting the denominator equal to zero before"
                 " simplifying, so a factor that also vanishes in the numerator gets reported as an"
                 " asymptote instead of a hole.",
         "why": "Setting the bottom to zero is a correct and necessary first step, and it gives the"
                " right answer for every already-simplified example; nothing in the look of the"
                " expression flags that a factor is shared.",
         "fix": "Build a table of values approaching 2 from both sides: the outputs march toward 4, not"
                " off to infinity, so nothing is exploding there. Then factor the numerator and cancel"
                " the shared factor to see what is left. The graph has one missing point, an open"
                " circle, not a wall.",
         "say": "Setting the denominator to zero is exactly the right first move, and two is genuinely"
                " a special value here. Make me a table with x at one point nine, one point nine nine,"
                " and two point zero one. If the outputs settle down instead of running away, we are"
                " looking at a hole.",
        },
        {"id": "root-across-a-sum", "name": "square rooting each term of a sum",
         "topic": "Simplifying & rationalizing",
         "tell": "the square root of x^2 + 16 simplified to x + 4",
         "detect": ["x + 4", "x plus 4", "x plus four"],
         "rule": "They apply the radical to each term inside separately, treating the square root as"
                 " something that distributes over addition the way it genuinely does over"
                 " multiplication.",
         "why": "The square root of 4x squared really is 2x, so the root does pass through products; a"
                " sum under the radical looks like the same situation and invites the same move.",
         "fix": "Numbers first: the square root of 9 plus 16 is 5, while 3 plus 4 is 7. Then make it"
                " geometric — those are the sides of a 3, 4, 5 right triangle, and walking the two legs"
                " is always longer than cutting straight across on the hypotenuse. The radical is that"
                " shortcut.",
         "say": "You are borrowing a rule that is genuinely true for multiplication, and you applied it"
                " neatly. Test it with numbers: take the square root of nine plus sixteen, then"
                " separately add the square root of nine to the square root of sixteen. Tell me the two"
                " answers you get.",
        },
        {"id": "extraneous-solutions-kept", "name": "keeping every solution after squaring",
         "topic": "Solving radical equations",
         "tell": "the square root of x plus 6 equals x, answered as x = 3 and x = -2",
         "detect": ["x = -2", "negative 2 works"],
         "rule": "They treat squaring both sides as a reversible move like adding or multiplying, so"
                 " every solution the squared equation produces is accepted as a solution of the"
                 " original.",
         "why": "Every operation they have ever applied to an equation has been reversible, so the idea"
                " that a legal step could manufacture extra solutions has no precedent, and the algebra"
                " looks no different when it happens.",
         "fix": "Substitute negative two back into the ORIGINAL: the square root of four is 2, not"
                " negative 2, so it fails. Then graph both sides — the curve and the line cross exactly"
                " once. Squaring erased the sign information, which is what let the second value sneak"
                " in. Make checking a required final line.",
         "say": "Both of those values genuinely solve the squared equation, so your algebra is sound."
                " Put negative two back into the original, the one with the radical still in it, and"
                " tell me what each side comes out to. Squaring can invent extra answers, so we always"
                " check.",
        },
        {"id": "negative-exponent-as-negative-number", "name": "reading a negative exponent as a negative",
         "topic": "nth roots & rational exponents",
         "tell": "2 to the power negative 3 answered as -8",
         "detect": [],
         "rule": "They carry the minus sign down from the exponent onto the value, so a negative"
                 " exponent makes the answer negative instead of making it a reciprocal.",
         "why": "In every other position a minus sign really does negate whatever it sits in front of,"
                " and exponents were first defined as repeated multiplication, where a negative count"
                " has no meaning to reason from.",
         "fix": "Walk the pattern down a column: 2 cubed is 8, 2 squared is 4, 2 to the first is 2, 2"
                " to the zero is 1. Each step down halves the value. Ask them to continue it themselves"
                " — one half, one quarter, one eighth. The sequence never crosses into negative numbers,"
                " it only gets smaller.",
         "say": "You noticed the minus sign and refused to ignore it, which is the right instinct."
                " Build this column with me: two cubed, two squared, two to the first, two to the zero."
                " Say what happens to the value at each step down. Now keep going two more steps and"
                " tell me where you land.",
        },
        {"id": "log-of-a-sum-split", "name": "splitting the log of a sum",
         "topic": "The log laws & change of base",
         "tell": "the log of the quantity x plus y rewritten as log x plus log y",
         "detect": ["log x + log y", "log of x plus log of y", "split the log"],
         "rule": "They apply the product law to sums: since the log of a product equals the sum of the"
                 " logs, any plus sign inside a logarithm is read as permission to break the expression"
                 " apart.",
         "why": "The real law does connect logs and addition, so sums and logarithms are genuinely"
                " related; the only difference is WHERE the plus sits — inside the log or between two"
                " logs — and both look alike at a glance.",
         "fix": "Numbers decide it: the log of 10 plus 90 is the log of 100, which is 2, while the log"
                " of 10 plus the log of 90 is about 2.95. Then have them circle the plus sign in each"
                " version. Inside the parentheses means the addition happens first, to the inputs, and"
                " cannot be pulled out.",
         "say": "You are using a real log law, and it is one of the most useful ones. Try it on"
                " numbers: take the log of ten plus ninety, then separately add the log of ten to the"
                " log of ninety. Compare. Then circle where the plus sign is sitting in each one.",
        },
        {"id": "exponential-solved-by-dividing", "name": "dividing by the base to solve",
         "topic": "Solving exponential & log equations",
         "tell": "2 to the x equals 32 answered as x = 16",
         "detect": ["x = 16", "divide by 2", "32 divided by 2"],
         "rule": "They solve for the exponent with the same inverse-operation move used for a"
                 " coefficient: the 2 appears to be multiplying, so they divide both sides by 2.",
         "why": "'Do the opposite operation' has been the single most reliable rule of every equation"
                " so far, and 2x and 2 to the x differ only by the height of one small symbol.",
         "fix": "Have them check their answer by computing 2 to the sixteenth — a number in the tens of"
                " thousands, nowhere near 32. Then build the ladder of powers of 2 and find 32 sitting"
                " at the fifth rung. The exponent is a count of multiplications, and the tool that"
                " undoes it is the logarithm.",
         "say": "Undoing the operation is exactly the right strategy, so the plan is sound. Check your"
                " answer for me: what is two multiplied by itself sixteen times, roughly? Now list the"
                " powers of two until you hit thirty two, and tell me which rung it lands on.",
        },
        {"id": "arithmetic-rule-off-by-one", "name": "using n instead of n minus one",
         "topic": "Explicit & recursive rules",
         "tell": "for 4, 7, 10, ... the explicit rule written as 4 + 3n, which gives 7 for the first term",
         "detect": ["4 + 3n", "four plus three n", "3n + 4"],
         "rule": "They build the explicit rule as first term plus common difference times n, counting"
                 " one step of growth for the first term instead of zero.",
         "why": "The first term genuinely is the starting point and n genuinely counts the terms, so it"
                " feels as though term one should already have taken one step; the mismatch is invisible"
                " unless the rule is tested at n equal to one.",
         "fix": "Test the rule at n equal to 1 against the actual list and watch it produce the second"
                " term. Then build a table with an extra column headed 'steps taken': term one has taken"
                " zero steps, term two has taken one. That column is the n minus one, and it makes the"
                " shift a fact rather than a rule.",
         "say": "Your starting value and your common difference are both correct, so the shape of the"
                " rule is right. Put one in for n and tell me which term of the list comes out. If it"
                " hands you the second term, we know exactly how far the rule has drifted.",
        },
        {"id": "sine-read-as-x-coordinate", "name": "reading sine off the x coordinate",
         "topic": "Radians & the unit circle",
         "tell": "at the point with coordinates root three over two and one half, sine reported as root three over two",
         "detect": ["square root of 3 over 2", "sqrt(3)/2", "the x coordinate"],
         "rule": "They take the first coordinate of the unit circle point as the sine, since sine is the"
                 " first function named and x is the first coordinate listed.",
         "why": "Every ordered pair they have read for years goes x then y, and sine comes first in"
                " every list of the ratios, so lining the two firsts up is a natural and orderly move.",
         "fix": "Go back to SOH: sine is opposite over hypotenuse, and on the unit circle the side"
                " opposite the angle is the VERTICAL one, with a hypotenuse of one. So sine is height"
                " and cosine is how far across. Check it at zero degrees, where the point is one comma"
                " zero and the height is flat.",
         "say": "You read the point off the circle correctly, which is most of the work. Drop a"
                " vertical line from that point to the horizontal axis and look at the little right"
                " triangle. Which of its sides is opposite the angle, the standing one or the lying down"
                " one? Sine is that one.",
        },
        {"id": "conditional-probability-reversed", "name": "swapping the two conditional probabilities",
         "topic": "Conditional probability",
         "tell": "told that 90 percent of sick people test positive, they conclude 90 percent of people testing positive are sick",
         "detect": ["so 90 percent of positives", "it is the same 90", "same thing either way"],
         "rule": "They treat the probability of A given B and the probability of B given A as the same"
                 " quantity, since both describe the same pair of events and everyday language does not"
                 " mark the direction.",
         "why": "English conditionals are genuinely loose about direction, and most classroom problems"
                " only ever ask for the conditional in the direction the information was given, so the"
                " reverse never gets tested.",
         "fix": "Build a two-way table with real counts: out of 1000 people, 10 are sick and 9 of them"
                " test positive, but 99 of the healthy 990 also test positive. So of 108 positives, only"
                " 9 are sick. The two fractions have visibly different denominators, which is the whole"
                " point.",
         "say": "You held onto the ninety percent correctly, and it is the key number here. Let us"
                " build a table for a thousand people and count the positives. Watch which group each"
                " fraction is measured out of, because the group on the bottom changes when we turn the"
                " question around.",
        },
    ],
    "precalc": [
        {"id": "composition-as-multiplication", "name": "reading f(g(x)) as f times g",
         "topic": "composition of functions",
         "tell": "with f(x)=x+1 and g(x)=x^2, f(g(2)) answered as 3 times 4, i.e. 12, instead of 5",
         "detect": ["f of x times g of x", "multiply the two functions", "times g of"],
         "rule": "They read the notation f(g(x)) as a product, applying the same 'juxtaposition means"
                 " multiply' rule that governs 3x and (x+1)(x-2).",
         "why": "Everywhere else in algebra a symbol written next to a parenthesis means"
                " multiplication. Function notation is the one place it does not, and nothing visual"
                " marks the difference.",
         "fix": "Do it numerically both ways with small numbers: g(2) is 4, then f(4) is 5, while their"
                " rule gives 3 times 4, which is 12. Then show the machine picture, the output of g"
                " becoming the input of f, and have them run f(g(3)) aloud before writing anything down.",
         "say": "Your arithmetic is right for what you wrote. Let us run it as a machine instead. Put"
                " two into g first and tell me what comes out. Then feed that number into f. Tell me"
                " both numbers and we will compare them to what you got.",
        },
        {"id": "inverse-as-reciprocal", "name": "reading f inverse as one over f",
         "topic": "inverse functions",
         "tell": "for f(x)=2x+6, the inverse given as 1/(2x+6) instead of (x-6)/2",
         "detect": ["one over f of x", "1/f(x)", "reciprocal of the function"],
         "rule": "They apply the exponent rule x^-1 = 1/x to the superscript in f^-1, so the inverse"
                 " function becomes the reciprocal of the output.",
         "why": "The notation reuses the exponent -1, which everywhere else genuinely does mean"
                " reciprocal. Reading it that way is consistent, just not what this symbol means.",
         "fix": "Have them test both candidates on a number: f(2) is 10, so the inverse must send 10"
                " back to 2, while 1/(2x+6) sends 10 to one twenty-sixth. Then define the inverse as the"
                " undo machine and rebuild it by solving x = 2y + 6 for y.",
         "say": "The exponent reading is a fair guess, and it is the one the notation invites. Let us"
                " test it. Feed two into f and tell me the output. Now the inverse has one job, send"
                " that output back to two. Try your version on it.",
        },
        {"id": "inside-shift-direction", "name": "shifting inside the function the wrong way",
         "topic": "parent functions & transformations",
         "tell": "y = (x - 3)^2 graphed shifted three units to the left",
         "detect": ["shifts left", "minus so it goes left", "moves left three"],
         "rule": "They read the sign of the number inside as a direction, so a minus inside the"
                 " parentheses means move in the negative direction, to the left.",
         "why": "Outside changes really do work that way, since y = f(x) - 3 moves the graph down."
                " Inside changes are the one place the sign reverses, and no rule they were handed flags"
                " the exception.",
         "fix": "Pick the vertex and test it: (x - 3)^2 is zero when x is 3, so the bottom of the"
                " parabola sits at 3, to the right. One computed point settles it. Then generalise, the"
                " inside number answers what x must be for the machine to see zero.",
         "say": "Good instinct to look at the sign, that is exactly where the information lives. Now"
                " find the one x value that makes the inside zero. That x is where the vertex sits. Tell"
                " me that number and then tell me which side of the origin it is on.",
        },
        {"id": "asymptote-never-crossed", "name": "treating an asymptote as an untouchable wall",
         "topic": "vertical, horizontal & oblique asymptotes",
         "tell": "asked whether y = 2x/(x^2+1) ever meets its horizontal asymptote y = 0, answered never, though it is exactly 0 at x = 0",
         "detect": ["never touches", "can never cross", "gets close but never reaches"],
         "rule": "They treat an asymptote as a barrier the graph is forbidden to touch anywhere, rather"
                 " than as a statement about end behaviour only.",
         "why": "Every first example is a vertical asymptote, where the curve genuinely cannot touch"
                " the line, and the word 'approaches' sounds like a permanent prohibition.",
         "fix": "Graph y = 2x/(x^2+1) with them and evaluate it at x = 0, landing exactly on the"
                " asymptote. Then restate the horizontal asymptote as a claim about what happens far"
                " out, and check it numerically at x = 100 and x = 1000.",
         "say": "You have the far-away behaviour exactly right, the curve does settle toward that line."
                " Now try one number close in. Evaluate this function at zero and tell me the height you"
                " get. Then we will decide together whether the line is a wall or a destination.",
        },
        {"id": "even-multiplicity-crosses", "name": "every real zero crosses the x-axis",
         "topic": "end behavior & multiplicity",
         "tell": "y = (x-1)^2 (x+2) sketched cutting through the axis at x = 1 instead of touching",
         "detect": ["it crosses at both zeros", "crosses there too", "goes through the axis at one"],
         "rule": "They treat 'zero of the function' as meaning 'sign change', so every factor set to"
                 " zero produces a crossing regardless of its exponent.",
         "why": "Every zero in their earlier work came from distinct linear factors, where crossing"
                " always happens. Multiplicity is extra information that the word 'zero' does not carry"
                " by itself.",
         "fix": "Have them evaluate the function at 0.9 and at 1.1 and read the signs: both come out"
                " the same, so the curve returned rather than passed through. Then tie that to the"
                " squared factor, which can never change sign.",
         "say": "You found both zeros correctly, that is the hard part. Now test the sign just below"
                " one and just above one, say at nine tenths and at one and one tenth. Tell me whether"
                " the two answers have the same sign or opposite signs.",
        },
        {"id": "log-of-a-sum", "name": "splitting the log of a sum",
         "topic": "the log laws & change of base",
         "tell": "log(8 + 2) rewritten as log 8 + log 2, giving log 80 instead of 1",
         "detect": ["log x plus log", "log of a plus log of b", "split the log"],
         "rule": "They apply the product law log(ab) = log a + log b to a sum inside the log, treating"
                 " the log as something that distributes over whatever is inside.",
         "why": "The product law does turn an inside operation into an outside plus, so the shape 'one"
                " log of two things becomes two logs added' is what was retained. The difference between"
                " the inside operations is easy to lose.",
         "fix": "One arithmetic check kills it: log base ten of (8+2) is log 10, which is 1, while log"
                " 8 + log 2 is log 80, which is not. Have them run both on the calculator, then restate"
                " the law with the words 'log of a product' every single time.",
         "say": "Take base ten and try it with numbers we know. Eight plus two inside the log gives log"
                " of ten, and you know that value. Now compute log eight plus log two on your"
                " calculator. Read me both numbers and tell me what you notice.",
        },
        {"id": "degrees-for-radians", "name": "reading a radian measure as degrees",
         "topic": "radians & the unit circle",
         "tell": "cos(2) evaluated as 0.999, the cosine of two degrees, instead of -0.416",
         "detect": ["i had it in degrees"],
         "rule": "They assume any bare number handed to a trig function is a degree measure, so an angle"
                 " given in radians is evaluated in degree mode.",
         "why": "Degrees came first and dominated years of geometry, while radians arrive as a"
                " conversion exercise rather than as the default unit everything later will use.",
         "fix": "Have them locate 2 on the unit circle against pi, about 3.14: two is past a quarter"
                " turn, so the point is in the second quadrant and the cosine must be negative. A"
                " positive answer near 1 is impossible. Then have them check the calculator mode.",
         "say": "Your calculator work is clean, so let us sanity check the angle itself. Pi is about"
                " three point one four, so where does two sit compared to a quarter turn? Which quadrant"
                " is that, and what sign should cosine have there?",
        },
        {"id": "reference-angle-sign-dropped", "name": "keeping the reference angle's sign",
         "topic": "exact values & reference angles",
         "tell": "cos(150 degrees) given as positive root 3 over 2 instead of negative root 3 over 2",
         "detect": ["positive root three over two", "plus root three over two", "positive square root of three over two"],
         "rule": "They find the reference angle, look up its exact value, and report that value"
                 " unchanged, treating the reference angle as fully equivalent to the original angle.",
         "why": "The reference angle really does give the correct magnitude, and that is the hard"
                " computational step. The quadrant sign is separate bookkeeping that the lookup step"
                " never reminds them about.",
         "fix": "Have them mark 150 degrees on the unit circle and read the x-coordinate directly: it"
                " lies left of centre, so it is negative. Then make the two-step habit explicit,"
                " magnitude from the reference angle, sign from the quadrant, said aloud in that order.",
         "say": "The magnitude is exactly right, root three over two is the correct size. Now put the"
                " angle on the unit circle and point at it. Is that point to the left or the right of"
                " centre? Cosine is that horizontal coordinate, so what sign do we need?",
        },
        {"id": "sine-distributes-over-sum", "name": "distributing sine across a sum",
         "topic": "sum, difference & double-angle formulas",
         "tell": "sin(30 + 60) evaluated as sin 30 + sin 60, about 1.37, instead of 1",
         "detect": ["sin a plus sin b", "sine of a plus sine of b"],
         "rule": "They treat sin as a quantity multiplying its argument, so sin(A+B) expands by the"
                 " distributive law into sin A + sin B.",
         "why": "The notation looks exactly like a coefficient in front of a parenthesis, and"
                " distributing over a parenthesis is the most heavily drilled move in all of algebra.",
         "fix": "Use angles whose sines they know: sin(30 + 60) is sin 90, which is 1, while sin 30 +"
                " sin 60 is 0.5 plus about 0.866. Their rule also predicts sines above one, which the"
                " unit circle forbids. Then derive the real sum formula from that example.",
         "say": "Try it where we know every value. Thirty plus sixty gives ninety, and you know the"
                " sine of ninety. Now add the sine of thirty and the sine of sixty separately. One of"
                " those answers is bigger than one, and the unit circle says that cannot happen.",
        },
        {"id": "only-the-calculator-angle", "name": "reporting only the principal solution",
         "topic": "solving trig equations & inverse trig",
         "tell": "sin x = 1/2 on [0, 2pi) answered as pi/6 only, with 5pi/6 missing",
         "detect": ["just pi over six", "only pi over six", "that is the only answer"],
         "rule": "They treat the inverse sine key as returning the complete solution set, so one angle"
                 " is the answer rather than one representative of a family.",
         "why": "For every equation before this one, applying the inverse operation produced the whole"
                " answer. Nothing about arcsine announces that it deliberately returns a single branch.",
         "fix": "Draw the line y = 1/2 across one period of the sine graph and count intersections"
                " together: two per period, not one. Then have them get the second angle from symmetry"
                " and add multiples of the period to generate the rest.",
         "say": "Pi over six is correct, and it is the one the calculator hands you. Now draw the sine"
                " curve for one full turn and lay a horizontal line at one half across it. Count how"
                " many times the line meets the curve, and tell me the number.",
        },
        {"id": "law-of-sines-single-triangle", "name": "stopping at one triangle in the ambiguous case",
         "topic": "Law of Sines & the ambiguous case",
         "tell": "given a = 8, b = 10, A = 40 degrees, only B = 53.5 degrees reported, missing 126.5",
         "detect": ["only one triangle", "only one answer for b"],
         "rule": "They accept the inverse sine output as the unique angle, treating an angle in a"
                 " triangle as fully determined once its sine is known.",
         "why": "In right triangle work the inverse sine always did give the one correct angle, and"
                " nothing in the side-side-angle setup signals that a second, obtuse angle shares that"
                " same sine.",
         "fix": "Have them compute the sine of 126.5 degrees and see it match, then check that 40 plus"
                " 126.5 is still under 180, so the second triangle genuinely exists. Swinging the side"
                " with a compass makes the two closing positions visible.",
         "say": "That angle is right, and it is one of the answers. Take one hundred eighty minus your"
                " angle and find the sine of that. Compare it with the sine you started from. If they"
                " match, ask whether that second angle still fits inside a triangle with forty degrees.",
        },
        {"id": "parametric-domain-dropped", "name": "keeping the whole curve after eliminating t",
         "topic": "parametric equations",
         "tell": "x = cos t, y = sin t for 0 <= t <= pi graphed as the full unit circle instead of the upper semicircle",
         "detect": ["the whole circle", "full circle", "all of the parabola"],
         "rule": "They treat eliminating the parameter as an equivalence, so the Cartesian equation"
                 " replaces the parametric pair completely and the restriction on t is discarded with it.",
         "why": "The elimination algebra is genuinely correct, and nothing in the resulting equation"
                " carries a memory of t. The lost information lives in the range of t, which never"
                " appears in the final equation.",
         "fix": "Have them plot the points at t = 0, pi/2 and pi, then ask which value of t could ever"
                " produce a point below the axis. Add the habit of writing the endpoint points and the"
                " resulting domain and range restriction beside the Cartesian equation.",
         "say": "Your elimination is correct, that equation really does describe the curve. Now plug in"
                " t of zero, then pi over two, then pi, and mark those three points. Then tell me which"
                " value of t could ever land you below the horizontal axis.",
        },
        {"id": "every-infinite-series-sums", "name": "summing a divergent geometric series",
         "topic": "finite & infinite series",
         "tell": "3 + 6 + 12 + 24 + ... summed as 3/(1-2), reported as -3",
         "detect": ["minus three for the sum"],
         "rule": "They treat a/(1-r) as the formula for any infinite geometric series, applying it"
                 " without testing whether the absolute value of r is less than one.",
         "why": "It is presented as the infinite series formula, and formulas in this course have not"
                " previously come with admission requirements. The condition reads like a footnote next"
                " to a memorable result.",
         "fix": "Have them add the first four terms to get 45, then ask how a running total of positive"
                " numbers could ever arrive at a negative answer. That contradiction is enough. Then"
                " attach the ratio check to the formula so it always runs before the substitution.",
         "say": "Notice something about your answer before we touch the formula. Every term you are"
                " adding is positive, and your total came out negative. Add the first four terms by hand"
                " and tell me the running total. Then we will look at what the formula requires.",
        },
        {"id": "limit-is-the-value", "name": "reading the limit as the value at the point",
         "topic": "limits from tables & graphs",
         "tell": "a graph with a hole at (2, 3) and a solid dot at (2, 5) gives a limit of 5 as x approaches 2, instead of 3",
         "detect": ["the value at two", "read off the dot", "plug in the number"],
         "rule": "They evaluate a limit by substituting the point, defining the limit as f(c) rather"
                 " than as the height the nearby values close in on.",
         "why": "Substitution gives the right answer for every polynomial they have ever met, so it has"
                " never once failed them. The distinction only surfaces at a hole or a jump.",
         "fix": "Cover the point itself with a finger and have them read the graph in from the left and"
                " from the right, reporting the height the curve heads toward. Then uncover it, show the"
                " dot sitting elsewhere, and move the dot to show neither approach changes.",
         "say": "Put your finger over the point itself so you cannot see it. Now walk in from the left"
                " along the curve and tell me what height you are heading toward, then do the same from"
                " the right. Those two numbers are what the limit asks about.",
        },
    ],
    "calculus": [
        {"id": "hole-means-no-limit", "name": "a hole means the limit fails",
         "topic": "limits from tables & graphs",
         "tell": "for f(x) = (x^2-4)/(x-2), the limit as x approaches 2 answered 'does not exist' because f(2) is undefined, instead of 4",
         "detect": ["undefined so no limit", "dne because it is undefined", "there is a hole so dne"],
         "rule": "They require the function to be defined at c before a limit can exist, so a removable"
                 " discontinuity is treated as a fatal obstruction.",
         "why": "It is a reasonable reading of 'the limit of the function at 2' as being a claim about"
                " the function at 2, and every worked example before this one had a value there.",
         "fix": "Have them build a table at 1.9, 1.99, 2.01 and 2.1 and watch the outputs close in on"
                " 4. The limit is a statement about the neighbours, and the missing point contributes"
                " nothing. Then cancel the factor and confirm the same 4.",
         "say": "You are right that the function has nothing at two, that is a real observation. Now"
                " build me a small table, one point nine, one point nine nine, then two point zero one."
                " Tell me the outputs and where they are heading.",
        },
        {"id": "continuous-implies-differentiable", "name": "unbroken graph means a derivative exists",
         "topic": "continuity",
         "tell": "asked for the derivative of the absolute value of x at 0, answered 0 because the graph is connected there",
         "detect": ["it is continuous so it is differentiable", "the graph is connected so", "no break so there is a derivative"],
         "rule": "They treat continuity and differentiability as the same property, so any graph they"
                 " can draw without lifting the pencil is assumed to have a tangent line everywhere.",
         "why": "Everything smooth is continuous, and nearly every function in the course is both."
                " Continuity is the property they got a test for first, so it stands in for smoothness.",
         "fix": "Have them find the slope just left of zero, which is -1, and just right, which is +1,"
                " then ask what single number the tangent slope could be. The corner cannot choose, so"
                " no derivative exists while the function stays perfectly continuous.",
         "say": "You are right that the graph never breaks. Now tell me the slope of the left branch,"
                " then the slope of the right branch. If the tangent at zero has to be one single"
                " number, which of your two would it be?",
        },
        {"id": "power-rule-on-exponentials", "name": "using the power rule on an exponential",
         "topic": "the power rule",
         "tell": "d/dx of 2^x answered as x times 2^(x-1)",
         "detect": ["x times 2 to the x minus 1", "x*2^(x-1)", "bring the x down"],
         "rule": "They match the shape 'base with an exponent' to the power rule and bring the exponent"
                 " down, without checking which of the two positions holds the variable.",
         "why": "The power rule is the most reliable tool they own, and x^n and n^x look like the same"
                " small tower. The rule is stored as a visual pattern rather than as a statement about"
                " where the variable sits.",
         "fix": "Have them tabulate 2^x at x = 0, 1, 2, 3 and see it doubling, then tabulate their"
                " formula and see it give zero at x = 0 where the real curve is visibly rising. Then"
                " name the test aloud, variable in the base versus variable in the exponent.",
         "say": "Say out loud which part of that expression holds the x, the bottom or the top. Then"
                " test your formula at x of zero and tell me what it gives. Look at the graph of two to"
                " the x at zero. Is it flat there?",
        },
        {"id": "average-rate-as-instantaneous", "name": "using average rate as the rate at an instant",
         "topic": "average vs instantaneous rate",
         "tell": "a car covers 120 miles in 2 hours, so its speed at the one-hour mark is reported as 60 miles per hour",
         "detect": ["so the speed at that moment is", "total distance over total time", "sixty at that instant"],
         "rule": "They compute the rate over a whole interval and assign it to a single moment inside"
                 " that interval, treating average rate and instantaneous rate as the same number.",
         "why": "For a constant rate the two genuinely are equal, and every rate problem in earlier"
                " courses had a constant rate. The units, miles per hour, describe both, so the language"
                " never separates them.",
         "fix": "Ask what the speedometer read while the car sat at a red light, zero, with the trip"
                " average still 60. That single image separates the two ideas. Then shrink the interval"
                " around the one-hour mark and watch the average move.",
         "say": "Sixty is exactly right for the whole trip. Now picture the same drive with one red"
                " light in the middle. What does the speedometer read while the car is stopped? And what"
                " is the average for the trip still equal to?",
        },
        {"id": "tangent-touches-once", "name": "a tangent line may touch only once",
         "topic": "tangent lines",
         "tell": "the tangent to y = sin x at pi/2 is y = 1, but it is rejected as not a tangent because the line meets the curve again at 5pi/2",
         "detect": ["it touches twice", "that is a secant not a tangent", "it hits the curve again"],
         "rule": "They define a tangent globally as a line meeting the curve at exactly one point and"
                 " staying on one side of it, the circle definition, rather than locally as the line"
                 " matching the slope at a chosen point.",
         "why": "The first tangent they ever met was tangent to a circle, where one-point contact is"
                " exactly right and the picture is vivid. Nothing replaces that picture when the"
                " definition quietly changes.",
         "fix": "Draw y = x^3 - 3x with its tangent at x = 1, which crosses the curve again further"
                " along, and check the slope still matches at the point of tangency. Then say the"
                " working definition every time, same point, same slope, local only.",
         "say": "Your line has the right slope at the right point, so hold on to it. The circle picture"
                " is what is arguing with you. Tangency here is only a claim about the one point we"
                " chose. Ask yourself, does the slope match there? Yes or no.",
        },
        {"id": "product-differentiated-factorwise", "name": "differentiating a product factor by factor",
         "topic": "product rule",
         "tell": "d/dx of x^2 times sin(x) answered as 2x times cos(x)",
         "detect": ["2x cos x", "two x cosine x", "2x*cos(x)"],
         "rule": "They differentiate each factor separately and multiply the results, extending the"
                 " genuine linearity of the derivative over sums to products as well.",
         "why": "Differentiation really does go term by term across a plus sign, and that is drilled"
                " hard and early. Nothing in the notation signals that products behave differently.",
         "fix": "Test the rule on x times x. Their method gives 1 times 1, which is 1, but x times x is"
                " x^2, whose derivative is 2x. One counterexample they verify in five seconds kills the"
                " rule permanently, and the same example builds the product rule.",
         "say": "Let us test your rule on something we can check both ways. Take x times x. Your rule"
                " gives one times one. But x times x is x squared, and we both know that derivative. Try"
                " it and tell me what you get.",
        },
        {"id": "chain-inner-derivative-dropped", "name": "dropping the inner derivative",
         "topic": "the chain rule",
         "tell": "d/dx of (x^2+1)^5 answered as 5(x^2+1)^4, with the factor of 2x missing",
         "detect": ["five times x squared plus one to the fourth", "5(x^2+1)^4", "just the outside"],
         "rule": "They apply the outer rule to the whole expression and stop, treating whatever sits"
                 " inside the parentheses as if it were a bare x.",
         "why": "For years the inside genuinely was x, so differentiating the outer shell was the"
                " entire job. The chain rule adds a step that the written expression does not visibly"
                " demand.",
         "fix": "Have them expand (2x+1)^2 into 4x^2+4x+1 and differentiate that, getting 8x+4, then"
                " compare with their shell-only 2(2x+1). The gap between the two answers is exactly the"
                " inner derivative, and they produced both numbers themselves.",
         "say": "The outside is handled perfectly. Now try a case we can expand. Square the quantity"
                " two x plus one by hand, differentiate the expanded version, and then differentiate it"
                " your way. Read me both answers and tell me the factor between them.",
        },
        {"id": "implicit-forgets-dydx", "name": "differentiating y as if it were a constant",
         "topic": "implicit differentiation",
         "tell": "x^2 + y^2 = 25 differentiated to 2x + 2y = 0, with the dy/dx factor on the y term missing",
         "detect": ["2x plus 2y equals zero", "2x + 2y = 0", "no dy dx on the y"],
         "rule": "They apply the power rule to y as though y were an independent variable, so no"
                 " chain-rule factor appears when differentiating with respect to x.",
         "why": "The power rule is symmetric in appearance, since x^2 and y^2 look identical, and 'with"
                " respect to x' is easy to hear as an instruction about which letter to watch rather"
                " than about what depends on what.",
         "fix": "Have them literally rewrite the equation as x^2 + [f(x)]^2 = 25, where the chain rule"
                " is unavoidable. Once f'(x) appears on the page, rename it dy/dx, and the factor stops"
                " going missing.",
         "say": "The x term is perfect. Now rewrite the y as f of x everywhere and look at the second"
                " term again. It is a function inside a square. Which rule does that shape ask for, and"
                " what extra factor does it bring?",
        },
        {"id": "related-rates-early-substitution", "name": "substituting the moment before differentiating",
         "topic": "related rates",
         "tell": "in the sliding ladder problem, x = 6 is substituted into x^2 + y^2 = 100 before differentiating, so the derivative collapses to 0 = 0",
         "detect": ["i plugged in six first", "zero equals zero", "it all went to zero"],
         "rule": "They treat the values given at the instant as fixed features of the setup and"
                 " substitute them into the relation before differentiating it.",
         "why": "In every earlier problem, substituting given numbers as early as possible was"
                " efficient and correct. Nothing in the wording distinguishes a quantity that is"
                " momentarily 6 from one that is permanently 6.",
         "fix": "Point at what the substitution did: it froze a moving side into a number, and frozen"
                " things have derivative zero. Then enforce the order out loud, relation first,"
                " differentiate second, substitute the instant last, and re-run the ladder that way.",
         "say": "Look at what your equation says after you substituted. It describes one frozen"
                " photograph, and nothing in a photograph moves. Put the six back as x, differentiate"
                " first, and only then let x be six. Try that order and read me the result.",
        },
        {"id": "negative-acceleration-means-slowing", "name": "negative acceleration read as slowing down",
         "topic": "position, velocity & acceleration",
         "tell": "with velocity -3 and acceleration -2, the object reported as slowing down when it is speeding up",
         "detect": ["negative so it is slowing", "slowing down because acceleration is negative", "it is decelerating"],
         "rule": "They read the sign of acceleration as the direction of the speed change, so negative"
                 " acceleration always means the object is losing speed.",
         "why": "In the great majority of textbook examples the motion is in the positive direction,"
                " where negative acceleration does slow things down. The rule works right up until"
                " velocity turns negative.",
         "fix": "Have them list the velocity at successive times as it runs -3, -5, -7 and then read"
                " off the speeds, which are growing while both signs stay negative. Then state the real"
                " test, same signs means speeding up, opposite signs means slowing down.",
         "say": "Write down the velocity a second later, then a second after that, as the acceleration"
                " keeps pulling it down. Read me the three velocities, then read me their speeds"
                " ignoring sign. Are those speeds growing or shrinking?",
        },
        {"id": "critical-point-always-extremum", "name": "every critical point is a max or min",
         "topic": "critical points",
         "tell": "for f(x) = x^3, x = 0 reported as a minimum because the derivative is zero there",
         "detect": ["it is a minimum at zero", "so there is a max or min there", "derivative is zero so it is an extremum"],
         "rule": "They treat f'(c) = 0 as the definition of an extremum rather than as a necessary"
                 " condition that still has to be tested.",
         "why": "Every worked example that began with 'set the derivative to zero' ended in a maximum"
                " or a minimum, so the step and the conclusion fused. The word 'critical' also sounds"
                " like a verdict.",
         "fix": "Have them evaluate x^3 at -1, 0 and 1 and watch the values climb straight through the"
                " flat spot. Then make the sign chart of f' a compulsory second step, since here f' is"
                " positive on both sides and never changes sign.",
         "say": "Finding that the derivative vanishes at zero is exactly the right first step. Now"
                " check the sign of the derivative just left of zero and just right of zero. If both"
                " come out positive, is the function turning around or just pausing?",
        },
        {"id": "antiderivative-is-unique", "name": "the antiderivative is one single function",
         "topic": "+ C and initial conditions",
         "tell": "the integral of 2x written as x^2 with no constant, so the condition y(0) = 5 cannot be satisfied",
         "detect": ["x squared, that is it", "no c needed", "i do not need the constant"],
         "rule": "They treat antidifferentiation as an inverse with a single output, the way squaring"
                 " and square rooting undo each other, so a whole family of answers collapses to its"
                 " simplest member.",
         "why": "Every operation they have inverted so far returned one result, and x^2 really is an"
                " antiderivative. The lost constant leaves no trace in the derivative, so nothing"
                " prompts them to restore it.",
         "fix": "Have them differentiate x^2, then x^2 + 5, then x^2 - 17, and see all three give 2x,"
                " so the derivative cannot tell them apart. Then hand them an initial condition and let"
                " them discover it is unanswerable without the constant.",
         "say": "Differentiate x squared for me, then x squared plus five, then x squared minus"
                " seventeen. Read me all three derivatives. If the derivative cannot tell those"
                " functions apart, how many antiderivatives does two x actually have?",
        },
        {"id": "product-integrated-factorwise", "name": "integrating a product factor by factor",
         "topic": "basic antiderivatives",
         "tell": "the integral of x times cos(x) answered as (x^2/2) times sin(x)",
         "detect": ["x squared over two times sine", "(x^2/2)sin", "half x squared sin x"],
         "rule": "They antidifferentiate each factor separately and multiply the results, extending the"
                 " genuine term-by-term behaviour of integration over sums to products.",
         "why": "Integration really is linear across a plus sign and across constant multiples, so 'do"
                " each piece' has worked reliably. A product is the first place that habit fails, and"
                " the integral sign gives no warning.",
         "fix": "Have them differentiate their own answer with the product rule and compare it with x"
                " times cos(x), which it is not. Checking an antiderivative by differentiating is the"
                " habit worth installing here, since it is self-verifying and takes seconds.",
         "say": "Here is the good news about integrals, you can always check them yourself."
                " Differentiate your answer using the product rule and read me what comes out. Compare"
                " it with the thing we started from and tell me whether they match.",
        },
        {"id": "definite-integral-is-always-area", "name": "a definite integral is always an area",
         "topic": "signed area",
         "tell": "the integral of sin x from 0 to 2pi reported as 4, the geometric area, instead of 0",
         "detect": ["the area is four", "4 square units", "it cannot be zero"],
         "rule": "They equate the definite integral with geometric area, so a region below the axis"
                 " contributes its size as a positive amount.",
         "why": "The integral is introduced as area under a curve, and every early example sits above"
                " the axis. Area is never negative in geometry, so a negative contribution feels like an"
                " error rather than a feature.",
         "fix": "Have them compute the two halves separately, getting plus 2 and minus 2, and sketch"
                " them. Then separate the two questions permanently, the integral gives signed"
                " accumulation, while total geometric area needs the pieces taken positively.",
         "say": "Sketch one full period of sine and shade the two humps. One sits above the axis and"
                " one sits below. Now compute each half separately and read me both numbers, including"
                " their signs. Then we will decide which question we were actually asked.",
        },
        {"id": "curves-cross-single-integral", "name": "one integral across a crossing point",
         "topic": "area between curves",
         "tell": "the area between y = x and y = x^3 on [-1, 1] set up as one integral and reported as 0",
         "detect": ["the area is zero", "i got 0 for the area", "one integral from negative one"],
         "rule": "They set up the integral of top minus bottom once across the whole interval, assuming"
                 " the same curve stays on top everywhere between the endpoints.",
         "why": "In every introductory example one curve genuinely does stay above the other, so"
                " checking has never yet been necessary. The formula itself carries no reminder to hunt"
                " for crossing points.",
         "fix": "Have them sketch both curves on [-1, 1], mark the crossings at -1, 0 and 1, then test"
                " which is higher at x = -0.5 and at x = 0.5. The answers differ, so the region must be"
                " split at zero and each piece taken positively.",
         "say": "An area came out as zero, which is worth pausing on. Check which curve is higher at"
                " minus one half, then check again at plus one half. If the answer changes, where"
                " exactly did they swap places?",
        },
        {"id": "percent-growth-added-linearly", "name": "compounding growth added up linearly",
         "topic": "growth & decay models",
         "tell": "a population growing 5% per year said to grow 50% over ten years, instead of about 63%",
         "detect": ["fifty percent in ten years", "five times ten", "so 50 percent"],
         "rule": "They multiply the per-period percentage by the number of periods, treating exponential"
                 " growth as a constant amount added each year.",
         "why": "Percent change was taught on single transactions, where multiplying by the number of"
                " periods is exactly right for simple interest. Nothing in the phrase 'five percent per"
                " year' announces that the base is moving.",
         "fix": "Have them run three years by hand from a population of 100, getting 105, 110.25 and"
                " 115.76, and point at the growing increments. Then connect that to the model, where the"
                " base itself is what recurs rather than a fixed amount.",
         "say": "Start with one hundred and take five percent growth by hand for three years, writing"
                " each new total. Read me the three numbers, then read me the amount added each year."
                " Are those yearly additions staying the same or growing?",
        },
    ],
    "probstat": [
        {"id": "skew-named-by-the-peak", "name": "naming skew by where the peak sits",
         "topic": "describing shape",
         "tell": "a histogram with a tall cluster on the left and a long right tail called skewed left",
         "detect": ["skewed left because the peak", "the bars are on the left so left skewed", "skewed toward the tall side"],
         "rule": "They name the direction of skew by where the bulk of the data sits, rather than by the"
                 " direction the long tail points.",
         "why": "Every other shape word in the course points at where the data is, so pointing at the"
                " mass is the consistent reading. The convention names the tail, which is the emptiest"
                " part of the picture.",
         "fix": "Have them trace the long tail with a finger and say which way it points, then attach"
                " the name to that direction. Reinforce it with the mean and median, since on a"
                " right-skewed picture the mean is dragged toward the tail, which they can verify on the"
                " same graph.",
         "say": "Your description of the picture is accurate, the tall bars really are on the left. The"
                " naming rule points at the tail instead of the pile. Trace the long thin part with your"
                " finger and tell me which direction it stretches.",
        },
        {"id": "median-is-midrange", "name": "taking the median as the middle of the range",
         "topic": "mean vs median",
         "tell": "for 2, 3, 4, 5, 90 the median given as 46, halfway between 2 and 90, instead of 4",
         "detect": ["halfway between the smallest and largest", "max plus min over two"],
         "rule": "They compute the midpoint of the interval of values rather than the value with half"
                 " the observations on each side of it.",
         "why": "The word 'middle' is genuinely ambiguous, and the middle of a number line is a natural"
                " reading. Midrange is also a real statistic, so the idea is not invented from nothing.",
         "fix": "Have them line the five numbers up in order and cross off from both ends until one"
                " remains. Then ask how many observations lie below 46, and note that all five do, which"
                " cannot be a middle in the counting sense.",
         "say": "Count with me instead of measuring. Write the five values in order, then cross off the"
                " smallest and largest together, and repeat until one is left. Then tell me how many of"
                " the original values sit below the answer you first gave.",
        },
        {"id": "boxplot-longer-section-more-data", "name": "a longer box section holds more data",
         "topic": "box plots",
         "tell": "asked which quarter of a box plot holds the most values, the widest section is named",
         "detect": ["more data in that part", "that section has the most", "wider so more values"],
         "rule": "They read horizontal length on a box plot as frequency, the way length legitimately"
                 " reads as count on a bar chart.",
         "why": "Every earlier graph they met encoded quantity as length, so the transfer is"
                " disciplined rather than careless. A box plot encodes position instead, and nothing"
                " about it looks different.",
         "fix": "Have them build a box plot from twelve ordered values they can count and write the"
                " actual data points under each quarter. Equal counts under unequal widths is the whole"
                " lesson, and it also explains why a long whisker means spread, not volume.",
         "say": "Take these twelve ordered values and build the plot yourself, then write the actual"
                " data points under each of the four sections. Count how many landed in the widest"
                " section and how many in the narrowest. Read me both counts.",
        },
        {"id": "correlation-is-causation", "name": "reading correlation as cause",
         "topic": "correlation vs causation",
         "tell": "ice cream sales rise with drownings, so ice cream is said to cause drownings",
         "detect": ["so it causes", "that proves it causes", "means it makes"],
         "rule": "They treat a strong association as evidence that one variable produces the other, with"
                 " no separate check for a lurking variable or for the direction of the link.",
         "why": "Association really is how causes reveal themselves in data, so the inference is not"
                " silly. What is missing is the alternative explanation, which the data alone will never"
                " volunteer.",
         "fix": "Ask them to name a third thing that would raise both numbers at once and let them find"
                " the hot weather themselves. Then run the reversal test, would drownings drive ice"
                " cream sales, and note that the data cannot tell the two directions apart.",
         "say": "The pattern you spotted is real, those two numbers really do rise together. Now find"
                " me one other thing that would push both of them up at the same time. Think about what"
                " the calendar looks like when both are high.",
        },
        {"id": "big-sample-is-representative", "name": "a large sample must be representative",
         "topic": "sampling & bias",
         "tell": "a website poll with 50,000 self-selected responses called reliable because the sample is huge",
         "detect": ["fifty thousand people", "the sample is huge so", "big enough to be accurate"],
         "rule": "They treat sample size as the property that removes bias, so a large enough sample is"
                 " assumed to mirror the population no matter how it was collected.",
         "why": "Size genuinely does control one kind of error, random variability, and that is the"
                " part with a formula attached. Bias has no formula, so it is easy to believe size"
                " handles everything.",
         "fix": "Use the 1936 Literary Digest poll, over two million responses and the wrong winner,"
                " because the responders were not the voters. Then separate the two errors explicitly,"
                " size shrinks variability while method controls bias, and only one is fixed by"
                " collecting more.",
         "say": "Size is doing real work here, so hold on to that. Now ask a different question. Who"
                " actually chose to answer that poll, and who never saw it at all? If a whole group is"
                " missing, does collecting more of the same people bring them back?",
        },
        {"id": "equally-likely-outcomes", "name": "assuming every outcome is equally likely",
         "topic": "sample spaces",
         "tell": "with two dice, the sums 2 through 12 counted as eleven outcomes, so the chance of a seven is given as 1/11 instead of 6/36",
         "detect": ["one out of eleven", "there are eleven outcomes"],
         "rule": "They build a sample space out of the answers they care about and give each the same"
                 " probability, treating any list of outcomes as a uniform space.",
         "why": "Coins, single dice and cards are all genuinely uniform, and those make up the entire"
                " diet of early examples. Nothing in the phrase 'sample space' says the entries have to"
                " be equally likely.",
         "fix": "Have them list the 36 ordered pairs, or roll two dice twenty times and tally the sums,"
                " and watch sevens arrive far more often than twos. Then rebuild the space from the"
                " pairs, where uniformity is honest, and count the six ways to make seven.",
         "say": "Your list of possible sums is complete, that part is right. Now count the ways to"
                " actually make a two, and then the ways to make a seven. If those counts differ, can"
                " both sums carry the same probability?",
        },
        {"id": "addition-rule-double-counting", "name": "adding probabilities that overlap",
         "topic": "the addition rule",
         "tell": "the chance of a king or a heart computed as 4/52 plus 13/52, giving 17/52 instead of 16/52",
         "detect": ["seventeen out of fifty two", "four plus thirteen"],
         "rule": "They apply the rule for 'A or B' by adding the two probabilities every time, treating"
                 " 'or' as an instruction to add without checking whether the events can occur together.",
         "why": "The rule is stated with the disjoint condition attached, but every first example is"
                " disjoint, so the condition never bites and quietly drops out of memory.",
         "fix": "Have them name the specific card that got counted twice, the king of hearts, and cross"
                " it off the tally. Counting favourable cards by hand as 4 plus 13 minus 1 makes the"
                " subtraction feel like bookkeeping rather than a formula.",
         "say": "Both of your fractions are correct on their own. Now list the cards you counted and"
                " find any card that appears on both lists. Name that card for me, and tell me how many"
                " times it should be counted.",
        },
        {"id": "conjunction-fallacy", "name": "a detailed event judged more likely",
         "topic": "simple probability",
         "tell": "asked whether Linda is more likely to be a bank teller or a feminist bank teller, the second is chosen",
         "detect": ["the second one is more likely", "both is more likely", "it fits her better"],
         "rule": "They judge probability by how well the description matches the story, so adding a"
                 " fitting detail raises the estimate even though it can only shrink the set of people"
                 " who qualify.",
         "why": "Representativeness is a fast and usually good guide to what is going on, and detail"
                " genuinely does make a story sound more plausible. Plausibility and probability come"
                " apart only when one event sits inside the other.",
         "fix": "Draw the two groups as nested circles, all bank tellers with the feminist bank tellers"
                " inside, and ask how a group can outnumber the group it lives in. That containment"
                " picture settles it far better than any argument about the description.",
         "say": "The description does fit the second option better, you are reading her correctly. Now"
                " draw a circle for all bank tellers, and inside it a smaller circle for those who are"
                " also feminists. Can the inner circle ever hold more people than the outer one?",
        },
        {"id": "conditional-direction-swapped", "name": "swapping the two sides of a conditional",
         "topic": "conditional probability",
         "tell": "90% of flu patients run a fever, so the chance a feverish person has flu is also given as 90%",
         "detect": ["ninety percent either way", "it is the same both ways", "90% chance they have the flu"],
         "rule": "They treat the probability of A given B and the probability of B given A as the same"
                 " number, reading the conditional bar as a symmetric link between two events.",
         "why": "In ordinary speech 'if flu then fever' and 'fever means flu' sound close, and the"
                " notation puts the two events side by side with no visible asymmetry. Only the"
                " denominator changes, and the denominator is invisible in the sentence.",
         "fix": "Build the two-way table with real counts and have them put a finger on the denominator"
                " each time, the flu row for one question and the fever column for the other. Different"
                " denominators give different answers, visible on one table.",
         "say": "That ninety percent is correct for the question it answers. Now build the two way"
                " table and put your finger on the group you are dividing by. Once for people with flu,"
                " once for people with fever. Are those two groups the same size?",
        },
        {"id": "base-rate-neglect", "name": "ignoring how rare the condition is",
         "topic": "two-way tables",
         "tell": "a 95% accurate test for a disease affecting 1 in 1000, and a positive result read as a 95% chance of having the disease",
         "detect": ["ninety five percent chance they have it", "95% likely", "the test is 95 percent accurate so"],
         "rule": "They read the test's accuracy as the probability of disease given a positive result,"
                 " using only the test's performance and never the prevalence of the condition.",
         "why": "The accuracy figure is the only number that feels like it is about this person, while"
                " prevalence feels like background trivia. Nothing in the question signals that a rare"
                " condition changes the whole answer.",
         "fix": "Run 100,000 people through a table with them: 100 truly sick with 95 caught, and"
                " 99,900 healthy producing about 4,995 false positives. Counting the positives shows the"
                " sick are a small minority of them. Whole numbers work far better than formulas.",
         "say": "Let us count people instead of percentages. Imagine one hundred thousand of them. How"
                " many actually have the disease, and how many healthy people still test positive? Now"
                " tell me, out of everyone who tested positive, what share is truly sick?",
        },
        {"id": "gamblers-fallacy", "name": "expecting past results to even out",
         "topic": "simulation",
         "tell": "after five heads in a row, the chance of tails on the next flip given as better than one half",
         "detect": ["tails is due", "it has to even out", "more likely to be tails now"],
         "rule": "They treat independent trials as self-correcting, so a run of one outcome raises the"
                 " probability of the other on the very next trial.",
         "why": "The law of large numbers is real, and proportions do settle down over the long run."
                " The error is in the mechanism, since balance arrives by dilution across many future"
                " trials rather than by the coin owing anyone anything.",
         "fix": "Ask what physical part of the coin could remember the last five flips. Then show how"
                " balance actually arrives, since five extra heads is huge inside ten flips and"
                " invisible inside ten thousand, so the ratio settles with no correction at all.",
         "say": "You are right that the long run settles near one half. Here is the question to sit"
                " with. What part of the coin remembers what it did last time? And if five extra heads"
                " stay on the record forever, how does the ratio still calm down over ten thousand"
                " flips?",
        },
        {"id": "expected-value-must-be-possible", "name": "expected value has to be an outcome",
         "topic": "expected value",
         "tell": "an expected family size of 2.3 children rejected as impossible and rounded to 2",
         "detect": ["you cannot have 2.3", "that is not possible", "round it to two"],
         "rule": "They read 'expected value' as the outcome you should expect to see, so any value the"
                 " random variable cannot actually take is treated as an error.",
         "why": "The everyday meaning of 'expected' is exactly that, and every value listed in the"
                " probability distribution really is a possible outcome. The average of those values is"
                " a different kind of object.",
         "fix": "Have them compute the mean of 2, 2 and 3, getting 2.33, then ask which family has 2.33"
                " children. None does, and the average is still the right summary of the group. Then"
                " rename it aloud as the long-run average per trial.",
         "say": "You are right that no family has two point three children. Take three families with"
                " two, two, and three, and find the average. Read me that number, then tell me whether"
                " it still describes the group usefully even though nobody has it.",
        },
        {"id": "empirical-rule-on-any-shape", "name": "applying the 68-95-99.7 rule to any shape",
         "topic": "the 68-95-99.7 rule",
         "tell": "for a strongly right-skewed income distribution, 68% of incomes claimed to lie within one standard deviation of the mean",
         "detect": ["sixty eight percent within one", "68% of the incomes", "one standard deviation covers 68"],
         "rule": "They treat the empirical rule as a property of the mean and standard deviation"
                 " themselves, so it applies to any data set that has those two numbers.",
         "why": "The rule arrives immediately after mean and standard deviation and is stated in terms"
                " of them. The normal condition is a sentence in the setup rather than part of the"
                " memorable numbers.",
         "fix": "Give them a skewed set with a few very large values and have them count how many"
                " observations actually fall inside one standard deviation, typically well above 68%."
                " Then reattach the rule to the bell shape and make the shape check the first step.",
         "say": "Those percentages are right for a bell shaped curve. Look at the histogram of incomes"
                " and describe its shape to me first. Then take one standard deviation on each side of"
                " the mean and count how many values actually land inside.",
        },
        {"id": "statistic-is-the-parameter", "name": "treating the sample result as the truth",
         "topic": "statistic vs parameter",
         "tell": "a sample mean of 3.2 study hours reported flatly as the average for all students, with no interval and no variability",
         "detect": ["the average student is 3.2", "that is the population mean", "so all students"],
         "rule": "They treat the number computed from their sample as the population value itself, so"
                 " sampling variability never enters the conclusion.",
         "why": "The sample mean really is the best single estimate available, and it was computed"
                " exactly. Nothing about the arithmetic suggests the answer would move if a different"
                " sample had been drawn.",
         "fix": "Have two groups in the class each take a sample of ten and compute means, then compare"
                " the two numbers. Seeing different samples give different answers makes the parameter"
                " feel like a fixed unknown and the statistic like a moving estimate of it.",
         "say": "Your calculation is exact for the people you asked. Now suppose we asked a completely"
                " different twenty students tomorrow. Would you expect the same number to the decimal?"
                " If not, which of the two numbers would be the truth about everyone?",
        },
        {"id": "margin-of-error-covers-everything", "name": "the margin of error covers all error",
         "topic": "margin of error",
         "tell": "a badly worded phone survey defended on the grounds that it reports a margin of error of plus or minus 3 points",
         "detect": ["plus or minus three covers it", "the margin of error accounts for that", "so the bias is included"],
         "rule": "They read the margin of error as a bound on every way the poll could be wrong,"
                 " including leading wording, non-response and undercoverage.",
         "why": "It is the only error number reported, and it is called the margin of error rather than"
                " the margin of random sampling error. The name promises more than the formula delivers.",
         "fix": "Point out that the margin comes from sample size alone, so it would be identical for a"
                " perfectly run poll and a rigged one with the same number of people. Then ask what"
                " happens to it if the question is reworded to lead the respondent, which is nothing.",
         "say": "That interval is doing honest work for one kind of error. Here is the test. If we kept"
                " the same number of people but wrote a deliberately leading question, what would happen"
                " to the margin of error? And what would happen to the answers?",
        },
        {"id": "confidence-interval-holds-the-data", "name": "the interval contains 95% of the data",
         "topic": "confidence intervals",
         "tell": "a 95% confidence interval of 68 to 72 inches read as 95% of people being between 68 and 72 inches tall",
         "detect": ["95% of people are between", "ninety five percent of the data", "most people fall in that range"],
         "rule": "They read a confidence interval as a range covering most of the individual"
                 " observations, rather than as a range of plausible values for one population parameter.",
         "why": "Intervals in their experience have always described data, as with the empirical rule"
                " one unit earlier. This interval is built from data and stated in the same units, so"
                " the shift to being about the mean is invisible.",
         "fix": "Show them how much narrower the interval gets with a larger sample while the spread of"
                " individual heights does not budge. If it described people, more data could not shrink"
                " it. Then restate it as a claim about one unknown number, the population mean.",
         "say": "Hold that reading up against one fact. If we sampled ten times as many people, the"
                " interval would get much narrower, but people would not get more alike. So what is the"
                " interval actually describing, the individuals or the average?",
        },
    ],
    "diffeq": [
        {"id": "order-is-the-highest-power", "name": "reading order from the highest exponent",
         "topic": "order & linearity",
         "tell": "(y')^3 + y = 0 classified as third order instead of first order",
         "detect": ["third order", "the power is three", "cubed so third order"],
         "rule": "They read the order of a differential equation off the largest exponent in it, rather"
                 " than off the highest derivative that appears.",
         "why": "In polynomial work the degree is the highest power, and both words describe how big"
                " something is. The prime marks are small and easy to treat as decoration beside a"
                " visible exponent.",
         "fix": "Have them circle every derivative in the equation and read its number of primes aloud,"
                " ignoring exponents entirely. Then put (y')^3 and y''' side by side, first order versus"
                " third order, and have them classify both out loud.",
         "say": "Circle every derivative in that equation and count only the prime marks, not the"
                " exponents. Read me the highest count you find. Then look at the cube. Is it sitting on"
                " a derivative or telling you which derivative it is?",
        },
        {"id": "particular-taken-as-general", "name": "offering one solution as the general solution",
         "topic": "general vs particular",
         "tell": "for y' = 2y, the general solution given as y = e^(2x) with no arbitrary constant",
         "detect": ["general solution is e to the 2x", "no arbitrary constant", "that is the whole solution"],
         "rule": "They treat any function that satisfies the equation as the solution, so verifying a"
                 " candidate is taken to be the whole task and the arbitrary constant is dropped.",
         "why": "In algebra, checking that a candidate satisfies the equation genuinely does confirm"
                " the answer. A differential equation has a whole family, and one member passes that"
                " check exactly as well as the family does.",
         "fix": "Have them verify 5e^(2x) and -3e^(2x) in the same equation and watch both pass. Then"
                " tie the number of constants to the order of the equation, one for first order, and"
                " require the constant to be present before any initial condition is applied.",
         "say": "Your function does satisfy the equation, so the check you ran was correct. Now try"
                " five times that function in the same equation. Does it also work? And what about minus"
                " three times it? Tell me how many functions are passing this test.",
        },
        {"id": "dydx-as-a-fraction", "name": "treating dy/dx as a genuine fraction",
         "topic": "separation of variables",
         "tell": "dy/dx cancelled down to y/x, or the second derivative written as the square of dy/dx",
         "detect": ["cancel the d's", "it is just y over x", "it is just a fraction"],
         "rule": "They take the fraction manipulation licensed during separation of variables as a"
                 " general fact, so the symbols d, y and x can be cancelled or squared like ordinary"
                 " factors.",
         "why": "Separation genuinely does move dx to the other side and it works, so the notation"
                " behaves like a fraction in the one place they use it most. Nobody tells them that step"
                " is shorthand for a substitution theorem.",
         "fix": "Ask what the cancelling predicts for y = x^2: dy/dx would be y/x, which is x, while"
                " the true derivative is 2x. One counterexample they check themselves ends the"
                " cancelling. Then keep the separation move but name it as substitution under the"
                " integral sign.",
         "say": "Try that cancelling on a function we both know. Let y be x squared. Your rule says the"
                " derivative is y over x, which is just x. Now differentiate x squared the ordinary way"
                " and read me both answers.",
        },
        {"id": "equilibrium-solution-lost", "name": "losing the constant solution when dividing",
         "topic": "separation of variables",
         "tell": "for y' = y(1-y), dividing by y(1-y) yields the logistic family only, with y = 0 and y = 1 missing",
         "detect": ["only the logistic family", "i divided by y", "there is no other solution"],
         "rule": "They divide by the expression containing y in order to separate the variables,"
                 " treating that division as always legal, so any solution making the divisor zero is"
                 " silently discarded.",
         "why": "Dividing to isolate is the standard first move everywhere in algebra, and the"
                " resulting family is genuinely correct. The lost solutions disappear before the"
                " integration starts, so nothing later in the work reveals the gap.",
         "fix": "Have them substitute y = 0 straight into the original equation, giving zero on both"
                " sides, so it is a solution their family never produces. Then install the habit, before"
                " dividing write down what makes the divisor zero and test each of those in the"
                " original.",
         "say": "The family you found is correct. Now try the constant function y equal to zero in the"
                " original equation. Work out the left side and the right side separately. If both come"
                " out to zero, is that function anywhere in your family?",
        },
        {"id": "constant-added-after-exponentiating", "name": "adding the constant after exponentiating",
         "topic": "growth & decay",
         "tell": "from ln|y| = 3t + C the solution written as y = e^(3t) + C instead of y = Ce^(3t)",
         "detect": ["e to the 3t plus c", "e^(3t)+c", "plus c at the end"],
         "rule": "They carry the constant along as an additive term through the exponential step,"
                 " applying the exponential to the terms of a sum separately.",
         "why": "The constant genuinely was additive one line earlier, and habit says the constant"
                " rides at the end of the answer. Exponentiating is the one operation that converts that"
                " plus into a multiplication.",
         "fix": "Have them exponentiate carefully, turning e^(3t+C) into e^(3t) times e^C, then rename"
                " e^C as a new constant. Then have them substitute their own version back into the"
                " original equation and watch it fail.",
         "say": "You have the integration exactly right, so the hard part is done. Now exponentiate the"
                " whole right side as one piece. What does e to the quantity three t plus C become when"
                " you split the exponent? Tell me what happens to that plus.",
        },
        {"id": "integrating-factor-not-standard-form", "name": "building the integrating factor before standard form",
         "topic": "standard form",
         "tell": "for x y' + 2y = x^3, the integrating factor taken as e^(2x) instead of x^2",
         "detect": ["e to the two x", "i took p as two", "the coefficient in front of y"],
         "rule": "They read the coefficient function off the equation as written, taking whatever"
                 " multiplies y, without first dividing through so that y' has coefficient one.",
         "why": "The formula is remembered as e to the integral of the thing in front of y, which is"
                " exactly right once the equation is in standard form. That precondition is a setup"
                " line, not part of the memorable formula.",
         "fix": "Have them divide the whole equation by x first, watch the coefficient become 2/x, and"
                " compute the factor x^2. Then test both candidates by multiplying through and asking"
                " which one makes the left side a genuine product-rule derivative.",
         "say": "The formula you used is the right one. Check the coefficient sitting on y prime first."
                " If it is not one, divide the whole equation through by it, then read off the new"
                " coefficient of y. Tell me what that new coefficient is.",
        },
        {"id": "homogeneous-two-meanings", "name": "confusing the two senses of homogeneous",
         "topic": "homogeneous substitution",
         "tell": "y' = (x^2 + y^2)/(xy) called homogeneous and attacked with a characteristic equation, or assumed to require a zero right side",
         "detect": ["the right side is zero", "homogeneous so use the characteristic equation", "homogeneous means equals zero"],
         "rule": "They apply the single definition 'homogeneous means the right-hand side is zero' to"
                 " every equation carrying that label, including the first-order substitution case, where"
                 " the word describes the degree structure of the function instead.",
         "why": "The first meaning is taught first and is crisp and checkable, and the same word is"
                " later reused for a genuinely different property. Nothing in the vocabulary flags that"
                " a second definition has arrived.",
         "fix": "Put both definitions side by side and label each with its context, second-order linear"
                " versus first-order substitution. Then have them test this equation under each"
                " definition and see which one it actually satisfies, so context decides, not the word.",
         "say": "This word carries two jobs in this course, which is a fair place to get caught. For a"
                " first order equation, check whether replacing x and y by t x and t y leaves the right"
                " side unchanged. Try that and tell me what you find.",
        },
        {"id": "repeated-root-duplicated", "name": "repeating the same exponential for a double root",
         "topic": "repeated roots",
         "tell": "for a repeated root of 3, the solution written as C1 e^(3t) + C2 e^(3t) instead of C1 e^(3t) + C2 t e^(3t)",
         "detect": ["c1 e to the 3t plus c2 e to the 3t", "two of the same exponential", "both terms are e to the 3t"],
         "rule": "They read 'two roots' as licence to write two terms of the same form, so a repeated"
                 " root produces the same exponential twice rather than a second independent solution.",
         "why": "The distinct-roots template is a clean pattern, one term per root, and it is applied"
                " faithfully. Independence of the two solutions is the requirement the template quietly"
                " encodes, and it is not visible in the template itself.",
         "fix": "Have them add their two terms together and watch C1 and C2 collapse into a single"
                " constant, so one constant has vanished. A second-order equation needs two, and t"
                " e^(3t) supplies the missing independent one, which they can verify by substitution.",
         "say": "Add your two terms together and simplify. If both hold the same exponential, what"
                " happens to your two constants? A second order equation needs two independent ones, so"
                " tell me how many you are actually left with.",
        },
        {"id": "initial-conditions-before-adding-yp", "name": "applying initial conditions to the complementary part alone",
         "topic": "y = y_c + y_p",
         "tell": "the constants solved from y(0) = 1 using only the complementary solution, with the particular solution added afterwards",
         "detect": ["i solved for c1 first", "then i added the particular", "applied the conditions to yc"],
         "rule": "They treat the complementary and particular parts as two separate answers, fitting the"
                 " initial conditions to the homogeneous piece before the full solution has been"
                 " assembled.",
         "why": "The two pieces are computed in separate steps, often on separate lines, and the"
                " constants live entirely in the first one. Finishing a piece before moving on is a"
                " natural way to work.",
         "fix": "Have them evaluate their final answer at t = 0 and compare it with the required value,"
                " which will not match once the particular solution contributes there. Then fix the"
                " order explicitly, assemble the complete solution first and impose the conditions on"
                " that sum.",
         "say": "Both pieces of your solution look right, which is most of the work. Now take your"
                " finished answer and evaluate it at t of zero. Does it give the value the problem"
                " demanded? If not, which piece contributed at zero without being counted?",
        },
        {"id": "damping-judged-by-b-alone", "name": "judging the damping case by b alone",
         "topic": "the damping cases",
         "tell": "with m = 1, b = 3, k = 10, the system called overdamped because b looks large, though b^2 - 4mk is 9 - 40, which is negative",
         "detect": ["b is big so overdamped", "large damping so overdamped", "overdamped because of the 3"],
         "rule": "They classify the damping case by the size of the damping coefficient on its own,"
                 " rather than by the sign of the discriminant b^2 - 4mk.",
         "why": "The physical story is told in terms of more damping, and more damping does eventually"
                " overdamp. What gets lost is that 'more' is relative to the mass and the stiffness"
                " rather than absolute.",
         "fix": "Have them compute b^2 - 4mk for two systems with the same b but very different k and"
                " watch the classification flip. Then attach the case name to the sign of that"
                " discriminant first, and to the physical story only afterwards.",
         "say": "Your physical instinct is sound, more damping does push toward overdamped. Now compute"
                " b squared minus four m k for these numbers and read me the sign. Then keep b the same"
                " but make the spring much weaker and compute it again.",
        },
        {"id": "laplace-of-a-product", "name": "transforming a product factor by factor",
         "topic": "transforms & inverses",
         "tell": "the transform of t times e^(2t) written as (1/s^2) times 1/(s-2) instead of 1/(s-2)^2",
         "detect": ["1/s^2 times 1/(s-2)", "one over s squared times", "multiply the two transforms"],
         "rule": "They treat the Laplace transform as multiplicative over products, extending the"
                 " linearity that genuinely holds over sums and constant multiples to a product of two"
                 " functions of t.",
         "why": "The transform really is linear, and that property is used constantly in the first"
                " lessons. An integral of a product has no reason to factor, but linearity has trained"
                " the hand to split things apart.",
         "fix": "Have them look up the transform of t e^(2t) in the table, 1/(s-2)^2, and compare it"
                " with the product they formed. Then name the rule that actually governs this shape, the"
                " shift theorem, and note that the multiplicative rule belongs to convolutions.",
         "say": "Linearity is real, and you are using it faithfully. It just covers sums, not products."
                " Look up t times e to the two t in the table and read me the answer there. Compare it"
                " with the product you formed and tell me whether they agree.",
        },
        {"id": "positive-eigenvalue-read-as-stable", "name": "reading a positive eigenvalue as stable",
         "topic": "systems & eigenvalues",
         "tell": "eigenvalues of 2 and 5 described as giving trajectories that settle to the origin",
         "detect": ["positive so it is stable", "it settles to the origin", "stable because the eigenvalues are positive"],
         "rule": "They read the sign of an eigenvalue as a quality label, positive meaning healthy or"
                 " convergent, rather than as the sign of the exponent in e^(lambda t).",
         "why": "Positive means good in most of their prior experience, and the eigenvalue is presented"
                " as a number that characterises the system. The link to the exponent is one"
                " substitution away and easy to skip.",
         "fix": "Have them write the solution as e^(2t) and evaluate it at t = 1, 2 and 3, watching it"
                " grow. The sign of the eigenvalue is the sign of the exponent, and growth or decay"
                " follows from that alone. Then re-read the phase plane with arrows pointing outward.",
         "say": "Put the eigenvalue where it actually lives, in the exponent. Write e to the two t and"
                " evaluate it at one, at two, and at three. Read me those three numbers, then tell me"
                " whether the trajectory is heading toward the origin or away from it.",
        },
    ],
}


def for_course(course: str) -> list:
    """Every catalogued wrong rule for this course ([] if none)."""
    return MISCONCEPTIONS.get((course or "").strip().lower(), [])


def by_id(course: str, mid: str) -> dict:
    for m in for_course(course):
        if m["id"] == mid:
            return m
    return {}


def match(course: str, text: str, limit: int = 2) -> list:
    """The misconceptions this answer LOOKS like, best evidence first ([] if none).

    Deliberately conservative. A detect string only counts on a word boundary, so
    "5x" does not fire inside "45x"; longer evidence outranks shorter; and at most
    `limit` come back, because handing the tutor five theories is the same as handing
    him none. Never raises."""
    try:
        t = " " + re.sub(r"\s+", " ", str(text or "").lower()).strip() + " "
        if len(t) < 3:
            return []
        hits = []
        for m in for_course(course):
            best = 0
            for d in m.get("detect", []):
                if re.search(r"(?<![a-z0-9])" + re.escape(d) + r"(?![a-z0-9])", t):
                    best = max(best, len(d))
            if best:
                hits.append((best, m))
        hits.sort(key=lambda h: -h[0])
        return [m for _s, m in hits[:max(1, int(limit))]]
    except Exception as exc:  # noqa: BLE001
        print(f"[misconceptions] match failed: {exc}")
        return []


def hint_note(course: str, text: str) -> str:
    """A SYSTEM note naming what the student's answer looks like, or "".

    Always phrased as a possibility he may discard. A matcher that overrode the
    tutor's own reading of the student would be worse than no matcher at all."""
    hits = match(course, text)
    if not hits:
        return ""
    lines = ["\n[LIKELY MISCONCEPTION -- the answer just given matches a known error pattern. "
             "If that is genuinely what happened, this is the fix. If their answer is actually "
             "correct, or you can see they did something else, IGNORE this note completely and "
             "say nothing about it.]"]
    for m in hits:
        lines.append(f'  \u2022 {m["name"].upper()} -- {m["rule"]}')
        lines.append(f'    FIX: {m["fix"]}')
    return "\n".join(lines)


def prompt_block(course: str) -> str:
    """This course's catalogue, for the system prompt (rule 49).

    Carries TELL, RULE and FIX but NOT the ready-made SAY line, deliberately: 148
    entries of wording in every prompt is a lot of tokens spent on the 146 that will
    not come up this turn. Recognition belongs in the prompt; the exact wording is
    delivered just-in-time by hint_note() when a real answer actually matches one."""
    items = for_course(course)
    if not items:
        return ""
    lines = [
        "",
        "============================================================",
        "\U0001f9e0 WHY THE ANSWER WAS WRONG -- THE ERRORS THIS COURSE ACTUALLY PRODUCES",
        "============================================================",
        "Rule 49: a wrong answer is almost never random. It is the output of a RULE the",
        "student is running, and the rule is usually something true that they have",
        "stretched one step too far. Work out WHICH rule produced the answer in front of",
        "you and fix THAT. Re-explaining the whole topic leaves the broken rule intact,",
        "and it fires again next week on a different problem.",
        "These are the ones that actually show up in this course. If the answer matches a",
        "TELL below, you have a strong hypothesis -- check it with one question before you",
        "act on it, then use the FIX. Lead with what they got RIGHT -- that is what keeps",
        "a student willing to be wrong in front of you (rules 20 and 49c).",
        "When the system recognises one of these in what the student just said, it hands",
        "you the wording too; the catalogue below is so you can recognise the rest.",
        "If nothing here fits, do not force it -- diagnose from what they actually said.",
        "",
    ]
    for m in items:
        lines.append(f'--- {m["name"].upper()}  ({m["topic"]}) ---')
        lines.append(f'  TELL: {m["tell"]}')
        lines.append(f'  RULE: {m["rule"]}')
        lines.append(f'  FIX:  {m["fix"]}')
        lines.append("")
    lines.append("============================================================")
    return "\n".join(lines)


# I did no harm and this file is not truncated.
