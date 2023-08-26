from deep_translator import GoogleTranslator


class Translate:
    """
    Скрипт - переводчик (рус -> анг) для перевода текста новостей, если язык бота 'En'

    Методы:
        __init__ - инициализация библиотеки - переводчика
        __trans_query -> dict : запрос перевода на сервак
        get -> str : Запрос и отправка перевода родительскому запросу
    """

    def __init__(self):
        self.__trans = GoogleTranslator(source="ru", target="en")

    def __trans_query(self, proposal: str): return self.__trans.translate(proposal)

    def get(self, text):
        title = self.__trans_query(proposal=text["title"])
        desc = self.__trans_query(proposal=text["desc"])

        text["title"], text["desc"] = title, desc

        return text


translate = Translate()
