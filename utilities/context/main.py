from googletrans import Translator
import yaml
from file import get_yaml, update_yaml
from myparser import split_pattern

tr = Translator()
# # tr.translate()



class Context:
    def __init__(self, path : str, langs : list = ['uz', 'ru', 'en']) -> None:
        self.data = get_yaml(path)
        print(self.data)
        self.path = path
        self.langs = langs
            

    def get(self, 
            pattern : str, 
            src : str = None, 
            target : str = None,
            key : str = 'hello',
            **args):
        
        if self.data.get(key):
            print('pass')
        
        else:
            print(pattern)
            data = {'pattern' : pattern, src : pattern}
            for lang in self.langs:
                if lang != src:
                    data[lang] = tr.translate(pattern, src = src, dest = lang).text
                    print(tr.translate(pattern, src = src, dest = lang).text)
            
            self.data[key] = data
            update_yaml(self.path, self.data)



con = Context('en.yaml')
print(con.get("salom {name}, qandaysiz?", src='uz', target = 'ru', key = 'hello', name = 'Shermukhammad'))
