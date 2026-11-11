"""Unit tests for RFC 7807 problem details generator."""

from src.errors import create_problem_details


def test_problem_details_structure():
    response = create_problem_details(
        status_code=400,
        title="Invalid Signature",
        detail="The cryptographic signature could not be verified against Fulcio root.",
        instance="/api/v1/verify-data",
    )
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/problem+json"
