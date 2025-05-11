import asyncio
import logging

from general.constants.variables import bot
from aiogram import Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

from cat_fact.constants.text import GREETING_TEXT
from cat_fact.handlers import cat_fact_router
from cat_picture.handlers import cat_picture_router
from gf.handlers import gf_router

load_dotenv()

logging.basicConfig(level=logging.INFO)


dp = Dispatcher()

dp.include_routers(
    cat_fact_router,
    cat_picture_router,
    gf_router
)


@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply(GREETING_TEXT)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())