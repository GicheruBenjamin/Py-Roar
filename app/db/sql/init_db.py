
# app/db/sql/init_db.py

import aiosqlite
from app.config import Log
from .migration import migrate_sqlite_db
from .default import add_default_users

SQLITEDBSESSION = aiosqlite.Connection

async def create_single_connection_db_session(url: str) -> SQLITEDBSESSION:
    """
    Create a single-connection DB session for migration.
    """
    Log.info("🔧 Opening single-connection session")
    session = await aiosqlite.connect(url)
    session.row_factory = aiosqlite.Row
    return session

async def close_single_connection_db_session(session: SQLITEDBSESSION) -> None:
    """
    Close a single-connection DB session.
    """
    Log.info("🔒 Closing single-connection session")
    await session.close()

async def create_multi_connection_db_session(
    url: str, pool_size: int = 100
) -> list[SQLITEDBSESSION]:
    """
    Create a simulated pool of connections (list) for app use.
    """
    Log.info(f"🚀 Opening multi-connection pool (size={pool_size})")
    sessions: list[SQLITEDBSESSION] = []
    for _ in range(pool_size):
        conn = await aiosqlite.connect(url, check_same_thread=False)
        conn.row_factory = aiosqlite.Row
        sessions.append(conn)
    return sessions

async def close_multi_connection_db_session(
    sessions: list[SQLITEDBSESSION],
) -> None:
    """
    Close all connections in the multi-connection pool.
    """
    Log.info("🧯 Closing multi-connection pool")
    for session in sessions:
        await session.close()

async def init_sqlite_db(url: str) -> list[SQLITEDBSESSION]:
    """
    Full DB initialization:
      1. Create single-connection session
      2. Migrate (create tables, indexes, constraints)
      3. Add default data
      4. Close single-connection session
      5. Create multi-connection pool for app
    Returns the list of pooled sessions.
    """
    # 1. Single connection
    single = await create_single_connection_db_session(url)

    # 2. Migrate
    ok = await migrate_sqlite_db(single)
    if not ok:
        await close_single_connection_db_session(single)
        raise RuntimeError("DB migration failed")

    # 3. Add defaults
    ok = await add_default_users(single)
    if not ok:
        await single.rollback()
        await close_single_connection_db_session(single)
        raise RuntimeError("Inserting default data failed")

    # 4. Close single session
    await close_single_connection_db_session(single)

    # 5. Create multi-connection pool
    pool = await create_multi_connection_db_session(url)
    Log.info("Database initialization complete")
    return pool
