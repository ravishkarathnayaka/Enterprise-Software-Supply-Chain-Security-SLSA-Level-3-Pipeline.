"""Unit tests for SecurityBenchmarkRunner."""

from src.security_benchmarks import SecurityBenchmarkRunner


def test_run_benchmark():
    res = SecurityBenchmarkRunner.run_benchmark(iterations=100)
    assert res["iterations"] == 100
    assert res["total_seconds"] > 0.0
    assert res["avg_latency_microseconds"] > 0.0
    assert res["algorithm"] == "SHA-256"
