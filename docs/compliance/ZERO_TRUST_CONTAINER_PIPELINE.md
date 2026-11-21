# DoD Zero Trust Reference Architecture 2.0: Container Pipeline

## 1. Target Pillar Mappings
- **Pillar 1: User**: Short-lived GitHub Actions OIDC identity tokens; no persistent secrets.
- **Pillar 2: Device**: Ephemeral isolated virtual machine build runners.
- **Pillar 3: Application & Workload**: Distroless runtime, SLSA Level 3 provenance, and Kyverno admission controls.
- **Pillar 4: Network**: Micro-segmented default-deny NetworkPolicies.
