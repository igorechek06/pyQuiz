from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    database: PostgresDsn


config = Config()
