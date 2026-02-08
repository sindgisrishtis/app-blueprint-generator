from fastapi import FastAPI
from pydantic import BaseModel

from generator.nlp_parser import parse_user_input
from generator.blueprint_generator import generate_blueprint
from validator.schema_validator import validate_schema
from validator.consistency_checker import check_consistency

app = FastAPI(title="App Blueprint Generator")


class AppRequest(BaseModel):
    description: str


@app.post("/generate-blueprint")
def generate_app_blueprint(request: AppRequest):
    parsed_intent = parse_user_input(request.description)
    blueprint = generate_blueprint(parsed_intent)

    schema_errors = validate_schema(blueprint)
    consistency_errors = check_consistency(parsed_intent, blueprint)

    errors = schema_errors + consistency_errors

    return {
        "parsed_intent": parsed_intent,
        "blueprint": blueprint,
        "errors": errors
    }
