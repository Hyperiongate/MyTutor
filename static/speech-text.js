/* =============================================================================
   speech-text.js  --  WHAT THE TUTOR SAYS OUT LOUD  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-08-17  NEW FILE (build hc -- Phase 2 of the full-app review). These
                 transforms were THREE hand-synced copies, one each in session.html,
                 topic.html and practice.html. Identical today is not identical
                 tomorrow: the review measured ~2,400 duplicated lines across those
                 pages, and build gz found two LIVE defects that existed only because
                 a fix reached one copy and not its siblings. One copy is the cure.
                 EXTRACTED VERBATIM -- not one character of logic changed in the move,
                 and the comments came with it, because here the reasoning IS the
                 code: every rule below was written from something a real child heard.
                 SCOPE, deliberately narrow: this file is TEXT ONLY -- what a string
                 should sound like. The voice CONTROL functions that sat beside it
                 (speechDeadline, stopAllSpeech, withDeadline) stayed in the pages
                 because they read page state (`paused`, `ttsAudio`); they belong to a
                 later voice.js that moves that state with them. Extracting them here
                 would have thrown a ReferenceError on the first pause.
                 Loaded as a CLASSIC script so these stay globals and every existing
                 call site works unchanged.
   ============================================================================= */
// Turn written math into words the voice can say cleanly (the visuals carry
// the actual notation). Prevents "x parenthesis parenthesis", "times x", etc.
// 2026-08-08 (build bp, Jim: "$1.85" was spoken as "one dot eight five — no dollar,
// no cents"): money is read as money, plain decimals as "point", never "dot".
//   $1.85 -> "1 dollar and 85 cents"   $3.75 -> "3 dollars and 75 cents"
//   $0.85 -> "85 cents"   $2 -> "2 dollars"   3.75 (no $) -> "3 point 7 5"
// 2026-08-09 (build bu, proactive audit #15): numbers are spoken the way people say
// them. A negative VALUE is "negative three" (never "minus"/"dash"); percents,
// ratios, common fractions and mixed numbers get their real names; thousands
// separators are dropped so a big number is read whole, not digit by digit.
var FRAC_WORDS = { "1/2": "one half", "1/3": "one third", "2/3": "two thirds",
  "1/4": "one fourth", "3/4": "three fourths", "1/5": "one fifth", "1/8": "one eighth",
  "1/10": "one tenth" };

function fracWords(m, a, b) { return FRAC_WORDS[a + "/" + b] || m; }

function mixedWords(m, whole, a, b) {
  var f = FRAC_WORDS[a + "/" + b] || (a + " over " + b);
  return whole + " and " + f;
}

function moneyWords(_, d, c) {
  const dollars = parseInt(d, 10);
  const cents = c === undefined ? null : parseInt(c, 10);
  const parts = [];
  if (dollars > 0 || cents === null || cents === 0)
    parts.push(dollars + (dollars === 1 ? " dollar" : " dollars"));
  if (cents !== null && cents > 0)
    parts.push(cents + (cents === 1 ? " cent" : " cents"));
  return parts.join(" and ");
}

function forSpeech(text) {
  return String(text)
    // build ga (2026-08-14): **bold** used to become TWO SPACES, which stranded a space
    // before whatever punctuation followed -- the log shows "that's a right angle ." going
    // to the voice -- and the voice reads that gap as a hesitation. Pairs go first and
    // leave nothing behind; a stray single asterisk still becomes a space, as before.
    .replace(/\*\*/g, "")
    .replace(/\*+/g, " ")                                       // strip markdown *
    .replace(/\$\s*(\d+)(?:\.(\d{1,2}))?/g, moneyWords)
    .replace(/(\d),(\d{3})\b/g, "$1$2")                            // 1,234 -> read whole
    .replace(/(^|[(=+\u00d7\u00f7*])\s*[-\u2212](\d)/g, "$1 negative $2")   // VALUE negatives
    .replace(/(\d+)\s+(\d+)\s*\/\s*(\d+)\b/g, mixedWords)         // 2 1/2 -> two and one half
    .replace(/\b(\d+)\s*\/\s*(\d+)\b/g, fracWords)                // 1/2 -> one half
    .replace(/\s*%/g, " percent ")                                  // 20% -> 20 percent
    .replace(/(\d)\s*:\s*(\d)/g, "$1 to $2")                       // 3:2 -> 3 to 2         // $1.85 -> 1 dollar and 85 cents
    .replace(/(\d)\.(\d+)/g, (m, a, b) => a + " point " + b.split("").join(" "))  // 3.75 -> 3 point 7 5
    .replace(/([A-Za-z])\s*\(\s*([A-Za-z0-9]+)\s*\)/g, "$1 of $2")  // f(x) -> f of x
    // build ga (2026-08-14): parentheses used to be DELETED, so the screen's "narrower
    // (a sharper turn), some are wider (a lazier, more open turn)" was SPOKEN as
    // "narrower a sharper turn , some are wider a lazier, more open turn ." -- the aside
    // ran straight into the sentence with no pause at all. A comma keeps the break the
    // writer meant. f(x) is already handled on the line above, so this never touches it.
    .replace(/\s*\(\s*/g, ", ").replace(/\s*\)\s*/g, ", ")
    .replace(/\s*=\s*/g, " equals ")
    .replace(/\s*\+\s*/g, " plus ")
    .replace(/(\d)\s*[-\u2212]\s*(\d)/g, "$1 minus $2")   // 2026-08-09: the board's
    .replace(/\s[-\u2212]\s/g, " minus ")                    // Unicode minus counts too
    .replace(/\s*[×*]\s*/g, " times ")
    .replace(/\s*[÷]\s*/g, " divided by ")
    .replace(/(\w)\s*\/\s*(\w)/g, "$1 over $2")
    .replace(/²/g, " squared ")
    .replace(/³/g, " cubed ")
    .replace(/π/g, " pi ")
    .replace(/θ/g, " theta ")
    .replace(/±/g, " plus or minus ")
    .replace(/≥/g, " is greater than or equal to ")
    .replace(/≤/g, " is less than or equal to ")
    .replace(/≠/g, " is not equal to ")
    .replace(/°/g, " degrees ")
    .replace(/\^/g, " to the power ")
    .replace(/√/g, " square root of ")
    // build ga (2026-08-14): tidy what the substitutions above leave behind -- a space
    // before punctuation, a comma butted against other punctuation, doubled commas, or a
    // sentence that now opens with one. Without this the voice hesitates in odd places.
    .replace(/\s+([,.;:!?])/g, "$1")
    .replace(/([,;:])[,;:]+/g, "$1")
    .replace(/,([.!?])/g, "$1")
    .replace(/^[\s,;:]+/, "")
    .replace(/\s{2,}/g, " ")
    .trim();
}

/* I did no harm and this file is not truncated. */
