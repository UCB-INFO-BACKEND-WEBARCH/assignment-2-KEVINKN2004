from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app import db, task_queue
from app.models import Task, Category
from app.schemas import TaskSchema, TaskUpdateSchema
from datetime import datetime, timezone, timedelta
from app.jobs import due_date_notif

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
    schema = TaskSchema()
    try:
        data = schema.load(request.get_json() or {})
    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    task = Task(
        title=data.get("title"),
        description=data.get("description"),
        due_date=data.get("due_date"),
        category_id=data.get("category_id")
    )

    db.session.add(task)
    db.session.commit()

    notification_queued = False
    if task.due_date is not None:
        now = datetime.now(timezone.utc)
        due = task.due_date if task.due_date.tzinfo else task.due_date.replace(tzinfo=timezone.utc)
        if now < due <= now + timedelta(hours=24):
            task_queue.enqueue(due_date_notif, task.title)
            notification_queued = True

    return jsonify({"task": dict_task(task), "notification_queued": notification_queued}), 201

@tasks_bp.put("/tasks/<int:task_id>")
def update_task(task_id):
    task = db.session.get(Task, task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    schema = TaskUpdateSchema()
    try:
        data = schema.load(request.get_json() or {})
    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    for field in ("title", "description", "completed", "due_date", "category_id"):
        if field in data:
            setattr(task, field, data[field])
    
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