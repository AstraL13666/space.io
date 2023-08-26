import os

from peewee import SqliteDatabase, Model, CharField

from utils import setting
from utils.misc import counter

# Создание пути/бд и подключение к ней
db_dir = os.path.dirname(__file__)
db_name = 'data_pic.db'

if not os.path.isdir(db_dir):
    os.makedirs(db_dir)

db_path = os.path.join(db_dir, db_name)

db = SqliteDatabase(db_path)


class DataPic(Model):
    """
    Создание структуры базы данных

    Атрибуты:
        file_id : CharField (string) - id файла для отправки в бот
        desc_ru : CharField (string) - описание к файлу на русском языке
        desc_en : CharField (string) - описание к файлу на английском языке
    """
    file_id = CharField()
    desc_ru = CharField()
    desc_en = CharField()

    class Meta:
        database = db
        table_name = 'pictures'


class WorkDB:
    """
        Взаимодействие с базой данных через функцию, запрос <-> ответ

        Атрибуты:
            value : str - тут получаем язык бота их настроек

        Методы:
            __init__ : инициализация класса и установка параметров
            __check_amount_files -> str : получаем кол-во файлов в базе данных
            __lang -> str : динамическое получение языка
            get -> dict : возвращаем файл (картинку) с описанием на определенном языке (get <-> __lang)
        """

    def __init__(self, value):
        self.__init_db = db.create_tables([DataPic])
        self.__setting = value

    @classmethod
    def __check_amount_files(cls): return max(list(pos.id for pos in DataPic.select(DataPic.id).distinct().execute()))

    @property
    def __lang(self): return "en" if self.__setting.language == "en" else "ru"

    def get(self):
        stop = self.__check_amount_files()

        pos = counter.db(stop=stop)
        pic = DataPic.select().where(DataPic.id == pos).get()

        lang = dict(en=pic.desc_en, ru=pic.desc_ru)

        return dict(file_id=pic.file_id, desc=lang[self.__lang])


link_db = WorkDB(setting)
