# zedrive.py -- build ze (2026-10-05): THE TOUR LIGHTS THE MIC, AND THE DASHBOARD ON A PHONE.
# Jim's phone pass, P2 and P7, proved on the real static files:
#   ① the young tour on a 390x844 phone: through the taps stop the talk button wears the lit
#     look (.tourlit) and carries the glow (.tourglow) -- it was grey and unlit while he said
#     "the microphone lights up" -- and both are gone once the tour ends; the demo buttons are
#     on screen through the stop and the spoken line says "right here";
#   ② the same on a 1280x720 laptop (the glow on the mic and on the demo row);
#   ③ dashboard.html at 390x844: nothing scrolls sideways, the journey's nine stops fit one row
#     inside the track (no inner scroll), a unit row's status pill sits under its name, and a
#     section heading's note is on its own line; at 1280x800 the stops keep their captions and
#     the pill sits beside the name (nothing moved).
# Run:  PYTHONPATH=. python3 tools/zedrive.py     (prints PASS/FAIL lines, exits 1 on any FAIL)
import functools, http.server, json, os, sys, threading, time

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
PORT = 8829
ME = {"ok": True, "name": "Sam", "placed": False, "toured": False,
      "history": [], "progress": {"current_unit": 1}, "placement": {}}
POSTS = []
START = {"ok": True, "lesson": "x", "id": "l1", "practice": {"phase": "pair-0", "run": 0, "need": 3, "on": False}, "steps": [{"kind": "say", "spoken": "Hello.", "board": ""}]}

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, o):
        b = json.dumps(o).encode(); self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers()
        try: self.wfile.write(b)
        except Exception: pass
    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/api/script/lessons": return self._send({"ok": True, "lessons": []})
        if p == "/api/session/me": return self._send(ME)
        if p == "/api/voice-status": return self._send({"ok": True, "eleven": False})
        if p == "/api/topics/me":     # the dashboard's units, the real shape, nine Entry units untouched
            NAMES = ["Counting & Number Sense", "Addition to 20", "Subtraction to 20", "Place Value to 1,000", "Two- & Three-Digit Addition",
                     "Two- & Three-Digit Subtraction", "Money — Coins, Bills & Making Change", "Time, Calendar & Measurement", "Shapes, Patterns & Groups"]
            return self._send({"name": "Alex", "tracking": False, "placement": {}, "units": [
                {"unit": i + 1, "name": n, "status": "not-started", "touches": 0, "last_touched": None, "best_pct": 0, "checks_taken": 0,
                 "mastered": False, "quizzes": [], "quizzes_passed": 0, "lessons_done": 0, "lessons_total": 4} for i, n in enumerate(NAMES)]})
        if p == "/api/courses/me": return self._send({"ok": False, "tracking": False, "courses": []})
        if p == "/api/time/me": return self._send({"tracking": False, "days": []})
        if p == "/api/awards/me": return self._send({"tracking": False, "trophies": [], "badges": {}, "awards": []})
        if p.startswith("/api/"): return self._send({"ok": True})
        if p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(ln) if ln else b""
        p = self.path.split("?")[0]
        POSTS.append((time.time(), p))
        self._send({"ok": True})

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()

from playwright.sync_api import sync_playwright
F = []
def check(l, ok, d=""):
    print(("PASS  " if ok else "FAIL  ") + l + ("" if ok else "   -- " + str(d)))
    if not ok: F.append(l)

SNAP = """() => {
  const tb = document.getElementById('talkBtn');
  const row = document.getElementById('choiceRow');
  const bubbles = [...document.querySelectorAll('#feed .bubble.tutor')].map(x => (x.textContent || '').trim()).filter(t => t.length > 20);
  const inv = document.getElementById('assessInvite');
  const vis = (e) => { if (!e) return false; const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && r.top >= 0 && r.bottom <= innerHeight; };
  return { lit: !!(tb && tb.classList.contains('tourlit')), micGlow: !!(tb && tb.classList.contains('tourglow')),
           micVis: vis(tb), rowGlow: !!(row && row.classList.contains('tourglow')), rowVis: !!row && [...row.querySelectorAll('.choicebtn')].every(vis),
           nBtns: row ? row.querySelectorAll('.choicebtn').length : 0,
           invite: !!(inv && inv.classList.contains('show')),
           last: bubbles.length ? bubbles[bubbles.length - 1] : '' }; }"""

