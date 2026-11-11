"""Boundary and edge case validation tests for VerificationPayload."""

import pytest
from pydantic import ValidationError
from src.main import VerificationPayload


def test_boundary_payload_lengths():
    # Valid min length (3 chars)
    payload = VerificationPayload(
        artifact_name="app",
        sha256_digest="0" * 64,
        environment="production",
    )
    assert payload.artifact_name == "app"

    # Invalid too short
    with pytest.raises(ValidationError):
        VerificationPayload(
            artifact_name="ab",
            sha256_digest="0" * 64,
        )


def test_boundary_uppercase_digest_normalization():
    # Valid uppercase hex normalized to lowercase
    digest = ("A" * 32) + ("F" * 32)
    payload = VerificationPayload(
        artifact_name="test-app",
        sha256_digest=digest,
    )
    assert payload.sha256_digest == digest.lower()
