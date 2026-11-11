"""Unit tests for CSP nonce and header builder."""

from src.csp import generate_csp_nonce, build_strict_csp_header


def test_nonce_generation():
    n1 = generate_csp_nonce()
    n2 = generate_csp_nonce()
    assert len(n1) > 10
    assert n1 != n2


def test_csp_header_format():
    nonce = generate_csp_nonce()
    header = build_strict_csp_header(nonce)
    assert f"'nonce-{nonce}'" in header
    assert "default-src 'none'" in header
    assert "frame-ancestors 'none'" in header
