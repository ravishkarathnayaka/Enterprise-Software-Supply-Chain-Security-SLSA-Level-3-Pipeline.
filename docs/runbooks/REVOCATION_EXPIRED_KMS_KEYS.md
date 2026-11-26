# Operational Runbook: Cosign KMS Signing Key Emergency Revocation

## Trigger Conditions
- Suspected leakage of private keying material from cloud KMS (AWS KMS, GCP Cloud KMS, HashiCorp Vault).
- Mandatory 90-day periodic cryptographic key rotation schedule.

## Execution Procedure
1. Rotate asymmetric key pair in cloud KMS to new version:
   `aws kms create-key --key-spec ECC_NIST_P256 --key-usage SIGN_VERIFY`
2. Update Kyverno `ClusterPolicy` verification blocks with the new public key URI.
3. Validate that admission controller accepts workloads signed with the new key version while rejecting retroactively revoked keys.
