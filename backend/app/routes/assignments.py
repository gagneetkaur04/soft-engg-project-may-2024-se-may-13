from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import AssignmentService, CourseService

authorizations = {
    "jsonWebToken" : {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

api = Namespace('assignments', description='Assignment operations', authorizations=authorizations)

question_model = api.model('Question', {
    'question_id': fields.Integer(readonly=True),
    'question_text': fields.String(required=True),
    'option_a': fields.String(required=True),
    'option_b': fields.String(required=True),
    'option_c': fields.String(required=True),
    'option_d': fields.String(required=True)
})

assignment_model = api.model('Assignment', {
    'assignment_id': fields.Integer(readonly=True),
    'questions': fields.List(fields.Nested(question_model))
})

all_assignments_model = api.model('AllAssignments', {
    # this model is used to return all assignments for a course
    'week_number': fields.Integer,
    'assignments': fields.List(fields.Nested(assignment_model))
})

submission_model = api.model('Submission', {
    'assignment_id': fields.Integer(required=True),
    'answers': fields.Raw(required=True) # e.g., {"1": "a", "2": "b", ...}
    # answers is a dictionary of question_id and the selected option
})

submission_answer_model = api.model('SubmissionAnswer', {
    'question_id': fields.Integer(readonly=True),
    'chosen_answer': fields.String(readonly=True),
    'is_correct': fields.Boolean(readonly=True)
})

grade_model = api.model('Grade', {
    'grade_id': fields.Integer(readonly=True),
    'student_id': fields.Integer(required=True),
    'assignment_id': fields.Integer(required=True),
    'score': fields.Float(required=True)
})

@api.route('/course/<string:course_id>')
class AssignmentList(Resource):
    @api.marshal_list_with(all_assignments_model)
    @jwt_required()
    @api.doc(security="jsonWebToken")
    def get(self, course_id):
        """Fetch all the assignments for a specific course grouped by week"""
        course = CourseService.get_course_by_id(course_id)

        if not course:
            api.abort(404, "Course not found")

        assignments = AssignmentService.get_all_assignments_by_course(course_id)

        if not assignments:
            api.abort(404, "No assignments found for this course")
        return assignments

@api.route('/course/<string:course_id>/week/<int:week_number>')
class AssignmentList(Resource):
    @api.marshal_list_with(assignment_model)
    @jwt_required()
    @api.doc(security="jsonWebToken")
    def get(self, course_id, week_number):
        """Fetch assignments for a specific week of a course"""
        course = CourseService.get_course_by_id(course_id)

        if not course:
            api.abort(404, "Course not found")

        assignments = AssignmentService.get_assignments_by_course_and_week(course_id, week_number)

        if not assignments:
            api.abort(404, "No assignments found for this week")
        return assignments

@api.route('/submit')
class SubmitAssignment(Resource):
    @api.expect(submission_model)
    @api.marshal_with(grade_model)
    @jwt_required()
    @api.doc(security="jsonWebToken")
    def post(self):
        """Submit an assignment"""
        student_id = get_jwt_identity()
        assignment_id = api.payload['assignment_id']
        answers = api.payload['answers']

        if not AssignmentService.assignment_exists(assignment_id):
            api.abort(404, "Assignment not found")

        # Check if the student has already submitted the assignment
        grade = AssignmentService.get_grade_by_assignment(student_id, assignment_id)

        if grade:
            api.abort(400, "Assignment already submitted")

        return AssignmentService.submit_assignment(student_id, assignment_id, answers), 201
    
@api.route('/submission/<int:assignment_id>')
class StudentSubmission(Resource):
    @api.marshal_list_with(submission_answer_model)
    @jwt_required()
    @api.doc(security="jsonWebToken")
    def get(self, assignment_id):
        """Fetch a student's submitted answers for a specific assignment"""
        student_id = get_jwt_identity()

        if not AssignmentService.assignment_exists(assignment_id):
            api.abort(404, "Assignment not found")

        submission = AssignmentService.get_student_submission(student_id, assignment_id)
        if submission:
            return submission
        api.abort(404, "No submission found for this assignment")

@api.route('/course/<string:course_id>/grades')
class CourseGrades(Resource):
    @api.marshal_list_with(grade_model)
    @jwt_required()
    @api.doc(security="jsonWebToken")
    def get(self, course_id):
        """Fetch all the grades for a specific course"""
        student_id = get_jwt_identity()

        course = CourseService.get_course_by_id(course_id)

        if not course:
            api.abort(404, "Course not found")

        grades = AssignmentService.get_all_grades_by_course(student_id, course_id)
        return grades

@api.route('/grade/<int:assignment_id>')
class AssignmentGrade(Resource):
    @api.marshal_with(grade_model)
    @jwt_required()
    @api.doc(security="jsonWebToken")
    def get(self, assignment_id):
        """Fetch current user's grade for a specific assignment"""
        student_id = get_jwt_identity()
        grade = AssignmentService.get_grade_by_assignment(student_id, assignment_id)
        if grade:
            return grade
        api.abort(404, "Grade not found for this assignment")