"""Integration tests for /api/v1/attestation/validate endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_post_attestation_validate_endpoint():
    statement = {
        "_type": "https://in-toto.io/Statement/v0.1",
        "subject": [{"name": "app", "digest": {"sha256": "0" * 64}}],
        "predicate": {"builder": {"id": "https://github.com/actions/runner"}},
    }
    resp = client.post("/api/v1/attestation/validate", json=statement)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is True
    assert data["slsa_level"] == "SLSA_BUILD_LEVEL_3"
