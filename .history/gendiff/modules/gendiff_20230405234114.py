import json


def generate_result(file1, file2):
    with open('gendiff/files/json/file1.json') as js1:
        file1 = json.loads(js1)
    with open('gendiff/files/json/file2.json') as js2:
        file2 = json.loads(js2)
    result = dict()
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
    print("{")
    for key in result:
        print(key, ':', result[key])
    print('}')
