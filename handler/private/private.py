import difflib

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from data_base import *  # link_db - взаимодействие с базой данных
from keyboard import kbrd
from loader import bot
from utils.manager import txt, image
from utils.misc.data_classes import data_wiki
from utils.misc.wiki_func import wiki

private_router = Router(name='private_router')


@private_router.message(Command(commands='start'))
async def start(m: Message):
    """
    Обработка команды /start

    :param m: aiogram.types.Message
    :return: None
    """

    await m.answer(
        text=txt.multi_lang.choice_lang,
        reply_markup=kbrd.inline.choice_language
    )


@private_router.message(Command(commands='help'))
async def help(m: Message):
    res_text = await txt.private.help(param="command")

    await m.answer_photo(
        photo=image.help,
        caption=res_text,
        parse_mode="HTML",
        reply_markup=kbrd.inline.change_lang()
    )


@private_router.message(F.text.in_({"Pic", "Картинки"}))
async def picture(m: Message):
    """
    Обработка кнопок картинки (вытягивает из базы картинку с описанием)

    :param m: aiogram.types.Message
    :return: None
    """

    data = link_db.get()  # Запрос в базу
    photo_id = data["file_id"]
    photo_desc = data["desc"]

    await bot.send_photo(
        chat_id=m.chat.id,
        photo=photo_id,
        caption=photo_desc
    )


@private_router.message(F.text.in_({"News", "Новости"}))
async def news(m: Message):
    """
    Парсинг новостей с сайта (3 новости)

    :param m: aiogram.types.Message
    :return: None
    """

    res = await txt.private.news()  # Получение данных (текст, картинка)

    await bot.send_photo(
        chat_id=m.chat.id,
        photo=res["image"],
        caption=res["text"],
        parse_mode="HTML",
        reply_markup=res["keyboard"]
    )


@private_router.message(F.text.in_({"Glossary", "Глоссарий"}))
async def glossary(m: Message):
    """
    Вики json

    :param m: aiogram.types.Message
    :return: None
    """
    await bot.send_photo(
        chat_id=m.chat.id,
        photo=image.wiki,
        caption=f"{await txt.private.glossary()} {data_wiki.page}",
        parse_mode="HTML",
        reply_markup=kbrd.inline.wiki()
    )


@private_router.message(F.text.in_({"Setting", "Настройки"}))
async def setting(m: Message):
    """
    Обработка кнопок настройки

    :param m: aiogram.types.Message
    :return: None
    """

    await m.answer(
        text=f'{await txt.private.setting()}',
        reply_markup=kbrd.inline.choice_language
    )


@private_router.message(F.text.in_({"Info", "Инфо"}))
async def setting(m: Message):
    """
    Обработка кнопок инфо

    :param m: aiogram.types.Message
    :return: None
    """

    await m.answer(
        text=f'{await txt.private.info()}',
        reply_markup=kbrd.inline.delete()
    )


@private_router.message()
async def echo(m: Message):
    """
    "Эхо - выдает термин из глоссария"

    :param m: aiogram.types.Message
    :return: None
    """

    # Получаем термины из глоссария на 2-х языках
    all_marks = wiki.call_all_marks()
    # Находим схожее слово
    res_diff = difflib.get_close_matches(word=m.text.title(), possibilities=all_marks, n=1, cutoff=0.7)

    if len(res_diff) == 0:
        await m.answer(
            text=await txt.private.not_found(),
            parse_mode="HTML",
            reply_markup=kbrd.button.remove()
        )

    else:
        res_call = wiki.requests_mark(term=res_diff[0])

        await m.answer_photo(
            photo=res_call["pic"],
            caption=f'{await txt.private.possible()}\n\n{res_diff[0]} {res_call["desc"]}',
            parse_mode="HTML",
            reply_markup=kbrd.inline.delete()
        )
