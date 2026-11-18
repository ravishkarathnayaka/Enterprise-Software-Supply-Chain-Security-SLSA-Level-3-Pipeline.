# PCI DSS v4.0 Requirement 6: Build & Software Security Controls

## 1. Overview
Payment Card Industry Data Security Standard (**PCI DSS**) v4.0 Requirement 6 mandates strict controls over the software development lifecycle.

---

## 2. Control Verification
- **Req 6.2.4**: Application code protected from code injection and common attacks (enforced via Pydantic input models and Semgrep).
- **Req 6.3.1**: Software vulnerabilities identified and managed before deployment (automated Trivy gates).
- **Req 6.3.2**: Inventory of bespoke and custom software dependencies maintained (CycloneDX SBOMs).
