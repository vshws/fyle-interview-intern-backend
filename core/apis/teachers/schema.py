from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from core.models.teachers import Teacher, TeacherRoleEnum  # Assuming you have a model called Teacher with roles
from core.libs.helpers import GeneralObject

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE  # Ignore unknown fields during deserialization

    id = auto_field(required=False, allow_none=True)
    name = auto_field(required=True)  # Assuming the Teacher model has a 'name' field
    email = auto_field(required=True)  # Assuming the Teacher model has an 'email' field
    role = fields.String(required=True)  # Assuming role is a string or you can use EnumField if it's an Enum
    created_at = auto_field(dump_only=True)  # Assume created_at is auto-generated
    updated_at = auto_field(dump_only=True)  # Assume updated_at is auto-generated

    @post_load
    def initiate_class(self, data_dict, many, partial):
        return Teacher(**data_dict)  # Create an instance of Teacher with the data

# If you have specific schemas for updating or creating teachers, you can add them here
class TeacherCreateSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    role = fields.String(required=True)  # Or EnumField if it's an enumeration

    @post_load
    def initiate_class(self, data_dict, many, partial):
        return GeneralObject(**data_dict)  # Use GeneralObject or however you want to handle creation

class TeacherUpdateSchema(Schema):
    name = fields.String()
    email = fields.Email()
    role = fields.String()  # Optional fields for update

    @post_load
    def initiate_class(self, data_dict, many, partial):
        return GeneralObject(**data_dict)  # Use GeneralObject or however you want to handle updates
