# SOC 2 Type II Trust Services Criteria: CI/CD Evidence Map

## 1. Purpose
Provides auditor-ready mappings between SOC 2 Type II Common Criteria (CC) and automated pipeline evidence artifacts.

---

## 2. Evidence Mappings

| SOC 2 Criteria | Control Description | Automated Pipeline Evidence |
|---|---|---|
| **CC6.1** | Logical Access Controls | Mandatory multi-factor branch protection, signed commits. |
| **CC6.6** | Boundary Protection & Network | Kyverno default-deny NetworkPolicies and TLS termination. |
| **CC7.1** | Vulnerability Detection | Automated Semgrep SAST, Gitleaks, and Trivy container scanning. |
| **CC8.1** | Change Management Authorization | In-toto SLSA provenance linking PR approvals to running digests. |
