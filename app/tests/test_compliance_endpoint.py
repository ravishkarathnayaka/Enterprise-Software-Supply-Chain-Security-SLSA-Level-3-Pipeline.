"""Integration tests for /api/v1/compliance/score endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_compliance_score_endpoint():
    resp = client.get("/api/v1/compliance/score")
    assert resp.status_code == 200
    data = resp.json()
    assert data["compliance_score"] >= 90.0
    assert data["grade"] in ("A", "A+")
    assert data["slsa_level_3_ready"] is True
