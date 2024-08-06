import re 




class ContextType:
    """_summary_\n
    class for Context type. Indecates pattern have args or not.
    """
    noargs = 0
    args = 1


def get_params(text : str) -> tuple[int, list[str]]:
    """_summary_

    Args:
        text (str): _description_

    Returns:
        tuple[int, list[str]]: _description_
    """
    matches = re.findall(r'\{([^}]*)\}', text)
    
    if matches:
        return ContextType.args, matches
    return ContextType.noargs, matches



def split_pattern(text : str) -> list[str]:
    return re.split(r'\{[^}]*\}', text)

def join_pattern(patter : list[str], params : list[str]) -> str:
    resolt = ''
    for index in range(len(patter)):
        resolt += patter[index]
        if index < len(params):
            resolt += params[index]
    

    return resolt
 

def add_params(params : list[str], args : dict[str, str]) -> list[str]:
    resolt = []
    for param in params:
        if args.get(param):
            resolt.append(args[param])
        else:
            resolt.append('null')

    return resolt

if __name__ == '__main__':
    # print(get_params("salom dfd   fdfdd "))
    split_pattern('salom {name} cddfd {age} dfd')
    join_pattern(['salom ', ' cddfd ', ' dfd'], ['Shermukhammad', '18'])