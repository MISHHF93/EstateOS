from functools import lru_cache

from pydantic import BaseModel, Field


class Settings(BaseModel):
    app_name: str = 'EstateOS Backend'
    api_prefix: str = '/api/v1'
    api_version: str = '0.1.0'
    environment: str = Field(default='development')
    docs_enabled: bool = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
