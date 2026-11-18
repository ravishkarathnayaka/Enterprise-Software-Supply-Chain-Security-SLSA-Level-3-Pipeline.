"""Unit tests for CryptographicVerifier."""

import pytest
from src.signature_verifier import CryptographicVerifier


def test_sha256_verification_pass():
    data = b"enterprise-build-artifact"
    expected = "5e56e4b47eb25556dc9b71e72e3992b8d002344ea8bb56209594f8373b5ee003"
    assert CryptographicVerifier.verify_sha256(data, expected) is True


def test_sha256_verification_fail():
    data = b"tampered-artifact"
    expected = "5e56e4b47eb25556dc9b71e72e3992b8d002344ea8bb56209594f8373b5ee003"
    assert CryptographicVerifier.verify_sha256(data, expected) is False


def test_rekor_bundle_claim_valid():
    res = CryptographicVerifier.verify_rekor_bundle_claim(
        log_index=12345,
        integrated_time=1700000000,
        entry_hash="a" * 64,
    )
    assert res["verified"] is True
    assert res["rekor_log_index"] == 12345
