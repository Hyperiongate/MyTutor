# yudrive.py -- build yu (2026-09-29): AN ANSWER ENDS A PAUSE, DRIVEN IN A REAL BROWSER.
# Jim's first-family playthrough, Entry unit 2 lesson 4: he tapped 12 on "what is
# 2 + 4 + 6?", the buttons vanished, nothing else happened, and the tutor sat waiting.
# The page was PAUSED (the status line had read "Paused"), and sendToTutor opened with
# `if (busy || paused) return;` -- board.js's tap handler had already cleared the row.
# This drive serves the real static files with a stub API (the xxdrive.py pattern),
# reaches the first ask, presses the real ⏸ Pause button, taps the right answer, and
# proves on the real session.html + board.js that:
#   ① the student's bubble appears (the answer was SENT, not dropped);
#   ② the next beats arrive (the stub's ANSWER: the praise and a fresh ask's buttons);
#   ③ the pause is released: the button reads "⏸ Pause" and the status line no longer
#     says "Paused";
#   ④ the same through the typed box: pause, type, Enter -- the bubble appears;
#   ⑤ and `busy` still gates: a tap while the page is busy leaves the row on screen.
# Run:  PYTHONPATH=. python3 tools/yudrive.py     (prints PASS/FAIL lines, exits 1 on any FAIL)
import functools, http.server, json, os, sys, threading

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
PORT = 8814
ME = {"ok": True, "name": "Sam", "placed": True, "toured": True,
      "history": [], "progress": {"current_unit": 1}, "placement": {"start_unit": 1}}

def lessons_for(course):
    return {"ok": True, "lessons": [{"id": course + "-l1", "topic": "Counting", "unit": 1,
                                     "course": course, "course_title": course}]}

START = {"ok": True, "lesson": "Counting", "id": "l1",
         "practice": {"phase": "pair-0", "run": 0, "need": 3, "on": False},
         "steps": [
  {"kind": "say", "spoken": "Two and two.", "board": '[[step eq="2 + 2 = 4"]]'},
  {"kind": "ask", "spoken": "What is 2 plus 4 plus 6?",
   "board": '[[step eq="2 + 4 + 6 = ?"]][[choices options="12 | 10 | 14"]]'}]}

ANSWER = {"ok": True,
          "practice": {"phase": "practice", "run": 1, "need": 3, "on": True},
          "streak": {"today_streak": 1, "streak_days": 1},
          "steps": [
  {"kind": "say", "spoken": "Yes, 12.", "board": '[[step eq="2 + 4 + 6 = 12"]]'},
  {"kind": "ask", "spoken": "What is 3 plus 1?",
   "board": '[[step eq="3 + 1 = ?"]][[choices options="4 | 5 | 3"]]'}]}

