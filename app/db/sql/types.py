# app/db/sql/types.py
import sqlite3
from typing import Optional

# Type alias for SQLite single connection session
SQLITEDBSESSION = Optional[sqlite3.Connection]

# Type alias for SQLite connection pool
SQLITEDBPOOL = Optional[list[sqlite3.Connection]]
