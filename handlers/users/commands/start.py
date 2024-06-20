from loader import dp, db, bot, types, BOT_NAME, InlineButtons, AdminType
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands='start', state = '*')
async def start_command_handler(update : types.Message, state : FSMContext):
    if db.is_user(update.from_user.id):
        await finish_state(state)
        user = db.get_user(update.from_user.id)

        await update.answer(f"👤 Foydalanuvchi: [{update.from_user.first_name}]({update.from_user.url}) \n⏳ Ro'yxatdan o'tdi: {user['registered']}  \n🎬 Kino kodni kirting yoki 🔍 kino izlash tugmasni bosing",
                            reply_markup = InlineButtons.search_movie,
                            parse_mode = types.ParseMode.MARKDOWN)
        

    elif db.is_admin(update.from_user.id):
        await finish_state(state)
        admin = db.get_admin(update.from_user.id)
        admin_type = get_admin_type(admin['type'])
        
        await bot.set_my_commands(commands = [types.BotCommand(command = 'start', description = '✈️ Botni ishga tushrish')],
                                  scope = types.BotCommandScopeChat(chat_id = update.from_user.id))
        
        await update.answer(f"👮‍♂️ Admin: [{update.from_user.first_name}]({update.from_user.url}) \n⏳ Ro'yxatdan o'tdi: {admin['registered']} \n📌 Status: {admin_type}",
                            reply_markup = InlineButtons.search_movie,
                            parse_mode = types.ParseMode.MARKDOWN)

    else:
        db.register_user(update.from_user.id, update.from_user.first_name)

        await bot.set_my_commands(commands = [types.BotCommand(command = 'start', description = '✈️ Botni ishga tushrish'),
                                              types.BotCommand(command = 'manual', description = "📖 Botdan foydalanish qo'llanmasi")],
                                  scope = types.BotCommandScopeChat(chat_id = update.from_user.id))
        
        await update.answer(f"👋 Assalomu alykum [{update.from_user.first_name}]({update.from_user.url}), xush kelibsiz! 🤖 Men {BOT_NAME}man \n🎬 Kino kodni kirting yoki 🔍 kino izlash tugmasni bosing", 
                            parse_mode = types.ParseMode.MARKDOWN,
                            reply_markup = InlineButtons.search_movie)
        

async def finish_state(state : FSMContext):
    if state:
        await state.finish()


def get_admin_type(admin_type : int) -> str:
    if admin_type == AdminType.owner:
        return "ega"
    return "tayinlangan"