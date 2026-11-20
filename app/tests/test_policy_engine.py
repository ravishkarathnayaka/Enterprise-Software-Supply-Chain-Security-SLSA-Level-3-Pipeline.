"""Unit tests for PolicyRuleEngine."""

from src.policy_engine import PolicyRuleEngine


def test_policy_engine_slsa_compliant():
    meta = {
        "slsa_level": "SLSA_BUILD_LEVEL_3",
        "signed_by": "sigstore-fulcio",
        "rekor_verified": True,
    }
    res = PolicyRuleEngine.evaluate_slsa_posture(meta)
    assert res["compliant"] is True
    assert res["status"] == "COMPLIANT"


def test_policy_engine_slsa_non_compliant():
    meta = {"slsa_level": "SLSA_BUILD_LEVEL_1", "rekor_verified": False}
    res = PolicyRuleEngine.evaluate_slsa_posture(meta)
    assert res["compliant"] is False
    assert len(res["missing_attributes"]) > 0
