"""Unit tests for SecurityEventBroadcaster."""

from src.event_broadcaster import SecurityEventBroadcaster


def test_broadcast_event():
    broadcaster = SecurityEventBroadcaster()
    evt = broadcaster.broadcast_event(
        event_type="UNAUTHORIZED_ADMISSION_ATTEMPT",
        severity="HIGH",
        details={"pod": "test-pod", "reason": "unsigned"},
    )
    assert evt["event_type"] == "UNAUTHORIZED_ADMISSION_ATTEMPT"
    assert evt["dispatched"] is True
    assert len(broadcaster.dispatched_events) == 1
