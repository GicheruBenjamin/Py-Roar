# app/log_config.py
import logging
from dataclasses import dataclass

# Define color codes (ANSI escape codes)
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
COLOR_BLUE = "\033[34m"
COLOR_MAGENTA = "\033[35m"
COLOR_CYAN = "\033[36m"
COLOR_WHITE = "\033[37m"

# Map log levels to colors
LEVEL_COLORS = {
    'DEBUG': COLOR_CYAN,
    'INFO': COLOR_GREEN,
    'WARNING': COLOR_YELLOW,
    'ERROR': COLOR_RED,
    'CRITICAL': COLOR_MAGENTA
}

class ColorFormatter(logging.Formatter):
    """
    Custom formatter that adds color based on log level.
    """
    def format(self, record):
        log_color = LEVEL_COLORS.get(record.levelname, COLOR_WHITE)
        record.levelname = f"{log_color}{record.levelname}{COLOR_RESET}"
        record.msg = f"{log_color}{record.msg}{COLOR_RESET}"
        return super().format(record)


@dataclass
class Log:
    """
    Central log config.
    Allows: Log.info(), Log.error(), Log.debug(), Log.warning(), Log.critical()
    """
    info: callable
    error: callable
    debug: callable
    warning: callable
    critical: callable


def LogConfig() -> Log:
    """
    Set up logger with colors: formatter, level, handlers.
    Returns Log dataclass with logging methods.
    """
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = ColorFormatter(
            '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        ch.setFormatter(formatter)

        logger.addHandler(ch)

    return Log(
        info=logger.info,
        error=logger.error,
        debug=logger.debug,
        warning=logger.warning,
        critical=logger.critical
    )
