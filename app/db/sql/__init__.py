
from .init_db import init_sqlite_db, close_multi_connection_db_session
from app.config import config

SQLITE_DB_SESSION = init_sqlite_db(config.SQLITE_DB_URL)

__all__ = [
    "SQLITE_DB_SESSION",
    "close_multi_connection_db_session"
]