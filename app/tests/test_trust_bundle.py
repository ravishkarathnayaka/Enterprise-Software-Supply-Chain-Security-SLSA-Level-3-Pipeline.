"""Unit tests for TrustBundleManager."""

from src.trust_bundle import TrustBundleManager


def test_trust_bundle_lookup():
    mgr = TrustBundleManager()
    assert mgr.is_root_trusted("sigstore-fulcio-root-v1") is True
    assert mgr.is_root_trusted("unknown-untrusted-ca") is False


def test_trust_bundle_summary():
    mgr = TrustBundleManager()
    summary = mgr.get_bundle_summary()
    assert summary["active_roots_count"] >= 2
    assert summary["status"] == "HEALTHY"
