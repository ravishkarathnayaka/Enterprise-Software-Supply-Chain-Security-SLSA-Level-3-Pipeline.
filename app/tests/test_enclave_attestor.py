"""Unit tests for EnclaveAttestationValidator."""

from src.enclave_attestor import EnclaveAttestationValidator


def test_valid_enclave_quote():
    valid_pcr = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    res = EnclaveAttestationValidator.validate_quote(
        "enclave-nitro-01", valid_pcr, "custom-data"
    )
    assert res["verified"] is True
    assert res["status"] == "ATTESTED"


def test_invalid_enclave_quote():
    res = EnclaveAttestationValidator.validate_quote(
        "enclave-nitro-01", "untrusted-pcr-hash", ""
    )
    assert res["verified"] is False
    assert res["status"] == "REJECTED_UNTRUSTED_PCR"
