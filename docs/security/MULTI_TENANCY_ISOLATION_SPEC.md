# Multi-Tenancy Isolation & Soft Multitenancy Architecture

## 1. Overview
Ensures microservices running within shared Kubernetes clusters are strictly partitioned across compute, network, and storage planes.

---

## 2. Isolation Controls
1. **Namespace Boundary**: Workload deployed strictly to dedicated `secure-supply-chain` namespace.
2. **Network Isolation**: Strict default-deny ingress and egress NetworkPolicies prevent cross-namespace lateral movement.
3. **Resource Fair-Share**: `ResourceQuota` and `LimitRange` prevent rogue workloads from starving neighboring namespaces.
4. **ServiceAccount Token Defense**: `automountServiceAccountToken: false` disables default token mounts.
