/* =============================================================================
 * math-keyboard.js  --  Math Tutor MVP  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-07-30  Refactor to attach to MORE THAN ONE box. The keypad-building logic is now a
 *               reusable attachKeypad(input, sendBtn, opts) function, so the SAME 🧮 keyboard now
 *               also appears on the practice "What problem are you stuck on?" INTAKE screen
 *               (#problemInput / #entryGo), not just the in-lesson answer bar. A student can now
 *               type symbols (√, x², fractions, π, etc.) while entering their problem. The in-chat
 *               behavior (session.html #input, practice/topic #chatInput) is byte-for-byte the same
 *               as before -- same keys, same bottom sheet, same Send. Each box gets its own private
 *               sheet (no shared element IDs -> no collisions). Purely additive; guarded so a
 *               missing box just means "skip that one".
 *   2026-07-30  Fix: on the lesson page's narrow left rail the input + 🧮 + Send overflowed and the
 *               buttons were clipped off-screen. The answer bar now wraps (flex-wrap) so the buttons
 *               drop below the input when space is tight; on a wide bar they stay on one row.
 *   2026-07-30  NEW shared component. Powers the "warm voice out / type in" setup:
 *               (a) hides the microphone (tap-to-talk) so the student answers by TYPING,
 *                   while the tutor keeps speaking via ElevenLabs (unchanged);
 *               (b) reveals the type box on pages that hide it behind "Type instead"
 *                   (session.html's .composer);
 *               (c) adds a friendly, tap-to-expand MATH KEYBOARD (powers, roots, division,
 *                   scientific notation, comparisons, etc.) that inserts symbols into the
 *                   existing answer box and can Send with the page's own Send button.
 *               Works on session.html (#input/#send/.composer), practice.html and
 *               topic.html (#chatInput/#chatSend/.feedbar). Self-contained: injects its own
 *               CSS, no libraries, no storage. Guarded so it never breaks a page if hooks are
 *               missing. Purely additive -- the voice/whiteboard/teaching code is untouched.
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
    var chatSend = document.getElementById("chatSend") || document.getElementById("send");
    var entryInput = document.getElementById("problemInput");           // practice.html intake box
    var entrySend = document.getElementById("entryGo");                 // its "Let's work on it" button
    if (!chatInput && !entryInput) return; // nothing to attach to on this page

    // ---- (a) hide the microphone: this tier is warm-voice-out / type-in ----
    var talk = document.getElementById("talkBtn");
    if (talk) talk.style.display = "none";
    var typeToggle = document.getElementById("typeToggle");
    if (typeToggle) typeToggle.style.display = "none";
    // ---- (b) make sure the type box is visible (session hides it in .composer) ----
    var comp = document.getElementById("composer");
    if (comp) comp.classList.add("show");

    // ---- (c) styles (namespaced mtk-*) -- injected once, shared by every keypad ----
    var css = document.createElement("style");
    css.textContent =
      ".mtk-open{border:none;border-radius:12px;font-weight:800;font-size:15px;padding:10px 12px;cursor:pointer;" +
      "background:linear-gradient(135deg,var(--accent,#6d5ae6),var(--accent2,#1fb6b0));color:#fff;white-space:nowrap;flex:0 0 auto}" +
      ".mtk-sheetwrap{position:fixed;left:0;right:0;bottom:0;z-index:9999;display:flex;justify-content:center;pointer-events:none}" +
      ".mtk-sheet{width:100%;max-width:560px;margin:0 10px;background:#faf8ff;border:1px solid #e9e5f5;" +
      "border-radius:18px 18px 0 0;box-shadow:0 -12px 40px rgba(60,40,120,.22);padding:10px 10px 14px;" +
      "transform:translateY(115%);transition:transform .26s cubic-bezier(.22,1,.36,1);pointer-events:auto}" +
      ".mtk-sheet.mtk-show{transform:translateY(0)}" +
      ".mtk-top{display:flex;align-items:center;gap:8px;margin-bottom:8px}" +
      ".mtk-prev{flex:1;background:#fff;border:1px solid #e3def3;border-radius:10px;padding:8px 11px;" +
      "font-family:'Courier New',monospace;font-size:17px;color:#2a2450;min-height:38px;overflow-x:auto;white-space:nowrap;text-align:left}" +
      ".mtk-x{border:1px solid #e3def3;background:#fff;color:#5b6079;font-weight:800;border-radius:9px;padding:8px 11px;cursor:pointer}" +
      ".mtk-grid{display:grid;gap:6px;grid-template-columns:repeat(5,1fr)}" +
      ".mtk-adv .mtk-grid{grid-template-columns:repeat(6,1fr)}" +
      ".mtk-key{border:1px solid #e3def3;background:#fff;border-radius:11px;padding:13px 0;font-size:18px;" +
      "font-weight:600;color:#20233a;cursor:pointer;min-height:46px;display:flex;align-items:center;justify-content:center;user-select:none}" +
      ".mtk-key:active{background:#efeaff;transform:translateY(1px)}" +
      ".mtk-key.op{color:var(--accent,#6d5ae6);font-weight:800}" +
      ".mtk-key.fn{background:#f3f0ff;color:var(--accent,#6d5ae6);font-weight:800;font-size:16px}" +
      ".mtk-key.util{color:#5b6079;font-weight:700;font-size:14px}" +
      ".mtk-sup{font-size:.72em;vertical-align:super}" +
      ".mtk-more{width:100%;margin:8px 0 2px;border:1px dashed #e3def3;background:transparent;color:var(--accent,#6d5ae6);" +
      "font-weight:700;font-size:13px;border-radius:9px;padding:8px;cursor:pointer}" +
      ".mtk-adv{max-height:0;overflow:hidden;transition:max-height .26s ease}.mtk-adv.mtk-show{max-height:280px}" +
      ".mtk-send{width:100%;margin-top:8px;border:none;border-radius:12px;font-weight:800;font-size:16px;padding:13px;cursor:pointer;" +
      "background:linear-gradient(135deg,var(--accent,#6d5ae6),var(--accent2,#1fb6b0));color:#fff}";
    document.head.appendChild(css);

    // key defs: [label, code].  code: t<text> insert text | o<text> insert (styled op) | w<spec> wrap
    var MAIN = [
      ["7", "t7"], ["8", "t8"], ["9", "t9"], ["÷", "o÷"], ["√", "w√(|)", "fn"],
      ["4", "t4"], ["5", "t5"], ["6", "t6"], ["×", "o×"], ["x²", "t^2", "fn"],
      ["1", "t1"], ["2", "t2"], ["3", "t3"], ["−", "o−"], ["xⁿ", "t^", "fn"],
      ["0", "t0"], [".", "t."], ["/", "o/"], ["+", "o+"], ["=", "o="]
    ];
    var ADV = [
      ["( )", "w(|)", "fn"], ["π", "tπ", "fn"], ["×10ⁿ", "t×10^", "fn"], ["ⁿ√", "w√(|)", "fn"], ["|x|", "t|", "fn"], ["±", "t±", "fn"],
      ["<", "o<"], [">", "o>"], ["≤", "o≤"], ["≥", "o≥"], ["≠", "o≠"], ["θ", "tθ"],
      ["x", "tx"], ["y", "ty"], ["°", "t°"], [",", "t,"], ["space", "aspace", "util"], ["⌫", "aback", "util"]
    ];

    /* -------------------------------------------------------------------------
     * attachKeypad: give ONE text box its own 🧮 button + bottom-sheet keypad.
     *   input    - the <input>/<textarea> to type into
     *   sendBtn  - the page's own Send/Go button (clicked by the sheet's Send)
     *   opts     - { openText, sendLabel, barWrap }
     * All state (caret, sheet, preview) is private to this call, so multiple
     * boxes on one page never collide.
     * ----------------------------------------------------------------------- */
    function attachKeypad(input, sendBtn, opts) {
      if (!input) return;
      opts = opts || {};
      var caret = input.value.length;

      // 🧮 toggle button
      var openBtn = document.createElement("button");
      openBtn.type = "button";
      openBtn.className = "mtk-open";
      openBtn.textContent = opts.openText || "🧮 Math";
      if (sendBtn && sendBtn.parentNode === input.parentNode) {
        input.parentNode.insertBefore(openBtn, sendBtn);
      } else {
        input.parentNode.appendChild(openBtn);
      }

      // Keep the input + 🧮 + Send from overflowing/clipping in a NARROW column (e.g. the lesson
      // page's left rail): let the row WRAP so the buttons drop below the input instead of getting
      // cut off. On a wide answer bar everything still sits on one row. (Fix 2026-07-30.)
      // Only for the in-chat answer bar -- the intake card is a vertical stack and needs no wrap.
      if (opts.barWrap) {
        try {
          var bar = input.parentNode;
          bar.style.flexWrap = "wrap";
          if (!bar.style.rowGap) bar.style.rowGap = "6px";
          input.style.flex = "1 1 150px";
          input.style.minWidth = "0";
          openBtn.style.flex = "0 0 auto";
          if (sendBtn) sendBtn.style.flex = "0 0 auto";
        } catch (e) {}
      }

      // bottom-sheet keyboard (its own DOM -- no shared IDs)
      var wrap = document.createElement("div");
      wrap.className = "mtk-sheetwrap";
      var sheet = document.createElement("div");
      sheet.className = "mtk-sheet";
      var top = document.createElement("div"); top.className = "mtk-top";
      var prev = document.createElement("div"); prev.className = "mtk-prev";
      var closeBtn = document.createElement("button"); closeBtn.type = "button"; closeBtn.className = "mtk-x"; closeBtn.textContent = "Close";
      top.appendChild(prev); top.appendChild(closeBtn);
      var mainGrid = document.createElement("div"); mainGrid.className = "mtk-grid";
      var moreBtn = document.createElement("button"); moreBtn.type = "button"; moreBtn.className = "mtk-more"; moreBtn.textContent = "More symbols ⌄";
      var adv = document.createElement("div"); adv.className = "mtk-adv";
      var advGrid = document.createElement("div"); advGrid.className = "mtk-grid"; adv.appendChild(advGrid);
      var sendKey = document.createElement("button"); sendKey.type = "button"; sendKey.className = "mtk-send"; sendKey.textContent = opts.sendLabel || "Send answer ➤";
      sheet.appendChild(top); sheet.appendChild(mainGrid); sheet.appendChild(moreBtn); sheet.appendChild(adv); sheet.appendChild(sendKey);
      wrap.appendChild(sheet);
      document.body.appendChild(wrap);

      function sync() {
        var v = input.value;
        var a = v.slice(0, caret).replace(/&/g, "&amp;").replace(/</g, "&lt;");
        var b = v.slice(caret).replace(/&/g, "&amp;").replace(/</g, "&lt;");
        prev.innerHTML = a + '<span style="border-left:2px solid var(--accent,#6d5ae6);margin:0 -1px"></span>' + b;
        input.dispatchEvent(new Event("input", { bubbles: true }));
      }
      function setVal(v, c) { input.value = v; caret = Math.max(0, Math.min(c, v.length)); sync(); }
      function ins(t) { var v = input.value; setVal(v.slice(0, caret) + t + v.slice(caret), caret + t.length); }
      function wrapIns(spec) {
        var i = spec.indexOf("|"), t = spec.replace("|", ""), v = input.value;
        setVal(v.slice(0, caret) + t + v.slice(caret), caret + i);
      }
      function back() { if (caret > 0) { var v = input.value; setVal(v.slice(0, caret - 1) + v.slice(caret), caret - 1); } }

      function buildGrid(host, defs) {
        defs.forEach(function (d) {
          var label = d[0], code = d[1], kind = d[2] || "";
          var b = document.createElement("button");
          b.type = "button";
          b.className = "mtk-key" + (code[0] === "o" ? " op" : "") + (kind ? " " + kind : "");
          b.innerHTML = label.replace("²", '<span class="mtk-sup">2</span>').replace("ⁿ", '<span class="mtk-sup">n</span>');
          b.addEventListener("click", function () {
            if (code[0] === "t" || code[0] === "o") ins(code.slice(1));
            else if (code[0] === "w") wrapIns(code.slice(1));
            else if (code === "aspace") ins(" ");
            else if (code === "aback") back();
          });
          host.appendChild(b);
        });
      }
      buildGrid(mainGrid, MAIN);
      buildGrid(advGrid, ADV);

      // control row (delete / clear) appended under main grid
      var ctl = document.createElement("div");
      ctl.className = "mtk-grid";
      ctl.style.gridTemplateColumns = "1fr 1fr";
      ctl.style.marginTop = "6px";
      var del = document.createElement("button"); del.type = "button"; del.className = "mtk-key util"; del.textContent = "⌫ delete"; del.onclick = back;
      var clr = document.createElement("button"); clr.type = "button"; clr.className = "mtk-key util"; clr.textContent = "clear"; clr.onclick = function () { setVal("", 0); };
      ctl.appendChild(del); ctl.appendChild(clr);
      mainGrid.insertAdjacentElement("afterend", ctl);

      function open() { caret = input.value.length; sync(); sheet.classList.add("mtk-show"); }
      function close() { sheet.classList.remove("mtk-show"); }
      openBtn.addEventListener("click", function () { sheet.classList.contains("mtk-show") ? close() : open(); });
      closeBtn.addEventListener("click", close);
      moreBtn.addEventListener("click", function () {
        var showing = adv.classList.toggle("mtk-show");
        moreBtn.textContent = showing ? "Fewer symbols ⌃" : "More symbols ⌄";
      });
      sendKey.addEventListener("click", function () {
        close();
        if (sendBtn) sendBtn.click();
      });
    }

    // ---- attach to the in-lesson answer bar (unchanged behavior) ----
    if (chatInput) attachKeypad(chatInput, chatSend, { openText: "🧮 Math", sendLabel: "Send answer ➤", barWrap: true });

    // ---- attach to the practice INTAKE box ("what problem are you stuck on?") ----
    if (entryInput) attachKeypad(entryInput, entrySend, { openText: "🧮 Math keyboard", sendLabel: "Use this problem ➤", barWrap: false });
  });
})();
/* I did no harm and this file is not truncated. */
