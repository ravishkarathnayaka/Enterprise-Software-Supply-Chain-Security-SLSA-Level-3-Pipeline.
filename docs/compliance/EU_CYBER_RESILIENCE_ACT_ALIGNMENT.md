# EU Cyber Resilience Act (CRA) Alignment Specification

## Overview
The EU Cyber Resilience Act establishes mandatory cybersecurity requirements for hardware and software products placed on the European Union market.

## Essential Requirements Compliance Matrix
| CRA Requirement | Pipeline Implementation | Verification Evidence |
| :--- | :--- | :--- |
| Annex I, Part I (1): Secure by Default | Distroless minimal base image, non-root user (UID 65532), read-only rootfs | Kyverno policy `require-ro-rootfs` |
| Annex I, Part I (2): Vulnerability Handling | Synchronous Trivy CVE gating on PR merges, automated VEX generation | `generate_vex_statement.py` output |
| Annex I, Part II: Machine-readable SBOM | CycloneDX 1.5 JSON & SPDX 2.3 formats signed with Cosign | `generate_cyclonedx_sbom.sh` |
| Security updates without downtime | Kubernetes zero-downtime rolling updates with PodDisruptionBudgets | `admission-webhook-pdb.yaml` |
