"""
nlp_parser.py
Responsible for extracting app intent from natural language input.
"""

def parse_user_input(user_text: str) -> dict:
    """
    Parses user input text and extracts app type, features, and roles.
    """

    text = user_text.lower()

    # --- Detect app type ---
    if "food" in text:
        app_type = "food_delivery"
    elif "ecommerce" in text or "shopping" in text:
        app_type = "ecommerce"
    elif "fitness" in text:
        app_type = "fitness"
    else:
        app_type = "generic"

    # --- Detect features ---
    features = []

    feature_keywords = {
        "login": ["login", "sign in", "authentication"],
        "cart": ["cart", "basket"],
        "payments": ["payment", "payments", "checkout"],
        "profile": ["profile", "user profile"],
    }

    for feature, keywords in feature_keywords.items():
        if any(keyword in text for keyword in keywords):
            features.append(feature)

    # --- Detect roles ---
    roles = ["user"]
    if "admin" in text or "dashboard" in text:
        roles.append("admin")
    else:
        roles.append("admin")  # default admin role

    return {
        "app_type": app_type,
        "features": features,
        "roles": roles
    }
