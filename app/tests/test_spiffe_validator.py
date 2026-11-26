"""Unit tests for SpiffeValidator."""

from src.spiffe_validator import SpiffeValidator


def test_valid_spiffe_id():
    sid = "spiffe://enterprise.supplychain.net/ns/prod/sa/secure-app"
    res = SpiffeValidator.validate_spiffe_id(sid)
    assert res["valid"] is True
    assert res["namespace"] == "prod"
    assert res["service_account"] == "secure-app"


def test_invalid_trust_domain():
    sid = "spiffe://rogue.untrusted.com/ns/prod/sa/secure-app"
    res = SpiffeValidator.validate_spiffe_id(sid)
    assert res["valid"] is False
    assert "Untrusted trust domain" in res["reason"]


def test_malformed_spiffe_uri():
    res = SpiffeValidator.validate_spiffe_id("https://not-a-spiffe-uri")
    assert res["valid"] is False
    assert res["reason"] == "Malformed SPIFFE ID format"
