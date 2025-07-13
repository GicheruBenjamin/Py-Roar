"""
Handles SQLite DB:
- Connect
- Run migrations
- Add default data
- Provide db session
"""
import sqlite3
from typing import Optional
from .migrate import run_migrations
from .default import add_default_users
from app.config import Log

DATABASE_CONNECTION = Optional[sqlite3.Connection]
DATABASE_SESSION = Optional[sqlite3.Connection]

async def connect_to_db(db_url: str) -> DATABASE_CONNECTION:
    """
    Connect to SQLite DB.
    """
    try:
        Log.info(f"🔌 Connecting to database: {db_url}")
        db_path = db_url.replace("sqlite:///", "", 1)
        conn = sqlite3.connect(db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        Log.info("✅ Database connection established.")
        return conn
    except Exception as e:
        Log.error(f"❌ Failed to connect to database: {e}")
        raise

async def provide_db_session(conn: DATABASE_CONNECTION) -> DATABASE_SESSION:
    """
    In sqlite3, conn itself acts as session.
    """
    Log.info("📦 Providing database session.")
    return conn

async def init_sqlite_db(db_url: str) -> DATABASE_SESSION:
    """
    Init DB:
    - Connect
    - Run migrations
    - Add default data
    - Return session
    """
    conn = None
    try:
        Log.info("🚀 Initializing SQLite database...")
        conn = await connect_to_db(db_url)
        conn.execute("BEGIN;")
        await run_migrations(conn)
        await add_default_users(conn)
        conn.commit()
        session = await provide_db_session(conn)
        Log.info("✅ Database initialized successfully.")
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
    Close db connection.
    """
    if conn:
        conn.close()
        Log.info("🔌 Database connection closed.")

async def close_db_session(session: DATABASE_SESSION) -> None:
    """
    Close db session.
    """
    if session:
        session.close()
        Log.info("🔒 Database session closed.")

