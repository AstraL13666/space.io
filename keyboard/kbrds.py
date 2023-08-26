from utils.settings import setting

from .button import Button
from .inline import Inline


class Keyboards:
    """
    Класс собирающий в себе (line, inline) кнопки - сделано для более удобной навигации в коде

    Атрибуты:
        button - инициализирует класс Button для получения line кнопок (Внизу бота, под полем ввода)
        inline - инициализирует класс Button для получения inline кнопок (под сообщением)
            value - настройки бота, получаем язык бота
    """

    def __init__(self):
        self.button = Button()
        self.inline = Inline(value=setting)


kbrd = Keyboards()
