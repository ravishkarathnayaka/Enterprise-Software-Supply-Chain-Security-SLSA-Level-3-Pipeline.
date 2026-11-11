#!/usr/bin/env bash
# ==============================================================================
# Automated Verification of Sigstore Keyless Signatures
# ==============================================================================
set -euo pipefail

IMAGE_REF="${1:-ghcr.io/ravishkarathnayaka/enterprise-supply-chain-app:latest}"
ISSUER="https://token.actions.githubusercontent.com"
SAN_REGEX="https://github.com/ravishkarathnayaka/Enterprise-Software-Supply-Chain-Security-SLSA-Level-3-Pipeline/.github/workflows/security-pipeline.yml@refs/heads/main"

echo "Verifying keyless signature for: ${IMAGE_REF}..."
cosign verify \
  --certificate-identity="${SAN_REGEX}" \
  --certificate-oidc-issuer="${ISSUER}" \
  "${IMAGE_REF}"

echo "[SUCCESS] Keyless cryptographic signature verified on Rekor transparency log."
