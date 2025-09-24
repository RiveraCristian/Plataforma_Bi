from functools import lru_cache
from typing import List, Optional
from pydantic import BaseSettings, Field, PostgresDsn, RedisDsn


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    project_name: str = Field(default="Plataforma BI")
    api_v1_prefix: str = Field(default="/api")

    database_url: PostgresDsn = Field(default="postgresql+psycopg2://postgres:postgres@localhost:5432/plataforma_bi")
    redis_url: RedisDsn = Field(default="redis://localhost:6379/0")

    minio_endpoint: str = Field(default="http://localhost:9000")
    minio_access_key: str = Field(default="minioadmin")
    minio_secret_key: str = Field(default="minioadmin")
    minio_bucket: str = Field(default="plataforma-bi")

    cors_origins: List[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    """Return cached settings instance."""

    return Settings()
