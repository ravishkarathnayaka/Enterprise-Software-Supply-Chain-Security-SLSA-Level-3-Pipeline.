"""Unit tests for Correlation ID propagation and context preservation."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_correlation_id_special_characters():
    custom_id = "trace-id-abc_123.456"
    resp = client.get("/healthz", headers={"X-Correlation-ID": custom_id})
    assert resp.status_code == 200
    assert resp.headers["X-Correlation-ID"] == custom_id


def test_correlation_id_in_metrics_request():
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert "X-Correlation-ID" in resp.headers
