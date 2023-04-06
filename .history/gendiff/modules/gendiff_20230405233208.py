import json


def generate_result(file1, file2):
    # объявляем конечный словарь который будем возращать.
    result = dict()
    # проходим в цикле по ключам первого файла,
    for key1 in file1:
        if key1 in file2:
            if file1[key1] == file2[key1]:
                result["  " + key1] = file1[key1]
            else:
                result["- " + key1] = file1[key1]
                result["+ " + key1] = file2[key1]
        else:
            result["- " + key1] = file1[key1]
    for key2 in file2:
        if key2 in file1:
            continue
        else:
            result["+ " + key2] = file2[key2]
    return json.dumps(result, indent=2)
