from app.config import Log

"""
This file runs DB migrations:
- Creates tables & joins
- Logs before and after each step
"""

# Example DDL statements:
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_uuid TEXT UNIQUE NOT NULL,
    username TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('user', 'leader', 'admin')),
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
"""

create_message_table = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_uuid TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    creator_id INTEGER NOT NULL,
    is_published BOOLEAN NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES users(id)
);
"""

create_migration_table = """
CREATE TABLE IF NOT EXISTS migrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    applied_at TEXT NOT NULL
);
"""

record_initial_migration = """
INSERT INTO migrations (name, applied_at)
VALUES ('initial_migration', datetime('now'));
"""

# (add your other DDL statements if needed)

async def run_migrations(conn):
    """
    Runs DB migrations synchronously on sqlite3 connection.
    """
    ddl_statements = [
        ("create_users_table", create_users_table),
        ("create_message_table", create_message_table),
        ("create_migration_table", create_migration_table),
        ("record_initial_migration", record_initial_migration)
    ]

    try:
        Log.info("🚀 Starting migrations...")
        conn.execute("BEGIN;")

        for name, ddl in ddl_statements:
            if ddl.strip():
                Log.debug(f"⚙️ Running migration: {name}")
                conn.execute(ddl)
                Log.info(f"✅ Migration '{name}' completed")
            else:
                Log.warning(f"⚠️ Skipped empty migration '{name}'")

        conn.execute("COMMIT;")
        Log.info("✅ All migrations applied successfully")
    except Exception as e:
        conn.execute("ROLLBACK;")
        Log.error(f"❌ Migration failed: {e}")
        raise
    finally:
        Log.debug("Migration process finished.")
