from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from utils.manager import txt


class Button:
    """
    Стандартное меню кнопок доступное пользователю

    Методы:
        welcome - то самое меню
        remove - удаление кнопок (всплывает при выборе языка)
    """

    def welcome(self):
        kb = [
            [
                KeyboardButton(text=txt.button.user_but(func="pic")),
                KeyboardButton(text=txt.button.user_but(func="news")),
                KeyboardButton(text=txt.button.user_but(func="wiki")),
            ],
            [
                KeyboardButton(text=txt.button.user_but(func="setting")),
                KeyboardButton(text=txt.button.user_but(func="info"))
            ]
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    def remove(self):
        return ReplyKeyboardRemove()
