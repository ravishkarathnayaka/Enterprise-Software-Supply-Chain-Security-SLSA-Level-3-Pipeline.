"""Unit tests for SecurityConfig module."""

from src.config import SecurityConfig


def test_config_defaults():
    cfg = SecurityConfig()
    assert cfg.SERVICE_NAME == "enterprise-supply-chain-api"
    assert cfg.SERVICE_VERSION == "1.0.0"
    assert cfg.RATE_LIMIT_ENABLED is True
    assert cfg.RATE_LIMIT_MAX_REQUESTS > 0
    assert cfg.SLSA_LEVEL == "SLSA_BUILD_LEVEL_3"
