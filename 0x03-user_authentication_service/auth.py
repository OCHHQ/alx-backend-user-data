#!/usr/bin/env python3
"""
Authentication module for password hashing
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password with a random salt using bcrypt.

    Args:
        password (str): The plaintext password to be hashed.

    Returns:
        bytes: The salted hash of the password.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    # Step 1: Generate a salt
    salt = bcrypt.gensalt()

    # Step 2: Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Step 3: Return the hashed password
    return hashed_password
