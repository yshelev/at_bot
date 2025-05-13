from aiogram import types, Router

from config_reader import config
from general.constants.variables import bot

chatting_router = Router()

@chatting_router.message()
async def copy_message_to_my_chat(message: types.Message):
    gf_chat_id = int(config.gf_chat_id.get_secret_value())
    my_chat_id = int(config.my_chat_id.get_secret_value())

    if gf_chat_id == message.chat.id:
        if not "/" in message.text:
            await message.copy_to(
                chat_id=my_chat_id
            )

    return False


@chatting_router.message_reaction()
async def send_gf_reaction_to_my_chat(message_reaction: types.MessageReactionUpdated):
    user = message_reaction.user
    chat = message_reaction.chat
    message_id = message_reaction.message_id
    old_reactions = message_reaction.old_reaction
    new_reactions = message_reaction.new_reaction
    gf_chat_id = int(config.gf_chat_id.get_secret_value())
    my_chat_id = int(config.my_chat_id.get_secret_value())

    if chat.id == gf_chat_id:
        await bot.send_message(
            my_chat_id,
            f"👀 {user.full_name} поставил реакцию на сообщение: {message_id}!\n"
            f"📌 Было: {old_reactions}\n"
            f"📌 Стало: {new_reactions}"
        )
    return False