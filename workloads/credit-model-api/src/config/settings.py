# settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "credit-model-api"
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    MODEL_VERSION: str = "1.0.0-mock"

    # Modern Pydantic V2 configuration
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

@lru_cache()
def get_settings():
    return Settings()