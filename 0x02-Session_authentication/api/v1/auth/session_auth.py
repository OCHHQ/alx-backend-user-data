#!/usr/bin/env python3
""" Session Authentication module. """

from api.v1.auth.auth import Auth
from uuid import uuid4
from typing import Dict


class SessionAuth(Auth):
    """ SessionAuth class that inherits from Auth.
    This class is empty for now and will be expanded later.
    """

    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a sesion ID from a user_id
        Args:
            user_id: string representation of the user_id
        Return:
            None if user_id is None or not a string
            Session ID ()string otherwise
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a unique Session ID
        session_id = str(uuid4())

        # Store the mapping of session_id to user_id
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID base on a Session ID
        Args:
            session with Id: string rep of the session Id
        Returns:
            None if session0id is None or not a string
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
