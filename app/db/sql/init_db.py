
# app/db/sql/init_db.py

from app.config import Log
from .migration import migrate_sqlite_db
from .default import add_default_users

# Type alias for SQLite session
SQLITEDBSESSION = aiosqlite.Connection


async def create_single_connection_db_session(url: str) -> SQLITEDBSESSION:
    """
    Create a single-connection DB session for initial setup.
    """
    Log.info("🔧 Opening single-connection DB session")
    session = await aiosqlite.connect(url)
    session.row_factory = aiosqlite.Row
    return session


async def close_single_connection_db_session(session: SQLITEDBSESSION) -> None:
    """
    Close a single-connection DB session.
    """
    Log.info("🔒 Closing single-connection DB session")
    await session.close()


async def create_multi_connection_db_session(
    url: str, pool_size: int = 100
) -> list[SQLITEDBSESSION]:
    """
    Create a simulated connection pool (list of DB sessions) for concurrent app usage.
    """
    Log.info(f"🚀 Creating multi-connection pool (size={pool_size})")
    sessions: list[SQLITEDBSESSION] = []
    for _ in range(pool_size):
        conn = await aiosqlite.connect(url, check_same_thread=False)
        conn.row_factory = aiosqlite.Row
        sessions.append(conn)
    return sessions


async def close_multi_connection_db_session(sessions: list[SQLITEDBSESSION]) -> None:
    """
    Gracefully close all connections in the simulated pool.
    """
    Log.info("🧯 Closing multi-connection pool")
    for session in sessions:
        await session.close()


async def init_sqlite_db(url: str) -> list[SQLITEDBSESSION]:
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
    single = await create_single_connection_db_session(url)

    # Step 2: Run migrations
    if not await migrate_sqlite_db(single):
        await close_single_connection_db_session(single)
        raise RuntimeError("❌ DB migration failed")

    # Step 3: Insert default data
    if not await add_default_users(single):
        await single.rollback()
        await close_single_connection_db_session(single)
        raise RuntimeError("❌ Default user insertion failed")

    # Step 4: Close setup session
    await close_single_connection_db_session(single)

    # Step 5: Create pool
    pool = await create_multi_connection_db_session(url)
    Log.info("✅ Database initialization complete")
    return pool
