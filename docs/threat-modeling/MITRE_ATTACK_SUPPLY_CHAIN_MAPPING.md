# MITRE ATT&CK Framework Mapping: Software Supply Chain Defense

## 1. Scope & Objective
This document maps our supply chain security architecture, Cosign cryptographic gates, and Kyverno admission controls against the **MITRE ATT&CK for Enterprise Matrix**, specifically addressing supply chain compromise techniques.

---

## 2. ATT&CK Technique Mapping Matrix

| MITRE ATT&CK ID | Technique Name | Adversary Vector | Pipeline Defensive Control | Verification Mechanism |
|---|---|---|---|---|
| **T1195.001** | Supply Chain Compromise: Compromise Software Dependencies | Poisoning open-source PyPI packages or Docker base images | Strict SHA-256 hash pinning in `requirements.txt`; Trivy SCA vulnerability gates | Stage 3 CI Gate |
| **T1195.002** | Supply Chain Compromise: Compromise Software Supply Chain | Tampering with build tooling or GitHub Actions runners | Ephemeral Ubuntu runners; Cosign keyless in-toto SLSA L3 provenance attestations | Fulcio / Rekor Transparency Log |
| **T1195.003** | Supply Chain Compromise: Compromise Development Tools | Backdooring compiler, IDE, or CI plugin components | Pinned action SHAs (`@<full-40-char-sha>`); Semgrep custom workflow rules | Stage 2 Semgrep Scan |
| **T1565.002** | Data Manipulation: Transmitted Data Manipulation | Man-in-the-Middle tampering of images in transit from registry to K8s | Mutually authenticated TLS; Kyverno cryptographic Cosign signature verification | Validating Admission Webhook |
| **T1610** | Deploy Container | Unauthorized deployment of rogue or backdoored container image | Default-deny Kyverno ClusterPolicy blocking all unsigned images | Kyverno `verifyImages` Rule |
| **T1611** | Escape to Host | Container breakout via privilege escalation or host volume mounting | Distroless runtime; `runAsNonRoot: true`; read-only rootfs; drop all Linux capabilities | Kyverno PSS-Restricted Rules |
