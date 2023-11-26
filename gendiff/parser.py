import json
import yaml


def get_file(path):
    format = path.split('.')[-1]
    with open(path) as f:
        source = f.read()
        return parse_file(source, format)
   
    
def parse_file(source, format):
    if format in ['yaml', 'yml']:
        return yaml.safe_load(source)
    elif format == 'json':
        return json.loads(source)
    raise ValueError('Unsupported file format')
