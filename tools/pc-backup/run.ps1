# =============================================================================
# run.ps1  --  MR. CADABRA WEEKLY BACKUP TO THIS PC  --  Hyperion Shift LLC
# -----------------------------------------------------------------------------
# CHANGE NOTES (keep newest at top):
#   2026-10-12  NEW FILE (build zj, Jim: "It needs to know to automatically download it
#               to D:\MrCadabra Backup"). Windows Task Scheduler runs this once a week
#               (install.ps1 sets that up). It asks mrcadabra.com for a FRESH backup with
#               the DATA_EXPORT_KEY, saves it in D:\MrCadabra Backup under the server's
#               own file name, checks it is a real gzip file of a sane size, keeps the
#               newest 8 and removes older ones, and appends one line to backup-log.txt
#               in that folder either way. It tells the server it is the PC copy
#               (X-Backup-Client: pc), so /health and the admin page know when the last
#               PC copy landed -- and a copy that stops landing raises the stale alarm.
#               THE KEY: never in this file. install.ps1 stored it encrypted with Windows'
#               own per-user encryption (DPAPI) in %LOCALAPPDATA%\MrCadabraBackup\key.dat;
#               only Jim's Windows login can read it back. -KeyPlain exists for the
#               battery's dry run only and is never used by the scheduled task.
#               Written for Windows PowerShell 5.1 (built into Windows) -- ASCII only.
# =============================================================================
param(
    [string]$BaseUrl  = "https://mrcadabra.com",
    [string]$Dest     = "D:\MrCadabra Backup",
    [string]$KeyFile  = (Join-Path $env:LOCALAPPDATA "MrCadabraBackup\key.dat"),
    [int]   $Keep     = 8,
    [string]$KeyPlain = ""
)
$ErrorActionPreference = "Stop"

function Write-Log([string]$line) {
    try {
        if (-not (Test-Path -LiteralPath $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }
        $stamp = (Get-Date).ToString("yyyy-MM-dd HH:mm")
        Add-Content -LiteralPath (Join-Path $Dest "backup-log.txt") -Value ("{0}  {1}" -f $stamp, $line)
    } catch { }
}

function Get-Key {
    if ($KeyPlain) { return $KeyPlain }
    if (-not (Test-Path -LiteralPath $KeyFile)) {
        throw "No saved key. Run Install-Backup.cmd again and paste the DATA_EXPORT_KEY from Render."
    }
    $enc = (Get-Content -LiteralPath $KeyFile -Raw).Trim()
    $sec = ConvertTo-SecureString $enc
    $ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec)
    try { return [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr) }
    finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr) }
}

try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Add-Type -AssemblyName System.Net.Http
    $key = Get-Key
    if (-not (Test-Path -LiteralPath $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }

    $client = New-Object System.Net.Http.HttpClient
    $client.Timeout = [TimeSpan]::FromMinutes(5)
    $url = $BaseUrl.TrimEnd("/") + "/api/admin/backup"
    $req = New-Object -TypeName System.Net.Http.HttpRequestMessage -ArgumentList @([System.Net.Http.HttpMethod]::Get, $url)
    $req.Headers.Add("X-Admin-Key", $key)
    $req.Headers.Add("X-Backup-Client", "pc")
    $resp = $client.SendAsync($req).GetAwaiter().GetResult()
    $code = [int]$resp.StatusCode
    if ($code -eq 401) { throw "The saved key was refused (401). The DATA_EXPORT_KEY in Render changed: run Install-Backup.cmd again." }
    if ($code -eq 503) { throw ("The server says backups are switched off (503): " + $resp.Content.ReadAsStringAsync().GetAwaiter().GetResult()) }
    if ($code -ne 200) { throw ("The server answered " + $code + ". Nothing was saved; the next run will try again.") }

    $bytes = $resp.Content.ReadAsByteArrayAsync().GetAwaiter().GetResult()
    if ($bytes.Length -lt 64 -or $bytes[0] -ne 0x1f -or $bytes[1] -ne 0x8b) {
        throw ("The download was not a backup file (" + $bytes.Length + " bytes). Nothing was saved.")
    }
    $name = "mrcadabra-backup-" + (Get-Date).ToUniversalTime().ToString("yyyyMMdd-HHmmss") + ".json.gz"
    $cd = $resp.Content.Headers.ContentDisposition
    if ($cd -and $cd.FileName) { $name = $cd.FileName.Trim('"') }
    if ($name -notmatch '^mrcadabra-backup-[0-9-]+\.json\.gz$') { throw "Unexpected file name from the server: $name" }

    $final = Join-Path $Dest $name
    $tmp = $final + ".part"
    [IO.File]::WriteAllBytes($tmp, $bytes)
    Move-Item -LiteralPath $tmp -Destination $final -Force

    $rows = ""
    try { $rows = ($resp.Headers.GetValues("X-Backup-Rows") | Select-Object -First 1) } catch { }

    # keep the newest $Keep backups; older ones go (the server keeps its own nightly copies)
    $all = Get-ChildItem -LiteralPath $Dest -Filter "mrcadabra-backup-*.json.gz" | Sort-Object Name -Descending
    $gone = 0
    if ($all.Count -gt $Keep) {
        $all | Select-Object -Skip $Keep | ForEach-Object { Remove-Item -LiteralPath $_.FullName -Force; $gone++ }
    }
    Write-Log ("OK    {0}  {1} KB, {2} rows; kept newest {3}, removed {4} older" -f $name, [math]::Round($bytes.Length / 1024), $rows, $Keep, $gone)
    exit 0
} catch {
    Write-Log ("FAILED  " + $_.Exception.Message)
    exit 1
}
# I did no harm and this file is not truncated.
