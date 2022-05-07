from lib2to3.pytree import Base
import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "To do API"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1  # 1 day


settings = Settings()
