# Enterprise Cryptographic Standards for Supply Chain Artifacts

## 1. Authorized Cryptographic Primitives

| Purpose | Approved Standard | Minimum Key Length | Banned / Deprecated |
|---|---|---|---|
| **Artifact Hashing** | SHA-256, SHA-512 | 256 bits | MD5, SHA-1 |
| **Commit Signing** | Ed25519, RSA | 3072 bits (RSA) / 256 bits (Ed25519) | RSA < 2048, DSA |
| **Cosign Asymmetric Keys** | ECDSA (NIST P-256), Ed25519 | P-256 curve | Secp256k1, RSA 1024 |
| **OIDC Token Encryption** | RS256, ES256 | Standard JWK | HS256 (symmetric) |
| **Transport Encryption** | TLS 1.3 (RFC 8446) | ECDHE key exchange | TLS 1.0, 1.1, SSLv3 |

---

## 2. Hash Pinning Mandate
All Dockerfile `FROM` directives and pip dependencies must strictly pin SHA-256 content hashes.
