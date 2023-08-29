import yaml
import pprint

file1 = yaml.safe_load(open('../tests/fixtures/file3.yml'))
file2 = yaml.safe_load(open('../tests/fixtures/file4.yml'))


def make_tree_recursive(file1, file2):
    multi_level_diff = {}
    keys = file1.keys() | file2.keys()
    for key in sorted(keys):
        if key not in file2:
            current_key = {}
            current_key['value'] = file1[key]
            current_key['meta'] = 'deleted'
            multi_level_diff[key] = current_key
        elif key in file1 and key in file2:
            if all(map(lambda x: isinstance(x, dict), (file1[key], file2[key]))):
                multi_level_diff[key] = make_tree_recursive(file1[key], file2[key])
            elif file1[key] == file2[key]:
                current_key = {}
                current_key['value'] = file1[key]
                current_key['meta'] = 'unchanged'
                multi_level_diff[key] = current_key
            elif file1[key] != file2[key]:
                current_key = {}
                current_key['value1'] = file1[key]
                current_key['value2'] = file2[key]
                current_key['meta'] = 'changed'
                multi_level_diff[key] = current_key        
        else:
            current_key = {}
            current_key['value'] = file2[key]
            current_key['meta'] = 'added'
            multi_level_diff[key] = current_key
    return multi_level_diff
pprint.pprint(make_tree_recursive(file1, file2))

              
                
                    