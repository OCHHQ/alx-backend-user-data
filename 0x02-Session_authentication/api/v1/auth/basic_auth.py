#!/usr/bin/env python3
"""
BasicAuth module for the API.
"""
import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    Basic authentication class that inherits from Auth.
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization header
        for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header value

        Returns:
            str: The Base64 part of the Authorization header
                 None if authorization_header is None
                 None if authorization_header is not a string
                 None if authorization_header doesn't start by 'Basic '
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        # Return the part after 'Basic '
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes a Base64 string.

        Args:
            base64_authorization_header (str): The Base64 string to decode

        Returns:
            str: The decoded string as UTF-8, or None if decoding fails
        """
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None

        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # Convert bytes to UTF-8 string
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts user email and password from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str):
            The decoded Base64 string

        Returns:
            tuple: (user_email, user_password)
               None, None if any checks fail
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str)):
            return None, None

        # Check if there is a colon ':' in the string
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string into email and password using the colon
        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.

        Args:
            user_email (str): The user's email address.
            user_pwd (str): The user's password.

        Returns:
            User: The User instance if credentials are valid, None otherwise.
        """
        # Validate input types
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for the user by email using the `search` class method
        user_list = User.search({'email': user_email})
        if not user_list or len(user_list) == 0:
            return None

        user = user_list[0]  # Assume the first match is the user we want

        # Check if the password is valid
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request.

        Args:
            request: The HTTP request object.

        Returns:
            User: The User instance if found, None otherwise.
        """
        # Get the Authorization header from the request
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        # Extract the Base64 part from the header
        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        # Decode the Base64 string
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None

        # Extract the user credentials (email and password)
        user_email, user_pwd = self.extract_user_credentials(decoded_auth)
        if user_email is None or user_pwd is None:
            return None

        # Retrieve the User instance using the email and password
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