POSTS = []

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
        if p == "/api/script/lessons": return self._send(lessons_for("entry"))
        if p == "/api/session/me": return self._send(ME)
        if p == "/api/voice-status": return self._send({"ok": True, "eleven": False})
        if p.startswith("/api/"): return self._send({"ok": True})
        if p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(ln) if ln else b""
        p = self.path.split("?")[0]
        try: POSTS.append((p, json.loads(raw or b"{}")))
        except Exception: POSTS.append((p, {}))
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
  const pb = document.getElementById('pauseBtn'), st = document.getElementById('status');
  const bubbles = [...document.querySelectorAll('.bubble.student, .msg.student, [class*="student"]')]
                    .map(x => (x.textContent || '').trim()).filter(Boolean);
  const btns = [...document.querySelectorAll('.choicerow .choicebtn:not(.notsure)')].map(b => b.textContent.trim());
  return {
    paused: (typeof paused !== 'undefined') ? paused : null,
    busy: (typeof busy !== 'undefined') ? busy : null,
    pending: (typeof SCR !== 'undefined') ? SCR.pending : null,
    pauseLabel: pb ? pb.textContent.trim() : '',
    pauseOn: pb ? pb.classList.contains('on') : null,
    status: st ? st.textContent.trim() : '',
    bubbles: bubbles,
    btns: btns
  };
}"""

def open_lesson(pw):
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1400, "height": 900})
    pg.goto("http://127.0.0.1:%d/static/session.html?code=0000&course=entry" % PORT, wait_until="load")
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
    return b, pg

def press_pause(pg):
    pg.evaluate("() => document.getElementById('pauseBtn').click()")
    pg.wait_for_timeout(300)

with sync_playwright() as pw:
    print("\n--- THE TAP, WHILE PAUSED ---")
    b, pg = open_lesson(pw)
    s0 = pg.evaluate(STATE); print("   at the ask:", s0)
    check("the first ask is on stage with its three buttons and the page is not busy",
          s0["pending"] is True and s0["busy"] is False and s0["btns"] == ["12", "10", "14"], s0)
    press_pause(pg)
    s1 = pg.evaluate(STATE); print("   paused:", s1)
    check("the real Pause button pauses the page (flag, 'Resume' label, 'Paused' status)",
          s1["paused"] is True and s1["pauseOn"] is True and "Resume" in s1["pauseLabel"] and s1["status"] == "Paused", s1)
    n_posts = len(POSTS)
    pg.evaluate("""() => { const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
        const n=bs.find(x=>x.textContent.trim()==='12'); if (n) n.click(); }""")
    pg.wait_for_timeout(1200)
    s2 = pg.evaluate(STATE); print("   after the tap:", s2)
    sent = [p for p in POSTS[n_posts:] if p[0] == "/api/script/answer"]
    # the praise beat plays under the silent-mode pacer (speak is stubbed): press Next until the fresh ask
    for _ in range(14):
        if pg.evaluate("() => (typeof SCR!=='undefined' && SCR.pending)"): break
        pg.evaluate("""() => { const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
            const n=bs.find(x=>/Next/.test(x.textContent)); if (n) n.click(); }""")
        pg.wait_for_timeout(700)
    pg.wait_for_timeout(600)
    s2b = pg.evaluate(STATE); print("   at the fresh ask:", s2b)
    check("⭐ ① the tapped answer was SENT (one POST /api/script/answer carrying 12)",
          len(sent) == 1 and str(sent[0][1].get("said", sent[0][1].get("value", ""))) == "12", POSTS[n_posts:])
    check("⭐ ① ...and the student's bubble shows it", any(x == "12" for x in s2["bubbles"]), s2["bubbles"])
    check("⭐ ② the next beats arrived: the praise, then the fresh ask's buttons", s2b["btns"] == ["4", "5", "3"] and s2b["pending"] is True, s2b["btns"])
    check("⭐ ③ the pause was released by the answer: flag off, '⏸ Pause' label, no 'Paused' status",
          s2["paused"] is False and s2["pauseOn"] is False and "Pause" in s2["pauseLabel"] and "Resume" not in s2["pauseLabel"]
          and s2["status"] != "Paused", s2)
    # ---- ⑤ busy still gates: a tap while busy leaves the row on screen and sends nothing ----
    n_posts = len(POSTS)
    pg.evaluate("() => { busy = true; }")
    pg.evaluate("""() => { const bs=[...document.querySelectorAll('.choicerow .choicebtn')];
        const n=bs.find(x=>x.textContent.trim()==='4'); if (n) n.click(); }""")
    pg.wait_for_timeout(600)
    s3 = pg.evaluate(STATE)
    check("⑤ busy still gates: a tap while the page is busy sends nothing and leaves the buttons up",
          not [p for p in POSTS[n_posts:] if p[0] == "/api/script/answer"] and s3["btns"] == ["4", "5", "3"], (POSTS[n_posts:], s3["btns"]))
    pg.evaluate("() => { busy = false; }")
    b.close()

    print("\n--- THE TYPED BOX, WHILE PAUSED ---")
    b, pg = open_lesson(pw)
    press_pause(pg)
    n_posts = len(POSTS)
    pg.evaluate("""() => { const t=document.getElementById('typeToggle'); if (t) t.click();
        const i=document.getElementById('input'); i.value='12';
        if (typeof sendTyped==='function') sendTyped(); }""")
    pg.wait_for_timeout(2500)
    s4 = pg.evaluate(STATE); print("   after typing:", s4)
    sent = [p for p in POSTS[n_posts:] if p[0] == "/api/script/answer"]
    check("⭐ ④ a typed answer while paused is sent too, the bubble shows it, and the pause is released",
          len(sent) == 1 and any(x == "12" for x in s4["bubbles"]) and s4["paused"] is False and s4["status"] != "Paused", (sent, s4))
    b.close()

print("\n%d failure(s)" % len(F))
sys.exit(1 if F else 0)
# I did no harm and this file is not truncated.
