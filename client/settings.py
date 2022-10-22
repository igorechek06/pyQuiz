from pydantic import BaseSettings


class Settings(BaseSettings):
    url: str = "http://pyquiz.igorek.dev:5000"
