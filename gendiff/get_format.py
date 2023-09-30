from .formatters.stylish import stylish
from .formatters.plain import plain


def get_format(format):
    if format == 'plain':
        return plain
    return stylish