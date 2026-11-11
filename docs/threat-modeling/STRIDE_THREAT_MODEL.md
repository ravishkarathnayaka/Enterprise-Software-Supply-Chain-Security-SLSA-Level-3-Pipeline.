# Threat Model Specification: STRIDE Methodology

## Overview
This document specifies the formal threat model for the Enterprise Software Supply Chain Security & SLSA Level 3 Pipeline. The system is evaluated using Microsoft's **STRIDE** methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) covering the entire SDLC from source commit to Kubernetes runtime admission.

---

## 1. System Components Under Review
1. **Developer Workstation & VCS (`git`)**: Source code origination and cryptographic commit signing.
2. **CI/CD Build Environment (GitHub Actions)**: Isolated runners, build provenance generators, SBOM tooling.
3. **Artifact Registry (GHCR / OCI)**: Storage for signed container images, in-toto attestations, and CycloneDX/SPDX SBOMs.
4. **Signature Verification & Transparency (Cosign / Sigstore / Rekor)**: Keyless identity provider (Fulcio) and tamper-proof log (Rekor).
5. **Admission Controller (Kyverno)**: Policy enforcement engine operating at the Kubernetes API server admission webhook.
6. **Container Runtime (Kubernetes)**: Distroless microservice execution with non-root user and read-only root filesystems.

---

## 2. STRIDE Threat Analysis Matrix

| ID | Threat Category | Threat Description | Attacker Objective | Impact | Mitigation Strategy | SLSA / Framework Control |
|---|---|---|---|---|---|---|
| **T-01** | **Spoofing** | Compromised developer identity pushing untracked commits | Inject backdoor or vulnerable dependency | High | Enforce mandatory GPG/SSH commit signature verification and branch protection rules. | SLSA Source Integrity (L3) |
| **T-02** | **Spoofing** | Forged in-toto attestation claiming false SLSA L3 build level | Bypass cluster admission gates | Critical | Keyless Fulcio OIDC cryptographic identity tokens bound to immutable GitHub workflow run claims. | SLSA Build Integrity (L3) |
| **T-03** | **Tampering** | Man-in-the-Middle tampering of upstream pip dependencies during container build | Poison application build dependencies | High | Pinned SHA-256 package hashes (`pip-compile` / hash-checking mode), private mirror caching. | NIST SSDF PW.4.1 |
| **T-04** | **Tampering** | Modification of container image layers post-build inside registry | Deploy malicious payloads | Critical | Immutable SHA256 digest references (`@sha256:...`) and Cosign cryptographic signatures. | CIS K8s 5.1.1 |
| **T-05** | **Repudiation** | Malicious build triggered with no audit trace of actor or parameters | Obfuscate attacker activities | Medium | Append-only transparency logging via Sigstore Rekor and GitHub workflow audit logs. | SLSA Non-falsifiable Provenance |
| **T-06** | **Information Disclosure** | Leakage of private API tokens or credentials inside container images | Exfiltrate secrets from published images | High | Gitleaks pre-commit + CI scanning, distroless runtime with zero embedded secrets, Trufflehog gates. | OWASP CI/CD-SEC-4 |
| **T-07** | **Denial of Service** | Resource exhaustion attacks against Kubernetes nodes via unbounded container limits | Cluster node crash / outage | Medium | Enforced Kubernetes `ResourceQuota`, `LimitRange`, and Kyverno CPU/Memory requirement policies. | CIS K8s 5.2.5 |
| **T-08** | **Elevation of Privilege** | Container escape to host node via root privileges or Linux capabilities | Full cluster node takeover | Critical | Non-root execution (`runAsUser: 65532`), distroless base image, `allowPrivilegeEscalation: false`, drop all capabilities. | Kyverno PSS-Restricted |

---

## 3. Residual Risk & Continual Evaluation
All identified threats are tracked with automated continuous validation in the CI/CD pipeline. Any drift from these controls fails the pipeline immediately.
