# High-Assurance Runtime Sandboxing: gVisor & MicroVMs

## 1. Motivation
Standard Linux container isolation relies on shared host kernel namespaces. High-risk multi-tenant microservices require user-space kernel sandboxing.

---

## 2. Architecture
- **RuntimeClass**: Configured via Kubernetes `RuntimeClass` pointing to `gVisor (runsc)`.
- **Syscall Filtering**: gVisor intercepts and handles over 300 Linux syscalls in user-space, preventing kernel exploits.
```yaml
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: gvisor
handler: runsc
```
