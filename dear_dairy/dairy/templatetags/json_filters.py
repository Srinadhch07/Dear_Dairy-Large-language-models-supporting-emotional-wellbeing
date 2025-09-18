import json
from django import template

register = template.Library()

@register.filter
def json_loads(value):
    """
    Parses a JSON string and returns a Python object.
    """
    try:
        return json.loads(value)
    except (TypeError, json.JSONDecodeError):
        return None