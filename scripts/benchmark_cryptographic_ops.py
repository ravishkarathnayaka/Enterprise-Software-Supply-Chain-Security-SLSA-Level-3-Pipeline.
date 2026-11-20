#!/usr/bin/env python3
"""Cryptographic verification latency benchmarking utility."""

import hashlib
import time


def benchmark_sha256(payload_size_mb: int = 10):
    data = b"0" * (payload_size_mb * 1024 * 1024)
    start = time.perf_counter()
    digest = hashlib.sha256(data).hexdigest()
    elapsed = time.perf_counter() - start
    print(f"Hashed {payload_size_mb} MB with SHA-256 in {elapsed*1000:.2f} ms")


if __name__ == "__main__":
    benchmark_sha256()
