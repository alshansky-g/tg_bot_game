import asyncio
import logging

from aiogram import Bot, Dispatcher

from config.config import load_config
from handlers import other, user


async def main():
    config = load_config()

    logging.basicConfig(level=config.log.level, format=config.log.format)

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    dp.include_router(user.router)
    dp.include_router(other.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
