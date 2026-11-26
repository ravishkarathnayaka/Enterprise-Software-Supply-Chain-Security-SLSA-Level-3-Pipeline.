# Timing Side-Channel Analysis in Attestation & Signature Verification

## Vulnerability Description
Non-constant-time string comparisons during HMAC, signature, or digest validation can leak cryptographic information to local or adjacent co-located processes through timing discrepancies.

## Implementation Standard
All hash and signature equality checks within `app/src` microservice components must utilize:
- Constant-time comparison functions: `hmac.compare_digest(a, b)`
- Constant-time SHA256 digest comparison routines preventing early termination leaks.
