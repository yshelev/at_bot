from aiogram import Bot
from googletrans import Translator

from config_reader import config

translator = Translator()
bot = Bot(token=config.bot_token.get_secret_value())
