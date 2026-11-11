# Cryptographic Key Revocation & Compromise Procedure

## 1. Overview
In the event that a private signing key, KMS credential, or repository identity is suspected of compromise, this runbook outlines the emergency revocation steps to prevent unauthorized artifacts from being accepted by admission controllers.

---

## 2. Emergency Revocation Checklist

### Step 1: Invalidate Current Public Keys in Kyverno
Immediately patch the `ClusterPolicy` in the target Kubernetes clusters to reject signatures from the compromised key:
```bash
kubectl patch clusterpolicy kyverno-verify-image \
  --type='json' \
  -p='[{"op": "replace", "path": "/spec/rules/0/verifyImages/0/key", "value": "REVOKED"}]'
```

### Step 2: Revoke Static Cosign Keys in KMS
If AWS KMS / GCP KMS is used:
- Disable the key immediately:
  ```bash
  aws kms disable-key --key-id <compromised-key-id>
  ```
- Schedule key deletion after 7 days quarantine.

### Step 3: Revoke GitHub Actions OIDC Trust
If GitHub repository tokens were compromised:
- Rotate all repository secrets and deploy keys:
  ```bash
  gh secret remove COSIGN_PRIVATE_KEY
  gh secret remove GITHUB_TOKEN
  ```
- Trigger a global session invalidation for repository administrators.

### Step 4: Audit Transparency Log (Rekor)
Query Rekor for all signatures generated during the suspected compromise window:
```bash
rekor-cli search --email "188481361+ravishkarathnayaka@users.noreply.github.com"
```
Tag and blacklist any unauthorized artifact hashes identified in the query results.
