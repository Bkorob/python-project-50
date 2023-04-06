import json

file1 = json.load(open('gendiff/files/json/file1.json', 'r'))
file2 = json.load(open('gendiff/files/json/file2.json', 'r'))

def generate_result(file1, file2):
    # объявляем конечный словарь который будем возращать.
    result = dict()
    # проходим в цикле по ключам первого файла, сравнивая их с ключами во втором.
    for key1 in file1:
        if key1 in file2:
            if file1[key1] == file2[key1]:
                result["  " + key1] = file1[key1]
            else:
                result["- " + key1] = file1[key1]
                result["+ " + key1] = file2[key1]
            result["- " + key1] = file1[key1]
    # проходим по ключам второго файла, выполняя те же действия.
    for key2 in file2:
        if key2 in file1:
            continue
        result["+ " + key2] = file2[key2]
    print("{")
    for key in result:
        print(key,':', result[key])
    print("}")
m = generate_result(file1, file2)
print(generate_result(file1, file2))


# if __name__ == '__main__':
#     generate_diff(filename1, filename2)