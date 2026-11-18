"""Integration tests for /healthz/deep endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_deep_health_probe_endpoint():
    resp = client.get("/healthz/deep")
    assert resp.status_code == 200
    data = resp.json()
    assert data["overall_status"] == "HEALTHY"
    assert "subsystems" in data
    assert data["subsystems"]["audit_integrity"] == "HEALTHY"
