<#
.SYNOPSIS
    Exports and validates the application runtime cryptographic hash-chain.
#>
[CmdletBinding()]
param (
    [string]$ApiEndpoint = "http://localhost:8080/api/v1/audit/events",
    [string]$OutputPath = "audit-export.json"
)

Write-Host "Querying cryptographic audit events from: $ApiEndpoint" -ForegroundColor Cyan
try {
    $resp = Invoke-RestMethod -Uri $ApiEndpoint -Method Get
    if ($resp.chain_integrity_valid -eq $true) {
        Write-Host "[SUCCESS] Audit log hash-chain integrity verified." -ForegroundColor Green
        $resp | ConvertTo-Json -Depth 5 | Set-Content -Path $OutputPath -Encoding UTF8
        Write-Host "Exported to $OutputPath" -ForegroundColor Green
    } else {
        Write-Error "Audit chain integrity verification FAILED."
    }
} catch {
    Write-Warning "Could not connect to service endpoint: $_"
}
