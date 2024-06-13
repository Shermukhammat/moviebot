import sqlite3
if __name__ == '__main__':
    from params import Params
    from users import UsersDb
    from admins import AdminsDb
    from movies import MoviesDb, Movie
    from tables import creat_tables
else:
    from .params import Params
    from .users import UsersDb
    from .admins import AdminsDb
    from .movies import MoviesDb, Movie
    from .tables import creat_tables


class DataBase(Params, UsersDb, AdminsDb, MoviesDb):
    def __init__(self, dbFilePath : str, paramsJsonPath : str) -> None:
        creat_tables(dbFilePath)
        
        Params.__init__(self, paramsJsonPath)
        UsersDb.__init__(self, dbFilePath)
        AdminsDb.__init__(self, dbFilePath)
        MoviesDb.__init__(self, dbFilePath)
        
    
        
        
        
        
        


if __name__ == '__main__':
    db =  DataBase('test.db', 'test.json')
    db.get_user(1)
    print(db.users_cache)
        