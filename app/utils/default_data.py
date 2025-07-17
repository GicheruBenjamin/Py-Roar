
from app.config import config
from .hash_password import hash_password
import uuid
from datetime import datetime   

# Default users in the system
_default_users = [
    {
        "id": 1,
        "user_uuid": str(uuid.uuid4()),
        "username": "admin",
        "role": "admin",
        "email": config.ADMIN_ONE_EMAIL,
        "password": hash_password(config.ADMIN_ONE_PASSWORD),
        "is_active": True,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    },
    {
        "id": 2,
        "user_uuid": str(uuid.uuid4()),
        "username": "user",
        "role": "user",
        "email": config.ADMIN_TWO_EMAIL,
        "password": hash_password(config.ADMIN_TWO_PASSWORD),
        "is_active": True,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
]
