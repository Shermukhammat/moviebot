import sqlite3
from .clock import now

class Status:
    active = 1
    blocked = 2
        

class UsersDb:
    def __init__(self, db_path : str) -> None:
        self.path = db_path 
        self.users_cache = {}
    
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
        status = Status.active
        
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
        
    
    def get_user(self, id) -> dict:
        data = self.users_cache.get(id)
        if data:
            return data
        data = get_user_from_db(self.path, id)
        if data:
            self.users_cache[id] = data
            return data 
        
    
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
        
        return updat_user_db_status(self.path, status, id)
       



def updat_user_db_status(path : str, status : int, id : int) -> bool:
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
    

if __name__ == '__main__':
    db = UsersDb('test.db')
    # db.register_user(2, 'sher2')
    db.get_user(1)
    
    # db.update_user_status(1, Status.blocked)
    print(db.users_cache)
    