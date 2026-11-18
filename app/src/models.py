"""Shared Pydantic v2 Domain Models for Supply Chain Entities.

Provides strict models for SBOM packages, In-Toto attestations, and compliance summaries.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class SbomComponent(BaseModel):
    name: str = Field(..., min_length=1, max_length=128)
    version: str = Field(..., min_length=1, max_length=64)
    purl: str = Field(..., description="Package URL (purl)")
    license: Optional[str] = "UNKNOWN"


class SbomSummaryResponse(BaseModel):
    component_count: int
    format: str = "CycloneDX-1.5"
    components: List[SbomComponent]
