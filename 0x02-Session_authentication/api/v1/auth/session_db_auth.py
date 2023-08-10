#!/usr/bin/env python3
"""SessionDBAuth module"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""

    def create_session(self, user_id=None):
        """Create a session ID for a user ID"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Get the user ID for a session ID"""
        if session_id is None:
            return None

        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return None

        user_session = user_sessions[0]
        return super().user_id_for_session_id(user_session.session_id)

    def destroy_session(self, request=None):
        """Destroy the user session / logout"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        if not super().destroy_session(request):
            return False

        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return False

        for user_session in user_sessions:
            user_session.remove()

        return True
