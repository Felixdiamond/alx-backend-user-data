#!/usr/bin/env python3
""" Module to manage API auth
"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=request) -> str:
        """Get the value of the authorization header.

        Args:
            request (Request): The Flask request object.

        Returns:
            str: The value of the authorization header, or None if it is not present.
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

