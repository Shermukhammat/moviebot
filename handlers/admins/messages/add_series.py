from loader import dp, bot, db, UserStates, AdminStates, BOT_NAME, types, InlineButtons, DefoltButtons, Movie
from aiogram.dispatcher import FSMContext




@dp.message_handler(state = AdminStates.get_movie_title)
async def get_movie_title(update : types.Message, state : FSMContext):
    if update.text == "❌ Bekor qilish":
        await state.reset_state()
        await update.answer("Menu", reply_markup = DefoltButtons.adminMenu())
    
    elif len(update.text) >= 5:
        await state.set_state(AdminStates.get_movie_thumb)
        async with state.proxy() as data:
            data['title'] = update.text

        await update.answer("Kino poster 🖼 rasmini jo'nating", reply_markup = DefoltButtons.back_button(cancle_button = True))

    else:
        await update.answer("❌ Kino nomi 4 ta belgidan ko'p bo'lishi kerak")


@dp.message_handler(state = AdminStates.get_movie_thumb)
async def get_movie_thumb(update : types.Message, state : FSMContext):
    pass
