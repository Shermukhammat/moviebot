from loader import dp, types


@dp.message_handler(commands='start')
async def start_command_handler(update : types.Message):
    await update.answer("I'm working :)")