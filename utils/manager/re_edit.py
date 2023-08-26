from emoji import emojize

"""Содержит формат редактирования текста и смайликов для бота"""


class Format:
    """
    Редактирование стиля текста
    """

    def __init__(self):
        # Одинарные стили
        self.__bold = '<b>{}</b>'  # Жирный
        self.__italic = '<i>{}</i>'  # Курсив
        self.__underline = '<u>{}</u>'  # Подчеркнутый
        self.__strike = '<s>{}</s>'  # Зачеркнутый

        # Двойные стили
        self.__bold_italic = '<b><i>{}</i></b>'  # Жирно-курсивный
        self.__bold_under = '<b><u>{}</u></b>'  # Жирно-подчеркнутый
        self.__bold_strike = '<b><s>{}</s></b>'  # Жирно-зачеркнутый

        self.__italic_underline = '<i><u>{}</u></i>'  # Курсивно-подчеркнутый
        self.__italic_strike = '<i><s>{}</s></i>'  # Курсивно-зачеркнутый

        # Тройные стили
        self.__bold_italic_under = '<b><i><u>{}</u></i></b>'  # Жирно-курсивно-подчеркнутый
        self.__bold_italic_strike = '<b><i><s>{}</s></i></b>'  # Жирно-курсивно-зачеркнутый

        # Библиотека стилей для получения по ключу
        self.__data = {
            'b': self.__bold,
            'i': self.__italic,
            'u': self.__underline,
            's': self.__strike,

            'bi': self.__bold_italic,
            'bu': self.__bold_under,
            'bs': self.__bold_strike,

            'iu': self.__italic_underline,
            'is': self.__italic_strike,

            'biu': self.__bold_italic_under,
            'bis': self.__bold_italic_strike,
        }

    def style(self, preset: str = None, string: str = None) -> str:
        """
        Редактирование стиля текста

        :param preset: Ключ редактирования (b, i, u, s, bi, ...) запрос к self.__data
        :param string: Строка к которой требуется применить стиль
        :return: str
        """
        return self.__data[preset].format(string)


class Emo:
    """
    Класс смайликов для бота
    """

    def __init__(self):
        # logger
        self.log_start = emojize(":check_mark_button:")
        self.log_stop = emojize(":cross_mark:")
        self.log_warning = emojize(":warning:")
        self.log_error = emojize(":double_exclamation_mark:")
        self.log_name = emojize(":keycap_*:")

        # choice
        self.flag_us = emojize(":United_States:")
        self.flag_ru = emojize(":Russia:")

        # setting
        self.setting = emojize(":gear:")

        # news
        self.news_title = emojize(":diamond_with_a_dot:")
        self.news_view = emojize(":eye:")
        self.news_comment = emojize(":speech_balloon:")

        # info
        self.bot_name = emojize(":ringed_planet:")
        self.teacher = emojize(":man_teacher:")
        self.student = emojize(":man_student:")
        self.purpose = emojize(":pushpin:")
        self.link = emojize(":globe_with_meridians:")

        # o`clock
        self.__one_clock = emojize(":one_o’clock:")
        self.__two_clock = emojize(":two_o’clock:")
        self.__three_clock = emojize(":three_o’clock:")
        self.__four_clock = emojize(":four_o’clock:")
        self.__five_clock = emojize(":five_o’clock:")
        self.__six_clock = emojize(":six_o’clock:")
        self.__seven_clock = emojize(":seven_o’clock:")
        self.__eight_clock = emojize(":eight_o’clock:")
        self.__nine_clock = emojize(":nine_o’clock:")
        self.__ten_clock = emojize(":ten_o’clock:")
        self.__eleven_clock = emojize(":eleven_o’clock:")
        self.__twelve_clock = emojize(":twelve_o’clock:")

        # other
        self.left_arrow = emojize(":left_arrow:")
        self.right_arrow = emojize(":right_arrow:")
        self.glossary = emojize(":books:")
        self.bookmark_tab = emojize(":bookmark_tabs:")
        self.cross_mark = emojize(":cross_mark:")
        self.info = emojize(":information:")

    def clock(self, time: int) -> str:
        """
        Смайлики часов

        :param time: Время в формате числа (1, 2, 3, ...)
        :return: str (смайлик часов с нужным временем)
        """

        data = {
            (1, 13): self.__one_clock,
            (2, 14): self.__two_clock,
            (3, 15): self.__three_clock,
            (4, 16): self.__four_clock,
            (5, 17): self.__five_clock,
            (6, 18): self.__six_clock,
            (7, 19): self.__seven_clock,
            (8, 20): self.__eight_clock,
            (9, 21): self.__nine_clock,
            (10, 22): self.__ten_clock,
            (11, 23): self.__eleven_clock,
            (12, 0): self.__twelve_clock
        }

        for key, value in data.items():
            if time in key:
                return value


class Temp:
    """
    Класс собирающий в себе (reformat, smile) - сделано для более удобной навигации в коде

    Атрибуты:
        reformat - инициализирует класс Format для изменения стиля текста
        smile - инициализирует класс Emo для получения смайликов
    """

    def __init__(self):
        self.reformat = Format()
        self.smile = Emo()


edit = Temp()
