from gendiff import generate

def stylish(data, indent_size=4, depth=1):
    result = []
    indent = ' ' * indent_size * depth
    result.append('{\n')
    for elem in data:
        if isinstance(elem, dict):
            if isinstance(elem['value'], dict):
                result.append(stylish(elem["value"], indent_size, depth +1))
            elif elem['meta'] == 'added':
                result.append(f'{indent}+ {elem["key"]}: {elem["value"]}')
            elif elem['meta'] == 'deleted':
                result.append(f'{indent}- {elem["key"]}: {elem["value"]}')
            elif elem['meta'] == 'unchanged': 
                result.append(f'{indent}  {elem["key"]}: {elem["value"]}')
            elif elem['meta'] == 'changed-':
                result.append(f'{indent}- {elem["key"]}: {elem["value"]}')
            elif elem['meta'] == 'changed+':                
                result.append(f'{indent}+ {elem["key"]}: {elem["value"]}')
            elif elem['meta'] == 'children':
                result.append(f'{indent}  {elem["key"]}: {stylish(elem["value"], indent_size, depth +1)}')
        else: # Пока не понимаю, что нужно сделать, чтобы просто записть "ключ:значение"
            result.append(f'{indent}{data[0]}: {data[1]}')
            
    return '\n'.join(result)
    # return result

               




print(stylish(generate.converting('./tests/fixtures/internal_state.json')))           
