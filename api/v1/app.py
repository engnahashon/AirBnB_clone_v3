#!/usr/bin/python3
"""First endpoint with flask"""
from flask import Flask
from os import getenv
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception=None):
    """ Closes the database again at the end of a request. """
    storage.close()

@app.errorhandler(404)
def errorhandler_404(err):
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response

if __name__ == "__main__":
    import os
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
