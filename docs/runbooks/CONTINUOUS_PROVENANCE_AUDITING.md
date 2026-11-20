# Operational Runbook: Continuous In-Cluster Provenance Auditing

## 1. Concept
While admission controllers gate image entry at deployment time, **continuous provenance auditing** ensures running workloads maintain cryptographic compliance throughout their entire lifecycle.

---

## 2. Automated Kyverno Background Scans
Kyverno runs continuous background scans every 60 minutes evaluating all active pods against `ClusterPolicy` rules:
```bash
# Query active cluster policy violation reports
kubectl get policyreport,clusterpolicyreport -A -o wide

# Filter for provenance verification failures
kubectl get clusterpolicyreport -o json | jq '.items[].results[] | select(.status == "fail")'
```

---

## 3. Alerting & Remediation
- Any background report indicating signature invalidation generates a high-priority PagerDuty / Slack alert.
- Automated SOAR script cordons affected pods pending forensic memory analysis.
