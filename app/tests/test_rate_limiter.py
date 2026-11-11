"""Unit tests for TokenBucketRateLimiter logic."""

from src.rate_limiter import TokenBucketRateLimiter


def test_rate_limiter_allows_and_blocks():
    # max 2 tokens, refills 0 per sec
    limiter = TokenBucketRateLimiter(app=None, max_tokens=2, refill_rate_per_sec=0.0)
    ip = "192.168.1.10"

    assert limiter._allow_request(ip) is True  # 1st request
    assert limiter._allow_request(ip) is True  # 2nd request
    assert limiter._allow_request(ip) is False  # 3rd request exhausted
