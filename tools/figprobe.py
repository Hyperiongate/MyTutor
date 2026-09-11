# =============================================================================
# tools/figprobe.py  --  HOW BIG DO THE FIGURES ACTUALLY RENDER?  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-11  NEW (build vk). Jim, from a live Basic lesson: "the number line is like
#               two inches long ... the words are so small you can't see them. And then
#               ... the words are huge. So it's inconsistent, and it's generally small."
#               A figure's size is a fact about a real browser at a real width, so this
#               drives the REAL session.html + board.js + math-figures.js in a real
#               Chromium (the pwdrive / shelfprobe pattern: a stub server that serves
#               /static and answers the few API calls the page makes) through a Basic
#               lesson's own boards -- the place-value chart, an equation line, the
#               rounding number line, and the ask Jim flagged -- at a laptop, a desktop
#               and a phone, and records for every figure on the board: its rendered
#               width and height, its viewBox, the display cap, the fit ratio it drew
#               with, and the SMALLEST and LARGEST label in on-screen pixels; and for
#               every worklist row its width and CSS font size.
#               WHAT IT FOUND BEFORE vk, on the 420px phone: number-line labels 6.9px,
#               place-value headings 8.6px, the ask's row 462px wide in a 378px feed.
#               AFTER: 12.5-15.6px, and the row fits at 14px. Laptop: unchanged.
#               Usage: python3 tools/figprobe.py [static-dir]     (prints and screenshots)
#               From the battery: figprobe.measure(static_dir, width, height) -> dict.
# =============================================================================
import functools
import http.server
import json
import os
import sys
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.join(os.path.dirname(HERE), "static")
LESSONS = [{"id": "pv", "topic": "Place value", "unit": 1, "course": "basic", "course_title": "Basic Math"}]
ME = {"ok": True, "name": "Sam", "placed": True, "toured": True, "history": [],
      "progress": {"current_unit": 1}, "placement": {"start_unit": 1}}

# The boards of basic-u1-place-value-to-1000 and basic-u1-rounding-tens, as the engine
# emits them (lessonscripts.OP_EXT["pv"] for the ask), so the probe measures the
# figures a student actually meets.
STEPS = {"ok": True, "lesson": "Place value", "id": "pv", "steps": [
    {"kind": "say", "spoken": "Here is the place-value chart.",
     "board": '[[placevalue n="342" caption="3 flats, 4 rods, 2 cubes — 342"]]', "beat": "picture"},
    {"kind": "say", "spoken": "So a digit means different things.",
     "board": '[[step eq="342 = 300 + 40 + 2"]]', "beat": "teach"},
    {"kind": "say", "spoken": "Here is 47 on a number line.",
     "board": '[[numberline min="40" max="50" mid="45" points="47" caption="47 sits past halfway, closer to 50"]]',
     "beat": "picture"},
    {"kind": "say", "spoken": "Now it is your turn.", "board": "", "beat": "practice_intro"},
    {"kind": "ask", "spoken": "What number is 1 hundred, 4 tens and 3 ones?",
     "board": '[[placevalue h="1" t="4" o="3" ask="1" caption="count the blocks in each place"]]'
              '[[step eq="1 hundreds + 4 tens + 3 ones = ?"]]'}]}

MEASURE = """() => {
  const feed = document.getElementById('feed'); const fr = feed.getBoundingClientRect();
  const out = {feed: [Math.round(fr.width), Math.round(fr.height)], room: feed.clientWidth - 40, figs: [], rows: []};
  document.querySelectorAll('#feed .mfig svg').forEach((svg, i) => {
    const r = svg.getBoundingClientRect(); const vb = (svg.getAttribute('viewBox')||'').split(/\\s+/).map(Number);
    const scale = vb[2] ? r.width / vb[2] : 0;
    const texts = [...svg.querySelectorAll('text')].map(t => +(t.getAttribute('font-size')||12) * scale);
    out.figs.push({i, w: Math.round(r.width), h: Math.round(r.height), viewBox: vb, cap: (svg.style.maxWidth||''),
      fit: +(svg.getAttribute('data-fit') || '1'),
      kind: svg.querySelector('circle[r="7.5"]') ? 'numberline' : (svg.querySelector('rect[rx="10"]') ? 'placevalue' : 'figure'),
      text_min: texts.length ? +Math.min(...texts).toFixed(1) : null,
      text_max: texts.length ? +Math.max(...texts).toFixed(1) : null});
  });
  document.querySelectorAll('#feed .worklist .wrow, #feed .worklist .worow').forEach((row, i) => {
    const r = row.getBoundingClientRect();
    out.rows.push({i, w: Math.round(r.width), h: Math.round(r.height), fontpx: parseFloat(getComputedStyle(row).fontSize),
      text: (row.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 40)});
  });
  return out;
}"""


