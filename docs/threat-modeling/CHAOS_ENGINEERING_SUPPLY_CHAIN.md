# Chaos Engineering Experiments for Supply Chain Resilience

## 1. Overview
Validates pipeline and admission controller fault-tolerance under adversarial and infrastructure degradation conditions.

---

## 2. Experiment Catalog
- **EXP-01: Sigstore Rekor Unavailability**: Simulates network timeout to public Rekor. Validates Kyverno webhook fail-closed behavior.
- **EXP-02: OCI Registry Latency Spike**: Introduces 10-second artificial delay on image digest pulls. Validates webhook timeout safeguards.
- **EXP-03: Corrupted Attestation Envelope**: Modifies a single byte in the in-toto payload. Verifies cryptographic signature failure detection.
