from gendiff.formatters.stylish import CONVERTING_VALUE as CV


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return f'{CV.get(value)}'


def get_path(previous_path, new_level):
    return f'{previous_path}.{new_level}'[1:]


def get_plain(data, key_name=''):
    result = ''
    for elem in data:
        key = elem['key']
        value = elem['value']
        meta = elem['meta']
        if meta == 'children':
            result += get_plain(value, key_name + f".{key}")
        elif meta == 'changed':
            result += (f"Property '{get_path(key_name, key)}' was updated."
                       f" From {get_value(value[0])} to {get_value(value[1])}\n")
        elif meta == 'added':
            result += (f"Property '{get_path(key_name, key)}'"
                       f" was added with value: {get_value(value)}\n")
        elif meta == 'deleted':
            result += f"Property '{get_path(key_name, key)}' was removed\n"
    return result


def plain(data):
    val = get_plain(data)
    return val.rstrip()
