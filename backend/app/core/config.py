import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None
    HF_MODEL_REPO: str | None = None
    USE_GPU: bool = False
    STORAGE_KEY: str | None = None
    SECRET_KEY: str = "change-me"
    MODEL_CACHE_DIR: str = "backend/app/models_cache"

settings = Settings()
