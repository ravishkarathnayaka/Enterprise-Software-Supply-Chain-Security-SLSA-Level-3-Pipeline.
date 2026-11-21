"""Integration tests for /api/v1/sbom/licenses endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_sbom_licenses_endpoint():
    resp = client.get("/api/v1/sbom/licenses")
    assert resp.status_code == 200
    data = resp.json()
    assert data["compliant"] is True
    assert data["compliant_packages"] >= 1
    assert data["flagged_count"] == 0
