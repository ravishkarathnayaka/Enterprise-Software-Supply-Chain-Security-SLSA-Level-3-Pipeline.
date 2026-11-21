# Purple Team Exercise Guide: Validating Admission Controls

## 1. Objective
Collaborative offensive and defensive testing of Kyverno policy enforcement and Cosign signature verification mechanisms.

---

## 2. Exercise Scenarios
1. **Red Team Action**: Attempt deploying an unsigned container image directly using `kubectl run`.
   - **Blue Team Validation**: Confirm Kyverno webhook intercepts request and outputs rejection event to audit log.
2. **Red Team Action**: Tamper with base image OS package without updating lockfile.
   - **Blue Team Validation**: Trivy SCA gate halts CI pipeline before build completion.
