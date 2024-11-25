#!/usr/bin/env python3
"""
Baic flask app module for user authentication
This module create a simple web application using
Flask framework that serves as a foundation for
our authentication service
"""
from flask import Flask, jsonify

app = flask(__name__)


@app.route('/', methods=['GET'])
def welcome() -> jsonify:
    """
    Root endpoint welcome users to the authentication service

    Route:
        -URL:/
        _Method: GET

   Return:
    Dict[str, str]: JSON response containing welcome
    format: {"message": "Bienvenue"}

   Response Details:
    -Content-Type: application/json
    -Status Code: 200 (ok)
    -Character Encoding: UTF-8
    """
    return jsonify({"messasge": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
