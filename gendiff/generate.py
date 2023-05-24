import json
import re


def generate_result(file1, file2):
    result = {}

    for key1 in file1:
        if key1 in file2 and file1[key1] == file2[key1]:
            result[f"  {key1}"] = file1[key1]
        elif key1 in file2 and file1[key1] != file2[key1]:
            result[f"- {key1}"] = file1[key1]
            result[f"+ {key1}"] = file2[key1]
        else:
            result[f"- {key1}"] = file1[key1]

    for key2 in file2:
        if key2 not in file1:
            result[f"+ {key2}"] = file2[key2]

    result = dict(sorted(result.items(), key=lambda x: x[0][2]))
    return result


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    dict_result = json.dumps(generate_result(file1, file2), indent=2)
    diff = re.sub(r'"', '', dict_result)
    return diff
