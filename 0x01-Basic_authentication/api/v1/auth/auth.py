#!/usr/bin/env python3
""" Module to manage API auth
"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """ The Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list
            of paths that do not require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize the path and excluded_paths to ensure they are slash
        # tolerant
        path = path.rstrip('/')
        excluded_paths = [p.rstrip('/') for p in excluded_paths]

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=request) -> str:
        """Get the value of the authorization header.

        Args:
            request (Request): The Flask request object.

        Returns:
            str: The value of the authorization header,
            or None if it is not present.
        """
        return None

    def current_user(self, request=request) -> User:
        """Get the current user.

        Args:
            request (Request): The Flask request object.

        Returns:
            User: The current user, or None if there is no current user.
        """
        return None
