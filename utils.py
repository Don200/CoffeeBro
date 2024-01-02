import openai
import logging
from config_reader import config
import texts
from openai import AsyncOpenAI
client = AsyncOpenAI(
    api_key=config.OPENAI_TOKEN
)

async def generate_text(prompt) -> dict:
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": texts.system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content, response.usage.total_tokens
    except Exception as e:
        logging.error(e)
   
