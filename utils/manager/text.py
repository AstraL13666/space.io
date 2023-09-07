from .re_edit import edit
from ..misc import counter, datanews, pos
from ..settings import setting

"""Библиотека текста, выполнена в стиле ООП - для наилучшей навигации в коде"""


class Library:
    """
    Основной сборник текстов бота
    """

    def __init__(self, value):
        self.__setting = value
        self.__data = {
            "select_lang": (f"Language set: {edit.smile.flag_us} English\nChange the language: Settings",
                            f"Выбран язык: {edit.smile.flag_ru} Русский\nИзменить язык: Настройки"),

            "setting": (
                f"{edit.smile.setting} Setting\n\nTo change the language, click on the corresponding button below:",
                f"{edit.smile.setting} Настройки\n\nЧтобы изменить язык, нажмите на соответствующую кнопку ниже:"
            ),

            "welcome": (f"{edit.reformat.style('b', 'Greetings young space lover!')}\n\n"
                        f"{edit.reformat.style('b', 'Briefly about the bot:')}\n"
                        f"╠ {edit.reformat.style('b', 'SS')} | WebApp | Menu button\n"
                        f"║ ╙ {edit.reformat.style('i', 'Briefly about the Solar system')}\n"
                        f"╠{'═' * 27}\n"
                        f"║ {edit.reformat.style('iu', 'Bot`s button')}\n"
                        f"╠{'═' * 27}\n"
                        f"╠ {edit.reformat.style('b', 'Pics')}\n"
                        f"║ ╙ {edit.reformat.style('i', 'Send a picture from the database')}\n"
                        f"╠ {edit.reformat.style('b', 'News')}\n"
                        f"║ ╙ {edit.reformat.style('i', 'Will send 3 latest news')}\n"
                        f"╚ {edit.reformat.style('b', 'Wiki')}\n"
                        f"   ╙ {edit.reformat.style('i', 'Send glossary')}\n",

                        f"{edit.reformat.style('b', 'Приветствую юный любитель космоса!')}\n\n"
                        f"{edit.reformat.style('b', 'Кратко о боте:')}\n"
                        f"╠ {edit.reformat.style('b', 'SS')} | WebApp | Кнопка меню\n"
                        f"║ ╙ {edit.reformat.style('i', 'Кратко о Солнечной системе')}\n"
                        f"╠{'═' * 27}\n"
                        f"║ {edit.reformat.style('iu', 'Кнопки бота')}\n"
                        f"╠{'═' * 27}\n"
                        f"╠ {edit.reformat.style('b', 'Картинки')}\n"
                        f"║ ╙ {edit.reformat.style('i', 'Отправит картинку из базы данных')}\n"
                        f"╠ {edit.reformat.style('b', 'Новости')}\n"
                        f"║ ╙ {edit.reformat.style('i', 'Отправит 3 последние новости')}\n"
                        f"╚ {edit.reformat.style('b', 'Глоссарий')}\n"
                        f"   ╙ {edit.reformat.style('i', 'Отправит глоссарий')}\n"),

            "glossary": (
                f"{edit.smile.glossary} Glossary - mini reference book about some of the terms collected here\n\n"
                f"{edit.smile.bookmark_tab} Page:",
                f"{edit.smile.glossary} Глоссарий - это мини справочник о некоторых терминах собранных здесь\n\n"
                f"{edit.smile.bookmark_tab} Страница:"
            ),

            "info": (
                f"{edit.smile.bot_name} space.io\n\n"
                f"{edit.smile.teacher} S. Crivosheev | K. Smirnov\n"
                f"{edit.smile.student} Vladimir Kotov\n\n"
                f"{edit.smile.purpose} Graduation project SkillBox\n\n"
                f"{edit.smile.link} Link:\n"
                f"TG: t.me/vlad_prin\n"
                f"GitLab: https://gitlab.skillbox.ru/vladimir_kotov_1\n\n"
                f"ver.: 1.3 (finally)",
                f"{edit.smile.bot_name} space.io\n\n"
                f"{edit.smile.teacher} С. Кривошеев | К. Смирнов\n"
                f"{edit.smile.student} Владимир Котов\n\n"
                f"{edit.smile.purpose} Дипломный проект SkillBox\n\n"
                f"{edit.smile.link} Ссылки:\n"
                f"TG: t.me/vlad_prin\n"
                f"GitLab: https://gitlab.skillbox.ru/vladimir_kotov_1\n\n"
                f"ver.: 1.3 (finally)",
            ),

            "help": (
                f"{edit.smile.info} Information\n\n"
                f"{edit.reformat.style(preset='b', string='The bot supports the following interactions:')}\n"
                f"╠ {edit.reformat.style(preset='iu', string='Commands')}\n"
                f"║ ╙ There are only two teams: /start /help\n"
                f"╠ {edit.reformat.style(preset='iu', string='WebApp')}\n"
                f"║ ║ To the left of the input line, there is a\n"
                f"║ ║ button SS - Solar Simulation\n"
                f"║ ║ - it will download WebApp\n"
                f"║ ╙ - site with data about Solar system\n"
                f"╠ {edit.reformat.style(preset='iu', string='Button')}\n"
                f"║ ║ The main interaction with the bot,\n"
                f"║ ╙ buttons under the input field\n"
                f"╚ {edit.reformat.style(preset='iu', string='Message')}\n"
                f"    ║ You enter a message and \n"
                f"    ║ send to the bot, \n"
                f"    ║ the bot sends you an action \n"
                f"    ║ or a term similar \n"
                f"    ║ to your request. \n"
                f"    ╙ (70% similarity)",

                f"{edit.smile.info} Информация\n\n"
                f"{edit.reformat.style(preset='b', string='Бот поддерживает следующие взаимодействия:')}\n"
                f"╠ {edit.reformat.style(preset='iu', string='Команды')}\n"
                f"║ ╙ Команды всего 2: /start /help\n"
                f"╠ {edit.reformat.style(preset='iu', string='WebApp')}\n"
                f"║ ║ Слева от строки ввода, есть кнопка \n"
                f"║ ║ SS - Solar Simulation - она прогрузит\n"
                f"║ ║ WebApp - сайт с данными о\n"
                f"║ ╙ Солнечной системе\n"
                f"╠ {edit.reformat.style(preset='iu', string='Кнопки')}\n"
                f"║ ║ Основное взаимодействие с ботом,\n"
                f"║ ╙ кнопки под полем ввода\n"
                f"╚ {edit.reformat.style(preset='iu', string='Сообщение')}\n"
                f"    ║ Вы вводите сообщение и \n"
                f"    ║ отправляете боту, \n"
                f"    ║ бот Вам отправить действие\n"
                f"    ║ или термин, похожим \n"
                f"    ║ на Ваш запрос. \n"
                f"    ╙ (Сходство 70%)"
            ),
            "change_lang": (
                f"{edit.smile.log_warning} The language has already been changed",
                f"{edit.smile.log_warning} Данный язык уже выбран"
            ),
            "possible": (
                f"{edit.smile.info} Perhaps you meant:",
                f"{edit.smile.info} Возможно Вы имели ввиду:"
            )
        }

    # Чекаем язык бота
    @property
    def __lang(self):
        return 0 if self.__setting.language == "en" else 1

    # Выбор языка
    async def select_lang(self):
        return self.__data["select_lang"][self.__lang]

    # Приветствие
    async def welcome(self):
        return self.__data["welcome"][self.__lang]

    # Настройки
    async def setting(self):
        return self.__data["setting"][self.__lang]

    # Парсинг новостей и реформат под сообщение бота
    async def news(self, param: str = None):
        from keyboard import kbrd

        if param == "prev":
            if pos.news_pos - 1 == 0:
                pos.news_pos = 0
            else:
                pos.news_pos -= 1
        else:
            if pos.news_pos + 1 == 3:
                pos.news_pos = 0
            else:
                pos.news_pos += 1

        title = (f"{datanews.news_en[pos.news_pos]['title']}", f"{datanews.news_ru[pos.news_pos]['title']}")
        desc = (f"{datanews.news_en[pos.news_pos]['desc']}", f"{datanews.news_ru[pos.news_pos]['desc']}")
        date = (f"{datanews.news_en[pos.news_pos]['date']}", f"{datanews.news_en[pos.news_pos]['date']}")
        view = (
            f"{datanews.news_en[pos.news_pos]['counts']['view']}",
            f"{datanews.news_ru[pos.news_pos]['counts']['view']}")

        comment = (f"{datanews.news_en[pos.news_pos]['counts']['comment']}",
                   f"{datanews.news_ru[pos.news_pos]['counts']['comment']}")

        link_url = datanews.news_en[pos.news_pos]['link']
        link_img = datanews.news_en[pos.news_pos]['image']

        publish_smile = int(date[0].split(" ")[1].split(":")[0])

        result = f"{edit.smile.news_title} {title[self.__lang]}\n\n" \
                 f"{desc[self.__lang]}\n\n" \
                 f"{edit.smile.news_view} {view[self.__lang]}  " \
                 f"{edit.smile.news_comment} {comment[self.__lang]}  " \
                 f"{edit.smile.clock(time=publish_smile)} {date[self.__lang]}\n\n" \
                 f"⋱ astronews.ru ⋰"

        return dict(text=result, keyboard=kbrd.inline.news_more(link=link_url), image=link_img)

    # Кнопка подробнее
    async def go_to_site(self):
        return self.__data["more"]

    # Глоссарий
    async def glossary(self):
        return self.__data["glossary"][self.__lang]

    # Описание глоссария
    async def wiki_desc(self, term: str, desc: str):
        return f'{edit.reformat.style(preset="b", string=term)} - {desc}'

    # Инфо о боте
    async def info(self):
        return self.__data["info"][self.__lang]

    # Помощь
    async def help(self, param: str) -> str:
        return self.__data["help"][self.__lang] if param == "command" else self.__data["help"][param]

    # Выбор языка помощи
    async def change_lang(self, param: str) -> str:
        return self.__data["change_lang"][0 if param == "change_en" else 1]

    # Поиск термина
    async def possible(self):
        return self.__data["possible"][self.__lang]

    # Поиск термина - не найден
    async def not_found(self):
        return f"{edit.smile.log_warning} Not found! | Не найдено!"


