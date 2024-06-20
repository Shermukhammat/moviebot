from aiogram.dispatcher.filters.state import State, StatesGroup



class AdminStates(StatesGroup):
    get_movie_title = State()
    get_movie_thumb = State()
    get_movie_caption = State()
    get_movie_year = State()
    get_movie_gener = State()
    
    

class UserStates(StatesGroup):
    pass