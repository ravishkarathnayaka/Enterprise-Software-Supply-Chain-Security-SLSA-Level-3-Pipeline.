"""Unit tests for ArtifactSigner."""

import base64
import json
from src.artifact_signer import ArtifactSigner


def test_sign_payload_structure():
    payload = {"artifact": "enterprise-api", "version": "1.0.0"}
    envelope = ArtifactSigner.sign_payload(payload, key_id="test-key-01")

    assert envelope["payloadType"] == "application/vnd.in-toto+json"
    assert len(envelope["signatures"]) == 1
    assert envelope["signatures"][0]["keyid"] == "test-key-01"

    # Decode and check payload content
    decoded = json.loads(base64.b64decode(envelope["payload"]).decode("utf-8"))
    assert decoded["artifact"] == "enterprise-api"
