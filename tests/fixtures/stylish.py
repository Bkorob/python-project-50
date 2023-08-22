def stringify(value, replacer=' ', spaces_count=1, _level=1):
    if not isinstance(value, dict):
        return str(value)
    else:
        indent = replacer * spaces_count * _level
        result = '{\n'
        for k, v in value.items():
            result += f'{indent}{k}: '
            result += f'{stringify(v, replacer, spaces_count, _level+1)}\n'
        result += f'{replacer * spaces_count * (_level - 1)}}}'
        return result
    
data = {"hello": "world", "is": True, "nested": {"count": 5}}    
print(stringify(data, '|-', 2))