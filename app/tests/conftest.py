"""Shared Pytest fixtures for Supply Chain Security Microservice."""

import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture(scope="session")
def test_client():
    """Provides a shared TestClient instance."""
    with TestClient(app) as client:
        yield client


@pytest.fixture
def sample_valid_digest():
    """Returns a valid 64-char hex SHA256 string."""
    return "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
