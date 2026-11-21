"""SBOM Component License Policy & Copyleft Risk Evaluator.

Classifies packages into Permissive, Weak Copyleft, and Viral Copyleft categories.
"""

from typing import Any, Dict, List


class LicenseRiskScanner:
    """Identifies licensing liabilities across installed components."""

    PERMISSIVE = {"MIT", "Apache-2.0", "BSD-3-Clause", "BSD-2-Clause", "ISC"}
    VIRAL_COPYLEFT = {"GPL-3.0", "GPL-2.0", "AGPL-3.0", "SSPL-1.0"}

    @classmethod
    def evaluate_licenses(cls, components: List[Dict[str, str]]) -> Dict[str, Any]:
        flagged: List[Dict[str, str]] = []
        compliant_count = 0

        for c in components:
            lic = c.get("license", "UNKNOWN")
            if lic in cls.VIRAL_COPYLEFT:
                flagged.append({"name": c.get("name", "unknown"), "license": lic, "risk": "HIGH_COPYLEFT"})
            else:
                compliant_count += 1

        is_clean = len(flagged) == 0
        return {
            "compliant": is_clean,
            "total_packages": len(components),
            "compliant_packages": compliant_count,
            "flagged_count": len(flagged),
            "flagged_packages": flagged,
        }


license_scanner = LicenseRiskScanner()
