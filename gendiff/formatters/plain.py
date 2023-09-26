from gendiff.formatters.stylish import convert_value


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    return convert_value(value)

def plain(data, key_name=''):
    result = ''
    for elem in data:
        key_name += f'.{elem["key"]}'
        value = elem['value']
        meta = elem['meta']
        # if isinstance(value, dict):
        #     result +=  
        if meta == 'children':
            result += plain(value) 
        elif meta == 'added':
            result += f'Property {key_name} was added with value: {get_value(value)}\n'
        elif meta == 'deleted':
            result += f'Property {key_name} was removed\n'
    return result  