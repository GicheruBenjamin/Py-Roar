

"""
Database bootstrap:
- Initializes SQLite DB on startup
- Provides typed holder
- Exports close functions for graceful shutdown
"""

import asyncio
from dataclasses import dataclass
from app.config import Log, config
from app.db.init_db import (
    init_sqlite_db,
    close_db_connection,
    close_db_session,
    DATABASE_SESSION,
)

@dataclass(frozen=True)
class Dbs:
    """
    Holds active database sessions.
    """
    sqlitedb: DATABASE_SESSION

async def init_dbs(cfg=config) -> Dbs:
    """
    Initialize the databases using configuration.
    """
    try:
        Log.info("🚀 Initializing SQLite database...")
        sqlitedb = await init_sqlite_db(cfg.DATABASE_URL)
        Log.info("✅ SQLite database initialized successfully.")
        return Dbs(sqlitedb=sqlitedb)
    except Exception as e:
        Log.error(f"❌ Failed to initialize databases: {e}")
        raise
    finally:
        Log.debug("🔧 init_dbs finished.")

# Synchronously run db initialization on startup.
# asyncio.run is safe here because it's top-level & script entry.
try:
    Databases: Dbs = asyncio.run(init_dbs())
except Exception as e:
    Log.critical(f"🚨 Could not start application due to DB init failure: {e}")
    raise SystemExit(1)

__all__ = [
    "close_db_connection",
    "close_db_session",
    "Dbs",
    "Databases",
]
