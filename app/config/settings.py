
# app/config/settings.py

import os
import re
from pathlib import Path
from typing import Any

from .types import Configtype, ENV_FILE, EXPECTED_ENV_VARS
from .log_config import Log  


def load_dotenv(env_path: Path = Path(ENV_FILE)) -> None:
    """
    Loads environment variables from a .env file if not already set.
    """
    if not env_path.exists():
        Log.warning(f"⚠️ .env file not found at: {env_path}")
        return

    with env_path.open("r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            match = re.match(r"^(\w+)=([^\n\r]*)$", line)
            if match:
                key, value = match.groups()
                os.environ.setdefault(key, value)
                Log.debug(f"Loaded {key} from .env")


def parse_value(key: str, expected: Any) -> Any:
    raw = os.getenv(key)
    if raw is None:
        raise ValueError(f"Missing required environment variable: {key}")

    if expected is int:
        try:
            return int(raw)
        except ValueError:
            raise ValueError(f"Invalid type for {key}: expected int, got {raw}")

    elif isinstance(expected, str) and expected.startswith("@"):
        if expected in raw:
            return raw
        raise ValueError(f"Invalid value for {key}: expected email containing '{expected}'")

    elif isinstance(expected, str):
        if expected in raw:
            return raw
        raise ValueError(f"Invalid value for {key}: expected to contain '{expected}'")

    elif expected is str:
        return raw

    raise TypeError(f"Unknown expected type for {key}")


def validate_env() -> None:
    errors = []
    for rule in EXPECTED_ENV_VARS:
        for key, expected in rule.items():
            try:
                _ = parse_value(key, expected)
                Log.debug(f"✅ {key} validated")
            except Exception as e:
                Log.error(f"❌ {key}: {e}")
                errors.append(f"{key}: {e}")

    if errors:
        raise RuntimeError(f"Environment validation failed:\n" + "\n".join(errors))


def get_config() -> Configtype:
    load_dotenv()
    validate_env()

    config = Configtype(
        DATABASE_URL=os.environ["DATABASE_URL"],
        REST_SERVER_PORT=int(os.environ["REST_SERVER_PORT"]),
        SOCKET_SERVER_PORT=int(os.environ["SOCKET_SERVER_PORT"]),
        ADMIN_ONE_EMAIL=os.environ["ADMIN_ONE_EMAIL"],
        ADMIN_ONE_PASSWORD=os.environ["ADMIN_ONE_PASSWORD"],
        ADMIN_TWO_EMAIL=os.environ["ADMIN_TWO_EMAIL"],
        ADMIN_TWO_PASSWORD=os.environ["ADMIN_TWO_PASSWORD"],
        REGULAR_HOST=os.environ["REGULAR_HOST"],
    )

    Log.info("✅ Configuration loaded successfully")
    return config


CONFIG = get_config()
