#!/usr/bin/env bash
# ==============================================================================
# Admission Control Automated Test Harness
# Validates: PSS Restricted + Kyverno Rules (Privileged, RootFS, Signatures)
# ==============================================================================
set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m'

NAMESPACE="secure-workloads"
PASSED_TESTS=0
TOTAL_TESTS=5

log_step() { echo -e "\n${BOLD}${BLUE}>>> [TEST $1/$TOTAL_TESTS] $2${NC}"; }
log_pass() { echo -e "${GREEN}[PASSED - EXPECTED BEHAVIOR]${NC} $1"; ((PASSED_TESTS++)); }
log_fail() { echo -e "${RED}[FAILED - UNEXPECTED ADMISSION RESULT]${NC} $1"; }

# ------------------------------------------------------------------------------
# Test 1: Reject Privileged Container
# ------------------------------------------------------------------------------
log_step 1 "Attempting deployment of a PRIVILEGED container..."
REJECTION_MSG=$(kubectl run test-privileged \
  --namespace="${NAMESPACE}" \
  --image="localhost:5001/secure-app:v1.0.0" \
  --restart=Never \
  --overrides='{"spec":{"containers":[{"name":"test","image":"localhost:5001/secure-app:v1.0.0","securityContext":{"privileged":true}}]}}' 2>&1 || true)

if echo "${REJECTION_MSG}" | grep -E -q "(disallow-privileged|violates PodSecurity|forbidden|blocked|denied)"; then
  log_pass "Privileged container was successfully blocked by admission controller."
  echo "    Admission Error Snippet: $(echo "${REJECTION_MSG}" | head -n 2)"
else
  log_fail "Privileged container was NOT blocked! Output: ${REJECTION_MSG}"
fi
kubectl delete pod test-privileged --namespace="${NAMESPACE}" --ignore-not-found=true 2>/dev/null || true

# ------------------------------------------------------------------------------
# Test 2: Reject Writable Root Filesystem
# ------------------------------------------------------------------------------
log_step 2 "Attempting deployment with a WRITABLE root filesystem..."
REJECTION_MSG=$(kubectl run test-writable-rootfs \
  --namespace="${NAMESPACE}" \
  --image="localhost:5001/secure-app:v1.0.0" \
  --restart=Never \
  --overrides='{"spec":{"containers":[{"name":"test","image":"localhost:5001/secure-app:v1.0.0","securityContext":{"readOnlyRootFilesystem":false,"allowPrivilegeEscalation":false,"runAsNonRoot":true,"runAsUser":65532,"capabilities":{"drop":["ALL"]}}}]}}' 2>&1 || true)

if echo "${REJECTION_MSG}" | grep -E -q "(require-ro-rootfs|readOnlyRootFilesystem|forbidden|blocked|denied)"; then
  log_pass "Writable root filesystem container was successfully blocked."
  echo "    Admission Error Snippet: $(echo "${REJECTION_MSG}" | head -n 2)"
else
  log_fail "Writable rootfs was NOT blocked! Output: ${REJECTION_MSG}"
fi
kubectl delete pod test-writable-rootfs --namespace="${NAMESPACE}" --ignore-not-found=true 2>/dev/null || true

# ------------------------------------------------------------------------------
# Test 3: Reject Root User (UID 0) Execution
# ------------------------------------------------------------------------------
log_step 3 "Attempting deployment running as ROOT user (UID 0)..."
REJECTION_MSG=$(kubectl run test-root-user \
  --namespace="${NAMESPACE}" \
  --image="localhost:5001/secure-app:v1.0.0" \
  --restart=Never \
  --overrides='{"spec":{"containers":[{"name":"test","image":"localhost:5001/secure-app:v1.0.0","securityContext":{"runAsUser":0,"runAsNonRoot":false,"readOnlyRootFilesystem":true,"allowPrivilegeEscalation":false,"capabilities":{"drop":["ALL"]}}}]}}' 2>&1 || true)

if echo "${REJECTION_MSG}" | grep -E -q "(runAsNonRoot|root user|UID 0|forbidden|blocked|denied)"; then
  log_pass "Root user container was successfully blocked."
  echo "    Admission Error Snippet: $(echo "${REJECTION_MSG}" | head -n 2)"
else
  log_fail "Root user container was NOT blocked! Output: ${REJECTION_MSG}"
fi
kubectl delete pod test-root-user --namespace="${NAMESPACE}" --ignore-not-found=true 2>/dev/null || true

# ------------------------------------------------------------------------------
# Test 4: Reject Unsigned Container Image
# ------------------------------------------------------------------------------
log_step 4 "Attempting deployment of an UNSIGNED container image..."
# Tag and push an untrusted dummy image to local registry
docker tag alpine:latest localhost:5001/untrusted-app:unsigned 2>/dev/null || true
docker push localhost:5001/untrusted-app:unsigned 2>/dev/null || true

REJECTION_MSG=$(kubectl run test-unsigned-image \
  --namespace="${NAMESPACE}" \
  --image="localhost:5001/untrusted-app:unsigned" \
  --restart=Never \
  --overrides='{"spec":{"securityContext":{"runAsNonRoot":true,"runAsUser":65532,"seccompProfile":{"type":"RuntimeDefault"}},"containers":[{"name":"test","image":"localhost:5001/untrusted-app:unsigned","securityContext":{"readOnlyRootFilesystem":true,"allowPrivilegeEscalation":false,"runAsNonRoot":true,"runAsUser":65532,"capabilities":{"drop":["ALL"]}}}]}}' 2>&1 || true)

if echo "${REJECTION_MSG}" | grep -E -q "(verify-image-signature|no signatures found|failed to verify image|denied|forbidden)"; then
  log_pass "Unsigned container image was successfully rejected by Kyverno Cosign verification."
  echo "    Admission Error Snippet: $(echo "${REJECTION_MSG}" | head -n 2)"
else
  log_fail "Unsigned container image was NOT rejected! Output: ${REJECTION_MSG}"
fi
kubectl delete pod test-unsigned-image --namespace="${NAMESPACE}" --ignore-not-found=true 2>/dev/null || true

# ------------------------------------------------------------------------------
# Test 5: Accept Hardened & Signed Workload
# ------------------------------------------------------------------------------
log_step 5 "Deploying compliant, hardened, and signed workload..."
kubectl apply -f kubernetes/manifests/deployment.yaml

echo "Waiting for rollout to complete..."
if kubectl -n "${NAMESPACE}" rollout status deployment/secure-app --timeout=60s; then
  log_pass "Signed and hardened workload admitted and successfully running."
else
  log_fail "Hardened workload failed rollout!"
fi

# ------------------------------------------------------------------------------
# Summary Matrix
# ------------------------------------------------------------------------------
echo -e "\n${BOLD}=================================================================="
echo -e "           ADMISSION CONTROL COMPLIANCE AUDIT RESULTS"
echo -e "==================================================================${NC}"
echo -e " Tests Passed: ${GREEN}${PASSED_TESTS}/${TOTAL_TESTS}${NC}"
if [ "${PASSED_TESTS}" -eq "${TOTAL_TESTS}" ]; then
  echo -e " Status:       ${GREEN}100% ENFORCEMENT VERIFIED (SLSA / PSS Compliant)${NC}"
else
  echo -e " Status:       ${YELLOW}PARTIAL COMPLIANCE - Review failures above${NC}"
fi
echo -e "${BOLD}==================================================================${NC}"
