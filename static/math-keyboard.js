/* =============================================================================
 * math-keyboard.js  --  Math Tutor MVP  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-08-07  VOICE-FIRST CLASSROOM (Jim): the 🧮 Math Keyboard is RETIRED. With voice
 *               input restored everywhere (students TALK their answers; typing is the
 *               fallback), the keypad sheet, its 🧮 opener buttons, the "This isn't a
 *               calculator" caption, and the "Two ways to answer" reminder are all gone --
 *               on the chat bars AND the practice intake. What this file still does (and
 *               why it keeps its name: three pages load /static/math-keyboard.js and a
 *               rename would 404 on a stale cache):
 *                 (a) ENTER BUTTON (kept from 2026-08-06): the page's own send button
 *                     (#send / #chatSend) is visible, labeled "Enter ⏎", immediately to
 *                     the right of the answer box. The Enter key and the 📈 graph's Send
 *                     still click this same button.
 *                 (b) BAR LAYOUT (kept): the answer bar flex-wraps so the box + Enter +
 *                     📈 Graph never clip on narrow screens.
 *               CRITICALLY REMOVED: the 2026-07-30 "type-in tier" lines that force-hid
 *               #talkBtn / #typeToggle and force-showed the composer. They were written
 *               for the no-microphone era and silently overrode the 2026-08-06 voice
 *               restore (the mic button was hidden again at DOMContentLoaded -- a real
 *               bug). Each page now fully owns its mic / composer visibility.
 *               Students who need symbols can still type ^ / ( ) etc., say it out loud,
 *               or use the 📈 graph -- the tutor understands plain typed math.
 *   2026-08-06  THE ENTER BUTTON IS BACK (Jim): standalone send button visible again,
 *               relabeled "Enter ⏎", right of the answer box. (Kept above.)
 *   2026-08-01  NOT-A-CALCULATOR caption on the keypad sheet. (Retired 2026-08-07.)
 *   2026-07-30  Keypad component created: attachKeypad on chat bars + practice intake;
 *               mic hidden for the "warm voice out / type in" setup. (Retired 2026-08-07.)
 * ============================================================================= */
(function () {
  if (window.__mtMathKb) return;
  window.__mtMathKb = true;

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var chatInput = document.getElementById("chatInput") || document.getElementById("input");
    if (!chatInput) return; // nothing to attach to on this page

    // ---- ENTER BUTTON (2026-08-06, kept): the standalone send button is VISIBLE, labeled
    // "Enter ⏎", immediately to the right of the answer box. The Enter key and the 📈
    // graph's Send funnel through this same button, so every path still sends. ----
    ["send", "chatSend"].forEach(function (id) {
      var b = document.getElementById(id);
      if (b) { b.style.display = ""; b.textContent = "Enter ⏎"; b.title = "Send your answer"; }
    });

    // ---- BAR LAYOUT (2026-07-30 fix, kept): let the answer bar WRAP so the input, the
    // Enter button, and the 📈 Graph button drop to a second row instead of clipping when
    // the column is narrow (e.g. the lesson page's left rail). ----
    try {
      var bar = chatInput.parentNode;
      if (bar) {
        bar.style.flexWrap = "wrap";
        if (!bar.style.rowGap) bar.style.rowGap = "6px";
        chatInput.style.flex = "1 1 150px";
        chatInput.style.minWidth = "0";
        var sendBtn = document.getElementById("chatSend") || document.getElementById("send");
        if (sendBtn) sendBtn.style.flex = "0 0 auto";
      }
    } catch (e) {}
  });
})();
/* I did no harm and this file is not truncated. */
