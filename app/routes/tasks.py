from flask import Blueprint, jsonify, request
from app import db
from app.models import Task, Category
from datetime import datetime

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.get("/tasks")
def tasks_list():
    query = Task.query

    completed_parameter = request.args.get("completed")
    if completed_parameter is not None:
        if completed_parameter.lower() == "true":
            query = query.filter_by(completed=True)
        elif completed_parameter.lower() == "false":
            query = query.filter_by(completed=False)

    tasks = query.all()
    return jsonify({"tasks": [dict_task(t) for t in tasks]}), 200

def dict_task(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "due_date": task.due_date.isoformat() if task.due_date else None,
        "category_id": task.category_id,
        "category": dict_category(task.category) if task.category else None,
        "created_at": task.created_at.isoformat() if task.created_at else None,
        "updated_at": task.updated_at.isoformat() if task.updated_at else None
    }

def dict_category(category):
    return {
        "id": category.id,
        "name": category.name,
        "color": category.color
    }

@tasks_bp.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = db.session.get(Task, task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(dict_task(task)), 200

@tasks_bp.post("/tasks")
def create_task():
    data = request.get_json()
    due_date = None
    if data.get("due_date"):
        due_date = datetime.fromisoformat(data["due_date"].replace("Z", "+00:00"))

    task = Task(
        title=data.get("title"),
        description=data.get("description"),
        due_date=due_date,
        category_id=data.get("category_id")
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"task": dict_task(task), "notification_queued": False}), 201

@tasks_bp.put("/tasks/<int:task_id>")
def update_task(task_id):
    task = db.session.get(Task, task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()

    if "title" in data:
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"]
    if "completed" in data:
        task.completed = data["completed"]
    if "category_id" in data:
        task.category_id = data["category_id"]
    if "due_date" in data:
        if data["due_date"]:
            task.due_date = datetime.fromisoformat(data["due_date"].replace("Z", "+00:00"))
        else:
            task.due_date = None
    
    db.session.commit()
    return jsonify(dict_task(task)), 200

@tasks_bp.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200