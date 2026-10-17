import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from db.connection import init_db
from middlewares.throttling import ThrottlingMiddleware
from handlers import user_router, operator_router, admin_router
from utils.logger import logger

async def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN .env faylida topilmadi! Iltimos, .env faylini tekshiring.")
        return

    logger.info("Initializing database...")
    await init_db()

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Register Middlewares
    dp.message.middleware(ThrottlingMiddleware())

    # Include Routers
    dp.include_router(admin_router)
    dp.include_router(operator_router)
    dp.include_router(user_router)

    logger.info("Bot starting polling...")
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Bot polling stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot shutdown completed.")