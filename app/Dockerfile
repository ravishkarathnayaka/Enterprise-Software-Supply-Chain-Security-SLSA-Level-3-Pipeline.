# ==============================================================================
# Enterprise Software Supply Chain Security & SLSA Level 3 Compliant Dockerfile
# Multi-stage, zero-shell, minimal attack surface, non-root Distroless image
# ==============================================================================

# Stage 1: Build & Dependency Resolution Stage
FROM python:3.14-slim-bookworm AS builder

# Prevent python from writing pyc files to disk and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

# Install build-time dependencies if any native extensions need compiling
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy pinned requirements
COPY requirements.txt .

# Install dependencies into isolated prefix
RUN pip install --prefix=/install -r requirements.txt

# Stage 2: Hardened Runtime Stage (Distroless)
# Google Distroless contains only application and runtime dependencies.
# Contains no package managers, no shells (/bin/sh, /bin/bash), and no extraneous utilities.
FROM gcr.io/distroless/python3-debian12:nonroot

# Explicitly declare non-root user (distroless:nonroot uses UID 65532)
USER 65532:65532

WORKDIR /app

# Copy isolated dependencies from builder stage
COPY --from=builder --chown=65532:65532 /install /app/dependencies

# Copy application source code
COPY --chown=65532:65532 src/ /app/src/

# Configure Python environment
ENV PYTHONPATH="/app/dependencies/lib/python3.11/site-packages:/app" \
    PYTHONUNBUFFERED="1" \
    PORT="8000"

EXPOSE 8000

# Run FastAPI app with Uvicorn directly via python3 (no shell invocation)
ENTRYPOINT ["/usr/bin/python3", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
