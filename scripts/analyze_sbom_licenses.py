#!/usr/bin/env python3
"""Audit CycloneDX SBOM components for copyleft or unapproved licenses."""

import json
import sys

ALLOWED = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC"}


def audit_sbom(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    components = data.get("components", [])
    violations = []
    for c in components:
        name = c.get("name")
        licenses = [l.get("license", {}).get("id") for l in c.get("licenses", [])]
        for lic in licenses:
            if lic and lic not in ALLOWED:
                violations.append((name, lic))
    if violations:
        print(f"License violations found: {violations}")
        return 1
    print("All SBOM component licenses approved.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: analyze_sbom_licenses.py <sbom.json>")
        sys.exit(0)
    sys.exit(audit_sbom(sys.argv[1]))
