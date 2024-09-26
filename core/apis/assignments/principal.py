from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.assignments import AssignmentStateEnum, GradeEnum
from flask import request


from .schema import AssignmentSchema, AssignmentGradeSchema

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of all submitted and graded assignments"""
    all_assignments = Assignment.get_all_submitted_and_graded()
    all_assignments_dump = AssignmentSchema().dump(all_assignments, many=True)
    return APIResponse.respond(data=all_assignments_dump)


@principal_teachers_resources.route('/assignments/grade', methods=['POST'])
@decorators.authenticate_teacher  # Assuming you have an authenticate decorator
def grade_assignment():
    json_data = request.get_json()
    assignment_id = json_data.get('id')
    grade = json_data.get('grade')

    assignment = Assignment.get_by_id(assignment_id)
    if not assignment:
        return APIResponse.respond(error="Assignment not found."), 404

    if assignment.state == AssignmentStateEnum.DRAFT:
        return APIResponse.respond(error="Only submitted assignments can be graded."), 400

    # Proceed with grading
    assignment.grade = GradeEnum(grade)
    assignment.state = AssignmentStateEnum.GRADED
    db.session.commit()

    return APIResponse.respond(data={"id": assignment.id, "grade": assignment.grade.value}), 200

