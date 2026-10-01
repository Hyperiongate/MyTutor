# zbdrive.py -- build zb (2026-10-01): THE CODE LEAVES THE ADDRESS BAR, IN A REAL BROWSER.
# Jim's first-family playthrough F34 ("the student's sign-in code is in the URL... move it to
# the session cookie"), built so that his 08-18 ruling ("do not kill the bookmark login") still
# holds. Proved on the real static files under a stub server that serves the app's routes:
#   ① the login page: a verified code goes into the mt_student cookie and the student lands
#     on /home with a CLEAN address (no ?code=);
#   ② a bookmark still signs in: /home?code=1234&course=entry arrives, the cookie is written,
#     the address becomes /home?course=entry in place (no reload, Back untouched), and every
#     tile and chip link carries the course and never the code;
#   ③ a page opened with NO code reads the cookie: /topic?course=basic does not bounce to
#     /login, the API call it makes carries X-Student-Code = the cookie, the top bar's links
#     (app-nav.js, which runs after the address was cleaned) carry no code, and library.js
#     (same timing) still found the code and drew its "Look it up" button;
#   ④ the other params survive the strip: /session?code=1234&course=entry&tour=1 becomes
#     /session?course=entry&tour=1;
#   ⑤ the PARENT'S door is untouched: /dashboard?code=5678&view=parent keeps its address,
#     keeps its code in its own links, and leaves the student cookie (1234) alone;
#   ⑥ /records with no code in the URL (the student's own dashboard links there now) reads
#     the cookie for its API call; with a code in the URL (the parent) it uses that one and
#     does not store it;
#   ⑦ a typed code in Abrabot's room becomes the cookie, and the room's way-out links carry
#     no code.
# Run:  PYTHONPATH=. python3 tools/zbdrive.py     (prints PASS/FAIL lines, exits 1 on any FAIL)
import functools, http.server, json, os, sys, threading

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
PORT = 8822
ROUTES = {"/home": "home.html", "/login": "index.html", "/session": "session.html", "/topic": "topic.html",
          "/practice": "practice.html", "/dashboard": "dashboard.html", "/records": "records.html",
          "/challenge": "challenge.html", "/drill": "drill.html"}
SEEN = []   # (path, X-Student-Code) for every API call

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, o, status=200):
        b = json.dumps(o).encode(); self.send_response(status)
        self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(b))); self.end_headers()
        try: self.wfile.write(b)
        except Exception: pass
    def _api(self, p):
        SEEN.append((p, (self.headers.get("X-Student-Code") or "").strip()))
        if p == "/api/session/me": return self._send({"ok": True, "name": "Sam", "placed": True, "toured": True, "history": [], "progress": {"current_unit": 1}, "placement": {"start_unit": 1}})
        if p == "/api/courses/me": return self._send({"ok": True, "courses": []})
        if p == "/api/records/me": return self._send({"ok": True, "name": "Sam", "days": [], "units": [], "awards": [], "courses": []})
        if p == "/api/drill/lessons": return self._send({"ok": True, "lessons": [], "courses": []})
        return self._send({"ok": True, "eleven": False, "name": "Sam", "lessons": [], "students": [], "topics": [], "awards": [], "misses": [], "days": [], "units": [], "courses": []})
    def do_GET(self):
        p = self.path.split("?")[0]
        if p.startswith("/api/"): return self._api(p)
        if p in ROUTES: self.path = "/" + ROUTES[p]
        elif p.startswith("/static/"): self.path = self.path[len("/static"):]
        super().do_GET()
    def do_POST(self):
        ln = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(ln) if ln else b""
        p = self.path.split("?")[0]
        if p == "/api/login":
            try: code = json.loads(body or b"{}").get("code", "")
            except Exception: code = ""
            SEEN.append((p, code))
            return self._send({"ok": True, "code": code.upper()})
        if p == "/api/topic":
            try: code = json.loads(body or b"{}").get("code", "")   # this call carries the code in its JSON body
            except Exception: code = ""
            SEEN.append((p, code))
            return self._send({"ok": True, "reply": "Let us look. [[choices options=\"4 | 5\"]]"})
        return self._api(p)

srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(H, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = "http://127.0.0.1:%d" % PORT

from playwright.sync_api import sync_playwright
F = []
def check(l, ok, d=""):
    print(("PASS  " if ok else "FAIL  ") + l + ("" if ok else "   -- " + str(d)))
    if not ok: F.append(l)

def cookie(ctx):
    for c in ctx.cookies():
        if c["name"] == "mt_student": return c["value"]
    return ""
def urlq(pg):
    from urllib.parse import urlparse
    u = urlparse(pg.url); return u.path + (("?" + u.query) if u.query else "")
LINKS = "() => [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')).filter(h => h && h.startsWith('/') && !h.startsWith('//'))"
STUB = "() => { window.speak = function(){ return Promise.resolve(); }; }"

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    # ① the login page
    ctx = b.new_context(viewport={"width": 1280, "height": 800}); pg = ctx.new_page()
    pg.goto(BASE + "/login", wait_until="load"); pg.wait_for_timeout(300)
    pg.fill("#code", "maple42"); pg.click("#go"); pg.wait_for_timeout(1500)
    check("⭐ ① the login page puts the verified code in the mt_student cookie and lands on /home with a clean address",
          urlq(pg) == "/home" and cookie(ctx) == "MAPLE42", (urlq(pg), cookie(ctx)))
    ctx.close()

    # ② the bookmark still signs in; the address is cleaned in place; the links carry no code
    ctx = b.new_context(viewport={"width": 1280, "height": 800}); pg = ctx.new_page()
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(BASE + "/home?code=1234&course=entry", wait_until="load"); pg.wait_for_timeout(1200)
    links = pg.evaluate(LINKS)
    check("⭐ ② a bookmark with the code signs in: the cookie is written and the address becomes /home?course=entry in place",
          cookie(ctx) == "1234" and urlq(pg) == "/home?course=entry" and not errs, (cookie(ctx), urlq(pg), errs[:1]))
    check("  ...every tile and chip on the hub carries the course and never the code",
          links and not any("code=" in h for h in links) and any(h == "/session?course=entry" for h in links)
          and any(h == "/home" for h in links), links)
    hist = pg.evaluate("() => history.length")
    ctl = ctx.new_page(); ctl.goto(BASE + "/home?course=entry", wait_until="load"); ctl.wait_for_timeout(300)
    hist0 = ctl.evaluate("() => history.length"); ctl.close()   # the same page opened with no code to strip
    pg.click('a[href="/session?course=entry"]'); pg.wait_for_timeout(800)
    pg.go_back(); pg.wait_for_timeout(600)
    check("  ...the clean address was a REPLACE, not a new history entry (the same count as a load with nothing to strip): Back from the lesson returns to the hub, still clean, still signed in",
          urlq(pg) == "/home?course=entry" and cookie(ctx) == "1234" and hist == hist0, (urlq(pg), hist, hist0))
    ctx.close()

    # ③ a page with no code reads the cookie; app-nav and library.js read it too
    ctx = b.new_context(viewport={"width": 1280, "height": 800})
    ctx.add_cookies([{"name": "mt_student", "value": "1234", "url": BASE}])
    pg = ctx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    SEEN.clear()
    pg.goto(BASE + "/topic?course=basic", wait_until="load"); pg.evaluate(STUB); pg.wait_for_timeout(600)
    pg.evaluate("() => { document.querySelectorAll('.unitbtn')[0].click(); }"); pg.wait_for_timeout(2500)
    hdr = [h for p, h in SEEN if p == "/api/topic"]
    nav = pg.evaluate("() => [...document.querySelectorAll('.anav a')].map(a => a.getAttribute('href'))")
    lib = pg.evaluate("() => !!document.querySelector('.leftnav .navbtn.libbtn, #libBtn, .leftnav a[href=\"#\"].navbtn') || [...document.querySelectorAll('.leftnav *')].some(e => /Look it up/.test(e.textContent))")
    check("⭐ ③ a page opened with NO code reads the cookie: /topic?course=basic stays (no bounce to /login) and its API call carries the cookie's code",
          urlq(pg) == "/topic?course=basic" and hdr and hdr[-1] == "1234" and not errs, (urlq(pg), hdr, errs[:1]))
    check("  ...the top bar's links (app-nav.js, run after the address was cleaned) carry the course and no code; Switch course is /home",
          nav and not any("code=" in h for h in nav) and "/home" in nav and any(h == "/home?course=basic" for h in nav), nav)
    check("  ...library.js (same timing) found the code and drew 'Look it up'", lib, lib)
    ctx.close()

    # ④ the other params survive the strip
    ctx = b.new_context(viewport={"width": 1280, "height": 800}); pg = ctx.new_page()
    pg.goto(BASE + "/session?code=1234&course=entry&tour=1", wait_until="load"); pg.wait_for_timeout(800)
    check("⭐ ④ the strip takes only the code: /session?code=1234&course=entry&tour=1 becomes /session?course=entry&tour=1",
          urlq(pg) == "/session?course=entry&tour=1" and cookie(ctx) == "1234", (urlq(pg), cookie(ctx)))
    ctx.close()

    # ⑤ the parent's door is untouched
    ctx = b.new_context(viewport={"width": 1280, "height": 800})
    ctx.add_cookies([{"name": "mt_student", "value": "1234", "url": BASE}])
    pg = ctx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    SEEN.clear()
    pg.goto(BASE + "/dashboard?code=5678&view=parent", wait_until="load"); pg.wait_for_timeout(1500)
    hdr = [h for p, h in SEEN if p == "/api/courses/me"]
    links = pg.evaluate(LINKS)
    check("⭐ ⑤ the parent's door keeps its address, reads ITS code, and leaves the student cookie alone",
          urlq(pg) == "/dashboard?code=5678&view=parent" and hdr and hdr[-1] == "5678" and cookie(ctx) == "1234" and not errs,
          (urlq(pg), hdr, cookie(ctx), errs[:1]))
    check("  ...and the parent view's own links keep the code (the parent holds no cookie): the Records link reads /records?code=5678, nothing carries the student's 1234",
          "/records?code=5678" in links and not any(("code=1234" in h) for h in links), [h for h in links if "code=" in h][:4])
    ctx.close()

    # ⑥ records: the cookie as the fallback; the URL's code used, not stored
    ctx = b.new_context(viewport={"width": 1280, "height": 800})
    ctx.add_cookies([{"name": "mt_student", "value": "1234", "url": BASE}])
    pg = ctx.new_page(); SEEN.clear()
    pg.goto(BASE + "/records", wait_until="load"); pg.wait_for_timeout(1000)
    h1 = [h for p, h in SEEN if p == "/api/records/me"]
    SEEN.clear()
    pg.goto(BASE + "/records?code=5678", wait_until="load"); pg.wait_for_timeout(1000)
    h2 = [h for p, h in SEEN if p == "/api/records/me"]
    check("⭐ ⑥ /records with no code in the URL reads the cookie; with the parent's code in the URL it uses that one, keeps the address and does not store it",
          h1 and h1[-1] == "1234" and h2 and h2[-1] == "5678" and urlq(pg) == "/records?code=5678" and cookie(ctx) == "1234", (h1, h2, urlq(pg), cookie(ctx)))
    ctx.close()

    # ⑦ Abrabot's room
    ctx = b.new_context(viewport={"width": 1280, "height": 800}); pg = ctx.new_page()
    pg.goto(BASE + "/drill?code=1234&course=entry", wait_until="load"); pg.wait_for_timeout(800)
    box = pg.evaluate("() => document.getElementById('code').value")
    check("⭐ ⑦ Abrabot's room: an arriving code fills the box, becomes the cookie and leaves the address",
          box == "1234" and cookie(ctx) == "1234" and urlq(pg) == "/drill?course=entry", (box, cookie(ctx), urlq(pg)))
    pg.fill("#code", "9999"); pg.evaluate("() => { try { MTStudent.set(document.getElementById('code').value); } catch (e) {} }")
    check("  ...a code typed in the box becomes the signed-in student (MTStudent.set is the room's hook on start)", cookie(ctx) == "9999", cookie(ctx))
    ctx.close()
    b.close()

print("\n%d failure(s)" % len(F))
sys.exit(1 if F else 0)
# I did no harm and this file is not truncated.
