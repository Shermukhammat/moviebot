from loader import dp, bot, db, UserStates, AdminStates, BOT_NAME, types, InlineButtons, DefoltButtons, Movie
from aiogram.dispatcher import FSMContext

@dp.message_handler(content_types = types.ContentType.PHOTO)
async def get_movie_thumb(update : types.Message, state : FSMContext):
    pass