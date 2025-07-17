
# app/db/sql/default.py

import aiosqlite
from app.utils import _default_users
from app.config import Log

async def add_default_users(session: aiosqlite.Connection) -> bool:
    """
    Use the session to insert default users into the DB.
    Returns True on success, False on failure.
    """
    Log.info("Adding default users to the DB")
    try:
        for user in _default_users:
            await session.execute(
                """
                INSERT OR IGNORE INTO users 
                (user_uuid, username, role, email, password, is_active, is_deleted, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user["user_uuid"],
                    user["username"],
                    user["role"],
                    user["email"],
                    user["password"],
                    user.get("is_active", 1),
                    user.get("is_deleted", 0),
                    user["created_at"],
                    user["updated_at"],
                ),
            )
            Log.info(f"Default user added successfully: {user['username']}")
        await session.commit()
        return True
    except Exception as e:
        await session.rollback()
        Log.error(f"Failed to add default users: {e}")
        return False
