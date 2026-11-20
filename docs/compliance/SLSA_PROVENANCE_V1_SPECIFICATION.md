# SLSA Provenance v1.0 Specification & Schema Migration

## 1. Background
SLSA v1.0 divides provenance into Build, Source, and Common specifications, superseding v0.2.

---

## 2. SLSA v1.0 Predicate Format
```json
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [{"name": "enterprise-supply-chain-app", "digest": {"sha256": "..."}}],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "buildDefinition": {
      "buildType": "https://actions.github.com/v1",
      "externalParameters": {"workflow": ".github/workflows/security-pipeline.yml"},
      "internalParameters": {"github": {"actor": "ravishkarathnayaka"}},
      "resolvedDependencies": []
    },
    "runDetails": {
      "builder": {"id": "https://github.com/actions/runner"},
      "metadata": {"invocationId": "..."}
    }
  }
}
```
