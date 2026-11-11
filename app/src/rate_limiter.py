"""Token Bucket Rate Limiting Middleware.

Mitigates denial-of-service and brute-force verification requests on sensitive API endpoints.
"""

import time
import threading
from typing import Dict, Tuple
from fastapi import Request, Response, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class TokenBucketRateLimiter(BaseHTTPMiddleware):
    """In-memory IP token-bucket rate limiter."""

    def __init__(self, app, max_tokens: int = 120, refill_rate_per_sec: float = 2.0) -> None:
        super().__init__(app)
        self.max_tokens = max_tokens
        self.refill_rate = refill_rate_per_sec
        self.clients: Dict[str, Tuple[float, float]] = {}  # ip -> (tokens, last_update)
        self._lock = threading.Lock()

    def _allow_request(self, ip: str) -> bool:
        now = time.time()
        with self._lock:
            if ip not in self.clients:
                self.clients[ip] = (self.max_tokens - 1, now)
                return True

            tokens, last_update = self.clients[ip]
            elapsed = now - last_update
            tokens = min(self.max_tokens, tokens + elapsed * self.refill_rate)

            if tokens >= 1.0:
                self.clients[ip] = (tokens - 1.0, now)
                return True
            else:
                self.clients[ip] = (tokens, now)
                return False

    async def dispatch(self, request: Request, call_next) -> Response:
        # Exempt health probes and metrics from rate limits
        if request.url.path in ("/healthz", "/readyz", "/metrics"):
            return await call_next(request)

        client_ip = request.client.host if request.client else "unknown"
        if not self._allow_request(client_ip):
            return JSONResponse(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                content={
                    "type": "https://enterprise.sec/errors/rate-limit-exceeded",
                    "title": "Too Many Requests",
                    "status": 429,
                    "detail": "Rate limit exceeded. Please back off before retrying.",
                },
                headers={"Retry-After": "30"},
            )

        return await call_next(request)
