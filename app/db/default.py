

# app/db/default.py

"""
This module inserts default users into the database.
"""

from app.config import Log, config
from app.utils.hash_password import hash_password

# hardcoded defaults; passwords will be hashed at runtime
DEFAULT_USERS_RAW = [
    {
        "user_uuid": "user-uuid-1",
        "username": "admin-one",
        "role": "admin",
        "email_index": 0,  # index in ADMIN_EMAILS
        "password": "adminonepassword",
        "is_active": True,
        "created_at": "2023-01-01T00:00:00",
        "updated_at": "2023-01-01T00:00:00"
    },
    {
        "user_uuid": "user-uuid-2",
        "username": "admin-two",
        "role": "admin",
        "email_index": 1,
        "password": "admintwopassword",
        "is_active": True,
        "created_at": "2023-01-01T00:00:00",
        "updated_at": "2023-01-01T00:00:00"
    }
]

async def add_default_users(conn):
    """
    Add default admin users to the database.
    """

    try:
        Log.info("Adding default admin users...")

        for user in DEFAULT_USERS_RAW:
            hashed_pwd = hash_password(user["password"])
            email = config.ADMIN_EMAILS[user["email_index"]]

            sql = """
                INSERT INTO users (
                    user_id, username, role, email, password, is_active, created_at, updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(email) DO NOTHING
            """

            params = (
                user["user_uuid"],
                user["username"],
                user["role"],
                email,
                hashed_pwd,
                user["is_active"],
                user["created_at"],
                user["updated_at"]
            )

            await conn.execute(sql, params)
            Log.info(f"Added default user: {user['username']}")

        Log.info("Default users added successfully.")

    except Exception as e:
        Log.error(f"Failed to add default users: {e}")
        raise
