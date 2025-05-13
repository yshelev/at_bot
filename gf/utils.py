from general.constants.variables import client

async def get_lovely_message():
	response = client.chat.completions.create(
		model="gpt-4o-mini",
		messages=[{"role": "user",
		           "content": "напиши любовное послание для девушки, ТОЛЬКО СООБЩЕНИЕ БЕЗ КОММЕНТАРИЕВ"}]
	)

	return response.choices[0].message.content