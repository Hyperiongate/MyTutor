#!/usr/bin/env python3
# =============================================================================
# notes_rollout.py  --  ROLL THE OLDER CHANGE NOTES OUT OF A HEADER  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-09-08  BUILD ui -- first version. Jim (09-08): main.py was 48% change notes,
#               tutor.py 27%, session.html 27%. This tool moves every header note dated
#               before a cutoff into changelog/<name>.md VERBATIM and leaves the newest
#               notes (and a dated pointer) at the top of the file. It proves, before it
#               writes, that the old header equals the new header with the moved lines
#               put back -- nothing edited, reordered or lost -- and PART 3ke of the
#               battery pins the result. Run it again when a header passes ~100 KB:
#                   python3 notes_rollout.py --root . --cutoff 2026-10-01 --build xx --apply main.py ...
#               (without --apply it only reports; --show-structure prints the lines it
#               will keep in place besides the notes, so you can eyeball a new file's
#               shape first). A second roll-out stacks its block ABOVE the earlier one.
# =============================================================================
"""notes_rollout.py -- roll the older CHANGE NOTES out of a file's header into
changelog/<file>.md, VERBATIM, keeping the newest notes in place. (build ui, 2026-09-08)

Usage:
    python3 notes_rollout.py --root /path/to/repo --cutoff 2026-09-01 [--apply] FILE...

Without --apply it only reports. With --apply it rewrites FILE and writes
changelog/<basename>.md. Every run proves the invariant before writing anything:
the old header == the new header with the moved lines put back in their places,
i.e. no line was edited, reordered or lost; the moved lines, in order, are the
changelog's body.

How a header is read:
  * Python files: the header is every line up to the first line that is neither a
    comment nor blank. An ENTRY starts at `#` + 1..5 spaces + a date. Lines shaped
    `#` + 2+ spaces + text, or a bare `#`, continue the entry. A `#` line with 0..1
    spaces before text (a banner, "HOW IT RUNS:", a rule) is STRUCTURE: it closes
    the entry and stays where it is; bare `#` lines right before structure are
    given back to the structure.
  * HTML pages: the header is everything before the first `<html` (or `<head`).
    An entry starts at 2..4 spaces, an optional "- ", an optional "(xx) ", a date.
    Lines that start at column 0 (`<!DOCTYPE`, `<!--`, `-->`) or with exactly two
    spaces and no date (the banner) are structure. Everything else continues the
    current entry.
  * An entry MOVES when its date is before the cutoff, wherever it sits (a file
    whose notes are slightly out of order is handled by date, not by position).
  * The pointer line is inserted after the "CHANGE NOTES (keep newest at top):"
    banner when there is one before the first kept entry, else after the header's
    first structure line.
"""
import argparse, os, re, sys, datetime

PY_ENTRY = re.compile(r"^#\s{1,5}(20\d\d-\d\d-\d\d)")
PY_CONT = re.compile(r"^#(\s{2,}\S|\s*$)")
HTML_ENTRY = re.compile(r"^\s{2,4}(?:-\s+)?(?:\(\w{1,2}\)\s+)?(20\d\d-\d\d-\d\d)")
BANNER = re.compile(r"CHANGE NOTES \(keep newest at top\)")


def split_header(path, text):
    lines = text.split("\n")
    if path.endswith(".py"):
        for i, l in enumerate(lines):
            if l.strip() and not l.startswith("#"):
                return lines[:i], lines[i:]
        raise SystemExit(f"{path}: no code after the header?")
    for i, l in enumerate(lines):
        if l.lstrip().startswith("<html") or l.lstrip().startswith("<head"):
            return lines[:i], lines[i:]
    raise SystemExit(f"{path}: no <html> after the header?")