class MultiLang:
    """
    Выбор языка, начальное сообщение после команды /start
    """

    def __init__(self):
        self.choice_lang = f"Hello!\nPlease, select Your Language:" \
                           f"\n{'-' * 50}\n" \
                           f"Здравствуйте!\nПожалуйста, выберите Ваш язык:"


class TextButton:
    """
    Текст кнопок бота
    """

    def __init__(self, value):
        self.__setting = value

        self.en_choice_lang = f'{edit.smile.flag_us} English'
        self.ru_choice_lang = f'{edit.smile.flag_ru} Русский'

        self.left_arrow = f"{edit.smile.left_arrow}"
        self.right_arrow = f"{edit.smile.right_arrow}"

        self.__data = {
            "more": ("More...", "Подробнее..."),
            "pic": ("Pic", "Картинки"),
            "news": ("News", "Новости"),
            "wiki": ("Glossary", "Глоссарий"),
            "setting": ("Setting", "Настройки"),
            "info": ("Info", "Инфо")
        }
        self.delete = f"{edit.smile.cross_mark}"

    # Чекаем язык бота
    @property
    def __lang(self): return 0 if self.__setting.language == "en" else 1

    # Точка запроса текста кнопок
    def user_but(self, func: str): return self.__data[func][self.__lang]


class Temp:
    """
    Класс собирающий в себе (multi_lang, button, private) - сделано для более удобной навигации в коде

    Атрибуты:
        multi_lang - инициализирует класс MultiLang начального текста выбора языка (после /start)
        button - инициализирует класс TextButton для получения текста кнопок
        private - инициализирует класс Library для получения текста
            value -> str : получаем язык бота
    """

    def __init__(self):
        self.multi_lang = MultiLang()
        self.button = TextButton(value=setting)
        self.private = Library(value=setting)


txt = Temp()
