import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from src.config.config import token
from database.db import DataBase

storage = MemoryStorage()
bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
db = DataBase('src/database/graduate_database.db3')

logging.basicConfig(level=logging.INFO)


async def main():
    from states import dp
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.get_session()


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except (KeyboardInterrupt, RuntimeError, SystemExit):
        print('Bot stopped!')
