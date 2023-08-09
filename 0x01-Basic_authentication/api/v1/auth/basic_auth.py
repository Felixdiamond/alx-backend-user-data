#!/usr/bin/env python3
""" A module that inherits from the Auth Class
"""

from .auth import Auth
import base64
from typing import Tuple

from models.user import User

class BasicAuth(Auth):
    """ The Basic Authentication Class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract the Base64 part of the Authorization
        header.

        Args:
            authorization_header (str): The value of
            the Authorization header.

         Returns:
            str: The Base64 part of the Authorization
            header, or None if it is not valid.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode a Base64 string.

        Args:
            base64_authorization_header (str): The Base64 string to decode.

        Returns:
            str: The decoded value as a UTF-8 string,
            or None if it is not valid.
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_value = base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None

        return decoded_value

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ Extract the user email and password from a Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str): The Base64 decoded
            value.

        Returns:
            Tuple[str, str]: The user email and password as a tuple, or
            (None, None) if they are not valid.
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> User:
        """ Get the User instance based on email and password.
    
        Args:
            user_email (str): The user's email address.
            user_pwd (str): The user's password.
    
        Returns:
            User: The User instance, or None if it is not
            found or the password is incorrect.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
    
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
    
        users = User.search({'email': user_email})
        if not users:
            return None
    
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
    
        return None
