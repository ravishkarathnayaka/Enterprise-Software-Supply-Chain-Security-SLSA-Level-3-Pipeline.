# Operational Runbook: Kyverno Admission Disaster Recovery

## 1. Overview
In the event of a catastrophic failure in the Kubernetes admission webhook infrastructure (e.g., Kyverno pod crash-loops, webhook TLS certificate expiration, API server communication timeouts), follow this procedure to restore cluster operations safely.

---

## 2. Diagnostics
```bash
# Inspect admission webhook status
kubectl get validatingwebhookconfigurations kyverno-resource-validating-webhook-cfg

# Check Kyverno controller logs
kubectl logs -n kyverno -l app.kubernetes.io/name=kyverno --tail=100
```

---

## 3. Safe Recovery Protocol
1. Verify TLS secret validity for webhook endpoints.
2. If certificates are expired, trigger `cert-manager` certificate renewal:
   ```bash
   kubectl delete secret kyverno-svc -n kyverno
   ```
3. Restart Kyverno controller deployment:
   ```bash
   kubectl rollout restart deployment/kyverno -n kyverno
   ```
