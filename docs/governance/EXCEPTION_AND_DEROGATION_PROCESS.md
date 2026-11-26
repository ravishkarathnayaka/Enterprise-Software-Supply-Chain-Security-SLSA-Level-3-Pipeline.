# Security Policy Exception & Cryptographic Derogation Lifecycle

## Purpose
Establishes a zero-exception baseline while defining rigorous, time-bounded emergency derogation procedures when upstream critical fixes require temporary policy overrides.

## Derogation Requirements
1. **Multi-Party Approval**: Requires cryptographic signatures from CISO and Lead Supply Chain Architect.
2. **Time-Bounded Expiry**: Maximum allowable exception window is 14 calendar days.
3. **Automated Admission Exemption**: Exemption manifests must reference explicit CVE IDs and expiration timestamps.
4. **Automatic Revocation**: Once expired, Kyverno policies revert automatically to fail-closed enforcement.
