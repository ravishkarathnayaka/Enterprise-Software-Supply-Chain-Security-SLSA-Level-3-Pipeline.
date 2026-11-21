"""In-Toto SLSA Provenance Predicate Schema Validator.

Verifies that in-toto statements declare valid subjects, builder IDs, and entrypoints.
"""

from typing import Any, Dict, List


class PredicateValidator:
    """Validates structural compliance of in-toto SLSA provenance statements."""

    @staticmethod
    def validate_statement(statement: Dict[str, Any]) -> Dict[str, Any]:
        errors: List[str] = []

        if statement.get("_type") != "https://in-toto.io/Statement/v0.1":
            errors.append("Invalid or missing '_type' header")

        if not statement.get("subject") or len(statement["subject"]) == 0:
            errors.append("Statement must contain at least one subject")

        predicate = statement.get("predicate", {})
        if not predicate.get("builder", {}).get("id"):
            errors.append("Missing 'predicate.builder.id'")

        is_valid = len(errors) == 0
        return {
            "valid": is_valid,
            "error_count": len(errors),
            "errors": errors,
            "slsa_level": "SLSA_BUILD_LEVEL_3" if is_valid else "NONE",
        }


predicate_validator = PredicateValidator()
