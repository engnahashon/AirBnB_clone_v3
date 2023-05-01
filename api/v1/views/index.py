#!/usr/bin/python3
"""index file"""
from api.v1.views import app_views
from flask import jsonify
import models


@app_views.route('/status', methods=['GET'])
def get_status():
    """ returns api status """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ returns number of each object by type """
    from models import storage

    model_names = dir(models)
    count_dict = {}
    for name in model_names:
        model = getattr(models, name)
        if hasattr(model, "__tablename__"):
            count_dict[name] = storage.count(model)

    return jsonify(count_dict)
