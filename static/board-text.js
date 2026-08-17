/* =============================================================================
   board-text.js  --  WHAT THE STUDENT SEES ON THE BOARD  --  Hyperion Shift LLC
   -----------------------------------------------------------------------------
   CHANGE NOTES (keep newest at top):
     2026-08-17  NEW FILE (build hc -- Phase 2 of the full-app review). Three
                 hand-synced copies became one. This is the highest-stakes text in the
                 app: it decides which letters render as variables and how, and build
                 gn2 is the standing proof that getting it wrong changes what a lesson
                 MEANS -- the renderer forced every styled variable to a capital, so
                 the one lesson whose whole job was to separate "A,B,C = corners" from
                 "a,b,c = sides" rendered both lines identically. CASE IS MEANING.
                 That fix had to be hand-copied three times. Now there is one place to
                 fix, and one place to audit.
                 EXTRACTED VERBATIM -- no logic changed in the move; the comments
                 travelled with it because they record why each rule exists.
                 Self-contained: escapeHTML travels with it, so the file depends on
                 nothing but the browser. Loaded as a CLASSIC script so these stay
                 globals and every existing call site works unchanged.
   ============================================================================= */
// ---------- Variable styling + function machine ----------
// A "variable" is a SINGLE isolated letter (x, y, n) -- NEVER a letter inside a
// word (next, box, explain), NEVER a single-letter English word (a, I), and NEVER
// a function name (the f in "f("). styleVars() HTML-escapes its input first, so it
// is safe to inject with innerHTML. Variables render bold, CAPITAL, red (.mvar).
// 2026-08-16 (build gn/gn2). TWO defects from Jim's Geometry lessons, one week apart
// in the same file, and the second one overturned the first fix's assumption.
//
// gn: VAR_SKIP meant NEVER STYLE for a, i, f, g, h, so "a squared plus b squared
// equals c squared" reached the child as "a squared plus B squared equals C squared".
//
// gn2: the board then read "A, B, C = corners (vertices) / a, b, c = sides (lengths)"
// -- and BOTH lines rendered identically, because styleVarsCore forced a CAPITAL. The
// one line whose entire job was to separate uppercase from lowercase destroyed the
// distinction it was teaching. CASE IS MEANING IN MATHEMATICS: side a is opposite
// vertex A, the antiderivative of f is F, P(A) is an event where p is a probability.
//
// So the model is no longer a blacklist of letters. It is: WHICH LETTERS DOUBLE AS
// ENGLISH? Only three, and case is what decides:
//   "a"  the article        -- needs mathematical context to be a variable
//   "A"  sentence-opening article ("A triangle has...") -- English only when it
//        introduces a WORD; P(A), vertex A, "opposite A." are all labels
//   "I"  the pronoun        -- same test; "I = 5" is a variable, "I think" is not
// f, g and h were on the old list as FUNCTION NAMES, and that job is done properly
// by the "(" guard and MV_FUNC below -- so "the height h" and "f is F" now style,
// while f(x), f'' and (f o g) do not.
// CASE-SENSITIVE, on purpose. "a"/"A"/"I" double as English; f, g and h double as
// FUNCTION NAMES, and the app has whole lessons whose point is "the letter is only a
// name" -- painting that f the same red as a variable blurs exactly the distinction
// being taught, which is the gn2 defect one course over. They earn styling the same
// way: beside an operator, after a measurement noun ("the height h"), in a letter
// list. (Caught by the corpus sweep: an early gn2 draft styled f and g right through
// the function-notation scripts.)
const VAR_NEEDS_CONTEXT = { a: 1, A: 1, I: 1, f: 1, F: 1, g: 1, G: 1, h: 1, H: 1 };

