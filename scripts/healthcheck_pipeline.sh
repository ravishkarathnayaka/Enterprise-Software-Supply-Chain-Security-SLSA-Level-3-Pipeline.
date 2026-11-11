#!/usr/bin/env bash
# ==============================================================================
# Pipeline Prerequisites & Health Checker
# ==============================================================================
set -euo pipefail

TOOLS=("git" "docker" "cosign" "syft" "trivy" "kubectl" "helm")
echo "Validating required supply chain toolchain..."

for tool in "${TOOLS[@]}"; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "  [FOUND] $tool: $(command -v "$tool")"
    else
        echo "  [MISSING] $tool is not installed or not in PATH."
    fi
done

echo "Environment audit complete."
