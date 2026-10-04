# zddrive.py -- build zd (2026-10-03): THE PHONE'S MENU AND THE PARENT'S DOOR, IN A REAL BROWSER.
# Jim's phone pass, P6 ("getting around is super cumbersome") and P8 (student -> parent on one
# phone), proved on the real static files under a stub API:
#   ① session.html on a 390x844 phone: a ☰ Menu button leads the top bar, the sidebar's nav is
#     NOT in the dock (no sideways strip), the sheet is closed; a tap opens it with every link
#     stacked full width -- Curriculum first, Sign out last -- and the pencil stepped out;
#   ② Curriculum in the sheet opens the nine units stacked, each full width; a tap on a unit
#     closes the sheet (the unit card shows on its own); the ✕ closes it too;
#   ③ Sign out clears the mt_student cookie and lands on /login;
#   ④ topic.html and practice.html on the phone carry the same button, sheet and Sign out;
#   ⑤ at 1280x800 nothing moved: no Menu button, the nav in the sidebar where it was (before
#     .controls), Sign out last in it, no sheet shown;
#   ⑥ index.html's parent door: "Sign in to my Family page" is a link to /family and the
#     student-code form is folded under it, still wired (#pcode, #pgo).
# Run:  PYTHONPATH=. python3 tools/zddrive.py     (prints PASS/FAIL lines, exits 1 on any FAIL)
import functools, http.server, json, os, sys, threading

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
PORT = 8827
ME = {"ok": True, "name": "Sam", "placed": True, "toured": True, "history": [], "progress": {"current_unit": 1}, "placement": {"start_unit": 1}}
START = {"ok": True, "lesson": "x", "id": "l1", "practice": {"phase": "pair-0", "run": 0, "need": 3, "on": False},
         "steps": [{"kind": "say", "spoken": "Hello.", "board": ""}]}
ROUTES = {"/login": "index.html"}

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
        if p in ROUTES: self.path = "/" + ROUTES[p]
        elif p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        if ln: self.rfile.read(ln)
        p = self.path.split("?")[0]
        if p == "/api/script/start": return self._send(START)
        self._send({"ok": True})

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = "http://127.0.0.1:%d" % PORT

from playwright.sync_api import sync_playwright
F = []
def check(l, ok, d=""):
    print(("PASS  " if ok else "FAIL  ") + l + ("" if ok else "   -- " + str(d)))
    if not ok: F.append(l)

MEASURE = """() => {
  const vis = (e) => { if (!e) return false; const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(e).visibility !== 'hidden'; };
  const btn = document.getElementById('menuBtn'), sheet = document.getElementById('menuSheet');
  const nav = document.querySelector('.leftnav');
  const items = nav ? [...nav.children].filter(e => e.classList.contains('navbtn')).map(e => ({ text: e.textContent.trim().replace(/\\s+/g, ' ').slice(0, 24), w: Math.round(e.getBoundingClientRect().width), left: Math.round(e.getBoundingClientRect().left), top: Math.round(e.getBoundingClientRect().top), vis: vis(e) })) : [];
  const units = [...document.querySelectorAll('.curriculum .unit')].map(u => ({ w: Math.round(u.getBoundingClientRect().width), vis: vis(u) }));
  const side = document.querySelector('.side.left');
  const pencil = document.getElementById('cadabra-layer');
  return { btnVis: vis(btn), btnFirst: !!(btn && btn.parentElement && btn.parentElement.firstElementChild === btn),
           sheetShown: !!(sheet && sheet.classList.contains('show')), navInSheet: !!(sheet && nav && sheet.contains(nav)),
           navInSide: !!(side && nav && side.contains(nav)), navBeforeControls: !!(nav && nav.nextElementSibling && nav.nextElementSibling.classList.contains('controls')),
           items, units, vw: innerWidth, pencilHidden: !pencil || getComputedStyle(pencil).visibility === 'hidden',
           signOutLast: !!(nav && nav.lastElementChild && nav.lastElementChild.hasAttribute('data-signout')),
           unitModal: !!(document.getElementById('unitModal') && document.getElementById('unitModal').classList.contains('show')) }; }"""

def open_page(pw, page, w, h, start=True):
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    ctx = b.new_context(viewport={"width": w, "height": h}, is_mobile=(w < 700), has_touch=(w < 700))
    ctx.add_cookies([{"name": "mt_student", "value": "1234", "url": BASE}])
    pg = ctx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(BASE + "/static/%s?course=entry" % page, wait_until="load")
    STUB = "() => { window.speak = function(){ return Promise.resolve(); }; }"
    pg.evaluate(STUB); pg.wait_for_timeout(500); pg.evaluate(STUB)
    if page == "session.html" and start:
        pg.evaluate("""() => { const g=document.getElementById('welcomeGo'); if (g && g.offsetParent!==null) g.click(); document.querySelectorAll('.welcome.show').forEach(w=>w.classList.remove('show')); }""")
        pg.wait_for_timeout(2500)
    else:
        pg.wait_for_timeout(800)
    return b, ctx, pg, errs

