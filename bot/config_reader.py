from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
import os

class Settings(BaseSettings):
    BOT_TOKEN: str # при необходими заменить на SecretStr
    OPENAI_TOKEN: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

print(os.getcwd())

config = Settings()
