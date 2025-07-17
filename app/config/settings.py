# app/config.py
import os
import re
from dataclasses import dataclass
from typing import List, Optional
from pathlib import Path

# Define expected env vars
EXPECTED_ENV_VARS = [
    "DATABASE_URL",
    "ADMIN_"
]

@dataclass
class Config:
    DATABASE_URL: str
    ADMIN_EMAILS: List[str]


def parse_admin_emails(raw: str) -> List[str]:
    """
    Parses a comma-separated list of emails and validates basic format.
    """
    emails = [email.strip().strip('"').strip("'") for email in raw.split(",")]
    # Optional: validate emails with a simple regex
    email_pattern = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
    for email in emails:
        if not email_pattern.match(email):
            raise ValueError(f"Invalid email format: {email}")
    return emails


def load_env_file(filepath: str = ".env") -> None:
    """
    Manually loads .env file into os.environ
    """
    env_path = Path(filepath)
    if not env_path.exists():
        raise FileNotFoundError(f".env file not found at {filepath}")
    
    with env_path.open() as f:
        for line in f:
            # Ignore comments and empty lines
            if line.strip() == "" or line.strip().startswith("#"):
                continue
            # Parse key=value
            if '=' in line:
                key, value = line.strip().split("=", 1)
                # Remove surrounding quotes if any
                cleaned_value = value.strip().strip('"').strip("'")
                os.environ.setdefault(key, cleaned_value)


def load_config() -> Optional[Config]:
    """
    Load and validate config from environment variables.
    Returns Config instance or raises error if missing / invalid.
    """
    # Step 1: Load .env first (if present)
    try:
        load_env_file()
    except Exception as e:
        print(f"Warning: failed to load .env file: {e}")

    # Step 2: Check required vars
    missing_vars = [var for var in EXPECTED_ENV_VARS if var not in os.environ]
    if missing_vars:
        raise EnvironmentError(f"Missing required env vars: {missing_vars}")

    # Step 3: Parse and validate values
    database_url = os.environ["DATABASE_URL"]
    raw_admin_emails = os.environ["ADMIN_EMAILS"]
    admin_emails = parse_admin_emails(raw_admin_emails)

    # Step 4: Return config object
    return Config(
        DATABASE_URL=database_url,
        ADMIN_EMAILS=admin_emails
    )
