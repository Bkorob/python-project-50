import json
#file1 = json.load(open('file1.json', 'r'))
file2 = json.load(open('gendiff/files/json/file2.json', 'r'))

js1 = '''{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": false
  }'''

js2 = '''{
    "timeout": 20,
    "verbose": true,
    "host": "hexlet.io"
  }'''

file1 = json.loads(js1)
# file2 = json.loads(js2)


def generate_result(file1, file2):
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
    result = sorted(result.items(), key=lambda x: x[0][2]))
    print("{")
    for key in result:
        if isinstance(result[key], str):
            print(key, ':', result[key].lower())
        else:
            print(key, ':', result[key])
        
    print("}")
print(generate_result(file1, file2))