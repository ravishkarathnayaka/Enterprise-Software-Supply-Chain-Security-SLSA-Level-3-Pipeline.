"""Unit tests for CVEDenylistFilter."""

from src.cve_denylist import CVEDenylistFilter


def test_denylist_hit():
    cves = ["CVE-2024-3094", "CVE-2024-0001"]
    res = CVEDenylistFilter.check_cves(cves)
    assert res["rejected"] is True
    assert "CVE-2024-3094" in res["blocked_cves"]


def test_denylist_clean():
    cves = ["CVE-2024-0001", "CVE-2024-0002"]
    res = CVEDenylistFilter.check_cves(cves)
    assert res["rejected"] is False
    assert res["blocked_count"] == 0
