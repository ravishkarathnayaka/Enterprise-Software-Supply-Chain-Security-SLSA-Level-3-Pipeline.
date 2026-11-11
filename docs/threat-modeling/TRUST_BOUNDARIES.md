# Architectural Trust Boundaries & Isolation Zones

## Executive Summary
This document delineates the architectural trust boundaries (TBs) across the end-to-end software delivery lifecycle. Zero Trust principles dictate that every component boundary assumes breach and performs independent cryptographic verification.

---

## Trust Boundary Taxonomy

```
 [TB-1: Workstation] -----> [TB-2: GitHub CI/CD] -----> [TB-3: OCI Registry] -----> [TB-4: Admission] -----> [TB-5: K8s Runtime]
 (GPG Signed Commits)        (Ephemeral Runners)         (Digest immutability)       (Kyverno Gates)          (Distroless Pods)
```

### Trust Boundary 1: Developer Workstation to Git Repository
- **Boundary**: Local developer environment connecting to GitHub enterprise repository.
- **Controls**:
  - Mandatory hardware-backed or passphrase-protected GPG/SSH commit signatures.
  - Linear git history enforced via branch protection rules.
  - Multi-party pull request approvals (minimum 2 independent peer reviewers).

### Trust Boundary 2: Git Repository to GitHub Actions Runner
- **Boundary**: Source code ingestion into the automated CI build environment.
- **Controls**:
  - Isolated, ephemeral virtual machine runners (`ubuntu-latest`).
  - Read-only GitHub token permissions by default (`permissions: contents: read`).
  - Minimal token scopes strictly elevated per-job (`id-token: write` only during signing).

### Trust Boundary 3: CI/CD Runner to OCI Container Registry
- **Boundary**: Pushing compiled artifacts and container images to `ghcr.io`.
- **Controls**:
  - Images pushed using immutable SHA256 content-addressable digests.
  - Mutual TLS (mTLS) transport encryption for all registry communications.
  - Ephemeral short-lived authentication tokens.

### Trust Boundary 4: OCI Registry to Admission Controller (Kyverno)
- **Boundary**: Kubernetes API Server intercepting `Pod` deployment requests.
- **Controls**:
  - Kyverno ValidatingWebhookConfiguration with `failurePolicy: Fail`.
  - Image signature validation via Cosign public trust root or keyless Rekor proofs.
  - Cosign in-toto attestation verification matching the exact commit SHA and workflow source.

### Trust Boundary 5: Admission Controller to Kubernetes Node Runtime
- **Boundary**: Pod execution on physical/virtual worker nodes.
- **Controls**:
  - Pod Security Standards: `restricted` enforcement.
  - Distroless container images with no package managers, shells, or debugging utilities.
  - Read-only root filesystem with ephemeral memory-backed volumes for temporary operations.
