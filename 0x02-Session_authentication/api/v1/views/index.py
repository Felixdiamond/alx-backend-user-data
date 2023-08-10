#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized/', strict_slashes=False)
def unauthorized():
    """ Endpoint that raises a 401 error.

    This endpoint uses the abort function from Flask to raise a
    401 error, which will trigger the error handler for the
    401 status code.
    """
    abort(401)


@app_views.route('/forbidden/', strict_slashes=False)
def forbidden():
    """ Endpoint that raises a 403 error.

    This endpoint uses the abort function from Flask to raise a
    403 error, which will trigger the error handler for the
    403 status code.
    """
    abort(403)
