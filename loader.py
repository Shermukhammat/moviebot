from aiogram import Bot, Dispatcher, types
from config import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())

