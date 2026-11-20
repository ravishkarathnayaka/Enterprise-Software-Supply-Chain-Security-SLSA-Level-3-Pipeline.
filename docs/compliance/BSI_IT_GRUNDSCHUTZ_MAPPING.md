# BSI IT-Grundschutz: Supply Chain Security Compliance Mapping

## 1. Overview
The German Federal Office for Information Security (**BSI**) defines baseline security standards through IT-Grundschutz modules.

---

## 2. IT-Grundschutz Module Alignment
- **OPS.1.1.5 (Logging)**: JSON structured logs with correlation IDs and immutable Rekor transparency logging.
- **CON.8 (Software Development)**: Enforced static analysis (Semgrep), secrets scanning (Gitleaks), and peer review controls.
- **APP.4.4 (Kubernetes Security)**: Hardened pods with dropped Linux capabilities and Kyverno admission controls.
