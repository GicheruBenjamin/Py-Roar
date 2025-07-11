# app/utils/hash_password.py

"""
This is the hash_password file
Used to hash passwords securely with salt (stdlib only)
"""

import hashlib
import os
from typing import Optional

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256 + random salt.
    Returns salt+hash as hex string: 'salt$hash'
    """
    salt = os.urandom(16)  # 16 bytes random salt
    salt_hex = salt.hex()
    pwd_bytes = password.encode('utf-8')
    hash_bytes = hashlib.sha256(salt + pwd_bytes).hexdigest()
    return f"{salt_hex}${hash_bytes}"

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifies a password against a hashed password (salt$hash format).
    """
    try:
        salt_hex, stored_hash = hashed_password.split('$')
        salt = bytes.fromhex(salt_hex)
        pwd_bytes = password.encode('utf-8')
        check_hash = hashlib.sha256(salt + pwd_bytes).hexdigest()
        return check_hash == stored_hash
    except Exception:
        return False
