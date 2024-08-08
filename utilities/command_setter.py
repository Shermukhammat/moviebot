from .context import Context
from aiogram import Bot, types

commands_context = Context('data/context/commands.yaml')


commands_context.put_and_update("✈️ Botni ishga tushrish", src = 'uz', key = 'start')
commands_context.put_and_update("🌐 Tilni o'zgartirish", src = 'uz', key = 'lang')
commands_context.put_and_update("☠️ Admin paneldan chiqish", src = 'uz', key = 'logout')

async def set_admin_commands(admin_id : int, bot : Bot, lang : str = None):
    await bot.set_my_commands(commands = [
        types.BotCommand(command = 'start', description = commands_context.get('start', target = lang)),
        types.BotCommand(command = 'lang', description = commands_context.get('lang', target = lang)),
        types.BotCommand(command = 'logout', description = commands_context.get('logout', target = lang))
    ],
    scope = types.BotCommandScopeChat(chat_id = admin_id))




async def set_user_commands(user_id : int, bot : Bot, lang : str = None):
    await bot.set_my_commands(commands = [
        types.BotCommand(command = 'start', description = commands_context.get('start', target = lang)),
        types.BotCommand(command = 'lang', description = commands_context.get('lang', target = lang)),
    ],
    scope = types.BotCommandScopeChat(chat_id = user_id))