# PROJECT WATCHTOWER: MASTER CONTEXT STRESS-TEST (V2 PowerShell Native)
# TARGET: D:\Watchtower_Ops\Payloads | MISSION: Stress-Test Pipeline

$StagingDir = "D:\Watchtower_Ops\Payloads"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$PayloadFile = Join-Path $StagingDir "Watchtower_StressTest_$Timestamp.md"

# 1. Define L1/L2/L3 Targets
$Targets = [ordered]@{
    "L3 GOVERNANCE (GEMINI.md)" = "D:\Watchtower_Ops\GEMINI.md"
    "L2 REFINED KNOWLEDGE (insights.md)" = "D:\Watchtower_Ops\insights.md"
    "L1 WORKING STATE (working.md)" = "D:\Watchtower_Ops\working.md"
    "RAW MESH TELEMETRY (mesh_sweep.txt)" = "D:\Watchtower_Ops\mesh_sweep.txt"
}

# 2. Ensure Payload Airlock Exists
if (-not (Test-Path $StagingDir)) { 
    New-Item -ItemType Directory -Path $StagingDir -Force | Out-Null 
}

Write-Host "[*] COMPILING TACTICAL INTELLIGENCE PAYLOAD..." -ForegroundColor Cyan

# 3. Aggregate Hierarchical Cache Layers
"# PROJECT WATCHTOWER: MASTER CONTEXT STRESS-TEST`nGenerated: $(Get-Date)`n---`n" | Out-File -FilePath $PayloadFile -Encoding utf8

foreach ($Target in $Targets.GetEnumerator()) {
    if (Test-Path $Target.Value) {
        "## $($Target.Name)`n" | Out-File -FilePath $PayloadFile -Encoding utf8 -Append
        Get-Content $Target.Value | Out-File -FilePath $PayloadFile -Encoding utf8 -Append
        "`n`n---`n`n" | Out-File -FilePath $PayloadFile -Encoding utf8 -Append
    } else {
        Write-Host "[!] WARNING: Target missing -> $($Target.Value)" -ForegroundColor Red
    }
}

Write-Host "[+] PAYLOAD GENERATED: $PayloadFile" -ForegroundColor Green
Write-Host "[*] ACTION REQUIRED: INGEST VIA WEB IMPORTER AND RUN ULTRA EXPORTER." -ForegroundColor Yellow
