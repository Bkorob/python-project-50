import json
import yaml
import re


def generate_result(file1, file2):
    result = {}
    keys = set(file1.keys()) | set(file2.keys())
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
    # for key1 in file1:
    #     if key1 in file2 and file1[key1] == file2[key1]:
    #         result[f"  {key1}"] = file1[key1]
    #     elif key1 in file2 and file1[key1] != file2[key1]:
    #         result[f"- {key1}"] = file1[key1]
    #         result[f"+ {key1}"] = file2[key1]
    #     else:
    #         result[f"- {key1}"] = file1[key1]

    # for key2 in file2:
    #     if key2 not in file1:
    #         result[f"+ {key2}"] = file2[key2]
    # return result

def converting(source):
    name = source.split('.')[1]
    if name == 'yml':
        source = yaml.safe_load(open(source))
    elif name == 'json':
        source = json.load(open(source))
    return source


def generate_diff(first_file, second_file):
    file1 = converting(first_file)
    file2 = converting(second_file)
    result = dict(sorted(generate_result(file1, file2).items(), key=lambda x: x[0][2]))
    dict_result = json.dumps(result, indent=2)
    diff = re.sub(r'[",]', '', dict_result)
    return diff
