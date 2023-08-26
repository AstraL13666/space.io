from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_data import token, logger_bot

bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

logger_bot = Bot(token=logger_bot)
