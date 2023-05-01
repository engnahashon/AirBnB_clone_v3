#!/usr/bin/python3
"""View to handle requests for the Place objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage, state


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """gets all place objects"""
    places = storage.all('Place')
    json_places = []
    for place in places.values():
        json_places.append(place.to_dict())
    return jsonify(json_places)

