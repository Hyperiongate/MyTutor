# pwdrive.py -- build pw: A DIFFERENT PROBLEM IS NOT A STALE SNAPSHOT.
# Jim's order-of-operations screenshot: "3 + 2 x 5" and the worked "6 + 4 x 2" both
# hidden behind "show the 5 earlier steps" while the board sat almost empty.
# Drives the REAL board.js in a real browser, twice:
#   (A) THREE DIFFERENT problems  -> nothing may fold
#   (B) the SAME problem re-stated -> the older snapshot MUST fold (build oz's win)
import functools, http.server, json, threading

ROOT = "/root/MyTutor/static"; PORT = 8812
LESSONS = [{"id": "o1", "topic": "Order of operations", "unit": 1,
            "course": "prealgebra", "course_title": "Pre-Algebra"}]
ME = {"ok": True, "name": "Sam", "placed": True, "toured": True,
      "history": [], "progress": {"current_unit": 1}, "placement": {"start_unit": 1}}

# (A) Jim's actual sequence: three DIFFERENT problems, one after another.
DIFFERENT = {"ok": True, "lesson": "Order of operations", "id": "o1", "steps": [
  {"kind": "say", "spoken": "What is 3 plus 2 times 5?",
   "board": '[[step eq="3 + 2 × 5 = ?"]]'},
  {"kind": "say", "spoken": "That's it. 2 times 5 equals 10, and 3 plus 10 equals 13.",
   "board": '[[step eq="3 + 2 × 5 = 13"]]'},
  {"kind": "say", "spoken": "One more together. 6 plus 4 times 2 equals 14.",
   "board": '[[step eq="6 + 4 × 2 = 14"]]'},
  {"kind": "ask", "spoken": "What is 2 plus 3 times 6?",
   "board": '[[step eq="2 + 3 × 6 = ?"]][[choices options="20 | 30 | 11"]]'}]}

# (B) the SAME problem re-stated turn after turn -- rule 35's restatement.
SAME = {"ok": True, "lesson": "Order of operations", "id": "o1", "steps": [
  {"kind": "say", "spoken": "Here it is.", "board": '[[step eq="2 + 3 × 6 = ?"]]'},
  {"kind": "say", "spoken": "Times first.",
   "board": '[[step eq="2 + 3 × 6 = ?"]][[step eq="3 × 6 = 18"]]'},
  {"kind": "ask", "spoken": "So what is it?",
   "board": '[[step eq="2 + 3 × 6 = ?"]][[step eq="3 × 6 = 18"]][[step eq="2 + 18 = ?"]]'
            '[[choices options="20 | 30 | 11"]]'}]}

MODE = {"steps": DIFFERENT}

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
        if p == "/api/script/lessons": return self._send({"ok": True, "lessons": LESSONS})
        if p == "/api/session/me": return self._send(ME)
        if p == "/api/voice-status": return self._send({"ok": True, "eleven": False})
        if p.startswith("/api/"): return self._send({"ok": True})
        if p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        if ln: self.rfile.read(ln)
        p = self.path.split("?")[0]
        if p == "/api/script/start": return self._send(MODE["steps"])
        if p == "/api/script/answer":
            return self._send({"ok": True, "steps": [
              {"kind": "end", "spoken": "Done.", "mastered": True}]})
        self._send({"ok": True})

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()

from playwright.sync_api import sync_playwright
F = []
def check(l, ok, d=""):
    print(("PASS  " if ok else "FAIL  ") + l + ("" if ok else "   -- " + str(d)))
    if not ok: F.append(l)

STATE = """() => ({
  blocks: document.querySelectorAll('#feed .mblock').length,
  superseded: document.querySelectorAll('#feed .mblock.superseded').length,
  chip: (document.querySelector('#feed .supchip') || {}).textContent || '',
  chips: document.querySelectorAll('#feed .supchip').length,
  visibleRows: [...document.querySelectorAll('#feed .mblock')]
      .filter(b => !b.classList.contains('superseded'))
      .map(b => (b.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 40))
})"""

def play(pw, steps_payload, label):
    MODE["steps"] = steps_payload
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1400, "height": 900})
    pg.goto("http://127.0.0.1:%d/static/session.html?code=0000&course=prealgebra" % PORT,
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
    st = pg.evaluate(STATE)
    print("\n--- %s ---" % label); print("   ", st)
    b.close()
    return st

with sync_playwright() as pw:
    a = play(pw, DIFFERENT, "A: three DIFFERENT problems (Jim's screenshot)")
    check("⭐ three different problems: NOTHING is folded away",
          a["superseded"] == 0, a)
    check("  ...so no 'show the N earlier steps' chip appears at all",
          a["chip"] == "", a["chip"])
    check("  ...and the worked example is still on the board",
          any("6 + 4" in r for r in a["visibleRows"]), a["visibleRows"])
    check("  ...and so is the first question",
          any("3 + 2" in r for r in a["visibleRows"]), a["visibleRows"])

    b_ = play(pw, SAME, "B: the SAME problem re-stated (build oz must still work)")
    check("⭐ a re-stated snapshot of the SAME problem still folds",
          b_["superseded"] >= 1, b_)
    check("  ...and the chip is there to bring it back",
          "earlier step" in b_["chip"], b_["chip"])
    check("⭐ ...and there is exactly ONE chip, counting them all honestly",
          b_["chips"] == 1 and str(b_["superseded"]) in b_["chip"],
          {"chips": b_["chips"], "chip": b_["chip"], "folded": b_["superseded"]})

print("\n%d failure(s)" % len(F))
