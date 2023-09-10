CONVERTING_VALUE = {False: 'false', None: 'null', True: 'true'}


def convert_value(value):
    return CONVERTING_VALUE.get(value, value)


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
    

def stylish(data, indent_size=4, depth=0):
    result = []
    indent = ''
    result.append('{')
    
    for elem in data:
        value = data[elem]["value"]
        key = data[elem]["key"]
        if isinstance(data[elem], dict):   
            indent =  ' ' * (depth * indent_size-2) if depth > 0 else ' ' * (indent_size-2)
            if isinstance(value, dict):
                result.append(f'{indent}  {get_sign(data[elem])}{key}}: {stylish(value, indent_size, depth+1)}')
            elif data[elem]['meta'] == 'children':
                result.append(f'{indent}  {get_sign(data[elem])}{key}: {stylish(value, indent_size, depth +1)}')
            else:
                result.append(f'{indent}  {get_sign(data[elem])}{key}: {convert_value(value)}')
        else:
            indent =  ' ' * (depth * indent_size) if depth > 0 else ' ' * (indent_size)
            result.append(f'{indent}  {get_sign(data[elem])}{data[elem]} {value}')
    indent =  ' ' * (depth * indent_size-2)
    result.append(indent + '}')           
    return '\n'.join(result)


# def stylish(data, indent_size=4, depth=0):
#     result = []
#     sign = ''
#     indent = ''
#     result.append('{\n')
#     for elem in data:
#         if isinstance(elem, dict):
#             if elem['meta'] not in data:
#                 sign = '  '
#             match elem['meta']:
#                 case 'added':
#                     sign = '+ '
#                 case 'deleted':
#                     sign = '- '
#                 case 'unchanged':
#                     sign = '  '
#                 case 'changed-':
#                     sign = '- '
#                 case 'changed+':
#                     sign = '+ '    
#             indent =  ' ' * (depth * indent_size-2) if depth > 0 else ' ' * (indent_size-2)
#             if isinstance(elem['value'], dict):
#                 result.append(f'{indent}  {sign}{elem["key"]}: {stylish(elem["value"], indent_size, depth+1)}')
#             elif elem['meta'] == 'children':
#                 result.append(f'{indent}  {sign}{elem["key"]}: {stylish(elem["value"], indent_size, depth +1)}')
#             else:
#                 result.append(f'{indent}  {sign}{elem["key"]}: {convert_value(elem["value"])}\n')
#         else:
#             indent =  ' ' * (depth * indent_size-2) if depth > 0 else ' ' * (indent_size-2)
#             result.append(f'{indent}    {sign}{elem}: {convert_value(data[elem])}\n')
#     indent =  ' ' * (depth * indent_size-2)
#     result.append(indent + '}\n')           
#     return ''.join(result)

