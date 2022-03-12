from os import getenv
from dataclasses import dataclass


@dataclass
class Config:
    app_port: int
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    def __init__(self):
        self.app_port = int(getenv("PORT", 5000))
        self.db_host = getenv("DB_HOST")
        self.db_port = int(getenv("DB_PORT", 5432))
        self.db_user = getenv("DB_USER")
        self.db_password = getenv("DB_PASSWORD")
        self.db_name = getenv("DB_NAME")
