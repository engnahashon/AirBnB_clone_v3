#!/usr/bin/python3
"""View to handle requests for the User objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage, state


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """gets all user objects"""
    users = storage.all('User')
    json_users = []
    for user in users.values():
        json_users.append(user.to_dict())
    return jsonify(json_users)

