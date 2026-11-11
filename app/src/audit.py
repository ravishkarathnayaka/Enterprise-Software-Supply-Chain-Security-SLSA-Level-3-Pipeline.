"""Cryptographic Security Audit Logger.

Generates tamper-evident, SHA256-chained security audit events for high-assurance supply chain tracking.
"""

import hashlib
import json
import threading
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


class SecurityAuditLogger:
    """Thread-safe, hash-chained in-memory audit log for security events."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._last_hash: str = "0000000000000000000000000000000000000000000000000000000000000000"
        self._entries: List[Dict[str, Any]] = []

    def record_event(
        self,
        event_type: str,
        actor: str,
        details: Dict[str, Any],
        correlation_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Appends a new audit record cryptographically linked to the previous entry."""
        with self._lock:
            timestamp = datetime.now(timezone.utc).isoformat()
            payload = {
                "sequence": len(self._entries) + 1,
                "timestamp": timestamp,
                "event_type": event_type,
                "actor": actor,
                "correlation_id": correlation_id or "system",
                "details": details,
                "previous_hash": self._last_hash,
            }
            serialized = json.dumps(payload, sort_keys=True)
            entry_hash = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
            payload["current_hash"] = entry_hash

            self._last_hash = entry_hash
            self._entries.append(payload)
            return payload

    def get_recent_entries(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Returns the most recent audit entries."""
        with self._lock:
            return list(self._entries[-limit:])

    def verify_integrity(self) -> bool:
        """Verifies the cryptographic hash-chain across all historical entries."""
        with self._lock:
            prev_hash = "0000000000000000000000000000000000000000000000000000000000000000"
            for entry in self._entries:
                if entry["previous_hash"] != prev_hash:
                    return False
                payload_to_verify = {
                    "sequence": entry["sequence"],
                    "timestamp": entry["timestamp"],
                    "event_type": entry["event_type"],
                    "actor": entry["actor"],
                    "correlation_id": entry["correlation_id"],
                    "details": entry["details"],
                    "previous_hash": entry["previous_hash"],
                }
                computed_hash = hashlib.sha256(
                    json.dumps(payload_to_verify, sort_keys=True).encode("utf-8")
                ).hexdigest()
                if computed_hash != entry["current_hash"]:
                    return False
                prev_hash = entry["current_hash"]
            return True


audit_logger = SecurityAuditLogger()
