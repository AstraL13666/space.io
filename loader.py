from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_data import data

bot = Bot(token=data["token"])
dp = Dispatcher(storage=MemoryStorage())

logger_bot = Bot(token=data["log_bot"])
