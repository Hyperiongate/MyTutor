/* =============================================================================
 * math-keyboard.js  --  Math Tutor MVP  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-08-25  ONE KEYBOARD, NOT TWO (build no; Jim's UI review, item 4): "if I
 *               decide to type things in, I want more of a conventional looking
 *               keyboard where I can type the letters AND the symbols... I don't
 *               want a combination of typing letters on my computer keyboard and
 *               then picking symbols out of the thing that pops up."
 *               THE SYMBOL STRIP: a slim row of math keys living INSIDE the answer
 *               bar itself (flex order:-1, so it sits directly above the input as
 *               the bar's first row). Nothing pops up and nothing floats:
 *                 - every key INSERTS AT THE CARET of the same input the physical
 *                   keyboard types into, so "2" [÷] "3" interleaves naturally;
 *                 - pointerdown + preventDefault keeps the input focused through
 *                   the tap -- the caret never jumps, mobile keyboards never close;
 *                 - the |x| key inserts BOTH bars and parks the caret between them;
 *                 - the strip lives inside the bar, so whenever a page hides its
 *                   composer (voice-first mode), the strip hides with it -- the
 *                   voice classroom is untouched.
 *               Attached to EVERY answer input on the page (session has one;
 *               practice/topic have an intake box and a chat box -- both get it).
 *               ⚠️ THIS IS NOT THE 2026-07-30 KEYPAD COMING BACK. That was a modal
 *               sheet that replaced the mic; this is a strip that decorates the
 *               typing path only. Voice stays the front door everywhere.
 *   2026-08-07  VOICE-FIRST CLASSROOM (Jim): the 🧮 Math Keyboard sheet RETIRED.
 *               Kept from that build, unchanged below: (a) the visible "Enter ⏎"
 *               send button; (b) the flex-wrap bar layout. (The file keeps its name:
 *               three pages load /static/math-keyboard.js and a rename would 404 on
 *               a stale cache.)
 *   2026-08-06  THE ENTER BUTTON IS BACK (Jim). Kept.
 *   2026-08-01  NOT-A-CALCULATOR caption. (Retired 2026-08-07.)
 *   2026-07-30  Keypad sheet created. (Retired 2026-08-07.)
 * ============================================================================= */
(function () {
  if (window.__mtMathKb) return;
  window.__mtMathKb = true;

  // The strip's keys: high-value symbols a physical keyboard makes awkward.
  // Each entry: [label, inserted text, caret offset from insert END (0 = after),
  // spoken-name tooltip]. The tooltip doubles as the reading (rule 48's spirit).
  var KEYS = [
    ["÷",  "÷",  0, "divided by"],
    ["×",  "×",  0, "times"],
    ["−",  "−",  0, "minus"],
    ["±",  "±",  0, "plus or minus"],
    ["²",  "²",  0, "squared"],
    ["³",  "³",  0, "cubed"],
    ["^",  "^",  0, "to the power of"],
    ["√",  "√",  0, "square root"],
    ["π",  "π",  0, "pi"],
    ["θ",  "θ",  0, "theta"],
    ["°",  "°",  0, "degrees"],
    ["(",  "(",  0, "open parenthesis"],
    [")",  ")",  0, "close parenthesis"],
    ["|x|", "||", 1, "absolute value — type between the bars"],
    ["≤",  "≤",  0, "less than or equal"],
    ["≥",  "≥",  0, "greater than or equal"],
    ["≠",  "≠",  0, "not equal"]
  ];

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  function ensureCSS() {
    if (document.getElementById("mtMathStripCSS")) return;
    var st = document.createElement("style");
    st.id = "mtMathStripCSS";
    st.textContent =
      ".mkstrip{flex:1 1 100%;order:-1;display:flex;flex-wrap:wrap;gap:4px;" +
      "padding:2px 0 4px}" +
      ".mkkey{min-width:30px;height:30px;padding:0 7px;border-radius:8px;" +
      "border:1px solid #e2ddf0;background:#faf9ff;color:#20233a;font-size:15px;" +
      "font-weight:700;cursor:pointer;line-height:1;display:inline-flex;" +
      "align-items:center;justify-content:center;user-select:none;" +
      "-webkit-user-select:none;touch-action:manipulation}" +
      ".mkkey:hover{background:#f0ecff;border-color:#c9beff}" +
      ".mkkey:active{transform:translateY(1px)}";
    document.head.appendChild(st);
  }

  // Insert at the caret of THIS input, keep focus, tell the page something typed.
  function insertAt(input, text, caretBack) {
    var s = (input.selectionStart != null) ? input.selectionStart : input.value.length;
    var e = (input.selectionEnd != null) ? input.selectionEnd : s;
    input.value = input.value.slice(0, s) + text + input.value.slice(e);
    var p = s + text.length - (caretBack || 0);
    try { input.setSelectionRange(p, p); } catch (err) {}
    try { input.dispatchEvent(new Event("input", { bubbles: true })); } catch (err) {}
    input.focus();
  }

  function attachStrip(input) {
    var bar = input.parentNode;
    if (!bar || bar.querySelector(".mkstrip")) return;
    ensureCSS();
    var strip = document.createElement("div");
    strip.className = "mkstrip";
    KEYS.forEach(function (k) {
      var b = document.createElement("button");
      b.type = "button"; b.className = "mkkey";
      b.textContent = k[0]; b.title = k[3];
      b.setAttribute("aria-label", k[3]);
      // pointerdown + preventDefault: the input NEVER loses focus, the caret never
      // jumps, and a phone's on-screen keyboard never closes mid-answer.
      b.addEventListener("pointerdown", function (ev) {
        ev.preventDefault();
        insertAt(input, k[1], k[2]);
      });
      // keyboard/AT users activate via click (pointerdown already handled pointers;
      // guard so a mouse click does not double-insert).
      b.addEventListener("click", function (ev) {
        if (ev.detail === 0) insertAt(input, k[1], k[2]);   // detail 0 = keyboard
      });
      strip.appendChild(b);
    });
    bar.appendChild(strip);          // order:-1 floats it to the bar's first row
  }

  ready(function () {
    // ---- ENTER BUTTON (2026-08-06, kept): visible, labeled, right of the box. ----
    ["send", "chatSend"].forEach(function (id) {
      var b = document.getElementById(id);
      if (b) { b.style.display = ""; b.textContent = "Enter ⏎"; b.title = "Send your answer"; }
    });

    // ---- BAR LAYOUT (2026-07-30 fix, kept) + THE STRIP (2026-08-25), for EVERY
    // answer input on the page: session has #input; practice/topic have an intake
    // #input and a chat #chatInput. Each bar wraps, each bar gets its own strip. ----
    ["chatInput", "input"].forEach(function (id) {
      var inp = document.getElementById(id);
      if (!inp) return;
      try {
        var bar = inp.parentNode;
        if (bar) {
          bar.style.flexWrap = "wrap";
          if (!bar.style.rowGap) bar.style.rowGap = "6px";
          inp.style.flex = "1 1 150px";
          inp.style.minWidth = "0";
          var sendBtn = document.getElementById("chatSend") || document.getElementById("send");
          if (sendBtn) sendBtn.style.flex = "0 0 auto";
        }
        attachStrip(inp);
      } catch (e) {}
    });
  });
})();
/* I did no harm and this file is not truncated. */
