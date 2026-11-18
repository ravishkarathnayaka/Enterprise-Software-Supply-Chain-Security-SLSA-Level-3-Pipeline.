"""Unit tests for HealthSubsystemProber."""

import time
from src.health import HealthSubsystemProber


def test_health_subsystems_healthy():
    prober = HealthSubsystemProber(start_time=time.time())
    res = prober.check_subsystems(audit_healthy=True)
    assert res["overall_status"] == "HEALTHY"
    assert res["subsystems"]["audit_integrity"] == "HEALTHY"


def test_health_subsystems_degraded():
    prober = HealthSubsystemProber(start_time=time.time())
    res = prober.check_subsystems(audit_healthy=False)
    assert res["overall_status"] == "DEGRADED"
    assert res["subsystems"]["audit_integrity"] == "CORRUPTED"
