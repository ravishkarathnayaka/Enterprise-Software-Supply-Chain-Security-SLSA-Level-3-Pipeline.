# CIS Kubernetes Benchmark v1.8: Pod Security Checklist

## Scope
This checklist cross-references the Kubernetes workload configurations and Kyverno admission policies against the **Center for Internet Security (CIS) Kubernetes Benchmark v1.8 Section 5 (Pod Security)**.

---

## CIS Benchmark Controls Matrix

| CIS Control | Description | Status | Implementation Mechanism |
|---|---|---|---|
| **5.1.1** | Minimize admission of privileged containers | **COMPLIANT** | `kyverno-disallow-privilege-escalation.yaml` |
| **5.1.2** | Minimize admission of containers wishing to share the host process ID namespace | **COMPLIANT** | `kyverno-disallow-host-namespaces.yaml` |
| **5.1.3** | Minimize admission of containers wishing to share the host IPC namespace | **COMPLIANT** | `kyverno-disallow-host-namespaces.yaml` |
| **5.1.4** | Minimize admission of containers wishing to share the host network namespace | **COMPLIANT** | `kyverno-disallow-host-namespaces.yaml` |
| **5.1.5** | Minimize admission of containers with `allowPrivilegeEscalation` | **COMPLIANT** | Deployment spec enforces `allowPrivilegeEscalation: false` |
| **5.1.6** | Minimize admission of root containers | **COMPLIANT** | `runAsNonRoot: true`, `runAsUser: 65532` |
| **5.1.7** | Minimize admission of containers with dangerous Linux capabilities | **COMPLIANT** | `capabilities.drop: ["ALL"]` |
| **5.2.1** | Ensure default namespace is not used | **COMPLIANT** | Dedicated namespace `secure-supply-chain` |
| **5.3.1** | Ensure Network Policies are established | **COMPLIANT** | Default-deny ingress/egress NetworkPolicy |
| **5.4.1** | Minimize default ServiceAccount token automounting | **COMPLIANT** | `automountServiceAccountToken: false` |
