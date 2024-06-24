from loader import AdminStates, db, dp, bot, types



@dp.callback_query_handler(state = AdminStates.get_movie_video_resolution)
async def get_movie_resolution_calback_handler(query : types.CallbackQuery):
    print(query.data)
