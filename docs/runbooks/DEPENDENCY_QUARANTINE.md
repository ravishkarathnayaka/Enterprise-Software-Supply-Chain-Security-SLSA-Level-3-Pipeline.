# Operational Runbook: Upstream Dependency Quarantine

## 1. Trigger Conditions
- Discovery of a compromised package, typosquatting attack, or maintainer account takeover in PyPI.
- Trivy/OSV alert with CVSS score >= 9.0 affecting transitive dependencies.
- Cryptographic hash mismatch between published wheel and registry metadata.

---

## 2. Automated Quarantine Workflow
1. **Blacklist in Dependency Proxy**: Immediately configure the artifact caching proxy (e.g., Nexus/Artifactory) to block downloading the target package version.
2. **Revoke Local Builds**: Halt active GitHub Actions workflows referencing the quarantined package.
3. **Trigger Surgical Patch Bot**: Generate an automated pull request with pinned safe alternatives or patches.
4. **Invalidate Build Caches**: Flush GitHub Actions runner dependency caches to purge tainted wheels.
