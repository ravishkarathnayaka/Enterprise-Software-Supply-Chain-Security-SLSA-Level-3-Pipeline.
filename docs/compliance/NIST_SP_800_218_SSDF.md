# NIST SP 800-218 (SSDF v1.1) Framework Alignment

## Overview
The NIST Secure Software Development Framework (**SSDF**) provides recommendations for mitigating software supply chain vulnerabilities. This matrix documents how the pipeline fulfills SSDF core practices.

---

## SSDF Practice Alignment Matrix

### 1. Prepare the Organization (PO)
- **PO.1.1 (Security Requirements)**: Security gates defined for SAST, SCA, and secrets scanning.
- **PO.3.2 (Supporting Toolchains)**: Pinned CI actions and verified toolchain binaries (Cosign, Syft, Trivy).

### 2. Protect Software (PS)
- **PS.1.1 (Code Integrity)**: All commits require cryptographic signatures; branch protection forbids unsigned force-pushes.
- **PS.2.1 (Software Packaging)**: Distroless container images with non-root execution and immutable content digests.
- **PS.3.1 (Verify Third-Party Software)**: Automated dependency scanning and CVE vulnerability thresholds before merging.
- **PS.3.2 (Integrity Verification)**: Kyverno admission controller enforces image signatures and SBOM attestations prior to pod scheduling.

### 3. Produce Well-Secured Software (PW)
- **PW.1.2 (Security in Architecture)**: Threat modeling via STRIDE, defense-in-depth, and least privilege.
- **PW.4.1 (Vulnerability Scanning)**: Semgrep SAST scans application logic on every pull request.
- **PW.5.1 (Code Review)**: Two-person rule enforced on all pull requests targeting `main`.

### 4. Respond to Vulnerabilities (RV)
- **RV.1.1 (Vulnerability Identification)**: Continuous CVE monitoring with automated Dependabot alerts.
- **RV.1.3 (Incident Response)**: Documented Supply Chain Incident Response Playbook (`IRP-01`).
