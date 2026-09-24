# xxdrive.py -- build xx (2026-09-24): THE CHILD-MODE SKIN, DRIVEN IN A REAL BROWSER.
# Serves the real static files with a stub API (the pwdrive.py pattern) and opens the
# lesson page twice -- once as Entry, once as Pre-Algebra -- to prove the four parts of
# the skin on the real page, the real board.js and the real board-theme.css:
#   ① the WARM BOARD: Entry's feed is cream on the light board, navy on the dark one;
#     Pre-Algebra's feed is still white.
#   ② BIGGER TAP TARGETS: Entry's answer buttons are >= 72px tall at 26px type;
#     Pre-Algebra's are the old 52px / 20px.
#   ③ THREE-IN-A-ROW DOTS: hidden at the start (practice.on = false), shown with one lit
#     dot after the first graded answer (on = true, run = 1), and NEVER shown on
#     Pre-Algebra even when the server says on = true.
#   ④ THE HELPER TEXT LEAVES: the "How to answer" line and #hint are visible before the
#     first answer and display:none after it -- on Entry only.
# Run:  PYTHONPATH=. python3 tools/xxdrive.py     (prints PASS/FAIL lines, exits 1 on any FAIL)
import functools, http.server, json, os, sys, threading

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
PORT = 8813
ME = {"ok": True, "name": "Sam", "placed": True, "toured": True,
      "history": [], "progress": {"current_unit": 1}, "placement": {"start_unit": 1}}

def lessons_for(course):
    return {"ok": True, "lessons": [{"id": course + "-l1", "topic": "Counting", "unit": 1,
                                     "course": course, "course_title": course}]}

START = {"ok": True, "lesson": "Counting", "id": "l1",
         "practice": {"phase": "pair-0", "run": 0, "need": 3, "on": False},
         "steps": [
  {"kind": "say", "spoken": "Two and two.", "board": '[[step eq="2 + 2 = 4"]]'},
  {"kind": "ask", "spoken": "What is 3 plus 1?",
   "board": '[[step eq="3 + 1 = ?"]][[choices options="4 | 5 | 3"]]'}]}

ANSWER = {"ok": True,
          "practice": {"phase": "practice", "run": 1, "need": 3, "on": True},
          "streak": {"today_streak": 1, "streak_days": 1},
          "steps": [
  {"kind": "say", "spoken": "Yes, 4.", "board": '[[step eq="3 + 1 = 4"]]'},
  {"kind": "ask", "spoken": "What is 2 plus 1?",
   "board": '[[step eq="2 + 1 = ?"]][[choices options="3 | 4 | 2"]]'}]}

CUR = {"course": "entry"}

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
        if p == "/api/script/lessons": return self._send(lessons_for(CUR["course"]))
        if p == "/api/session/me": return self._send(ME)
        if p == "/api/voice-status": return self._send({"ok": True, "eleven": False})
        if p.startswith("/api/"): return self._send({"ok": True})
        if p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        if ln: self.rfile.read(ln)
        p = self.path.split("?")[0]
        if p == "/api/script/start": return self._send(START)
        if p == "/api/script/answer": return self._send(ANSWER)
        self._send({"ok": True})

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()

from playwright.sync_api import sync_playwright
F = []
def check(l, ok, d=""):
    print(("PASS  " if ok else "FAIL  ") + l + ("" if ok else "   -- " + str(d)))
    if not ok: F.append(l)

STATE = """() => {
  const cs = (el) => el ? getComputedStyle(el) : null;
  const feed = document.getElementById('feed');
  const btn = document.querySelector('.choicerow .choicebtn:not(.notsure)');
  const eh = document.querySelector('.elem-hint'), hint = document.getElementById('hint');
  const dots = document.getElementById('runDots');
  return {
    elem: document.body.classList.contains('elem-mode'),
    settled: document.body.classList.contains('elem-settled'),
    feedBg: cs(feed) && cs(feed).backgroundColor,
    btnH: btn ? btn.getBoundingClientRect().height : -1,
    btnFont: btn ? cs(btn).fontSize : '',
    ehShown: !!(eh && cs(eh).display !== 'none'),
    hintShown: !!(hint && cs(hint).display !== 'none'),
    dotsShown: !!(dots && !dots.hidden && cs(dots).display !== 'none'),
    dotsOn: dots ? dots.querySelectorAll('.rd.on').length : -1,
    dotsLab: dots ? (document.getElementById('runDotsLab') || {}).textContent : ''
  };
}"""

