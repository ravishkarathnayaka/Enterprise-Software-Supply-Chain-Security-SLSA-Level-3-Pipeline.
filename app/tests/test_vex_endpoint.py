"""Integration tests for /api/v1/vex/status endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_vex_status_endpoint():
    resp = client.get("/api/v1/vex/status?cve_id=CVE-2026-1188")
    assert resp.status_code == 200
    data = resp.json()
    assert data["cve"] == "CVE-2026-1188"
    assert data["status"] == "not_affected"
    assert data["action"] == "ALLOW"
