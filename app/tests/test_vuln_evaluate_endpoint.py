"""Integration tests for /api/v1/vuln/evaluate endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_vuln_evaluate_endpoint():
    payload = {"cve_id": "CVE-2024-1234", "cvss": 9.5, "epss": 0.50}
    resp = client.post("/api/v1/vuln/evaluate", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["blocked"] is True
    assert data["severity"] == "CRITICAL"
