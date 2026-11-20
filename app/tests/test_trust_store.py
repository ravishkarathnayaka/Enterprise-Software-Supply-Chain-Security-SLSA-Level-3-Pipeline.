"""Unit tests for TrustStore."""

from src.trust_store import TrustStore


def test_trust_store_allowed_issuers():
    ts = TrustStore()
    assert ts.is_issuer_trusted("https://token.actions.githubusercontent.com") is True
    assert ts.is_issuer_trusted("https://evil-untrusted-issuer.com") is False


def test_trust_store_key_revocation():
    ts = TrustStore()
    key_id = "cosign-key-2026-compromised"
    assert ts.is_key_revoked(key_id) is False
    ts.revoke_key(key_id)
    assert ts.is_key_revoked(key_id) is True
