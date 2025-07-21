# app/db/sql/init_db.py
import sqlite3
from app.config import Log
from .migration import migrate_sqlite_db
from .default import add_default_users
from .types import SQLITEDBSESSION, SQLITEDBPOOL


def create_single_connection_db_session(url: str) -> SQLITEDBSESSION:
    """
    Create a single-connection DB session for initial setup.
    """
    Log.info("🔧 Opening single-connection DB session")
    try:
        conn = sqlite3.connect(url)
        conn.row_factory = sqlite3.Row  # optional: for dict-like row access
        Log.success("✅ Single DB session opened")
        return conn
    except sqlite3.Error as e:
        Log.error(f"❌ Failed to open DB session: {e}")
        return None


def close_single_connection_db_session(session: SQLITEDBSESSION) -> None:
    """
    Close a single-connection DB session.
    """
    if session:
        session.close()
        Log.info("🔒 Single-connection DB session closed")


def create_multi_connection_db_session(url: str, pool_size: int = 100) -> SQLITEDBPOOL:
    """
    Create a simulated connection pool (list of DB sessions) for concurrent app usage.
    """
    Log.info(f"🚀 Creating multi-connection pool (size={pool_size})")
    pool = []
    for i in range(pool_size):
        try:
            conn = sqlite3.connect(url, check_same_thread=False)
            conn.row_factory = sqlite3.Row
            pool.append(conn)
        except sqlite3.Error as e:
            Log.error(f"❌ Failed to create connection #{i + 1}: {e}")
    Log.success(f"✅ Connection pool created with {len(pool)} sessions")
    return pool


def close_multi_connection_db_session(sessions: SQLITEDBPOOL) -> None:
    """
    Gracefully close all connections in the simulated pool.
    """
    Log.info("🧯 Closing multi-connection pool")
    if sessions:
        for i, conn in enumerate(sessions):
            try:
                conn.close()
            except sqlite3.Error as e:
                Log.error(f"❌ Failed to close pool connection #{i + 1}: {e}")
    Log.info("✅ Multi-connection pool closed")


def init_sqlite_db(url: str, pool_size: int = 100) -> SQLITEDBPOOL:
    """
    Full database setup pipeline:
    1. Create single session for migration & seeding
    2. Run DDL migrations (tables, constraints, indexes)
    3. Add default data (e.g. users)
    4. Close the single-use session
    5. Create and return a pool of reusable connections
    """
    Log.info("🛠️ Starting full database initialization")

    # Step 1: Single connection session
    session = create_single_connection_db_session(url)
    if not session:
        Log.error("❌ Aborting: could not open DB for setup.")
        return []

    # Step 2: Run migrations
    if not migrate_sqlite_db(session):
        close_single_connection_db_session(session)
        Log.error("❌ Aborting: migration failed.")
        return []

    # Step 3: Insert default data
    if not add_default_users(session):
        close_single_connection_db_session(session)
        Log.error("❌ Aborting: failed to seed default data.")
        return []

    # Step 4: Close setup session
    close_single_connection_db_session(session)

    # Step 5: Create pool
    pool = create_multi_connection_db_session(url, pool_size)
    Log.success("✅ Database initialization complete")

    return pool
