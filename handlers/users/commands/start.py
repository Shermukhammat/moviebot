from loader import dp, db, types, BOT_NAME


@dp.message_handler(commands='start')
async def start_command_handler(update : types.Message):
    if db.is_user(update.from_user.id):
        pass
    elif db.is_admin(update.from_user.id):
        pass
    else:
        print(1)
        await update.answer(f"👋 Assalomu alykum [{update.from_user.first_name}]({update.from_user.username})! Xush kelibsiz! 🎬 Bugun nima kino ko'ramiz?", 
                            parse_mode = types.ParseMode.MARKDOWN_V2)