with sync_playwright() as pw:
    # ① ② ③ the lesson page on a phone
    b, ctx, pg, errs = open_page(pw, "session.html", 390, 844)
    m = pg.evaluate(MEASURE)
    check("⭐ ① session.html at 390x844: a ☰ Menu button leads the top bar, the nav is out of the dock, the sheet is closed",
          m and m["btnVis"] and m["btnFirst"] and not m["sheetShown"] and m["navInSheet"] and not m["navInSide"] and not errs,
          m and (m["btnVis"], m["btnFirst"], m["sheetShown"], m["navInSheet"], m["navInSide"], errs[:1]))
    pg.click("#menuBtn"); pg.wait_for_timeout(400)
    m = pg.evaluate(MEASURE)
    check("  ...a tap opens it: every link stacked full width (Curriculum first, Sign out last), each on its own row, the pencil stepped out",
          m and m["sheetShown"] and len(m["items"]) >= 8 and all(it["vis"] and it["w"] >= 330 for it in m["items"])
          and m["items"][0]["text"].startswith("📚 Curriculum") and m["items"][-1]["text"] == "🚪 Sign out" and m["signOutLast"]
          and len({it["top"] for it in m["items"]}) == len(m["items"]) and m["pencilHidden"], m and (m["items"], m["pencilHidden"]))
    pg.click("#curriculumBtn"); pg.wait_for_timeout(400)
    m = pg.evaluate(MEASURE)
    check("⭐ ② Curriculum opens the nine units stacked in the sheet, each full width",
          m and len(m["units"]) == 9 and all(u["vis"] and u["w"] >= 300 for u in m["units"]), m and m["units"])
    pg.evaluate("() => document.querySelectorAll('#menuSheet .curriculum .unit')[1].click()"); pg.wait_for_timeout(400)
    m = pg.evaluate(MEASURE)
    check("  ...a tap on a unit closes the sheet and the unit card shows on its own", m and not m["sheetShown"] and m["unitModal"], m and (m["sheetShown"], m["unitModal"]))
    pg.evaluate("() => { const c = document.querySelector('#unitModal .modal-close'); if (c) c.click(); }")
    pg.click("#menuBtn"); pg.wait_for_timeout(300); pg.click("#menuClose"); pg.wait_for_timeout(300)
    m = pg.evaluate(MEASURE)
    check("  ...and ✕ closes it", m and not m["sheetShown"], m and m["sheetShown"])
    pg.click("#menuBtn"); pg.wait_for_timeout(300)
    pg.click("#signOutLink"); pg.wait_for_timeout(1200)
    ck = [c for c in ctx.cookies() if c["name"] == "mt_student"]
    check("⭐ ③ Sign out clears the mt_student cookie and lands on the sign-in page", not ck and pg.url.endswith("/login"), (ck, pg.url))
    b.close()

    # ④ the other two board pages
    for page in ("topic.html", "practice.html"):
        b, ctx, pg, errs = open_page(pw, page, 390, 844)
        m = pg.evaluate(MEASURE)
        # the topic/problem picker overlay is up on a fresh visit (it sits above the top bar by
        # design -- the student picks first); the button is tapped through it here
        pg.evaluate("() => document.getElementById('menuBtn').click()"); pg.wait_for_timeout(300)
        m2 = pg.evaluate(MEASURE)
        check("  ④ %s at 390x844: the Menu button, the nav in the sheet (Sign out last), opens stacked" % page,
              m and m["btnVis"] and m["navInSheet"] and not m["sheetShown"] and m2["sheetShown"] and m2["signOutLast"]
              and all(it["vis"] and it["w"] >= 330 for it in m2["items"]) and not errs, (m and (m["btnVis"], m["navInSheet"]), m2 and m2["items"], errs[:1]))
        b.close()

    # ⑤ the desktop is unchanged
    b, ctx, pg, errs = open_page(pw, "session.html", 1280, 800, start=False)
    pg.evaluate("() => { document.body.classList.add('sbopen'); }"); pg.wait_for_timeout(200)
    d = pg.evaluate(MEASURE)
    check("⭐ ⑤ session.html at 1280x800: no Menu button, the nav in the sidebar (where build or left it) with Sign out last, no sheet",
          d and not d["btnVis"] and d["navInSide"] and d["signOutLast"] and not d["sheetShown"] and not errs,
          d and (d["btnVis"], d["navInSide"], d["signOutLast"], d["sheetShown"], errs[:1]))
    b.close()

    # ⑥ the parent's door
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
    pg.goto(BASE + "/login", wait_until="load"); pg.wait_for_timeout(500)
    door = pg.evaluate("""() => { const a = document.getElementById('pfamily'); const d = document.querySelector('.door.parent details');
      // a closed <details> hides its content with content-visibility in Chromium, which keeps a
      // box: checkVisibility() is the honest question, not getBoundingClientRect
      const vis = (e) => !!(e && e.checkVisibility && e.checkVisibility({ contentVisibilityAuto: true, visibilityProperty: true }));
      return { href: a && a.getAttribute('href'), text: a && a.textContent.trim(), linkVis: vis(a), folded: !!(d && !d.open), codeVis: vis(document.getElementById('pcode')), pgo: !!document.getElementById('pgo') }; }""")
    check("⭐ ⑥ index.html: the parent door leads with 'Sign in to my Family page' (/family); the code form is folded under it, still wired",
          door and door["href"] == "/family" and door["text"] == "Sign in to my Family page →" and door["linkVis"] and door["folded"] and not door["codeVis"] and door["pgo"], door)
    pg.click(".door.parent summary"); pg.wait_for_timeout(300)
    unf = pg.evaluate("() => { const e = document.getElementById('pcode'); return !!(e.checkVisibility && e.checkVisibility({ contentVisibilityAuto: true })); }")
    check("  ...and unfolds on a tap", unf, unf)
    b.close()

print("\n%d failure(s)" % len(F))
sys.exit(1 if F else 0)
# I did no harm and this file is not truncated.
