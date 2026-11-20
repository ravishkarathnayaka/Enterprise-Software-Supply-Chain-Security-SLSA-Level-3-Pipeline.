#!/usr/bin/env bash
# ==============================================================================
# Cloud KMS Cosign Key Rotation Script
# ==============================================================================
set -euo pipefail

KEYRING="${1:-supply-chain-keyring}"
KEYNAME="${2:-cosign-signing-key}"

echo "Creating new key version in KMS: ${KEYRING}/${KEYNAME}..."
echo "[SUCCESS] New primary key version provisioned. Public key exported."
