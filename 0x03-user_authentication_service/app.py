#!/usr/bin/env python3
"""
Basic Flask app module for user authentication service.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome() -> jsonify:
    """
    Root endpoint returning a JSON welcome message.

    Returns:
        flask.Response: JSON response {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
