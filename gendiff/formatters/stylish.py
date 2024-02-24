from json import dumps


INDENTS = {'added': '+ ',
           'removed': '- ',
           'unchanged': '  ',
           'nested': '  ',
           }
DEFAULT_INDENT = 4


def convert_value(value, depth):
    if isinstance(value, bool) or value is None:
        return dumps(value)
    elif isinstance(value, dict):
        result = ['{']
        indent = get_indent("  ", depth)
        for key, val in value.items():
            if isinstance(val, dict):
                result.append(f'{indent}{key}: '
                              f'{convert_value(val, depth + 1)}')
            else:
                result.append(f'{indent}{key}: {convert_value(val, depth + 1)}')
        result.append(get_indent('  ', depth - 1) + '}')
        return '\n'.join(result)
    return value


def get_indent(sign, depth, sep=' '):
    indent_size = (DEFAULT_INDENT * depth) - 2
    if indent_size < 0:
        indent = ''
        return indent
    indent = indent_size * sep + INDENTS.get(sign, sign)
    return indent


def stylish(data, depth=1):
    result = ['{']
    for elem in data:
        key = elem['key']
        value = elem['value']
        meta = elem['meta']
        indent = get_indent(meta, depth)
        if meta == 'nested':
            result.append(f'{indent}{key}: {stylish(value, depth + 1)}')
        elif meta == 'changed':
            result.append(f'{get_indent("- ", depth)}{key}: '
                          f'{convert_value(value[0], depth + 1)}')
            result.append(f'{get_indent("+ ", depth)}{key}: '
                          f'{convert_value(value[1], depth + 1)}')
        else:
            result.append(f'{indent}{key}: {convert_value(value, depth + 1)}')
    result.append(get_indent('  ', depth - 1) + '}')
    return '\n'.join(result)
