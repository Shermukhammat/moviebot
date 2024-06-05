import sqlite3
if __name__ == '__main__':
    from params import Params
    from data.base.clock import now
else:
    from .params import Params 
    from .base.clock import now


class Status:
    def __init__(self) -> None:
        self.active = 1
        self.blocked = 2

class Test:
    def __init__(self, blah : int) -> None:
        self.blah = blah

class DataBase(Params):
    def __init__(self, db_path : str, params_path : str) -> None:
        self.status = Status()
        Params.__init__(params_path)
        
        
        self.path = db_path 
        creat_tables(db_path)

        self.users_cache = {}
        self.admins_cache = {}
    
    def is_user(self, id : int) -> bool:
        if self.users_cache.get(id):
            return True
        
        user_data = get_user_from_db(self.path, id)
        if user_data:
            self.users_cache[id] = user_data
            return True
        return False

    def register_user(self, id : int, name : str):
        time = now()
        status = self.status.active
        
        try:
            con = sqlite3.connect(self.path)
            cursor = con.cursor()
            cursor.execute("INSERT INTO users (id, registered, status, name) VALUES(?, ?, ?, ?);", (id, time, status, name))

            con.commit()
            con.close()

            self.users_cache[id] = {'registered' : time, 'status' : status, 'name' : name}
            return True
        
        except Exception as e:
            print(e)
            return False
        
    
    def get_user(self, id):
        data = self.users_cache.get(id)
        if data:
            return data
        data = get_user_from_db(self.path, id)
        self.users_cache[id] = data
        return data 
    
    def clean_caches(self):
        self.users_cache.clear()
        self.admins_cache.clear()
        
    
    def remove_user(self, id):
        if self.users_cache.get(id):
            del self.users_cache[id]
            
        con = sqlite3.connect(self.path)
        cursor = con.cursor()
        
        cursor.execute(f"DELETE FROM users WHERE id = {id};")
        
        con.commit()
        con.close()

    def update_user_status(self, id : int, status : int) -> bool:
        if self.users_cache.get(id):
            self.users_cache[id]['status'] = status 
        
        return updat_user_db_status(self.path, status)
       



def updat_user_db_status(path : str, status : int) -> bool:
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        
        cursor.execute(f"UPDATE users SET status = {status} WHERE id = {id};")
        
        con.commit()
        con.close()
        return True
    
    except:
        return False
    
def get_user_from_db(db_path : str, id : int) -> dict:
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    
    for row in cursor.execute(f"SELECT registered, status, name FROM users WHERE id = {id};"):
        con.close()
        return {'registered' : row[0], 'status' : row[1], 'name' : row[2]}
    
    con.close()
    return {}

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
    db = DataBase('test.db', 'test.json')
    db.register_user(123454, 'sher')
    
    print(db.users_cache)
    print(db.get_user(123454))
    print(db.get_user(123454))
    print(db.users_cache)
    