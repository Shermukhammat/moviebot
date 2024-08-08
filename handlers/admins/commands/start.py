from loader import dp, db, bot, types, BOT_NAME, InlineButtons, AdminType, DefoltButtons, Context
from aiogram.dispatcher import FSMContext 


@dp.message_handler(lambda update : db.is_admin(update.from_user.id), commands='start', state = '*')
async def start_command_handler(update : types.Message, state : FSMContext):
    await finish_state(state)
    
    admin = db.get_admin(update.from_user.id)
    admin_type = get_admin_type(admin['type'])
        
    await bot.set_my_commands(commands = [types.BotCommand(command = 'start', description = '✈️ Botni ishga tushrish')],
                              scope = types.BotCommandScopeChat(chat_id = update.from_user.id))

    await update.answer(Context.menu.get(admin['lang']), reply_markup = DefoltButtons.adminMenu()) 
    await update.answer(f"👮‍♂️ Admin: [{update.from_user.first_name}]({update.from_user.url}) \n⏳ Ro'yxatdan o'tdi: {admin['registered']} \n📌 Status: {admin_type}",
                            reply_markup = InlineButtons.search_movie,
                            parse_mode = types.ParseMode.MARKDOWN)


        

async def finish_state(state : FSMContext):
    if state:
        await state.finish()


def get_admin_type(admin_type : int) -> str:
    if admin_type == AdminType.owner:
        return "ega"
    return "tayinlangan"