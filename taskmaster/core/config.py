from pydantic import MariaDBDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_ignore_empty=True)

    DB_HOST: str
    DB_PORT: int = 3306
    DB_USER: str
    DB_PASSWORD: str
    DB: str

    @property
    def DATABASE_URL(self) -> 'MariaDBDsn':
        SCHEME = 'mariadb+mariadbconnector'

        return MariaDBDsn.build(
            scheme=SCHEME,
            host=self.DB_HOST,
            port=self.DB_PORT,
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            path=self.DB,
        )
