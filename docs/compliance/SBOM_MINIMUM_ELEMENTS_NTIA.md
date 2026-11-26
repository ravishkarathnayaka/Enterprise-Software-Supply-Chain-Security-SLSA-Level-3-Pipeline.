# NTIA Minimum Elements for Software Bill of Materials (SBOM) Alignment

## Scope & Compliance Baseline
Pursuant to Executive Order 14028, this pipeline strictly implements the 7 minimum data fields mandated by the National Telecommunications and Information Administration (NTIA):

| NTIA Minimum Field | CycloneDX Representation | SPDX Representation | Pipeline Enforcement |
| :--- | :--- | :--- | :--- |
| Supplier Name | `component.supplier` | `PackageSupplier` | Mandatory in CI Generator |
| Component Name | `component.name` | `PackageName` | Parsed from lockfile |
| Version of Component | `component.version` | `PackageVersion` | Pinned exact SemVer |
| Other Unique Identifiers | `component.purl` | `PackageExternalRef` | Package URL (PURL) spec |
| Dependency Relationship | `dependencies[].dependsOn` | `Relationship: DEPENDS_ON` | Direct and transitive |
| Author of SBOM Data | `metadata.authors` | `Creator` | GitHub Actions Hermetic Runner |
| Timestamp | `metadata.timestamp` | `Created` | ISO-8601 UTC timestamp |
