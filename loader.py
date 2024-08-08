from aiogram import Bot, Dispatcher, types
from config import API_TOKEN, BOT_NAME, BOT_USER_NAME
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import DataBase, AdminType, Movie
from utilities.states import AdminStates, UserStates 
from utilities.buttons import InlineButtons, DefoltButtons
from utilities.picsum import Picsum
from context import Context 
from utilities.context import Context as Context2
from utilities.command_setter import set_admin_commands, set_user_commands

bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())

db = DataBase('data/data.db', 'data/settings.json')
picsum = Picsum(db.TELEGRAPH_TOKEN) 

adim_context = Context2('data/context/admin.yaml')
user_context = Context2('data/context/user.yaml')
# commands_context = Context2('data/context/commands.yaml')
