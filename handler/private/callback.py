import asyncio

from aiogram import Router, F
from aiogram.handlers.callback_query import CallbackQuery

from keyboard import kbrd
from loader import bot
from utils import setting
from utils.manager import txt, image
from utils.misc.data_classes import data_wiki
from utils.misc.wiki_func import wiki

callback_router = Router(name='callback_router')


@callback_router.callback_query(F.data.in_({"en_choice_lang", "ru_choice_lang"}))
async def choose_language(call: CallbackQuery):
    """
    Ловим кэлбэк (ответ) языка от пользователя, выбор языка бота (рус, анг)

    :param call: aiogram.handlers.callback_query.CallbackQuery
    :return: None
    """

    if call.data == "en_choice_lang":
        setting.language = "en"

    else:
        setting.language = "ru"

    await call.answer(text=f"{await txt.private.select_lang()}", show_alert=True)
    await asyncio.sleep(0.2)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    await bot.send_photo(
        chat_id=call.message.chat.id,
        photo=image.logo,
        caption=f"{await txt.private.welcome()}",
        parse_mode="HTML",
        reply_markup=kbrd.button.welcome()
    )


@callback_router.callback_query(F.data.in_({"next_news", "prev_news"}))
async def pages(call: CallbackQuery):
    """
    Ловим ответ кнопок пользователя переключения окон новостей (1 окно <-> 2 окно <-> 3 окно)

    :param call: aiogram.handlers.callback_query.CallbackQuery
    :return: None
    """

    # В зависимости от полученного кэлбэка изменяем номер страницы (влияет на загрузку контента новостей)
    param_page = "next" if call.data == "next_news" else "prev"
    res = await txt.private.news(param_page)

    await bot.edit_message_media(
        media={"type": "photo",
               "media": res["image"],
               "caption": res["text"],
               "parse_mode": "HTML"},
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=res["keyboard"]
    )


@callback_router.callback_query(F.data.in_({"prev_wiki", "next_wiki"}))
async def wiki_tab(call: CallbackQuery):
    """
    Ловим ответ кнопок пользователя переключения окон Глоссария (1 окно <-> 2 окно <-> ... окно)

    :param call: aiogram.handlers.callback_query.CallbackQuery
    :return: None
    """

    # В зависимости от полученного кэлбэка изменяем номер страницы (влияет на загрузку кнопок терминов)
    if call.data == "prev_wiki":
        data_wiki.page -= 1
    else:
        data_wiki.page += 1

    await bot.edit_message_caption(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        caption=f'{await txt.private.glossary()} {data_wiki.page}',
        parse_mode="HTML",
        reply_markup=kbrd.inline.wiki()
    )


@callback_router.callback_query(F.data.in_(wiki.call_all_marks()))
async def wiki_echo(call: CallbackQuery):
    """
    Ловим кэлбэк термина (от пользователя) если он есть в списке, редактируем сообщение на содержимое термина
    полученного из json

    :param call: aiogram.handlers.callback_query.CallbackQuery
    :return: None
    """

    # Делаем запрос в функцию, для получения контента по термину
    res = wiki.requests_mark(term=call.data)

    await bot.edit_message_media(
        media={"type": "photo",
               "media": res["pic"],
               "caption": f"{await txt.private.wiki_desc(term=call.data, desc=res['desc'])}",
               "parse_mode": "HTML"},
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=kbrd.inline.back_to_wiki()
    )


@callback_router.callback_query(F.data == "back_wiki")
async def reopen_tab_wiki(call: CallbackQuery):
    """
    Возвращаемся к таблице кнопок с терминами

    :param call: aiogram.handlers.callback_query.CallbackQuery
    :return: None
    """

    await bot.edit_message_media(
        media={"type": "photo",
               "media": image.wiki,
               "caption": f"{await txt.private.glossary()} {data_wiki.page}",
               "parse_mode": "HTML"},
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=kbrd.inline.wiki()
    )


@callback_router.callback_query(F.data == "delete")
async def delete(call: CallbackQuery):
    """
    Удаление сообщения

    :param call: aiogram.handlers.callback_query.CallbackQuery
    :return: None
    """
    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )


@callback_router.callback_query(F.data.in_({"change_ru", "change_en"}))
async def change_lang_help(call: CallbackQuery):
    """
    изменение языка окна Помощи

    :param call: aiogram.handlers.callback_query.CallbackQuery
    :return: None
    """

    res_text = await txt.private.help(param=1) if call.data == "change_ru" else await txt.private.help(param=0)

    try:
        await bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=res_text,
            parse_mode="HTML",
            reply_markup=kbrd.inline.change_lang()
        )

    except Exception:
        await call.answer(text=await txt.private.change_lang(param=call.data), show_alert=True)
