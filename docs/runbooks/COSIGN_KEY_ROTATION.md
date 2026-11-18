# Operational Runbook: Cosign Key Rotation Procedure

## 1. Overview
When operating KMS-backed or asymmetric Cosign keys as fallbacks to keyless Sigstore, keys must undergo scheduled 90-day rotation or emergency rotation following suspected exposure.

---

## 2. Rotation Sequence (Zero-Downtime Transition)
1. **Phase 1: Pre-Stage New Public Key**:
   - Generate new keypair `cosign-2026-q4`.
   - Update Kyverno `ClusterPolicy` with dual-key trust roots (accepting both old and new signatures).
2. **Phase 2: Cutover Signing Pipeline**:
   - Update CI/CD secret `COSIGN_KEY_ID` to reference the new KMS key version.
   - Run verification pipeline and validate new signatures in staging.
3. **Phase 3: Deprecate Old Key**:
   - After grace period (minimum 14 days), remove the retired public key from Kyverno admission policies.
   - Archive the retired key in cold storage for historic audit verification.
