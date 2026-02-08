"""
schema_validator.py
Validates the structure of generated blueprints.
"""

REQUIRED_TOP_LEVEL_KEYS = [
    "ui_screens",
    "backend_apis",
    "database_schema",
    "tech_stack"
]


def validate_schema(blueprint: dict) -> list:
    """
    Validates required top-level fields.
    Returns a list of errors (empty if valid).
    """
    errors = []

    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in blueprint:
            errors.append(f"Missing required field: {key}")

    return errors
