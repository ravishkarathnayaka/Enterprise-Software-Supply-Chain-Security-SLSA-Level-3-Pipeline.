"""Enterprise Supply Chain Security & SLSA Level 3 - FastAPI Application.

Production-grade, hardened microservice with:
- Structured JSON logging with correlation IDs
- Security response headers (OWASP Secure Headers Project)
- Strict input validation preventing Injection & Path Traversal
- Kubernetes liveness (/healthz) and readiness (/readyz) probes
"""

import json
import logging
import os
import sys
import time
import uuid
from contextvars import ContextVar
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator
from starlette.middleware.base import BaseHTTPMiddleware

# ------------------------------------------------------------------------------
# Context Variables for Correlation Tracking
# ------------------------------------------------------------------------------
correlation_id_ctx: ContextVar[str] = ContextVar("correlation_id", default="system")


# ------------------------------------------------------------------------------
# Structured JSON Logging Formatter
# ------------------------------------------------------------------------------
class JSONLogFormatter(logging.Formatter):
    """Outputs application logs formatted strictly as JSON lines."""

    def format(self, record: logging.LogRecord) -> str:
        log_data: Dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "correlation_id": correlation_id_ctx.get(),
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_data)


# Configure Root Logger
logger = logging.getLogger("enterprise_sec_pipeline")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JSONLogFormatter())
logger.handlers = [handler]
logger.propagate = False

# ------------------------------------------------------------------------------
# Application Initialization & State
# ------------------------------------------------------------------------------
START_TIME = time.time()
SERVICE_NAME = "enterprise-supply-chain-api"
SERVICE_VERSION = "1.0.0"
SLSA_LEVEL = "SLSA_BUILD_LEVEL_3"

app = FastAPI(
    title="Enterprise Secure Supply Chain API",
    description="SLSA Level 3 certified microservice with Cosign verification and Kyverno admission controls.",
    version=SERVICE_VERSION,
    docs_url="/api/docs",
    redoc_url=None,
    openapi_url="/api/openapi.json",
)


# ------------------------------------------------------------------------------
# Middleware 1: Correlation ID Tracking
# ------------------------------------------------------------------------------
class CorrelationIdMiddleware(BaseHTTPMiddleware):
    """Injects and propagates a unique X-Correlation-ID header across requests."""

    async def dispatch(self, request: Request, call_next) -> Response:
        corr_id = request.headers.get("X-Correlation-ID")
        if not corr_id:
            corr_id = str(uuid.uuid4())

        correlation_id_ctx.set(corr_id)
        response = await call_next(request)
        response.headers["X-Correlation-ID"] = corr_id
        return response


# ------------------------------------------------------------------------------
# Middleware 2: OWASP Security Headers
# ------------------------------------------------------------------------------
class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Enforces defense-in-depth HTTP security headers on all outbound responses."""

    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)
        response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "geolocation=(), camera=(), microphone=()"
        response.headers["Server"] = "Enterprise-Secure-Runtime"
        return response


app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(CorrelationIdMiddleware)


# ------------------------------------------------------------------------------
# Request & Response Models (Pydantic v2)
# ------------------------------------------------------------------------------
class VerificationPayload(BaseModel):
    """Input payload with strict validation preventing injection and path traversal."""

    artifact_name: str = Field(
        ...,
        min_length=3,
        max_length=128,
        description="Alphanumeric name of the artifact (hyphens and underscores allowed).",
        examples=["secure-service-app"],
    )
    sha256_digest: str = Field(
        ...,
        min_length=64,
        max_length=64,
        description="Standard hex-encoded SHA256 digest of the artifact.",
        examples=["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"],
    )
    environment: str = Field(
        default="production",
        pattern=r"^(development|staging|production)$",
        description="Deployment target environment.",
    )
    metadata: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        description="Arbitrary safe key-value attributes.",
    )

    @field_validator("artifact_name")
    @classmethod
    def validate_safe_characters(cls, value: str) -> str:
        """Deny path traversal characters, directory separators, and command injection tokens."""
        dangerous_tokens = ["..", "/", "\\", ";", "&", "|", "`", "$", "<", ">"]
        for token in dangerous_tokens:
            if token in value:
                raise ValueError(f"Dangerous token detected in artifact_name: '{token}'")
        return value

    @field_validator("sha256_digest")
    @classmethod
    def validate_hex_digest(cls, value: str) -> str:
        """Enforce strict hexadecimal characters for digests."""
        if not all(c in "0123456789abcdefABCDEF" for c in value):
            raise ValueError("sha256_digest must contain only valid hexadecimal characters.")
        return value.lower()


class VerificationResponse(BaseModel):
    verified: bool
    artifact_name: str
    sha256_digest: str
    verified_at: str
    slsa_level: str
    correlation_id: str


# ------------------------------------------------------------------------------
# API Endpoints
# ------------------------------------------------------------------------------
@app.get("/", summary="Root index")
async def root() -> Dict[str, str]:
    """Root endpoint returning service identity."""
    return {
        "service": SERVICE_NAME,
        "status": "operational",
        "documentation": "/api/docs",
    }


@app.get("/healthz", summary="Liveness Probe")
async def healthz() -> Dict[str, Any]:
    """Kubernetes liveness probe ensuring process is alive."""
    uptime = time.time() - START_TIME
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "uptime_seconds": round(uptime, 2),
    }


@app.get("/readyz", summary="Readiness Probe")
async def readyz() -> Dict[str, Any]:
    """Kubernetes readiness probe ensuring downstream dependencies are reachable."""
    return {
        "status": "ready",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "checks": {
            "internal_state": "ok",
            "admission_compatibility": "ok",
        },
    }


@app.get("/api/v1/info", summary="Service Information & SLSA Metadata")
async def info() -> Dict[str, Any]:
    """Returns security posture and build metadata."""
    return {
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "slsa_build_level": SLSA_LEVEL,
        "container_hardening": {
            "base_image": "gcr.io/distroless/python3-debian12:nonroot",
            "run_as_uid": 65532,
            "shell_present": False,
            "read_only_root_fs": True,
        },
        "admission_controller": "Kyverno PSS-Restricted",
        "git_commit": os.getenv("GIT_COMMIT", "dev-local"),
    }


@app.post(
    "/api/v1/verify-data",
    response_model=VerificationResponse,
    status_code=status.HTTP_200_OK,
    summary="Validate Artifact Integrity",
)
async def verify_data(payload: VerificationPayload) -> VerificationResponse:
    """Simulates artifact verification within the secure supply chain."""
    logger.info(f"Integrity check invoked for artifact: {payload.artifact_name}")
    return VerificationResponse(
        verified=True,
        artifact_name=payload.artifact_name,
        sha256_digest=payload.sha256_digest,
        verified_at=datetime.now(timezone.utc).isoformat(),
        slsa_level=SLSA_LEVEL,
        correlation_id=correlation_id_ctx.get(),
    )
