from aiogram.filters import Command

from aiogram import Router, types
from aiohttp import ClientResponseError
from pydantic import ValidationError

from cat_picture.constants.text import (FETCH_API_ERROR_DEV,
                                        RESPONSE_DOESNT_CONTAINS_URL_PICTURE)
from cat_picture.utils import fetch_cat_photo_api
from general.utils import handle_error

cat_picture_router = Router()


@cat_picture_router.message(Command("cat_picture"))
async def send_cat_picture(message: types.Message):
	try:
		photo_url = await fetch_cat_photo_api()
	except ClientResponseError:
		handle_error(error_text=FETCH_API_ERROR_DEV,
		             message_to_response=message)
		return
	except ValidationError:
		handle_error(error_text=RESPONSE_DOESNT_CONTAINS_URL_PICTURE,
		             message_to_response=message)
		return


	await message.answer_photo(caption="вот котик 😽",
	                           photo=photo_url)
