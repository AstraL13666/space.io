from dataclasses import dataclass

"""Хранит язык бота"""


@dataclass
class Setting:
    language: str = "en"


setting = Setting()
