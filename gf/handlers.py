from aiogram import Router, types
from aiogram.filters import Command

from general.constants.variables import bot
from gf.constants.text import GF_ANS_TEXT
from config_reader import config
from gf.constants.text import NOT_TEXT_AFTER_GF_COMMAND

gf_router = Router()

@gf_router.message(Command("gf_message"))
async def send_to_gf(message: types.Message):
    gf_chat_id = int(config.gf_chat_id.get_secret_value())
    my_chat_id = int(config.my_chat_id.get_secret_value())

    if message.chat.id == gf_chat_id:
        await bot.send_message(
            chat_id=gf_chat_id,
            text=GF_ANS_TEXT
        )
    elif message.chat.id == my_chat_id:
        stripped_text = message.text.lstrip("/gf_message")
        if not stripped_text:
            await message.reply(
                text=NOT_TEXT_AFTER_GF_COMMAND
            )

        await bot.send_message(
            chat_id=gf_chat_id,
            text=stripped_text
        )