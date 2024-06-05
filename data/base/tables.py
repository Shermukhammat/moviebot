import sqlite3


def creat_tables(db_path : str):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name, registered, status INTEGER); """)
    cursor.execute(""" CREATE TABLE IF NOT EXISTS amdmins(id INTEGER PRIMARY KEY, name, registered, owner INTEGER); """)
    
    cursor.execute(""" CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY, name, lang, country, gener, year INTEGER, duration, image_url); """)
    cursor.execute(""" CREATE TABLE IF NOT EXISTS movies_resolution(id INTEGER, movie_id INTEGER, resolution INTEGER); """)
    
    con.commit()
    con.close()
    
    
if __name__ == '__main__':
    creat_tables('test.db')