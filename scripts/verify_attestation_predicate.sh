#!/usr/bin/env bash
# ==============================================================================
# Verify In-Toto SLSA Provenance Attestation Predicate
# ==============================================================================
set -euo pipefail

IMAGE_REF="${1:-ghcr.io/ravishkarathnayaka/enterprise-supply-chain-app:latest}"
PREDICATE_TYPE="https://slsa.dev/provenance/v0.2"

echo "Verifying in-toto attestation (${PREDICATE_TYPE}) for: ${IMAGE_REF}..."
cosign verify-attestation \
  --type="${PREDICATE_TYPE}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  --certificate-identity-regexp="https://github.com/ravishkarathnayaka/.*" \
  "${IMAGE_REF}"

echo "[SUCCESS] In-toto provenance attestation verified."
