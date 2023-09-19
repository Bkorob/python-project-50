CONVERTING_VALUE = {
        False: 'false',
        None: 'null', 
        True: 'true'
        }
INDENTS = {
    'added': '+ ', 
    'deleted': '- ', 
    'unchanged': '  ',
    'children': '  '
    }
DEFAULT_INDENT = 4


def convert_value(value):
    if isinstance(value, bool) or value == None:
        return CONVERTING_VALUE[value]
    return value


def get_indent(sign, depth, sep = ' '):
    indent_size = (DEFAULT_INDENT * depth) - 2
    if indent_size < 0:
        indent = ''
        return indent
    indent = indent_size * sep + INDENTS.get(sign, '  ')
    return indent


def get_sign(value):
    count = 1
    if value['meta'] == 'added':
        return '+ '
    elif value['meta'] == 'deleted':
        return '- '
    elif value['meta'] == 'changed':
        count +=1
        return '- ' if count//2 else '+ '
    else:
        return '  '


def stylish(data, depth=1):
    result = []
    result.append('{')
    for elem in data:
        if isinstance(elem, dict):
            key = elem['key']
            value = elem['value']  
            if isinstance(value, dict):
                result.append(f'{get_indent(elem["meta"], depth)}{key}: {stylish(value, depth+1)}')
            elif elem['meta'] == 'children':
                result.append(f'{get_indent(elem["meta"], depth)}{key}: {stylish(value, depth +1)}')
            else:
                result.append(f'{get_indent(elem["meta"], depth)}{key}: {convert_value(value)}')
        else:
            if isinstance(data[elem], dict):
                result.append(f'{get_indent("  ", depth)}{elem}: {stylish(data[elem], depth+1)}')
            else:
                result.append(f'{get_indent("  ", depth)}{elem}: {convert_value(data[elem])}')            
    result.append(get_indent('  ', depth-1) + '}')           
    return '\n'.join(result)
