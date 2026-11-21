"""Unit tests for PredicateValidator."""

from src.predicate_validator import PredicateValidator


def test_predicate_validator_valid():
    statement = {
        "_type": "https://in-toto.io/Statement/v0.1",
        "subject": [{"name": "app", "digest": {"sha256": "0" * 64}}],
        "predicate": {
            "builder": {"id": "https://github.com/actions/runner"},
        },
    }
    res = PredicateValidator.validate_statement(statement)
    assert res["valid"] is True
    assert res["slsa_level"] == "SLSA_BUILD_LEVEL_3"


def test_predicate_validator_invalid_type():
    statement = {"_type": "invalid_type"}
    res = PredicateValidator.validate_statement(statement)
    assert res["valid"] is False
    assert res["error_count"] > 0
