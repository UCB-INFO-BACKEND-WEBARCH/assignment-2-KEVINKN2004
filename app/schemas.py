import re
from marshmallow import Schema, fields, validate, validates, ValidationError
from app.models import Category

HEX_COLOR_PATTERN = re.compile(r"^#[0-9A-Fa-f]{6}$")

class TaskSchema(Schema):
    title = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100)
    )

    description = fields.String(
        required=False,
        allow_none=True,
        validate=validate.Length(max=500)
    )

    completed = fields.Boolean(required=False)
    due_date = fields.DateTime(required=False, allow_none=True)
    category_id = fields.Integer(required=False, allow_none=True)

    @validates("category_id")
    def validate_category_exists(self, value, **kwargs):
        if value is None:
            return
        if Category.query.get(value) is None:
            raise ValidationError("Category does not exist.")

class TaskUpdateSchema(Schema):
    title = fields.String(
        required=False,
        validate=validate.Length(min=1, max=100)
    )

    description = fields.String(
        required=False,
        allow_none=True,
        validate=validate.Length(max=500)
    )

    completed = fields.Boolean(required=False)
    due_date = fields.DateTime(required=False, allow_none=True)
    category_id = fields.Integer(required=False, allow_none=True)

    @validates("category_id")
    def validate_category_exists(self, value, **kwargs):
        if value is None:
            return
        if Category.query.get(value) is None:
            raise ValidationError("Category does not exist.")

class CategorySchema(Schema):
    name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=50)
    )

    color = fields.String(
        required=False,
        allow_none=True
    )

    @validates("color")
    def validate_color(self, value, **kwargs):
        if value is None:
            return
        if not HEX_COLOR_PATTERN.match(value):
            raise ValidationError("Color must be a valid hex format like #RRGGBB.")
        
    @validates("name")
    def validate_unique_name(self, value, **kwargs):
        existing = Category.query.filter_by(name=value).first()
        if existing is not None:
            raise ValidationError("Category with this name already exists.")