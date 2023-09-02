import json
import yaml
import re


def generate_result(file1, file2):
    result = {}
    keys = file1.keys() | file2.keys()
    for key in sorted(keys):
        if key not in file2:
            result[f'- {key}'] = file1[key]
        elif key in file1 and key in file2:
            if file2[key] != file1[key]:
                result[f"- {key}"] = file1[key]
                result[f"+ {key}"] = file2[key]
            elif file1[key] == file2[key]:
                result[f'  {key}'] = file1[key]
        else:
            result[f'+ {key}'] = file2[key]
    return result


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
    return parse_file
    


def generate_diff(first_file, second_file):
    file1 = parse_file(first_file)
    file2 = parse_file(second_file)
    result = dict(sorted(generate_result(file1, file2).items(), key=lambda x: x[0][2]))
    dict_result = json.dumps(result, indent=2)
    diff = re.sub(r'[",]', '', dict_result)
    return diff