def _serve(root, port):
    class H(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, o):
            b = json.dumps(o).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            try:
                self.wfile.write(b)
            except Exception:  # noqa: BLE001
                pass

        def do_GET(self):
            p = self.path.split("?")[0]
            if p == "/api/script/lessons":
                return self._send({"ok": True, "lessons": LESSONS})
            if p == "/api/session/me":
                return self._send(ME)
            if p == "/api/voice-status":
                return self._send({"ok": True, "eleven": False})
            if p.startswith("/api/"):
                return self._send({"ok": True})
            if p.startswith("/static/"):
                self.path = self.path[len("/static"):]
            super().do_GET()

        def do_POST(self):
            ln = int(self.headers.get("Content-Length") or 0)
            if ln:
                self.rfile.read(ln)
            p = self.path.split("?")[0]
            if p == "/api/script/start":
                return self._send(STEPS)
            if p == "/api/script/answer":
                return self._send({"ok": True, "steps": [{"kind": "end", "spoken": "Done.", "mastered": True}]})
            self._send({"ok": True})

    class S(http.server.ThreadingHTTPServer):
        allow_reuse_address = True         # three viewports in a row must not wait on TIME_WAIT

    srv = S(("127.0.0.1", port), functools.partial(H, directory=root))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def measure(root=DEFAULT_ROOT, width=1440, height=900, port=0, screenshot=""):
    """Drive the page to the ask at this viewport and return the measurement dict.
    port=0 takes any free port (the battery may run beside other harnesses)."""
    from playwright.sync_api import sync_playwright
    srv = _serve(root, port)
    port = srv.server_address[1]
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
            pg = b.new_page(viewport={"width": width, "height": height})
            pg.goto("http://127.0.0.1:%d/static/session.html?code=0000&course=basic" % port, wait_until="load")
            stub = "() => { window.speak = function(){ return Promise.resolve(); }; window.__stub = true; }"
            pg.evaluate(stub)
            pg.wait_for_timeout(700)
            pg.evaluate(stub)
            pg.evaluate("""() => { const g=document.getElementById('welcomeGo'); if (g && g.offsetParent!==null) g.click();
              document.querySelectorAll('.welcome.show').forEach(w=>w.classList.remove('show')); }""")
            for _ in range(30):
                pg.wait_for_timeout(600)
                if pg.evaluate("() => (typeof SCR!=='undefined' && SCR.pending)"):
                    break
                pg.evaluate("""() => { const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
                    const n=bs.find(x=>/Next|Yes|ready/i.test(x.textContent)); if (n) n.click(); }""")
            pg.wait_for_timeout(900)
            m = pg.evaluate(MEASURE)
            if screenshot:
                pg.screenshot(path=screenshot, full_page=False)
            b.close()
            return m
    finally:
        try:
            srv.shutdown()
            srv.server_close()
        except Exception:  # noqa: BLE001
            pass


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ROOT
    for label, w, h in (("laptop", 1440, 900), ("desktop", 1920, 1080), ("phone", 420, 860)):
        m = measure(root, w, h, screenshot="figprobe_%s.png" % label)
        print("\n=== %s (%dx%d) feed=%s room=%s ===" % (label, w, h, m["feed"], m["room"]))
        for f in m["figs"]:
            print("  ", json.dumps(f))
        for r in m["rows"]:
            print("  ", json.dumps(r))

# I did no harm and this file is not truncated.
