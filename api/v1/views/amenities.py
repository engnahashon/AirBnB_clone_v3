#!/usr/bin/python3
"""View to handle requests for the Amenity objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage, state


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """gets all amenity objects"""
    amenities = storage.all('Amenity')
    json_amenities = []
    for amenity in amenities.values():
        json_amenities.append(state.to_dict())
    return jsonify(json_amenities)

