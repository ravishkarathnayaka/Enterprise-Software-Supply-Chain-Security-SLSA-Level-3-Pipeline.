# Software Supply Chain SLA & Patching Lifecycle Policy

## 1. Base Image Refresh Cadence
- Distroless Debian 12 base images must be automatically re-scanned and rebuilt weekly.
- Any critical base image patch must be deployed to production within **24 hours**.

---

## 2. Dependency Vulnerability SLA Matrix
- **CRITICAL (CVSS >= 9.0)**: Fixed within 24 hours. Pipeline build blocks immediately.
- **HIGH (CVSS 7.0 - 8.9)**: Fixed within 7 calendar days.
- **MEDIUM (CVSS 4.0 - 6.9)**: Evaluated in next bi-weekly sprint.
- **LOW (CVSS 0.1 - 3.9)**: Addressed in quarterly maintenance cycle.
