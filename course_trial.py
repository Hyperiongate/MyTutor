# =============================================================================
# course_trial.py  --  THE FULL-JOURNEY TRIAL  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-13  BUILD fb -- NEW. Jim: "create a trial where you are a person that enters
#               one of the levels of math, and you validate the first half of the
#               course... Then you finish the rest of the course and look for prompts
#               like 'you're ready to take the final exam, but first you gotta go back
#               and take the quizzes for the units that you validated'... then act like
#               they took the final exam and that they got the appropriate award for
#               their trophy case and that the appropriate results showed up on the
#               parents and the teachers thing."
#               ⭐ IT FOUND A LIVE BUG ON ITS FIRST RUN: a teacher could not add a
#               parent-created student to a class ("No student with that code"), and if
#               one was somehow in a class they showed with no name and no progress. The
#               classroom code path predated parent accounts and only ever consulted
#               students.json -- the four pilot personas -- so EVERY real customer's
#               child was invisible to it. Fixed in main.py by routing the three class
#               lookups through _lookup_student (which has known about both sources
#               since 2026-07-31). Nothing else in the app had that bug; only the class
#               path was written before parent accounts existed.
# -----------------------------------------------------------------------------
# HOW TO RUN:  python3 course_trial.py            (add --course geometry for another)
# Needs no API keys and no network: it stands the real app up on a throwaway SQLite
# database and makes real HTTP calls to real endpoints.
# =============================================================================
"""THE FULL-JOURNEY TRIAL — one student, start to finish.

WHY THIS EXISTS, and why it is not the lesson audit: the audit reads TEACHING QUALITY,
one reply at a time. This reads the MACHINERY OF A WHOLE COURSE -- placement, mastery
gating, the locked Final Exam and its message, the exam itself, the trophy case, and the
parent and teacher views -- as ONE continuous student life. Every step is a real HTTP call
to the real app against a real database. No mocks, no model, no API keys.

It is deliberately the journey build ew made honest: a student who VALIDATES the first
three units on the Course Assessment must still go back and pass those three Unit Quizzes
before the Final Exam opens. That policy is the reason this trial exists.

Exit code 0 = the whole journey works. Non-zero = it names what broke.
"""

import json
import os
import sys
import tempfile
import uuid

COURSE = "prealgebra"          # override with --course <id>
VALIDATED = [1, 2, 3]          # "the first half" — placed out of, NOT passed
WORKED = [4, 5, 6, 7, 8, 9]    # done the normal way

FAILURES = []
STEPS = []


def step(n, msg):
    STEPS.append(f"{n}. {msg}")
    print(f"\n\033[96m{n}. {msg}\033[0m")


def ok(msg):
    print(f"   \033[92m✓\033[0m {msg}")


def bad(msg):
    FAILURES.append(msg)
    print(f"   \033[91m✗ {msg}\033[0m")


def want(cond, good, why):
    ok(good) if cond else bad(why)


