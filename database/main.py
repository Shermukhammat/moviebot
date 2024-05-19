import sqlite3
if __name__ == '__main__':
    from params import Params
else:
    from .params import Params



class DataBase(Params):
    def __init__(self, db_path : str, params_path : str) -> None:
        super().__init__(params_path)
        
        self.path = db_path 
        creat_tables(db_path)
        
        
    
    


def creat_tables(db_path : str):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()  
    
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, registred); """)
    
    con.commit()
    con.close()


if __name__ == '__main__':
    db = DataBase('test.db', 'test.json')
    print(db.PASWORD)