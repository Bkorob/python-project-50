import json

first_file = json.load(open('gendiff/files/json/file1.json'))
second_file = json.load(open('gendiff/files/json/file2.json'))

def generate_result(first_file, second_file): 
    result = {}
    for key1 in first_file:
        if key1 in second_file and first_file[key1] == second_file[key1]:
            result["  " + key1] = first_file[key1]
        elif key1 in second_file and first_file[key1] != second_file[key1]:
            result["- " + key1] = first_file[key1]
            result["+ " + key1] = second_file[key1]
        else:
            result["- " + key1] = first_file[key1]
    for key2 in second_file:
        if key2 not in first_file:
            result["+ " + key2] = second_file[key2]
    result = dict(sorted(result.items(), key=lambda x: x[0][2]))
    return result


def get_print(generate_result):
        print("{")
        for key, val in generate_result(first_file, second_file).items():
            if isinstance(val, bool):
                print(key, ':', str(val).lower())
            else:
                print(key, ':', val)
        print("}")


def main():
    
    generate_result(first_file, second_file)
    get_print(generate_result)
    

if __name__ == '__main__':
    main()
