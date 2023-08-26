from dataclasses import dataclass

"""Временные классы памяти"""


@dataclass
class Position:
    """
    Сохраняет в оперативной памяти, при работе бота, данные позиции картинок
    из базы данных и номер страницы новостей

    Атрибуты:
        db_pos: int - номер картинки из базы данных, цель: циклическое переключение по базе
        news_pos: int - номер страницы новостей, цель: переключение между новостями (1 <-> 2 <-> 3)
    """

    db_pos: int = 1
    news_pos: int = 0


@dataclass
class WikiMemory:
    """
    Сохраняет в оперативной памяти, при работе бота, данные глоссария

    Атрибуты:
        page: int - номер страницы
        lens: int - кол-во страниц (генерация кнопок)
    """
    page: int = 1
    lens: int = None


@dataclass
class MemoryNews:
    """
    Сохраняет в оперативной памяти, при работе бота,
    данные полученные в результате парсинга сайта

    Атрибуты:
        news_en: dict - сохранение новостей на английском языке {текст, картинка, ссылка}
        news_ru: dict - сохранение новостей на русском языке {текст, картинка, ссылка}
    """

    news_en: dict = None
    news_ru: dict = None


class Counter:
    """Счетчик с классом памяти"""

    def __init__(self):
        self.__pos = Position()
        self.news = Position.news_pos

    def db(self, stop: int):

        if self.__pos.db_pos == stop:
            self.__pos.db_pos = 1

        else:
            self.__pos.db_pos += 1

        return self.__pos.db_pos


counter = Counter()
datanews = MemoryNews()
data_wiki = WikiMemory()
