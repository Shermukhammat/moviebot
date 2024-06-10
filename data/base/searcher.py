from fuzzywuzzy import process



def search(query : str, choices : list):
    matches = process.extract()