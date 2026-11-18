#!/usr/bin/env bash
# ==============================================================================
# Automated SPDX 2.3 JSON SBOM Generation (ISO/IEC 5962:2021)
# ==============================================================================
set -euo pipefail

IMAGE_REF="${1:-ghcr.io/ravishkarathnayaka/enterprise-supply-chain-app:latest}"
OUTPUT_PATH="${2:-spdx-sbom.json}"

echo "Generating ISO-compliant SPDX 2.3 SBOM for: ${IMAGE_REF}..."
syft "${IMAGE_REF}" -o spdx-json="${OUTPUT_PATH}"

echo "[SUCCESS] SPDX 2.3 SBOM successfully created at ${OUTPUT_PATH}."
