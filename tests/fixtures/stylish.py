import json


def stylish(data, indent_size=4, depth=1):
    result = []
    indent = ' ' * indent_size * depth
    result.append('{\n')
    for elem in data:
        if isinstance(elem, dict):
            if elem['meta'] == 'added':
                result.append(f'{indent}+ {elem["key"]}: {elem["value"]}')
            elif elem['meta'] == 'deleted':
                result.append(f'{indent}- {elem["key"]}: {elem["value"]}')
            elif elem['meta'] == 'unchanged':
                result.append(f'{indent}  {elem["key"]}: {elem["value"]}')
            elif elem['meta'] == 'changed':
                result.append(f'{indent}- {elem["key"]}: {elem["value1"]}')
                result.append(f'{indent}+ {elem["key"]}: {elem["value2"]}')
            elif elem['meta'] == 'children':
                result.append(f'{indent}  {elem["key"]}: {stylish(elem["value"], indent_size, depth +1)}')

        else:
            result.append('\n' + indent + elem)
            
    return '\n'.join(result)
    # return result


data = [{'key': 'common',
  'meta': 'children',
  'value': [{'key': 'follow', 'meta': 'added', 'value': False},
            {'key': 'setting1', 'meta': 'unchanged', 'value': 'Value 1'},
            {'key': 'setting2', 'meta': 'deleted', 'value': 200},
            {'key': 'setting3',
             'meta': 'changed',
             'value1': True,
             'value2': None},
            {'key': 'setting4', 'meta': 'added', 'value': 'blah blah'},
            {'key': 'setting5', 'meta': 'added', 'value': {'key5': 'value5'}},
            {'key': 'setting6',
             'meta': 'children',
             'value': [{'key': 'doge',
                        'meta': 'children',
                        'value': [{'key': 'wow',
                                   'meta': 'changed',
                                   'value1': '',
                                   'value2': 'so much'}]},
                       {'key': 'key', 'meta': 'unchanged', 'value': 'value'},
                       {'key': 'ops', 'meta': 'added', 'value': 'vops'}]}]},
 {'key': 'group1',
  'meta': 'children',
  'value': [{'key': 'baz',
             'meta': 'changed',
             'value1': 'bas',
             'value2': 'bars'},
            {'key': 'foo', 'meta': 'unchanged', 'value': 'bar'},
            {'key': 'nest',
             'meta': 'changed',
             'value1': {'key': 'value'},
             'value2': 'str'}]},
 {'key': 'group2',
  'meta': 'deleted',
  'value': {'abc': 12345, 'deep': {'id': 45}}},
 {'key': 'group3',
  'meta': 'added',
  'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

print(stylish(data))           
