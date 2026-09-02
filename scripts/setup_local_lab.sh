#!/usr/bin/env bash
# ==============================================================================
# Setup Local DevSecOps Kubernetes Lab
# Configures: Local Registry (port 5001) -> Multi-Node Kind -> Kyverno -> Policies
# ==============================================================================
set -euo pipefail

# ANSI color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

CLUSTER_NAME="devsecops-cluster"
REG_NAME="kind-registry"
REG_PORT="5001"
KYVERNO_VERSION="v1.12.5"

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# ------------------------------------------------------------------------------
# 1. Dependency Checks
# ------------------------------------------------------------------------------
log_info "Verifying required CLI tools..."
for tool in docker kind kubectl; do
  if ! command -v "$tool" &> /dev/null; then
    log_error "Missing required dependency: '$tool'. Please install it before running this script."
    exit 1
  fi
done
log_success "All prerequisite CLI tools are available."

# ------------------------------------------------------------------------------
# 2. Local Docker Registry Provisioning
# ------------------------------------------------------------------------------
log_info "Checking local container registry '${REG_NAME}' on port ${REG_PORT}..."
if [ "$(docker inspect -f '{{.State.Running}}' "${REG_NAME}" 2>/dev/null || true)" != 'true' ]; then
  log_info "Spinning up local Docker registry on port ${REG_PORT}..."
  docker run -d --restart=always -p "127.0.0.1:${REG_PORT}:5000" --network bridge --name "${REG_NAME}" registry:2
  log_success "Local Docker registry started."
else
  log_info "Local registry '${REG_NAME}' is already running."
fi

# ------------------------------------------------------------------------------
# 3. Multi-Node Kind Cluster Provisioning
# ------------------------------------------------------------------------------
log_info "Checking if Kind cluster '${CLUSTER_NAME}' exists..."
if ! kind get clusters | grep -q "^${CLUSTER_NAME}$"; then
  log_info "Creating multi-node Kind cluster '${CLUSTER_NAME}' with registry integration..."
  kind create cluster --name "${CLUSTER_NAME}" --config kubernetes/kind-config.yaml
  log_success "Kind cluster created successfully."
else
  log_info "Kind cluster '${CLUSTER_NAME}' already exists. Switching context..."
  kubectl config use-context "kind-${CLUSTER_NAME}"
fi

# Connect registry to cluster network
log_info "Connecting local registry '${REG_NAME}' to Kind Docker network..."
docker network connect "kind" "${REG_NAME}" 2>/dev/null || true

# ------------------------------------------------------------------------------
# 4. Configure Containerd Registry Mirrors on All Nodes
# ------------------------------------------------------------------------------
log_info "Configuring containerd certs.d registry endpoints on Kind nodes..."
REGISTRY_DIR="/etc/containerd/certs.d/localhost:${REG_PORT}"
for node in $(kind get nodes --name "${CLUSTER_NAME}"); do
  docker exec "${node}" mkdir -p "${REGISTRY_DIR}"
  docker exec -i "${node}" sh -c "cat <<EOF > ${REGISTRY_DIR}/hosts.toml
server = \"http://${REG_NAME}:5000\"
[host.\"http://${REG_NAME}:5000\"]
  capabilities = [\"pull\", \"resolve\"]
  skip_verify = true
EOF"
done

# Document the local registry hosting config
kubectl apply -f - <<EOF
apiVersion: v1
kind: ConfigMap
metadata:
  name: local-registry-hosting
  namespace: kube-system
data:
  localRegistryHosting.v1: |
    host: "localhost:${REG_PORT}"
    help: "https://kind.sigs.k8s.io/docs/user/local-registry/"
EOF
log_success "Containerd local registry mirror configured."

# ------------------------------------------------------------------------------
# 5. Kyverno Admission Controller Installation
# ------------------------------------------------------------------------------
log_info "Installing Kyverno ${KYVERNO_VERSION} admission controller..."
kubectl apply -f "https://github.com/kyverno/kyverno/releases/download/${KYVERNO_VERSION}/install.yaml"

log_info "Waiting for Kyverno admission controller deployment to be ready (up to 180s)..."
kubectl -n kyverno rollout status deployment/kyverno-admission-controller --timeout=180s
log_success "Kyverno admission controller is active and healthy."

# ------------------------------------------------------------------------------
# 6. Apply Namespaces and Security Policies
# ------------------------------------------------------------------------------
log_info "Applying restricted workload namespace..."
kubectl apply -f kubernetes/manifests/namespace.yaml

log_info "Applying Kyverno ClusterPolicies (Privileged, Read-Only RootFS, Image Signatures)..."
kubectl apply -f kubernetes/policies/kyverno-disallow-privileged.yaml
kubectl apply -f kubernetes/policies/kyverno-require-ro-rootfs.yaml
kubectl apply -f kubernetes/policies/kyverno-verify-image-signature.yaml

# Wait briefly for policies to be processed
sleep 5

log_success "=================================================================="
log_success " Local DevSecOps Lab Ready!"
log_success " Cluster:   ${CLUSTER_NAME}"
log_success " Registry:  localhost:${REG_PORT}"
log_success " Namespace: secure-workloads (PSS Restricted)"
log_success " Run:       ./scripts/verify_admission.sh to test admission gates"
log_success "=================================================================="
