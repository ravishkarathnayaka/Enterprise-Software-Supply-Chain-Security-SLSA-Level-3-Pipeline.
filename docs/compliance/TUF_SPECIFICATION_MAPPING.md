# The Update Framework (TUF) Specification & Trust Delegation

## 1. Overview
The Update Framework (**TUF**) provides resilience against key compromise and repository rollback attacks. Sigstore's root-of-trust relies on TUF metadata.

---

## 2. TUF Roles in Sigstore Architecture
- **Root Role**: Distributes trust anchors and signs root keys with threshold multi-party keys.
- **Timestamp Role**: Prevents replay attacks by issuing short-lived validity timestamps.
- **Snapshot Role**: Guarantees consistency across all metadata files.
- **Targets Role**: Delivers verifiable public keys for Fulcio CA and Rekor transparency log.
