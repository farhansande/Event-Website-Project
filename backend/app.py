from flask import Flask, jsonify, request
import SQLConnection
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # Enable CORS for React

# ---------------- USERS ----------------

@app.route("/users", methods=["GET"])
def list_users():
    users = SQLConnection.getAllUsers()
    return jsonify(users)

@app.route("/users/<int:id>", methods=["GET"])
def list_user(id):
    user = SQLConnection.getUser(id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(force=True)
    username = data.get("username")
    password = data.get("password")

    result = SQLConnection.insert_user(username, password)
    return jsonify({"message": result or "User created"})

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    rows_deleted = SQLConnection.remove_user(id)
    if rows_deleted == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"})

@app.route("/users/<int:id>", methods=["PUT"])
def modify_user(id):
    data = request.get_json(force=True)
    username = data.get("username")
    password = data.get("password")

    SQLConnection.update_user(id, username, password)
    return jsonify({"message": "User updated"})

# ---------------- EVENTS ----------------

@app.route("/events", methods=["GET"])
def list_events():
    events = SQLConnection.getAllEvents()
    return jsonify(events)

@app.route("/events/<int:id>", methods=["GET"])
def list_event(id):
    event = SQLConnection.getEvent(id)
    if event is None:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(event)

@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json(force=True)
    name = data.get("name")
    time = data.get("time")
    location = data.get("location")
    description = data.get("description")

    result = SQLConnection.insert_event(name, time, location, description)
    return jsonify({"message": result or "Event created"})

@app.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):
    rows_deleted = SQLConnection.delete_event(id)
    if rows_deleted == 0:
        return jsonify({"error": "Event not found"}), 404
    return jsonify({"message": "Event deleted"})

@app.route("/events/<int:id>", methods=["PUT"])
def modify_event(id):
    data = request.get_json(force=True)
    name = data.get("name")
    time = data.get("time")
    location = data.get("location")
    description = data.get("description")

    SQLConnection.update_event(id, name, time, location, description)
    return jsonify({"message": "Event updated"})

if __name__ == "__main__":
    app.run(debug=True)
