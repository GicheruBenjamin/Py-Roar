
# app/config/settings.py
import os
import re
from dataclasses import dataclass
from typing import Optional
from pathlib import Path
from .log_config import Log

# === ENV FILE PATH ===
ENV_PATH = ".env"

# === Basic email regex ===
EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

@dataclass
class Config:
    DATABASE_URL: str
    ADMIN_ONE_EMAIL: str
    ADMIN_ONE_PASSWORD: str
    ADMIN_TWO_EMAIL: str
    ADMIN_TWO_PASSWORD: str


def load_env_file(filepath: str = ENV_PATH) -> None:
    """
    Load .env file into os.environ if not already set.
    Ignores blank lines and comments.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"⚠️ .env file not found at: {filepath}")

    with path.open() as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            cleaned = value.strip().strip('"').strip("'")
            os.environ.setdefault(key.strip(), cleaned)


def validate_email(email: str, var_name: str) -> None:
    """
    Validate email format.
    """
    if not EMAIL_REGEX.match(email):
        raise ValueError(f"❌ Invalid email format in {var_name}: '{email}'")


def load_config() -> Config:
    """
    Load config from environment variables, validate, and return Config instance.
    Raises errors if required values are missing or invalid.
    """
    try:
        load_env_file()
    except Exception as e:
        Log.error(f"⚠️ Skipped .env loading: {e}")

    required_vars = [
        "DATABASE_URL",
        "ADMIN_ONE_EMAIL",
        "ADMIN_ONE_PASSWORD",
        "ADMIN_TWO_EMAIL",
        "ADMIN_TWO_PASSWORD"
    ]

    missing = [var for var in required_vars if var not in os.environ]
    if missing:
        raise EnvironmentError(f"❌ Missing required env vars: {missing}")

    # Validate emails
    validate_email(os.environ["ADMIN_ONE_EMAIL"], "ADMIN_ONE_EMAIL")
    validate_email(os.environ["ADMIN_TWO_EMAIL"], "ADMIN_TWO_EMAIL")

    return Config(
        DATABASE_URL=os.environ["DATABASE_URL"],
        ADMIN_ONE_EMAIL=os.environ["ADMIN_ONE_EMAIL"],
        ADMIN_ONE_PASSWORD=os.environ["ADMIN_ONE_PASSWORD"],
        ADMIN_TWO_EMAIL=os.environ["ADMIN_TWO_EMAIL"],
        ADMIN_TWO_PASSWORD=os.environ["ADMIN_TWO_PASSWORD"]
    )
