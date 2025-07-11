
from .init_db import init_sqlite_db, close_db_coection, close_db_session , DATABASE_SESSION
from dataclasses import dataclass
from app.config import Log, config
import asyncio

@dataclass
class Dbs:
    sqlitedb : DATABASE_SESSION

async def init_dbs(c)-> Dbs:
    """
    Initialize the database.
    """
    try:
        Log.info("Initializing database...")
        sqlitedb = await init_sqlite_db(c.DATABASE_URL)
        return Dbs(sqlitedb)
    except Exception as e:
        Log.error(f"Failed to initialize database: {e}")
        raise
    finally:
        Log.info("Initialization process finished.")

Databases = asyncio.run(init_dbs(config))

__all__ = [
    "close_db_coection",
    "close_db_session",
    "Dbs",
    "Databases"
]