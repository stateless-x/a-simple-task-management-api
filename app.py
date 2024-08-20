from flask import Flask, jsonify, request, abort
from tasks import add_task, get_tasks, update_task, get_task, delete_task

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_tasks())


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task_by_id(task_id):
    task = get_task(task_id)
    if task is None:
        abort(404)
    return jsonify(task)


@app.route("/tasks", methods=["POST"])
def create_task():
    if not request.json or not "title" in request.json:
        abort(400)
    task = add_task(
        title=request.json["title"],
        description=request.json.get("description", "") #allows description to be optional, return ""
    )
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task_by_id(task_id):
    task = get_task(task_id)
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    task = update_task(
        task_id,
        title=request.json.get("title"),
        description=request.json.get("description")
    )
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task_by_id(task_id):
    task = get_task(task_id)
    if task is None:
        abort(400)
    task = delete_task(task_id)
    return '', 204


if __name__ == "__main__":
    app.run(debug=True)