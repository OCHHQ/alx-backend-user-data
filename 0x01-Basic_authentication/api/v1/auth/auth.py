#!/usr/bin/env python3
""" Auth module for the API
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if a path requires authentication
        Args:
            path (str): The current path.
            excluded_paths (List[str]): List of excluded paths.
        Returns:
            bool: True if authentication is required, False otherwise.
        """

        # Return True if path is None
        if path is None:
            return True

        # Return True if excluded_paths is None or empty
        if not excluded_paths:
            return True

        # Ensure the path has a trailing slash for comparison
        if path[-1] != '/':
            path += '/'

        # Check if the path matches any in excluded_paths
        for excluded_path in excluded_paths:
            # Ensure the excluded path also has a trailing slash for comparison
            if excluded_path[-1] != '/':
                excluded_path += '/'
            if path == excluded_path:
                return False

        # If no match is found, authentication is required
        return True

    def authorization_header(self, request=None) -> str:
        """ Method to return the authorization
            header, which returns None for now.
        Args:
            request (Flask Request): The Flask request object.
        Returns:
            str: set the value auth header or None if not present.
        """
        if request is None:
            return None
        # check if the authenicaton header is in the request
        if 'Authorization' not in request.headers:
            return None

        # Return the value of the 'Authorization' header
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to return the current user, which returns None for now.

        Args:
            request (Flask Request): The Flask request object.
        Returns:
            None: Always returns None.
        """
        return None
