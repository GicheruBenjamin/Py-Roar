# app/config/log_config.py

import logging
import os
import sys

def init_logger(name="app", level=None):
    """
    Initialize and return a logger with colorized output in development.
    Logs only to terminal (stdout), no file output.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger  

    # Determine environment
    app_env = os.getenv("APP_ENV", "dev").lower()
    is_dev = app_env == "dev"

    # Set logging level
    level = level or (logging.DEBUG if is_dev else logging.INFO)
    logger.setLevel(level)

    # Formatter: color in dev, plain in prod
    if is_dev:
        class ColorFormatter(logging.Formatter):
            COLORS = {
                'DEBUG': '\033[37m',
                'INFO': '\033[32m',
                'WARNING': '\033[33m',
                'ERROR': '\033[31m',
                'CRITICAL': '\033[41m'
            }
            RESET = '\033[0m'

            def format(self, record):
                color = self.COLORS.get(record.levelname, self.RESET)
                message = super().format(record)
                return f"{color}{message}{self.RESET}"

        formatter = ColorFormatter('%(asctime)s - %(levelname)s - %(message)s')
    else:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Console handler (stdout)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Disable propagation to avoid duplicate logs
    logger.propagate = False

    # Add a helper for clean multiline logging
    def multiline(text, level="info", prefix=""):
        """
        Log multiline text so each line gets formatted consistently.
        """
        log_method = getattr(logger, level, logger.info)
        for line in text.strip().splitlines():
            log_method(f"{prefix}{line}")

    logger.multiline = multiline

    return logger

# Initialize and expose default logger
Log = init_logger()
