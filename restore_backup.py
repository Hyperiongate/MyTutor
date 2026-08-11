# =============================================================================
# restore_backup.py  --  THE WAY BACK  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-08-11  NEW FILE (build dj). Jim: "if Render falters or something falters, do
#               we have sufficient backup so that we could recreate everything right
#               away?" This is the restore half of the answer. It is a COMMAND-LINE
#               script on purpose -- there is no restore endpoint in the product,
#               because a remote wipe-and-replace is a foot-gun, not a feature. It
#               refuses to run without the --yes-i-mean-it flag, prints exactly what
#               it is about to do first, restores inside ONE transaction (any failure
#               rolls the whole thing back -- a half-restored database cannot exist),
#               and prints per-table row counts when it is done.
#
# HOW TO USE IT (the two-minute drill; the full runbook is RECOVERY.md):
#   1. Get a backup file. Either the /admin "Download a backup" button (a fresh
#      snapshot, saved to your computer) or one of the nightly files in
#      /var/data/backups on the Render disk (Render -> service -> Shell tab).
#   2. Point DATABASE_URL at the database you are restoring INTO. For a brand-new
#      Render Postgres, that is its External Database URL (dashboard -> the database
#      -> Connect -> External). The app's own tables are created automatically the
#      first time the service boots against it -- boot the service once first.
#   3. Dry look (free, changes nothing):
#          python restore_backup.py mrcadabra-backup-20260811.json.gz
#      It prints what the snapshot contains and STOPS.
#   4. The real restore (REPLACES the database's contents with the snapshot):
#          python restore_backup.py mrcadabra-backup-20260811.json.gz --yes-i-mean-it
#   5. Open /health (db true) and the parent dashboard, and spot-check one student.
# =============================================================================
import gzip
import json
import sys


def main() -> int:
    args = [a for a in sys.argv[1:]]
    go = "--yes-i-mean-it" in args
    paths = [a for a in args if not a.startswith("--")]
    if len(paths) != 1:
        print(__doc__ or "usage: python restore_backup.py <backup.json.gz> [--yes-i-mean-it]")
        print("usage: python restore_backup.py <backup.json.gz> [--yes-i-mean-it]")
        return 2

    raw = open(paths[0], "rb").read()
    if raw[:2] == b"\x1f\x8b":                       # gzip magic
        raw = gzip.decompress(raw)
    snap = json.loads(raw.decode("utf-8"))

    counts = snap.get("row_counts") or {k: len(v or []) for k, v in
                                        (snap.get("tables") or {}).items()}
    total = sum(counts.values())
    print(f"Snapshot: format {snap.get('format')} · taken {snap.get('created_utc')} "
          f"· from a {snap.get('dialect')} database")
    print(f"Contents: {len(counts)} tables, {total} rows")
    for name in sorted(counts):
        print(f"  {name:<20} {counts[name]:>7} rows")

    import store
    store.init()                                     # connects using DATABASE_URL and creates tables
    if not store.enabled():
        print("\nSTOP: DATABASE_URL is not set (or the database could not be reached).")
        print("Point DATABASE_URL at the database you are restoring INTO and run again.")
        return 1

    if not go:
        print("\nDRY LOOK ONLY -- nothing was changed.")
        print("To REPLACE the target database's contents with this snapshot, run again")
        print("with the flag:  --yes-i-mean-it")
        return 0

    print("\nRestoring (one transaction; any failure rolls the whole restore back)...")
    result = store.import_all(snap, wipe=True)
    for name in sorted(result["restored"]):
        print(f"  restored {name:<20} {result['restored'][name]:>7} rows")
    if result["skipped"]:
        print(f"  skipped tables this build does not know: {result['skipped']}")
    print("Done. Now verify: /health shows db true; open the parent dashboard; "
          "spot-check one student's mastery.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# I did no harm and this file is not truncated.
