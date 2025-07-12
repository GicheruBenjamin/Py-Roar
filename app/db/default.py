
"""
Insert default admin users into the database.
"""

from app.config import Log, config
from app.utils.hash_password import hash_password

# hardcoded defaults; passwords will be hashed at runtime
DEFAULT_USERS_RAW = [
    {
        "user_uuid": "user-uuid-1",
        "username": "admin-one",
        "role": "admin",
        "email_index": 0,
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
    Add default admin users to the users table if not already present.
    """
    try:
        Log.info("🚀 Adding default admin users...")

        for user in DEFAULT_USERS_RAW:
            hashed_pwd = hash_password(user["password"])
            email = config.ADMIN_EMAILS[user["email_index"]]

            sql = """
                INSERT OR IGNORE INTO users (
                    user_uuid, username, role, email, password, is_active, created_at, updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """

            params = (
                user["user_uuid"],
                user["username"],
                user["role"],
                email,
                hashed_pwd,
                int(user["is_active"]),  # SQLite uses 0/1
                user["created_at"],
                user["updated_at"]
            )

            await conn.execute(sql, params)
            Log.info(f"✅ Added default user: {user['username']}")

        Log.info("🎉 Default admin users added successfully.")

    except Exception as e:
        Log.error(f"❌ Failed to add default users: {e}")
        raise
