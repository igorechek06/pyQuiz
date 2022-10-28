from pydantic import BaseSettings


class Settings(BaseSettings):
    url: str = "https://pyquiz.igorek.dev"


settings = Settings()
