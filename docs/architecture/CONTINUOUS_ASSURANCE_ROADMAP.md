# Continuous Cryptographic Assurance & SLSA Level 4 Roadmap (2027)

## Architectural Vision
Building upon the established SLSA Level 3 certified pipeline, the 2027 continuous assurance roadmap targets:

1. **Hardware Enclave Build Hermeticity**: Full migration of GitHub Actions self-hosted builders to AWS Nitro Enclaves with cryptographic PCR verification.
2. **Post-Quantum Cryptography (PQC)**: Transitioning Sigstore Cosign keys from ECDSA NIST P-256 to ML-DSA (CRYSTALS-Dilithium) and ML-KEM (CRYSTALS-Kyber).
3. **Automated Continuous Re-Attestation**: Dynamic admission controllers continually verifying live workload memory integrity via eBPF.
