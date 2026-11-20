# Software Material Traceability: Commit to Pod Lineage

## 1. Lineage Graph
Every container running in our production clusters maintains an unbroken cryptographic thread:
```
Git Commit SHA ──► GitHub Run ID ──► Distroless Layer SHA256 ──► In-Toto Attestation ──► Kyverno Admission Audit
```

---

## 2. Traceability Verification Steps
Given any running pod in the cluster:
1. Extract image digest: `kubectl get pod <pod> -o jsonpath="{.status.containerStatuses[0].imageID}"`
2. Extract signed in-toto attestation from OCI registry via Cosign.
3. Validate builder ID and commit SHA recorded in provenance match the official git log.
