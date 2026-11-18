#!/usr/bin/env bash
# ==============================================================================
# Batch Cluster Image Verification Auditor
# ==============================================================================
set -euo pipefail

INPUT_FILE="${1:-running_images.txt}"
if [[ ! -f "$INPUT_FILE" ]]; then
    echo "Usage: $0 <images_list.txt>"
    exit 1
fi

echo "Auditing running container images against Cosign trust roots..."
while IFS= read -r image; do
    echo "Verifying: $image"
    cosign verify --certificate-oidc-issuer="https://token.actions.githubusercontent.com" "$image" || echo "[UNVERIFIED] $image"
done < "$INPUT_FILE"
