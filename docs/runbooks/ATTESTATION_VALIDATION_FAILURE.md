# Operational Runbook: In-Toto Attestation Failure Troubleshooting

## 1. Failure Categories
- **Type 1: Predicate Type Mismatch**: The image attestation uses `https://slsa.dev/provenance/v0.1` while policy mandates `v0.2`.
- **Type 2: Identity Claim Drift**: Workflow identity in Rekor does not match the admission policy regexp.
- **Type 3: Hash Inconsistency**: SHA256 digest of container image does not match the in-toto `subject.digest`.

---

## 2. Debugging Steps
```bash
# Download raw attestation payload
cosign download attestation ghcr.io/ravishkarathnayaka/app@sha256:... > attestation.json

# Decode and inspect in-toto payload
cat attestation.json | jq -r '.payload' | base64 -d | jq .
```
Verify that `predicate.builder.id` and `invocation.configSource.uri` match expected repository values.
