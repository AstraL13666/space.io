import json
import os
from functools import reduce
from typing import Any

import jmespath

from utils.misc.data_classes import data_wiki
from utils.settings import setting

"""Работа с глоссарием"""


class WikiWork:
    """
    Класс для чтения, реформата, и вывода текста из json

    Атрибуты:
        __setting -> str : чекаем язык бота
    """

    def __init__(self, value):
        self.__setting = value

    # чтение языка бота
    @property
    def __lang(self):
        return self.__setting.language

    def __loader(self):

        """
        Открываем json - читаем

        :return: str
        """

        path = os.path.join(os.getcwd(), "utils", "misc", "wiki.json")

        with open(path, mode="r") as file:
            return json.load(file)

    def __search(self, lang: str = None):

        """
        Достаем термины по ключу, в зависимости языка

        :param lang: str - язык бота, для динамической прогрузки
        :return: dict
        """

        return jmespath.search(expression=f"{lang}", data=dict(self.__loader()))

    def __devide(self, arr: list) -> Any:

        """
        Разделяем полученные данные по спискам и отдаем родительскому запросу

        :param arr: list - Список терминов
        :return: list
        """

        pages = len(arr) // 9
        if len(arr) % 9 > 1:
            pages += 1

        data_wiki.lens = pages

        arr_list = [arr[i:i + 3] for i in range(0, len(arr), 3)]

        if data_wiki.page == 1:
            return arr_list[:data_wiki.page + 2]

        elif data_wiki.page == data_wiki.lens:
            return arr_list[data_wiki.page * 3 - 3:]

        else:
            return arr_list[data_wiki.page * 3 - 3:data_wiki.page * 3]

    def marks(self) -> list:

        """
        Вывод терминов, требуется в генерации кнопок (зависимость от языка)

        :return: dict
        """

        return self.__devide(arr=list(self.__search(self.__lang)))

    def call_all_marks(self) -> list:

        """
        Вывод всех терминов, нужен для проверки кэлбэка термина
        (зависимости языка нет, поэтому получаем русские и английские термины)

        :return: list
        """

        all_marks = list(list(self.__search(lang=lang)) for lang in ('ru', 'en'))
        return reduce(lambda x, y: x + y, all_marks)

    def requests_mark(self, term: str = None) -> dict:

        """
        Вывод одинарного термина

        :param term:
        :return: dict
        """

        return self.__search(lang=self.__lang)[term]


wiki = WikiWork(value=setting)