def play(pw, course):
    CUR["course"] = course
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1400, "height": 900})
    pg.goto("http://127.0.0.1:%d/static/session.html?code=0000&course=%s" % (PORT, course),
            wait_until="load")
    STUB = "() => { window.speak = function(){ return Promise.resolve(); }; window.__stub = true; }"
    pg.evaluate(STUB); pg.wait_for_timeout(700); pg.evaluate(STUB)
    pg.evaluate("""() => { const g=document.getElementById('welcomeGo');
      if (g && g.offsetParent!==null) g.click();
      document.querySelectorAll('.welcome.show').forEach(w=>w.classList.remove('show')); }""")
    for _ in range(14):
        pg.wait_for_timeout(700)
        if pg.evaluate("() => (typeof SCR!=='undefined' && SCR.pending)"): break
        pg.evaluate("""() => { const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
            const n=bs.find(x=>/Next/.test(x.textContent)); if (n) n.click(); }""")
    pg.wait_for_timeout(900)
    before = pg.evaluate(STATE)
    # the dark board, then back to white
    pg.evaluate("() => { try { MTBoard.apply('dark'); } catch (e) { document.getElementById('feed').setAttribute('data-board','dark'); } }")
    pg.wait_for_timeout(200)
    dark_bg = pg.evaluate("() => getComputedStyle(document.getElementById('feed')).backgroundColor")
    pg.evaluate("() => { try { MTBoard.apply('white'); } catch (e) { document.getElementById('feed').setAttribute('data-board','white'); } }")
    pg.wait_for_timeout(200)
    # the first answer: tap the right button
    pg.evaluate("""() => { const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
        const n=bs.find(x=>x.textContent.trim()==='4'); if (n) n.click(); }""")
    pg.wait_for_timeout(1800)
    after = pg.evaluate(STATE)
    b.close()
    return before, dark_bg, after

with sync_playwright() as pw:
    print("\n--- ENTRY ---")
    eb, edark, ea = play(pw, "entry")
    print("   before:", eb); print("   dark:", edark); print("   after:", ea)
    check("⭐ ① Entry: the light board is the warm cream (#fff8e8)", eb["feedBg"] == "rgb(255, 248, 232)", eb["feedBg"])
    check("  ① Entry: the dark board is still the navy (#221f33)", edark == "rgb(34, 31, 51)", edark)
    check("⭐ ② Entry: the answer buttons are at least 72px tall at 26px type",
          eb["btnH"] >= 72 and eb["btnFont"] == "26px", (eb["btnH"], eb["btnFont"]))
    check("⭐ ③ Entry: no dots before practice (the server said on = false)", not eb["dotsShown"], eb)
    check("⭐ ③ Entry: after the first graded answer the dots show ONE lit of three",
          ea["dotsShown"] and ea["dotsOn"] == 1 and ea["dotsLab"] == "1 of 3 in a row", ea)
    check("⭐ ④ Entry: the helper text is there for the first answer...", eb["ehShown"] and eb["hintShown"], eb)
    check("⭐ ④ ...and gone after it", ea["settled"] and not ea["ehShown"] and not ea["hintShown"], ea)

    print("\n--- PRE-ALGEBRA (do no harm) ---")
    pb, pdark, pa = play(pw, "prealgebra")
    print("   before:", pb); print("   dark:", pdark); print("   after:", pa)
    check("⭐ Pre-Algebra: the light board is still white", pb["feedBg"] == "rgb(255, 255, 255)", pb["feedBg"])
    check("  Pre-Algebra: the dark board is still the navy", pdark == "rgb(34, 31, 51)", pdark)
    check("⭐ Pre-Algebra: the answer buttons are the old size (52px / 20px)",
          50 <= pb["btnH"] < 60 and pb["btnFont"] == "20px", (pb["btnH"], pb["btnFont"]))
    check("⭐ Pre-Algebra: NO dots, even though the server said on = true", not pa["dotsShown"], pa)
    check("  Pre-Algebra: no elem-mode, no settling, the hint stays", not pb["elem"] and not pa["settled"] and pa["hintShown"], pa)

print("\n%d failure(s)" % len(F))
sys.exit(1 if F else 0)

# I did no harm and this file is not truncated.
