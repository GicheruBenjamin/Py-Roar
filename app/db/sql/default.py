# app/db/sql/default.py
from app.utils import _default_users
from app.config import Log
from .types import SQLITEDBSESSION

def add_default_users(session: SQLITEDBSESSION) -> bool:
    """
    Insert default users into the 'users' table.
    Uses INSERT OR IGNORE to avoid duplicate user_uuid/email conflicts.
    Returns True on full success, False if any error occurs.
    """
    Log.info("Starting to insert default users...")

    try:
        session.execute("BEGIN")

        for user in _default_users:
            Log.info(f"Inserting user: {user['username']} ({user['user_uuid']})")

            session.execute(
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
                    int(user.get("is_active", True)),
                    int(user.get("is_deleted", False)),
                    user["created_at"],
                    user["updated_at"],
                ),
            )

        session.commit()
        Log.info("All default users inserted successfully ✅")
        return True

    except Exception as e:
        session.rollback()
        Log.error(f"Failed to insert default users ❌: {e}")
        return False
