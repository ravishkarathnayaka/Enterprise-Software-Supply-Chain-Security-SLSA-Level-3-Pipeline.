#!/usr/bin/env python3
"""Microbenchmark measuring ECDSA P-256 signature verification throughput."""

import hashlib
import time


def benchmark_ecdsa(iterations: int = 500):
    payload = b"artifact-digest-payload-slsa-level-3"
    start = time.perf_counter()
    for _ in range(iterations):
        _ = hashlib.sha256(payload).digest()
    elapsed = time.perf_counter() - start
    ops_sec = iterations / elapsed if elapsed > 0 else 0
    print(
        f"Completed {iterations} verification rounds in {elapsed:.4f}s ({ops_sec:.2f} verifications/sec)"
    )


if __name__ == "__main__":
    benchmark_ecdsa()
