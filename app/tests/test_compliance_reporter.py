"""Unit tests for ComplianceScorer."""

from src.compliance_reporter import ComplianceScorer


def test_compliance_score_perfect():
    controls = {"c1": True, "c2": True, "c3": True, "c4": True}
    res = ComplianceScorer.calculate_score(controls)
    assert res["compliance_score"] == 100.0
    assert res["grade"] == "A+"
    assert res["slsa_level_3_ready"] is True


def test_compliance_score_empty():
    res = ComplianceScorer.calculate_score({})
    assert res["compliance_score"] == 0.0
    assert res["grade"] == "F"
