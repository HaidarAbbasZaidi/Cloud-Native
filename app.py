
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Learn Kubernetes", "completed": False}
]

@app.route("/")
def home():
    return jsonify({
        "message": "Cloud-Native Task Manager is running!",
        "available_endpoints": ["/health", "/tasks"]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Task title is required"}), 400

    new_task = {
        "id": max((task["id"] for task in tasks), default=0) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
