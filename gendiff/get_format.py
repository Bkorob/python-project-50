from .formatters.stylish import stylish
from .formatters.plain import plain
from .formatters.json import json

def get_format(format):
    if format == 'plain':
        return plain
    if format == 'json':
        return json
    return stylish
