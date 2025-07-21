# app/db/__init__.py

from .sql import SQLITEDBPOOL, init_sqlite_db, close_multi_connection_db_session
from dataclasses import dataclass
from app.config import Configtype,CONFIG

@dataclass
class DB:
    SQLITEDB: SQLITEDBPOOL

def init_dbs(c : Configtype) -> DB:
    """
    Initializes the database connection pool.
    Returns a DB dataclass with the pools.
    """
    Sqlitedatabase = init_sqlite_db(c.DATABASE_URL)
    return DB(
        SQLITEDB=Sqlitedatabase
    )

DBS = init_dbs(CONFIG)

__all__ = [
    "DBS",
    "close_multi_connection_db_session",
]



