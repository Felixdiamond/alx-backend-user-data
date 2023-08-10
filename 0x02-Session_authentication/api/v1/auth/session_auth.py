#!/usr/bin/env python3
""" A module that inherits from the Auth Class
"""

from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ The Session Authentication Class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID

        Args:
            session_id (str): The Session ID for which
            to retrieve the User ID

        Returns:
            str: The User ID associated with the given
            Session ID, or None if the Session ID is invalid
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
