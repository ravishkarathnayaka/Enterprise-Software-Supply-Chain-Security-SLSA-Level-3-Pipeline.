# ISO/IEC 27001:2022 Control 8.28: Secure Coding Mapping

## 1. Scope
Cross-references pipeline capabilities against ISO/IEC 27001:2022 Annex A Control 8.28 (Secure Coding Guidelines).

---

## 2. Control Matrix
- **A.8.28.1 (Coding Standards)**: Enforced via Ruff / Flake8 and Semgrep OWASP rulesets.
- **A.8.28.2 (Pre-Commit & CI Gates)**: Git hooks, Gitleaks secret scans, automated test execution.
- **A.8.28.3 (Component Security)**: Pinned dependencies, automated Dependabot regression testing.
