#!/usr/bin/env bash
# ==============================================================================
# Generate SBOM & Cryptographic Attestations (Local Lab Helper)
# Builds image, runs Syft for SPDX/CycloneDX, signs with Cosign, creates attestations
# ==============================================================================
set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

IMAGE_TAG="localhost:5001/secure-app:v1.0.0"
KEY_FILE="cosign.key"
PUB_FILE="cosign.pub"
export COSIGN_PASSWORD="${COSIGN_PASSWORD:-devsecops-secret}"

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# ------------------------------------------------------------------------------
# 1. Cosign Keypair Generation
# ------------------------------------------------------------------------------
if [ ! -f "${KEY_FILE}" ] || [ ! -f "${PUB_FILE}" ]; then
  log_info "Generating local Cosign cryptographic keypair..."
  if command -v cosign &> /dev/null; then
    cosign generate-key-pair
  else
    log_info "Cosign not found locally; running via container..."
    docker run --rm -v "${PWD}:/work" -w /work -e COSIGN_PASSWORD="${COSIGN_PASSWORD}" \
      gcr.io/projectsigstore/cosign:v2.4.1 generate-key-pair
  fi
  log_success "Generated ${KEY_FILE} and ${PUB_FILE}."
else
  log_info "Existing Cosign keypair detected (${KEY_FILE}, ${PUB_FILE})."
fi

# ------------------------------------------------------------------------------
# 2. Build and Push Container Image to Local Registry
# ------------------------------------------------------------------------------
log_info "Building hardened Distroless container image '${IMAGE_TAG}'..."
docker build -t "${IMAGE_TAG}" ./app

log_info "Pushing container image to local registry on localhost:5001..."
docker push "${IMAGE_TAG}"
log_success "Image pushed successfully."

# ------------------------------------------------------------------------------
# 3. SBOM Generation with Syft
# ------------------------------------------------------------------------------
log_info "Extracting Software Bill of Materials (SBOM) using Syft..."
if command -v syft &> /dev/null; then
  syft "${IMAGE_TAG}" -o spdx-json=sbom.spdx.json
  syft "${IMAGE_TAG}" -o cyclonedx-json=sbom.cdx.json
else
  log_info "Syft not found locally; running via container..."
  docker run --rm --net=host -v "${PWD}:/work" -w /work \
    anchore/syft:latest "${IMAGE_TAG}" -o spdx-json=sbom.spdx.json
  docker run --rm --net=host -v "${PWD}:/work" -w /work \
    anchore/syft:latest "${IMAGE_TAG}" -o cyclonedx-json=sbom.cdx.json
fi
log_success "Generated sbom.spdx.json and sbom.cdx.json."

# ------------------------------------------------------------------------------
# 4. Sign Image with Cosign
# ------------------------------------------------------------------------------
log_info "Signing container image with Cosign private key..."
if command -v cosign &> /dev/null; then
  cosign sign --yes --key "${KEY_FILE}" "${IMAGE_TAG}"
else
  docker run --rm --net=host -v "${PWD}:/work" -w /work -e COSIGN_PASSWORD="${COSIGN_PASSWORD}" \
    gcr.io/projectsigstore/cosign:v2.4.1 sign --yes --key "${KEY_FILE}" "${IMAGE_TAG}"
fi
log_success "Container image cryptographically signed."

# ------------------------------------------------------------------------------
# 5. Attest SBOM Predicate
# ------------------------------------------------------------------------------
log_info "Attesting SPDX SBOM predicate to container image..."
if command -v cosign &> /dev/null; then
  cosign attest --yes --key "${KEY_FILE}" --predicate sbom.spdx.json --type spdxjson "${IMAGE_TAG}"
else
  docker run --rm --net=host -v "${PWD}:/work" -w /work -e COSIGN_PASSWORD="${COSIGN_PASSWORD}" \
    gcr.io/projectsigstore/cosign:v2.4.1 attest --yes --key "${KEY_FILE}" --predicate sbom.spdx.json --type spdxjson "${IMAGE_TAG}"
fi
log_success "SBOM attestation successfully recorded in registry."

# ------------------------------------------------------------------------------
# 6. Synchronize Public Key into Kyverno ClusterPolicy
# ------------------------------------------------------------------------------
if command -v kubectl &> /dev/null; then
  log_info "Updating Kyverno ClusterPolicy with generated public key..."
  PUB_KEY_CONTENT=$(sed 's/^/            /' "${PUB_FILE}")
  
  cat <<EOF | kubectl apply -f -
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-image-signature
  annotations:
    policies.kyverno.io/title: Verify Cosign Image Signatures
    policies.kyverno.io/category: Software Supply Chain Security
    policies.kyverno.io/severity: critical
spec:
  validationFailureAction: Enforce
  webhookTimeoutSeconds: 30
  rules:
    - name: verify-local-image-signature
      match:
        any:
          - resources:
              kinds:
                - Pod
              namespaces:
                - secure-workloads
      verifyImages:
        - imageReferences:
            - "localhost:5001/*"
            - "kind-registry:5000/*"
          mutateDigest: false
          required: true
          key: |-
${PUB_KEY_CONTENT}
EOF
  log_success "Kyverno image signature policy updated with active public key."
fi

log_success "=================================================================="
log_success " Image Signing & Attestation Complete!"
log_success " Signed Image: ${IMAGE_TAG}"
log_success " SBOM Files:   sbom.spdx.json, sbom.cdx.json"
log_success " Public Key:   ${PUB_FILE}"
log_success "=================================================================="
