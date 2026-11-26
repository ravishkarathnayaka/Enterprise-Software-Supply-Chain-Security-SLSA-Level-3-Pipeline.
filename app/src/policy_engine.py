"""Dynamic Microservice Policy Admission Engine.

Evaluates arbitrary workload specifications against active enterprise admission rules.
"""

from typing import Any, Dict, List


class AdmissionPolicyEngine:
    """In-memory admission rule evaluation engine."""

    REQUIRED_LABELS = ["app.kubernetes.io/name", "app.kubernetes.io/part-of"]

    @classmethod
    def evaluate(cls, manifest: Dict[str, Any]) -> Dict[str, Any]:
        violations: List[str] = []
        labels = manifest.get("metadata", {}).get("labels", {})
        for req in cls.REQUIRED_LABELS:
            if req not in labels:
                violations.append(f"Missing required label: {req}")

        spec = manifest.get("spec", {})
        containers = spec.get("containers", [])
        for c in containers:
            sec_ctx = c.get("securityContext", {})
            if sec_ctx.get("privileged", False):
                violations.append(f"Privileged container not allowed: {c.get('name')}")
            if not sec_ctx.get("readOnlyRootFilesystem", False):
                violations.append(
                    f"Container must set readOnlyRootFilesystem=true: {c.get('name')}"
                )

        allowed = len(violations) == 0
        return {
            "allowed": allowed,
            "violations_count": len(violations),
            "violations": violations,
        }


policy_engine = AdmissionPolicyEngine()
