from googletrans import Translator
from copy import deepcopy

if __name__ == '__main__':
    from file import UGUtils
    from myparser import PPUtils
else:
    from .file import UGUtils
    from .myparser import PPUtils 


tr = Translator()


class ContextHelper(PPUtils, UGUtils):
    def __init__(self, path, langs : list = ['uz', 'ru', 'en']):
        super().__init__(yaml_file=path)
        self.is_empty = len(self.data) == 0
        self.path = path
        self.langs = langs

    def _load_cache(self):
        self.cache = deepcopy(self.data)
        for key, data in self.cache.items():
            for lang in self.langs:
                self.cache[key][lang] = self.split_pattern(data[lang])
            type_, params = self.get_params(data['pattern'])
            self.cache[key]['type'] = type_
            if type_ == self._args:
                self.cache[key]['params'] = params

    def _put_helper(self, pattern: str, src: str = None, key: str = '') -> None:
        data = {'pattern' : pattern, src : pattern}
        for lang in self.langs:
            if lang != src:
                data[lang] = tr.translate(pattern, src = src, dest = lang).text
        self.data[key] = data
        self.update_yaml(self.data)
        self._load_cache()


class Context(ContextHelper):
    def __init__(self, path : str) -> None:
        super().__init__(path)
        self._load_cache()

    def put_and_update(self, pattern: str, src: str = None, key: str = '') -> None:
        """_summary_
        if it is exist we don't need put just return given object or just validate
        if params not given just translate then add it in yaml file
        if params given we need split it into patterns and params, then translate them
        then load load cache for get updated data, if after put immediately comes get 

        Args:
            pattern (str): _description_
            src (str, optional): _description_. Defaults to None.
            key (str, optional): _description_. Defaults to ''.
        """
        
        

        translated_key = self.data.get(key, None)
        stored_pattern = translated_key['pattern'] if translated_key is not None else None
        is_updateable = True if stored_pattern != pattern else False
        if not self.is_empty:
            if is_updateable:
                self._put_helper(pattern, src, key)
        elif translated_key == None:
            self._put_helper(pattern, src, key)
            
    def get(self, 
            key : str,
            target : str = None,
            **args) -> str:
        
        if self.data.get(key, None) == None:
            return None
        
        if not self.cache[key]['type']:
            if len(args) > 0:
                raise Exception("Not required any params, please remove them")
            return self.data.get(key).get(target)

        params = self.add_params(self.cache[key]['params'], args)
        return self.join_pattern(self.cache[key][target], params)


if __name__ == '__main__':
    con = Context('data.yaml')
    con.put_and_update("salom, {name} [surname] qandaysiz?", src='uz', key = 'hello')
    print(con.get('hello', target = 'en', name="Shermuhammad", surname="Temirov"))