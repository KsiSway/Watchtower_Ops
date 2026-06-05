# Watchtower Master Sync & Archive Script
$OpsPath = "D:\Watchtower_Ops"
$ArchivePath = "D:\Watchtower_Ops\pam_archive"
$Timestamp = Get-Date -Format "yyyy-MM-dd_HHmm"

if (!(Test-Path $ArchivePath)) { New-Item -ItemType Directory -Path $ArchivePath }

Write-Host "[*] Initiating OSINT Log Sweep..." -ForegroundColor Cyan

# Sweep loose .txt files into archive
$LooseLogs = Get-ChildItem -Path $OpsPath -Filter "*.txt" | Where-Object { $_.Name -notmatch "Manual.txt|requirements.txt" }
foreach ($Log in $LooseLogs) {
    $Dest = Join-Path $ArchivePath ($Log.BaseName + "_" + $Timestamp + $Log.Extension)
    Move-Item -Path $Log.FullName -Destination $Dest -Force
    Write-Host "[+] Archived: $($Log.Name)" -ForegroundColor Green
}

Write-Host "[*] Generating Master Intelligence Context..." -ForegroundColor Cyan
# Add logic here to aggregate logs into Watchtower_Master_Context.md
Write-Host "[+] Mission Complete." -ForegroundColor Green
