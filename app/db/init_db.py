

"""
Initialize the database:
- Connect
- Run migrations
- Add default data
- Return db session
"""

import sqlite3
from typing import Optional
from app.db.default import add_default_users
from app.db.migrate import run_migrations
from app.config import Log

# Types
DATABASE_CONNECTION = Optional[sqlite3.Connection]
DATABASE_SESSION = Optional[sqlite3.Connection]

async def connect_to_db(db_url: str) -> DATABASE_CONNECTION:
    """
    Create a connection to the SQLite database.
    """
    try:
        Log.info(f"🔌 Connecting to database: {db_url}")
        db_path = db_url.replace("sqlite:///", "", 1)
        conn = sqlite3.connect(db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row  # dict-like row access
        Log.info("✅ Database connection established.")
        return conn
    except Exception as e:
        Log.error(f"❌ Failed to connect to database: {e}")
        raise

async def provide_db_session(conn: DATABASE_CONNECTION) -> DATABASE_SESSION:
    """
    Provide a db session (in sqlite, same as connection).
    """
    Log.info("📦 Providing DB session.")
    return conn

async def init_sqlite_db(db_url: str) -> DATABASE_SESSION:
    """
    Initialize the database:
    - connect
    - run migrations
    - add default data
    - return session
    """
    conn: DATABASE_CONNECTION = None
    try:
        conn = await connect_to_db(db_url)

        Log.info("⚙️ Starting database initialization...")
        conn.execute("BEGIN")
        await run_migrations(conn)
        await add_default_users(conn)
        conn.commit()

        session = await provide_db_session(conn)
        Log.info("🎉 Database initialized successfully.")
        return session

    except Exception as e:
        Log.error(f"❌ Failed to initialize database: {e}")
        if conn:
            conn.rollback()
            Log.warning("🔄 Rolled back changes due to error.")
        raise
    finally:
        Log.debug("✅ Initialization process finished.")

async def close_db_connection(conn: DATABASE_CONNECTION) -> None:
    """
    Close the database connection.
    """
    if conn:
        conn.close()
        Log.info("🔒 Database connection closed.")

async def close_db_session(session: DATABASE_SESSION) -> None:
    """
    Close the db session (same as connection).
    """
    if session:
        session.close()
        Log.info("🔒 Database session closed.")
