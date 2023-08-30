import yaml


def make_tree_recursive(file1, file2):
    tree = []
    keys = file1.keys() | file2.keys()
    for key in sorted(keys):
        if key not in file2:
            tree.append({
                'key': key,
                'value': file1[key],
                'meta': 'deleted'
            })
        elif key in file1 and key in file2:
            if all(map(lambda x: isinstance(x, dict), (file1[key], file2[key]))):
                tree.append({
                    'key': key,
                    'value': make_tree_recursive(file1[key], file2[key]),
                    'meta': 'children'
                })
            elif file1[key] == file2[key]:
                tree.append({
                    'key': key,
                    'value': file1[key],
                    'meta': 'unchanged'
                })
            elif file1[key] != file2[key]:
                tree.append({
                    'key': key,
                    'value1': file1[key],
                    'value2': file2[key],
                    'meta': 'changed'
                })
                
        else:
            tree.append({
                'key': key,
                'value': file2[key],
                'meta': 'added'
            })
    return tree
                    