def classify(path, header):
    """Yield (kind, date, line) with kind in {'structure', 'entry'}; entry lines
    carry the date of the entry they belong to."""
    py = path.endswith(".py")
    out = []
    cur = None          # date of the open entry, or None
    pending_blank = []  # bare-# / blank lines that may belong to structure
    for l in header:
        if py:
            m = PY_ENTRY.match(l)
            if m:
                out.extend(("entry", cur, x) for x in pending_blank) if cur else out.extend(("structure", None, x) for x in pending_blank)
                pending_blank = []
                cur = m.group(1); out.append(("entry", cur, l)); continue
            if cur and PY_CONT.match(l):
                if l.strip() == "#":
                    pending_blank.append(l); continue
                out.extend(("entry", cur, x) for x in pending_blank); pending_blank = []
                out.append(("entry", cur, l)); continue
            # structure: closes the entry; blanks before it go to structure
            out.extend(("structure", None, x) for x in pending_blank); pending_blank = []
            cur = None; out.append(("structure", None, l)); continue
        else:
            m = HTML_ENTRY.match(l)
            if m:
                out.extend(("entry", cur, x) for x in pending_blank) if cur else out.extend(("structure", None, x) for x in pending_blank)
                pending_blank = []
                cur = m.group(1); out.append(("entry", cur, l)); continue
            is_structure = (l and not l.startswith(" ")) or (re.match(r"^  \S", l) and not re.match(r"^  -", l))
            if cur and not is_structure:
                if l.strip() == "":
                    pending_blank.append(l); continue
                out.extend(("entry", cur, x) for x in pending_blank); pending_blank = []
                out.append(("entry", cur, l)); continue
            out.extend(("structure", None, x) for x in pending_blank); pending_blank = []
            cur = None; out.append(("structure", None, l)); continue
    out.extend(("structure", None, x) for x in pending_blank)
    return out


def pointer_lines(path, cutoff, today, build, kept, moved, name):
    """The pointer, wrapped like the notes around it (a first line, then continuations)."""
    import textwrap
    py = path.endswith(".py")
    body = (f"{today}  OLDER NOTES (before {cutoff}) live in changelog/{name}.md -- moved out on "
            f"{today} (build {build}) VERBATIM, {moved} entries; {kept} stay here. Keep adding new "
            f"notes HERE, newest at top; roll them out again (notes_rollout.py) when this header "
            f"passes ~100 KB.")
    first, cont = ("#   ", "#               ") if py else ("    ", "                ")
    w = textwrap.wrap(body, width=90 - len(cont))
    return [first + w[0]] + [cont + x for x in w[1:]]


