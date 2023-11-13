from json import dumps


INDENTS = {'added': '+ ',
           'deleted': '- ',
           'unchanged': '  ',
           'children': '  ',
           }
DEFAULT_INDENT = 4


def convert_value(value, depth):
    if isinstance(value, bool) or value is None:
        return dumps(value)
    elif isinstance(value, dict):
        key = list(value)[0]
        indent_strt = get_indent("  ", depth + 1)
        indent_fin = get_indent("  ", depth)
        value = '{\n' + (f'{indent_strt}{key}'
                         f': {value.get(key)}\n') + indent_fin + '}'
        return value
    return value


def get_indent(sign, depth, sep=' '):
    indent_size = (DEFAULT_INDENT * depth) - 2
    if indent_size < 0:
        indent = ''
        return indent
    indent = indent_size * sep + INDENTS.get(sign, sign)
    return indent


def stylish(data, depth=1):
    result = []
    result.append('{')
    for elem in data:
        if isinstance(elem, dict):
            key = elem['key']
            value = elem['value']
            meta = elem['meta']
            indent = get_indent(meta, depth)
            if isinstance(value, dict):
                result.append(f'{indent}{key}: {stylish(value, depth + 1)}')
            elif meta == 'children':
                result.append(f'{indent}{key}: {stylish(value, depth + 1)}')
            elif meta == 'changed':
                result.append(f'{get_indent("- ", depth)}{key}: '
                              f'{convert_value(value[0], depth)}')
                result.append(f'{get_indent("+ ", depth)}{key}: '
                              f'{convert_value(value[1], depth)}')
            else:
                result.append(f'{indent}{key}: {convert_value(value, depth)}')
        else:
            indent = get_indent("  ", depth)
            if isinstance(data[elem], dict):
                result.append(f'{indent}{elem}: {stylish(data[elem], depth+1)}')
            else:
                result.append(f'{indent}{elem}: {convert_value(data[elem], depth)}')
    result.append(get_indent('  ', depth - 1) + '}')
    return '\n'.join(result)
