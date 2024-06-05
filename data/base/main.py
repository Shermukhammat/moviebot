import sqlite3
if __name__ == '__main__':
    from params import Params
    from users import UsersDb
else:
    from .params import Params 
    from .users import UsersDb


class DataBase(Params, UsersDb):
    def __init__(self, dbFilePath : str, paramsJsonPath : str) -> None:
        self.path = dbFilePath
        Params.__init__(self, paramsJsonPath)
        UsersDb.__init__(self, dbFilePath)
        
        
        
        


if __name__ == '__main__':
    db =  DataBase('test.db', 'test.json')
    db.get_user(1)
    print(db.users_cache)
        