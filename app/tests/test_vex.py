"""Unit tests for VexEvaluator."""

from src.vex import VexEvaluator, VexStatement, VexStatus


def test_vex_evaluation_not_affected():
    evaluator = VexEvaluator()
    evaluator.register_statement(
        VexStatement(
            vulnerability_id="CVE-2026-9999",
            status=VexStatus.NOT_AFFECTED,
            justification="code_not_reachable",
        )
    )
    res = evaluator.evaluate_cve("CVE-2026-9999")
    assert res["status"] == "not_affected"
    assert res["action"] == "ALLOW"


def test_vex_evaluation_unassessed_blocks():
    evaluator = VexEvaluator()
    res = evaluator.evaluate_cve("CVE-UNKNOWN")
    assert res["status"] == "unassessed"
    assert res["action"] == "BLOCK_BY_DEFAULT"
