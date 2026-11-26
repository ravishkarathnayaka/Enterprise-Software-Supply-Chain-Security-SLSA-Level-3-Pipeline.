# Attack Surface Analysis: SBOM Poisoning & Omission Vectors

## Threat Profile
An attacker with compromised build tool access may manipulate CycloneDX/SPDX generation tools to:
- Omit vulnerable or backdoored components from the generated bill of materials.
- Substitute clean dependency hashes in place of compromised artifacts.

## Mitigations Implemented
1. **Multi-Engine Generation**: Independent generation using CycloneDX and SPDX generators.
2. **Cryptographic Attestation**: The SBOM itself is attached as an in-toto predicate and signed with Cosign.
3. **Lockfile Cross-Verification**: The CI runner reconciles SBOM components against pinned lockfiles.
