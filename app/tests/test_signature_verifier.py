"""Unit tests for CryptographicVerifier."""

import pytest
from src.signature_verifier import CryptographicVerifier


def test_sha256_verification_pass():
    data = b"enterprise-build-artifact"
    expected = "eb1746f6dc0d275dfe7a55e7f4da0114a1bfb1e35cd5cec0c6dc18104f302fb2"
    assert CryptographicVerifier.verify_sha256(data, expected) is True


def test_sha256_verification_fail():
    data = b"tampered-artifact"
    expected = "eb1746f6dc0d275dfe7a55e7f4da0114a1bfb1e35cd5cec0c6dc18104f302fb2"
    assert CryptographicVerifier.verify_sha256(data, expected) is False


def test_rekor_bundle_claim_valid():
    res = CryptographicVerifier.verify_rekor_bundle_claim(
        log_index=12345,
        integrated_time=1700000000,
        entry_hash="a" * 64,
    )
    assert res["verified"] is True
    assert res["rekor_log_index"] == 12345
