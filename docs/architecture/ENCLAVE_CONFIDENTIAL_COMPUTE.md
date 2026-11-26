# Confidential Computing Enclaves for Cryptographic Attestation Signing

## Architecture Overview
To eliminate hypervisor and host OS compromise vectors during SLSA artifact signing, signing keys execute strictly within hardware-isolated Trusted Execution Environments (TEEs):

- **Supported Enclaves**: AWS Nitro Enclaves, AMD SEV-SNP, Intel SGX.
- **Hardware Root of Trust**: Asymmetric keying material never resides in plaintext host memory.
- **Remote Attestation**: Before granting signing authority, the KMS verifies cryptographic measurement quotes against golden PCR (Platform Configuration Register) hashes.
