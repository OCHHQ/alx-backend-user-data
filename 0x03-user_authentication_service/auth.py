#!/usr/bin/env python3
"""
Authentication module for password hashing
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


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


class Auth:
    """A  Class to interact with the authentication database"""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with an email and a password.

        Args:
            email (str): the email address of New user
            password (str): the password for New user

        Returns:
            User: The newly created User object

        Raises:
            ValueError: if a user with provided email already exists
        """
        try:
            self._db.find_user_by(email=email)
            # here is point where exception is raised when user exist
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password = _hash_password(password)

        new_user = self._db.add_user(
                email=email,
                hashed_password=hashed_password
        )

        # litrally return User Object
        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate a user's login credentials.

        Args:
            email (str): User's email.
            password (str): User's password.

        Returns:
            bool: True if credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(
                    password.encode('utf-8'),
                    user.hashed_password):
                return True
        except Exception:
            pass
        return False

    def _generate_uuid() -> str:
        """
        Generate a new UUID and return its string representation.

        Returns:
            str: A string representation of a new UUID.
        """
        return str(uuid.uuid4())
