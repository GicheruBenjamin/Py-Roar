# app/db/sql/migration_ddl.py

# Users Table
create_users_table: str = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_uuid TEXT UNIQUE NOT NULL,
    username TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('user', 'leader', 'admin')),
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_active INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0,1)),
    is_deleted INTEGER NOT NULL DEFAULT 0 CHECK (is_deleted IN (0,1)),
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    updated_at DATETIME NOT NULL DEFAULT (datetime('now'))
);
"""

# Messages Table
create_messages_table: str = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_uuid TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    slug TEXT UNIQUE,
    creator_uuid TEXT NOT NULL,
    updated_by TEXT,
    is_published INTEGER NOT NULL DEFAULT 0 CHECK (is_published IN (0,1)),
    is_deleted INTEGER NOT NULL DEFAULT 0 CHECK (is_deleted IN (0,1)),
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    updated_at DATETIME NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (creator_uuid) REFERENCES users(user_uuid),
    FOREIGN KEY (updated_by) REFERENCES users(user_uuid)
);
"""

# UserMessages Table
create_user_messages_table: str = """
CREATE TABLE IF NOT EXISTS user_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_uuid TEXT NOT NULL,
    message_uuid TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    updated_at DATETIME NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (user_uuid) REFERENCES users(user_uuid),
    FOREIGN KEY (message_uuid) REFERENCES messages(message_uuid),
    UNIQUE(user_uuid, message_uuid)
);
"""

# Tags Table
create_tags_table: str = """
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_uuid TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    slug TEXT UNIQUE,
    creator_uuid TEXT NOT NULL,
    updated_by TEXT,
    description TEXT,
    is_deleted INTEGER NOT NULL DEFAULT 0 CHECK (is_deleted IN (0,1)),
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    updated_at DATETIME NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (creator_uuid) REFERENCES users(user_uuid),
    FOREIGN KEY (updated_by) REFERENCES users(user_uuid)
);
"""

# UserTags Table
create_user_tags_table: str = """
CREATE TABLE IF NOT EXISTS user_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_uuid TEXT NOT NULL,
    tag_uuid TEXT NOT NULL,
    created_by TEXT,
    notes TEXT,
    weight INTEGER DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    updated_at DATETIME NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (user_uuid) REFERENCES users(user_uuid),
    FOREIGN KEY (tag_uuid) REFERENCES tags(tag_uuid),
    FOREIGN KEY (created_by) REFERENCES users(user_uuid),
    UNIQUE(user_uuid, tag_uuid)
);
"""

# MessageTags Table
create_message_tags_table: str = """
CREATE TABLE IF NOT EXISTS message_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_uuid TEXT NOT NULL,
    tag_uuid TEXT NOT NULL,
    created_by TEXT,
    notes TEXT,
    weight INTEGER DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    updated_at DATETIME NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (message_uuid) REFERENCES messages(message_uuid),
    FOREIGN KEY (tag_uuid) REFERENCES tags(tag_uuid),
    FOREIGN KEY (created_by) REFERENCES users(user_uuid),
    UNIQUE(message_uuid, tag_uuid)
);
"""

# Comments Table
create_comments_table: str = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment_uuid TEXT UNIQUE NOT NULL,
    content TEXT NOT NULL,
    creator_uuid TEXT NOT NULL,
    updated_by TEXT,
    message_uuid TEXT NOT NULL,
    is_deleted INTEGER NOT NULL DEFAULT 0 CHECK (is_deleted IN (0,1)),
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    updated_at DATETIME NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (creator_uuid) REFERENCES users(user_uuid),
    FOREIGN KEY (updated_by) REFERENCES users(user_uuid),
    FOREIGN KEY (message_uuid) REFERENCES messages(message_uuid)
);
"""

# MessageComments Table
create_message_comments_table: str = """
CREATE TABLE IF NOT EXISTS message_comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_uuid TEXT NOT NULL,
    comment_uuid TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    updated_at DATETIME NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (message_uuid) REFERENCES messages(message_uuid),
    FOREIGN KEY (comment_uuid) REFERENCES comments(comment_uuid),
    UNIQUE(message_uuid, comment_uuid)
);
"""

# Extra indexes for performance
create_indexes: str = """
CREATE INDEX IF NOT EXISTS idx_users_user_uuid ON users(user_uuid);
CREATE INDEX IF NOT EXISTS idx_messages_message_uuid ON messages(message_uuid);
CREATE INDEX IF NOT EXISTS idx_messages_creator_uuid ON messages(creator_uuid);
CREATE INDEX IF NOT EXISTS idx_tags_tag_uuid ON tags(tag_uuid);
CREATE INDEX IF NOT EXISTS idx_tags_creator_uuid ON tags(creator_uuid);
CREATE INDEX IF NOT EXISTS idx_comments_comment_uuid ON comments(comment_uuid);
CREATE INDEX IF NOT EXISTS idx_comments_message_uuid ON comments(message_uuid);
CREATE INDEX IF NOT EXISTS idx_user_tags_user_uuid ON user_tags(user_uuid);
CREATE INDEX IF NOT EXISTS idx_user_tags_tag_uuid ON user_tags(tag_uuid);
CREATE INDEX IF NOT EXISTS idx_message_tags_message_uuid ON message_tags(message_uuid);
CREATE INDEX IF NOT EXISTS idx_message_tags_tag_uuid ON message_tags(tag_uuid);
"""

# DDL statements
DDL_STATEMENTS: list = [
    create_users_table,
    create_messages_table,
    create_user_messages_table,
    create_tags_table,
    create_user_tags_table,
    create_message_tags_table,
    create_comments_table,
    create_message_comments_table,
    create_indexes
]