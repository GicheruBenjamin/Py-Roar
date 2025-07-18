
# app/db/sql/migration.py

import aiosqlite
from .migration_ddl import DDL_STATEMENTS
from app.config import Log

async def migrate_sqlite_db(session: aiosqlite.Connection) -> bool:
    """
    Migrate the SQLite database using the DDL_STATEMENTS.
    Uses a single-connection session.
    Returns True if migration succeeds, False otherwise.
    """
    try:
        Log.info("Beginning migration transaction")
        await session.execute("BEGIN")
        for statement in DDL_STATEMENTS:
            preview = statement.strip().splitlines()[0]
            Log.info(f"Executing DDL: {preview}...")
            # executescript handles multiple-statement strings
            await session.executescript(statement)
            Log.info(f"Executed successfully: {preview}")
        await session.commit()
        Log.info("Migration committed successfully")
        return True
    except Exception as e:
        await session.rollback()
        Log.error(f"Migration failed, rolled back: {e}")
        return False
