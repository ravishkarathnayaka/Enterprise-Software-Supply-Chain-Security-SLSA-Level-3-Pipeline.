"""Distributed Tracing & W3C TraceContext Header Generator.

Provides correlation across multi-stage build pipelines and container runtimes.
"""

import os
import random
import time


class TraceContext:
    """Generates W3C traceparent headers for distributed supply chain tracing."""

    @staticmethod
    def generate_traceparent() -> str:
        version = "00"
        trace_id = f"{random.getrandbits(128):032x}"
        parent_id = f"{random.getrandbits(64):016x}"
        trace_flags = "01"  # sampled
        return f"{version}-{trace_id}-{parent_id}-{trace_flags}"


telemetry = TraceContext()
