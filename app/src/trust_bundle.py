"""Sigstore Trust Bundle Manager.

Maintains and validates root certificates and transparency log verification keys.
"""

from typing import Any, Dict, List


class TrustBundleManager:
    """Manages trusted root public keys and Fulcio CAs."""

    def __init__(self) -> None:
        self._roots: List[str] = [
            "sigstore-fulcio-root-v1",
            "enterprise-private-ca-root",
        ]

    def is_root_trusted(self, root_id: str) -> bool:
        return root_id in self._roots

    def get_bundle_summary(self) -> Dict[str, Any]:
        return {
            "active_roots_count": len(self._roots),
            "trusted_roots": list(self._roots),
            "status": "HEALTHY",
        }


trust_bundle_manager = TrustBundleManager()
