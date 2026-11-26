"""SPIFFE Workload SVID Validator.

Parses and validates SPIFFE IDs (RFC 3986 format) according to SPIFFE standards.
"""

import re
from typing import Any, Dict

SPIFFE_REGEX = re.compile(
    r"^spiffe://([a-zA-Z0-9.\-]+)/ns/([a-zA-Z0-9_\-]+)/sa/([a-zA-Z0-9_\-]+)$"
)


class SpiffeValidator:
    """Validates SPIFFE verifiable identity documents and URIs."""

    @staticmethod
    def validate_spiffe_id(
        spiffe_id: str,
        expected_trust_domain: str = "enterprise.supplychain.net",
    ) -> Dict[str, Any]:
        match = SPIFFE_REGEX.match(spiffe_id)
        if not match:
            return {
                "valid": False,
                "reason": "Malformed SPIFFE ID format",
                "spiffe_id": spiffe_id,
            }
        trust_domain, namespace, service_account = match.groups()
        if trust_domain != expected_trust_domain:
            return {
                "valid": False,
                "reason": f"Untrusted trust domain: {trust_domain}",
                "expected": expected_trust_domain,
            }
        return {
            "valid": True,
            "trust_domain": trust_domain,
            "namespace": namespace,
            "service_account": service_account,
            "spiffe_id": spiffe_id,
        }


spiffe_validator = SpiffeValidator()
