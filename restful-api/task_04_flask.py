#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

user = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def getData():
    user_list = list(user.keys())
    return jsonify(user_list), 200

@app.route('/status')
def getStatus():
    return "OK"

@app.route('/users/<username>')
def getUser(username):
    user = user.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def addUser():
    new_user = request.get_json()
    username = new_user.get("username")
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    user[username] = {
        "username": username,
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }

    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == "__main__":
    app.run(debug=True)