#!/usr/bin/env bash
# ==============================================================================
# Automated CycloneDX v1.5 SBOM Generation & Inspection
# ==============================================================================
set -euo pipefail

TARGET_IMAGE="${1:-ghcr.io/ravishkarathnayaka/enterprise-supply-chain-app:latest}"
OUTPUT_FILE="${2:-cyclonedx-sbom.json}"

echo "Generating CycloneDX SBOM for: ${TARGET_IMAGE}..."
syft "${TARGET_IMAGE}" -o cyclonedx-json="${OUTPUT_FILE}"

PACKAGE_COUNT=$(jq '.components | length' "${OUTPUT_FILE}")
echo "[SUCCESS] CycloneDX SBOM generated at ${OUTPUT_FILE} with ${PACKAGE_COUNT} components cataloged."
