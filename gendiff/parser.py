import json
import yaml


def get_path(path):
    format = path.split('.')[-1]
    with open(path) as f:
        source = f.read()
        return parse_data(source, format)


def parse_data(source, format):
    if format in ['yaml', 'yml']:
        return yaml.safe_load(source)
    elif format == 'json':
        return json.loads(source)
    raise ValueError('Unsupported file format')
