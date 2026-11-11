"""RFC 7807 Problem Details HTTP Error Handlers.

Uniform error serialization ensuring internal implementation details are never leaked.
"""

from typing import Any, Dict
from fastapi import Request, status
from fastapi.responses import JSONResponse


def create_problem_details(
    status_code: int,
    title: str,
    detail: str,
    error_type: str = "about:blank",
    instance: str = "/",
    extra: Dict[str, Any] = None,
) -> JSONResponse:
    """Creates a standardized RFC 7807 Problem Details response."""
    payload = {
        "type": error_type,
        "title": title,
        "status": status_code,
        "detail": detail,
        "instance": instance,
    }
    if extra:
        payload.update(extra)

    return JSONResponse(
        status_code=status_code,
        content=payload,
        headers={"Content-Type": "application/problem+json"},
    )
