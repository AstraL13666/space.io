from os import getenv

from dotenv import load_dotenv, find_dotenv

from utils import Error

connect = find_dotenv(".env")

# Если файл .env не найден -> выходим из программы с выводом ошибки
if not connect:
    exit(Error(100))

else:  # иначе подгружаем значения
    load_dotenv(connect)
    t = getenv("token")

    data = dict(token=getenv("token"), admin_id=getenv("admin_id"), log_bot=getenv("log_bot"), nasa_api=getenv("nasa_api"))
