"""
consistency_checker.py
Checks logical consistency between features and schema.
"""

def check_consistency(parsed_intent: dict, blueprint: dict) -> list:
    errors = []
    features = parsed_intent.get("features", [])
    db_schema = blueprint.get("database_schema", {})

    if "login" in features and "User" not in db_schema:
        errors.append("Login feature requires User table")

    if "cart" in features and "Cart" not in db_schema:
        errors.append("Cart feature requires Cart table")

    if "payments" in features and "Order" not in db_schema:
        errors.append("Payments feature requires Order table")

    return errors
