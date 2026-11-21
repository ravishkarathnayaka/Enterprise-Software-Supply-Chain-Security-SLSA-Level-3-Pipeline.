"""Integration tests for /api/v1/crypto/benchmark endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_crypto_benchmark_endpoint():
    resp = client.get("/api/v1/crypto/benchmark?iterations=50")
    assert resp.status_code == 200
    data = resp.json()
    assert data["iterations"] == 50
    assert data["algorithm"] == "SHA-256"
    assert data["admission_overhead_status"] == "OPTIMAL"
