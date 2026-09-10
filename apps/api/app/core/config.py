import os

class Settings:
    PROJECT_NAME: str = "Agriculture & Voice AI Advisory API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://copilot_user:copilot_secure_password@localhost:5432/crop_advisory_db")

settings = Settings()
