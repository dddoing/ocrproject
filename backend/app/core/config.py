"""
Application configuration management
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings from environment variables"""

    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Universal Document Translator"

    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:3001"]

    # Database
    DATABASE_URL: str = "postgresql://docuser:yourpassword@localhost:5432/docdb"

    # Redis
    REDIS_URL: str = "redis://localhost:6379"

    # LLM APIs
    ANTHROPIC_API_KEY: str = ""
    OPENAI_API_KEY: str = ""

    # File Upload
    MAX_IMAGE_SIZE_MB: int = 10
    UPLOAD_DIR: str = "uploads"
    TEMP_FILE_RETENTION_HOURS: int = 24

    # OCR Settings
    OCR_LANGUAGES: List[str] = ["ko", "en", "ja", "ch_sim"]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
