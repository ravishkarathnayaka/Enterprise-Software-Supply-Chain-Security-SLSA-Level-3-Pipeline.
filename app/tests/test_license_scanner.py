"""Unit tests for LicenseRiskScanner."""

from src.license_scanner import LicenseRiskScanner


def test_license_scanner_permissive():
    components = [
        {"name": "fastapi", "license": "MIT"},
        {"name": "pydantic", "license": "Apache-2.0"},
    ]
    res = LicenseRiskScanner.evaluate_licenses(components)
    assert res["compliant"] is True
    assert res["flagged_count"] == 0


def test_license_scanner_flags_copyleft():
    components = [
        {"name": "viral-lib", "license": "AGPL-3.0"},
    ]
    res = LicenseRiskScanner.evaluate_licenses(components)
    assert res["compliant"] is False
    assert res["flagged_count"] == 1
    assert res["flagged_packages"][0]["risk"] == "HIGH_COPYLEFT"
