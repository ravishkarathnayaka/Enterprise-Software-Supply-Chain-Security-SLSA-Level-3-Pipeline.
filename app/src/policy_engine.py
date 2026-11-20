"""Lightweight Policy-as-Code Evaluation Engine.

Validates microservice operational metadata against enterprise governance rules.
"""

from typing import Dict, Any


class PolicyRuleEngine:
    """Executes declarative security posture checks."""

    @staticmethod
    def evaluate_slsa_posture(metadata: Dict[str, Any]) -> Dict[str, Any]:
        required_keys = ["slsa_level", "signed_by", "rekor_verified"]
        missing = [k for k in required_keys if k not in metadata]

        is_l3 = metadata.get("slsa_level") == "SLSA_BUILD_LEVEL_3"
        valid = len(missing) == 0 and is_l3 and metadata.get("rekor_verified") is True

        return {
            "compliant": valid,
            "slsa_level": metadata.get("slsa_level", "NONE"),
            "status": "COMPLIANT" if valid else "NON_COMPLIANT",
            "missing_attributes": missing,
        }


policy_engine = PolicyRuleEngine()
