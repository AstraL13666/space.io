from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from utils.manager import txt
from utils.misc import counter, wiki, pos
from utils.misc.data_classes import data_wiki


class Inline:
    """
    inline - класс, набор кнопок меню под сообщением

    Атрибуты:
        choice_language - выбор языка
        __setting - чтение языка из настроек
        del_button - кнопка удаления меню

    Методы:
        __lang -> str : Язык бота
        __choice_language -> from aiogram.utils.keyboard.InlineKeyboardBuilder : Выбор языка, начальное сообщение
        news_more -> from aiogram.utils.keyboard.InlineKeyboardBuilder : Кнопки с гипер-ссылкой на новость и переключение
        wiki -> from aiogram.utils.keyboard.InlineKeyboardBuilder : Вывод кнопок терминов Wiki из json
        back_to_wiki  -> from aiogram.utils.keyboard.InlineKeyboardBuilder : Аналог кнопки назад Термин -> Вики
        delete  -> from aiogram.utils.keyboard.InlineKeyboardBuilder : Кнопка удаления сообщения
        change_lang  -> from aiogram.utils.keyboard.InlineKeyboardBuilder : Выбор языка в окне помощи
    """

    def __init__(self, value):
        self.choice_language = self.__choice_language()
        self.__setting = value
        self.del_button = InlineKeyboardButton(text="Delete", callback_data="delete")

    @property
    def __lang(self):
        return self.__setting.language

    def __choice_language(self):

        button = [
            InlineKeyboardButton(text=txt.button.en_choice_lang, callback_data='en_choice_lang'),
            InlineKeyboardButton(text=txt.button.ru_choice_lang, callback_data='ru_choice_lang')
        ]

        return InlineKeyboardBuilder().row(*button).adjust(1).as_markup()

    def news_more(self, link):
        text_button = txt.button.user_but(func="more")
        size = 3 if pos.news_pos == 1 else 2

        if pos.news_pos == 0:
            button = [
                InlineKeyboardButton(text=text_button, url=link),
                InlineKeyboardButton(text=txt.button.right_arrow, callback_data="next_news")
            ]

        elif pos.news_pos == 1:
            button = [
                InlineKeyboardButton(text=txt.button.left_arrow, callback_data="prev_news"),
                InlineKeyboardButton(text=text_button, url=link),
                InlineKeyboardButton(text=txt.button.right_arrow, callback_data="next_news"),
            ]

        else:
            button = [
                InlineKeyboardButton(text=txt.button.left_arrow, callback_data="prev_news"),
                InlineKeyboardButton(text=text_button, url=link)
            ]

        return InlineKeyboardBuilder().row(*button).adjust(size).as_markup()

    def wiki(self):
        res_wiki = wiki.marks()

        b = InlineKeyboardBuilder()

        for exl in range(len(res_wiki)):
            for inl in range(len(res_wiki[exl])):
                b.row(
                    InlineKeyboardButton(text=res_wiki[exl][inl],
                                         callback_data=f'{res_wiki[exl][inl]}')
                )

        b.adjust(3)

        if data_wiki.page == 1:
            b.row(InlineKeyboardButton(text=txt.button.right_arrow, callback_data="next_wiki"))

        elif data_wiki.page == data_wiki.lens:
            b.row(InlineKeyboardButton(text=txt.button.left_arrow, callback_data="prev_wiki"))

        else:
            b.row(
                InlineKeyboardButton(text=txt.button.left_arrow, callback_data="prev_wiki"),
                InlineKeyboardButton(text=txt.button.right_arrow, callback_data="next_wiki")
            )

        return b.as_markup()

    def back_to_wiki(self):
        return InlineKeyboardBuilder().row(
            InlineKeyboardButton(text=txt.button.left_arrow, callback_data="back_wiki")).as_markup()

    def delete(self, param=False):
        button = [
            InlineKeyboardButton(text=txt.button.delete, callback_data="delete")
        ]

        if param is False:
            return InlineKeyboardBuilder().row(*button).as_markup()
        else:
            return button

    def change_lang(self):
        button = [
            InlineKeyboardButton(text=txt.button.ru_choice_lang, callback_data="change_ru"),
            InlineKeyboardButton(text=txt.button.en_choice_lang, callback_data="change_en"),
            *self.delete(param=True)
        ]

        return InlineKeyboardBuilder().row(*button).adjust(2).as_markup()
