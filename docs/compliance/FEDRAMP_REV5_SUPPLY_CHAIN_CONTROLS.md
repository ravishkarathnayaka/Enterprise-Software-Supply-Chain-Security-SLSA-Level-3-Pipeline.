# FedRAMP High Revision 5 Baseline: Supply Chain Risk Management (SR)

## Mapped Security Controls
- **SR-3: Supply Chain Controls and Processes**: Strict vendor verification, open-source dependency auditing with OSV-Scanner and Trivy.
- **SR-4: Provenance**: SLSA Build Level 3 non-forgeable provenance generated on isolated GitHub Actions builders.
- **SR-5: Acquisition Strategy, Tools, and Funding**: Automated license compliance audit eliminating non-approved OSS licenses.
- **SI-7: Software, Firmware, and Information Integrity**: Cryptographic signing of build artifacts with Cosign and Sigstore transparency logging.
