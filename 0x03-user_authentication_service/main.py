#!/usr/bin/env python3
""" The Main Module
"""

import requests

BASE_URL = "http://localhost:5000"

def register_user(email: str, password: str) -> None:
    """Register a user"""
    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/users", data=data)
    assert response.status_code == 200

def log_in_wrong_password(email: str, password: str) -> None:
    """Log in with wrong password"""
    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/sessions", data=data)
    assert response.status_code == 401

def log_in(email: str, password: str) -> str:
    """Log in"""
    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/sessions", data=data)
    assert response.status_code == 200
    session_id = response.cookies.get("session_id")
    return session_id

def profile_unlogged() -> None:
    """Get profile without being logged in"""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403

def profile_logged(session_id: str) -> None:
    """Get profile while being logged in"""
    cookies = {"session_id": session_id}
    response = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    assert response.status_code == 200

def log_out(session_id: str) -> None:
    """Log out"""
    cookies = {"session_id": session_id}
    response = requests.delete(f"{BASE_URL}/sessions", cookies=cookies)
    assert response.status_code == 200

def reset_password_token(email: str) -> str:
    """Get reset password token"""
    data = {"email": email}
    response = requests.post(f"{BASE_URL}/reset_password", data=data)
    assert response.status_code == 200
    reset_token = response.json().get("reset_token")
    return reset_token

def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update password"""
    data = {"email": email, "reset_token": reset_token, "new_password": new_password}
    response = requests.put(f"{BASE_URL}/reset_password", data=data)
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)

