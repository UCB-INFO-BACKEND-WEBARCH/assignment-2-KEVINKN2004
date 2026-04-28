from flask import Blueprint, jsonify, request
from app import db
from app.models import Task, Category
from datetime import datetime
from app.schemas import CategorySchema
from marshmallow import ValidationError

categories_bp = Blueprint("categories", __name__)

def dict_category_task_count(category):
    return {
        "id": category.id,
        "name": category.name,
        "color": category.color,
        "task_count": len(category.tasks)
    }

def dict_simple_task(task):
    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }

@categories_bp.get("/categories")
def categories_list():
    categories = Category.query.all()
    return jsonify({"categories": [dict_category_task_count(c) for c in categories]}), 200

@categories_bp.get("/categories/<int:category_id>")
def get_category(category_id):
    category = db.session.get(Category, category_id)
    if category is None:
        return jsonify({"error": "Category not found"}), 404
    return jsonify({
        "id": category.id,
        "name": category.name,
        "color": category.color,
        "tasks": [dict_simple_task(t) for t in category.tasks]
    }), 200

@categories_bp.post("/categories")
def create_category():
    schema = CategorySchema()
    try:
        data = schema.load(request.get_json() or {})
    except ValidationError as error:
        return jsonify({"errors": error.messages}), 400

    category = Category(
        name=data.get("name"),
        color=data.get("color")
    )

    db.session.add(category)
    db.session.commit()

    return jsonify({
        "id": category.id,
        "name": category.name,
        "color": category.color
    }), 201

@categories_bp.delete("/categories/<int:category_id>")
def delete_category(category_id):
    category = db.session.get(Category, category_id)
    if category is None:
        return jsonify({"error": "Category not found"}), 404
    
    if len(category.tasks) > 0:
        return jsonify({
            "error": "Cannot delete category with existing tasks. Move or delete tasks first."
        }), 400

    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted"}), 200