# Zero Trust Immutable Container Lifecycle & Provenance Enforcement

## Architectural Lifecycle Stages
Every production container artifact progresses through an immutable lifecycle:

```mermaid
flowchart LR
    A["Code Commit (GPG)"] --> B["Isolated Hermetic Build"]
    B --> C["SLSA L3 Provenance"]
    C --> D["Sigstore Cosign Signing"]
    D --> E["Rekor Merkle Log"]
    E --> F["Admission Webhook (Kyverno)"]
    F --> G["Enforced Runtime (Distroless)"]
```

## Key Invariants
1. **Never Trust Tags**: Images are referenced solely by immutable cryptographic SHA-256 digests.
2. **Keyless Ephemeral Identity**: Cosign leverages Fulcio OIDC short-lived certificates tied to GitHub Actions OIDC claims.
3. **Transparency Logging**: Every signing event publishes an immutable inclusion proof to Sigstore Rekor before artifact promotion.
