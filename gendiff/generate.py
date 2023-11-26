from .get_format import get_format
from .parser import get_file


def make_inner_view(file1, file2):
    tree = []
    keys = file1.keys() | file2.keys()
    for key in sorted(keys):
        if key not in file2:
            tree.append({
                'key': key,
                'value': file1[key],
                'meta': 'deleted'
            })
        elif key in file1 and key in file2:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                tree.append({
                    'key': key,
                    'value': make_inner_view(file1[key], file2[key]),
                    'meta': 'children'
                })
            elif file1[key] == file2[key]:
                tree.append({
                    'key': key,
                    'value': file1[key],
                    'meta': 'unchanged'
                })
            elif file1[key] != file2[key]:
                tree.append({
                    'key': key,
                    'value': (file1[key], file2[key]),
                    'meta': 'changed'
                })
        else:
            tree.append({
                'key': key,
                'value': file2[key],
                'meta': 'added'
            })
    return tree


def generate_diff(first_file, second_file, format_name='stylish'):
    file1 = get_file(first_file)
    file2 = get_file(second_file)
    intermediate_result = make_inner_view(file1, file2)
    formatter = get_format(format_name)
    result = formatter(intermediate_result)
    return result
