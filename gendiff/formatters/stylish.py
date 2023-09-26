CONVERTING_VALUE = {False: 'false',
                    None: 'null',
                    True: 'true'
                    }
INDENTS = {'added': '+ ',
           'deleted': '- ',
           'unchanged': '  ',
           'children': '  ',
           'changed+': '+ ',
           'changed-': '- '
           }
DEFAULT_INDENT = 4


def convert_value(value):
    if isinstance(value, bool) or value is None:
        return CONVERTING_VALUE[value]
    return value


def get_indent(sign, depth, sep=' '):
    indent_size = (DEFAULT_INDENT * depth) - 2
    if indent_size < 0:
        indent = ''
        return indent
    indent = indent_size * sep + INDENTS.get(sign, '  ')
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
            else:
                result.append(f'{indent}{key}: {convert_value(value)}')
        else:
            indent = get_indent("  ", depth)
            if isinstance(data[elem], dict):
                result.append(f'{indent}{elem}: {stylish(data[elem], depth+1)}')
            else:
                result.append(f'{indent}{elem}: {convert_value(data[elem])}')
    result.append(get_indent('  ', depth - 1) + '}')
    return '\n'.join(result)
