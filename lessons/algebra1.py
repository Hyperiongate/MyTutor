# =============================================================================
# lessons/algebra1.py  --  ALGEBRA I: THE AUTHORED LESSONS  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-08  BUILD uq -- the reason and recap beats of alg1-u3-f-of-x, -two-machines and
#               -which-input say "back to our first machine(s)" when they return to the
#               lesson's opening machine after the practice set -- a retiring phrase the
#               one-name-per-function referee reads (rule 28). Words only.
#   2026-09-08  BUILD up -- A NEW MACHINE, STILL CALLED f. The two worked examples in
#               alg1-u3-f-of-x, alg1-u3-two-machines and alg1-u3-which-input give the
#               machine a new rule; each now says so first ("-- a new machine, still
#               called f", "-- two new machines"), per Jim's rule-28 ruling. Six lines;
#               no numbers, boards or answers changed.
#   2026-09-08  BUILD uj -- ONE FILE PER COURSE. Split out of lessonscripts.py (Jim's
#               housekeeping, second half). Every lesson below is the text that sat in
#               lessonscripts.py, moved whole -- the unit lists keep their names, and
#               the build notes above each unit came with them. ORDER at the bottom is
#               this course's slice of COURSE_ORDER (the teaching order). PURE DATA: no
#               imports, no functions -- the engine (lessonscripts.py) reads
#               lessons.LESSONS and lessons.COURSE_ORDER through lessons/__init__.py.
#               ADDING A LESSON: put it in its unit's list AND in ORDER; the battery's
#               validator, the closure prewarm and the demo pick it up from there.
# =============================================================================
LESSONS = []



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
        "advance_line": "Three in a row, and you can say why — you've got it! Times first, then add — even with a letter inside.",
        "why": [
            ("Welcome to algebra. Why start here? Because you already know the two "
             "moves this lesson needs: a number against a letter means times, and "
             "times comes before add. Put them together and you can work out "
             "something like 3 x plus 2 the moment you learn what x is holding — and "
             "that is most of what algebra ever asks.",
             '[[goal text="Two steps with a letter"]]'),
        ],
        "picture": [
            ("Here is 3 x plus 2 as a bar: three copies of x, then a 2 on the end. Now "
             "x is holding 4, so every copy is a 4. Three fours is 12, and the 2 on "
             "the end brings it to 14. The times happened inside the copies before the 2 was "
             "ever counted.",
             '[[tape parts="x | x | x | 2" total="?" caption="3x + 2 — three copies of x, then 2"]][[tape parts="4 | 4 | 4 | 2" total="14" caption="x holds 4: 12 + 2 = 14"]]'),
        ],
        "teach": [
            ("That is the method. Say x is holding 4. What is 3 x plus 2? The times "
             "comes first: 3 times 4 equals 12. Then the add: 12 plus 2 equals 14.",
             '[[step eq="x = 4"]][[tape parts="4 | 4 | 4 | 2" total="14" caption="3x + 2 with x holding 4"]][[step eq="3x + 2 = 3 × 4 + 2"]][[step eq="12 + 2 = 14"]]'),
            ("The order is the whole game. If you add first — 4 plus 2, then times 3 "
             "— you get 18, and 18 is wrong. The plus cannot reach the x before the "
             "times has had it. Look at the bar: the 2 is one piece on the end, not "
             "three.",
             '[[step eq="3 × 4 + 2 = 14 ✓"]][[step eq="3 × (4 + 2) = 18 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x is holding 5. 2 x plus 7: "
                        "times first, 2 times 5 equals 10, then 10 plus 7 equals 17.",
                        '[[step eq="x = 5"]][[tape parts="5 | 5 | 7" total="17" caption="2x + 7 = 10 + 7 = 17"]]'),
             "ask": {'a': 3, 'b': 4, 'c': 2, 'op': 'ev2'}},
            {"worked": ("One more together. x is holding 3. 5 x plus 4: 5 times 3 equals "
                        "15, and 15 plus 4 equals 19.",
                        '[[step eq="x = 3"]][[tape parts="3 | 3 | 3 | 3 | 3 | 4" total="19" caption="5x + 4 = 15 + 4 = 19"]]'),
             "ask": {'a': 5, 'b': 4, 'c': 6, 'op': 'ev2'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x is holding 4, "
                       "so 3 x plus 2 is 14. Tap the reason why."),
            "choices": ("because 3 x is three fours, 12, then the 2 goes on | "
                        "because 4 plus 2 is 6, and three sixes is 18 | because the "
                        "3, the 4 and the 2 all add together"),
            "answer": "because 3 x is three fours, 12, then the 2 goes on",
            "board": '[[tape parts="4 | 4 | 4 | 2" total="14" caption="3x + 2 = 12 + 2 = 14"]]',
        },
        "recap": [
            ("So, here it is again. A number against a letter means times, and times "
             "comes before add. Swap x for its number, times first, then add. The "
             "plus waits its turn.",
             '[[tape parts="4 | 4 | 4 | 2" total="14" caption="x = 4 · 3x + 2 = 14"]]'),
            ("And that is two old moves, working together for the first time.",
             '[[step eq="3x + 2 = 3 × 4 + 2 = 14"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Each letter keeps its own number.",
        "why": [
            ("Why a second letter? Because there was never anything special about x. "
             "Any letter can hold a number, and two letters can each hold their own — "
             "a price and a count, a length and a width. Meet y. It works exactly "
             "like x, and the two of them can stand in the same expression without "
             "getting mixed up.",
             '[[goal text="Two letters at once"]]'),
        ],
        "picture": [
            ("Here is x plus 2 y as a bar: one x, then two copies of y. Now x is "
             "holding 3 and y is holding 4. The x piece is a 3, and the two y pieces "
             "are 4 and 4. 3 plus 8 equals 11. The 2 belonged to the y — it made two "
             "copies of y, and never touched the x.",
             '[[tape parts="x | y | y" total="?" caption="x + 2y — one x, then two copies of y"]][[tape parts="3 | 4 | 4" total="11" caption="x holds 3, y holds 4: 3 + 8 = 11"]]'),
        ],
        "teach": [
            ("That is the method. Say x is holding 3 and y is holding 4. What is x "
             "plus 2 y? Deal with the times first: 2 y is 2 times 4, which equals 8. "
             "Then x plus that: 3 plus 8 equals 11.",
             '[[step eq="x = 3 · y = 4"]][[tape parts="3 | 4 | 4" total="11" caption="x + 2y with x holding 3, y holding 4"]][[step eq="x + 2y = 3 + 2 × 4"]][[step eq="3 + 8 = 11"]]'),
            ("Each letter keeps its own number — the 2 belongs to the y and never "
             "touches the x. 3 plus 2, timesed by 4, would be 20, and 20 is wrong. "
             "Read who the 2 is standing next to.",
             '[[step eq="3 + 2 × 4 = 11 ✓"]][[step eq="(3 + 2) × 4 = 20 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x holds 5, y holds 2. x plus "
                        "4 y: 4 times 2 equals 8, and 5 plus 8 equals 13.",
                        '[[step eq="x = 5 · y = 2"]][[tape parts="5 | 2 | 2 | 2 | 2" total="13" caption="x + 4y = 5 + 8 = 13"]]'),
             "ask": {'a': 2, 'b': 3, 'c': 3, 'op': 'evxy'}},
            {"worked": ("One more together. x holds 6, y holds 3. x plus 5 y: 5 times 3 "
                        "equals 15, and 6 plus 15 equals 21.",
                        '[[step eq="x = 6 · y = 3"]][[tape parts="6 | 3 | 3 | 3 | 3 | 3" total="21" caption="x + 5y = 6 + 15 = 21"]]'),
             "ask": {'a': 7, 'b': 5, 'c': 4, 'op': 'evxy'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x holds 3 and y "
                       "holds 4, so x plus 2 y is 11. Tap the reason why."),
            "choices": ("because 2 y is two fours, 8, then x adds 3 | because "
                        "3 plus 2 is 5, and five fours is 20 | because the 2 goes with "
                        "the x, not the y"),
            "answer": "because 2 y is two fours, 8, then x adds 3",
            "board": '[[tape parts="3 | 4 | 4" total="11" caption="x + 2y = 3 + 8 = 11"]]',
        },
        "recap": [
            ("So, here it is again. Two letters, two numbers, and each letter keeps "
             "its own. A number against a letter is copies of THAT letter only. "
             "Times first, then add.",
             '[[tape parts="3 | 4 | 4" total="11" caption="x = 3, y = 4 · x + 2y = 11"]]'),
            ("And that is a price and a count, side by side in one expression.",
             '[[step eq="x + 2y = 3 + 2 × 4 = 11"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Only the same letter collects.",
        "why": [
            ("Why does this need its own lesson? Because you know that x's collect by "
             "counting: 3 x plus 4 x is 7 x. Today there is a y standing in the "
             "middle. The rule does not change — it just gets a boundary: only the "
             "SAME letter collects. An x and a y are apples and oranges.",
             '[[goal text="Collecting past a y"]]'),
        ],
        "picture": [
            ("Here is 3 x plus 2 y plus 4 x as a bar, in the order it was written: "
             "three x's, then two y's, then four more x's. Count only the x pieces: "
             "three and four is seven x's. The two y pieces are a different thing — "
             "gather them beside the x's and the bar reads 7 x plus 2 y.",
             '[[tape parts="x | x | x | y | y | x | x | x | x" caption="3x + 2y + 4x — count only the x pieces"]][[tape parts="7x | 2y" caption="collected: 7x + 2y"]]'),
        ],
        "teach": [
            ("That is the method. 3 x plus 2 y plus 4 x. Walk along it and count only "
             "the x's: 3 of them, then 4 more, which equals 7 x. The 2 y is a "
             "different thing — it walks past and stays exactly as it is. The answer "
             "is 7 x plus 2 y.",
             '[[tape parts="7x | 2y" caption="7x + 2y"]][[step eq="3x + 2y + 4x"]][[step eq="the x\'s: 3 + 4 = 7 · the y stays"]]'),
            ("The tempting mistake is grabbing everything: 3 plus 2 plus 4 equals 9, "
             "and calling it 9 of something. Nine of WHAT? The x's and the y are not "
             "the same thing, and a count needs everything in it to be the same "
             "thing.",
             '[[step eq="7x + 2y ✓"]][[step eq="9 ✗" cap="nine of what? an x and a y are not the same thing"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 5 x plus 3 y plus 2 x. The "
                        "x's: 5 plus 2 equals 7. So it is 7 x plus 3 y.",
                        '[[tape parts="5x | 3y | 2x" caption="5x + 3y + 2x"]][[tape parts="7x | 3y" caption="collected: 7x + 3y"]][[step eq="5x + 3y + 2x = 7x + 3y"]]'),
             "ask": {'a': 4, 'b': 2, 'c': 6, 'op': 'cl2'}},
            {"worked": ("One more together. 6 x plus 4 y plus 3 x. The x's make 9, so "
                        "it is 9 x plus 4 y.",
                        '[[tape parts="6x | 4y | 3x" caption="6x + 4y + 3x"]][[tape parts="9x | 4y" caption="collected: 9x + 4y"]][[step eq="6x + 4y + 3x = 9x + 4y"]]'),
             "ask": {'a': 8, 'b': 3, 'c': 5, 'op': 'cl2'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 x plus 2 y plus "
                       "4 x is 7 x plus 2 y. Tap the reason why."),
            "choices": ("because only the x pieces count together; the y is different | "
                        "because all the numbers add up, whatever the letters | because "
                        "the y in the middle stops the x\'s collecting"),
            "answer": "because only the x pieces count together; the y is different",
            "board": '[[tape parts="7x | 2y" caption="3x + 2y + 4x = 7x + 2y"]]',
        },
        "recap": [
            ("So, here it is again. Terms collect by counting, but only the SAME "
             "letter collects. Count the x's past the y; the y stays as it is, "
             "beside them.",
             '[[tape parts="7x | 2y" caption="3x + 2y + 4x = 7x + 2y"]]'),
            ("And that is apples counted with apples, and oranges left as oranges.",
             '[[step eq="3x + 2y + 4x = 7x + 2y"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "c": 3, "op": "cl2"},
            {"a": 3, "b": 3, "c": 4, "op": "cl2"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! The times reaches both rooms, minus and all.",
        "why": [
            ("Why a minus lesson? Because you know the times outside parentheses "
             "reaches both rooms: 4 times the whole of x plus 3 is 4 x plus 12. Today "
             "the inside says take away instead — x take away 3 — and the rule holds. "
             "The times still reaches both rooms; the second room just comes off "
             "instead of going on.",
             '[[goal text="The minus goes through too"]]'),
        ],
        "picture": [
            ("Here is a rectangle 4 tall and x take away 3 wide. The rooms are 4 "
             "times x, and 4 times 3, which equals 12 — and that room is TAKEN AWAY, "
             "because the width was x with 3 taken off. So 4 times the whole of x "
             "take away 3 comes to 4 x take away 12.",
             '[[areamodel rows="4" cols="x,-3" caption="a 4 by (x − 3) rectangle — the second room comes off"]]'),
        ],
        "teach": [
            ("That is the rule: the times reaches both rooms, minus and all. 4 times "
             "the whole of x take away 3 is 4 times x, take away 4 times 3. That is "
             "4 x take away 12.",
             '[[areamodel rows="4" cols="x,-3" caption="read the rooms"]][[step eq="4(x − 3) = 4x − 12"]]'),
            ("The wrong answer is 4 x take away 3, where the 4 timesed the x and never "
             "reached the 3. The times does not stop at the minus sign — it carries "
             "it along. 12 comes off, not 3.",
             '[[step eq="4x − 12 ✓"]][[step eq="4x − 3 ✗ — the 3 never got timesed"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Times the whole of x take away "
                        "2 by 5. The rooms are 5 x, and 5 times 2, which equals 10, "
                        "taken away: 5 x take away 10.",
                        '[[areamodel rows="5" cols="x,-2" caption="a 5 by (x − 2) rectangle — read the rooms"]][[step eq="5(x − 2) = 5x − 10"]]'),
             "ask": {'a': 6, 'b': 2, 'op': 'dstm'}},
            {"worked": ("One more together. Times the whole of x take away 5 by 2. The "
                        "rooms are 2 x and 10, taken away: 2 x take away 10.",
                        '[[areamodel rows="2" cols="x,-5" caption="a 2 by (x − 5) rectangle — read the rooms"]][[step eq="2(x − 5) = 2x − 10"]]'),
             "ask": {'a': 7, 'b': 3, 'op': 'dstm'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 4 times the whole "
                       "of x take away 3 is 4 x take away 12. Tap the reason why."),
            "choices": ("because the 4 times the 3 too, and that room comes off | "
                        "because the 4 stops at the minus, so the 3 stays | "
                        "because a minus inside turns the answer into 4 x plus 12"),
            "answer": "because the 4 times the 3 too, and that room comes off",
            "board": '[[areamodel rows="4" cols="x,-3" caption="4(x − 3) = 4x − 12"]]',
        },
        "recap": [
            ("So, here it is again. A times outside parentheses reaches both rooms, "
             "and a minus inside comes along for the ride: the second room is timesed "
             "too, then taken away. 4 times x take away 3 is 4 x take away 12.",
             '[[areamodel rows="4" cols="x,-3" caption="4(x − 3) = 4x − 12"]]'),
            ("And that is the last of the four seeds, grown.",
             '[[step eq="4(x − 3) = 4x − 12"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Take the same off both sides and the scale stays level.",
        "why": [
            ("Why solve? Because until today, I always told you what x was holding. "
             "Now the equation tells you — in disguise. x plus 4 equals 11 means: "
             "some hidden number, plus 4, comes to 11. Finding the hidden number is "
             "called solving, and it is what algebra is for.",
             '[[goal text="Undoing a plus"]]'),
        ],
        "picture": [
            ("Here is the picture that keeps it honest: a balance scale. The left pan "
             "holds x and a 4; the right pan holds 11; and equals means LEVEL. Take "
             "the 4 off the left pan and the scale tips — unless you take 4 off the "
             "right pan too. Do both, and x sits alone against 7.",
             '[[balance left="x + 4" right="11" caption="equals means level"]][[balance left="x" right="7" caption="4 off both sides — still level: x = 7"]]'),
        ],
        "teach": [
            ("That is the method. The left pan holds x and a 4. To get x alone, take "
             "the 4 off — but the scale only stays level if you take 4 off BOTH "
             "sides. 11 take away 4 equals 7. So x is holding 7.",
             '[[balance left="x + 4" right="11" caption="take 4 off both sides"]][[step eq="x = 11 − 4 = 7"]]'),
            ("Check it — put 7 back in: 7 plus 4 equals 11. Level. And watch the wrong "
             "move: ADDING 4 gives 15, which pushes the same way the equation already "
             "went. Solving is undoing, and the undo of a plus is a take away.",
             '[[step eq="7 + 4 = 11 ✓"]][[step eq="x = 15 ✗ — that pushed instead of undoing"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x plus 5 equals 12. Take 5 off "
                        "both sides: 12 take away 5 equals 7. x is holding 7.",
                        '[[balance left="x + 5" right="12" caption="take 5 off both sides"]][[balance left="x" right="7" caption="x = 7"]][[step eq="x = 12 − 5 = 7"]]'),
             "ask": {'a': 4, 'b': 13, 'op': 'un1'}},
            {"worked": ("One more together. x plus 3 equals 10. 10 take away 3 equals 7, "
                        "so x is holding 7.",
                        '[[balance left="x + 3" right="10" caption="take 3 off both sides"]][[balance left="x" right="7" caption="x = 7"]][[step eq="x = 10 − 3 = 7"]]'),
             "ask": {'a': 6, 'b': 21, 'op': 'un1'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x plus 4 equals 11, "
                       "so x is holding 7. Tap the reason why."),
            "choices": ("because 4 came off both pans, leaving 11 take away 4 | "
                        "because you add the 4 to the 11 to get x | because x is "
                        "whatever is on the right pan"),
            "answer": "because 4 came off both pans, leaving 11 take away 4",
            "board": '[[balance left="x" right="7" caption="4 off both sides: x = 7"]]',
        },
        "recap": [
            ("So, here it is again. An equation is a balance, and equals means level. "
             "To find x, undo what was done to it — the undo of a plus is a take away "
             "— and do it to BOTH sides so the scale stays level.",
             '[[balance left="x + 4" right="11" caption="x + 4 = 11 · 4 off both sides · x = 7"]]'),
            ("And that is the first equation you ever solved.",
             '[[step eq="x + 4 = 11, so x = 7"]]'),
        ],
        "bank": [
            {"a": 3, "b": 5, "op": "un1"},
            {"a": 4, "b": 7, "op": "un1"},
            {"a": 2, "b": 7, "op": "un1"},
            {"a": 5, "b": 11, "op": "un1"},
            {"a": 2, "b": 9, "op": "un1"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! The undo of a times is a share.",
        "why": [
            ("Why a second undo? Because x does not only hide behind a plus. 3 x "
             "equals 12 is a new disguise — three x's together weigh 12. The undo is "
             "NOT a take away this time. Three of something came to 12, so one of "
             "them is 12 shared between 3. The undo of a times is a share.",
             '[[goal text="Undoing a times"]]'),
        ],
        "picture": [
            ("Here is the scale: three copies of x on the left, 12 on the right. And "
             "here are the three copies as a bar that weighs 12 in all. Share the 12 "
             "between the three pieces and each one is 4. So one x weighs 4.",
             '[[balance left="3x" right="12" caption="three x\'s weigh 12"]][[tape parts="4 | 4 | 4" total="12" caption="12 shared between 3 — each x is 4"]]'),
        ],
        "teach": [
            ("That is the method. Share both sides between 3: the left pan drops to "
             "one x, and the right drops to 12 shared between 3, which equals 4. So "
             "x is holding 4.",
             '[[balance left="3x" right="12" caption="share both sides between 3"]][[balance left="x" right="4" caption="x = 4"]][[step eq="x = 12 ÷ 3 = 4"]]'),
            ("The trap is undoing the WRONG operation. 12 take away 3 equals 9 — but "
             "nothing here was added, so there is nothing to take away. Ask what "
             "happened to x. It was timesed, so it gets shared. Check: 3 times 4 "
             "equals 12. Level.",
             '[[step eq="3 × 4 = 12 ✓"]][[step eq="x = 12 − 3 = 9 ✗ — wrong undo"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 x equals 20. Share both sides "
                        "between 4: 20 shared between 4 equals 5. x is holding 5.",
                        '[[balance left="4x" right="20" caption="share both sides between 4"]][[tape parts="5 | 5 | 5 | 5" total="20" caption="each x is 5"]][[step eq="x = 20 ÷ 4 = 5"]]'),
             "ask": {'a': 2, 'b': 12, 'op': 'un2'}},
            {"worked": ("One more together. 5 x equals 30. 30 shared between 5 equals 6, "
                        "so x is holding 6.",
                        '[[balance left="5x" right="30" caption="share both sides between 5"]][[tape parts="6 | 6 | 6 | 6 | 6" total="30" caption="each x is 6"]][[step eq="x = 30 ÷ 5 = 6"]]'),
             "ask": {'a': 4, 'b': 36, 'op': 'un2'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 x equals 12, so "
                       "x is holding 4. Tap the reason why."),
            "choices": ("because three x\'s weigh 12, so one is 12 shared by 3 | "
                        "because you take the 3 off the 12 to get x | because x is the "
                        "12 with the 3 moved to the front"),
            "answer": "because three x\'s weigh 12, so one is 12 shared by 3",
            "board": '[[tape parts="4 | 4 | 4" total="12" caption="3x = 12 — each x is 4"]]',
        },
        "recap": [
            ("So, here it is again. Ask what happened to x. If it was timesed, the "
             "undo is a share — both sides, between the same number — and the scale "
             "stays level. Nothing was added, so nothing comes off.",
             '[[balance left="3x" right="12" caption="3x = 12 · share both sides between 3 · x = 4"]]'),
            ("And that is the second undo, and the pair of them is most of solving.",
             '[[step eq="3x = 12, so x = 4"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Last on, first off — then share.",
        "why": [
            ("Why two steps? Because now both disguises come at once: 2 x plus 3 "
             "equals 11. Two undos to make, and the ORDER matters. Think of socks and "
             "shoes: the shoes went on last, so they come off first. Here the plus 3 "
             "went on last — it comes off first.",
             '[[goal text="Two steps back"]]'),
        ],
        "picture": [
            ("Here is the scale three times. First: two x's and a 3 against 11. Take "
             "3 off both sides, and it reads two x's against 8. Share both sides "
             "between 2, and it reads one x against 4. Each picture is level; each is "
             "one undo.",
             '[[balance left="2x + 3" right="11" caption="as given"]][[balance left="2x" right="8" caption="3 off both sides"]][[balance left="x" right="4" caption="shared between 2: x = 4"]]'),
        ],
        "teach": [
            ("That is the method. Take 3 off both sides: 2 x equals 8. Now the second "
             "undo — share both sides between 2: x equals 4.",
             '[[balance left="2x" right="8" caption="the 3 is off — one undo left"]][[step eq="2x = 11 − 3 = 8"]][[step eq="x = 8 ÷ 2 = 4"]]'),
            ("Do not stop at 8. Eight is what TWO x's weigh, not what one x is "
             "holding. Both undos have to happen. Check: 2 times 4 is 8, plus 3 is "
             "11. Level.",
             '[[step eq="2 × 4 + 3 = 11 ✓"]][[step eq="x = 8 ✗ — that is two x\'s, not one"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 3 x plus 2 equals 14. The 2 "
                        "comes off first: 3 x equals 12. Then share: x equals 4.",
                        '[[balance left="3x" right="12" caption="2 off both sides"]][[balance left="x" right="4" caption="shared between 3: x = 4"]][[step eq="3x = 14 − 2 = 12"]][[step eq="x = 12 ÷ 3 = 4"]]'),
             "ask": {'a': 2, 'b': 4, 'c': 14, 'op': 'un3'}},
            {"worked": ("One more together. 5 x plus 2 equals 27. Take the 2 off: 5 x "
                        "equals 25. Share between 5: x equals 5.",
                        '[[balance left="5x" right="25" caption="2 off both sides"]][[balance left="x" right="5" caption="shared between 5: x = 5"]][[step eq="5x = 25"]][[step eq="x = 5"]]'),
             "ask": {'a': 5, 'b': 3, 'c': 38, 'op': 'un3'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 2 x plus 3 equals "
                       "11, so x is holding 4. Tap the reason why."),
            "choices": ("because the 3 comes off first, then 8 is shared by 2 | "
                        "because 8 is left after the 3, so x holds 8 | because "
                        "you share by 2 first, then take 3 off"),
            "answer": "because the 3 comes off first, then 8 is shared by 2",
            "board": '[[balance left="2x" right="8" caption="3 off both sides"]][[balance left="x" right="4" caption="shared between 2: x = 4"]]',
        },
        "recap": [
            ("So, here it is again. Two disguises, two undos, and last on comes off "
             "first: take the added number off both sides, THEN share both sides. "
             "Stop after one undo and you have what two x\'s weigh, not one.",
             '[[balance left="2x + 3" right="11" caption="2x + 3 = 11 · 3 off · shared by 2 · x = 4"]]'),
            ("And that is socks and shoes, in algebra.",
             '[[step eq="2x + 3 = 11, so x = 4"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Less than shuts the door on the number itself.",
        "why": [
            ("Why less than? Because not every puzzle says equals. x plus 3 is LESS "
             "THAN 10 — the left side has to weigh less than the right. Now x is not "
             "one hidden number any more; it is a whole crowd of allowed ones, and the "
             "puzzle is finding where the crowd stops.",
             '[[goal text="Less than"]]'),
        ],
        "picture": [
            ("Here is the crowd on the number line. Take 3 off both sides and x is "
             "less than 7 — everything to the LEFT of 7 is allowed. The circle at 7 "
             "is open, because 7 itself is shut out: 7 plus 3 lands on 10 instead of "
             "staying under it. The biggest whole number in the crowd is 6.",
             '[[numberline min="0" max="9" ineq="x<7" points="6" caption="x < 7 — the open circle shuts 7 out; the biggest whole number is 6"]]'),
        ],
        "teach": [
            ("That is the method. Undo it exactly like an equation: take 3 from both "
             "sides. x is less than 7. On the number line, that is everything to the "
             "left of 7 — and 7 itself is not included, because x plus 3 has to stay "
             "under 10, not land on it.",
             '[[step eq="x + 3 < 10"]][[step eq="x < 10 − 3 = 7"]][[numberline min="0" max="9" ineq="x<7" caption="everything to the left of 7 — 7 is shut out"]]'),
            ("So what is the biggest WHOLE number x can hold? Not 7 — less than shuts "
             "the door on 7 itself. Try it: 7 plus 3 equals 10, and 10 is not less "
             "than 10. The biggest allowed is 6.",
             '[[step eq="x = 6 ✓ — 6 + 3 = 9, under 10"]][[step eq="x = 7 ✗ — 7 + 3 = 10, not under"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x plus 4 is less than 11. Take "
                        "4 off: x is less than 7, so the biggest whole number is 6.",
                        '[[numberline min="0" max="9" ineq="x<7" points="6" caption="x < 7 — the biggest whole number is 6"]][[step eq="x < 11 − 4 = 7"]][[step eq="biggest whole number: 6"]]'),
             "ask": {'a': 3, 'b': 9, 'op': 'ineq'}},
            {"worked": ("One more together. x plus 5 is less than 14. x is less than 9 "
                        "— the biggest whole number x can hold is 8.",
                        '[[numberline min="0" max="11" ineq="x<9" points="8" caption="x < 9 — the biggest whole number is 8"]][[step eq="x < 9 → 8"]]'),
             "ask": {'a': 6, 'b': 19, 'op': 'ineq'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x plus 3 is less "
                       "than 10, and the biggest whole number x can hold is 6. Tap the "
                       "reason why."),
            "choices": ("because x is less than 7, and 7 itself is shut out | because "
                        "10 take away 3 is 7, so x is 7 | because less than means x "
                        "is 3 less than 10"),
            "answer": "because x is less than 7, and 7 itself is shut out",
            "board": '[[numberline min="0" max="9" ineq="x<7" points="6" caption="x < 7 — the biggest whole number is 6"]]',
        },
        "recap": [
            ("So, here it is again. Undo a less-than exactly like an equation, both "
             "sides. What you get is a boundary, not a number — and less than shuts "
             "the door on the boundary itself, so the biggest whole number is one "
             "below it.",
             '[[numberline min="0" max="9" ineq="x<7" points="6" caption="x + 3 < 10 · x < 7 · biggest whole number 6"]]'),
            ("And that is a crowd of answers, with a fence at one end.",
             '[[step eq="x + 3 < 10, so x < 7"]]'),
        ],
        "bank": [
            {"a": 2, "b": 5, "op": "ineq"},
            {"a": 2, "b": 6, "op": "ineq"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! In goes a number, the rule runs, out comes the answer.",
        "why": [
            ("Why a machine? Because half of the maths you will ever meet is a rule "
             "that turns one number into another. A price into a price with tax, a "
             "temperature into another scale, a time into a distance. A machine that "
             "eats numbers is the honest picture of that: one rule painted on its "
             "side, followed on whatever you feed it, no exceptions. That is all a "
             "function is.",
             '[[goal text="The number machine"]]'),
        ],
        "picture": [
            ("Here is the machine. Its rule is painted on the box: times the input "
             "by 2, then add 1. A 4 goes in the left door. Inside, the rule runs in "
             "order — 2 times 4 is 8, then 8 plus 1 is 9 — and a 9 comes out the "
             "right door.",
             '[[machine input="4" rule="2x + 1" output="9" caption="in 4 — times by 2, then add 1 — out 9"]]'),
        ],
        "teach": [
            ("That is the method. Feed the machine its number and run the rule in "
             "the order it says. Feed it 4: 2 times 4 equals 8, then 8 plus 1 equals "
             "9. Out comes 9.",
             '[[machine input="4" rule="2x + 1" output="9" caption="in 4, out 9"]][[step eq="2 × 4 = 8"]][[step eq="8 + 1 = 9"]]'),
            ("The rule says its steps in order, and the order is part of the rule. "
             "Times by 2 THEN add 1 is not the same machine as add 1 then times by 2 "
             "— feed them both a 4 and one puts out 9, the other 10.",
             '[[step eq="2 × 4 + 1 = 9 ✓"]][[step eq="(4 + 1) × 2 = 10 — a DIFFERENT machine"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. The rule is times by 3, then "
                        "add 2. Feed it 5: 3 times 5 equals 15, plus 2 equals 17.",
                        '[[machine input="5" rule="3x + 2" output="17" caption="in 5, out 17"]][[step eq="3 × 5 = 15"]][[step eq="15 + 2 = 17"]]'),
             "ask": {'a': 3, 'b': 2, 'c': 4, 'op': 'fm1'}},
            {"worked": ("One more together. Times by 4, then add 1. Feed it 3: 4 times 3 "
                        "equals 12, plus 1 equals 13.",
                        '[[machine input="3" rule="4x + 1" output="13" caption="in 3, out 13"]][[step eq="4 × 3 = 12"]][[step eq="12 + 1 = 13"]]'),
             "ask": {'a': 5, 'b': 3, 'c': 5, 'op': 'fm1'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The rule is times "
                       "by 2, then add 1, and a 4 goes in. Out comes 9. Tap the reason "
                       "why."),
            "choices": ("because the rule runs in order: 2 times 4, then 1 more | "
                        "because you add the 1 first, then times by 2 | because the "
                        "machine adds the 2, the 1 and the 4"),
            "answer": "because the rule runs in order: 2 times 4, then 1 more",
            "board": '[[machine input="4" rule="2x + 1" output="9" caption="in 4, out 9"]]',
        },
        "recap": [
            ("So, here it is again. A function is a machine with one rule. Feed it a "
             "number, run the rule in the order it says, and read what comes out. "
             "Change the order and you have a different machine.",
             '[[machine input="4" rule="2x + 1" output="9" caption="in 4, out 9"]]'),
            ("And that is a price into a price with tax, and a time into a distance.",
             '[[step eq="2 × 4 + 1 = 9"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! f of 3 means feed the machine 3.",
        "why": [
            ("Why a name? Because mathematicians got tired of drawing the machine, so "
             "they gave it one: f. And look under the machine — the board has been "
             "writing its shorthand all along. f of 4 equals 9 means: feed machine f "
             "the number 4, and 9 comes out. That is the whole code, and every "
             "textbook after this one speaks it.",
             '[[goal text="Saying f of x"]]'),
        ],
        "picture": [
            ("Here is machine f. Its rule is x plus 5. Feed it 3, and 3 plus 5 comes "
             "out: 8. Under the machine the board writes it the short way — f of 3 "
             "equals 8 — the name, the number that went in, and the number that came "
             "out.",
             '[[machine input="3" rule="x + 5" output="8" fname="f" caption="in 3, out 8 — written f(3) = 8"]]'),
        ],
        "teach": [
            ("That is the method. f of x equals x plus 5 — that is the rule, written "
             "with the name in front. So what is f of 3? Feed the machine 3: 3 plus "
             "5 equals 8. f of 3 equals 8.",
             '[[machine input="3" rule="x + 5" output="8" fname="f" caption="in 3, out 8"]][[step eq="f(3) = 3 + 5 = 8"]]'),
            ("Now the warning, and it is a fair one. In the distributive lesson, "
             "parentheses meant TIMES. Here, f followed by 3 in parentheses does NOT "
             "mean f times 3 — there is no timesing anywhere. It is the machine\'s "
             "name and its meal. Same marks, different job.",
             '[[step eq="f(3) = feed f the number 3 ✓"]][[step eq="f × 3 ✗ — nothing is being timesed"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you — a new machine, still called f. f of x equals x plus 4. f of "
                        "6: feed it 6, and 6 plus 4 equals 10.",
                        '[[machine input="6" rule="x + 4" output="10" fname="f" caption="f(6) = 6 + 4 = 10"]][[step eq="f(6) = 6 + 4 = 10"]]'),
             "ask": {'a': 3, 'b': 5, 'op': 'fnot'}},
            {"worked": ("One more together — a new machine, still called f. f of x equals x plus 2. f of 9 is 9 plus 2, "
                        "which equals 11.",
                        '[[machine input="9" rule="x + 2" output="11" fname="f" caption="f(9) = 9 + 2 = 11"]][[step eq="f(9) = 11"]]'),
             "ask": {'a': 7, 'b': 4, 'op': 'fnot'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Back to our first machine, f: f of x equals x "
                       "plus 5, so f of 3 is 8. Tap the reason why."),
            "choices": ("because f of 3 means feed the machine 3, not times | "
                        "because f of 3 means f times 3 | because the 3 in parentheses "
                        "is done first, then f"),
            "answer": "because f of 3 means feed the machine 3, not times",
            "board": '[[machine input="3" rule="x + 5" output="8" fname="f" caption="f(3) = 8"]]',
        },
        "recap": [
            ("So, here it is again, back to our first machine. f is the machine\'s name, and f of 3 means feed "
             "it 3. The parentheses hold the meal — nothing is timesed. Run the rule "
             "and write what came out: f of 3 equals 8.",
             '[[machine input="3" rule="x + 5" output="8" fname="f" caption="f(3) = 3 + 5 = 8"]]'),
            ("And that is the code every textbook after this one speaks.",
             '[[step eq="f(3) = 8"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "fnot"},
            {"a": 4, "b": 2, "op": "fnot"},
            {"a": 3, "b": 4, "op": "fnot"},
            {"a": 4, "b": 4, "op": "fnot"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! The first machine's output is the second machine's input.",
        "why": [
            ("Why two machines? Because machines can stand in a line, and the world "
             "is full of them lined up — a price gets a discount, THEN tax goes on. "
             "The first machine\'s out-door feeds the second machine\'s in-door. Two "
             "small rules in a row can do the work of one bigger rule.",
             '[[goal text="Two machines in a row"]]'),
        ],
        "picture": [
            ("Here are two machines, nose to tail. The first adds 2; the second times "
             "by 3. Feed a 4 into the first: 4 plus 2 is 6, and that 6 does not stop "
             "— it rolls straight into the second machine, where 6 times 3 is 18. In "
             "4, out 18.",
             '[[machine input="4" rule="x + 2" output="6" caption="machine one: in 4, out 6"]][[machine input="6" rule="3x" output="18" fname="g" caption="machine two: in 6, out 18"]]'),
        ],
        "teach": [
            ("That is the method. Feed the number through both, in order. Machine "
             "one: 4 plus 2 equals 6. That 6 goes into machine two: 6 times 3 equals "
             "18.",
             '[[machine input="4" rule="x + 2" output="6" caption="in 4, out 6"]][[machine input="6" rule="3x" output="18" fname="g" caption="in 6, out 18"]]'),
            ("The order is everything. Run the same two machines the other way round "
             "— times 3 first, then add 2 — and 4 becomes 12 becomes 14, not 18. "
             "Same machines, different line-up, different answer. Read WHICH machine "
             "is first before you feed anything.",
             '[[step eq="(4 + 2) × 3 = 18 ✓"]][[step eq="4 × 3 + 2 = 14 — the other order"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you — two new machines. First adds 3, second times by "
                        "2. Feed 5: 5 plus 3 equals 8, and 8 times 2 equals 16.",
                        '[[machine input="5" rule="x + 3" output="8" caption="in 5, out 8"]][[machine input="8" rule="2x" output="16" fname="g" caption="in 8, out 16"]]'),
             "ask": {'a': 2, 'b': 2, 'c': 5, 'op': 'fm2'}},
            {"worked": ("One more together — two new machines. First adds 2, second times by 4. Feed 3: 3 "
                        "plus 2 equals 5, and 5 times 4 equals 20.",
                        '[[machine input="3" rule="x + 2" output="5" caption="in 3, out 5"]][[machine input="5" rule="4x" output="20" fname="g" caption="in 5, out 20"]]'),
             "ask": {'a': 4, 'b': 4, 'c': 2, 'op': 'fm2'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Back to our first two machines: the first machine "
                       "adds 2, the second times by 3, and a 4 goes in. Out comes 18. "
                       "Tap the reason why."),
            "choices": ("because the 6 from machine one is what gets timesed | "
                        "because the 4 is timesed first, then the 2 goes on | because "
                        "both machines run on the 4 and the answers add"),
            "answer": "because the 6 from machine one is what gets timesed",
            "board": '[[machine input="4" rule="x + 2" output="6" caption="in 4, out 6"]][[machine input="6" rule="3x" output="18" fname="g" caption="in 6, out 18"]]',
        },
        "recap": [
            ("So, here it is again, back to our first two machines. Two machines in a row: what comes out of the "
             "first goes straight into the second. Read which machine is first, "
             "because the order changes the answer.",
             '[[machine input="4" rule="x + 2" output="6" caption="in 4, out 6"]][[machine input="6" rule="3x" output="18" fname="g" caption="in 6, out 18"]]'),
            ("And that is a discount and then a tax, in the right order.",
             '[[step eq="(4 + 2) × 3 = 18"]]'),
        ],
        "bank": [
            {"a": 2, "b": 2, "c": 3, "op": "fm2"},
            {"a": 2, "b": 3, "c": 2, "op": "fm2"},
            {"a": 2, "b": 2, "c": 4, "op": "fm2"},
            {"a": 2, "b": 3, "c": 3, "op": "fm2"},
            {"a": 3, "b": 3, "c": 2, "op": "fm2"},
            {"a": 2, "b": 5, "c": 2, "op": "fm2"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! Undo the rule and the input walks back out.",
        "why": [
            ("Why run it backwards? Because sometimes you know what came OUT and need "
             "what went in — the bill, and you want the price before tax. f of x "
             "equals x plus 3, and somebody tells you the machine put out 10, but not "
             "what went in. f of WHAT equals 10? The input is hiding, exactly like x "
             "hid on the balance.",
             '[[goal text="Which input was it"]]'),
        ],
        "picture": [
            ("Here is machine f with a blank at its in-door and a 10 at its out-door. "
             "The rule added 3 on the way through. So walk back through the machine "
             "the other way: undo the add, 10 take away 3, and a 7 appears at the "
             "in-door. Feed 7 forwards and 7 plus 3 is 10 — it fits.",
             '[[machine input="?" rule="x + 3" output="10" fname="f" caption="in ?, out 10 — run it backwards"]][[machine input="7" rule="x + 3" output="10" fname="f" caption="in 7, out 10 — it fits"]]'),
        ],
        "teach": [
            ("That is the method, and you already know the move. Something plus 3 "
             "came to 10 — that is an equation in machine clothes. Undo the rule: 10 "
             "take away 3 equals 7. The input was 7.",
             '[[machine input="?" rule="x + 3" output="10" fname="f" caption="in ?, out 10 — run it backwards"]][[step eq="? + 3 = 10"]][[step eq="? = 10 − 3 = 7"]]'),
            ("Check it by running the machine forwards: feed 7, and 7 plus 3 equals "
             "10. It fits. The careless move is running the machine forwards with "
             "the OUTPUT — feeding it the 10 and getting 13. The 10 came out of the "
             "machine; it never went in.",
             '[[step eq="f(7) = 10 ✓"]][[step eq="10 + 3 = 13 ✗ — the 10 came OUT, it never went in"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you — a new machine, still called f. f of x equals x plus 4, and "
                        "the output is 11. Undo: 11 take away 4 equals 7. The input "
                        "was 7.",
                        '[[machine input="?" rule="x + 4" output="11" fname="f" caption="in ?, out 11 — run it backwards"]][[machine input="7" rule="x + 4" output="11" fname="f" caption="f(7) = 11 ✓"]][[step eq="? = 11 − 4 = 7"]]'),
             "ask": {'a': 3, 'b': 13, 'op': 'fback'}},
            {"worked": ("One more together — a new machine, still called f. f of x equals x plus 2, and out came 15. "
                        "15 take away 2 equals 13 — the input was 13.",
                        '[[machine input="?" rule="x + 2" output="15" fname="f" caption="in ?, out 15 — run it backwards"]][[machine input="13" rule="x + 2" output="15" fname="f" caption="f(13) = 15 ✓"]][[step eq="? = 15 − 2 = 13"]]'),
             "ask": {'a': 6, 'b': 20, 'op': 'fback'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Back to our first machine, f: f of x equals x "
                       "plus 3, and f of what equals 10? The input was 7. Tap the "
                       "reason why."),
            "choices": ("because the machine added 3, so undo it: 10 take away 3 | "
                        "because you feed the 10 in, and 10 plus 3 is 13 | because the "
                        "input is always 3 less than the rule says"),
            "answer": "because the machine added 3, so undo it: 10 take away 3",
            "board": '[[machine input="7" rule="x + 3" output="10" fname="f" caption="f(7) = 10 ✓"]]',
        },
        "recap": [
            ("So, here it is again, back to our first machine. Told the output, undo the rule to walk back to "
             "the input — the undo of a plus is a take away — then run the machine "
             "forwards to check. The output came out; it never went in.",
             '[[machine input="7" rule="x + 3" output="10" fname="f" caption="? + 3 = 10 · ? = 7 · f(7) = 10"]]'),
            ("And that is the price before tax, found from the bill.",
             '[[step eq="f(?) = 10, so ? = 7"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Every point is an input standing under its output.",
        "why": [
            ("Why a graph? Because last unit the machine answered one input at a "
             "time. A graph answers ALL of them at once. The rule y equals x plus 2 "
             "becomes a line on the grid, and every x along the bottom has its answer "
             "waiting straight above it.",
             '[[goal text="Reading the line"]]'),
        ],
        "picture": [
            ("Here is y equals x plus 2 as a line. Pick x equals 5 along the bottom "
             "and climb straight up until you hit the line. The height you reach is "
             "7 — because 5 plus 2 is 7. That spot is the point 5 comma 7: the input "
             "and its output, standing together.",
             '[[graph lines="y=x+2" points="(5,7)" range="0..9" caption="y = x + 2 — climb from x = 5 to the point (5, 7)"]]'),
        ],
        "teach": [
            ("That is the method. What is y when x is 5? Find 5 along the bottom, "
             "climb up to the line, and read the height: 5 plus 2 equals 7. The "
             "point sits at 5 comma 7.",
             '[[graph lines="y=x+2" points="(5,7)" range="0..9" caption="the point (5, 7)"]][[step eq="x = 5"]][[step eq="y = 5 + 2 = 7"]]'),
            ("Keep the partners straight. The first number is the x you were given; "
             "the second is the y you found. At 5 comma 7, the answer to the question "
             "what is y is 7 — not the 5 you started from.",
             '[[step eq="(5, 7): x = 5, y = 7"]][[step eq="y = 5 ✗ — that is the input"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals x plus 4, and x is 2. "
                        "Climb: 2 plus 4 equals 6. The point is 2 comma 6, and y is 6.",
                        '[[graph lines="y=x+4" points="(2,6)" range="0..8" caption="y = x + 4 — the point (2, 6)"]][[step eq="y = 2 + 4 = 6"]]'),
             "ask": {'a': 3, 'b': 6, 'op': 'lny'}},
            {"worked": ("One more together. y equals x plus 5, and x is 4. Climb: 4 plus "
                        "5 equals 9. The point is 4 comma 9, so y is 9.",
                        '[[graph lines="y=x+5" points="(4,9)" range="0..11" caption="y = x + 5 — the point (4, 9)"]][[step eq="y = 4 + 5 = 9"]]'),
             "ask": {'a': 7, 'b': 6, 'op': 'lny'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the line y "
                       "equals x plus 2, when x is 5, y is 7. Tap the reason why."),
            "choices": ("because the height above 5 on the line is 5 plus 2 | "
                        "because the first number of the point is the answer | because "
                        "the line adds 2 to the height, so y is 9"),
            "answer": "because the height above 5 on the line is 5 plus 2",
            "board": '[[graph lines="y=x+2" points="(5,7)" range="0..9" caption="the point (5, 7): x = 5, y = 7"]]',
        },
        "recap": [
            ("So, here it is again. A line is a rule drawn out. Find the x along the "
             "bottom, climb to the line, read the height — that is y. The point is "
             "the input standing under its output, and the answer is the second "
             "number.",
             '[[graph lines="y=x+2" points="(5,7)" range="0..9" caption="x = 5 · climb · y = 7"]]'),
            ("And that is every input answered at once, on one picture.",
             '[[step eq="y = x + 2 at x = 5: y = 7"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "lny"},
            {"a": 2, "b": 4, "op": "lny"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! The slope is the climb, not the height.",
        "why": [
            ("Why the climb? Because lines are straight, and straight means FAIR: "
             "every time x steps one to the right, y climbs by the same amount. That "
             "amount — the climb per step — is called the slope. It is the line\'s "
             "personality: big slope, steep line; small slope, gentle line.",
             '[[goal text="The climb of a line"]]'),
        ],
        "picture": [
            ("Here are two points on a line: 2 comma 3, and 3 comma 5. From the first "
             "to the second, x stepped once to the right — 2 to 3. And y climbed from "
             "3 up to 5: a climb of 2. Draw the line through them and it climbs 2 for "
             "every step, all the way along.",
             '[[graph lines="y=2x-1" points="(2,3),(3,5)" range="0..5" caption="one step right, 2 up — the slope is 2"]]'),
        ],
        "teach": [
            ("That is the method. Take two neighbouring points, one step apart. y "
             "went from 3 to 5, and 5 take away 3 equals 2. The slope is 2 — and it "
             "is 2 between ANY two neighbouring steps on this line.",
             '[[graph points="(2,3),(3,5)" range="0..5" caption="from (2, 3) to (3, 5)"]][[step eq="y: 3 → 5"]][[step eq="slope = 5 − 3 = 2"]]'),
            ("The slope is the CLIMB, not the height. This line reaches height 5, "
             "but its slope is not 5 — 5 is where y landed, and 3 is where it "
             "started. The slope is the difference between them: how far y MOVED.",
             '[[step eq="slope = 5 − 3 = 2 ✓"]][[step eq="slope = 5 ✗ — that is a height, not a climb"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Through 1 comma 4 and 2 comma "
                        "7. y went from 4 to 7 — a climb of 3. The slope is 3.",
                        '[[graph lines="y=3x+1" points="(1,4),(2,7)" range="0..4" caption="one step right, 3 up — slope 3"]][[step eq="7 − 4 = 3"]]'),
             "ask": {'a': 3, 'b': 2, 'c': 5, 'op': 'slp'}},
            {"worked": ("One more together. Through 2 comma 2 and 3 comma 6. From 2 up "
                        "to 6 is a climb of 4 — the slope is 4.",
                        '[[graph lines="y=4x-6" points="(2,2),(3,6)" range="0..5" caption="one step right, 4 up — slope 4"]][[step eq="6 − 2 = 4"]]'),
             "ask": {'a': 6, 'b': 3, 'c': 4, 'op': 'slp'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. A line goes "
                       "through 2 comma 3 and 3 comma 5, and its slope is 2. Tap the "
                       "reason why."),
            "choices": ("because y climbed from 3 to 5 while x stepped once | because "
                        "the line reaches a height of 5 | because the slope is the "
                        "first number of the first point"),
            "answer": "because y climbed from 3 to 5 while x stepped once",
            "board": '[[graph lines="y=2x-1" points="(2,3),(3,5)" range="0..5" caption="one step right, 2 up — slope 2"]]',
        },
        "recap": [
            ("So, here it is again. The slope is how far y climbs when x steps one to "
             "the right — the second height take away the first. It is a climb, "
             "never a height, and it is the same between every pair of steps on the "
             "line.",
             '[[graph lines="y=2x-1" points="(2,3),(3,5)" range="0..5" caption="slope = 5 − 3 = 2"]]'),
            ("And that is a line\'s personality in one number.",
             '[[step eq="slope = 5 − 3 = 2"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! At x equals zero, the times part vanishes.",
        "why": [
            ("Why the start? Because every line has a starting height: where it "
             "stands when x is zero, right at the left wall of the grid. A rule like "
             "y equals 2 x plus 3 tells you that height without any drawing — put "
             "zero in for x and watch what happens.",
             '[[goal text="Where the line starts"]]'),
        ],
        "picture": [
            ("Here is y equals 2 x plus 3 on the grid. Look at the left wall, where x "
             "is zero. The line stands at height 3 there — that is the point 0 comma "
             "3 — and it does all its climbing from that start.",
             '[[graph lines="y=2x+3" points="(0,3)" range="0..5" caption="y = 2x + 3 — at x = 0 the line stands at 3"]]'),
        ],
        "teach": [
            ("That is the method. y equals 2 times zero plus 3. But 2 times zero is "
             "ZERO — the whole times part vanishes. All that is left is the plus 3. "
             "So at x equals zero, y equals 3.",
             '[[graph lines="y=2x+3" points="(0,3)" range="0..5" caption="the start: (0, 3)"]][[step eq="y = 2 × 0 + 3"]][[step eq="y = 0 + 3 = 3"]]'),
            ("So in y equals 2 x plus 3, the two numbers have two different jobs: the "
             "2 is the climb per step, and the 3 is where the climbing starts. Asked "
             "where the line starts, the answer is the plus number — not the 2.",
             '[[step eq="start = 3 ✓"]][[step eq="start = 2 ✗ — that is the climb, not the start"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals 4 x plus 5. At x "
                        "equals zero, 4 times zero vanishes, and y equals 5.",
                        '[[graph lines="y=4x+5" points="(0,5)" range="0..5" caption="at x = 0 the line stands at 5"]][[step eq="y = 4 × 0 + 5 = 5"]]'),
             "ask": {'a': 4, 'b': 3, 'op': 'yint'}},
            {"worked": ("One more together. y equals 3 x plus 7. At zero, y equals 7 — "
                        "that is the starting height.",
                        '[[graph lines="y=3x+7" points="(0,7)" range="0..5" caption="at x = 0 the line stands at 7"]][[step eq="y = 3 × 0 + 7 = 7"]]'),
             "ask": {'a': 6, 'b': 8, 'op': 'yint'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The line y equals "
                       "2 x plus 3 starts at height 3. Tap the reason why."),
            "choices": ("because 2 times zero vanishes, and only the plus 3 is left | "
                        "because the first number in the rule is the start | because at "
                        "x equals zero, y is 2 plus 3"),
            "answer": "because 2 times zero vanishes, and only the plus 3 is left",
            "board": '[[graph lines="y=2x+3" points="(0,3)" range="0..5" caption="the start: (0, 3)"]]',
        },
        "recap": [
            ("So, here it is again. A line starts where x is zero, at the left wall. "
             "Put zero in for x: the times part vanishes, and the plus number is the "
             "starting height. The other number is the climb, and it has a different "
             "job.",
             '[[graph lines="y=2x+3" points="(0,3)" range="0..5" caption="y = 2 × 0 + 3 = 3"]]'),
            ("And that is a line read at its left wall, with no drawing needed.",
             '[[step eq="y = 2 × 0 + 3 = 3"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Start at the plus number, climb the slope once per step.",
        "why": [
            ("Why put the two together? Because y equals 3 x plus 2 is the whole "
             "line in one sentence: start at height 2, and climb 3 for every step x "
             "takes. Two numbers, two jobs — and between them they answer any x you "
             "like.",
             '[[goal text="Start plus climb"]]'),
        ],
        "picture": [
            ("Here is y equals 3 x plus 2. It starts at height 2 on the left wall. "
             "Now walk x out to 4: four steps, each a climb of 3, is 12 of climbing. "
             "12 on top of the start of 2 is 14, and there is the point 4 comma 14, "
             "right on the line.",
             '[[graph lines="y=3x+2" points="(0,2),(4,14)" range="0..6" caption="start 2, four steps of 3 — the point (4, 14)"]]'),
        ],
        "teach": [
            ("That is the method. What is y when x is 4? Four steps, each a climb of "
             "3: 3 times 4 equals 12 of climbing. Add the start: 12 plus 2 equals 14. "
             "The line stands at height 14 over x equals 4.",
             '[[graph lines="y=3x+2" points="(4,14)" range="0..6" caption="the point (4, 14)"]][[step eq="y = 3 × 4 + 2"]][[step eq="12 + 2 = 14"]]'),
            ("Count your steps carefully. The height at x equals 4 is 14; one step "
             "earlier, at x equals 3, it was only 11. Stopping a step short is the "
             "easiest mistake on a grid — land on the x you were asked about, then "
             "read the height.",
             '[[step eq="x = 4: 14 ✓"]][[step eq="x = 3: 11 ✗ — one step short"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals 2 x plus 5, at x "
                        "equals 3. Climb: 2 times 3 equals 6. Start: plus 5. y equals 11.",
                        '[[graph lines="y=2x+5" points="(3,11)" range="0..5" caption="start 5, three steps of 2 — the point (3, 11)"]][[step eq="y = 2 × 3 + 5 = 11"]]'),
             "ask": {'a': 2, 'b': 3, 'c': 4, 'op': 'lin2'}},
            {"worked": ("One more together. y equals 4 x plus 1, at x equals 5: 4 times 5 "
                        "equals 20, plus 1 equals 21.",
                        '[[graph lines="y=4x+1" points="(5,21)" range="0..7" caption="start 1, five steps of 4 — the point (5, 21)"]][[step eq="y = 4 × 5 + 1 = 21"]]'),
             "ask": {'a': 5, 'b': 3, 'c': 5, 'op': 'lin2'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the line y "
                       "equals 3 x plus 2, when x is 4, y is 14. Tap the reason why."),
            "choices": ("because four steps of 3 is 12, plus the start of 2 | "
                        "because 3 plus 2 is 5, and 5 climbs to 14 | because the line "
                        "starts at 3 and climbs 2 four times"),
            "answer": "because four steps of 3 is 12, plus the start of 2",
            "board": '[[graph lines="y=3x+2" points="(4,14)" range="0..6" caption="the point (4, 14)"]]',
        },
        "recap": [
            ("So, here it is again. y equals 3 x plus 2 means start at 2 and climb 3 "
             "per step. For any x, times the climb by the steps, then add the start "
             "— and land on the x you were asked about, not one short.",
             '[[graph lines="y=3x+2" points="(4,14)" range="0..6" caption="3 × 4 + 2 = 14"]]'),
            ("And that is the whole line, answering any x you like.",
             '[[step eq="y = 3 × 4 + 2 = 14"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! The crossing is where both rules tell the same story.",
        "why": [
            ("Why two rules? Because two rules can both talk about the same x and y. "
             "One says y equals x plus 2. Another says y equals 3 times x. Usually "
             "they disagree — feed them the same x and they give different y\'s. But "
             "two straight lines that are not parallel cross somewhere, and at the "
             "crossing they agree.",
             '[[goal text="Where two rules agree"]]'),
        ],
        "picture": [
            ("Here are both rules on one grid: two lines, and they cross. At the "
             "crossing, both rules give the SAME y. Try x equals 1: the first rule "
             "says 1 plus 2, which is 3; the second says 3 times 1, which is 3. They "
             "agree — and that is what the crossing point means.",
             '[[graph lines="y=x+2; y=3x" range="0..4" caption="both rules on one grid — they cross at (1, 3)"]]'),
        ],
        "teach": [
            ("That is the method. The crossing is the one x where both lines stand at "
             "the same height. You can find it without the picture too: if both "
             "rules give the same y, then x plus 2 EQUALS 3 x — an equation, and you "
             "know what to do with equations. It is true at x equals 1.",
             '[[graph lines="y=x+2; y=3x" range="0..4" caption="they cross at (1, 3)"]][[step eq="x + 2 = 3x"]][[step eq="true at x = 1: 3 = 3"]]'),
            ("Keep the question straight. The answer asked for is the x of the "
             "crossing, not its height. Both rules say 3 there — but 3 is the y, and "
             "the x is 1.",
             '[[step eq="x = 1 ✓"]][[step eq="y = 3 is the HEIGHT, not the x"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals x plus 4, and y equals "
                        "3 times x. They agree where x plus 4 equals 3 x — at x equals "
                        "2, where both say 6.",
                        '[[graph lines="y=x+4; y=3x" range="0..5" caption="they cross at (2, 6) — the x is 2"]][[step eq="x + 4 = 3x"]][[step eq="x = 2"]]'),
             "ask": {'a': 10, 'b': 6, 'op': 'sys1'}},
            {"worked": ("One more together. y equals x plus 6, and y equals 4 times x. x "
                        "plus 6 equals 4 x at x equals 2, where both rules say 8.",
                        '[[graph lines="y=x+6; y=4x" range="0..5" caption="they cross at (2, 8) — the x is 2"]][[step eq="x + 6 = 4x"]][[step eq="x = 2"]]'),
             "ask": {'a': 12, 'b': 5, 'op': 'sys1'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. y equals x plus 2 "
                       "and y equals 3 x agree at x equals 1. Tap the reason why."),
            "choices": ("because at x equals 1 both rules give the same y | because "
                        "the lines cross at height 3, so x is 3 | because the "
                        "plus number, 2, is always where lines cross"),
            "answer": "because at x equals 1 both rules give the same y",
            "board": '[[graph lines="y=x+2; y=3x" range="0..4" caption="they cross at (1, 3) — the x is 1"]]',
        },
        "recap": [
            ("So, here it is again. Two rules on one grid cross once, and the crossing "
             "is the x where both give the same y. Set the two rules equal and solve, "
             "or read the crossing — and answer with its x, not its height.",
             '[[graph lines="y=x+2; y=3x" range="0..4" caption="x + 2 = 3x at x = 1"]]'),
            ("And that is two stories agreeing at exactly one point.",
             '[[step eq="x + 2 = 3x at x = 1"]]'),
        ],
        "bank": [
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
        "advance_line": "Three in a row, and you can say why — you've got it! Swap y for what it equals, and one letter is left.",
        "why": [
            ("Why swap? Because here is the strongest trick in this whole unit. If "
             "one rule TELLS you what y equals, you can swap y out of the other rule "
             "entirely — write what it equals in its place. Two letters become one, "
             "and one letter you can solve.",
             '[[goal text="Swapping a letter in"]]'),
        ],
        "picture": [
            ("Here is x plus y equals 10 as a bar that weighs 10. The first rule says "
             "y is x plus 2 — so the y piece is really an x piece and a 2. Swap it "
             "in, and the bar holds two x\'s and a 2. Take the 2 off and two x\'s "
             "are 8, so one x is 4.",
             '[[tape parts="x | x | 2" total="10" caption="x + y = 10, and y = x + 2 — two x\'s and a 2"]][[tape parts="4 | 4 | 2" total="10" caption="x = 4 · y = 6"]]'),
        ],
        "teach": [
            ("That is the method. y equals x plus 2. Also, x plus y equals 10. Swap "
             "the y in the second rule for x plus 2: x plus x plus 2 equals 10. That "
             "is 2 x plus 2 equals 10 — so 2 x equals 8, and x equals 4.",
             '[[tape parts="x | x | 2" total="10" caption="two x\'s and a 2 weigh 10"]][[step eq="x + (x + 2) = 10"]][[step eq="2x = 8"]][[step eq="x = 4"]]'),
            ("Two cares. First: after the swap there are TWO x\'s — count them. "
             "Second: the question asked for x. y is 6 here, and 6 is also standing "
             "in the problem waiting to be tapped — but it is the other letter\'s "
             "answer, not yours.",
             '[[step eq="x = 4 ✓ · y = 6 — the OTHER letter"]][[step eq="check: 4 + 6 = 10 ✓"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals x plus 4, and x plus y "
                        "equals 12. Swap: x plus x plus 4 equals 12, so 2 x equals 8, "
                        "and x equals 4.",
                        '[[tape parts="4 | 4 | 4" total="12" caption="two x\'s and a 4 weigh 12 — x = 4"]][[step eq="2x + 4 = 12"]][[step eq="x = 4"]]'),
             "ask": {'a': 5, 'b': 13, 'op': 'sys2'}},
            {"worked": ("One more together. y equals x plus 3, and x plus y equals 11. "
                        "Swap: 2 x plus 3 equals 11, so x equals 4.",
                        '[[tape parts="4 | 4 | 3" total="11" caption="two x\'s and a 3 weigh 11 — x = 4"]][[step eq="2x + 3 = 11"]][[step eq="x = 4"]]'),
             "ask": {'a': 7, 'b': 23, 'op': 'sys2'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. y equals x plus 2, "
                       "and x plus y equals 10, so x is 4. Tap the reason why."),
            "choices": ("because swapping y in leaves two x\'s and a 2 weighing 10 | "
                        "because 10 shared between x and y is 5 each | because y is 6, "
                        "and 6 is the bigger letter"),
            "answer": "because swapping y in leaves two x\'s and a 2 weighing 10",
            "board": '[[tape parts="4 | 4 | 2" total="10" caption="x = 4 · y = 6 · 4 + 6 = 10"]]',
        },
        "recap": [
            ("So, here it is again. When one rule says what y equals, swap that in "
             "for y in the other rule. One letter is left; count the x\'s, solve, and "
             "answer with the letter you were asked for.",
             '[[tape parts="x | x | 2" total="10" caption="x + (x + 2) = 10 · x = 4"]]'),
            ("And that is two letters turned into one.",
             '[[step eq="x + (x + 2) = 10, so x = 4"]]'),
        ],
        "bank": [
            {"a": 3, "b": 7, "op": "sys2"},
            {"a": 4, "b": 8, "op": "sys2"},
            {"a": 2, "b": 8, "op": "sys2"},
            {"a": 5, "b": 11, "op": "sys2"},
            {"a": 7, "b": 15, "op": "sys2"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! Add the two clues and the smaller number cancels itself away.",
        "why": [
            ("Why two clues? Because this is the oldest puzzle with two unknowns: two "
             "secret numbers, and two clues. Put together they equal 10. Their "
             "difference — the bigger take away the smaller — equals 4. Neither clue "
             "alone is enough; together they trap the answer completely.",
             '[[goal text="The sum and the difference"]]'),
        ],
        "picture": [
            ("Here are the two secret numbers as one bar, weighing 10 together. And "
             "here is the bigger one on its own: it is the smaller one and 4 more. So "
             "the bar is really the smaller, the smaller, and 4. Two smallers and a "
             "4 make 10, so two smallers make 6 and the smaller is 3. The bigger is "
             "3 and 4: 7.",
             '[[tape parts="bigger | smaller" total="10" caption="together 10"]][[tape parts="3 | 4 | 3" total="10" caption="the bigger is the smaller and 4 more: 7 and 3"]]'),
        ],
        "teach": [
            ("That is the method — the trap closing. Add the two clues: big plus "
             "small, plus big take away small — the small cancels itself away, leaving "
             "two bigs. 10 plus 4 equals 14, so two bigs equal 14, and the big one is "
             "7. The small one is what is left: 3.",
             '[[tape parts="7 | 3" total="10" caption="7 + 3 = 10 · 7 − 3 = 4"]][[step eq="two bigs = 10 + 4 = 14"]][[step eq="big = 7 · small = 3"]]'),
            ("Check both clues: 7 plus 3 equals 10, and 7 take away 3 equals 4. Both "
             "happy. The lazy answer is 5 — half of 10 — but that ignores the second "
             "clue entirely: 5 and 5 have no difference at all.",
             '[[step eq="7 + 3 = 10 ✓ · 7 − 3 = 4 ✓"]][[step eq="5 and 5 ✗ — their difference is 0, not 4"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Together 12, difference 2. Two "
                        "bigs equal 14, so the bigger is 7 and the smaller is 5.",
                        '[[tape parts="7 | 5" total="12" caption="7 + 5 = 12 · 7 − 5 = 2"]][[step eq="two bigs = 12 + 2 = 14"]][[step eq="big = 7"]]'),
             "ask": {'a': 8, 'b': 6, 'op': 'sumd'}},
            {"worked": ("One more together. Together 16, difference 6. Two bigs equal "
                        "22, the bigger is 11, the smaller is 5.",
                        '[[tape parts="11 | 5" total="16" caption="11 + 5 = 16 · 11 − 5 = 6"]][[step eq="two bigs = 16 + 6 = 22"]][[step eq="big = 11"]]'),
             "ask": {'a': 22, 'b': 6, 'op': 'sumd'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Together 10, "
                       "difference 4, and the bigger number is 7. Tap the reason why."),
            "choices": ("because adding the clues leaves two bigs, 14 | "
                        "because half of 10 is 5, and 5 is the bigger | because the "
                        "bigger is the difference, 4, and 3 more"),
            "answer": "because adding the clues leaves two bigs, 14",
            "board": '[[tape parts="7 | 3" total="10" caption="7 + 3 = 10 · 7 − 3 = 4"]]',
        },
        "recap": [
            ("So, here it is again. Two clues, together and apart: add them and the "
             "smaller cancels itself away, leaving two bigs. Halve that for the "
             "bigger; the smaller is what is left. Then check both clues.",
             '[[tape parts="7 | 3" total="10" caption="two bigs = 14 · big 7 · small 3"]]'),
            ("And that is two secret numbers, trapped by two clues.",
             '[[step eq="big = (10 + 4) ÷ 2 = 7"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Take one buy away from the other and a whole unknown vanishes.",
        "why": [
            ("Why two shopping trips? Because nobody told you what anything costs, "
             "and yet you can work it out. Trip one: two pencils and an eraser, 14 "
             "cents. Trip two: one pencil and the same eraser, 9 cents. Two unknowns, "
             "two receipts — and one of the unknowns is about to vanish.",
             '[[goal text="The eraser vanishes"]]'),
        ],
        "picture": [
            ("Here are the two trips as bars. Trip one: pencil, pencil, eraser — 14 "
             "cents. Trip two: pencil, eraser — 9 cents. Lay them side by side and the "
             "only difference is one pencil. So one pencil is 14 take away 9: 5 cents.",
             '[[tape parts="pencil | pencil | eraser" total="14" caption="trip one: 14 cents"]][[tape parts="pencil | eraser" total="9" caption="trip two: 9 cents — the difference is one pencil"]]'),
        ],
        "teach": [
            ("That is the method. Take the second trip away from the first. The "
             "eraser is in both, so it vanishes. One pencil is left over on one side, "
             "and 14 take away 9 equals 5 on the other. A pencil costs 5 cents.",
             '[[tape parts="5 | 5 | 4" total="14" caption="pencil 5, pencil 5, eraser 4"]][[step eq="difference: 1 pencil = 14 − 9 = 5"]]'),
            ("And the eraser? Put the pencil back into trip two: 5 plus eraser "
             "equals 9, so the eraser is 4 cents. Careful when you tap — 4 is the "
             "ERASER\'S price, and the question asked for the pencil. A system holds "
             "two answers, and only one of them is yours.",
             '[[step eq="pencil = 5 ✓ · eraser = 4 — the other unknown"]][[step eq="check: 2 × 5 + 4 = 14 ✓"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Two pencils and an eraser, 12 "
                        "cents; one pencil and the eraser, 7. Take away: one pencil "
                        "equals 5 cents.",
                        '[[tape parts="pencil | pencil | eraser" total="12" caption="12 cents"]][[tape parts="pencil | eraser" total="7" caption="7 cents"]][[step eq="1 pencil = 12 − 7 = 5"]]'),
             "ask": {'a': 18, 'b': 13, 'op': 'elim'}},
            {"worked": ("One more together. Two pencils and an eraser, 16 cents; one "
                        "pencil and the eraser, 9. The pencil is 16 take away 9 — 7 "
                        "cents.",
                        '[[tape parts="pencil | pencil | eraser" total="16" caption="16 cents"]][[tape parts="pencil | eraser" total="9" caption="9 cents"]][[step eq="1 pencil = 16 − 9 = 7"]]'),
             "ask": {'a': 24, 'b': 13, 'op': 'elim'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Two pencils and an "
                       "eraser are 14 cents; one pencil and the eraser are 9. A pencil "
                       "is 5 cents. Tap the reason why."),
            "choices": ("because the trips differ by one pencil, 14 take away 9 | "
                        "because 14 shared between the two pencils is 7 | because the "
                        "eraser is 4, and 4 is the pencil too"),
            "answer": "because the trips differ by one pencil, 14 take away 9",
            "board": '[[tape parts="5 | 5 | 4" total="14" caption="pencil 5 · pencil 5 · eraser 4"]][[tape parts="5 | 4" total="9" caption="5 + 4 = 9"]]',
        },
        "recap": [
            ("So, here it is again. Two buys with the same unknown in both: take one "
             "away from the other and that unknown vanishes, leaving the other one "
             "alone. Then answer with the one you were asked for.",
             '[[tape parts="5 | 5 | 4" total="14" caption="14 − 9 = one pencil = 5"]]'),
            ("And that is a price found with no price ever told.",
             '[[step eq="1 pencil = 14 − 9 = 5"]]'),
        ],
        "bank": [
            {"a": 10, "b": 8, "op": "elim"},
            {"a": 8, "b": 5, "op": "elim"},
            {"a": 10, "b": 7, "op": "elim"},
            {"a": 10, "b": 6, "op": "elim"},
            {"a": 16, "b": 11, "op": "elim"},
            {"a": 14, "b": 8, "op": "elim"},
            {"a": 18, "b": 11, "op": "elim"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! Multiplying powers ADDS the counts.",
        "why": [
            ("Why count copies? Because you know x to the power 3 means three x\'s "
             "multiplied. So what is x to the 3, times x to the 2? Do not guess — "
             "WRITE IT OUT and count. A power is just a count of copies, and counts "
             "you can see.",
             '[[goal text="Counting the copies"]]'),
        ],
        "picture": [
            ("Here is x to the 3 times x to the 2 written out as a bar: three x\'s "
             "multiplied, then two more x\'s multiplied, all in one row. Count them "
             "along the bar: one, two, three, four, five. Five x\'s — x to the "
             "power 5.",
             '[[tape parts="x | x | x | x | x" total="x⁵" caption="x³ · x² written out — 3 x\'s then 2 more: 5 x\'s"]]'),
        ],
        "teach": [
            ("That is the whole rule: when powers of x multiply, their counts ADD. 3 "
             "x\'s and 2 x\'s are 5 x\'s — the same way 3 apples and 2 apples are 5 "
             "apples. The power is just a count.",
             '[[tape parts="x | x | x | x | x" total="x⁵" caption="3 + 2 = 5 x\'s"]][[step eq="x³ · x² = (x · x · x) · (x · x)"]][[step eq="x³ · x² = x⁵"]]'),
            ("The tempting wrong move is timesing the powers: 3 times 2 equals 6, so "
             "x to the 6. Write it out and count — there are only five x\'s on the "
             "page. Nothing here made copies of copies; two piles just joined.",
             '[[step eq="x³ · x² = x⁵ ✓"]][[step eq="x⁶ ✗ — count the x\'s: there are 5"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x to the 4 times x to the 3. "
                        "Four x\'s joined by three more: seven x\'s, so x to the 7.",
                        '[[tape parts="x | x | x | x | x | x | x" total="x⁷" caption="4 + 3 = 7 x\'s"]][[step eq="x⁴ · x³ = x⁷"]]'),
             "ask": {'a': 3, 'b': 7, 'op': 'exadd'}},
            {"worked": ("One more together. x to the 5 times x to the 2: five x\'s and "
                        "two x\'s are SEVEN x\'s. x to the 7.",
                        '[[tape parts="x | x | x | x | x | x | x" total="x⁷" caption="5 + 2 = 7 x\'s"]][[step eq="x⁵ · x² = x⁷"]]'),
             "ask": {'a': 4, 'b': 6, 'op': 'exadd'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x to the 3 times "
                       "x to the 2 is x to the 5. Tap the reason why."),
            "choices": ("because three x\'s joined by two x\'s is five x\'s | because "
                        "3 times 2 is 6, so the power is 6 | because the bigger power "
                        "wins when powers multiply"),
            "answer": "because three x\'s joined by two x\'s is five x\'s",
            "board": '[[tape parts="x | x | x | x | x" total="x⁵" caption="x³ · x² = x⁵"]]',
        },
        "recap": [
            ("So, here it is again. A power is a count of copies. When powers of x "
             "multiply, the piles join and the counts add — write them out and count "
             "if you are ever unsure.",
             '[[tape parts="x | x | x | x | x" total="x⁵" caption="x³ · x² = x⁵"]]'),
            ("And that is apples and apples, with a power in place of the apple.",
             '[[step eq="x³ · x² = x⁵"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Copies of copies times the counts.",
        "why": [
            ("Why a second rule? Because now comes the OTHER situation, and it looks "
             "teasingly similar. Take x to the 3 — all of it, parentheses around it — "
             "and raise THAT to the power 2. That means two copies of the whole "
             "thing: two copies of three x\'s.",
             '[[goal text="Copies of copies"]]'),
        ],
        "picture": [
            ("Here is x to the 3, all of it, raised to the power 2, as a bar: two "
             "groups side by side, and each group is three x\'s. Two groups of three "
             "is 3 times 2, which equals 6 x\'s. x to the power 6.",
             '[[tape parts="x³ | x³" total="x⁶" caption="(x³)² — two copies of three x\'s: 6 x\'s"]]'),
        ],
        "teach": [
            ("That is the rule: a power OF a power TIMES the counts — because you are "
             "making copies of copies, and copies of copies is exactly what timesing "
             "counts. Two copies of three x\'s: 3 times 2 equals 6.",
             '[[tape parts="x³ | x³" total="x⁶" caption="2 copies of 3 x\'s"]][[step eq="(x³)² = (x · x · x) · (x · x · x)"]][[step eq="(x³)² = x⁶"]]'),
            ("Yesterday multiplying powers ADDED; today a power of a power TIMES — "
             "and telling the two apart is the entire skill. Ask one question: am I "
             "JOINING two piles, or COPYING a whole pile? Joining adds. Copying "
             "times.",
             '[[step eq="x³ · x² = x⁵ — joining, ADD"]][[step eq="(x³)² = x⁶ — copying, TIMES"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x to the 4, all raised to the "
                        "power 2. Two copies of four x\'s: 4 times 2 equals 8, so x to "
                        "the 8.",
                        '[[tape parts="x⁴ | x⁴" total="x⁸" caption="2 copies of 4 x\'s — 8 x\'s"]][[step eq="(x⁴)² = x⁸"]]'),
             "ask": {'a': 3, 'b': 4, 'op': 'exmul'}},
            {"worked": ("One more together. x to the 2, raised to the power 5. Five "
                        "copies of two x\'s is 10: x to the 10.",
                        '[[tape parts="x² | x² | x² | x² | x²" total="x¹⁰" caption="5 copies of 2 x\'s — 10 x\'s"]][[step eq="(x²)⁵ = x¹⁰"]]'),
             "ask": {'a': 5, 'b': 4, 'op': 'exmul'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x to the 3, all "
                       "raised to the power 2, is x to the 6. Tap the reason why."),
            "choices": ("because it is two copies of three x\'s, and copies times | "
                        "because 3 and 2 join into one pile of 5 | because the outside "
                        "power is the answer on its own"),
            "answer": "because it is two copies of three x\'s, and copies times",
            "board": '[[tape parts="x³ | x³" total="x⁶" caption="(x³)² = x⁶"]]',
        },
        "recap": [
            ("So, here it is again. A power of a power is copies of copies, and "
             "copies of copies times the counts. Joining two piles adds; copying a "
             "whole pile times. Ask which one you are doing.",
             '[[tape parts="x³ | x³" total="x⁶" caption="(x³)² = x⁶"]]'),
            ("And that is the two power rules, told apart.",
             '[[step eq="(x³)² = x⁶"]]'),
        ],
        "bank": [
            {"a": 2, "b": 3, "op": "exmul"},
            {"a": 2, "b": 4, "op": "exmul"},
            {"a": 3, "b": 3, "op": "exmul"},
            {"a": 5, "b": 2, "op": "exmul"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! The power counts the zeros.",
        "why": [
            ("Why powers of ten? Because they are the friendliest powers there are. "
             "10 to the power 3 is 10 times 10 times 10, which equals 1000 — a one "
             "with three zeros. The power counts the zeros, and that is why "
             "scientists write huge numbers this way.",
             '[[goal text="Times ten, again and again"]]'),
        ],
        "picture": [
            ("Here is a 6 on the place-value chart, sitting in the ones. Times it by "
             "10 to the power 2 — that is 10 times 10, a hundred. The 6 moves two "
             "places up the chart, into the hundreds, with two zeros marching behind "
             "it. 6 times 10 to the 2 is 600.",
             '[[placevalue n="6" caption="6 in the ones"]][[placevalue n="600" caption="6 × 10² = 600 — two places up, two zeros behind"]]'),
        ],
        "teach": [
            ("That is the method. Put a digit in front of a power of ten: 6 times 10 "
             "to the power 2 is 6 times 100, which equals 600 — the 6 with two zeros "
             "behind it. The power says how many places the digit moves.",
             '[[placevalue n="600" caption="6 × 10² = 600"]][[step eq="6 × 10² = 6 × 100 = 600"]]'),
            ("The trap is reading the power as a TIMES: 6 times 10 times 2 equals "
             "120, and 120 is nowhere near 600. The 2 up there is not a number to "
             "times by — it is a count of how many times the ten itself appears.",
             '[[step eq="6 × 10² = 600 ✓"]][[step eq="6 × 10 × 2 = 120 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 7 times 10 to the 3. That is 7 "
                        "times 1000 — 7000, the 7 with three zeros behind it.",
                        '[[placevalue n="7000" caption="7 × 10³ = 7000"]][[step eq="7 × 10³ = 7000"]]'),
             "ask": {'a': 2, 'b': 4, 'op': 'sci'}},
            {"worked": ("One more together. 8 times 10 to the 2. That is 8 times 100 — "
                        "800, the 8 with two zeros behind it.",
                        '[[placevalue n="800" caption="8 × 10² = 800"]][[step eq="8 × 10² = 800"]]'),
             "ask": {'a': 3, 'b': 5, 'op': 'sci'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 6 times 10 to the "
                       "power 2 is 600. Tap the reason why."),
            "choices": ("because 10 to the 2 is 100: the 6 moves two places | "
                        "because 6 times 10 is 60, and times 2 is 120 | because the "
                        "power 2 puts a 2 after the 6"),
            "answer": "because 10 to the 2 is 100: the 6 moves two places",
            "board": '[[placevalue n="600" caption="6 × 10² = 600"]]',
        },
        "recap": [
            ("So, here it is again. 10 to a power is a 1 with that many zeros, and a "
             "digit times it moves that many places up the chart. The power counts "
             "the zeros — it is never a number to times by.",
             '[[placevalue n="600" caption="6 × 10² = 600"]]'),
            ("And that is how a scientist writes a huge number in a small space.",
             '[[step eq="6 × 10² = 600"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Doubling doubles everything there is, not just the start.",
        "why": [
            ("Why a pond? Because a pond has 3 lily pads, and lily pads double: every "
             "day, each pad becomes two. Watch a few days go by — 3, then 6, then 12, "
             "then 24. Look how fast that pulled away. This kind of growing has a "
             "name: exponential.",
             '[[goal text="The doubling pond"]]'),
        ],
        "picture": [
            ("Here are the days as bars. Day zero: 3 pads. Day one: 6. Day two: 12. "
             "Day three: 24. Each bar is twice the one before it, because each day "
             "doubles EVERYTHING there is — and look how the bars pull away from a "
             "straight line.",
             '[[bars data="day 0:3 | day 1:6 | day 2:12 | day 3:24" caption="3 pads doubling — 3, 6, 12, 24"]]'),
        ],
        "teach": [
            ("That is the method. After 3 days the pond has been doubled 3 times: 3 "
             "times 2 times 2 times 2, which equals 24. The days count the doublings "
             "— the days are a power of 2.",
             '[[bars data="day 0:3 | day 1:6 | day 2:12 | day 3:24" caption="3 × 2³ = 24"]][[step eq="3 × 2 × 2 × 2 = 24"]][[step eq="3 × 2³ = 24"]]'),
            ("A careful person who has not seen doubling before guesses like a "
             "walker: up by the same amount each day, 3, 5, 7, 9. But the pond is not "
             "walking — it is doubling, and by day 3 it holds 24, not 9. Growth that "
             "FEEDS ON ITSELF leaves walking behind.",
             '[[step eq="doubling: 3 → 24 ✓"]][[step eq="up by 2 a day: 3 → 9 ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 4 pads, doubling for 2 days: 4, "
                        "8, 16. That is 4 times 2 to the power 2 — 16 pads.",
                        '[[bars data="day 0:4 | day 1:8 | day 2:16" caption="4 × 2² = 16"]][[step eq="4 → 8 → 16"]]'),
             "ask": {'a': 3, 'b': 6, 'op': 'dbl'}},
            {"worked": ("One more together. 2 pads, doubling for 6 days: 2, 4, 8, 16, "
                        "32, 64, 128. That is 2 times 2 to the power 6 — 128 pads.",
                        '[[bars data="day 0:2 | day 1:4 | day 2:8 | day 3:16 | day 4:32 | day 5:64 | day 6:128" caption="2 × 2⁶ = 128"]][[step eq="2 → 4 → 8 → 16 → 32 → 64 → 128"]]'),
             "ask": {'a': 4, 'b': 6, 'op': 'dbl'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 3 lily pads double "
                       "every day, and after 3 days there are 24. Tap the reason why."),
            "choices": ("because each day doubles everything: 3 times 2, three times | "
                        "because 3 days of doubling adds 2 a day, 3 to 9 | because "
                        "doubling means 3 times 2, then times 3 days"),
            "answer": "because each day doubles everything: 3 times 2, three times",
            "board": '[[bars data="day 0:3 | day 1:6 | day 2:12 | day 3:24" caption="3 × 2³ = 24"]]',
        },
        "recap": [
            ("So, here it is again. Doubling doubles everything there is, so the days "
             "are a power of 2: the start, times 2 for every day. It is not walking "
             "up by the same amount — it feeds on itself and pulls away.",
             '[[bars data="day 0:3 | day 1:6 | day 2:12 | day 3:24" caption="3 × 2³ = 24"]]'),
            ("And that is exponential growth, in a pond.",
             '[[step eq="3 × 2³ = 24"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "op": "dbl"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! The middle rooms add; the corner room times.",
        "why": [
            ("Why four rooms? Because the rectangle picture grows up today. x plus 2, "
             "times x plus 3 — BOTH sides have an x in them now, so the wall cuts "
             "each way. Every pair of brackets you will ever multiply is this "
             "rectangle, and it always has four rooms.",
             '[[goal text="The four rooms"]]'),
        ],
        "picture": [
            ("Here is the rectangle: x plus 2 tall, x plus 3 wide. Four rooms. The "
             "big one is x times x — x squared. The two middle rooms are 3 x and 2 "
             "x. The corner is 2 times 3, which is 6. Read them, all four rooms: x "
             "squared plus 5 x plus 6.",
             '[[areamodel rows="x,2" cols="x,3" caption="(x + 2) by (x + 3) — four rooms: x², 3x, 2x, 6"]]'),
        ],
        "teach": [
            ("That is the method. Read the rooms. x times x is x squared. The two "
             "middle rooms are 3 x and 2 x — together 5 x. The corner is 2 times 3, "
             "which equals 6. So x plus 2, times x plus 3, comes to x squared plus 5 "
             "x plus 6.",
             '[[areamodel rows="x,2" cols="x,3" caption="read the rooms"]][[step eq="(x + 2)(x + 3) = x² + 5x + 6"]]'),
            ("Two different jobs in one picture: the MIDDLE rooms add the two numbers "
             "— 2 plus 3 equals 5 — and the CORNER room times them — 2 times 3 equals "
             "6. Mixing those two jobs up is the whole danger of this unit, so say "
             "them apart: middles add, corner times.",
             '[[step eq="middles: 2 + 3 = 5"]][[step eq="middle term: 5x"]][[step eq="corner: 2 × 3 = 6"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x plus 4, times x plus 2. "
                        "Middles: 4 plus 2 equals 6, so 6 x. Corner: 4 times 2 equals "
                        "8. x squared plus 6 x plus 8.",
                        '[[areamodel rows="x,4" cols="x,2" caption="(x + 4)(x + 2) = x² + 6x + 8"]][[step eq="(x + 4)(x + 2) = x² + 6x + 8"]]'),
             "ask": {'a': 4, 'b': 6, 'op': 'foil'}},
            {"worked": ("One more together. x plus 5, times x plus 3: middles make 8 x, "
                        "corner is 15. x squared plus 8 x plus 15.",
                        '[[areamodel rows="x,5" cols="x,3" caption="(x + 5)(x + 3) = x² + 8x + 15"]][[step eq="(x + 5)(x + 3) = x² + 8x + 15"]]'),
             "ask": {'a': 5, 'b': 6, 'op': 'foil'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x plus 2, times x "
                       "plus 3, has 5 x in the middle. Tap the reason why."),
            "choices": ("because the two middle rooms are 3x and 2x, and they add | "
                        "because 2 times 3 is 6, and the middle is 6x | because the "
                        "middle is the bigger of the two numbers"),
            "answer": "because the two middle rooms are 3x and 2x, and they add",
            "board": '[[areamodel rows="x,2" cols="x,3" caption="(x + 2)(x + 3) = x² + 5x + 6"]]',
        },
        "recap": [
            ("So, here it is again. Two brackets make a rectangle with four rooms: x "
             "squared, two middle rooms that ADD to the x count, and a corner that "
             "TIMES the two numbers. Middles add, corner times.",
             '[[areamodel rows="x,2" cols="x,3" caption="(x + 2)(x + 3) = x² + 5x + 6"]]'),
            ("And that is every pair of brackets you will ever multiply, in one "
             "picture.",
             '[[step eq="(x + 2)(x + 3) = x² + 5x + 6"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! The right number fits BOTH clues at once.",
        "why": [
            ("Why run it backwards? Because sometimes you are handed the finished sum "
             "— x squared plus 6 x plus 8 — and asked what two sides built it. "
             "Working back from the rooms to the sides is called factoring, and it "
             "is a detective game with two clues.",
             '[[goal text="Running the rooms backwards"]]'),
        ],
        "picture": [
            ("Here is the rectangle with one side hidden. You know the rooms add up "
             "to x squared plus 6 x plus 8, and you know one side is x plus 2. The "
             "hidden number has to add with 2 to make the 6 x, AND times with 2 to "
             "make the corner, 8. Only 4 does both — so the other side is x plus 4.",
             '[[areamodel rows="x,2" cols="x,4" ask="side" caption="x² + 6x + 8 — one side is x + 2: what is the other?"]][[areamodel rows="x,2" cols="x,4" caption="(x + 2)(x + 4) — the rooms come back"]]'),
        ],
        "teach": [
            ("That is the method. The clues: the two hidden numbers ADD to the x "
             "count, 6, and TIMES to the corner, 8. With 2 as one of them, try "
             "partners: 3? Adds to 5 — no. 4? 2 plus 4 is 6 AND 2 times 4 is 8. Both "
             "clues fit, so the sides are x plus 2 and x plus 4.",
             '[[areamodel rows="x,2" cols="x,4" ask="side" caption="the hidden side"]][[step eq="2 + ? = 6 · 2 × ? = 8"]][[step eq="2 + 4 = 6 ✓ · 2 × 4 = 8 ✓"]]'),
            ("Both clues, always. A number that only adds right, or only timeses "
             "right, is an impostor. And you can check the whole answer for free — "
             "multiply the sides back out and watch the original come back.",
             '[[step eq="(x + 2)(x + 4) = x² + 6x + 8 ✓"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x squared plus 7 x plus 10, "
                        "equals x plus 5, times x plus what? The partner must add with "
                        "5 to 7 and times with 5 to 10 — that is 2, both ways.",
                        '[[areamodel rows="x,5" cols="x,2" caption="(x + 5)(x + 2) = x² + 7x + 10"]][[step eq="5 + 2 = 7 ✓ · 5 × 2 = 10 ✓"]]'),
             "ask": {'a': 6, 'b': 2, 'op': 'fnum'}},
            {"worked": ("One more together. x squared plus 9 x plus 20, equals x plus "
                        "5, times x plus what? 5 plus 4 equals 9, and 5 times 4 equals "
                        "20. It is 4.",
                        '[[areamodel rows="x,5" cols="x,4" caption="(x + 5)(x + 4) = x² + 9x + 20"]][[step eq="(x + 5)(x + 4) = x² + 9x + 20"]]'),
             "ask": {'a': 4, 'b': 6, 'op': 'fnum'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x squared plus 6 "
                       "x plus 8 is x plus 2, times x plus 4. Tap the reason why."),
            "choices": ("because 4 adds with 2 to 6 and times to 8 | because 8 "
                        "take away 2 is 6, so the partner is 6 | because the partner "
                        "is the x count, 6, every time"),
            "answer": "because 4 adds with 2 to 6 and times to 8",
            "board": '[[areamodel rows="x,2" cols="x,4" caption="(x + 2)(x + 4) = x² + 6x + 8"]]',
        },
        "recap": [
            ("So, here it is again. Factoring runs the rooms backwards: the hidden "
             "number must add to the x count AND times to the corner. Test partners "
             "against both clues, then multiply back out to check.",
             '[[areamodel rows="x,2" cols="x,4" caption="(x + 2)(x + 4) = x² + 6x + 8"]]'),
            ("And that is a detective game with two clues, solved.",
             '[[step eq="x² + 6x + 8 = (x + 2)(x + 4)"]]'),
        ],
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
            {"a": 6, "b": 6, "op": "fnum"},
        ],
    },
    {
        "id": "alg1-u7-the-common-factor",
        "course": "algebra1", "unit": 7,
        "topic": "Pulling out the common factor",
        "op": "gcfx", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("common factor", "x"),
        "advance_line": "Three in a row, and you can say why — you've got it! Both parts share, or it is not a common factor.",
        "why": [
            ("Why a common factor? Because sometimes the whole expression shares one "
             "number. Look at 6 x plus 9: the 6 is 3 times 2, and the 9 is 3 times 3. "
             "The 3 lives in BOTH parts — it is a common factor, and you can pull it "
             "out front.",
             '[[goal text="Pulling out the common factor"]]'),
        ],
        "picture": [
            ("Here is 6 x plus 9 as a rectangle 3 tall. Its two rooms are 6 x and 9. "
             "A rectangle 3 tall with a 6 x room is 2 x wide there, and with a 9 room "
             "is 3 wide there. So the whole width is 2 x plus 3, and the rectangle "
             "is 3 times, 2 x plus 3.",
             '[[areamodel rows="3" cols="2x,3" caption="3 tall: rooms 6x and 9 — width 2x + 3"]]'),
        ],
        "teach": [
            ("That is the method. Pull the 3 out: 6 x plus 9 equals 3 times, 2 x plus "
             "3. Check it with the distributive lesson\'s own rule — the 3 reaches "
             "both rooms: 3 times 2 x is 6 x, and 3 times 3 is 9. It all comes back.",
             '[[areamodel rows="3" cols="2x,3" caption="6x + 9 = 3(2x + 3)"]][[step eq="6x + 9 = 3(2x + 3)"]][[step eq="check: 3 × 2x = 6x ✓ · 3 × 3 = 9 ✓"]]'),
            ("The mistake is pulling the factor from ONE part only: 3 times, 2 x plus "
             "9 — multiply that back and you get 6 x plus 27, not 6 x plus 9. A common "
             "factor comes out of everything it was in, or it does not come out at "
             "all.",
             '[[step eq="3(2x + 3) ✓"]][[step eq="3(2x + 9) ✗ — that is 6x + 27"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 10 x plus 4 equals 2 times, 5 x "
                        "plus 2. Both the 10 and the 4 gave up their 2.",
                        '[[areamodel rows="2" cols="5x,2" caption="10x + 4 = 2(5x + 2)"]][[step eq="10x + 4 = 2(5x + 2)"]]'),
             "ask": {'a': 3, 'b': 5, 'c': 2, 'op': 'gcfx'}},
            {"worked": ("One more together. 15 x plus 10 equals 5 times, 3 x plus 2.",
                        '[[areamodel rows="5" cols="3x,2" caption="15x + 10 = 5(3x + 2)"]][[step eq="15x + 10 = 5(3x + 2)"]]'),
             "ask": {'a': 7, 'b': 2, 'c': 3, 'op': 'gcfx'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. 6 x plus 9 is 3 "
                       "times, 2 x plus 3. Tap the reason why."),
            "choices": ("because the 3 comes out of both the 6x and the 9 | "
                        "because the 3 comes out of the 6x only | "
                        "because 6 plus 9 is 15, and 15 is 3 times 5"),
            "answer": "because the 3 comes out of both the 6x and the 9",
            "board": '[[areamodel rows="3" cols="2x,3" caption="6x + 9 = 3(2x + 3)"]]',
        },
        "recap": [
            ("So, here it is again. A common factor lives in every part. Pull it "
             "out front and divide EVERY part by it — then check by timesing it "
             "back in: the factor reaches both rooms.",
             '[[areamodel rows="3" cols="2x,3" caption="6x + 9 = 3(2x + 3)"]]'),
            ("And that is the distributive lesson, run in reverse.",
             '[[step eq="6x + 9 = 3(2x + 3)"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! Plus and take away the same x's — the middles cancel.",
        "why": [
            ("Why one special pair? Because one pair of sides does something "
             "wonderful. x plus 3, times x TAKE AWAY 3. Build the rooms and watch the "
             "middle of the answer vanish — a pattern famous enough to have a name.",
             '[[goal text="The vanishing middle"]]'),
        ],
        "picture": [
            ("Here is the rectangle: x plus 3 tall, x take away 3 wide. The rooms: x "
             "squared; a middle room of take away 3 x; a middle room of plus 3 x; and "
             "a corner of 3 times 3, taken away — 9. The two middles are the same "
             "size with opposite signs, so they cancel, and the sum is x squared take "
             "away 9.",
             '[[areamodel rows="x,3" cols="x,-3" caption="(x + 3) by (x − 3) — the middles cancel: x² − 9"]]'),
        ],
        "teach": [
            ("That is the method. Watch the middles: plus 3 x and take away 3 x. They "
             "cancel — land exactly on nothing. All that survives is x squared take "
             "away 9. The whole middle of the answer vanished.",
             '[[areamodel rows="x,3" cols="x,-3" caption="read the rooms"]][[step eq="+3x − 3x = 0"]][[step eq="(x + 3)(x − 3) = x² − 9"]]'),
            ("And notice WHICH 9: it is 3 squared, not 3 and not 6. The corner room is "
             "3 times 3. This pattern — x squared take away a square — is called the "
             "difference of squares, and it works for any number in the 3\'s place.",
             '[[step eq="x² − 9 ✓ (9 = 3²)"]][[step eq="x² − 3 ✗ · x² − 6 ✗ — the corner is 3 × 3"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x plus 5, times x take away 5. "
                        "The middles cancel, the corner is 5 squared: x squared take "
                        "away 25.",
                        '[[areamodel rows="x,5" cols="x,-5" caption="(x + 5)(x − 5) = x² − 25"]][[step eq="(x + 5)(x − 5) = x² − 25"]]'),
             "ask": {'a': 13, 'b': 0, 'op': 'dsq'}},
            {"worked": ("One more together. x plus 10, times x take away 10: x squared "
                        "take away 100.",
                        '[[areamodel rows="x,10" cols="x,-10" caption="(x + 10)(x − 10) = x² − 100"]][[step eq="(x + 10)(x − 10) = x² − 100"]]'),
             "ask": {'a': 14, 'b': 0, 'op': 'dsq'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x plus 3, times x "
                       "take away 3, is x squared take away 9. Tap the reason why."),
            "choices": ("because the middles cancel, and the corner is 3 times 3 | "
                        "because the middles add to 6x, and the corner is 3 | because "
                        "take away 3 means x squared take away 3"),
            "answer": "because the middles cancel, and the corner is 3 times 3",
            "board": '[[areamodel rows="x,3" cols="x,-3" caption="(x + 3)(x − 3) = x² − 9"]]',
        },
        "recap": [
            ("So, here it is again. Plus a number on one side and take away the same "
             "number on the other: the middle rooms cancel, and only x squared and "
             "the corner survive — the number squared, taken away.",
             '[[areamodel rows="x,3" cols="x,-3" caption="(x + 3)(x − 3) = x² − 9"]]'),
            ("And that is the difference of squares, the one pair that vanishes in "
             "the middle.",
             '[[step eq="(x + 3)(x − 3) = x² − 9"]]'),
        ],
        "bank": [
                        {"a": 4, "b": 0, "op": "dsq"},
                        {"a": 6, "b": 0, "op": "dsq"},
            {"a": 7, "b": 0, "op": "dsq"},
            {"a": 8, "b": 0, "op": "dsq"},
            {"a": 9, "b": 0, "op": "dsq"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! Squared means times itself, never times two.",
        "why": [
            ("Why a curve? Because every line you have drawn was straight. Meet the "
             "first rule that bends: y equals x squared. Feed it 1, 2, 3, 4 and out "
             "come 1, 4, 9, 16 — each step up costs more than the last, so the graph "
             "bends into a curve, shaped like a bowl.",
             '[[goal text="The curve"]]'),
        ],
        "picture": [
            ("Here is y equals x squared plus 2 on the grid — a bowl, not a line. "
             "Climb from x equals 3 up to the curve: 3 squared is 3 times 3, which is "
             "9, and plus 2 brings it to 11. The point 3 comma 11 sits on the curve, high "
             "up its right side.",
             '[[graph func="x^2+2" points="(3,11)" range="-4..4" caption="y = x² + 2 — the point (3, 11)"]]'),
        ],
        "teach": [
            ("That is the method. Read it like any rule. y equals x squared plus 2, "
             "at x equals 3: 3 squared is 3 times 3, which equals 9, plus 2 equals "
             "11.",
             '[[graph func="x^2+2" points="(3,11)" range="-4..4" caption="the point (3, 11)"]][[step eq="y = 3² + 2 = 9 + 2 = 11"]]'),
            ("The one error to burn away now: squared means TIMES ITSELF, not times "
             "two. 3 squared is 9, not 6. At x equals 2 the two happen to agree — 2 "
             "times 2 and 2 plus 2 are both 4 — and that coincidence at 2 is exactly "
             "what plants the habit. Everywhere else it breaks.",
             '[[step eq="3² = 3 × 3 = 9 ✓"]][[step eq="3² = 6 ✗ — that is doubling"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals x squared plus 3, at x "
                        "equals 4: 16 plus 3 equals 19.",
                        '[[graph func="x^2+3" points="(4,19)" range="-5..5" caption="y = x² + 3 — the point (4, 19)"]][[step eq="y = 4² + 3 = 19"]]'),
             "ask": {'a': 3, 'b': 7, 'op': 'sqy'}},
            {"worked": ("One more together. y equals x squared plus 1, at x equals 5: 25 "
                        "plus 1 equals 26.",
                        '[[graph func="x^2+1" points="(5,26)" range="-6..6" caption="y = x² + 1 — the point (5, 26)"]][[step eq="y = 5² + 1 = 26"]]'),
             "ask": {'a': 6, 'b': 7, 'op': 'sqy'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. On the curve y "
                       "equals x squared plus 2, when x is 3, y is 11. Tap the reason "
                       "why."),
            "choices": ("because 3 squared is 3 times 3, and then 2 more | because 3 "
                        "squared is 3 times 2, and then 2 more | because the curve "
                        "climbs 2 for every step, like a line"),
            "answer": "because 3 squared is 3 times 3, and then 2 more",
            "board": '[[graph func="x^2+2" points="(3,11)" range="-4..4" caption="the point (3, 11)"]]',
        },
        "recap": [
            ("So, here it is again. A rule with x squared in it bends into a bowl. "
             "Read it like any rule — swap in the x, square it by timesing it by "
             "itself, then add the rest. Squared is never times two.",
             '[[graph func="x^2+2" points="(3,11)" range="-4..4" caption="3² + 2 = 11"]]'),
            ("And that is the first rule that bends, read straight.",
             '[[step eq="y = 3² + 2 = 11"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! A product is zero only when a factor is zero.",
        "why": [
            ("Why two answers? Because here is a fact so plain it hides its power: "
             "zero times ANYTHING is zero — and NOTHING ELSE, times anything, ever "
             "lands on zero. So if two brackets multiply to zero, one of the brackets "
             "MUST be zero. There is no other way.",
             '[[goal text="Zero times anything"]]'),
        ],
        "picture": [
            ("Here is the curve for x take away 3, times x take away 5. A bowl — and "
             "look where it touches the ground, where y is zero: at x equals 3, and "
             "again at x equals 5. Two touches, because each bracket has its own x "
             "that turns it to zero.",
             '[[graph func="(x-3)*(x-5)" points="(3,0),(5,0)" range="0..7" caption="(x − 3)(x − 5) — the ground at x = 3 and x = 5"]]'),
        ],
        "teach": [
            ("That is the method. x take away 3, times x take away 5, equals zero. "
             "When is the first bracket zero? At x equals 3. The second? At x equals "
             "5. So the equation has TWO answers, 3 and 5 — a bending curve can touch "
             "the ground twice.",
             '[[graph func="(x-3)*(x-5)" points="(3,0),(5,0)" range="0..7" caption="the ground at 3 and 5"]][[step eq="(x − 3)(x − 5) = 0"]][[step eq="x = 3 or x = 5"]]'),
            ("Do not do arithmetic on the two numbers — they are not asking to be "
             "added or timesed. Each one answers its own bracket. Check: at x equals "
             "5, the second bracket is zero, and zero times anything wipes out the "
             "whole thing.",
             '[[step eq="x = 3, x = 5 ✓"]][[step eq="x = 8 ✗ · x = 15 ✗ — nobody asked for 3 + 5 or 3 × 5"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. x take away 2, times x take "
                        "away 6, equals zero. The answers are 2 and 6 — one per bracket.",
                        '[[graph func="(x-2)*(x-6)" points="(2,0),(6,0)" range="0..8" caption="the ground at 2 and 6"]][[step eq="(x − 2)(x − 6) = 0"]][[step eq="x = 2 or 6"]]'),
             "ask": {'a': 6, 'b': 4, 'op': 'roots'}},
            {"worked": ("One more together. x take away 4, times x take away 7: the "
                        "answers are 4 and 7.",
                        '[[graph func="(x-4)*(x-7)" points="(4,0),(7,0)" range="0..9" caption="the ground at 4 and 7"]][[step eq="x = 4 or x = 7"]]'),
             "ask": {'a': 7, 'b': 5, 'op': 'roots'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. x take away 3, "
                       "times x take away 5, equals zero, and the answers are 3 and 5. "
                       "Tap the reason why."),
            "choices": ("because a product is zero only when one bracket is zero | "
                        "because 3 and 5 add to 8, and 8 is the answer | because the "
                        "curve is a bowl, and bowls have one bottom"),
            "answer": "because a product is zero only when one bracket is zero",
            "board": '[[graph func="(x-3)*(x-5)" points="(3,0),(5,0)" range="0..7" caption="the ground at x = 3 and x = 5"]]',
        },
        "recap": [
            ("So, here it is again. Two brackets multiply to zero only when one of "
             "them is zero. Each bracket names its own x, so a curve touches the "
             "ground twice — two answers, and no arithmetic between them.",
             '[[graph func="(x-3)*(x-5)" points="(3,0),(5,0)" range="0..7" caption="x = 3 or x = 5"]]'),
            ("And that is zero times anything, doing all the work.",
             '[[step eq="(x − 3)(x − 5) = 0, so x = 3 or x = 5"]]'),
        ],
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
        "advance_line": "Three in a row, and you can say why — you've got it! A square is never below zero, so the plus number is the floor.",
        "why": [
            ("Why a lowest point? Because a square can never be below zero. Times "
             "any number by itself — even a negative one — and the answer refuses to "
             "be negative. That single refusal gives every bending curve of this "
             "shape a FLOOR: a lowest point it touches and never goes under.",
             '[[goal text="The lowest point"]]'),
        ],
        "picture": [
            ("Here is y equals: x take away 3, squared, plus 2. A bowl with its "
             "bottom marked — the point 3 comma 2. The squared part is zero right at "
             "x equals 3, and there y is 0 plus 2. Everywhere else the square is "
             "bigger than zero, so the curve is higher.",
             '[[graph func="(x-3)^2+2" points="(3,2)" range="0..6" caption="y = (x − 3)² + 2 — the lowest point (3, 2)"]]'),
        ],
        "teach": [
            ("That is the method. The squared part is smallest when it is exactly "
             "zero — which happens right at x equals 3. At that moment y is 0 plus 2, "
             "which equals 2. The lowest y this curve ever reaches is 2.",
             '[[graph func="(x-3)^2+2" points="(3,2)" range="0..6" caption="the lowest point (3, 2)"]][[step eq="(x − 3)² is 0 at x = 3"]][[step eq="lowest y = 0 + 2 = 2"]]'),
            ("The rule\'s two numbers do two jobs — the start-and-climb lesson again, "
             "curved. The 3 says WHERE the low point sits, left and right. The 2 says "
             "HOW LOW the curve goes. Asked for the lowest y, the answer is the plus "
             "number, not the number inside the brackets.",
             '[[step eq="lowest y = 2 ✓"]][[step eq="3 ✗ — that is where it sits, not how low"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals: x take away 5, "
                        "squared, plus 4. The square bottoms out at zero, so the lowest "
                        "y is 4.",
                        '[[graph func="(x-5)^2+4" points="(5,4)" range="2..8" caption="the lowest point (5, 4) — lowest y = 4"]][[step eq="lowest y = 4"]]'),
             "ask": {'a': 4, 'b': 3, 'op': 'vtx'}},
            {"worked": ("One more together. y equals: x take away 2, squared, plus 6. "
                        "Lowest y: 6.",
                        '[[graph func="(x-2)^2+6" points="(2,6)" range="-1..5" caption="the lowest point (2, 6) — lowest y = 6"]][[step eq="lowest y = 6"]]'),
             "ask": {'a': 7, 'b': 8, 'op': 'vtx'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. y equals x take "
                       "away 3, squared, plus 2, and its lowest y is 2. Tap the reason "
                       "why."),
            "choices": ("because the square bottoms out at 0, leaving the plus 2 | "
                        "because the 3 inside the brackets is the lowest y | because "
                        "3 plus 2 is 5, and 5 is the floor"),
            "answer": "because the square bottoms out at 0, leaving the plus 2",
            "board": '[[graph func="(x-3)^2+2" points="(3,2)" range="0..6" caption="the lowest point (3, 2)"]]',
        },
        "recap": [
            ("So, here it is again. A square is never below zero, so the squared "
             "part bottoms out at 0 and the plus number is the floor. The number "
             "inside the brackets says where the floor sits; the plus number says "
             "how low.",
             '[[graph func="(x-3)^2+2" points="(3,2)" range="0..6" caption="lowest y = 0 + 2 = 2"]]'),
            ("And that is a floor no bowl ever goes under.",
             '[[step eq="lowest y = 0 + 2 = 2"]]'),
        ],
        "bank": [
            {"a": 4, "b": 2, "op": "vtx"},
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
        "advance_line": "Three in a row, and you can say why — you've got it! Ask what number squared equals the height.",
        "why": [
            ("Why a ball? Because throw one and its height follows a bending curve — "
             "quadratics are how the world falls. Here is one: y equals 25 take away "
             "x squared. At x equals 0 the height is 25, and as x grows, x squared "
             "eats the height away.",
             '[[goal text="The ball comes down"]]'),
        ],
        "picture": [
            ("Here is the curve, starting at height 25 and bending down to the "
             "ground. It reaches the ground — height zero — at x equals 5, because "
             "25 take away 5 squared is 25 take away 25, which is zero. The point 5 "
             "comma 0 is where the ball lands.",
             '[[graph func="25-x^2" points="(0,25),(5,0)" range="0..6" caption="y = 25 − x² — from height 25 down to the ground at x = 5"]]'),
        ],
        "teach": [
            ("That is the method. The ground is where the height is zero, so 25 take "
             "away x squared equals 0 — x squared must equal 25. Now the question "
             "turns around — WHAT NUMBER, squared, equals 25? Five: 5 times 5 is 25. "
             "The ball lands at x equals 5.",
             '[[graph func="25-x^2" points="(5,0)" range="0..6" caption="the ground at x = 5"]][[step eq="25 − x² = 0"]][[step eq="x² = 25"]][[step eq="x = 5"]]'),
            ("That backwards question has a name: 5 is the square root of 25 — the "
             "number that squares to it. It is not half of 25. Halving undoes "
             "doubling; the square root undoes SQUARING, and you have known since the "
             "curve lesson that those are different beasts.",
             '[[step eq="x = 5 ✓ (5² = 25)"]][[step eq="x = 12 ✗ — half undoes DOUBLING, not squaring"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. y equals 36 take away x "
                        "squared. It lands where x squared equals 36 — and 6 squared is "
                        "36. x equals 6.",
                        '[[graph func="36-x^2" points="(6,0)" range="0..7" caption="the ground at x = 6"]][[step eq="x² = 36"]][[step eq="x = 6"]]'),
             "ask": {'a': 13, 'b': 0, 'op': 'hitg'}},
            {"worked": ("One more together. y equals 49 take away x squared. 7 squared "
                        "is 49, so it lands at x equals 7.",
                        '[[graph func="49-x^2" points="(7,0)" range="0..8" caption="the ground at x = 7"]][[step eq="x² = 49"]][[step eq="x = 7"]]'),
             "ask": {'a': 14, 'b': 0, 'op': 'hitg'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. The height is 25 "
                       "take away x squared, and the ball lands at x equals 5. Tap the "
                       "reason why."),
            "choices": ("because 5 squared is 25, so the height reaches zero there | "
                        "because half of 25 is about 12, and halving undoes squaring | "
                        "because the ball lands at the height it started from"),
            "answer": "because 5 squared is 25, so the height reaches zero there",
            "board": '[[graph func="25-x^2" points="(5,0)" range="0..6" caption="x² = 25, so x = 5"]]',
        },
        "recap": [
            ("So, here it is again. The ground is where the height is zero, so set "
             "the rule to zero and ask what number squared equals the height. That "
             "number is the square root — and it undoes squaring, not doubling.",
             '[[graph func="25-x^2" points="(5,0)" range="0..6" caption="25 − x² = 0 at x = 5"]]'),
            ("And that is how the world falls, read off a curve.",
             '[[step eq="x² = 25, so x = 5"]]'),
        ],
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


# =============================================================================
# ALGEBRA I -- UNIT 9: DATA & STATISTICS (build lc, 2026-08-22)
# =============================================================================
# THE LAST UNIT OF ALGEBRA I, and the last renderers on July's shelf: [[dotplot]],
# [[bars]] and [[boxplot]] have been in math-figures.js since July and none had ever
# been drawn by a scripted lesson. Every lesson here puts the DATA on the board and
# asks a question the picture can answer -- which is the whole argument for teaching
# statistics with a plot instead of a formula.
#
# THE UNIT BUILDS TO ONE IDEA: the mean and the median are not interchangeable. Three
# lessons lay the tools, and the fourth walks one unusual number into the room and
# shows the mean move while the median stands still. That is the lesson a child
# actually needs -- every misleading statistic they will ever meet lives there.
_ALGEBRA1_U9 = [
    {
        "id": "alg1-u9-the-mean",
        "course": "algebra1", "unit": 9,
        "topic": "The mean",
        "op": "mean", "max_value": 200,
        "levels": ("abstract",),
        "symbols": ("mean", "share"),
        "advance_line": "Three in a row, and you can say why — you've got it! The mean shares everything out equally.",
        "why": [
            ("Why the mean? Because it is what everybody would have if you piled all "
             "of it together and shared it out equally. Five children with 3, 5, 5, "
             "6 and 6 sweets have 25 sweets between them — and the mean asks what "
             "each would hold if that pile were dealt out fairly.",
             '[[goal text="The mean"]]'),
        ],
        "picture": [
            ("Here are the five amounts as dots — 3, 5, 5, 6 and 6 — and here is "
             "the whole pile of 25 as a bar, shared into five equal parts. Every "
             "part is 5. That is the mean: 25 shared between 5 is 5 each.",
             '[[dotplot values="3,5,5,6,6" caption="one dot per value — 25 in all"]][[tape parts="5 | 5 | 5 | 5 | 5" total="25" caption="25 shared between 5 — the mean is 5"]]'),
        ],
        "teach": [
            ("That is the method — two steps, and one of them you already know. Add "
             "everything up to find how much there is in all, then share that "
             "between HOW MANY there are. 25 shared between 5 equals 5. The mean is "
             "5.",
             '[[tape parts="5 | 5 | 5 | 5 | 5" total="25" caption="25 ÷ 5 = 5 each"]][[step eq="3 + 5 + 5 + 6 + 6 = 25"]][[step eq="25 ÷ 5 = 5"]]'),
            ("Divide by the COUNT, not by anything else. Five numbers means divide by "
             "five — however big or small those numbers happen to be. And the mean is "
             "not the whole pile: 25 is what they have together, 5 is what they have "
             "each.",
             '[[step eq="mean = 5 ✓"]][[step eq="25 ✗ — that is the whole pile, not the mean"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Three numbers add up to 18. "
                        "Share 18 between 3: the mean is 6.",
                        '[[tape parts="6 | 6 | 6" total="18" caption="18 ÷ 3 = 6 each"]][[step eq="18 ÷ 3 = 6"]]'),
             "ask": {'a': 4, 'b': 7, 'op': 'mean'}},
            {"worked": ("One more together. Five numbers add up to 35. 35 shared between "
                        "5 equals 7.",
                        '[[tape parts="7 | 7 | 7 | 7 | 7" total="35" caption="35 ÷ 5 = 7 each"]][[step eq="35 ÷ 5 = 7"]]'),
             "ask": {'a': 6, 'b': 9, 'op': 'mean'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Five numbers add "
                       "up to 25, and their mean is 5. Tap the reason why."),
            "choices": ("because 25 shared equally between the 5 of them is 5 each | "
                        "because 25 is what they have, so the mean is 25 | because the "
                        "mean is the biggest number in the set"),
            "answer": "because 25 shared equally between the 5 of them is 5 each",
            "board": '[[tape parts="5 | 5 | 5 | 5 | 5" total="25" caption="25 ÷ 5 = 5 — the mean is 5"]]',
        },
        "recap": [
            ("So, here it is again. The mean is the pile shared out equally: add "
             "everything to find how much in all, then divide by how many there "
             "are — the count, never anything else.",
             '[[tape parts="5 | 5 | 5 | 5 | 5" total="25" caption="25 ÷ 5 = 5"]]'),
            ("And that is one number standing for the whole set, fairly.",
             '[[step eq="mean = 25 ÷ 5 = 5"]]'),
        ],
        "bank": [
            {"a": 3, "b": 2, "op": "mean"},
            {"a": 4, "b": 3, "op": "mean"},
            {"a": 5, "b": 4, "op": "mean"},
            {"a": 4, "b": 5, "op": "mean"},
            {"a": 6, "b": 5, "op": "mean"},
            {"a": 4, "b": 6, "op": "mean"},
            {"a": 5, "b": 8, "op": "mean"},
            {"a": 7, "b": 9, "op": "mean"},
            {"a": 6, "b": 12, "op": "mean"},
            {"a": 8, "b": 15, "op": "mean"},
        ],
    },
    {
        "id": "alg1-u9-the-median",
        "course": "algebra1", "unit": 9,
        "topic": "The median",
        "op": "medn", "max_value": 30,
        "levels": ("abstract",),
        "symbols": ("median", "middle"),
        "advance_line": "Three in a row, and you can say why — you've got it! Line them up and walk in from both ends.",
        "why": [
            ("Why a second middle? Because the median is a different kind of middle: "
             "not shared out, just stood in a line. Put the numbers in order, smallest "
             "first, and the median is the one standing in the middle of the queue.",
             '[[goal text="The median"]]'),
        ],
        "picture": [
            ("Here are five numbers as dots, in order: 4, 5, 6, 7, 8. Walk in from "
             "both ends at once — 4 and 8 go first, then 5 and 7 — and you meet at "
             "6. Two dots below it, two above it. The median is 6.",
             '[[dotplot values="4,5,6,7,8" caption="one dot per value — walk in from both ends and meet at 6"]]'),
        ],
        "teach": [
            ("That is the method. Five numbers: 4, 5, 6, 7, 8. Walk in from both "
             "ends at once — 4 and 8, then 5 and 7 — and you meet at 6. Two numbers "
             "below it, two above it. The median is 6.",
             '[[dotplot values="4,5,6,7,8" caption="2 below · 6 · 2 above"]][[step eq="2 below · 6 · 2 above"]]'),
            ("In order FIRST — that is the step people skip. And the median is the "
             "middle NUMBER, not the middle of the ends: a queue\'s middle person is "
             "found by counting in, not by looking at who is at the front and the "
             "back.",
             '[[step eq="median = 6 ✓"]][[step eq="4 ✗ · 8 ✗ — those are the ends"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. 7, 8, 9, 10, 11, 12, 13. Seven "
                        "numbers, so three each side — the median is 10.",
                        '[[dotplot values="7,8,9,10,11,12,13" caption="3 below · 10 · 3 above"]][[step eq="3 below · 10 · 3 above"]]'),
             "ask": {'a': 3, 'b': 9, 'op': 'medn'}},
            {"worked": ("One more together. 11, 12, 13, 14, 15. Walk in from both ends: "
                        "the median is 13.",
                        '[[dotplot values="11,12,13,14,15" caption="2 below · 13 · 2 above"]][[step eq="median = 13"]]'),
             "ask": {'a': 2, 'b': 12, 'op': 'medn'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Of 4, 5, 6, 7 and "
                       "8, the median is 6. Tap the reason why."),
            "choices": ("because 6 is the middle one, with two below and two above | "
                        "because 6 is halfway between the two ends, 4 and 8 | because "
                        "5 is written in the middle of the list"),
            "answer": "because 6 is the middle one, with two below and two above",
            "board": '[[dotplot values="4,5,6,7,8" caption="2 below · 6 · 2 above — the median is 6"]]',
        },
        "recap": [
            ("So, here it is again. Put the numbers in order, then walk in from "
             "both ends at once; where you meet is the median — the middle number, "
             "with as many below it as above it.",
             '[[dotplot values="4,5,6,7,8" caption="the median is 6"]]'),
            ("And that is the middle of the queue, found by counting in.",
             '[[step eq="median = 6"]]'),
        ],
        "bank": [
            {"a": 2, "b": 4, "op": "medn"},
            {"a": 2, "b": 5, "op": "medn"},
            {"a": 3, "b": 6, "op": "medn"},
            {"a": 2, "b": 7, "op": "medn"},
            {"a": 3, "b": 8, "op": "medn"},
            {"a": 4, "b": 9, "op": "medn"},
            {"a": 3, "b": 11, "op": "medn"},
            {"a": 4, "b": 12, "op": "medn"},
            {"a": 3, "b": 15, "op": "medn"},
            {"a": 4, "b": 18, "op": "medn"},
        ],
    },
    {
        "id": "alg1-u9-the-range",
        "course": "algebra1", "unit": 9,
        "topic": "The range",
        "op": "rnge", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("range", "spread"),
        "advance_line": "Three in a row, and you can say why — you've got it! The range is how far the data stretches.",
        "why": [
            ("Why the range? Because the mean and the median both tell you where the "
             "data SITS — and nothing about how far it stretches. Biggest take away "
             "smallest: one take away, and it describes the whole spread of the "
             "data.",
             '[[goal text="The range"]]'),
        ],
        "picture": [
            ("Here are the two ends as bars: smallest 4, biggest 19. And here they "
             "are on a number line, with the stretch between them — from 4 all the "
             "way to 19 is a stretch of 15. That stretch is the range.",
             '[[bars data="smallest:4 | biggest:19" caption="smallest 4, biggest 19"]][[numberline min="0" max="21" points="4,19" caption="from 4 to 19 — a stretch of 15"]]'),
        ],
        "teach": [
            ("That is the method. The range tells you something else entirely from "
             "the middles: how far the data stretches. Smallest 4, biggest 19. The "
             "range is 19 take away 4, which equals 15. The data covers a stretch of "
             "15.",
             '[[numberline min="0" max="21" points="4,19" caption="19 − 4 = 15"]][[step eq="19 − 4 = 15"]]'),
            ("Two sets can share a mean and be nothing alike. Children all aged 9, 9, "
             "9 have a range of 0 — identical. Children aged 4, 9, 14 have the same "
             "mean of 9 and a range of 10 — wildly spread. The middle alone never "
             "tells you that.",
             '[[step eq="9, 9, 9 → mean 9, range 0"]][[step eq="4, 9, 14 → mean 9, range 10"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Smallest 5, biggest 21. The "
                        "range is 21 take away 5, which equals 16.",
                        '[[numberline min="0" max="23" points="5,21" caption="from 5 to 21 — a stretch of 16"]][[step eq="21 − 5 = 16"]]'),
             "ask": {'a': 3, 'b': 15, 'op': 'rnge'}},
            {"worked": ("One more together. Smallest 7, biggest 25. The range is 25 take "
                        "away 7, which equals 18.",
                        '[[numberline min="0" max="27" points="7,25" caption="from 7 to 25 — a stretch of 18"]][[step eq="25 − 7 = 18"]]'),
             "ask": {'a': 9, 'b': 30, 'op': 'rnge'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Smallest 4, "
                       "biggest 19, and the range is 15. Tap the reason why."),
            "choices": ("because the range is the stretch from 4 up to 19 | because the "
                        "range adds the two ends, 4 and 19 | because the range is the "
                        "biggest number, 19"),
            "answer": "because the range is the stretch from 4 up to 19",
            "board": '[[numberline min="0" max="21" points="4,19" caption="19 − 4 = 15"]]',
        },
        "recap": [
            ("So, here it is again. The range is how far the data stretches: the "
             "biggest take away the smallest. It says nothing about where the data "
             "sits, and everything about how spread out it is.",
             '[[numberline min="0" max="21" points="4,19" caption="range = 19 − 4 = 15"]]'),
            ("And that is the spread, in one take away.",
             '[[step eq="range = 19 − 4 = 15"]]'),
        ],
        "bank": [
            {"a": 2, "b": 5, "op": "rnge"},
            {"a": 3, "b": 8, "op": "rnge"},
            {"a": 4, "b": 12, "op": "rnge"},
            {"a": 2, "b": 11, "op": "rnge"},
            {"a": 6, "b": 18, "op": "rnge"},
            {"a": 5, "b": 20, "op": "rnge"},
            {"a": 8, "b": 26, "op": "rnge"},
            {"a": 4, "b": 25, "op": "rnge"},
            {"a": 7, "b": 32, "op": "rnge"},
            {"a": 6, "b": 38, "op": "rnge"},
        ],
    },
    {
        "id": "alg1-u9-the-odd-one-out",
        "course": "algebra1", "unit": 9,
        "topic": "When one number is unusual",
        "op": "outl", "max_value": 60,
        "levels": ("abstract",),
        "symbols": ("median", "mean"),
        "advance_line": "Three in a row, and you can say why — you've got it! One unusual number drags the mean and leaves the median standing.",
        "why": [
            ("Why this last lesson? Because it gives the other three their point. "
             "Four children have 5 pencils each. A fifth walks in carrying 45. Watch "
             "what that ONE child does to each of our middles.",
             '[[goal text="When one number is unusual"]]'),
        ],
        "picture": [
            ("Here are the five as dots: four stacked at 5, and one far out on its "
             "own at 45. Walk in from both ends and the middle dot is still at 5 — "
             "the median. But pile everything up — 65 — and share it between 5, and "
             "the mean is 13. Nobody in the room has 13.",
             '[[dotplot values="5,5,5,5,45" caption="four at 5, one at 45 — median 5, mean 13"]]'),
        ],
        "teach": [
            ("That is the method. The mean: 5 and 5 and 5 and 5 and 45 add up to 65, "
             "shared between 5 gives 13. Thirteen! Not one child in that room has 13 "
             "pencils. The median, though — line them up, walk in from both ends, "
             "and the middle child still has 5.",
             '[[dotplot values="5,5,5,5,45" caption="the middle dot is still at 5"]][[step eq="mean = 65 ÷ 5 = 13"]][[step eq="median = 5"]]'),
            ("A single unusual number DRAGS the mean and leaves the median standing. "
             "That is why you should ask which middle someone is quoting you — "
             "averages that sound strange usually have one very odd number hiding "
             "behind them.",
             '[[step eq="median 5 — the room ✓"]][[step eq="mean 13 — nobody ✗"]]'),
        ],
        "pairs": [
            {"worked": ("Here is one more, done for you. Four children with 6 each, and "
                        "one with 36. The mean is 12, but the median is still 6.",
                        '[[dotplot values="6,6,6,6,36" caption="four at 6, one at 36 — median 6, mean 12"]][[step eq="median = 6 · mean = 12"]]'),
             "ask": {'a': 4, 'b': 4, 'c': 34, 'op': 'outl'}},
            {"worked": ("One more together. Four with 3 each and one with 28: the mean "
                        "climbs to 8, the median stays at 3.",
                        '[[dotplot values="3,3,3,3,28" caption="four at 3, one at 28 — median 3, mean 8"]][[step eq="median = 3 · mean = 8"]]'),
             "ask": {'a': 4, 'b': 5, 'c': 40, 'op': 'outl'}},
        ],
        "practice_intro": ("Now it's your turn. Three right answers in a row and we're "
                           "done — here comes the first one."),
        "show_work_on_correct": True,
        "explain": {
            "spoken": ("One more thing — not the answer, the reason. Four children have "
                       "5 pencils and one has 45, and the median is 5. Tap the reason "
                       "why."),
            "choices": ("because the middle child, counting in from both ends, has 5 | "
                        "because 65 shared between 5 is 13, so the median is 13 | "
                        "because the median is the unusual number, 45"),
            "answer": "because the middle child, counting in from both ends, has 5",
            "board": '[[dotplot values="5,5,5,5,45" caption="median 5 — the room · mean 13 — nobody"]]',
        },
        "recap": [
            ("So, here it is again. One unusual number drags the mean away from the "
             "room and leaves the median standing where the middle is. When an "
             "average sounds strange, ask which middle it is.",
             '[[dotplot values="5,5,5,5,45" caption="median 5 · mean 13"]]'),
            ("And that is the point of having three middles — and the end of "
             "Algebra 1.",
             '[[step eq="median = 5 · mean = 13"]]'),
        ],
        "bank": [
            {"a": 4, "b": 2, "c": 22, "op": "outl"},
            {"a": 4, "b": 2, "c": 32, "op": "outl"},
            {"a": 4, "b": 3, "c": 23, "op": "outl"},
            {"a": 4, "b": 3, "c": 33, "op": "outl"},
            {"a": 4, "b": 4, "c": 24, "op": "outl"},
            {"a": 4, "b": 5, "c": 25, "op": "outl"},
            {"a": 4, "b": 6, "c": 26, "op": "outl"},
            {"a": 4, "b": 7, "c": 27, "op": "outl"},
            {"a": 4, "b": 8, "c": 28, "op": "outl"},
            {"a": 4, "b": 9, "c": 29, "op": "outl"},
        ],
    },
]
LESSONS.extend(_ALGEBRA1_U9)

# ---- this course's slice of COURSE_ORDER: the teaching order (lessons/__init__.py joins the ten) ----
ORDER = [

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
    # Unit 9: Data & Statistics -- ALGEBRA I COMPLETE
    "alg1-u9-the-mean", "alg1-u9-the-median",
    "alg1-u9-the-range", "alg1-u9-the-odd-one-out",
]

# I did no harm and this file is not truncated.
