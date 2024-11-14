#!/usr/bin/env python3
"""
BasicAuth module for the API.
"""
import base64
from api.v1.auth.auth import Auth


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
        user_email, user_password = decoded_base64_authorization_header.split(':', 1)
        return (user_email,
                user_password)
