"""Unit tests for AdmissionPolicyEngine."""

from src.policy_engine import AdmissionPolicyEngine


def test_policy_engine_valid_manifest():
    manifest = {
        "metadata": {
            "labels": {
                "app.kubernetes.io/name": "test-app",
                "app.kubernetes.io/part-of": "enterprise-supply-chain",
            }
        },
        "spec": {
            "containers": [
                {
                    "name": "app",
                    "securityContext": {
                        "privileged": False,
                        "readOnlyRootFilesystem": True,
                    },
                }
            ]
        },
    }
    res = AdmissionPolicyEngine.evaluate(manifest)
    assert res["allowed"] is True
    assert res["violations_count"] == 0


def test_policy_engine_privileged_blocked():
    manifest = {
        "metadata": {"labels": {}},
        "spec": {
            "containers": [
                {"name": "bad", "securityContext": {"privileged": True}}
            ]
        },
    }
    res = AdmissionPolicyEngine.evaluate(manifest)
    assert res["allowed"] is False
    assert res["violations_count"] >= 2
