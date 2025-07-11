

'''
This is the init_db file.
Used to use config to setup the database.

Plan:
=> 1. Connect to the database and create a single connection.
=> 2. Setup by creating tables and columns.
=> 3. Add default data.
=> 4. Close the connection to allow a db_session to be created.
=> 5. Provide a db session that allows a lot of operations.
=> 6. Have a backwards compatibility to close if needed.
'''

import sqlite3
from typing import Optional
from .default import add_default_users
from .migrate import run_migrations
from app.config import Log

# === Types ===
DATABASE_CONNECTION = Optional[sqlite3.Connection]
DATABASE_SESSION = Optional[sqlite3.Connection]  # sqlite3.Connection will act as session here

# -------------------------------------------------------
# Connect to the database (async wrapper around sync sqlite3)
# -------------------------------------------------------
async def connect_to_db(db_url: str) -> DATABASE_CONNECTION:
    """
    Create a single connection to the SQLite database.
    """
    try:
        Log.info(f"Connecting to database: {db_url}")
        # Parse db_url like sqlite:///data/db.sqlite3 → get path
        db_path = db_url.replace("sqlite:///", "", 1)
        conn = sqlite3.connect(db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row  # Enables dict-like access
        Log.info("Database connection established successfully.")
        return conn
    except Exception as e:
        Log.error(f"Failed to connect to database: {e}")
        raise

# -------------------------------------------------------
# Provide a db session
# -------------------------------------------------------
async def provide_db_session(conn: DATABASE_CONNECTION) -> DATABASE_SESSION:
    """
    Provide a db session to be used by repositories.
    In sqlite3, the connection itself acts as the session.
    """
    Log.info("Providing database session.")
    return conn

# -------------------------------------------------------
# Initialize the database fully
# -------------------------------------------------------
async def init_sqlite_db(db_url: str) -> DATABASE_SESSION:
    """
    Initialize the database:
    - connect
    - run migrations
    - add default data
    - return db session
    """
    try:
        conn = await connect_to_db(db_url)
        
        # Begin transaction for safety
        conn.execute("BEGIN")
        await run_migrations(conn)
        await add_default_users(conn)
        conn.commit()
        
        session = await provide_db_session(conn)
        Log.info("Database initialized successfully.")
        return session
    except Exception as e:
        Log.error(f"Failed to initialize database: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        Log.info("Initialization process finished.")

# -------------------------------------------------------
# Close connection and session
# -------------------------------------------------------
async def close_db_coection(conn: DATABASE_CONNECTION) -> None:
    """
    Close the database connection.
    """
    if conn:
        conn.close()
        Log.info("Database connection closed.")

async def close_db_session(session: DATABASE_SESSION) -> None:
    """
    Close the db session.
    In sqlite3, session is the same as connection.
    """
    if session:
        session.close()
        Log.info("Database session closed.")
