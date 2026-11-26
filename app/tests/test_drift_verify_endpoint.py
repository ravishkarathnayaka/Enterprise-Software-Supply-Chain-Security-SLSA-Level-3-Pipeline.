"""Integration tests for /api/v1/drift/verify endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_drift_verify_endpoint():
    digest = "sha256:" + "c" * 64
    payload = {"baseline_digest": digest, "running_digest": digest}
    resp = client.post("/api/v1/drift/verify", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["drift_detected"] is False
    assert data["status"] == "ALIGNED"
