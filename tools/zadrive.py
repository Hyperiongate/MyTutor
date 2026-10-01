# zadrive.py -- build za (2026-09-30): THE TOPIC PAGE AND THE PARENT PAGES, IN A REAL BROWSER.
# Seven of Jim's first-family flags (F31, F32, F33, F1, F2, F3; F34 read and brought to Jim),
# each proved on the real static files under a stub API:
#   ① topic.html for Basic at 1280x800 is the lesson page's screen: the sidebar starts
#     collapsed behind the edge tab, the board takes the width, the name + controls sit in
#     the strip UNDER the board, and the answer buttons (72px, child mode) land there whole
#     -- every one inside the window; the tab opens and closes the sidebar (F31);
#   ② the same page on a 390x844 phone keeps dz's dock: no tab, the controls back in the
#     sidebar under the board, the buttons on screen (do no harm);
#   ③ practice.html for Basic has the same strip and the same buttons under the board;
#   ④ the symbol strip follows the course: + - x divide for Basic (and Entry), no theta for
#     Algebra I, the full eighteen for Geometry (F32);
#   ⑤ the feed is CREAM on Basic -- body.elem-mode is set and board-theme.css paints it --
#     so F33 is the remembered dark-board pick, not a missing skin (read and left);
#   ⑥ family.html says "Every student covered." and walks the three numbered steps from the
#     real state: signed out (1 here), signed in with no student (1 done, 2 here, the two
#     cards stacked in step order), with students (1 and 2 done, 3 here, two columns) (F2, F3);
#   ⑦ landing.html's hero holds four doors with "Start free -- create your account" second,
#     all of them in the first screen at 1280x800, and the FREE pricing card is the featured
#     one with the filled button (F1).
# Run:  PYTHONPATH=. python3 tools/zadrive.py     (prints PASS/FAIL lines, exits 1 on any FAIL)
import functools, http.server, json, os, sys, threading

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
PORT = 8818
REPLY = {"ok": True, "reply": "Division is sharing fairly. Twelve cookies for three friends is four each. "
         '[[objects emoji="🍪" groups="4" caption="four each"]] Have you worked with division before? '
         '[[choices options="I have seen it | Start from the beginning"]]'}
FAMILY = {"state": "out"}   # "out" | "empty" | "kids" -- what /api/parent/me answers

