from aiogram import Bot
from googletrans import Translator

from g4f.client import Client

from config_reader import config

client = Client()

translator = Translator()
bot = Bot(token=config.bot_token.get_secret_value())