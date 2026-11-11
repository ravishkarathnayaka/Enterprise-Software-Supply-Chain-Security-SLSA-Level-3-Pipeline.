"""Application Configuration & Security Settings.

Loads configuration from environment variables with safe defaults and strict validation.
"""

import os
from typing import List


class SecurityConfig:
    """Security and environment configuration parameters."""

    SERVICE_NAME: str = os.getenv("SERVICE_NAME", "enterprise-supply-chain-api")
    SERVICE_VERSION: str = os.getenv("SERVICE_VERSION", "1.0.0")
    ENVIRONMENT: str = os.getenv("APP_ENV", "production")
    DEBUG: bool = os.getenv("APP_DEBUG", "false").lower() in ("true", "1", "yes")

    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = os.getenv("RATE_LIMIT_ENABLED", "true").lower() in ("true", "1")
    RATE_LIMIT_MAX_REQUESTS: int = int(os.getenv("RATE_LIMIT_MAX_REQUESTS", "100"))
    RATE_LIMIT_WINDOW_SECONDS: int = int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "60"))

    # Cryptographic & SLSA Metadata
    SLSA_LEVEL: str = os.getenv("SLSA_LEVEL", "SLSA_BUILD_LEVEL_3")
    ALLOWED_ORIGINS: List[str] = [
        origin.strip()
        for origin in os.getenv("ALLOWED_ORIGINS", "https://localhost,https://127.0.0.1").split(",")
        if origin.strip()
    ]


config = SecurityConfig()
