# app/db/sql/migration.py

import sqlite3
from .migration_ddl import DDL_STATEMENTS
from app.config import Log
from .types import SQLITEDBSESSION

def migrate_sqlite_db(session: SQLITEDBSESSION) -> bool:
    """
    Migrate the SQLite database using the DDL_STATEMENTS.
    Uses a single-connection session.
    Returns True if migration succeeds, False otherwise.
    """

    Log.info("Beginning migration transaction...")
    try:
        session.execute("BEGIN")

        for statement in DDL_STATEMENTS:
            preview = statement.strip().splitlines()[0].strip()
            Log.info(f"Executing DDL: {preview}")
            session.executescript(statement)
            Log.info(f"Success: {preview}")

        session.commit()
        Log.info("Migration committed successfully ✅")
        return True

    except Exception as e:
        session.rollback()
        Log.error(f"Migration failed and rolled back ❌: {e}")
        return False
