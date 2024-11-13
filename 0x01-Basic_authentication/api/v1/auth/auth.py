#!/usr/bin/env python3
""" Auth module for the API
"""
from typing import List, TypeVar
from flask import request

class Auth:
    """ Auth class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns False for now
        Args:
            path (str): The current path.
            excluded_paths (List[str]): List of excluded paths.
        Returns:
            bool: Always returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to return the authorization header, which returns None for now.
        Args:
            request (Flask Request): The Flask request object.
        Returns:
            str: Always returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to return the current user, which returns None for now.
        Args:
            request (Flask Request): The Flask request object.
        Returns:
            None: Always returns None.
        """
        return None
