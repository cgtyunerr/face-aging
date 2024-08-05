"""Configuration for the project."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the project."""

    DEBUG: bool = False
    LOG_LEVEL: str = "info"


settings: Settings = Settings()
