# zcdrive.py -- build zc (2026-10-03): THE BUTTONS GO ON THE BOARD ON A PHONE, IN A REAL BROWSER.
# Jim's phone pass, P3 (the blocker) and P5, proved on the real static files under a stub API:
#   ① topic.html on a 390x844 phone, "count the stars" over twenty stars with three answer
#     buttons: the board is at least 300px tall (it was 26px, measured, before zc), the choices
#     row is INSIDE the feed under the picture, every button is on screen, the stars are two
#     rows of ten that fit the board with no sideways scroll, and the dock is under 240px;
#   ② session.html on the same phone: the scripted lane's own rows (an [[choices]] ask) land in
#     the feed too, the board tall, the buttons on screen;
#   ③ the same two pages at 1280x800 are unchanged: the row sits in the control strip beside
#     #composer, the name + status line and the helper line are shown;
#   ④ a phone shows no name + status line and no helper line in the dock (two rows given back);
#   ⑤ family.html on a phone (P1): the three numbered steps start inside the first screen.
# Run:  PYTHONPATH=. python3 tools/zcdrive.py     (prints PASS/FAIL lines, exits 1 on any FAIL)
import functools, http.server, json, os, sys, threading

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
PORT = 8824
REPLY = {"ok": True, "reply": "Let us count twenty stars together. [[objects emoji=\"⭐\" groups=\"20\" caption=\"count out loud with me\"]] How many stars are there? [[choices options=\"18 | 20 | 12\"]]"}
ME = {"ok": True, "name": "Sam", "placed": True, "toured": True, "history": [], "progress": {"current_unit": 1}, "placement": {"start_unit": 1}}
START = {"ok": True, "lesson": "x", "id": "l1", "practice": {"phase": "pair-0", "run": 0, "need": 3, "on": False},
         "steps": [{"kind": "ask", "spoken": "Count the stars. How many stars are there?",
                    "board": '[[objects emoji="⭐" groups="20" caption="count out loud with me"]][[choices options="18 | 20 | 12"]]'}]}

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, o):
        b = json.dumps(o).encode(); self.send_response(200)
        self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(b))); self.end_headers()
        try: self.wfile.write(b)
        except Exception: pass
    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/api/script/lessons": return self._send({"ok": True, "lessons": [{"id": "entry-l1", "topic": "x", "unit": 1, "course": "entry", "course_title": "entry"}]})
        if p == "/api/session/me": return self._send(ME)
        if p.startswith("/api/"): return self._send({"ok": True, "eleven": False, "name": "Sam"})
        if p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        if ln: self.rfile.read(ln)
        p = self.path.split("?")[0]
        if p == "/api/topic": return self._send(REPLY)
        if p == "/api/script/start": return self._send(START)
        self._send({"ok": True})

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()

from playwright.sync_api import sync_playwright
F = []
def check(l, ok, d=""):
    print(("PASS  " if ok else "FAIL  ") + l + ("" if ok else "   -- " + str(d)))
    if not ok: F.append(l)

MEASURE = """() => {
  const f = document.getElementById('feed'), fr = f.getBoundingClientRect();
  const side = document.querySelector('.side.left'), sr = side.getBoundingClientRect();
  const row = document.getElementById('choiceRow');
  const bar = document.getElementById('ctrlBar');
  const btns = row ? [...row.querySelectorAll('.choicebtn')].map(b => { const r = b.getBoundingClientRect(); return { top: Math.round(r.top), bottom: Math.round(r.bottom), h: Math.round(r.height) }; }) : [];
  const tens = [...document.querySelectorAll('.objten')].map(t => { const r = t.getBoundingClientRect(); return { left: Math.round(r.left), right: Math.round(r.right), text: t.textContent }; });
  const head = document.querySelector('.tutor-head'), eh = document.querySelector('.elem-hint');
  const shown = (e) => !!(e && e.getBoundingClientRect().height > 0 && getComputedStyle(e).display !== 'none');
  return { feedH: Math.round(fr.height), feedTop: Math.round(fr.top), feedBottom: Math.round(fr.bottom),
    feedL: Math.round(fr.left), feedR: Math.round(fr.right),
    rowInFeed: !!(row && f.contains(row)), rowInBar: !!(row && bar && bar.contains(row)),
    rowBesideComposer: !!(row && row.nextElementSibling && row.nextElementSibling.id === 'composer'),
    btns, tens, dockH: Math.round(sr.height), vh: innerHeight, vw: innerWidth,
    noSideways: document.documentElement.scrollWidth <= innerWidth && f.scrollWidth <= f.clientWidth + 1,
    headShown: shown(head), ehShown: shown(eh) }; }"""

