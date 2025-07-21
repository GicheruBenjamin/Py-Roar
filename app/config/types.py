
# app/config/types.py

from dataclasses import dataclass

ENV_FILE: str = ".env"

@dataclass
class Configtype:
    DATABASE_URL: str
    REST_SERVER_PORT: int
    SOCKET_SERVER_PORT: int  
    ADMIN_ONE_EMAIL: str
    ADMIN_ONE_PASSWORD: str
    ADMIN_TWO_EMAIL: str
    ADMIN_TWO_PASSWORD: str
    REGULAR_HOST: str

# Format: {ENV_VAR_NAME: expected type or required pattern}
EXPECTED_ENV_VARS = [
    {"DATABASE_URL": "sqlite:///"},
    {"REST_SERVER_PORT": int},
    {"SOCKET_SERVER_PORT": int},
    {"ADMIN_ONE_EMAIL": "@gmail.com"},
    {"ADMIN_ONE_PASSWORD": str},
    {"ADMIN_TWO_EMAIL": "@gmail.com"},
    {"ADMIN_TWO_PASSWORD": str},
    {"REGULAR_HOST": "localhost"},
]
