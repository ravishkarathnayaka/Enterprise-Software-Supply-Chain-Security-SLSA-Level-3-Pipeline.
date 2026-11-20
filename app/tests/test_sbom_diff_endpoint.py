"""Integration tests for /api/v1/sbom/diff endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_sbom_diff_endpoint():
    resp = client.get("/api/v1/sbom/diff")
    assert resp.status_code == 200
    data = resp.json()
    assert "drift_detected" in data
    assert "added" in data
