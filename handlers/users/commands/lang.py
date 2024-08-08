from loader import dp, db, types, Context, InlineButtons



@dp.message_handler(lambda update : db.is_user(update.from_user.id), commands = 'lang')
async def lang_handler(update : types.Message):
    await update.answer("")