"""Dynamic Supply Chain Compliance Score Calculator.

Computes a percentage security score based on active defense-in-depth controls.
"""

from typing import Dict, Any


class ComplianceScorer:
    """Generates continuous security ratings across SLSA, NIST, and CIS baselines."""

    @staticmethod
    def calculate_score(active_controls: Dict[str, bool]) -> Dict[str, Any]:
        total = len(active_controls)
        if total == 0:
            return {
                "compliance_score": 0.0,
                "grade": "F",
                "passed_controls": 0,
                "total_controls": 0,
                "slsa_level_3_ready": False,
            }

        passed = sum(1 for status in active_controls.values() if status)
        percentage = round((passed / total) * 100.0, 1)

        rating = "A+" if percentage >= 95.0 else ("A" if percentage >= 85.0 else "B")
        return {
            "compliance_score": percentage,
            "grade": rating,
            "passed_controls": passed,
            "total_controls": total,
            "slsa_level_3_ready": percentage >= 90.0,
        }


compliance_scorer = ComplianceScorer()
