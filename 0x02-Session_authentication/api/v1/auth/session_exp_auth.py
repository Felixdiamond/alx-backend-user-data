#!/usr/bin/env python3
"""SessionExpAuth module"""

from .auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""

    def __init__(self):
        """Constructor method"""
        super().__init__()
        self.session_duration = int(getenv('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """Create a session ID for a user ID"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Get the user ID for a session ID"""
        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id:
            return None

        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]['user_id']

        if 'created_at' not in self.user_id_by_session_id[session_id]:
            return None

        created_at = self.user_id_by_session_id[session_id]['created_at']
        if (created_at + timedelta(
            seconds=self.session_duration
        )) < datetime.now():
            return None

        return self.user_id_by_session_id[session_id]['user_id']
