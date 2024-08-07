import re 




class ContextType:
    """_summary_\n
    class for Context type. Indecates pattern have args or not.
    """
    _noargs = 0
    _args = 1

class PPUtils(ContextType):
    def get_params(self, text : str) -> tuple[int, list[str]]:
        """_summary_

        Args:
            text (str): _description_

        Returns:
            tuple[int, list[str]]: _description_
        """
        # matches= re.findall(r'\{([^}]*)\}', text)
        matches = re.findall(r'\((.*?)\)|\[(.*?)\]|\{(.*?)\}', text)
        matches = [match for group in matches for match in group if match]
        
        
        if matches:
            return ContextType._args, matches
        return ContextType._noargs, matches


    def split_pattern(self, text : str) -> list[str]:
        return re.split(r'\{[^}]*\}|\[[^\]]*\]|\([^)]*\)', text)

    def join_pattern(self, patter : list[str], params : list[str]) -> str:
        resolt = ''
        for index in range(len(patter)):
            resolt += patter[index]
            if index < len(params):
                resolt += params[index]
        return resolt
    

    def add_params(self, params : list[str], args : dict[str, str]) -> list[str]:
        resolt = []
        for param in params:
            if args.get(param, None) == None:
                raise Exception("Given invalid param!")
            resolt.append(args[param])
        return resolt

# if __name__ == '__main__':
    # pp = PPUtils()
    # print(pp.get_params("Text with (parentheses), [square brackets], and {curly braces}."))
    # print(pp.split_pattern('salom bolam , {name}, {surname} cddfd tasted {age} dfd'))
    # print(pp.join_pattern(split_pattern('salom bolam , {name}, [surname] cddfd tasted (age) dfd'), ['Shermukhammad', "temirov", '18']))