# DISA Kubernetes Security Technical Implementation Guide (STIG)

## 1. Scope
Department of Defense (DoD) DISA STIG requirements for containerized workloads.

---

## 2. Key STIG Controls Verified
- **V-242414**: Containers must run with a non-root user ID.
- **V-242415**: Containers must drop all default capabilities.
- **V-242417**: Containers must have read-only root filesystems.
- **V-242418**: Host networking, IPC, and PID namespaces must be disabled.
- **V-242422**: Automated image vulnerability scanning before cluster admission.
