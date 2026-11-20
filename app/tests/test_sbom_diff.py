"""Unit tests for SbomDiffer."""

from src.sbom_diff import SbomDiffer


def test_sbom_differ_detects_addition_and_modification():
    base = [{"name": "pkg-a", "version": "1.0.0"}]
    cand = [{"name": "pkg-a", "version": "1.1.0"}, {"name": "pkg-b", "version": "2.0.0"}]

    diff = SbomDiffer.compare_components(base, cand)
    assert diff["drift_detected"] is True
    assert diff["added_count"] == 1
    assert "pkg-b" in diff["added"]
    assert diff["modified_count"] == 1
    assert diff["modified"][0]["name"] == "pkg-a"
