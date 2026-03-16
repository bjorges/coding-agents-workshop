"""Main Flask application for TaskAPI."""

from flask import Flask, request, jsonify
from database import db
import config

app = Flask(__name__)
app.config["DEBUG"] = config.DEBUG


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Get all tasks."""
    tasks = db.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])


@app.route("/tasks", methods=["POST"])
def create_task():
    """Create a new task."""
    data = request.get_json()

    # TODO: Add input validation
    # TODO: Add error handling
    task = db.create_task(
        title=data.get("title"),
        description=data.get("description", ""),
        due_date=data.get("due_date"),
    )

    return jsonify(task.to_dict()), 201


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Get a specific task."""
    task = db.get_task(task_id)

    if not task:
        # TODO: Return proper 404 error
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task.to_dict())


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Update a task."""
    task = db.get_task(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    # TODO: Add input validation
    updated = db.update_task(task_id, **data)

    return jsonify(updated.to_dict())


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task."""
    success = db.delete_task(task_id)

    if not success:
        return jsonify({"error": "Task not found"}), 404

    return "", 204


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
