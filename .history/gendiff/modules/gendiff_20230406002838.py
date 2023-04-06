import json


def generate_result(file1, file2):
    file1 = json.load(open('gendiff/files/json/file2.json'))
    file2 = json.load(open('gendiff/files/json/file2.json'))
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
    result = dict(sorted(result.items(), key=lambda x: x[0][2]))
    print("{")
    for key in result:
        if isinstance(result[key], bool):
            print(key, ':', str(result[key]).lower())
        else:
            print(key, ':', result[key])
        
    print("}")
