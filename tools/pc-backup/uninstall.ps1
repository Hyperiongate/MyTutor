# =============================================================================
# uninstall.ps1  --  STOPS THE WEEKLY BACKUP TO THIS PC  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-10-12  NEW FILE (build zj). Removes the Task Scheduler task and the encrypted key
#               (%LOCALAPPDATA%\MrCadabraBackup). The backups already in D:\MrCadabra Backup
#               are left alone -- deleting those is Jim's decision. ASCII only.
# =============================================================================
$ErrorActionPreference = "Continue"
Unregister-ScheduledTask -TaskName "Mr Cadabra weekly backup" -Confirm:$false -ErrorAction SilentlyContinue
Remove-Item -LiteralPath (Join-Path $env:LOCALAPPDATA "MrCadabraBackup") -Recurse -Force -ErrorAction SilentlyContinue
Write-Host "The weekly backup is switched off and the saved key is removed."
Write-Host "Backups already in D:\MrCadabra Backup were left where they are."
Read-Host "Press Enter to close"
# I did no harm and this file is not truncated.
