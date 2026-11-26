# ISO/IEC 27001:2022 Annex A.8: Technological Controls Mapping

## Control Alignment Matrix
- **Control A.8.25: Secure Development Life Cycle**: Formally defined SLSA Level 3 CI/CD pipeline with segregated build phases.
- **Control A.8.28: Secure Coding**: Semgrep security rule sets enforcing memory safety, input sanitization, and parameterized execution.
- **Control A.8.30: Outsourced Development**: Rigorous dependency screening and hash verification against public PyPI and container registries.
- **Control A.8.31: Separation of Development, Testing and Production**: Immutable container promotions via cryptographic signatures rather than rebuilding code.
