from .get_format import get_format
from .parser import get_path


def make_inner_view(data1, data2):
    tree = []
    keys = data1.keys() | data2.keys()
    for key in sorted(keys):
        if key not in data2:
            tree.append({
                'key': key,
                'value': data1[key],
                'meta': 'removed'
            })
        elif key in data1 and key in data2:
            if all(map(lambda x: isinstance(x, dict), (data2[key], data1[key]))):
                tree.append({
                    'key': key,
                    'value': make_inner_view(data1[key], data2[key]),
                    'meta': 'nested'
                })
            elif data1[key] == data2[key]:
                tree.append({
                    'key': key,
                    'value': data1[key],
                    'meta': 'unchanged'
                })
            elif data1[key] != data2[key]:
                tree.append({
                    'key': key,
                    'value': (data1[key], data2[key]),
                    'meta': 'changed'
                })
        else:
            tree.append({
                'key': key,
                'value': data2[key],
                'meta': 'added'
            })
    return tree


def generate_diff(first_data, second_data, format_name='stylish'):
    data1 = get_path(first_data)
    data2 = get_path(second_data)
    intermediate_result = make_inner_view(data1, data2)
    formatter = get_format(format_name)
    result = formatter(intermediate_result)
    return result
