from googletrans import Translator
import yaml
from file import get_yaml, update_yaml
from myparser import split_pattern, get_params, join_pattern, ContextType, add_params

tr = Translator()
# # tr.translate()



class Context:
    def __init__(self, path : str, langs : list = ['uz', 'ru', 'en']) -> None:
        self.data = get_yaml(path)
        self.path = path
        self.langs = langs

        self.load_cache()
            

    def get(self, 
            pattern : str, 
            src : str = None, 
            target : str = None,
            key : str = 'hello',
            **args):
        
        if self.data.get(key):
            if self.cache[key]['checked']:
                params = add_params(self.cache[key]['params'], args)
                return join_pattern(self.cache[key][target], params)

            elif self.data[key]['pattern'] == pattern:
                self.cache[key]['checked'] = True
                params = add_params(self.cache[key]['params'], args)
                return join_pattern(self.cache[key][target], params)

            else:
                pass
                #update pattern 
        
        else:
            data = {'pattern' : pattern, src : pattern}
            for lang in self.langs:
                if lang != src:
                    data[lang] = tr.translate(pattern, src = src, dest = lang).text
                    print(tr.translate(pattern, src = src, dest = lang).text)
            
            self.data[key] = data
            update_yaml(self.path, self.data)

    def load_cache(self):
        self.cache = self.data

        for key, data in self.cache.items():
            for lang in self.langs:
                self.cache[key][lang] = split_pattern(data[lang])
            type_, params = get_params(data['pattern'])
            self.cache[key]['type'] = type_
            if type_ == ContextType.args:
                self.cache[key]['params'] = params
            self.cache[key]['checked'] = False

con = Context('en.yaml')
print(con.get("salom {name}, qandaysiz?", 
              src='uz', target = 'ru', key = 'hello', 
              name = 'Shermukhammad'))
# print(con.cache)