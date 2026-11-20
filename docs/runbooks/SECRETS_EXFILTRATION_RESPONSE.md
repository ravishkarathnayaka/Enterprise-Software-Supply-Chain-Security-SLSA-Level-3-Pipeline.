# Operational Runbook: Secrets Exposure & Token Revocation Playbook

## 1. Purpose
Governs emergency response upon discovery of exposed tokens, signing keys, or CI/CD secrets in public git history or logs.

---

## 2. Immediate 15-Minute Containment Checklist
1. **GitHub Organization Tokens**: Invalidate repository `GITHUB_TOKEN` active sessions.
2. **Sigstore Rekor Check**: Review Rekor log for any unauthorized signing events using the compromised identity.
3. **KMS / Cloud IAM**: Rotate associated KMS key aliases and invalidate temporary STS credentials.
4. **Git History Scrub**: Run `git-filter-repo` or BFG Repo-Cleaner to permanently excise credentials from history.
5. **Enforce Force-Push Lockout**: Verify branch protection prevents force-pushing rewritten history without SecOps approval.
