"""Integration tests for /api/v1/identity/spiffe/verify endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_spiffe_verify_endpoint():
    payload = {
        "spiffe_id": "spiffe://enterprise.supplychain.net/ns/prod/sa/app",
        "expected_trust_domain": "enterprise.supplychain.net",
    }
    resp = client.post("/api/v1/identity/spiffe/verify", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is True
    assert data["namespace"] == "prod"
