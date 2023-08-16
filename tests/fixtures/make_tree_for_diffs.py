import yaml
file1 = yaml.safe_load(open('./file3.yml'))
file2 = yaml.safe_load(open('./file4.yml'))
for key in file1.keys():
    if file1[key] == file2[key]:
        value_items = set(file1.items(), file2.items())
        for value in value_items:
            if not isinstance(value, dict):
                print(value)