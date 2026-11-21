"""Supply Chain Security Event Broadcaster & Webhook Dispatcher.

Dispatches structured event envelopes to registered SIEM and alert sinks.
"""

from typing import Any, Dict, List


class SecurityEventBroadcaster:
    """Buffers and formats security event notifications."""

    def __init__(self) -> None:
        self.dispatched_events: List[Dict[str, Any]] = []

    def broadcast_event(self, event_type: str, severity: str, details: Dict[str, Any]) -> Dict[str, Any]:
        envelope = {
            "event_type": event_type,
            "severity": severity,
            "details": details,
            "dispatched": True,
        }
        self.dispatched_events.append(envelope)
        return envelope


event_broadcaster = SecurityEventBroadcaster()
