# Supply Chain Threat Matrix: MITRE ATT&CK for ICS/Enterprise & STRIDE

## Scope and Threat Vector Taxonomy
This document maps common and advanced software supply chain attack surfaces across source control, CI/CD runners, container registries, and runtime Kubernetes environments against MITRE ATT&CK tactics and STRIDE modeling.

| Threat Category | STRIDE Vector | MITRE Technique | Defense Mechanism | Validation Control |
| :--- | :--- | :--- | :--- | :--- |
| Malicious Source Injection | Tampering / Spoofing | T1195.001 | Mandatory GPG / SSH Commit Signing, Protected Main Branch | GitHub Branch Protection Rule GH013 |
| Compromised Build Runner | Elevation of Privilege | T1195.002 | Ephemeral Isolated Runners, SLSA Level 3 Provenance | In-toto Provenance Attestation & Sigstore Rekor |
| Dependency Confusion / Typosquatting | Spoofing / Tampering | T1195.001 | Private Artifact Mirror, SHA-512 Pinned Hashes, SBOM Lock | CycloneDX & SPDX Lockfile Integrity Scan |
| Registry Tag Poisoning | Tampering | T1525 | Cosign Keyless Image Signing, Mutating Digest Enforcement | Kyverno `require-image-digest` Admission Policy |
| Container Runtime Escape | Elevation of Privilege | T1611 | PSS Restricted, Seccomp `RuntimeDefault`, Read-only RootFS | Falco System Call Telemetry & Kyverno Enforce |
