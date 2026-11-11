# Supply Chain Attack Trees & Defense-in-Depth

## Overview
Attack trees represent visual and logical graphs of attack vectors targeting our enterprise supply chain pipeline. Each tree details the adversary objective, leaf attacks, and corresponding pipeline defense gates.

---

## Attack Tree 1: Compromise Container Image in Production Cluster

```
Goal: Execute Malicious Container in Production Cluster
â”œâ”€â”€ 1. Deploy Unsigned Image Directly to K8s
â”‚   â””â”€â”€ Defense: Kyverno admission policy blocks any image lacking valid Cosign signature.
â”œâ”€â”€ 2. Bypass Admission Webhook
â”‚   â”œâ”€â”€ 2.1 Disable Validating Webhook Configuration
â”‚   â”‚   â””â”€â”€ Defense: K8s RBAC disallows mutation of ClusterPolicy/ValidatingWebhook by standard users.
â”‚   â””â”€â”€ 2.2 Network Partition Webhook (force open)
â”‚       â””â”€â”€ Defense: Webhook failurePolicy set to 'Fail' (closed).
â”œâ”€â”€ 3. Forged Cosign Signature
â”‚   â”œâ”€â”€ 3.1 Steal Private Signing Key
â”‚   â”‚   â””â”€â”€ Defense: Keyless Fulcio/Rekor signing eliminates long-lived static private keys entirely.
â”‚   â””â”€â”€ 3.2 Compromise GitHub OIDC Identity
â”‚       â””â”€â”€ Defense: Verification validates exact repository, ref, and workflow identity claims in SAN.
â””â”€â”€ 4. Supply Chain Dependency Injection
    â”œâ”€â”€ 4.1 Dependency Confusion / Typo-squatting
    â”‚   â””â”€â”€ Defense: Locked dependency hashes in requirements.txt with Pip hash verification.
    â””â”€â”€ 4.2 Malicious Upstream Maintainer Update
        â””â”€â”€ Defense: Trivy SCA scans and Renovate/Dependabot automated regression verification gates.
```

---

## Attack Tree 2: Build Environment Tampering (SLSA L3 Focus)

```
Goal: Modify Artifact During Build Phase without Detection
â”œâ”€â”€ 1. Tamper with Build Script on Ephemeral Runner
â”‚   â””â”€â”€ Defense: Ephemeral runners spawned fresh per build; in-toto provenance cryptographically records runner environment.
â”œâ”€â”€ 2. Inject Code via GitHub Action Dependency
â”‚   â””â”€â”€ Defense: All 3rd-party actions pinned to immutable 40-character commit SHAs; Semgrep rules enforce pinning.
â””â”€â”€ 3. Modify Attestation Post-Build
    â””â”€â”€ Defense: In-toto attestations signed with Cosign and published to Rekor transparency log; immutable.
```
