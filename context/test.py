from pickle import GET
from googletrans import Translator
import yaml


# tr = Translator()
# # tr.translate()

class Context:
    def __init__(self, path : str) -> None:
        with open(path, 'r') as file:
            self.data = yaml.safe_load(file)
            file.close()
            

    def get(self, 
            pattern : str, 
            src : str = None, 
            target : str = None,
            key : str = 'hello',
            **args):
        pass



con = Context('en.yaml')
print(con.get("salom {name}, qandaysiz?", src='uz', target = 'ru', key = 'hello', name = 'Shermukhammad'))
