"""Integration tests for /api/v1/enclave/attest endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_enclave_attest_endpoint():
    valid_pcr = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    payload = {
        "enclave_id": "enclave-nitro-01",
        "pcr0": valid_pcr,
        "user_data": "sample",
    }
    resp = client.post("/api/v1/enclave/attest", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["verified"] is True
    assert data["status"] == "ATTESTED"
