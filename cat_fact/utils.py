import aiohttp

from cat_fact.models import Fact
from config_reader import config

async def fetch_fact_api() -> str:
	async with aiohttp.ClientSession() as session:
		async with session.get(config.cat_fact_api.get_secret_value()) as response:
			response.raise_for_status()
			data = await response.json()
			validated_data = validate_fact_api_output(data)
			return validated_data.fact

def validate_fact_api_output(data: dict) -> Fact:
	return Fact(**data)

