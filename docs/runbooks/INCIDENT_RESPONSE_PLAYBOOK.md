# Incident Response Playbook: Supply Chain Security (IRP-01)

## 1. Purpose & Scope
This incident response playbook governs security alerts originating from supply chain events, including:
- Detection of unsigned or unverified container images attempting cluster admission.
- Failure of in-toto SLSA provenance verification.
- Critical vulnerability zero-day disclosure in upstream base images or Python libraries.
- Discrepancies between build provenance and deployed runtime digests.

---

## 2. Incident Severity Levels

- **SEV-1 (Critical)**: Active breach detected; malicious image running in cluster; compromised GitHub token or signing identity.
- **SEV-2 (High)**: Blocked admission attempt of tampered or unsigned container in production; CRITICAL CVE actively exploited in the wild.
- **SEV-3 (Medium)**: Trivy/Semgrep gate failure in CI; signature verification failure in staging.
- **SEV-4 (Low)**: Expired attestation certificate; non-exploitable LOW/MEDIUM CVE.

---

## 3. Step-by-Step Response Procedure

### Phase 1: Containment
1. If an untrusted pod bypassed admission, cordon and drain affected nodes immediately:
   ```bash
   kubectl cordon <node-name>
   kubectl drain <node-name> --delete-emptydir-data --force --ignore-daemonsets
   ```
2. Isolate the pod via NetworkPolicy:
   ```bash
   kubectl label namespace secure-supply-chain isolation=quarantine --overwrite
   ```

### Phase 2: Eradication
1. Delete the compromised Deployment/Pod:
   ```bash
   kubectl delete pod <pod-name> -n secure-supply-chain --grace-period=0 --force
   ```
2. Revoke any active GitHub Actions OIDC sessions or personal access tokens in the organization settings.

### Phase 3: Recovery
1. Re-run clean build pipeline with verified commit hash.
2. Verify image signature and attestation on Rekor transparency log.
3. Redeploy through standard Kyverno admission gates.

### Phase 4: Post-Mortem
- Conduct root cause analysis within 48 hours. Document lessons learned and update Kyverno rules or Semgrep policies accordingly.
