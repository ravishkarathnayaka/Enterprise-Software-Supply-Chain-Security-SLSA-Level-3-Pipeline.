# Adversary Emulation Plan: Supply Chain Attack Scenarios

## 1. Scenario 1: SolarWinds-Style Build Step Injection (UNC2452)
- **Objective**: Simulate covert modification of compiled binaries between checkout and packaging.
- **Simulation**: Inject a benign test string into a source file during the build container step.
- **Expected Outcome**: In-toto provenance attestation records the unexpected runner artifact hash drift, blocking deployment at the admission controller.

---

## 2. Scenario 2: Codecov-Style Runner Credential Exfiltration
- **Objective**: Simulate exfiltration of environment tokens via malicious curl invocation in CI.
- **Simulation**: Introduce an unauthorized curl outbound request in pipeline step.
- **Expected Outcome**: Egress firewall blocks non-whitelisted outbound network connections from runners; Gitleaks flags exposed tokens.

---

## 3. Scenario 3: 3CX-Style Multi-Stage Upstream Library Tampering
- **Objective**: Simulate loading a secondary malicious payload via a transitive Python dependency.
- **Simulation**: Reference an unpinned transitive library with modified cryptographic checksum.
- **Expected Outcome**: Pip hash checking failure halts container build step immediately.
