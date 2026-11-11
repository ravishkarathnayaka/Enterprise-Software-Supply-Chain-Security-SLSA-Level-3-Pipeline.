# In-Toto Attestation Predicate Schema & Metadata

## 1. Concept Architecture
The **in-toto** attestation framework provides a verifiable claim that a software artifact was generated in accordance with specified build steps, policies, and environments.

---

## 2. In-Toto Statement Envelope

```json
{
  "_type": "https://in-toto.io/Statement/v0.1",
  "subject": [
    {
      "name": "ghcr.io/ravishkarathnayaka/enterprise-supply-chain-app",
      "digest": {
        "sha256": "7a356cb67a9cf582310ab46e8f49890539fb0426b69cfd7b278783e44be33c5e"
      }
    }
  ],
  "predicateType": "https://slsa.dev/provenance/v0.2",
  "predicate": {
    "builder": {
      "id": "https://github.com/ravishkarathnayaka/Enterprise-Software-Supply-Chain-Security-SLSA-Level-3-Pipeline/actions/runs/..."
    },
    "buildType": "https://github.com/actions/runner/v1",
    "invocation": {
      "configSource": {
        "uri": "git+https://github.com/ravishkarathnayaka/Enterprise-Software-Supply-Chain-Security-SLSA-Level-3-Pipeline",
        "digest": {
          "sha1": "7ba94e1e912..."
        },
        "entryPoint": ".github/workflows/security-pipeline.yml"
      }
    }
  }
}
```
