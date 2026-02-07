"""
output_formatter.py
Ensures blueprint output is clean, readable, and JSON-serializable.
"""

import json


def format_blueprint(blueprint: dict) -> str:
    """
    Formats blueprint dictionary into pretty JSON string.
    """
    import json
    return json.dumps(blueprint, indent=4)
