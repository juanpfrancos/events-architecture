from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_URL = f"{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/{os.getenv("EVENTS_DB")}"


class Settings(BaseSettings):
    DATABASE_URL: str = f"postgresql://{DATABASE_URL}"
    APP_NAME: str = "Auth Service"

settings = Settings()
