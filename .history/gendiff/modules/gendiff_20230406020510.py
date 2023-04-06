import json
first_file = json.load(open('gendiff/files/json/file1.json'))
second_file = json.load(open('gendiff/files/json/file2.json'))


def generate_result(first_file, second_file):
    result = dict()
    for key1 in first_file:
        if key1 in second_file:
            if first_file[key1] == second_file[key1]:
                result["  " + key1] = first_file[key1]
            else:
                result["- " + key1] = first_file[key1]
                result["+ " + key1] = second_file[key1]
        else:
            result["- " + key1] = first_file[key1]
    for key2 in second_file:
        if key2 in first_file:
            continue
        else:
            result["+ " + key2] = second_file[key2]
    result = dict(sorted(result.items(), key=lambda x: x[0][2]))
    print("{")
    for key in result:
        if isinstance(result[key], bool):
            print(key, ':', str(result[key]).lower())
        else:
            print(key, ':', result[key])
   
    print("}")


if __name__ == '__main__':
    generate_result(first_file, second_file)