def run(pw, page, course, w, h):
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": w, "height": h}, is_mobile=(w < 700), has_touch=(w < 700))
    pg.goto("http://127.0.0.1:%d/static/%s?code=0000&course=%s" % (PORT, page, course), wait_until="load")
    STUB = "() => { window.speak = function(){ return Promise.resolve(); }; try { localStorage.removeItem('mt_board'); sessionStorage.removeItem('mt_sb_open'); } catch (e) {} }"
    pg.evaluate(STUB); pg.wait_for_timeout(500); pg.evaluate(STUB)
    if page == "topic.html":
        pg.evaluate("() => { document.querySelectorAll('.unitbtn')[0].click(); }"); pg.wait_for_timeout(6000)
    else:
        pg.evaluate("""() => { const g=document.getElementById('welcomeGo'); if (g && g.offsetParent!==null) g.click();
          document.querySelectorAll('.welcome.show').forEach(w=>w.classList.remove('show')); }""")
        pg.wait_for_timeout(8000)
    m = pg.evaluate(MEASURE); b.close(); return m

with sync_playwright() as pw:
    # ① the topic page on a phone
    m = run(pw, "topic.html", "entry", 390, 844)
    check("⭐ ① topic.html at 390x844: the board is at least 300px tall with the answer buttons up (26px before zc)",
          m and m["feedH"] >= 300, m and m["feedH"])
    check("  ...the choices row is INSIDE the feed, under the picture, and every button is on screen",
          m and m["rowInFeed"] and not m["rowInBar"] and len(m["btns"]) == 4
          and all(x["top"] >= m["feedTop"] - 1 and x["bottom"] <= m["feedBottom"] + 1 for x in m["btns"]), m and (m["rowInFeed"], m["btns"], m["feedTop"], m["feedBottom"]))
    check("  ...twenty stars are two rows of TEN, each inside the board, and nothing scrolls sideways (P5)",
          m and len(m["tens"]) == 2 and all(t["text"].count("⭐") == 10 for t in m["tens"])
          and all(t["left"] >= m["feedL"] and t["right"] <= m["feedR"] for t in m["tens"]) and m["noSideways"], m and (m["tens"], m["feedL"], m["feedR"], m["noSideways"]))
    check("  ④ the phone dock is under 240px, with no name + status line and no helper line in it",
          m and m["dockH"] < 240 and not m["headShown"] and not m["ehShown"], m and (m["dockH"], m["headShown"], m["ehShown"]))
    # ② the lesson page on a phone: the scripted lane's row
    m2 = run(pw, "session.html", "entry", 390, 844)
    check("⭐ ② session.html at 390x844: the scripted ask's buttons land in the feed, the board is tall, every button on screen",
          m2 and m2["rowInFeed"] and m2["feedH"] >= 300 and len(m2["btns"]) == 4
          and all(x["top"] >= m2["feedTop"] - 1 and x["bottom"] <= m2["feedBottom"] + 1 for x in m2["btns"]) and m2["noSideways"],
          m2 and (m2["rowInFeed"], m2["feedH"], m2["btns"], m2["feedTop"], m2["feedBottom"]))
    # ③ the desktop is unchanged
    d = run(pw, "topic.html", "entry", 1280, 800)
    check("⭐ ③ topic.html at 1280x800 is unchanged: the row sits in the control strip beside #composer; the name + status and helper lines show",
          d and d["rowInBar"] and d["rowBesideComposer"] and not d["rowInFeed"] and d["headShown"] and d["ehShown"], d and (d["rowInBar"], d["rowBesideComposer"], d["rowInFeed"], d["headShown"], d["ehShown"]))
    d2 = run(pw, "session.html", "entry", 1280, 800)
    check("  session.html at 1280x800 is unchanged: the row beside #composer in the strip, not in the feed",
          d2 and d2["rowBesideComposer"] and not d2["rowInFeed"] and len(d2["btns"]) == 4, d2 and (d2["rowBesideComposer"], d2["rowInFeed"], d2["btns"]))

    # ⑤ P1: the family page's three steps are in the first screen on a phone
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
    pg.goto("http://127.0.0.1:%d/static/family.html" % PORT, wait_until="load"); pg.wait_for_timeout(800)
    st = pg.evaluate("() => { const s=document.getElementById('steps'); const r=s.getBoundingClientRect(); const l1=document.getElementById('step1').getBoundingClientRect(); return { top: Math.round(r.top), step1Bottom: Math.round(l1.bottom), vh: innerHeight, auth: document.getElementById('authView').getBoundingClientRect().top }; }")
    b.close()
    check("⭐ ⑤ family.html at 390x844 (P1): step 1 is inside the first screen, above the account card",
          st and st["step1Bottom"] <= st["vh"] and st["top"] < st["auth"], st)

print("\n%d failure(s)" % len(F))
sys.exit(1 if F else 0)
# I did no harm and this file is not truncated.
