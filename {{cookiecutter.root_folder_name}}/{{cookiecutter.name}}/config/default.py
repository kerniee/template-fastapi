from os import environ

from pydantic import BaseSettings


class DefaultSettings(BaseSettings):
    """
        Default configs for application.

        Usually, we have three environments: for development, testing and production.
        But in this situation, we only have standard settings for local development.
        """

    ENV: str = environ.get("ENV", "local")
    DEBUG: bool = bool(environ.get("DEBUG", ""))
    PATH_PREFIX: str = environ.get("PATH_PREFIX", "")

    DB_NAME: str = environ.get("DB_NAME", "shortener_db")
    DB_PATH: str = environ.get("DB_PATH", "localhost")
    DB_USER: str = environ.get("DB_USER", "master")
    DB_PORT: int = int(environ.get("DB_PORT", 5432))
    DB_PASSWORD: str = environ.get("DB_PASSWORD", "hackme")
    DB_ECHO: bool = bool(environ.get("DB_ECHO", ""))

    @property
    def database_settings(self) -> dict:
        """
        Get all settings for connection with database.
        """
        return {
            "database": self.DB_NAME,
            "user": self.DB_USER,
            "password": self.DB_PASSWORD,
            "host": self.DB_PATH,
            "port": self.DB_PORT,
        }

    @property
    def database_uri(self) -> str:
        """
        Get uri for connection with database.
        """
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )
