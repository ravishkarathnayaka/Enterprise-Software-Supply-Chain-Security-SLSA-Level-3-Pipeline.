"""Unit tests for ThreatInspectionMiddleware."""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.security_middleware import ThreatInspectionMiddleware

test_app = FastAPI()
test_app.add_middleware(ThreatInspectionMiddleware)


@test_app.get("/ping")
def ping():
    return {"status": "pong"}


client = TestClient(test_app)


def test_threat_middleware_blocks_suspicious_header():
    resp = client.get("/ping", headers={"x-forwarded-host-injection": "evil.com"})
    assert resp.status_code == 400
    assert resp.json()["error"] == "SECURITY_PROBE_DETECTED"


def test_threat_middleware_allows_clean_request():
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json()["status"] == "pong"
