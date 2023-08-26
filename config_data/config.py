from os import getenv

from dotenv import load_dotenv, find_dotenv

from utils import Error

# Если файл .env не найден -> выходим из программы с выводом ошибки
if not find_dotenv():
    exit(Error(100))

# иначе подгружаем значения
else:
    load_dotenv()

token = getenv("token")
admin = getenv("admin_id")
logger_bot = getenv("logger_bot")
rapid_api_key = getenv("rapid_api")
