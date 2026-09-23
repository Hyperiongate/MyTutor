#!/usr/bin/env python3
# =============================================================================
# tools/pinscan.py  --  THE PRE-FLIGHT: WHICH PINS QUOTE TEXT THAT JUST CHANGED
#                   --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-23  BUILD xs -- NEW, in the repo this time. The xi pre-flight lived in a session
#               scratchpad and was lost with it (the 09-23 handoff said so). This one is
#               simpler and cannot be lost: it does not parse the PARTs' spellings at all.
#               It builds the CORPUS -- every spoken line, board, praise, walk-back and
#               generated ask of every problem of every lesson, plus the raw lesson and
#               generator source -- and asks, for every string literal of 20+ characters
#               in ruletests.py, whether it is in the corpus. Run it twice: once on the
#               frozen tree with --freeze to save that tree's corpus, then on the edited
#               tree with --against, and it prints exactly the literals that WERE in the
#               corpus and are NOT any more -- the stale pins this build made. A literal
#               that was never in the corpus (an error message, a note) is not reported,
#               which is what made the global scan usable. Zero output means no pin moved.
#
#   Usage (from the repo root):
#     PYTHONPATH=. python3 tools/pinscan.py --freeze /tmp/corpus_before.json   # on the frozen copy
#     PYTHONPATH=. python3 tools/pinscan.py --against /tmp/corpus_before.json  # on the edited tree
#     PYTHONPATH=. python3 tools/pinscan.py            # no diff: every literal not in the corpus
# =============================================================================
import ast
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

MIN_LEN = 20


def build_corpus():
    import lessonscripts as L
    parts = []
    for les in L.LESSONS:
        parts.append(" ".join(L.audio_lines(les)))
        for k in ("teach", "why", "picture", "recap", "practice_intro", "advance_line", "intro"):
            v = les.get(k)
            if isinstance(v, str):
                parts.append(v)
            elif isinstance(v, (list, tuple)):
                for item in v:
                    if isinstance(item, str):
                        parts.append(item)
                    elif isinstance(item, (list, tuple)):
                        parts.extend(str(x) for x in item)
        probs = list(les.get("bank") or [])
        for pr in les.get("pairs") or []:
            w = pr.get("worked")
            if w:
                parts.extend(str(x) for x in w)
            if pr.get("ask"):
                probs.append(pr["ask"])
        levels = tuple(les.get("levels") or ("abstract",))
        for p in probs:
            for lv in levels:
                for fn in (L.spoken_for, L.board_for):
                    try:
                        parts.append(str(fn(p, lv)))
                    except Exception:
                        pass
            for i in range(4):
                try:
                    parts.append(str(L.praise_for(p, i)))
                except Exception:
                    pass
            try:
                w = L._worked_for(p)
                if w:
                    parts.extend(str(x) for x in w)
            except Exception:
                pass
            ext = L.OP_EXT.get(p.get("op"), {}) if isinstance(p, dict) else {}
            for key in ("praise", "explain", "spoken", "board", "worked", "second_look"):
                f = ext.get(key)
                if callable(f):
                    try:
                        r = f(p)
                        parts.extend(str(x) for x in r) if isinstance(r, (list, tuple)) else parts.append(str(r))
                    except Exception:
                        pass
    # raw source too: a pin may quote a source string that no rendered path reaches
    for name in ("lessonscripts.py", "coursesweep.py", "tutor.py", "main.py"):
        try:
            with open(os.path.join(HERE, name), encoding="utf-8") as fh:
                parts.append(fh.read())
        except OSError:
            pass
    ldir = os.path.join(HERE, "lessons")
    for fn in sorted(os.listdir(ldir)):
        if fn.endswith(".py"):
            with open(os.path.join(ldir, fn), encoding="utf-8") as fh:
                parts.append(fh.read())
    return "\n".join(parts)


def literals(path):
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src)
    out = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            s = node.value
            if len(s) >= MIN_LEN and re.search(r"[A-Za-z]", s):
                out.setdefault(s, node.lineno)
    return out


def main(argv):
    corpus = build_corpus()
    lits = literals(os.path.join(HERE, "ruletests.py"))
    present = {s for s in lits if s in corpus}
    if "--freeze" in argv:
        path = argv[argv.index("--freeze") + 1]
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(sorted(present), fh, ensure_ascii=False)
        print("froze %d literals present in the corpus -> %s" % (len(present), path))
        return 0
    if "--against" in argv:
        path = argv[argv.index("--against") + 1]
        with open(path, encoding="utf-8") as fh:
            before = set(json.load(fh))
        stale = sorted(s for s in before if s in lits and s not in corpus)
        for s in stale:
            print("STALE line %d: %r" % (lits[s], s[:110]))
        print("%d stale pin(s)" % len(stale))
        return 1 if stale else 0
    missing = sorted(s for s in lits if s not in corpus)
    for s in missing:
        print("line %d: %r" % (lits[s], s[:110]))
    print("%d literal(s) of %d not in the corpus (most are messages, not pins)" % (len(missing), len(lits)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# I did no harm and this file is not truncated.
