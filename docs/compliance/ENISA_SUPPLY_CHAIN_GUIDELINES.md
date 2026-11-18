# ENISA Software Supply Chain Security Guidelines Alignment

## 1. Overview
The European Union Agency for Cybersecurity (**ENISA**) outlines recommended baseline security requirements for managing supply chain cybersecurity risks.

---

## 2. Compliance Mapping

| ENISA Control | Description | Pipeline Implementation |
|---|---|---|
| **SC-01** | Supplier Risk Assessment | Automated dependency reputation and vulnerability score checks. |
| **SC-02** | Software Integrity Assurance | Cosign cryptographic signatures verified at admission time. |
| **SC-03** | Transparency & Traceability | Comprehensive SPDX/CycloneDX SBOMs generated on every build. |
| **SC-04** | Vulnerability Remediation | Enforced Trivy gates with zero-tolerance for critical CVEs. |
