"""Integration tests for /api/v1/admission/simulate endpoint."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_post_admission_simulate_endpoint():
    payload = {
        "securityContext": {"runAsNonRoot": True},
        "containers": [
            {
                "name": "microservice",
                "securityContext": {
                    "allowPrivilegeEscalation": False,
                    "readOnlyRootFilesystem": True,
                },
            }
        ],
    }
    resp = client.post("/api/v1/admission/simulate", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["allowed"] is True
    assert data["decision"] == "ACCEPT"
