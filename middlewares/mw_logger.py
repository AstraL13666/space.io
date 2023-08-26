import asyncio
import logging
from typing import List, Union

from loguru import logger

from config_data import admin
from loader import logger_bot

"""Вывод логгера в консоль и отправка в отдельного бота логов, для отслеживания работы"""


class InterceptHandler(logging.Handler):
    """
    Структура логгера, отправка в консоль
    """

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        if level == 'ERROR' or record.getMessage() in ("Start polling", "Polling stopped"):
            asyncio.create_task(notify(msg=f"{level} | {record.getMessage()}"))
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


async def notify(msg: str):
    """
    Отправка лога в бот

    :param msg: str
    :return: None
    """
    await logger_bot.send_message(chat_id=admin, text=f'@space_io_bot | {msg}')


def custom_notify(text: str) -> None:
    """
    Отправка лога в консоль

    :param text: str
    :return: None
    """
    logger.info(text)


def setup_logger(level: Union[str, int] = "DEBUG", ignored: List[str] = ""):
    """
    Работа логгера в консоли

    :param level: уровень, значимость лога
    :param ignored: игнор-лист логов
    :return: None
    """
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.getLevelName(level))

    for ignore in ignored:
        logger.disable(ignore)

    logger.info('Logging is successfully configured')
