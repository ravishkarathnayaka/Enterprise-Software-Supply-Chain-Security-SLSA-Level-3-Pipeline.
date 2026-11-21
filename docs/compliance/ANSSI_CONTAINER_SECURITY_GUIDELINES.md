# ANSSI Recommendations for Container Security Alignment

## 1. Overview
The French National Cybersecurity Agency (**ANSSI**) publishes recommendations for securing container runtimes and build chains.

---

## 2. ANSSI Recommendations Matrix
- **R1 (Minimal Base Images)**: Mandate distroless container images with zero shell binaries.
- **R4 (Immutability)**: Mount filesystems read-only and enforce cryptographic image digests.
- **R7 (Isolation)**: Prevent container privilege escalation and enforce non-root user accounts.
