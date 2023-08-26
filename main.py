from asyncio import run

from handler import private_router, callback_router
from loader import dp, bot
from middlewares import setup_logger, news_feed


async def polling_bot() -> None:
    """Функция инициализации и запуска бота"""

    # логгирование
    setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])

    # чтение сигналов
    dp.include_routers(private_router, callback_router)

    try:
        # Загружаем новости в локал
        await news_feed.parsing()

        # пропускаем обновления
        await bot.delete_webhook(drop_pending_updates=True)

        # запуск бота
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

    # если ловим ошибку - выводим в консоль и выключаем бота (finally)
    except Exception as error:
        print(f'ERROR | {error}')

    finally:
        await bot.session.close()


if __name__ == '__main__':
    run(polling_bot())
