"""Runtime Workload Image Drift Detector.

Compares running container image digests against approved cryptographic baseline digests.
"""

from typing import Any, Dict


class WorkloadDriftDetector:
    """Detects unexpected image digest modifications or drift in running workloads."""

    @staticmethod
    def detect_drift(baseline_digest: str, running_digest: str) -> Dict[str, Any]:
        if not baseline_digest or not running_digest:
            return {"drift_detected": True, "reason": "Missing digest parameter"}
        drift = baseline_digest.strip().lower() != running_digest.strip().lower()
        return {
            "drift_detected": drift,
            "baseline": baseline_digest,
            "running": running_digest,
            "status": "DRIFT_ALERT" if drift else "ALIGNED",
        }


drift_detector = WorkloadDriftDetector()
