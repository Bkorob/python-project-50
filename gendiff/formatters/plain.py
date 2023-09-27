from gendiff.formatters.stylish import convert_value


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    return convert_value(value)


def get_path(previous_path, new_part):
    new_path = f'{previous_path}.{new_part}'
    return new_path


def plain(data, key_name=''):
    result = ''
    for elem in data:
        key = elem['key']
        value = elem['value']
        meta = elem['meta']
        if meta == 'children':
            result += plain(value, key_name=elem['key'])
        elif meta == 'changed+' or meta == 'changed-':
            result += (f'Property {get_path(key_name, key)} was updated.'
                       f'From {get_value(value)} to {get_value(value)}')
            # тут пока затык.
            # Видимо надо переделывать логику добавления внутреннего представления.
        elif meta == 'unchanged':
            continue
        elif meta == 'added':
            result += f'Property {get_path(key_name, key)}'
            f'was added with value: {get_value(value)}\n'
        elif meta == 'deleted':
            result += f'Property {get_path(key_name, key)} was removed\n'
    return result
