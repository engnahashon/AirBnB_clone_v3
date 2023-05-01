#!/usr/bin/python3
"""View to handle requests for the State objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage, State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """gets all state objects"""
    states = storage.all('State')
    json_states = []
    for state in states.values():
        json_states.append(state.to_dict())
	return jsonify(json_states)
