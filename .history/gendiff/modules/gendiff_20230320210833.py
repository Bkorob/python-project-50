import json
j_file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}

j_file2 = {
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}

file1 = json.load(j_file1)
file2 = json.load(j_file2)
print(file1, file2)
def generate_diff(path_to_file1, path_to_file2):
    pass


if __name__ == '__main__':
    generate_diff(path_to_file1, path_to_file2)