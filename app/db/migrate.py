
# app/db/migrate.py
from app.config import Log

"""
This is the migration file.
It sets up the SQLite database schema safely.
"""

# --- optional roles lookup table instead of enum ---
create_roles_table = """
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);
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
create_messages_table = """
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
create_user_messages_table = """
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
create_tags_table = """
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_uuid TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    creator_id INTEGER NOT NULL,
    description TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES users(id)
);
"""

# --- user_tags join table ---
create_user_tags_table = """
CREATE TABLE IF NOT EXISTS user_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);
"""

# --- message_tags join table ---
create_message_tags_table = """
CREATE TABLE IF NOT EXISTS message_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (message_id) REFERENCES messages(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);
"""

# --- comments table ---
create_comments_table = """
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
create_message_comments_table = """
CREATE TABLE IF NOT EXISTS message_comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,
    comment_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (message_id) REFERENCES messages(id),
    FOREIGN KEY (comment_id) REFERENCES comments(id)
);
"""

# --- migrations table to track history ---
create_migrations_table = """
CREATE TABLE IF NOT EXISTS migrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    applied_at TEXT NOT NULL
);
"""

# --- insert migration record safely ---
record_initial_migration = """
INSERT OR IGNORE INTO migrations (name, applied_at)
VALUES ('initial_migration', datetime('now'));
"""

async def run_migrations(conn):
    """
    Runs all migrations inside a transaction, logs each step, and rolls back on failure.
    """
    ddl_statements = [
        ("create_roles_table", create_roles_table),
        ("create_users_table", create_users_table),
        ("create_messages_table", create_messages_table),
        ("create_user_messages_table", create_user_messages_table),
        ("create_tags_table", create_tags_table),
        ("create_user_tags_table", create_user_tags_table),
        ("create_message_tags_table", create_message_tags_table),
        ("create_comments_table", create_comments_table),
        ("create_message_comments_table", create_message_comments_table),
        ("create_migrations_table", create_migrations_table),
        ("record_initial_migration", record_initial_migration),
    ]

    try:
        Log.info("🚀 Starting database migrations...")
        await conn.execute("BEGIN;")
        for name, ddl in ddl_statements:
            Log.debug(f"▶️ Running migration: {name}")
            await conn.execute(ddl)
            Log.info(f"✅ Migration '{name}' applied successfully")
        await conn.execute("COMMIT;")
        Log.info("🎉 All migrations completed without errors")
    except Exception as e:
        await conn.execute("ROLLBACK;")
        Log.error(f"❌ Migration failed: {e}")
        raise
    finally:
        Log.debug("📦 Migration process finished.")
