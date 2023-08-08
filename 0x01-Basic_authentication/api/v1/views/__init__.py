#!/usr/bin/env python3
"""This module sets up the Flask blueprint for the API views.

It imports the necessary modules and creates a Flask blueprint with the name `app_views` and the URL prefix `/api/v1`. It also imports the necessary view functions from the `index` and `users` modules and calls the `load_from_file` method of the `User` class.
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *

User.load_from_file()

