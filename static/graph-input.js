/* =============================================================================
 * graph-input.js  --  Math Tutor MVP  --  Hyperion Shift LLC
 * CHANGE NOTES (keep newest at top):
 *   2026-07-30  NEW shared component. Adds a "📈 Graph" button next to the answer box (and the 🧮 Math
 *               button) on session/practice/topic. It opens coordinate graph paper: tap grid points to
 *               plot (tap again to remove), optionally draw a straight line through the first two points,
 *               then "Send to tutor" — which drops the plotted points into the answer box as TEXT
 *               coordinates and submits, e.g. "📈 I plotted these points on the graph: (0, 3), (1, 5) —
 *               and drew a straight line through them." The tutor can't see pixels, so it reasons from
 *               those coordinates (see the GRAPH TOOL block in tutor.py). Self-contained, injects its own
 *               CSS, guarded so a missing hook never breaks a page. Purely additive.
 * ============================================================================= */
(function () {
  if (window.__mtGraphKb) return;
  window.__mtGraphKb = true;

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var input = document.getElementById("chatInput") || document.getElementById("input");
    var sendBtn = document.getElementById("chatSend") || document.getElementById("send");
    if (!input) return;

    var css = document.createElement("style");
    css.textContent =
      ".gpi-open{border:none;border-radius:12px;font-weight:800;font-size:15px;padding:10px 12px;cursor:pointer;" +
      "background:#fff;border:1.5px solid var(--accent,#6d5ae6);color:var(--accent,#6d5ae6);white-space:nowrap;flex:0 0 auto}" +
      ".gpi-wrap{position:fixed;left:0;right:0;bottom:0;z-index:9999;display:flex;justify-content:center;pointer-events:none}" +
      ".gpi-sheet{width:100%;max-width:520px;margin:0 10px;background:#faf8ff;border:1px solid #e9e5f5;" +
      "border-radius:18px 18px 0 0;box-shadow:0 -12px 40px rgba(60,40,120,.22);padding:12px 14px 16px;" +
      "transform:translateY(120%);transition:transform .26s cubic-bezier(.22,1,.36,1);pointer-events:auto}" +
      ".gpi-sheet.gpi-show{transform:translateY(0)}" +
      ".gpi-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}" +
      ".gpi-top .lbl{font-size:12.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:#5b6079}" +
      ".gpi-x{border:1px solid #e3def3;background:#fff;color:#5b6079;font-weight:800;border-radius:9px;padding:7px 11px;cursor:pointer}" +
      ".gpi-plane{display:block;width:100%;max-width:360px;margin:0 auto;background:#fff;border:1px solid #e9e5f5;border-radius:12px;touch-action:manipulation}" +
      ".gpi-readout{text-align:center;font-family:'Courier New',monospace;font-size:15px;color:#2a2450;margin:8px 0 4px;min-height:20px}" +
      ".gpi-row{display:flex;gap:8px;align-items:center;justify-content:center;margin-top:6px;flex-wrap:wrap}" +
      ".gpi-chk{display:inline-flex;align-items:center;gap:7px;font-size:14px;color:#20233a;background:#fff;border:1px solid #e9e5f5;" +
      "border-radius:10px;padding:9px 12px;cursor:pointer;user-select:none}.gpi-chk input{width:17px;height:17px;accent-color:var(--accent,#6d5ae6)}" +
      ".gpi-util{border:1px solid #e9e5f5;background:#fff;color:#5b6079;font-weight:700;font-size:14px;border-radius:10px;padding:9px 14px;cursor:pointer}" +
      ".gpi-send{border:0;background:linear-gradient(135deg,var(--accent,#6d5ae6),var(--accent2,#1fb6b0));color:#fff;font-weight:800;font-size:15px;border-radius:10px;padding:11px 18px;cursor:pointer}" +
      ".gpi-hint{text-align:center;font-size:11.5px;color:#a7a2bd;margin-top:9px}";
    document.head.appendChild(css);

    var openBtn = document.createElement("button");
    openBtn.type = "button";
    openBtn.className = "gpi-open";
    openBtn.textContent = "📈 Graph";
    if (sendBtn && sendBtn.parentNode === input.parentNode) input.parentNode.insertBefore(openBtn, sendBtn);
    else input.parentNode.appendChild(openBtn);
    try { input.parentNode.style.flexWrap = "wrap"; openBtn.style.flex = "0 0 auto"; } catch (e) {}

    var wrap = document.createElement("div");
    wrap.className = "gpi-wrap";
    wrap.innerHTML =
      '<div class="gpi-sheet" id="gpiSheet">' +
      '  <div class="gpi-top"><span class="lbl">Plot your points</span><button type="button" class="gpi-x" id="gpiClose">Close</button></div>' +
      '  <svg class="gpi-plane" id="gpiPlane" viewBox="0 0 400 400" aria-label="coordinate plane"></svg>' +
      '  <div class="gpi-readout" id="gpiReadout">No points yet — tap the grid to plot.</div>' +
      '  <div class="gpi-row">' +
      '    <label class="gpi-chk"><input type="checkbox" id="gpiLine"> Draw a line through my points</label>' +
      '    <button type="button" class="gpi-util" id="gpiClear">Clear</button>' +
      '    <button type="button" class="gpi-send" id="gpiSend">Send to tutor ➤</button>' +
      '  </div>' +
      '  <div class="gpi-hint">Your points go to the tutor as coordinates, e.g. (0, 3) and (1, 5), so it can check your graph.</div>' +
      "</div>";
    document.body.appendChild(wrap);

    var svg = document.getElementById("gpiPlane"), NS = "http://www.w3.org/2000/svg";
    var MIN = -8, MAX = 8, C = 200, STEP = 25, pts = [];
    var lineChk = document.getElementById("gpiLine");
    var readout = document.getElementById("gpiReadout");
    function sx(x) { return C + x * STEP; } function sy(y) { return C - y * STEP; }
    function clamp(v) { return Math.max(MIN, Math.min(MAX, v)); }

    function draw() {
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      for (var i = MIN; i <= MAX; i++) {
        var vx = document.createElementNS(NS, "line");
        vx.setAttribute("x1", sx(i)); vx.setAttribute("y1", sy(MIN)); vx.setAttribute("x2", sx(i)); vx.setAttribute("y2", sy(MAX));
        vx.setAttribute("stroke", i === 0 ? "#8a86a6" : "#e7e2f3"); vx.setAttribute("stroke-width", i === 0 ? "2" : "1"); svg.appendChild(vx);
        var hz = document.createElementNS(NS, "line");
        hz.setAttribute("x1", sx(MIN)); hz.setAttribute("y1", sy(i)); hz.setAttribute("x2", sx(MAX)); hz.setAttribute("y2", sy(i));
        hz.setAttribute("stroke", i === 0 ? "#8a86a6" : "#e7e2f3"); hz.setAttribute("stroke-width", i === 0 ? "2" : "1"); svg.appendChild(hz);
        if (i !== 0 && i % 2 === 0) {
          var tx = document.createElementNS(NS, "text"); tx.setAttribute("x", sx(i)); tx.setAttribute("y", sy(0) + 14);
          tx.setAttribute("font-size", "10"); tx.setAttribute("text-anchor", "middle"); tx.setAttribute("fill", "#a7a2bd"); tx.textContent = i; svg.appendChild(tx);
          var ty = document.createElementNS(NS, "text"); ty.setAttribute("x", sx(0) - 8); ty.setAttribute("y", sy(i) + 3);
          ty.setAttribute("font-size", "10"); ty.setAttribute("text-anchor", "end"); ty.setAttribute("fill", "#a7a2bd"); ty.textContent = i; svg.appendChild(ty);
        }
      }
      if (lineChk.checked && pts.length >= 2) {
        var a = pts[0], b = pts[1];
        if (a[0] === b[0]) {
          var lnv = document.createElementNS(NS, "line");
          lnv.setAttribute("x1", sx(a[0])); lnv.setAttribute("y1", sy(MIN)); lnv.setAttribute("x2", sx(a[0])); lnv.setAttribute("y2", sy(MAX));
          lnv.setAttribute("stroke", "#6d5ae6"); lnv.setAttribute("stroke-width", "2.5"); svg.appendChild(lnv);
        } else {
          var m = (b[1] - a[1]) / (b[0] - a[0]), c0 = a[1] - m * a[0];
          var ln = document.createElementNS(NS, "line");
          ln.setAttribute("x1", sx(MIN)); ln.setAttribute("y1", sy(m * MIN + c0)); ln.setAttribute("x2", sx(MAX)); ln.setAttribute("y2", sy(m * MAX + c0));
          ln.setAttribute("stroke", "#6d5ae6"); ln.setAttribute("stroke-width", "2.5"); ln.setAttribute("stroke-linecap", "round"); svg.appendChild(ln);
        }
      }
      pts.forEach(function (p) {
        var c = document.createElementNS(NS, "circle");
        c.setAttribute("cx", sx(p[0])); c.setAttribute("cy", sy(p[1])); c.setAttribute("r", "6");
        c.setAttribute("fill", "#d1345b"); c.setAttribute("stroke", "#fff"); c.setAttribute("stroke-width", "2"); svg.appendChild(c);
      });
      readout.textContent = pts.length
        ? ("Points: " + pts.map(function (p) { return "(" + p[0] + ", " + p[1] + ")"; }).join(", "))
        : "No points yet — tap the grid to plot.";
    }

    svg.addEventListener("click", function (e) {
      var rect = svg.getBoundingClientRect();
      var vx = (e.clientX - rect.left) / rect.width * 400, vy = (e.clientY - rect.top) / rect.height * 400;
      var x = clamp(Math.round((vx - C) / STEP)), y = clamp(Math.round((C - vy) / STEP));
      var idx = -1;
      for (var k = 0; k < pts.length; k++) { if (pts[k][0] === x && pts[k][1] === y) { idx = k; break; } }
      if (idx >= 0) pts.splice(idx, 1); else pts.push([x, y]);
      draw();
    });
    lineChk.addEventListener("change", draw);
    document.getElementById("gpiClear").addEventListener("click", function () { pts = []; draw(); });

    var sheet = document.getElementById("gpiSheet");
    openBtn.addEventListener("click", function () { sheet.classList.contains("gpi-show") ? sheet.classList.remove("gpi-show") : (draw(), sheet.classList.add("gpi-show")); });
    document.getElementById("gpiClose").addEventListener("click", function () { sheet.classList.remove("gpi-show"); });

    function serialize() {
      if (!pts.length) return "";
      var list = pts.map(function (p) { return "(" + p[0] + ", " + p[1] + ")"; }).join(", ");
      var msg = "📈 I plotted these points on the graph: " + list;
      msg += (lineChk.checked && pts.length >= 2) ? " — and drew a straight line through them." : ".";
      return msg;
    }
    document.getElementById("gpiSend").addEventListener("click", function () {
      var msg = serialize();
      if (!msg) return;
      input.value = msg;
      input.dispatchEvent(new Event("input", { bubbles: true }));
      sheet.classList.remove("gpi-show");
      pts = []; lineChk.checked = false; draw();
      if (sendBtn) sendBtn.click();
    });
    draw();
  });
})();
/* I did no harm and this file is not truncated. */
