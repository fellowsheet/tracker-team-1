import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config_data.config import settings
from handlers import router as main_router

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode="HTML"),
        )
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_routers(main_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
