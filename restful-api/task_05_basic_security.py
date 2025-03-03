#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
application = Flask(__name__)
basic_auth = HTTPBasicAuth()

# Configuration for JWT
application.config['JWT_SECRET_KEY'] = 'your-ultra-secure-key-here'
jwt_manager = JWTManager(application)

# Mock user database
user_data = {
    "alice": {
        "username": "alice",
        "password": generate_password_hash("alicepass"),
        "role": "user"
    },
    "bob": {
        "username": "bob",
        "password": generate_password_hash("bobpass"),
        "role": "admin"
    }
}

# Basic authentication handler
@basic_auth.verify_password
def validate_user_credentials(username, password):
    user = user_data.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

# Home route
@application.route('/')
def home_page():
    return "Welcome to the Secure API!"

# Basic authentication protected route
@application.route('/protected-basic')
@basic_auth.login_required
def basic_auth_route():
    return "Basic Authentication: You're in!"

# JWT authentication route
@application.route('/get-token', methods=['POST'])
def generate_token():
    credentials = request.json
    username = credentials.get('username')
    password = credentials.get('password')

    user = user_data.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401

    token_data = {
        "username": username,
        "role": user["role"]
    }
    token = create_access_token(identity=token_data)
    return jsonify({"access_token": token})

# JWT protected route
@application.route('/protected-jwt')
@jwt_required()
def jwt_protected_route():
    return "JWT Authentication: Access granted!"

# Admin-only route
@application.route('/admin-area')
@jwt_required()
def admin_only_route():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin privileges required"}), 403
    return "Admin Area: Welcome, admin!"

# JWT error handlers
@jwt_manager.unauthorized_loader
def handle_missing_or_invalid_token(error):
    return jsonify({"error": "Token is missing or invalid"}), 401

@jwt_manager.invalid_token_loader
def handle_invalid_jwt_token(error):
    return jsonify({"error": "Invalid JWT token"}), 401

@jwt_manager.expired_token_loader
def handle_expired_jwt_token(error):
    return jsonify({"error": "JWT token has expired"}), 401

# Run the application
if __name__ == '__main__':
    application.run(debug=True)