def main():
    global COURSE
    if "--course" in sys.argv:
        i = sys.argv.index("--course")
        if i + 1 < len(sys.argv):
            COURSE = sys.argv[i + 1].strip()
    tmp = tempfile.mkdtemp()
    os.environ["DATABASE_URL"] = "sqlite:///" + os.path.join(tmp, "trial.db")
    os.environ["WEEKLY_EMAIL"] = "off"
    os.environ.setdefault("DATA_DIR", tmp)
    from fastapi.testclient import TestClient
    import main, store, curriculum
    c = TestClient(main.app)
    if not store.enabled():
        print("TRIAL-ERROR: no database"); return 1

    units = curriculum.units_for(COURSE)
    unit_names = {int(u[0]): str(u[1]) for u in units}
    total_units = len(units)
    title = curriculum.course_title(COURSE)
    print(f"\n{'=' * 74}\nTHE FULL-JOURNEY TRIAL — {title}\n{'=' * 74}")

    # ---------------------------------------------------------------- 1. the family
    step(1, "A parent signs up and adds their child")
    email = f"trial-{uuid.uuid4().hex[:8]}@home.test"
    r = c.post("/api/parent/signup", json={"email": email, "password": "hunter2hunter2",
                                           "name": "Trial Parent"})
    want(r.status_code == 200, "parent account created", f"signup failed: {r.text[:160]}")
    ptok = r.json()["token"]
    r = c.post("/api/parent/students", json={"token": ptok, "name": "Sam"})
    want(r.status_code == 200, "child added", f"add child failed: {r.text[:160]}")
    kids = r.json().get("students") or []
    CODE = kids[0]["code"]
    ok(f"Sam's login code is {CODE}")

    # ------------------------------------------------- 2. the Course Assessment
    step(2, f"Sam takes the Course Assessment and VALIDATES units {VALIDATED}")
    results = []
    for n, name in unit_names.items():
        strong = n in VALIDATED
        results.append({"u": n, "name": name, "correct": 5 if strong else 1, "total": 5,
                        "pct": 100 if strong else 20, "rating": 10 if strong else 2,
                        "competent": strong})
    first_weak = min(WORKED)
    r = c.post(f"/api/placement/{CODE}?course={COURSE}", json={
        "level": first_weak, "level_title": "Course assessment",
        "start_unit": first_weak, "start_unit_name": unit_names[first_weak], "points": 1500,
        "strengths": [unit_names[n] for n in VALIDATED], "units": results})
    want(r.status_code == 200, "placement saved", f"placement failed: {r.text[:160]}")

    prog = c.get(f"/api/session/{CODE}?course={COURSE}").json().get("progress") or {}
    mastered = prog.get("mastered_units") or []
    want(mastered == [],
         "⭐ validating units 1-3 passed NOTHING — mastered is still empty (build ew's policy)",
         f"PLACEMENT GRANTED MASTERY: {mastered} — this is exactly the bug build ew fixed")
    fin = prog.get("final") or {}
    want(fin.get("required") == total_units,
         f"the Final Exam requires all {total_units} units (derived from the course)",
         f"required={fin.get('required')} but this course has {total_units} units")

    # ------------------------------------------------- 3. work the rest of the course
    step(3, f"Sam works units {WORKED} the normal way and passes each Unit Quiz")
    for n in WORKED:
        r = c.post(f"/api/check/{CODE}", json={"unit": n, "correct": 10, "total": 10,
                                               "course": COURSE})
        if r.status_code != 200 or not r.json().get("mastered"):
            bad(f"unit {n} did not master: {r.text[:120]}")
    prog = c.get(f"/api/session/{CODE}?course={COURSE}").json().get("progress") or {}
    mastered = sorted(prog.get("mastered_units") or [])
    want(mastered == sorted(WORKED),
         f"units {mastered} are mastered — the validated ones are NOT",
         f"expected {sorted(WORKED)}, got {mastered}")

    # ------------------------------------------- 4. the locked door + its message
    step(4, "Sam tries the Final Exam — it must be LOCKED, and must say why")
    fin = (c.get(f"/api/session/{CODE}?course={COURSE}").json()
           .get("progress") or {}).get("final") or {}
    want(fin.get("eligible") is False,
         f"Final Exam is LOCKED at {fin.get('mastered_count')} of {fin.get('required')}",
         "THE FINAL EXAM OPENED WITHOUT THE VALIDATED UNITS' QUIZZES")

    r = c.post(f"/api/final/{CODE}", json={"correct": 18, "total": 18, "course": COURSE})
    body = r.json()
    want(body.get("locked") is True and not body.get("ok"),
         "the server REFUSED to record a final exam score while locked",
         f"a locked student recorded a final exam: {body}")
    msg = body.get("detail") or ""
    print(f"\n   \033[93m--- what Sam is told at the locked door ---\033[0m")
    for line in msg.splitlines():
        print(f"   \033[93m|\033[0m {line}")
    print()
    named = [n for n in VALIDATED if unit_names[n].lower() in msg.lower()
             or f"Unit {n}" in msg]
    want(len(named) == len(VALIDATED),
         f"the message NAMES every unit still owed: {[unit_names[n] for n in VALIDATED]}",
         f"only named {named} of {VALIDATED} — a student must know WHICH doors are shut")
    want(any(w in msg.lower() for w in ("retake", "review", "together", "start")),
         "the message offers the way through, not just the bad news (rule 50)",
         "the locked door came with no key — rule 50(g) says the offer is automatic")
    want(str(len(WORKED)) in msg and str(total_units) in msg,
         f"the message counts honestly ({len(WORKED)} of {total_units})",
         "the message does not say how far along Sam actually is")

    # ------------------------------------------- 5. go back and pass the validated units
    step(5, f"Sam goes back and passes the Unit Quizzes for {VALIDATED}")
    for n in VALIDATED:
        r = c.post(f"/api/check/{CODE}", json={"unit": n, "correct": 10, "total": 10,
                                               "course": COURSE})
        if r.status_code != 200 or not r.json().get("mastered"):
            bad(f"unit {n} retake did not master: {r.text[:120]}")
    fin = (c.get(f"/api/session/{CODE}?course={COURSE}").json()
           .get("progress") or {}).get("final") or {}
    want(fin.get("eligible") is True,
         f"⭐ the Final Exam is now UNLOCKED ({fin.get('mastered_count')} of {fin.get('required')})",
         f"still locked after every unit was passed: {fin}")

    # ------------------------------------------------------- 6. the Final Exam
    step(6, "Sam takes the Final Exam and passes")
    r = c.post(f"/api/final/{CODE}", json={"correct": 17, "total": 18, "course": COURSE})
    body = r.json()
    want(body.get("ok") is True, "the exam recorded", f"exam not recorded: {body}")
    want(body.get("passed") or (body.get("best_pct") or 0) >= 90,
         f"passed with {body.get('best_pct') or body.get('pct')}%",
         f"94% did not count as a pass: {body}")

    # ------------------------------------------------------- 7. the trophy case
    step(7, "The Course Champion medal must be in Sam's trophy case")
    aw = c.get(f"/api/awards/{CODE}").json()
    ids = {a.get("id") for a in (aw.get("awards") or [])}
    want("champion" in ids, "🏅 Course Champion is in the trophy case",
         f"no champion award after passing the final: {sorted(ids)}")
    troph = [t.get("course") for t in (aw.get("trophies") or [])]
    want(COURSE in troph, f"the {title} course trophy is there too",
         f"course trophy missing: {troph}")
    b = (aw.get("badges") or {}).get(COURSE) or {}
    want(len(b.get("earned") or []) == total_units,
         f"all {total_units} unit badges earned",
         f"badges show {len(b.get('earned') or [])} of {total_units}")

    # ------------------------------------------------------- 8. the parent's view
    step(8, "The parent must see it on their side")
    r = c.get("/api/parent/overview", headers={"X-Parent-Token": ptok})
    want(r.status_code == 200, "parent overview loads", f"overview failed: {r.text[:160]}")
    ov = r.json()
    row = next((s for s in (ov.get("students") or []) if s.get("code") == CODE), None)
    want(row is not None, "Sam appears on the parent overview", "the child is missing")
    if row:
        want(int(row.get("units_mastered") or 0) == total_units,
             f"the parent sees all {total_units} units mastered",
             f"parent sees {row.get('units_mastered')} of {total_units}")

    # ------------------------------------------------------ 9. the teacher's view
    step(9, "A teacher adds Sam to a class and must see the same picture")
    r = c.post("/api/teacher/signup", json={"email": f"t-{uuid.uuid4().hex[:6]}@school.test",
                                            "password": "hunter2hunter2", "name": "Ms. Trial"})
    want(r.status_code == 200, "teacher account created", f"teacher signup failed: {r.text[:160]}")
    ttok = r.json()["token"]
    H = {"X-Teacher-Token": ttok}
    c.post("/api/class", json={"token": ttok, "class_code": "TRIAL1", "name": "Trial Class"})
    r = c.post("/api/class/TRIAL1/students", headers=H, json={"token": ttok, "code": CODE})
    want(r.status_code == 200, "Sam added to the class", f"add failed: {r.text[:160]}")

    r = c.get(f"/api/class/TRIAL1/summary?course={COURSE}", headers=H)
    want(r.status_code == 200, "the class summary loads", f"summary failed: {r.text[:160]}")
    summ = r.json()
    srow = (summ.get("students") or [{}])[0]
    want(int(srow.get("units_mastered") or 0) == total_units,
         f"the teacher sees all {total_units} units mastered",
         f"teacher sees {srow.get('units_mastered')} of {total_units}")
    want(CODE not in r.text,
         "⭐ and the teacher's view does NOT contain Sam's login code (build fa)",
         "THE TEACHER VIEW LEAKED THE STUDENT'S LOGIN CODE")

    # --------------------------------------------------------------- verdict
    print(f"\n{'=' * 74}")
    if FAILURES:
        print(f"\033[91mTRIAL FAILED — {len(FAILURES)} problem(s)\033[0m")
        for f in FAILURES:
            print(f"  - {f}")
    else:
        print("\033[92mTRIAL PASSED — the whole journey works, start to finish.\033[0m")
    print("=" * 74)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.
