#!/usr/bin/env python3
"""
Module for hashing passwords using the bcrypt library.
"""
import bcrypt
from typing import str, bytes


def hash_password(password: str) -> bytes:
    """
    Hash a password with a salt and return the hashed password.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The hashed password.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
