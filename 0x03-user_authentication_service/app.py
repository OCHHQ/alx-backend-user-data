#!/usr/bin/env python3
"""
Basic Flask app module for user authentication service.
"""
from flask import Flask, jsonify, request
from auth import Auth
from typing import Dict, Any

app = Flask(__name__)
AUTH = Auth()  # Make sure this is initialized correctly


@app.route('/', methods=['GET'])
def welcome() -> jsonify:
    """
    Root endpoint returning a JSON welcome message.
    Returns:
        flask.Response: JSON response {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> Any:
    """
    Register a new user or handle already registered users.
    Request Body:
        - email: User's email address
        - password: User's password
    Responses:
        - 200 OK: {"email": "<email>", "message": "user created"}
        - 400 Bad Request: {"message": "email already registered"}
    """
    email = request.form.get('email')  # Get 'email' from the form data
    password = request.form.get('password')
    # Ensure email and password are provided
    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400
    try:
        # Attempt to register the user
        new_user = AUTH.register_user(email, password)
        return jsonify({
            "email": new_user.email,
            "message": "user created"
        }), 200
    except ValueError:
        # Handle case where email is already registered
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    """
    Main entry point of the application.
    Only executes if the script is run directly (not imported as a module).
    """
    app.run(host="0.0.0.0", port=5000)
