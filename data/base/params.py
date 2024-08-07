import json
import os


class Params:
    def __init__(self, file : str) -> None:
        self.path = file
        self.data = load_params(file)
        
        self.PASWORD = self.data.get('pasword')
        self.OWNER_ID = self.data.get('ownerId')
        self.TELEGRAPH_TOKEN = self.data.get('telegraph_token')
        self.DATA_CHANEL_ID = self.data.get('data_chanel_id')
        
    
    def update(self):
        file = open(self.path, 'w')
        file.write(json.dumps(self.data, indent = 4))
        file.close()
        
    def update_pasword(self, pasword : str):
        self.data['pasword'] = pasword
        self.PASWORD = pasword
        self.update()
        
    def update_owner_id(self, id : int):
        self.data['ownerId'] = id
        self.OWNER_ID = id
        self.update()
        
        
        
def load_params(path_json : str) -> dict:
    file = open(path_json, 'r')
    data = json.loads(file.read())
    file.close()
    
    return data


if __name__ == '__main__':
    #{"pasword": "354abc", "ownerId": 1234}
    pa = Params('test.json')
    # pa.update_pasword('354abc')
    # print(pa.PASWORD)