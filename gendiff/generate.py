import json
import yaml
import re
from .formatters.stylish import stylish

def make_performance(file1, file2):
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
            if all(map(lambda x: isinstance(x, dict), (file1[key], file2[key]))):
                tree.append({
                    'key': key,
                    'value': make_performance(file1[key], file2[key]),
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
                    'value': file2[key],
                    'meta': 'changed-'
                })
                tree.append({
                    'key': key,
                    'value': file1[key],
                    'meta': 'changed+'
                })                
        else:
            tree.append({
                'key': key,
                'value': file2[key],
                'meta': 'added'
            })
    return tree


def parse_file(path):
    filepath = path
    if filepath.endswith('yaml') or filepath.endswith('yml'):
        with open(path) as p_y:
            source = yaml.safe_load(p_y)
            return source
    elif filepath.endswith('json'):
        with open(path) as p_j:
            source = json.load(p_j)
            return source
    raise ValueError('Unsupported file format')


def generate_diff(first_file, second_file, formatter=stylish):
    file1 = parse_file(first_file)
    file2 = parse_file(second_file)
    intermediate_result = make_performance(file1, file2)
    result = formatter(intermediate_result)
    diff = re.sub(r'[",]', '', result)
    return diff
