"""Cryptographic Trust Store & Allowed OIDC Issuer Registry.

Maintains authorized identity providers, public keys, and certificate authorities.
"""

from typing import Dict, List, Set


class TrustStore:
    """Manages trusted root certificates and allowed OIDC issuers."""

    def __init__(self) -> None:
        self._allowed_issuers: Set[str] = {
            "https://token.actions.githubusercontent.com",
            "https://accounts.google.com",
        }
        self._revoked_keys: Set[str] = set()

    def is_issuer_trusted(self, issuer_url: str) -> bool:
        return issuer_url.rstrip("/") in self._allowed_issuers

    def revoke_key(self, key_id: str) -> None:
        self._revoked_keys.add(key_id)

    def is_key_revoked(self, key_id: str) -> bool:
        return key_id in self._revoked_keys


trust_store = TrustStore()
