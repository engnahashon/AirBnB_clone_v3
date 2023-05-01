#!/usr/bin/python3
"""View to handle requests for the Cities objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage, state


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """gets all cities objects"""
    cities = storage.all('Cities')
    json_cities = []
    for city in cites.values():
        json_cities.append(state.to_dict())
    return jsonify(json_cities)

