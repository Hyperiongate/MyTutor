# =============================================================================
# install.ps1  --  SETS UP THE WEEKLY BACKUP TO THIS PC  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-10-12  NEW FILE (build zj). Started by double-clicking Install-Backup.cmd. It:
#               1. asks once for the DATA_EXPORT_KEY (Jim copies it from Render ->
#                  mytutor-2 -> Environment) and stores it ENCRYPTED with Windows' per-user
#                  DPAPI in %LOCALAPPDATA%\MrCadabraBackup\key.dat -- never in the repo, never
#                  in plain text, readable only by this Windows login;
#               2. copies run.ps1 next to it (so the task never depends on the repo folder);
#               3. makes D:\MrCadabra Backup if it is missing;
#               4. registers a Task Scheduler task "Mr Cadabra weekly backup": Sundays 9:00,
#                  and if the PC was off then, as soon as it is next on (StartWhenAvailable);
#               5. runs it once right now and shows the result, so Jim sees it work today.
#               Running it again replaces the key and the task (that is how a changed key is
#               fixed). ASCII only, Windows PowerShell 5.1.
# =============================================================================
param([string]$Dest = "D:\MrCadabra Backup")
$ErrorActionPreference = "Stop"
$home2 = Join-Path $env:LOCALAPPDATA "MrCadabraBackup"
$taskName = "Mr Cadabra weekly backup"

Write-Host ""
Write-Host "Mr. Cadabra - weekly backup to this PC" -ForegroundColor Cyan
Write-Host "Backups will be saved in: $Dest"
Write-Host ""
Write-Host "Paste the DATA_EXPORT_KEY from Render (mytutor-2 -> Environment), then press Enter."
Write-Host "(Nothing shows while you paste - that is normal.)"
$sec = Read-Host -AsSecureString "DATA_EXPORT_KEY"
if ($sec.Length -lt 8) { Write-Host "That key looks too short. Nothing was changed." -ForegroundColor Red; exit 1 }

New-Item -ItemType Directory -Path $home2 -Force | Out-Null
New-Item -ItemType Directory -Path $Dest -Force | Out-Null
Set-Content -LiteralPath (Join-Path $home2 "key.dat") -Value (ConvertFrom-SecureString $sec)
Copy-Item -LiteralPath (Join-Path $PSScriptRoot "run.ps1") -Destination (Join-Path $home2 "run.ps1") -Force

$runner = Join-Path $home2 "run.ps1"
$arg = "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$runner`" -Dest `"$Dest`""
$action  = New-ScheduledTaskAction -Execute "powershell.exe" -Argument $arg
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 9am
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Minutes 15)
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings `
    -Description "Downloads a fresh Mr. Cadabra backup to $Dest every week (build zj)." -Force | Out-Null

Write-Host ""
Write-Host "Saved the key (encrypted) and set up the weekly task. Taking the first backup now..."
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File $runner -Dest $Dest
if ($LASTEXITCODE -eq 0) {
    Write-Host "Done. The first backup is in $Dest" -ForegroundColor Green
} else {
    Write-Host "The first backup did not work. The reason is the last line of:" -ForegroundColor Yellow
    Write-Host "  $Dest\backup-log.txt"
}
Write-Host ""
Read-Host "Press Enter to close"
# I did no harm and this file is not truncated.
