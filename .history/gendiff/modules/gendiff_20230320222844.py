import json
# file1 = json.load(open('file1.json', 'r'))
# file2 = json.load(open('gendiff/files/json/file2.json', 'r'))

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
file2 = json.loads(js2)

# def generate_diff(path_to_file1, path_to_file2):
file_lst1 = list(file1.items()) 
file_lst2 = list(file2.items())
res = [] 
for i, v in enumerate(file_lst1):
    if v in file_lst2:
        res.append(v)
        continue
    if file_lst1[i][0] in file2.keys():
        res.append(str(file_lst1[i])
        res.append(file2[[i]])

print(res)

# if __name__ == '__main__':
#     generate_diff(path_to_file1, path_to_file2)