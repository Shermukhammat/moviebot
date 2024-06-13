import sqlite3
from fuzzywuzzy import process


class Movie:
    def __init__(self, id : int, 
                 title : str, 
                 image_url : str, 
                 qualities : dict,
                 
                 duration : str = None, 
                 lang : str = None, 
                 year : int = None, 
                 genere : str = None, 
                 country : str = None) -> None:
        
        self.id = id
        self.title = title
        self.image_url = image_url
        self.duration = duration
        self.lang = lang
        self.year = year
        self.genere = genere
        self.country = country
        self.qualities = qualities
        


class MoviesDb:
    def __init__(self, db_path : str) -> None:
        self.path = db_path
        self.movies_title_cache = get_movies_title_from_db(db_path)
        self.movies_cache = {}
    
    def get_movie(self, id : int) -> Movie:
        if self.movies_cache.get(id):
            return self.movies_cache[id]
        movie = get_movie_from_db(self.path, id)
        if movie:
            self.movies_cache[id] = movie
            self.movies_title_cache[movie.title] = movie.id
            return movie 
        
    # def get_movies(self) -> li:
        
        
    
    def add_movie(self, movie : Movie):        
        if add_movie_to_db(self.path, movie):
            self.movies_cache[movie.id] = movie
            self.movies_title_cache[movie.title] = movie.id
            return True 
        
    
    def search_movie(self, query : str, limit : int = 50) -> list:
        matches = process.extract(query, self.movies_title_cache.keys(), limit = limit)
        return [match[0] for match in matches]
        
    



def get_movie_from_db(path : str, id : int) -> Movie:
    con = sqlite3.connect(path)
    cursor = con.cursor()
    
    cursor.execute(""" SELECT id, title, image_url, lang, country, gener, year, duration FROM movies WHERE id = ?; """, (id,))
    row = cursor.fetchone()
    if row:
        qualities = {}
        for row2 in cursor.execute(f""" SELECT resolution, data_id FROM movies_quality WHERE movie_id = ?; """, (id,)):
            qualities[row2[0]] = row2[1]
        
        return Movie(id, row[1], row[2], qualities, 
                     lang = row[3], 
                     country = row[4], 
                     genere = row[5], 
                     year = row[6], 
                     duration = row[7])
    
    con.close()

def get_movies_title_from_db(path : str) -> dict:
    con = sqlite3.connect(path)
    cursor = con.cursor()
    data = {}
    
    for row in cursor.execute("SELECT title, id FROM movies;"):
        data[row[0]] = row[1]
    
    con.close()
    return data
    
def get_movies_from_db(path : str) -> dict:
    con = sqlite3.connect(path)
    cursor = con.cursor()
    data = {}
    
    rows = cursor.execute(""" SELECT id, title, image_url, lang, country, gener, year, duration FROM movies; """)       
    for row in rows.fetchall():
        qualities = get_resolutions(cursor, row[0])
        movie = Movie(row[0], row[1], row[2], qualities, 
                     lang = row[3], 
                     country = row[4], 
                     genere = row[5], 
                     year = row[6], 
                     duration = row[7])
        
        data[movie.id] = movie
    
    con.close()
    return data
    
def get_resolutions(cursor : sqlite3.Cursor, id : int) -> dict:
    qualities = {}
    for row in cursor.execute(f""" SELECT resolution, data_id FROM movies_quality WHERE movie_id = ? ; """, (id,)):
        qualities[row[0]] = row[1]
    
    return qualities

def add_movie_to_db(path : str, movie : Movie) -> bool:
    con = sqlite3.connect(path)
    cursor = con.cursor()
    
    cursor.execute(f""" INSERT INTO movies (id, title, lang, country, gener, year, duration, image_url) VALUES(?, ?, ?, ?, ?, ?, ?, ?); """, 
                   (movie.id, movie.title, movie.lang, movie.country, movie.genere, movie.year, movie.duration, movie.image_url))
    
    for quality, data_id in movie.qualities.items():
        cursor.execute(f""" INSERT INTO movies_quality (movie_id, resolution, data_id) VALUES(?, ?, ?); """,
                       (movie.id, quality, data_id))
    
    con.commit()
    con.close()
    
    return True


if __name__ == '__main__':
    movie = Movie(5, 'qasoskorlar 5', 'www.ex.io', {360 : 1, 480 : 2, 720 : 3})
    db = MoviesDb('test.db')
    
    # print(db.add_movie(movie))
    # db.get_movie(1)
    # for title in ['tor', 'Oskar', 'Smurflar', 'silicon valley', 'smurflar 3', 'tezlik', 'manyak', "O'rgimchak odam"]:
    #     db.movies_title_cache[title] = 1
        
    # # for n in range(10_000):
    # #     db.movies_title_cache[f'name{n}'] = n
    
    # n = input('start')   
    # print(db.search_movie("tez", limit=50))
    # def show(movie : Movie):
    #     print(movie.id, movie.title, movie.image_url, movie.country)
        
    # for movie in db.movies_cache.values():
    #     show(movie)
    
    # print(get_movies_from_db('test.db'))
    print(get_movies_title_from_db('test.db'))