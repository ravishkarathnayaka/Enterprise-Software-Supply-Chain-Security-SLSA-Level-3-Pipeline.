# Open Source Software Bill of Rights & Vendor Tiering Criteria

## Guiding Principles
Enterprise workloads must only consume external dependencies that satisfy rigorous provenance and maintenance standards:

## Vendor & Dependency Tiering
- **Tier 1 (Core Foundation)**: Maintained by recognized foundations (Apache, Linux Foundation, CNCF, Python Software Foundation). Minimum OpenSSF Scorecard >= 8.0.
- **Tier 2 (Enterprise Commercial)**: Supported by commercial vendors with contractual SLAs and vulnerability disclosure programs.
- **Tier 3 (Community Maintained)**: Evaluated per-release; requires dual-maintainer review, pinned SHA digests, and license allowlist validation.
- **Tier 4 (Unmaintained / High Risk)**: Strictly prohibited from production deployment.
