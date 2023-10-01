from .formatters.stylish import stylish
from .formatters.plain import plain
from .formatters.json import get_json


def get_format(format):
    if format == 'plain':
        return plain
    if format == 'json':
        return get_json
    return stylish
