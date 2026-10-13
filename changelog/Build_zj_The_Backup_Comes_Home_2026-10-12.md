# Build zj — the backup comes home (2026-10-12)

Stamp: `2026-10-12zj-the-backup-comes-home`. Battery: **13,590 passed · 0 failed · 3 skipped** (PART 3pd, 16 checks). **Nothing to prewarm.**
Builds on zg, zh, zi (on disk, not yet pushed — one push carries all four).

Jim, 10-12: *"the backup didn't work because the DATA_EXPORT_KEY was dropped. It's still in
render. Also, it needs to know to automatically download it to D:\MrCadabra Backup."*

## 1. The key that kept getting dropped

The admin page's **Download a fresh backup** asks once for the `DATA_EXPORT_KEY` and remembers
it for the tab. But it threw the remembered key away on **any** failure: a slow snapshot (502 or
504), a restart mid-deploy. A good key had to be typed again every time something unrelated went
wrong, which looks exactly like "the key was dropped".

Now the key is forgotten **only on a 401**, when the server says the key itself is wrong.
Any other failure says what happened: "the server was busy or restarting. Your key is still
remembered; press again in a minute."

## 2. The backup downloads itself to D:\MrCadabra Backup

A web page cannot write into a folder on Jim's PC on its own, so the PC does the pulling.
`tools/pc-backup/` adds a Windows Task Scheduler job:

- **Install-Backup.cmd** (double-click once): asks for the `DATA_EXPORT_KEY` (copied from
  Render) and stores it **encrypted by Windows for Jim's login only** (DPAPI,
  `%LOCALAPPDATA%\MrCadabraBackup\key.dat`). The key is never in the repo or in plain text.
  It then registers **"Mr Cadabra weekly backup"**: Sundays 9:00, or as soon as the PC is next
  on if it was off. It takes the first backup immediately and says whether it worked.
- **run.ps1** (what the task runs): fetches a fresh backup and checks it is a real gzip file.
  It writes to a temporary file and renames it, keeps the **newest 8** in
  `D:\MrCadabra Backup`, and appends `OK` or `FAILED` with the reason to `backup-log.txt` there.
  A wrong key says to run the installer again.
- **Uninstall-Backup.cmd**: removes the task and the key, and leaves the backups alone.
- Windows PowerShell 5.1 (built into Windows), ASCII only. `.gitattributes` keeps `.cmd` files
  CRLF, the line ending cmd.exe needs.

**The server watches it.** The script tells the server it is the PC copy
(`X-Backup-Client: pc`), recorded as an ops pass. `/health` ages it as a new ops job,
**pcbackup**:

- it reads `off` ("not set up yet") until the first PC copy lands, so not installed is not an alarm;
- after that it is `ok` for up to nine days;
- past nine days it is `stale`, which sends the **STALE JOB** email and turns the admin
  Nightly jobs tile red (it now lists "PC copy").

A click on the admin button is recorded too, as a separate `download` pass.

## Proof

PART 3pd: the key is forgotten only on 401; the route records the pass after the key check; the
job's verdicts (off when never taken, ok at 3 days, stale at 10); the six files; ASCII-only
PowerShell; DPAPI store and read-back; the Sunday task with catch-up; the gzip check,
write-then-rename, keep-8 and log lines; CRLF launchers.

**Dry run**: the real `run.ps1` was driven by PowerShell 7 against the real app on a test
database. Three runs saved three real backups (a valid snapshot) and kept the newest 2 (with
`-Keep 2`), logging each. A wrong key exited 1 and logged the 401 with nothing saved.
`/health` then showed the PC copy `ok`.

**Not testable off Windows:** the DPAPI key save and the Task Scheduler registration in
`install.ps1` were checked for syntax only. The installer's own first run is the live test, and
it prints the result.

## Files

`main.py` (stamp, the route records the pass, the pcbackup ops job), `static/admin.html`
(the key fix, the tile), `tools/pc-backup/` (6 files, NEW), `.gitattributes` (`*.cmd`/`*.bat`
CRLF), `ruletests.py` (PART 3pd), this doc.

I did no harm and this file is not truncated.
