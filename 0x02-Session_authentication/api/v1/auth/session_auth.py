#!/usr/bin/env python3
""" A module that inherits from the Auth Class
"""

from .auth import Auth
from uuid import uuid4

from models.user import User


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

    def current_user(self, request=None):
        """Returns a User instance based on a cookie
        value

        Args:
            request: The Flask request object to
            retrieve the cookie from

        Returns:
            User: The User instance associated with
            the cookie value, or None if not found
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes the user session / logout

        Args:
            request: The Flask request object to
            retrieve the cookie from
    
        Returns:
            bool: True if the session was successfully
            deleted, False otherwise
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
    
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
    
        del self.user_id_by_session_id[session_id]
        return True
