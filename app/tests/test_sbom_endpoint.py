"""Integration tests for /api/v1/sbom/components endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_sbom_components():
    resp = client.get("/api/v1/sbom/components")
    assert resp.status_code == 200
    data = resp.json()
    assert data["format"] == "CycloneDX-1.5"
    assert data["total_packages"] >= 1
    assert any(pkg["name"] == "fastapi" for pkg in data["packages"])
