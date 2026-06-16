import requests
from jsonschema import validate, ValidationError
# Define the strict OpenAPI Contract
USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "job": {"type": "string"}
    },
    "required": ["id", "name", "job"]
}