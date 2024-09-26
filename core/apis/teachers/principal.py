from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from core.apis.teachers.schema import TeacherSchema

# Create a Blueprint for principal teachers resources
principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns a list of all teachers."""
    try:
        all_teachers = Teacher.get_all()  # Assuming this method retrieves all teachers
        all_teachers_dump = TeacherSchema().dump(all_teachers, many=True)
        return APIResponse.respond(data=all_teachers_dump), 200  # Explicitly set status code
    except Exception as e:
        # Log the error (consider using a logging framework)
        # logger.error(f"Error fetching teachers: {str(e)}")  # Uncomment and use a logger as appropriate
        return APIResponse.respond(error="Failed to fetch teachers.", message=str(e)), 500  # Return a 500 error with a message
