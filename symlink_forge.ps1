# PROJECT WATCHTOWER: MCP Symlink Forge (Namespace Boundary Enforcement)
# Architecture: OptiPlex x64 Host -> Windows PowerShell
$ErrorActionPreference = "Stop"

# 1. Define the paths
$SecureConfig = "D:\Watchtower_Ops\.gemini\antigravity\mcp_config.json"
$LegacyDir = "C:\Users\Lance\.gemini\antigravity"
$LegacyPath = "$LegacyDir\mcp_config.json"

# 2. Ensure the legacy directory exists
if (-not (Test-Path $LegacyDir)) {
    New-Item -ItemType Directory -Path $LegacyDir -Force | Out-Null
}

# 3. Forge the Symbolic Link (Overwrites any existing generic configs)
if (Test-Path $LegacyPath) { Remove-Item $LegacyPath -Force }
New-Item -ItemType SymbolicLink -Path $LegacyPath -Target $SecureConfig -Force

Write-Host "[+] SYMLINK FORGED. C:\ namespace safely redirected to D:\ airlock." -ForegroundColor Green
Write-Host "[*] ACTION REQUIRED: Verify physical Mango VPN Router tunnel is active, then restart Antigravity." -ForegroundColor Yellow
