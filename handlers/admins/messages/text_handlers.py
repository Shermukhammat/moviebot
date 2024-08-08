from loader import dp, db, types, AdminStates, DefoltButtons, Context
from aiogram.dispatcher import FSMContext


@dp.message_handler(lambda update : db.is_admin(update.from_user.id))
async def admin_text_handler(update : types.Message, state : FSMContext):
    admin = db.get_admin(update.from_user.id)
    
    if update.text == "🎬 Kino qo'shish ➕":
        await state.set_state(AdminStates.get_movie_title)
        await update.answer(f"Ok, [{update.from_user.first_name}]({update.from_user.url}) kino nomni kiriting", 
                            reply_markup = DefoltButtons.cancle_button,
                            parse_mode = types.ParseMode.MARKDOWN)
    
    elif update.text in ["⚙️ Sozlamalar", "⚙️ Настройки", "⚙️ Settings"]:
        await state.set_state(AdminStates.change_lang)
        await update.answer(Context.owner_not_registred)

    else:
        await update.answer('menu', reply_markup = DefoltButtons.adminMenu())