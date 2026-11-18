"""Unit tests for Pydantic domain models."""

import pytest
from pydantic import ValidationError
from src.models import SbomComponent


def test_sbom_component_valid():
    c = SbomComponent(
        name="fastapi",
        version="0.110.0",
        purl="pkg:pypi/fastapi@0.110.0",
        license="MIT",
    )
    assert c.name == "fastapi"
    assert c.license == "MIT"


def test_sbom_component_invalid_length():
    with pytest.raises(ValidationError):
        SbomComponent(
            name="",
            version="1.0",
            purl="pkg:pypi/test@1.0",
        )
