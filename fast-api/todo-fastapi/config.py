from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "todo API"

    class Config:
        env_file = ".env"