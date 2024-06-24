from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	BOT_TOKEN: str = "BOT_TOKEN"
	

settings = Settings()