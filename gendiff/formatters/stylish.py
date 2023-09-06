CONVERTING_VALUE = {False: 'false', None: 'null', True: 'true'}


def convert_value(value):
    return CONVERTING_VALUE.get(value, value)


def stylish(data, indent_size=4, depth=0):
    result = []
    sign = ''
    indent = ''
    result.append('{\n')
    for elem in data:
        if isinstance(elem, dict):
            if elem['meta'] not in data:
                sign = '  '
            match elem['meta']:
                case 'added':
                    sign = '+ '
                case 'deleted':
                    sign = '- '
                case 'unchanged':
                    sign = '  '
                case 'changed-':
                    sign = '- '
                case 'changed+':
                    sign = '+ '    
            indent =  ' ' * (depth * indent_size-2) + sign if depth > 0 else ' ' * (indent_size-2) + sign
            if isinstance(elem['value'], dict):
                result.append(f'{indent}  {elem["key"]}: {stylish(elem["value"], indent_size, depth+1)}')
            elif elem['meta'] == 'children':
                result.append(f'{indent}  {elem["key"]}: {stylish(elem["value"], indent_size, depth +1)}')
            else:
                result.append(f'{indent}  {elem["key"]}: {elem["value"]}\n')
        else:
            indent =  ' ' * (depth * indent_size-2) + sign if depth > 0 else ' ' * (indent_size-2) + sign
            result.append(f'{indent}  {elem}: {data[elem]}\n')
    indent =  ' ' * (depth * indent_size)
    result.append(indent + '}\n')           
    return ''.join(result)
               




