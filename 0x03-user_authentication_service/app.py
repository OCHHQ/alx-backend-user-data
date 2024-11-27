#!/usr/bin/env python3
"""
Basic Flask app module for user authentication service.
"""
from flask import Flask, jsonify, request, abort, make_response
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

    if not email or not password:
        abort(401)
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


@app.route('/sessions', methods=['POST'])
def login():
    """
    Handle user login via POST request.

    Form Data:
        email: User's email
        password: User's password

    Returns:
        JSON response with user email and login message,
        sets session_id cookie on successful login
    """
    # Get email and password from form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Validate login credentials
    if not AUTH.valid_login(email, password):
        # If credentials are invalid, abort with 401 Unauthorized
        abort(401)

    # Generate session ID for the user
    session_id = AUTH.create_session(email)

    # Create response with login confirmation
    response = make_response(jsonify({
        "email": email,
        "message": "logged in"
    }))

    # Set session_id as a cookie
    response.set_cookie('session_id', session_id)

    return response


if __name__ == "__main__":
    """
    Main entry point of the application.
    Only executes if the script is run directly (not imported as a module).
    """
    app.run(host="0.0.0.0", port=5000)
