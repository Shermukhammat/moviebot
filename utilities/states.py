from aiogram.dispatcher.filters.state import State, StatesGroup



class AdminStates(StatesGroup):
    get_movie_title = State()
    get_movie_thumb = State()
    get_movie_caption = State()
    edit_movie_menu = State()
    get_movie_video = State()
    chose_resolution = State()
    get_movie_year = State()
    get_movie_gener = State()

    change_lang = State()
    


class UserStates(StatesGroup):
    pass