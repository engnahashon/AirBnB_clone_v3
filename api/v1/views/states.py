#!/usr/bin/python3
"""View to handle requests for the State objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage, state


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """gets all state objects"""
    states = storage.all('State')
    json_states = []
    for state in states.values():
        json_states.append(state.to_dict())
    return jsonify(json_states)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object: GET /api/v1/states/<state_id>"""
    state = storage.get('State', state_id)
    if state:
        return jsonify(state.to_dict())
    abort(404)

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({})
