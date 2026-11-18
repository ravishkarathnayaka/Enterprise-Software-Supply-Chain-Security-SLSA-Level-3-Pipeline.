# Operational Runbook: Air-Gapped Signature Verification

## 1. Overview
In air-gapped or disconnected data center environments without direct internet access to Sigstore Fulcio, Rekor, or OCI public registries, signature and provenance verification requires local cryptographic trust roots.

---

## 2. Architecture for Disconnected Enclaves
- **Local Mirroring**: Images and their Cosign signature/attestation tags are mirrored into an on-premises private registry (`registry.internal:5000`).
- **Offline Rekor/TUF**: An internal The Update Framework (TUF) repository hosts offline root metadata, timestamp keys, and Rekor public keys.
- **Root-of-Trust Bundles**: Verification relies on pre-staged, hardware-verified root certificate bundles.

---

## 3. Verification Procedure
```bash
# Export offline TUF root
export SIGSTORE_ROOT_FILE=/etc/pki/sigstore/root.json

# Verify offline signature using exported public certificate
cosign verify \
  --key /etc/pki/cosign/enterprise-airgap.pub \
  --offline \
  registry.internal:5000/secure-supply-chain/app@sha256:...
```
