import logging
from aiogram import types

from general.constants.text import (MAIN_ERROR_OUTPUT,
                                    TRANSLATION_ERROR_OUTPUT)
from general.constants.variables import translator
from general.errors import TranslationException


async def translate(text: str,
              dest: str = "ru") -> str:
	try:
		return (await translator.translate(text, dest)).text
	except ValueError:
		raise TranslationException(TRANSLATION_ERROR_OUTPUT)

def handle_error(error_text: str,
                      message_to_response: types.Message):
	logging.error(error_text)
	message_to_response.answer(MAIN_ERROR_OUTPUT)