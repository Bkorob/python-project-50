import json


def generate_result():
    first_file = json.load(open('gendiff/files/json/file1.json'))
    second_file = json.load(open('gendiff/files/json/file2.json'))
    result = {}
    for first_key in first_file:
        if first_key in second_file and first_file[first_key] == second_file[first_key]:
            result["  " + first_key] = first_file[first_key]
        elif first_key in second_file and first_file[first_key] != second_file[first_key]:
            result["- " + first_key] = first_file[first_key]
            result["+ " + first_key] = second_file[first_key]
        else:
            result["- " + first_key] = first_file[first_key]
    for second_key in second_file:
        if second_key not in first_file:
            result["+ " + second_key] = second_file[second_key]
    result = dict(sorted(result.items(), key=lambda x: x[0][2]))
    return result


def get_print(generate_result):
        print("{")
        for key, val in generate_result().items():
            if isinstance(val, bool):
                print(key, ':', str(val).lower())
            else:
                print(key, ':', val)
        print("}")


if __name__ == '__main__':
    generate_result()
    get_print(generate_result)
