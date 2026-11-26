# Incident Response Playbook: Compromised CI/CD Runner / Builder Node

## Severity: P0 - Critical
## Detection Triggers
- Gitleaks detects leaked runner credentials or CI tokens in public transparency logs.
- Unexpected network egress from runner during container build phase.
- Discrepancy detected between source git SHA and SLSA provenance material hashes.

## Immediate Containment Actions
1. **Revoke Runner Tokens**: Invalidate GitHub Actions runner registration tokens immediately.
2. **Quarantine Artifacts**: Mark candidate container digests as untrusted in registry catalog.
3. **Invalidate Sigstore Attestations**: Publish revocation notice to Rekor transparency log.
4. **Trigger Hermetic Rebuild**: Rebuild release candidates on clean, isolated hardware runners.
