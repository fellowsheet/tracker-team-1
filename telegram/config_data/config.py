from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	bot_token: str
	status: list = ["Done", "In review", "In progress", "Pending"]
	priority: list = ["Hight", "Normal", "Low"]

	class Config:
		env_file = ".env"

settings = Settings()