#!/usr/bin/env python3
"""
Authentication module for password hashing
"""
import bcrypt
from typing import Union


def _hash_password(password: str) -> bytes:
    """
    Hashes a password with a random salt using bycrpt.

    Args:
        password (str): the password string to be hashed
    Returns:
        bytes: the salted hash of the password

    implementation details:
        1.encode the password string to bytes
        2.Generate a salt and hash the password using bcrypt
        3.The salt is automatically stored as part of the hashed password
    """
    # converting the password string to bytes
    encoded_password = password.encode(utf-8)

    # here generate salt and hashed
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)

    return _hash_password
