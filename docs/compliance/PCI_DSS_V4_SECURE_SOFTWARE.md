# PCI DSS v4.0 Requirement 6: Develop and Maintain Secure Systems and Software

## Control Objectives & Implementation
1. **Requirement 6.2.4: Software Development Vulnerabilities**: SAST analysis with Semgrep scanning for OWASP Top 10 vulnerabilities (CWE-89, CWE-79, CWE-22, CWE-95) on every commit.
2. **Requirement 6.3.1: Security Vulnerability Identification**: Automated container scanning via Trivy integrated into CI blocking Critical and High vulnerabilities.
3. **Requirement 6.3.2: Software Inventory**: CycloneDX machine-readable software inventory (SBOM) tracking all runtime third-party libraries.
