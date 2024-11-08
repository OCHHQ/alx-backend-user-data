#!/usr/bin/env python3
"""
Module for hashing and validating passwords using the bcrypt library.
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate that the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
