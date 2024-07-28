from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import ProgrammingAssignmentService

api = Namespace('programming_assignments', description='Programming assignment operations')

assignment_model = api.model('ProgrammingAssignment', {
    'prog_assignment_id': fields.Integer(readonly=True),
    'course_id': fields.String(required=True),
    'title': fields.String(required=True),
    'description': fields.String(required=True)
})

submission_input_model = api.model('ProgrammingSubmissionInput', {
    'code': fields.String(required=True),
})

submission_output_model = api.model('ProgrammingSubmissionOutput', {
    'prog_submission_id': fields.Integer(readonly=True),
    'prog_assignment_id': fields.Integer(required=True),
    'student_id': fields.Integer(required=True),
    'code': fields.String(required=True),
    'score': fields.Float(readonly=True)
})

test_case_model = api.model('TestCase', {
    'test_case_id': fields.Integer(readonly=True),
    'prog_assignment_id': fields.Integer(required=True),
    'input_data': fields.String(required=True),
    'expected_output': fields.String(required=True)
})

@api.route('/')
class ProgrammingAssignments(Resource):
    @api.doc(security="jsonWebToken")
    @api.marshal_list_with(assignment_model)
    @jwt_required()
    def get(self):
        """Get all programming assignments"""
        assignments = ProgrammingAssignmentService.get_all_assignments()
        return assignments

@api.route('/<int:id>')
@api.param('id', 'The programming assignment identifier')
class ProgrammingAssignment(Resource):
    @api.doc(security="jsonWebToken")
    @api.marshal_with(assignment_model)
    @jwt_required()
    def get(self, id):
        """Fetch a programming assignment given its identifier"""
        assignment = ProgrammingAssignmentService.get_assignment(id)
        if assignment:
            return assignment
        api.abort(404, "Programming assignment {} doesn't exist".format(id))

@api.route('/<int:id>/submit')
@api.param('id', 'The programming assignment identifier')
class ProgrammingAssignmentSubmission(Resource):
    @api.doc(security="jsonWebToken")
    @api.expect(submission_input_model)
    @api.marshal_with(submission_output_model)
    @jwt_required()
    def post(self, id):
        """Submit a solution for a programming assignment"""
        data = api.payload
        student_id = get_jwt_identity()

        if ProgrammingAssignmentService.get_submission_by_student(assignment_id=id, student_id=student_id):
            api.abort(400, "You have already submitted a solution for this assignment")

        submission = ProgrammingAssignmentService.submit_assignment(id, student_id, data['code'])

        # usually, the submission is a marshalled object of type ProgrammingSubmission
        # but in case of an error, a dict is returned with an 'error' key explaining the error
        if type(submission) is dict and "error" in submission:
            api.abort(400, submission["error"])
        
        return submission, 201

@api.route('/grades')
class ProgrammingAssignmentGrades(Resource):
    @api.doc(security="jsonWebToken")
    @api.marshal_list_with(submission_output_model)
    @jwt_required()
    def get(self):
        """Get all the programming assignment submissions for the current user"""
        student_id = get_jwt_identity()
        submissions = ProgrammingAssignmentService.get_all_submissions_by_student(student_id)
        return submissions