from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    cat_fact_api: SecretStr
    cat_picture_api: SecretStr
    gf_chat_id: SecretStr
    my_chat_id: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()