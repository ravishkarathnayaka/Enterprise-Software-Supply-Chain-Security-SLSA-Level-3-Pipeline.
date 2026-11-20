#!/usr/bin/env bash
# ==============================================================================
# In-Toto SLSA Provenance Generation Utility
# ==============================================================================
set -euo pipefail

IMAGE_REF="${1:-app:latest}"
OUTPUT_FILE="${2:-predicate.json}"

echo "Generating SLSA v0.2 provenance predicate for ${IMAGE_REF}..."
cat <<EOF > "${OUTPUT_FILE}"
{
  "builder": {"id": "https://github.com/actions/runner"},
  "buildType": "https://github.com/actions/runner/v1",
  "invocation": {"configSource": {"uri": "git+https://github.com/ravishkarathnayaka/pipeline"}}
}
EOF

echo "[SUCCESS] Provenance predicate written to ${OUTPUT_FILE}."
