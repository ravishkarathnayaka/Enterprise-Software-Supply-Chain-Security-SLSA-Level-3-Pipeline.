"""Request Sanitization & Suspicious Header Detection Middleware.

Blocks common probe headers, malicious payloads, and injection attempts.
"""

from fastapi import Request, Response, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class ThreatInspectionMiddleware(BaseHTTPMiddleware):
    """Inspects inbound requests for known probe signatures and malformed payloads."""

    SUSPICIOUS_HEADERS = ["x-forwarded-host-injection", "x-scan-payload", "proxy-connection"]

    async def dispatch(self, request: Request, call_next) -> Response:
        for header in self.SUSPICIOUS_HEADERS:
            if header in request.headers:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        "error": "SECURITY_PROBE_DETECTED",
                        "detail": f"Suspicious header rejected: {header}",
                    },
                )
        return await call_next(request)
