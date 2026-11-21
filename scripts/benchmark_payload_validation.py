#!/usr/bin/env python3
"""Benchmark payload parsing and DSSE envelope decoding rate."""

import json
import time


def benchmark(iterations: int = 1000):
    statement = {
        "_type": "https://in-toto.io/Statement/v0.1",
        "subject": [{"name": "app", "digest": {"sha256": "0" * 64}}],
        "predicateType": "https://slsa.dev/provenance/v1",
        "predicate": {
            "buildDefinition": {
                "buildType": "https://slsa.dev/container-based-build/v0.1"
            }
        },
    }
    serialized = json.dumps(statement)
    start = time.perf_counter()
    for _ in range(iterations):
        _ = json.loads(serialized)
    elapsed = time.perf_counter() - start
    ops_per_sec = iterations / elapsed if elapsed > 0 else 0
    print(
        f"Decoded {iterations} statements in {elapsed:.4f}s ({ops_per_sec:.2f} ops/sec)"
    )


if __name__ == "__main__":
    benchmark()
