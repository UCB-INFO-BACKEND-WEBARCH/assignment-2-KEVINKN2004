import os
from flask import Flask, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

tasks = {}
next_id = 1

@app.get('/tasks')
def list_tasks():
    all_tasks = list(tasks.values())
    return jsonify({"tasks": all_tasks})

@app.get('/tasks/<int:task_id>')
def get_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

@app.post('/tasks')
def create_task():
    global next_id
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    if not data.get("title").strip():
        return jsonify({"error": "Title is required"}), 400
    
    task = {
        "id": next_id,
        "title": data["title"],
        "description": data.get("description"),
        "completed": False,
        "due_date": (timezone.utc).isoformat().replace('+00:00', 'Z'),
        "category_id" : data.get("category"),
        "category": data.get("id"),
        "created_at": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    }
    tasks[next_id] = task
    next_id += 1
    return jsonify(task), 201

@app.put('/tasks/<int:task_id>')
def update_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    for key, value in data.items():
        if key == "id":
            continue
        task[key] = value

    return jsonify(task), 200

@app.delete('/tasks/<int:task_id>')
def delete_task(task_id):
    task = tasks.pop(task_id, None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted"}), 200

@app.get('/categories')
def list_categories():
    all_tasks = list(categories.values())
    return jsonify({"categories": all_categories})

@app.get('/categories/<int:categories_id>')
def get_categories(categories_id):
    categories = categories.get(categories_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category), 200

@app.post('/categories')
def create_task():
    global next_id
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    if not data.get("title").strip():
        return jsonify({"error": "Title is required"}), 400
    
    category = {
        "name": data["name"],
        "color": data["color"],
    }

    task = {
        "id": next_id,
        "title": data["title"],
        "description": data.get("description"),
        "completed": False,
        "due_date": (timezone.utc).isoformat().replace('+00:00', 'Z'),
        "category_id" : data.get("category"),
        "category": data.get("id"),
        "created_at": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    }
    tasks[next_id] = task
    next_id += 1
    return jsonify(task), 201

@app.put('/categories/<int:category_id>')
def update_categories(task_id):
    category = tasks.get(task_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    for key, value in data.items():
        if key == "id":
            continue
        category[key] = value

    return jsonify(category), 200

@app.delete('/category/<int:category_id>')
def delete_category(category_id):
    category = category.pop(category_id, None)
    if not category:
        return jsonify({"error": "Cannot delete category with existing task"}), 404
    return jsonify({"message": "Category deleted"}), 200