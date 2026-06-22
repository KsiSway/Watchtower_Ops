# PROJECT WATCHTOWER: Coral_Env (Python 3.9) Provisioning
# Architecture: OptiPlex 3050 (Windows 11) -> Google Coral TPU
$ErrorActionPreference = "Stop"

Write-Host "[*] INITIATING PYTHON 3.9 SANDBOX PROVISIONING..." -ForegroundColor Cyan

# 1. Fetch Python 3.9 via Scoop (versions bucket)
Write-Host "[*] Fetching Python 3.9 binary..." -ForegroundColor Yellow
scoop bucket add versions | Out-Null
scoop install python39

# 2. Forge the Virtual Environment
$Py39Path = "$(scoop prefix python39)\python.exe"
$EnvPath = "D:\Watchtower_Ops\Coral_Env"

if (-not (Test-Path $EnvPath)) {
    Write-Host "[*] Generating Coral_Env at $EnvPath..." -ForegroundColor Yellow
    & $Py39Path -m venv $EnvPath
} else {
    Write-Host "[!] Coral_Env directory already exists. Injecting drivers..." -ForegroundColor Yellow
}

# 3. Inject Drivers into the Sandbox (NUMPY ABI CONSTRAINT ENFORCED)
Write-Host "[*] Securing hardware and database bindings..." -ForegroundColor Yellow
$PipPath = "$EnvPath\Scripts\pip.exe"

# Upgrade pip and install specific Google Coral dependencies
& $PipPath install --upgrade pip
& $PipPath install --extra-index-url https://google-coral.github.io/py-repo/ pycoral~=2.0 tflite-runtime~=2.5.0.post1 "numpy<2" psycopg2-binary Pillow

Write-Host "[+] Coral_Env FORGED. Hardware bindings secured." -ForegroundColor Green
Write-Host "[*] ACTION REQUIRED: Execute osint_tpu_vision_v2.py via $EnvPath\Scripts\python.exe" -ForegroundColor Green
