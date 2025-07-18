
# app/config/__init__.py
# Init config and logging appropriately
from .settings import load_config
from .log_config import Log

config = load_config()

__all__ = [
    "config",
    "Log"
]