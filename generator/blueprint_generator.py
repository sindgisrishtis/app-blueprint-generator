"""
blueprint_generator.py
Generates UI, backend APIs, DB schema, and tech stack from parsed intent.
"""

def generate_blueprint(parsed_intent: dict) -> dict:
    features = parsed_intent["features"]
    app_type = parsed_intent["app_type"]

    return {
        "ui_screens": _generate_ui_screens(features),
        "backend_apis": _generate_backend_apis(features),
        "database_schema": _generate_database_schema(features),
        "tech_stack": _recommend_tech_stack(app_type)
    }


def _generate_ui_screens(features: list) -> list:
    screens = []

    if "login" in features:
        screens.append({
            "screen": "Login",
            "components": ["email_input", "password_input", "login_button"]
        })

    screens.append({
        "screen": "Home",
        "components": ["navigation_bar", "content_feed"]
    })

    if "cart" in features:
        screens.append({
            "screen": "Cart",
            "components": ["item_list", "price_summary", "checkout_button"]
        })

    if "payments" in features:
        screens.append({
            "screen": "Payment",
            "components": ["payment_method_selector", "pay_button"]
        })

    return screens


def _generate_backend_apis(features: list) -> list:
    apis = []

    if "login" in features:
        apis.append({"POST /auth/login": "Authenticate user"})
        apis.append({"POST /auth/register": "Register new user"})

    apis.append({"GET /items": "Fetch available items"})

    if "cart" in features:
        apis.extend([
            {"GET /cart": "Get cart items"},
            {"POST /cart": "Add item to cart"},
            {"DELETE /cart/item": "Remove item from cart"}
        ])

    if "payments" in features:
        apis.append({"POST /payment": "Process payment"})

    return apis


def _generate_database_schema(features: list) -> dict:
    schema = {
        "User": ["id", "email", "password_hash", "created_at"]
    }

    if "cart" in features:
        schema["Cart"] = ["id", "user_id"]
        schema["CartItem"] = ["id", "cart_id", "item_id", "quantity"]

    if "payments" in features:
        schema["Order"] = ["id", "user_id", "total_amount", "status"]

    return schema


def _recommend_tech_stack(app_type: str) -> dict:
    return {
        "backend": "FastAPI",
        "database": "PostgreSQL",
        "frontend": "React",
        "auth": "JWT",
        "deployment": "Docker"
    }
