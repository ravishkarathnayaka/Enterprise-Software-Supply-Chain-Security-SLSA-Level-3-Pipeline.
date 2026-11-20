"""Unit tests for TraceContext."""

from src.telemetry import TraceContext


def test_traceparent_format():
    tp = TraceContext.generate_traceparent()
    parts = tp.split("-")
    assert len(parts) == 4
    assert parts[0] == "00"
    assert len(parts[1]) == 32  # trace_id
    assert len(parts[2]) == 16  # parent_id
    assert parts[3] == "01"     # flags
