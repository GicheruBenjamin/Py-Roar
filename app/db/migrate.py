
# app/db/migrate.py
from app.config import Log

"""
This is the migration file
It is used to setup the database
"""

# --- simulate enum: user roles ---
create_user_role_enum = """
-- SQLite has no native ENUM, use CHECK constraint instead
"""

# --- users table ---
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

# --- messages table ---
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

# --- user_messages join table ---
create_user_message_table = """
CREATE TABLE IF NOT EXISTS user_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    message_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (message_id) REFERENCES messages(id)
);
"""

# --- tags table ---
create_tag_table = """
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    creator_id INTEGER NOT NULL,
    description TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES users(id)
);
"""

# --- user_tags join table ---
create_user_tag_table = """
CREATE TABLE IF NOT EXISTS user_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);
"""

# --- message_tags join table ---
create_message_tag_table = """
CREATE TABLE IF NOT EXISTS message_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (message_id) REFERENCES messages(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);
"""

# --- comments table ---
create_comment_table = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment_uuid TEXT UNIQUE NOT NULL,
    content TEXT NOT NULL,
    creator_id INTEGER NOT NULL,
    message_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES users(id),
    FOREIGN KEY (message_id) REFERENCES messages(id)
);
"""

# --- message_comments join table ---
create_message_comment_table = """
CREATE TABLE IF NOT EXISTS message_comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,
    comment_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (message_id) REFERENCES messages(id),
    FOREIGN KEY (comment_id) REFERENCES comments(id)
);
"""

# --- migrations table ---
create_migration_table = """
CREATE TABLE IF NOT EXISTS migrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    applied_at TEXT NOT NULL
);
"""

# --- insert record to migrations ---
record_migration = """
INSERT INTO migrations (name, applied_at)
VALUES ('initial_migration', datetime('now'));
"""


async def run_migrations(conn):
    """
    Used to run migrations:
    - Runs each DDL statement safely
    - Logs before & after each migration
    - Wraps in transaction if possible
    """
    ddl_statements = [
        ("create_user_role_enum", create_user_role_enum),
        ("create_users_table", create_users_table),
        ("create_message_table", create_message_table),
        ("create_user_message_table", create_user_message_table),
        ("create_tag_table", create_tag_table),
        ("create_user_tag_table", create_user_tag_table),
        ("create_message_tag_table", create_message_tag_table),
        ("create_comment_table", create_comment_table),
        ("create_message_comment_table", create_message_comment_table),
        ("create_migration_table", create_migration_table),
        ("record_initial_migration", record_migration),
    ]

    try:
        Log.info("Starting migrations...")
        # BEGIN transaction (some drivers auto-handle, but explicit better)
        await conn.execute("BEGIN;")
        
        for name, ddl in ddl_statements:
            if ddl.strip():  # skip empty statements
                Log.debug(f"Running migration: {name}")
                await conn.execute(ddl)
                Log.info(f"✅ Migration '{name}' completed")
            else:
                Log.warning(f"⚠️ Skipped empty migration '{name}'")

        await conn.execute("COMMIT;")
        Log.info("✅ All migrations applied successfully")
        
    except Exception as e:
        await conn.execute("ROLLBACK;")
        Log.error(f"❌ Migration failed: {e}")
        raise

    finally:
        Log.debug("Migration process finished.")