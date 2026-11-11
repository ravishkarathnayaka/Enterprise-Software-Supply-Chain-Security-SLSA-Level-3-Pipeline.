# Executive Order 14028 Supply Chain Compliance Attestation

## Executive Summary
United States Executive Order 14028 ("Improving the Nation's Cybersecurity") directs federal agencies and suppliers to adhere to rigorous software supply chain security standards. This document details our compliance attestation.

---

## EO 14028 Core Requirements & Evidence

### 1. Software Bill of Materials (SBOM) Generation
- **Requirement**: Produce an automated, machine-readable SBOM for every software release.
- **Compliance**: Automated generation of SPDX 2.3 and CycloneDX 1.5 JSON SBOMs using Syft during Stage 5 of the CI/CD pipeline.
- **Evidence**: Cryptographically signed SBOM attestation attached to the container image in GHCR.

### 2. Cryptographic Provenance & Signature
- **Requirement**: Maintain immutable provenance attestation linking compiled binaries to their source repository.
- **Compliance**: Cosign keyless signing using GitHub Actions OIDC identity with Sigstore Rekor ledger entries.
- **Evidence**: In-toto provenance predicate (`https://slsa.dev/provenance/v0.2`).

### 3. Automated Vulnerability Scanning (SAST/SCA)
- **Requirement**: Continuous testing for software defects and dependencies prior to distribution.
- **Compliance**: Semgrep SAST, Gitleaks secret scanning, and Trivy CVE scanning in automated CI gates.
