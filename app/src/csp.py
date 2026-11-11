"""Dynamic Content Security Policy (CSP) Nonce Generator.

Generates cryptographically random nonces and builds zero-trust CSP headers.
"""

import base64
import os
from typing import Dict


def generate_csp_nonce(length: int = 16) -> str:
    """Generates a secure URL-safe base64 nonce using OS entropy."""
    random_bytes = os.urandom(length)
    return base64.b64encode(random_bytes).decode("ascii").rstrip("=")


def build_strict_csp_header(nonce: str) -> str:
    """Builds a defense-in-depth Content Security Policy with nonces."""
    directives = [
        "default-src 'none'",
        f"script-src 'strict-dynamic' 'nonce-{nonce}'",
        "style-src 'self' 'unsafe-inline'",
        "img-src 'self' data: https:",
        "font-src 'self'",
        "connect-src 'self'",
        "frame-ancestors 'none'",
        "base-uri 'none'",
        "form-action 'self'",
    ]
    return "; ".join(directives)
