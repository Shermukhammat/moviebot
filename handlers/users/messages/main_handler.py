from loader import dp, bot, db, UserStates, AdminStates, BOT_NAME, types, InlineButtons
from aiogram.dispatcher import FSMContext



@dp.message_handler()
async def main_user_text_handler(update : types.Message, state : FSMContext):
    if db.is_user(update.from_user.id):
        await user_handler(update, state)

    elif db.is_admin(update.from_user.id):
        await admin_handler(update, state)

    else:
        db.register_user(update.from_user.id, update.from_user.first_name)

        await bot.set_my_commands(commands = [types.BotCommand(command = 'start', description = '✈️ Botni ishga tushrish'),
                                              types.BotCommand(command = 'manual', description = "📖 Botdan foydalanish qo'llanmasi")],
                                  scope = types.BotCommandScopeChat(chat_id = update.from_user.id))
        
        await update.answer(f"👋 Assalomu alykum [{update.from_user.first_name}]({update.from_user.url}), xush kelibsiz! 🤖 Men {BOT_NAME}man \n🎬 Kino kodni kirting yoki 🔍 kino izlash tugmasni bosing", 
                            parse_mode = types.ParseMode.MARKDOWN,
                            reply_markup = InlineButtons.search_movie)
        

async def user_handler(update : types.Message, state : FSMContext):
    if update.text.isnumeric():
        pass
    
    else:
        await update.answer("Kino kodni kiriting yoki kino izlash tugmasini bosing")
        


async def admin_handler(update : types.Message, state : FSMContext):
    pass