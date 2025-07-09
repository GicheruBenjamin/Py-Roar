
# app/config/__init__.py
# Init config and logging appropriately
from .settings import load_config
from .log_config import LogConfig

config = load_config()
Log = LogConfig()

__all__ = [
    "config",
    "log"
]