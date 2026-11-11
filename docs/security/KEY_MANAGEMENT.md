# Cryptographic Trust Anchor & Key Lifecycle Management

## 1. Cryptographic Architecture
This pipeline leverages **Sigstore** keyless signing as the primary cryptographic trust anchor, backed by an optional Hardware Security Module (HSM) / Cloud KMS fallback model.

### Keyless Sigstore Infrastructure
- **Fulcio (CA)**: Short-lived X.509 certificates (10-minute validity) bound to OpenID Connect (OIDC) tokens issued by GitHub Actions.
- **Rekor (Transparency Log)**: Append-only, cryptographically verifiable Merkle tree recording every signature and attestation.
- **Cosign**: Client utility used in GitHub Actions to sign artifacts and in Kubernetes/Kyverno to verify integrity.

---

## 2. Key Lifecycle & Rotation Schedule

| Key Type | Storage Location | Validity Duration | Rotation Strategy | Audit Cadence |
|---|---|---|---|---|
| **Fulcio Ephemeral Cert** | Ephemeral memory in CI runner | 10 minutes | Generated per-signing event; no long-term storage | Real-time via Rekor log |
| **Cosign Asymmetric Key (Fallback)** | Azure Key Vault / AWS KMS / GCP KMS | 90 days | Automated rotation via KMS schedule with versioned aliases | Weekly audit review |
| **Kyverno Admission CA** | Kubernetes Secret (`cert-manager`) | 365 days | Automated rotation with dual-cert trust transition | Monthly automated check |
| **GPG Committer Keys** | Developer YubiKey / Hardware Token | 365 days | Annual expiration with mandatory revocation check | Continuous per commit |

---

## 3. Trust Anchor Verification Commands

To verify a container image against the keyless trust anchor:
```bash
cosign verify \
  --certificate-identity-regexp="https://github.com/ravishkarathnayaka/.*" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/ravishkarathnayaka/enterprise-supply-chain-app@sha256:...
```
