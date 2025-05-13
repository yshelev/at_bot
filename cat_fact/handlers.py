import aiohttp
from aiogram import Router, types
from aiogram.filters import Command
from pydantic import ValidationError

from cat_fact.constants.text import (FETCH_API_ERROR_DEV,
                                     RESPONSE_DOESNT_CONTAINS_FACT)
from cat_fact.utils import fetch_fact_api
from general.constants.text import (TRANSLATION_ERROR_OUTPUT)
from general.errors import TranslationException
from general.utils import translate, handle_error

cat_fact_router = Router()


@cat_fact_router.message(Command('catfact'))
async def send_cat_fact(message: types.Message):
    try:
        fact = await fetch_fact_api()
    except ValidationError:
        handle_error(RESPONSE_DOESNT_CONTAINS_FACT,
                     message)
        return
    except aiohttp.ClientError as e:
        handle_error(FETCH_API_ERROR_DEV,
                     message)
        return


    try:
        translated_fact = await translate(fact)
    except TranslationException as e:
        handle_error(TRANSLATION_ERROR_OUTPUT,
                     message)
        return

    await message.answer(translated_fact)