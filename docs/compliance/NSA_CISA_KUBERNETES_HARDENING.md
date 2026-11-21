# NSA / CISA Kubernetes Hardening Guidance v2.0 Cross-Reference

## 1. Core Principles Alignment
The National Security Agency (NSA) and Cybersecurity and Infrastructure Security Agency (CISA) provide baseline Kubernetes hardening guidance.

---

## 2. Control Audit
- **Pod Security**: Enforce non-root execution, disable privilege escalation, drop capabilities (COMPLIANT).
- **Network Separation**: Implement default-deny NetworkPolicies across all tenant namespaces (COMPLIANT).
- **Authentication & RBAC**: Disable service account token auto-mounting on non-API pods (COMPLIANT).
- **Supply Chain**: Cryptographic image verification with immutable digests (COMPLIANT).
