# Operational Runbook: Periodic Cluster Supply Chain Audit

## 1. Objective
Perform weekly and monthly automated audits of all running Kubernetes workloads to guarantee zero unverified, unsigned, or untracked images bypass admission gates.

---

## 2. Audit Execution
```bash
# Extract all running pod images
kubectl get pods --all-namespaces -o jsonpath="{..image}" | tr -s '[[:space:]]' '\n' | sort -u > running_images.txt

# Run batch signature audit script
./scripts/audit_cluster_images.sh running_images.txt
```

---

## 3. Reporting
All unverified images must be quarantined and investigated within 2 hours of audit completion.
