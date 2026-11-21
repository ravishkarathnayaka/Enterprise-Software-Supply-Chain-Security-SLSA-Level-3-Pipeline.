# Provenance Data Retention & Attestation Lifecycle Policy

## 1. Compliance Retention Windows
- **Production Provenance**: Retained indefinitely in Sigstore Rekor public transparency log.
- **Internal Build Logs**: Retained in encrypted cloud storage for minimum **7 years** (SOC 2 / ISO 27001).
- **CycloneDX SBOMs**: Stored alongside container images in OCI registry indefinitely.

---

## 2. Archival & Cryptographic Immutability
All attestation envelopes are cryptographically hashed and mirrored to write-once-read-many (WORM) storage tiers.
