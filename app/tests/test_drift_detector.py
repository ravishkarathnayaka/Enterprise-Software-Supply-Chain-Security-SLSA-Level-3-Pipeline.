"""Unit tests for WorkloadDriftDetector."""

from src.drift_detector import WorkloadDriftDetector


def test_no_drift():
    digest = "sha256:" + "a" * 64
    res = WorkloadDriftDetector.detect_drift(digest, digest)
    assert res["drift_detected"] is False
    assert res["status"] == "ALIGNED"


def test_drift_detected():
    d1 = "sha256:" + "a" * 64
    d2 = "sha256:" + "b" * 64
    res = WorkloadDriftDetector.detect_drift(d1, d2)
    assert res["drift_detected"] is True
    assert res["status"] == "DRIFT_ALERT"
