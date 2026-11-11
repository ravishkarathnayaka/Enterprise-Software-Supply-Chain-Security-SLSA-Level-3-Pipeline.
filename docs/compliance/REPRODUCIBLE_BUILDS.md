# Deterministic & Reproducible Container Builds

## 1. Motivation
A build is **reproducible** if given the exact same source code, build environment, and build instructions, it produces bit-for-bit identical output artifacts. Reproducibility ensures that no rogue compilation artifacts or backdoors are covertly introduced during builds.

---

## 2. Techniques Enforced in Dockerfile

### 1. Uniform Timestamps (`SOURCE_DATE_EPOCH`)
Timestamps inside compiled files and container layers are normalized to a fixed epoch based on the git commit timestamp:
```dockerfile
ARG SOURCE_DATE_EPOCH
ENV SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH}
```

### 2. Deterministic File Ordering
Tarballs and archive layers sort directory listings alphabetically to eliminate file system traversal nondeterminism.

### 3. Pinned Distroless Base Digest
Base images are pinned strictly by SHA-256 digest rather than rolling tags:
```dockerfile
FROM gcr.io/distroless/python3-debian12@sha256:41656820ff569d675da...
```

### 4. Pinned Python Wheels
All dependencies are pinned with exact versions and cryptographic hashes in `requirements.txt`.
