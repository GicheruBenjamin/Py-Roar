
# app/db/__init__.py

import asyncio
from .sql import init_sqlite_db, close_multi_connection_db_session, SQLITEDBSESSION
from dataclasses import dataclass
from app.config import config 

@dataclass
class Databases:
    """Databaes available for use in the app"""
    sqlite: SQLITEDBSESSION

async def init_db(c) -> Databases:
    """Initialize the database"""
    db = await init_sqlite_db(c.DATABASE_URL)
    return Databases(sqlite=db)

DBS = asyncio.run(init_db(config))

__all__ = [
    "Databases",
    "DBS"
]