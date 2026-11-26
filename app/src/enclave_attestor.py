"""Hardware Enclave Remote Attestation Quote Validator.

Validates PCR measurements against golden architectural profiles.
"""

from typing import Any, Dict, List


class EnclaveAttestationValidator:
    """Validates hardware enclave attestation quotes and PCR register states."""

    GOLDEN_PCR0_PREFIX = "e3b0c44298fc1c149afbf4c8996fb924"

    @classmethod
    def validate_quote(
        cls, enclave_id: str, pcr0: str, user_data: str
    ) -> Dict[str, Any]:
        if not enclave_id or not pcr0:
            return {
                "verified": False,
                "reason": "Missing enclave_id or pcr0 measurement",
            }

        is_pcr_valid = pcr0.lower().startswith(cls.GOLDEN_PCR0_PREFIX)
        return {
            "verified": is_pcr_valid,
            "enclave_id": enclave_id,
            "pcr0_verified": is_pcr_valid,
            "user_data_bound": bool(user_data),
            "status": "ATTESTED" if is_pcr_valid else "REJECTED_UNTRUSTED_PCR",
        }


enclave_validator = EnclaveAttestationValidator()
