# Software Bill of Materials (SBOM) Format Specifications

## Overview
A Software Bill of Materials (**SBOM**) is a formal, machine-readable inventory of software components, dependencies, and hierarchical relationships.

---

## Supported Specifications

### 1. CycloneDX v1.5 (JSON)
- **Standard**: OWASP CycloneDX Specification
- **Primary Use**: Dependency analysis, vulnerability scanning, and license compliance.
- **Schema Attributes**:
  - `bomFormat`: "CycloneDX"
  - `specVersion`: "1.5"
  - `metadata.component`: Top-level microservice container image.
  - `components[]`: Every installed OS package (Debian) and Python wheel package.
  - `components[].purl`: Package URL format (`pkg:deb/debian/libssl3@3.0.11`, `pkg:pypi/fastapi@0.110.0`).

### 2. SPDX v2.3 (JSON / Tag-Value)
- **Standard**: ISO/IEC 5962:2021
- **Primary Use**: Federal compliance, intellectual property licensing, and long-term archival.
- **Schema Attributes**:
  - `spdxVersion`: "SPDX-2.3"
  - `dataLicense`: "CC0-1.0"
  - `packages[].licenseConcluded`: Extracted SPDX license identifier.
  - `relationships[]`: `DEPENDS_ON` and `DESCRIBES` relationships.

---

## Verification & Extraction Command
```bash
# Download and view attached SBOM from registry
cosign download sbom ghcr.io/ravishkarathnayaka/enterprise-supply-chain-app@sha256:...
```
