"""Unit tests for cryptographic SecurityAuditLogger."""

from src.audit import SecurityAuditLogger


def test_audit_event_hash_chain():
    logger = SecurityAuditLogger()
    e1 = logger.record_event("SIGNATURE_VERIFIED", "kyverno", {"image": "app:v1"})
    e2 = logger.record_event("ATTESTATION_VALIDATED", "cosign", {"level": "L3"})

    assert e1["sequence"] == 1
    assert e2["sequence"] == 2
    assert e2["previous_hash"] == e1["current_hash"]
    assert logger.verify_integrity() is True


def test_audit_tamper_detection():
    logger = SecurityAuditLogger()
    logger.record_event("EV1", "actor", {"k": "v"})
    logger.record_event("EV2", "actor", {"k": "v2"})

    # Tamper with entry in memory
    logger._entries[0]["details"]["k"] = "tampered"
    assert logger.verify_integrity() is False
