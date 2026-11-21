"""Cryptographic Artifact Signer & Envelope Generator.

Generates DSSE (Dead Simple Signing Envelope) formatted payloads with simulated signatures.
"""

import base64
import hashlib
import json
from typing import Any, Dict


class ArtifactSigner:
    """Produces DSSE compliant signed attestation envelopes."""

    @staticmethod
    def sign_payload(payload: Dict[str, Any], key_id: str = "enterprise-kms-cosign-01") -> Dict[str, Any]:
        raw_json = json.dumps(payload, sort_keys=True)
        encoded_payload = base64.b64encode(raw_json.encode("utf-8")).decode("ascii")
        sig_hash = hashlib.sha256(raw_json.encode("utf-8")).hexdigest()

        return {
            "payloadType": "application/vnd.in-toto+json",
            "payload": encoded_payload,
            "signatures": [
                {
                    "keyid": key_id,
                    "sig": f"simulated_ecdsa_sig_{sig_hash[:32]}",
                }
            ],
        }


artifact_signer = ArtifactSigner()
