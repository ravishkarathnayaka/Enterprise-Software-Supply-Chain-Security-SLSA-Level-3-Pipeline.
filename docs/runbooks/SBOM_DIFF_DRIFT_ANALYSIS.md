# Operational Runbook: SBOM Drift & Dependency Diff Analysis

## 1. Purpose
Detect unintended transitive dependency updates, license modifications, or package additions between successive production builds.

---

## 2. Automated SBOM Comparison
```bash
# Compare previous release SBOM with candidate release SBOM
syft-diff release-v1.0.0-sbom.json candidate-sbom.json --output markdown > diff.md
```

---

## 3. Review Criteria
- **Flagged Items**:
  - Any new package without explicit pull request declaration.
  - License shifts from permissive (MIT/Apache-2.0) to copyleft (GPL-3.0/AGPL).
  - Unannounced binary blob inclusions.