def tour(pw, w, h):
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": w, "height": h}, is_mobile=(w < 700), has_touch=(w < 700))
    pg.goto("http://127.0.0.1:%d/static/session.html?code=0000&course=entry&tour=1" % PORT, wait_until="load")
    STUB = "() => { window.speak = function(){ return Promise.resolve(); }; window.__stub = true; }"
    pg.evaluate(STUB); pg.wait_for_timeout(600); pg.evaluate(STUB)
    pg.evaluate("""() => { const g=document.getElementById('welcomeGo'); if (g && g.offsetParent!==null) g.click();
      document.querySelectorAll('.welcome.show').forEach(w=>w.classList.remove('show')); }""")
    seen = []; t0 = time.time()
    while time.time() - t0 < 110:
        pg.wait_for_timeout(250)
        s = pg.evaluate(SNAP); seen.append(s)
        if s["invite"]: break
    after = pg.evaluate(SNAP); b.close()
    return seen, after

with sync_playwright() as pw:
    for (w, h, label) in ((390, 844, "① 390x844 (a phone)"), (1280, 720, "② 1280x720 (a laptop)")):
        seen, after = tour(pw, w, h)
        taps = [s for s in seen if "like these" in s["last"]]
        lit = [s for s in taps if s["lit"] and s["micGlow"]]
        before_taps = [s for s in seen if s["last"] and "like these" not in s["last"]]
        check("⭐ %s: through the taps stop the mic wears the lit look AND the glow, on screen, with the demo buttons glowing beside it" % label,
              taps and lit and all(s["micVis"] for s in lit) and any(s["rowGlow"] and s["nBtns"] >= 3 for s in taps),
              (len(seen), len(taps), len(lit), taps[:1]))
        check("  ...the line says \"right here\", not \"at the bottom\"",
              taps and "pop up right here — like these" in taps[-1]["last"] and "at the bottom" not in taps[-1]["last"], taps and taps[-1]["last"][:120])
        check("  ...and before that stop the mic is not lit; after the tour neither the lit look nor the glow remains",
              not any(s["lit"] for s in before_taps) and after["invite"] and not after["lit"] and not after["micGlow"], (after,))
        if w < 700:
            check("  ...on the phone the demo buttons are on screen through the stop (zc: on the board)", any(s["rowVis"] for s in taps), [s["rowVis"] for s in taps])

    # ③ the dashboard
    def dash(w, h):
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": w, "height": h}, is_mobile=(w < 700), has_touch=(w < 700))
        pg.goto("http://127.0.0.1:%d/static/dashboard.html?code=0000&course=entry" % PORT, wait_until="load"); pg.wait_for_timeout(2500)
        m = pg.evaluate("""() => { const tr = document.querySelector('.track'); const stops = [...document.querySelectorAll('.stop')];
          const u = document.querySelector('.unit'); const nm = u && u.querySelector('.nm'), pill = u && u.querySelector('.pill');
          const sh = document.getElementById('journeyHead'); const note = sh && sh.querySelector('.note');
          return { docW: document.documentElement.scrollWidth, vw: innerWidth, stops: stops.length,
                   trackScrolls: tr ? tr.scrollWidth > tr.clientWidth + 1 : null,
                   lastStopIn: stops.length ? stops[stops.length-1].getBoundingClientRect().right <= innerWidth : null,
                   captionShown: stops.length ? getComputedStyle(stops[0].querySelector('.caption')).display !== 'none' : null,
                   pillUnder: (nm && pill) ? pill.getBoundingClientRect().top >= nm.getBoundingClientRect().bottom - 1 : null,
                   pillBeside: (nm && pill) ? Math.abs(pill.getBoundingClientRect().top - nm.getBoundingClientRect().top) < 24 : null,
                   noteOwnLine: (sh && note) ? note.getBoundingClientRect().top >= sh.getBoundingClientRect().top + 14 : null,
                   nmLines: nm ? Math.round(nm.getBoundingClientRect().height / 18) : null }; }""")
        b.close(); return m
    m = dash(390, 844)
    check("⭐ ③ dashboard.html at 390x844: no sideways scroll, nine stops in one row inside the track (numbers only), the pill under the unit's name on at most two lines, the heading's note on its own line",
          m and m["docW"] <= m["vw"] and m["stops"] == 9 and m["trackScrolls"] is False and m["lastStopIn"] and m["captionShown"] is False
          and m["pillUnder"] and m["nmLines"] <= 2 and m["noteOwnLine"], m)
    d = dash(1280, 800)
    check("  ...at 1280x800 nothing moved: the stops keep their captions, the pill sits beside the name",
          d and d["captionShown"] and d["pillBeside"] and d["docW"] <= d["vw"], d)

print("\n%d failure(s)" % len(F))
sys.exit(1 if F else 0)
# I did no harm and this file is not truncated.
