from loader import AdminStates, db, dp, bot, types, InlineButtons
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(lambda query : query.data == 'save_movie', state = AdminStates.edit_movie_menu)
async def get_movie_resolution_calback_handler(query : types.CallbackQuery, state : FSMContext):
    data = await state.get_data()
    resolutions = data.get('resolutions')

    if not resolutions:
        await query.answer("❌ Iltimos birnchi kinoni yuklang", show_alert = True)
        return
    

    
@dp.callback_query_handler(lambda query : query.data == 'upload_movie', state = AdminStates.edit_movie_menu)
async def chose_resolution(query : types.CallbackQuery, state : FSMContext):
    await state.set_state(AdminStates.chose_resolution)
    await bot.edit_message_caption(chat_id = query.from_user.id,
                                   caption = "🎞 Iltimos video sifatni tanlang👇",
                                   reply_markup = InlineButtons.get_resolutions())
        

@dp.callback_query_handler(state = AdminStates.chose_resolution)
async def get_resolutions(query : types.CallbackQuery, state : FSMContext):
    if query.data.isnumeric() and int(query.data) in InlineButtons.resolutions:
        async with state.proxy() as data:
            data['resolution'] = int(query.data)
        await state.set_state(AdminStates.get_movie_video)
        # await bot.del        

    elif query.data == 'back':
        await  state.set_state(AdminStates.get_movie_video_resolution)
        
        data = await state.get_data()
        await bot.copy_message(chat_id = query.from_user.id,
                               from_chat_id = db.DATA_CHANEL_ID,
                               message_id = data['id'],
                               caption = f"Kino nomi: {data['title']} ",
                               reply_markup = InlineButtons.movie_add_menu())