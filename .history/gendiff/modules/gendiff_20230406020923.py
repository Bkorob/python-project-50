import json


first_file = json.load(open('gendiff/files/json/file1.json'))
second_file = json.load(open('gendiff/files/json/file2.json'))


def generate_result(first_file, second_file):
    result = dict()
    for first_key in first_file:
        if first_key in second_file and first_file[first_key] == second_file[first_key]:
                result["  " + first_key] = first_file[first_key]
            else:
                result["- " + first_key] = first_file[first_key]
                result["+ " + first_key] = second_file[first_key]
        else:
            result["- " + first_key] = first_file[first_key]
    for second_key in second_file:
        if second_key in first_file:
            continue
        else:
            result["+ " + second_key] = second_file[second_key]
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