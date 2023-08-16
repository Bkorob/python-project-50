import yaml
import pprint

file1 = yaml.safe_load(open('tests/fixtures/file3.yml'))
file2 = yaml.safe_load(open('tests/fixtures/file4.yml'))


def make_tree_recursive(file1, file2):
    multi_level_diff = {}
    keys = file1.keys() | file2.keys()
    for key in sorted(keys):
        if key in file1 and key in file2: 
            value_items = file1[key], file2[key]
            if all(map(lambda x: isinstance(x, dict), value_items)):
                multi_level_diff[key] = make_tree_recursive(file1[key], file2[key])
        if key not in file2:
            multi_level_diff[key] = ['deleted', file1[key]]
        elif key not in file1:
            multi_level_diff[key] = ['added', file2[key]]
        elif file1[key] == file2[key]:
            multi_level_diff[key] = ['unchanged', file1[key]]
        elif file1[key] != file2[key]:
            multi_level_diff[key] = ['changed', file1[key], file2[key]]
    return multi_level_diff
pprint.pprint(make_tree_recursive(file1, file2))
                
                
                    