def family_me():
    base = {"ok": True, "parent": {"email": "pat@example.com", "name": "Pat"},
            "subscription": {"status": "none"}, "billing_ready": False, "students": []}
    if FAMILY["state"] == "kids":
        base["students"] = [{"name": "Ana", "code": "MAPLE42", "covered": False}]
    return base

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, o, status=200):
        b = json.dumps(o).encode(); self.send_response(status)
        self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(b))); self.end_headers()
        try: self.wfile.write(b)
        except Exception: pass
    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/api/parent/me":
            if FAMILY["state"] == "out": return self._send({"detail": "no"}, 401)
            return self._send(family_me())
        if p == "/api/parent/overview": return self._send({"ok": True, "students": []})
        if p.startswith("/api/"): return self._send({"ok": True, "eleven": False, "name": "Sam"})
        if p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        if ln: self.rfile.read(ln)
        p = self.path.split("?")[0]
        if p in ("/api/topic", "/api/practice"): return self._send(REPLY)
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
  const tab = document.getElementById('sbTab');
  const bar = document.getElementById('ctrlBar');
  const ctr = document.querySelector('.controls');
  const row = document.getElementById('choiceRow');
  const btns = row ? [...row.querySelectorAll('.choicebtn')].map(b => { const r = b.getBoundingClientRect();
    return { top: Math.round(r.top), bottom: Math.round(r.bottom), h: Math.round(r.height), text: b.textContent }; }) : [];
  return {
    feed: { left: Math.round(fr.left), width: Math.round(fr.width), bottom: Math.round(fr.bottom) },
    feedBg: getComputedStyle(f).backgroundColor, elem: document.body.classList.contains('elem-mode'),
    sideW: Math.round(sr.width), sideShown: !!(side.offsetParent), sbopen: document.body.classList.contains('sbopen'),
    tabShown: !!(tab && tab.getBoundingClientRect().width > 0),   /* position:fixed has no offsetParent */
    tabText: tab ? tab.textContent : '',
    ctrlInBar: !!(ctr && bar && ctr.parentElement === bar),
    ctrlInSide: !!(ctr && ctr.parentElement === side),
    rowInBar: !!(row && bar && bar.contains(row)),
    rowTop: row ? Math.round(row.getBoundingClientRect().top) : -1,
    btns, keys: [...document.querySelectorAll('.feedbar .mkkey')].map(k => k.textContent),
    vh: window.innerHeight, vw: window.innerWidth,
    course: document.body.getAttribute('data-course') };
}"""

def open_board(pw, page, course, width, height, start=True):
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": width, "height": height})
    pg.goto("http://127.0.0.1:%d/static/%s?code=0000&course=%s" % (PORT, page, course), wait_until="load")
    STUB = "() => { window.speak = function(){ return Promise.resolve(); }; try { localStorage.removeItem('mt_board'); sessionStorage.removeItem('mt_sb_open'); } catch (e) {} }"
    pg.evaluate(STUB); pg.wait_for_timeout(400)
    if start:
        if page == "topic.html":
            pg.evaluate("() => { document.querySelectorAll('.unitbtn')[0].click(); }")
        else:
            pg.evaluate("() => { const t = document.getElementById('problemInput'); t.value = '12 ÷ 3'; t.dispatchEvent(new Event('input', {bubbles:true})); document.getElementById('entryGo').click(); }")
        pg.wait_for_timeout(4500)
    return b, pg

with sync_playwright() as pw:
    # ① the topic page for Basic, on a laptop
    b, pg = open_board(pw, "topic.html", "basic", 1280, 800)
    m = pg.evaluate(MEASURE)
    check("⭐ ① topic.html at 1280x800: the sidebar starts collapsed behind the edge tab and the board takes the width",
          m and not m["sideShown"] and not m["sbopen"] and m["tabShown"] and "Open the sidebar" in m["tabText"]
          and m["feed"]["left"] < 40 and m["feed"]["width"] >= 1100, m and {k: m[k] for k in ("sideShown", "sbopen", "tabShown", "tabText", "feed")})
    check("  ...the name + controls live in the strip UNDER the board, and the answer buttons land there",
          m and m["ctrlInBar"] and m["rowInBar"] and m["rowTop"] > m["feed"]["bottom"], m and {k: m[k] for k in ("ctrlInBar", "rowInBar", "rowTop", "feed")})
    check("  ...every button whole, inside the window, at child size (72px) -- not cut off in a 308px column",
          m and len(m["btns"]) >= 3 and all(x["top"] >= 0 and x["bottom"] <= m["vh"] and x["h"] >= 72 for x in m["btns"]), m and m["btns"])
    pg.evaluate("() => document.getElementById('sbTab').click()"); pg.wait_for_timeout(300)
    m2 = pg.evaluate(MEASURE)
    check("  ...the tab opens the sidebar (308px, the links) and reads Close; a second tap closes it again",
          m2 and m2["sbopen"] and m2["sideShown"] and m2["sideW"] == 308 and "Close the sidebar" in m2["tabText"]
          and m2["ctrlInBar"], m2 and {k: m2[k] for k in ("sbopen", "sideShown", "sideW", "tabText")})
    pg.evaluate("() => document.getElementById('sbTab').click()"); pg.wait_for_timeout(300)
    m3 = pg.evaluate(MEASURE)
    check("  ...closed again", m3 and not m3["sbopen"] and not m3["sideShown"], m3 and m3["sbopen"])
    # ④ the strip, ⑤ the cream
    check("⭐ ④ the symbol strip on Basic is + − × ÷ and nothing else (data-course=basic)",
          m and m["keys"] == ["+", "−", "×", "÷"] and m["course"] == "basic", m and m["keys"])
    check("⭐ ⑤ the feed is CREAM on Basic (body.elem-mode set, board-theme's warm board) -- F33 is the remembered dark-board pick, not a missing skin",
          m and m["elem"] and m["feedBg"] == "rgb(255, 248, 232)", m and (m["elem"], m["feedBg"]))
    b.close()

    # ② the same page on a phone: dz's dock, untouched
    b, pg = open_board(pw, "topic.html", "basic", 390, 844)
    m = pg.evaluate(MEASURE)
    check("⭐ ② topic.html at 390x844 keeps the phone dock: no tab, the controls back in the sidebar under the board, the buttons on screen",
          m and not m["tabShown"] and m["ctrlInSide"] and not m["ctrlInBar"] and m["sideShown"]
          and len(m["btns"]) >= 3 and all(x["top"] >= 0 and x["bottom"] <= m["vh"] for x in m["btns"]),
          m and {k: m[k] for k in ("tabShown", "ctrlInSide", "ctrlInBar", "sideShown", "btns", "vh")})
    b.close()

    # ③ practice.html, the twin
    b, pg = open_board(pw, "practice.html", "basic", 1280, 800)
    m = pg.evaluate(MEASURE)
    check("⭐ ③ practice.html at 1280x800: the same collapsed sidebar, the strip under the board, the buttons there whole, the four-key strip",
          m and not m["sideShown"] and m["tabShown"] and m["feed"]["width"] >= 1100 and m["ctrlInBar"] and m["rowInBar"]
          and m["rowTop"] > m["feed"]["bottom"] and len(m["btns"]) >= 3
          and all(x["top"] >= 0 and x["bottom"] <= m["vh"] and x["h"] >= 72 for x in m["btns"]) and m["keys"] == ["+", "−", "×", "÷"],
          m and {k: m[k] for k in ("sideShown", "tabShown", "feed", "ctrlInBar", "rowInBar", "rowTop", "btns", "keys")})
    b.close()

    # ④ the other tiers (the same page, other courses; the strip is built from data-course)
    b, pg = open_board(pw, "topic.html", "algebra1", 1280, 800, start=False)
    k1 = pg.evaluate("() => [...document.querySelectorAll('.feedbar .mkkey')].map(k => k.textContent)")
    b.close()
    b, pg = open_board(pw, "topic.html", "geometry", 1280, 800, start=False)
    k2 = pg.evaluate("() => [...document.querySelectorAll('.feedbar .mkkey')].map(k => k.textContent)")
    b.close()
    check("  ④ Algebra I gets the strip without theta (17 keys); Geometry the full eighteen, in the original order",
          len(k1) == 17 and "θ" not in k1 and "π" in k1 and "|x|" in k1 and len(k2) == 18 and k2[:4] == ["÷", "×", "−", "+"] and "θ" in k2,
          (k1, k2))

    # ⑥ the family page in its three states
    def family(state):
        FAMILY["state"] = state
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": 1280, "height": 900})
        pg.goto("http://127.0.0.1:%d/static/family.html" % PORT, wait_until="load")
        pg.evaluate("() => { try { localStorage.setItem('mt_parent_token', '%s'); } catch (e) {} }" % ("" if state == "out" else "tok"))
        pg.reload(wait_until="load"); pg.wait_for_timeout(900)
        r = pg.evaluate("""() => {
          const st = [1,2,3].map(i => { const li = document.getElementById('step' + i); return li.className + ':' + li.querySelector('.st').textContent; });
          const grid = document.getElementById('famGrid');
          const cards = [...grid.querySelectorAll(':scope > .card')].map(c => { const r = c.getBoundingClientRect(); return { top: Math.round(r.top), left: Math.round(r.left), h2: c.querySelector('h2').textContent.trim() }; });
          return { h1: document.querySelector('h1').textContent, steps: st, first: grid.classList.contains('firstvisit'),
                   auth: document.getElementById('authView').style.display !== 'none', fam: document.getElementById('famView').style.display !== 'none',
                   cards, kidsNote: (document.getElementById('kids').textContent || '').trim().slice(0, 60) }; }""")
        b.close(); return r
    out = family("out")
    check("⭐ ⑥ family.html says 'One account. Every student covered.' (F2)", out and out["h1"] == "One account. Every student covered.", out and out["h1"])
    check("  signed out: step 1 is where they are, 2 and 3 next; the account card shows",
          out and out["steps"] == ["now:You are here", "next:Next", "next:Next"] and out["auth"] and not out["fam"], out and out["steps"])
    emp = family("empty")
    check("⭐ signed in with no student (the first visit): 1 done, 2 here, 3 next -- and the two cards STACK in step order, students first",
          emp and emp["steps"] == ["done:Done", "now:You are here", "next:Next"] and emp["first"] and emp["fam"]
          and len(emp["cards"]) == 2 and emp["cards"][0]["h2"].startswith("2") and emp["cards"][1]["h2"].startswith("3")
          and emp["cards"][1]["top"] > emp["cards"][0]["top"] and emp["cards"][1]["left"] == emp["cards"][0]["left"]
          and emp["kidsNote"].startswith("You’re on step 2"), emp)
    kids = family("kids")
    check("  with a student added: 1 and 2 done, 3 here; the family keeps its two-column view",
          kids and kids["steps"] == ["done:Done", "done:Done", "now:You are here"] and not kids["first"]
          and len(kids["cards"]) == 2 and kids["cards"][1]["left"] > kids["cards"][0]["left"], kids)

    # ⑦ the front page's first screen
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1280, "height": 800})
    pg.goto("http://127.0.0.1:%d/static/landing.html" % PORT, wait_until="load"); pg.wait_for_timeout(500)
    land = pg.evaluate("""() => {
      const doors = [...document.querySelectorAll('.doors a')].map(a => { const r = a.getBoundingClientRect(); return { text: a.textContent.trim(), href: a.getAttribute('href'), bottom: Math.round(r.bottom), cls: a.className }; });
      const plans = [...document.querySelectorAll('#pricing .plan')].map(p => ({ feat: p.classList.contains('feat'), h3: p.querySelector('h3').textContent.trim(), btn: (p.querySelector('.btn') || {}).className, tag: (p.querySelector('.tag') || {}).textContent }));
      return { doors, plans, vh: window.innerHeight }; }""")
    b.close()
    check("⭐ ⑦ the front page: four doors in the hero, 'Start free — create your account' second, every one inside the first screen (F1)",
          land and [d["text"] for d in land["doors"]] == ["▶ Try a lesson", "Start free — create your account", "Take the tour", "Sign in"]
          and land["doors"][1]["href"] == "/family" and all(d["bottom"] <= land["vh"] for d in land["doors"]), land and land["doors"])
    check("  ...and the FREE pricing card is the featured one with the filled button; Full access is the plain card",
          land and len(land["plans"]) == 2 and land["plans"][0]["feat"] and land["plans"][0]["h3"] == "Free" and "btn-primary" in land["plans"][0]["btn"]
          and land["plans"][0]["tag"] == "Start here — free" and not land["plans"][1]["feat"] and "btn-ghost" in land["plans"][1]["btn"], land and land["plans"])

print("\n%d failure(s)" % len(F))
sys.exit(1 if F else 0)
# I did no harm and this file is not truncated.
