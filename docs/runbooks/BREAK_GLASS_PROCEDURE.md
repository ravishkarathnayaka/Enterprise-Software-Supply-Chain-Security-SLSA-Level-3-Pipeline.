# Emergency Admission Bypass Protocol (Break-Glass Procedure)

## 1. Purpose
During catastrophic infrastructure emergencies (e.g., global Sigstore Rekor downtime, failure of the admission webhook infrastructure), an authorized emergency bypass protocol ("Break-Glass") allows deploying critical patches without admission controller disruption.

---

## 2. Authorization Requirements
- Must be approved by at least **two authorized Security Officers**.
- Valid only for a maximum duration of **4 hours**.
- Must generate an immutable, high-priority SIEM audit alert.

---

## 3. Execution Steps

### Step 1: Temporarily Switch Webhook Failure Policy
Switch Kyverno validating webhook from `Fail` (closed) to `Ignore` (open) for emergency maintenance:
```bash
kubectl patch validatingwebhookconfiguration kyverno-resource-validating-webhook-cfg \
  --type='json' \
  -p='[{"op": "replace", "path": "/webhooks/0/failurePolicy", "value": "Ignore"}]'
```

### Step 2: Annotate Emergency Deployments
All emergency manifests deployed under break-glass conditions must carry explicit audit annotations:
```yaml
metadata:
  annotations:
    security.enterprise.io/break-glass: "true"
    security.enterprise.io/incident-ticket: "INC-88992"
    security.enterprise.io/authorized-by: "secops-lead"
    security.enterprise.io/expiry-timestamp: "2026-11-11T16:00:00Z"
```

### Step 3: Restore Enforcing Posture Immediately
Once emergency maintenance is complete, restore the webhook failure policy to `Fail`:
```bash
kubectl patch validatingwebhookconfiguration kyverno-resource-validating-webhook-cfg \
  --type='json' \
  -p='[{"op": "replace", "path": "/webhooks/0/failurePolicy", "value": "Fail"}]'
```
Run an audit scan to ensure all running workloads comply with baseline signature policies.
