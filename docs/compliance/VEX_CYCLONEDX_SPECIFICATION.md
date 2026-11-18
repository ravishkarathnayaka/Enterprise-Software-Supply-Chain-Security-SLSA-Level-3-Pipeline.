# Vulnerability Exploitability eXchange (VEX) CycloneDX Integration

## 1. Motivation
Raw vulnerability scans produce excessive false positives for code paths never invoked at runtime. **VEX** provides machine-readable assertions of exploitability.

---

## 2. VEX Status Enum
- `not_affected`: Code is present but non-vulnerable, non-reachable, or mitigated.
- `affected`: Exploitability confirmed; requires remediation.
- `fixed`: Patch has been applied.
- `under_investigation`: Triage in progress.
