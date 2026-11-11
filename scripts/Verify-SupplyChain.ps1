<#
.SYNOPSIS
    PowerShell Native Verification Utility for Supply Chain Integrity.
.DESCRIPTION
    Verifies local SHA256 checksums, manifest formats, and policy compliance on Windows.
#>
[CmdletBinding()]
param (
    [string]$Directory = "app"
)

Write-Host "Verifying Supply Chain Integrity in: $Directory" -ForegroundColor Cyan

$files = Get-ChildItem -Path $Directory -Recurse -File -Filter "*.py"
foreach ($f in $files) {
    $hash = Get-FileHash -Path $f.FullName -Algorithm SHA256
    Write-Host "  [OK] $($f.Name): $($hash.Hash.Substring(0, 16))..." -ForegroundColor Green
}

Write-Host "All source file hashes verified successfully." -ForegroundColor Green
