import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from config import TOKEN
from Handlers.admin import router as admin_router
from Handlers.admin_delete import router as delete_router
from Handlers.admin_create_serial import router as serial_cr_router
from Handlers.admin_add_serial import router as serial_add_router
from Handlers.admin_add_kino import router as kino_add_router
from Handlers.users_kino import router as user_kino
from Handlers.user_serial import router as user_serial


dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(admin_router)
    dp.include_router(serial_cr_router)
    dp.include_router(serial_add_router)
    dp.include_router(kino_add_router)
    dp.include_router(delete_router)
    dp.include_router(user_kino)
    dp.include_router(user_serial)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

