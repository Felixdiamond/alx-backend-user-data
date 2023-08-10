#!/usr/bin/env python3
""" A module that inherits from the Auth Class
"""

from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ The Session Authentication Class
    """
    user_id_by_session_id = {}

    def def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a given user ID

        Args:
            user_id (str): The user ID for which to create
            a session ID

        Returns:
            str: The created session ID, or None if the
            user ID is invalid
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
