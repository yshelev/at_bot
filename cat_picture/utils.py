import aiohttp

from cat_picture.models import Photo
from config_reader import config


async def fetch_cat_photo_api():
	async with aiohttp.ClientSession() as session:
		async with session.get(config.cat_picture_api.get_secret_value()) as response:
			response.raise_for_status()
			data = await response.json()
			validated_data = validate_data(data)
			return validated_data.url

def validate_data(data: dict):
	data = data[0]
	return Photo(**data)