def rollout(root, rel, cutoff, today, build, apply):
    path = os.path.join(root, rel)
    text = open(path, encoding="utf-8").read()
    header, rest = split_header(rel, text)
    cls = classify(rel, header)
    dates = sorted({d for k, d, _ in cls if k == "entry"})
    moved = [l for k, d, l in cls if k == "entry" and d < cutoff]
    kept_lines = [l for k, d, l in cls if not (k == "entry" and d < cutoff)]
    n_entries = lambda lines: sum(1 for l in lines if (PY_ENTRY if rel.endswith(".py") else HTML_ENTRY).match(l))
    # ---- the invariant: old header == new header with the moved lines put back ----
    merged = []; mi = ki = 0
    for k, d, l in cls:
        if k == "entry" and d < cutoff:
            merged.append(moved[mi]); mi += 1
        else:
            merged.append(kept_lines[ki]); ki += 1
    assert merged == header and mi == len(moved) and ki == len(kept_lines), f"{rel}: invariant broken"
    assert not any((PY_ENTRY if rel.endswith(".py") else HTML_ENTRY).match(l) and
                   (PY_ENTRY if rel.endswith(".py") else HTML_ENTRY).match(l).group(1) < cutoff for l in kept_lines)
    name = os.path.basename(rel)
    n_moved, n_kept = n_entries(moved), n_entries(kept_lines)
    # ---- the pointer ----
    ptr = pointer_lines(rel, cutoff, today, build, n_kept, n_moved, name)
    first_kept = next((i for i, l in enumerate(kept_lines)
                       if (PY_ENTRY if rel.endswith(".py") else HTML_ENTRY).match(l)), len(kept_lines))
    banner_at = next((i for i, l in enumerate(kept_lines[:first_kept]) if BANNER.search(l)), None)
    if banner_at is not None:
        at = banner_at + 1
    elif rel.endswith(".py"):
        at = 0
    else:
        at = next(i for i, l in enumerate(kept_lines) if l.strip() == "<!--") + 1   # INSIDE the comment
    kept_lines[at:at] = ptr
    new_text = "\n".join(kept_lines + rest)
    structure = [l for k, d, l in cls if k == "structure"]
    report = {
        "file": rel, "header_before": sum(len(l) + 1 for l in header),
        "header_after": sum(len(l) + 1 for l in kept_lines), "entries_kept": n_kept,
        "entries_moved": n_moved, "oldest_kept": min((d for k, d, _ in cls if k == "entry" and d >= cutoff), default=None),
        "newest_moved": max((d for k, d, _ in cls if k == "entry" and d < cutoff), default=None),
        "structure_lines": structure,
    }
    if not moved:
        report["note"] = "nothing older than the cutoff"
        return report
    fence = "```"
    body = "\n".join(moved)
    while fence in body:
        fence += "`"
    changelog = (f"# CHANGELOG -- {name}  (notes rolled out of the file's header)\n\n"
                 f"Moved out of `{rel}` on {today} (build {build}): every CHANGE NOTE dated before "
                 f"{cutoff} -- {n_moved} entries, VERBATIM, in the order they sat in the file (newest first). "
                 f"The {n_kept} notes from {cutoff} on stay at the top of `{rel}` itself, and new notes keep going "
                 f"there. Nothing below was edited; grep this file for a build letter or a date. When the header "
                 f"is rolled out again, the newer block is added ABOVE this one.\n\n"
                 f"{fence}text\n{body}\n{fence}\n\nI did no harm and this file is not truncated.\n")
    report["changelog"] = os.path.join("changelog", name + ".md")
    report["changelog_bytes"] = len(changelog)
    if apply:
        os.makedirs(os.path.join(root, "changelog"), exist_ok=True)
        cl_path = os.path.join(root, "changelog", name + ".md")
        if os.path.exists(cl_path):
            old = open(cl_path, encoding="utf-8").read()
            # a second roll-out stacks its block ABOVE the earlier one
            head, sep, tail = old.partition(fence + "text\n")
            changelog = changelog.rstrip("\n").rsplit("\n\nI did no harm", 1)[0] + "\n\n---\n\n" + sep + tail
        open(cl_path, "w", encoding="utf-8").write(changelog)
        open(path, "w", encoding="utf-8").write(new_text)
        # re-read and prove it
        again = open(path, encoding="utf-8").read()
        h2, r2 = split_header(rel, again)
        assert r2 == rest, f"{rel}: the code after the header changed"
        cl = open(cl_path, encoding="utf-8").read()
        assert body in cl, f"{rel}: the changelog lost the body"
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True); ap.add_argument("--cutoff", required=True)
    ap.add_argument("--build", default="ui"); ap.add_argument("--today", default=str(datetime.date.today()))
    ap.add_argument("--apply", action="store_true"); ap.add_argument("--show-structure", action="store_true")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    for rel in a.files:
        r = rollout(a.root, rel, a.cutoff, a.today, a.build, a.apply)
        tail = (f"-> {r['changelog']} ({r['changelog_bytes']:,} B)" if "changelog" in r else r.get("note", ""))
        print(f"{r['file']:28s} header {r['header_before']:>8,} -> {r['header_after']:>8,}  kept {r['entries_kept']:>3}  "
              f"moved {r['entries_moved']:>3}  oldest kept {r['oldest_kept']}  newest moved {r['newest_moved']}  {tail}")
        if a.show_structure:
            for l in r["structure_lines"]:
                print("     |", l[:110])


if __name__ == "__main__":
    main()

# I did no harm and this file is not truncated.
