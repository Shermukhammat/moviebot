import yaml, os
from ruamel.yaml import YAML

def get_yaml(path : str) -> dict:
    if not os.path.exists(path):
        with open(path, 'w', encoding = 'utf-8') as file:
            file.write('')

    
    with open(path, encoding = 'utf-8') as file:
        data = yaml.safe_load(file)

        if not data:
            return {}
        return data


yaml2 = YAML()
yaml2.indent(mapping=2, sequence=4, offset=2)
yaml2.default_flow_style = False  
yaml2.encoding = 'utf-8'

def update_yaml(path: str, data: dict):
    with open(path, 'w', encoding = 'utf-8') as file:
        data = yaml2.dump(data, file)
    
    if data:
        return data
    return {}

if __name__ == '__main__':
    print(get_yaml('en.yaml'))
    update_yaml('en.yaml', {'menu' : 'balh', 'test' : ['sal', 'pall', 'nima']})