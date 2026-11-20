"""Kubernetes Admission Webhook Decision Simulator.

Evaluates in-memory pod specs against Kyverno PSS-Restricted standards prior to cluster deployment.
"""

from typing import Any, Dict, List


class AdmissionSimulator:
    """Evaluates securityContext attributes against restricted admission policies."""

    @staticmethod
    def evaluate_pod_spec(spec: Dict[str, Any]) -> Dict[str, Any]:
        violations: List[str] = []

        # Check runAsNonRoot
        sec_ctx = spec.get("securityContext", {})
        if not sec_ctx.get("runAsNonRoot", False):
            violations.append("Pod must set securityContext.runAsNonRoot to true")

        # Check containers
        for c in spec.get("containers", []):
            c_sec = c.get("securityContext", {})
            if c_sec.get("allowPrivilegeEscalation", True):
                violations.append(f"Container '{c.get('name')}' must set allowPrivilegeEscalation to false")
            if not c_sec.get("readOnlyRootFilesystem", False):
                violations.append(f"Container '{c.get('name')}' must set readOnlyRootFilesystem to true")

        allowed = len(violations) == 0
        return {
            "allowed": allowed,
            "decision": "ACCEPT" if allowed else "DENY",
            "violation_count": len(violations),
            "violations": violations,
        }


admission_simulator = AdmissionSimulator()
