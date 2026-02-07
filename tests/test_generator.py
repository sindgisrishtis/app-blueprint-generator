from generator.nlp_parser import parse_user_input
from generator.blueprint_generator import generate_blueprint


def test_food_delivery_app():
    user_input = "Food delivery app with login, cart and payments"
    parsed = parse_user_input(user_input)
    blueprint = generate_blueprint(parsed)

    assert "ui_screens" in blueprint
    assert "backend_apis" in blueprint
    assert "database_schema" in blueprint
    assert "tech_stack" in blueprint
