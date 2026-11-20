# FedRAMP Rev 5: Software Supply Chain Control Baseline

## 1. Overview
Federal Risk and Authorization Management Program (**FedRAMP**) Rev 5 incorporates NIST SP 800-53 Rev 5 supply chain security families.

---

## 2. Control Cross-Reference
- **SR-3 (Supply Chain Controls & Processes)**: Automated SBOM generation in CycloneDX/SPDX formats.
- **SA-4 (Acquisition Process)**: Third-party component vulnerability tracking via Trivy.
- **SA-11 (Developer Testing & Evaluation)**: Automated SAST and unit test suites running in isolated CI runners.
- **SI-7 (Software & Firmware Integrity)**: Cosign cryptographic attestation validation at the admission webhook.
