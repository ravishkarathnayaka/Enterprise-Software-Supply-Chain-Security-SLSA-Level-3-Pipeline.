"""Unit tests for RekorProofValidator."""

from src.rekor_client import RekorProofValidator


def test_rekor_proof_valid():
    res = RekorProofValidator.validate_inclusion_proof(
        log_index=100,
        root_hash="a" * 64,
        entry_uuid="b" * 32,
    )
    assert res["valid"] is True
    assert res["verified_in_merkle_tree"] is True


def test_rekor_proof_invalid_index():
    res = RekorProofValidator.validate_inclusion_proof(
        log_index=-1,
        root_hash="a" * 64,
        entry_uuid="b" * 32,
    )
    assert res["valid"] is False