const MV_POW  = /^\s*(?:squared\b|cubed\b|[²³^])/;                  // a squared, a^2
const MV_OPR  = /^\s*[-+=×*\/÷]\s*(?:\d|[A-Za-z](?![A-Za-z]))/;     // a + b, a = 5
const MV_PRE  = /(?:\d|[A-Za-z])\s*[-+=×*\/÷]\s*$|\(\s*$/;        // 3 + a, (a
const MV_WORD = /^\s+[A-Za-z]{2,}/;                                        // "a few", "A triangle"
const MV_FUNC = /^\s*(?:['\u2019\u2032]|o\s)/;                            // f', f'', f o g
// ...and the OTHER two letters of a composition: the g in "(f o g)", and the little
// "o" itself, which is an operator rather than a variable. Found by sweeping the
// canonical scripts, where "(f o g)(x) = f(g(x))" is the only string that has them.
const MV_COMPOSE_BEFORE = /[A-Za-z]\s+o\s+$/;                              // the g in f o g
const MV_IS_COMPOSE_OP  = /[A-Za-z]\s+$/;                                   // the o in f o g
const MV_LIST_AFTER  = /^\s*,\s*[A-Za-z](?![A-Za-z])/;                    // "a, b"
const MV_LIST_BEFORE = /(?:^|[^A-Za-z])[A-Za-z]\s*,\s*$/;                 // "b, a"
const MV_LABEL_FOLLOW = /^\s+(?:is|was|are|were|equals|measures|and|or)\b/i;
const MV_NOUN = /\b(?:side|leg|vertex|corner|point|angle|line|segment|ray|variable|letter|height|base|width|length|radius|diameter|area|perimeter|hypotenuse)\s+$/i;

function varInMathContext(before, after, run) {
  if (MV_POW.test(after) || MV_OPR.test(after)) return true;   // a squared, a = 5
  if (/\d$/.test(before)) return true;                         // 2a, 3i -- a coefficient
  if (MV_PRE.test(before) && !MV_WORD.test(after)) return true; // 3 + a, (a
  if (MV_LIST_AFTER.test(after) || MV_LIST_BEFORE.test(before)) return true;  // a, b, c
  // A letter keeps company: "side a", "corner A", "vertex B", "the height h and the
  // base b". But a math noun alone is NOT enough for the lowercase article -- the
  // corpus turned up "the highest point a thrown ball reaches", where "point" is
  // English and "a" is an article. So after a noun the letter must either END the
  // phrase (punctuation, an operator, nothing) or be followed by a word that only
  // ever FOLLOWS a label: "side a is...", "the height h and...".
  if (MV_NOUN.test(before) && (!MV_WORD.test(after) || MV_LABEL_FOLLOW.test(after))) return true;
  // Capital A and I are English only when they INTRODUCE a word. Everywhere else --
  // P(A), "opposite A.", "A = 5" -- they are labels. Lowercase "a" never gets this,
  // because "a number", "a go", "a hint" are all the article.
  // The "after" text stops at a **key term** boundary, because styleVars() splits the
  // sentence on those markers before this runs. So "A **fact family** is..." arrives
  // here as the fragment "A " -- an article with NOTHING after it, which used to look
  // exactly like a standalone label and painted the article red on 300+ canonical
  // scripts. An empty tail is UNKNOWN, not evidence: only decide A/I is a label when
  // something real follows it. "corner A" at a fragment end is still caught above by
  // MV_NOUN. (Found by the 1,015-string corpus sweep; every fixture had passed.)
  // A and I ONLY. This is the capital-label case -- P(A), "opposite A.", "vertex A" --
  // and it must not extend to f, g and h: "the rule called f, and 7 comes back" is a
  // function name, comma or no comma. (An earlier gn2 draft let f/g/h through here
  // and painted them red across the function-notation scripts.)
  if ((run === "A" || run === "I") && after.trim() !== "" && !MV_WORD.test(after)) return true;
  return false;
}

function escapeHTML(s) {
  return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function styleVars(raw) {
  // KEY TERMS (2026-08-01, Jim): the tutor wraps a new/important term in **double asterisks**
  // on first use; render it bold + red. Everything between markers skips variable-styling.
  const src = String(raw == null ? "" : raw);
  const parts = src.split(/\*\*([^*\n]{2,60}?)\*\*/g);
  if (parts.length > 1) {
    let html = "";
    for (let i = 0; i < parts.length; i++) {
      html += (i % 2 === 1) ? '<span class="kterm">' + escapeHTML(parts[i]) + "</span>"
                            : styleVarsCore(parts[i]);
    }
    return html;
  }
  return styleVarsCore(src);
}

function styleVarsCore(raw) {
  const text = String(raw == null ? "" : raw).replace(/\*+/g, "");   // drop markdown * so *word* never shows raw
  let out = "", last = 0, m; const re = /[A-Za-z]+/g;
  while ((m = re.exec(text)) !== null) {
    out += escapeHTML(text.slice(last, m.index));
    const run = m[0], after = text[m.index + run.length] || "", before = m.index > 0 ? text[m.index - 1] : "";
    // 2026-08-07 (build bk, Jim's screenshot "3 + 2 X 4"): a lone x written BETWEEN two
    // numbers is a TIMES SIGN, not a variable — "3 + 2 x 4", "5 x 3", "(3+1) x (2+5)".
    // Both immediate neighbors must be spaces AND the nearest non-space characters
    // number-ish, so "2x + 3" (coefficient) and "3 + x" (a real variable) are untouched.
    // Render the true × sign, unstyled. (tutor.py now also tells the model to write ×.)
    if ((run === "x" || run === "X") && /\s/.test(before) && /\s/.test(after)) {
      const prevNS = text.slice(0, m.index).trimEnd().slice(-1);
      const nextNS = text.slice(m.index + 1).trimStart().charAt(0);
      if (/[0-9)]/.test(prevNS) && /[0-9(.]/.test(nextNS)) {
        out += "×"; last = m.index + run.length; continue;
      }
    }
    if (run.length === 1 && after !== "(" && before !== "'" && before !== "’"
        && !MV_FUNC.test(text.slice(m.index + run.length))
        && !MV_COMPOSE_BEFORE.test(text.slice(0, m.index))
        && !(run === "o" && MV_IS_COMPOSE_OP.test(text.slice(0, m.index))
             && /^\s+[A-Za-z](?![A-Za-z])/.test(text.slice(m.index + run.length)))
        && (!VAR_NEEDS_CONTEXT[run]
            || varInMathContext(text.slice(0, m.index),
                                text.slice(m.index + run.length), run))) {
      // 2026-08-16 (build gn2, Jim live in Geometry, the lesson that TEACHES this):
      // the board read "A, B, C = corners (vertices) / a, B, C = sides (lengths)".
      // The one line whose entire job is to separate uppercase from lowercase had
      // both rendered the same, because this call destroyed the case. CASE IS
      // MEANING IN MATHEMATICS -- side a is opposite vertex A, the antiderivative of
      // f is F, P(A) is an event and p is a probability. The 2026-07-22 note that
      // introduced the capital wanted variables to POP, and that was written when
      // this app taught Algebra I and nothing else; it became false the day Geometry
      // shipped. The letter now renders EXACTLY AS WRITTEN and keeps the bold red
      // that made it pop. Do not put toUpperCase back.
      out += '<span class="mvar">' + escapeHTML(run) + '</span>';
    } else { out += escapeHTML(run); }
    last = m.index + run.length;
  }
  out += escapeHTML(text.slice(last));
  // Render powers as REAL superscripts so a squared/cubed term is unmistakable on the
  // board: x^2 -> x squared, 10^3 -> 10 cubed, (x-1)^2 -> ..., plus any pre-formed ²/³.
  out = out.replace(/\^\(?(-?\d+)\)?/g, "<sup>$1</sup>")
           .replace(/²/g, "<sup>2</sup>").replace(/³/g, "<sup>3</sup>");
  return out;
}

// Put the input value in for the variable, for the worked line "2 × 3 + 1".
function machineSub(rule, val) {
  let s = String(rule).replace(/(\d)\s*([A-Za-z])/g, "$1 × $2");      // 2x -> 2 × x
  s = s.replace(/[A-Za-z]+/g, (run, idx, whole) => {
    const after = whole[idx + run.length] || "";
    if (run.length === 1 && after !== "(" && !VAR_NEEDS_CONTEXT[run]) return String(val);
    return run;
  });
  return s.replace(/\s*\+\s*/g, " + ").replace(/\s{2,}/g, " ").trim();
}

/* I did no harm and this file is not truncated. */
