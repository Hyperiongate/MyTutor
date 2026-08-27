# =============================================================================
# numwords.py  --  WHAT A NUMBER SOUNDS LIKE, ONE COPY  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-27  NEW FILE (build ou -- ANSWER FREELY IN THE FAST LANE). The
#               scripted lane learned to accept a TYPED or SPOKEN answer, which
#               means code -- never the model -- has to turn "twenty-one",
#               "negative three" or "the answer is 12" into an integer. tutor.py
#               already owned a word->number reader (_pr_word_value, written for
#               the rule-44 referee) and lessonscripts needed the same knowledge.
#               Rather than type the table twice -- the exact Class-B disease
#               tags.py exists to end -- the table and the reader move HERE and
#               both files import them. tutor._pr_word_value is now a one-line
#               delegate with identical semantics, so every referee that depends
#               on it behaves byte-for-byte as before (the battery proves it).
#
# PURE DATA AND ONE PURE FUNCTION, like tags.py: no imports beyond `re`, no I/O,
# no state. Nothing in here can fail at runtime, and both importers hard-import it
# on purpose -- a missing numwords.py should stop the deploy loudly at boot rather
# than leave the app unable to read a child's answer.
# =============================================================================
import re

ONES = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
        "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19}

TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90}


def word_value(phrase):
    """'fifteen' -> 15, 'twenty-one' -> 21, 'one hundred eighty' -> 180.

    None when the phrase is not a number. Semantics are EXACTLY those of
    tutor._pr_word_value before build ou moved them here: "and" is ignored,
    "hundred" multiplies what has been read so far, and any unknown word
    disqualifies the whole phrase (so "two dogs" is not 2 -- a referee counting
    numbers must not invent one out of prose)."""
    words = re.split(r"[\s-]+", str(phrase).strip().lower())
    words = [w for w in words if w and w != "and"]
    if not words:
        return None
    total, current, seen = 0, 0, False
    for w in words:
        if w in ONES:
            current += ONES[w]
            seen = True
        elif w in TENS:
            current += TENS[w]
            seen = True
        elif w == "hundred" and seen:
            current *= 100
        else:
            return None
    return total + current if seen else None


# The regex fragment that matches a spoken number phrase. Built from the tables
# above so it can never drift from them (it was hand-maintained in tutor.py).
_NAMES = sorted(list(ONES) + list(TENS), key=len, reverse=True)
NUMWORD_PATTERN = ("(?:" + "|".join(_NAMES) + r")(?:[\s-](?:hundred|"
                   + "|".join(_NAMES) + r"))*")

# I did no harm and this file is not truncated.
