"""Unit tests for AdmissionSimulator."""

from src.admission_simulator import AdmissionSimulator


def test_admission_simulator_accepts_hardened_spec():
    spec = {
        "securityContext": {"runAsNonRoot": True},
        "containers": [
            {
                "name": "app",
                "securityContext": {
                    "allowPrivilegeEscalation": False,
                    "readOnlyRootFilesystem": True,
                },
            }
        ],
    }
    res = AdmissionSimulator.evaluate_pod_spec(spec)
    assert res["allowed"] is True
    assert res["decision"] == "ACCEPT"


def test_admission_simulator_denies_unhardened_spec():
    spec = {
        "securityContext": {"runAsNonRoot": False},
        "containers": [{"name": "insecure-app", "securityContext": {}}],
    }
    res = AdmissionSimulator.evaluate_pod_spec(spec)
    assert res["allowed"] is False
    assert res["decision"] == "DENY"
    assert res["violation_count"] >= 2
