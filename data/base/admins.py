import sqlite3
from .clock import now

class AdminType:
    owner = 1
    usual = 2
    
        

class AdminsDb:
    def __init__(self, db_path : str) -> None:
        self.path = db_path 
        self.admins_cache = {}
    
    def is_admin(self, id : int) -> bool:
        if self.admins_cache.get(id):
            return True
        
        admin_data = get_admin_from_db(self.path, id)
        if admin_data:
            self.admins_cache[id] = admin_data
            return True
        return False

    def register_admin(self, id : int, name : str, admin_type : int = AdminType.usual):
        time = now()
        
        try:
            con = sqlite3.connect(self.path)
            cursor = con.cursor()
            cursor.execute("INSERT INTO admins (id, registered, type, name) VALUES(?, ?, ?, ?);", (id, time, admin_type, name))

            con.commit()
            con.close()

            self.admins_cache[id] = {'registered' : time, 'type' : admin_type, 'name' : name}
            return True
        
        except Exception as e:
            print(e)
            return False
        
    
    def get_admin(self, id) -> dict:
        data = self.admins_cache.get(id)
        if data:
            return data
        data = get_admin_from_db(self.path, id)
        if data:
            self.admins_cache[id] = data
            return data 
        
    
    def remove_admin(self, id):
        if self.admins_cache.get(id):
            del self.admins_cache[id]
            
        con = sqlite3.connect(self.path)
        cursor = con.cursor()
        
        cursor.execute(f"DELETE FROM admins WHERE id = {id};")
        
        con.commit()
        con.close()


    
def get_admin_from_db(db_path : str, id : int) -> dict:
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    
    for row in cursor.execute(f"SELECT name, registered, type FROM admins WHERE id = {id};"):
        con.close()
        return {'registered' : row[1], 'type' : row[2], 'name' : row[0]}
    
    con.close()
    

if __name__ == '__main__':
    db = AdminsDb('test.db')
    # db.register_admin(2, 'sher2')
    # db.remove_admin(2)
    # db.get_admin(2)
    
    # db.update_user_status(1, Status.blocked)
    print(db.admins_cache)
    