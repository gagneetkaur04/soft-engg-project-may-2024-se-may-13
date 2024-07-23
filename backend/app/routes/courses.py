from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.course_service import CourseService

authorizations = {
    "jsonWebToken" : {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

api = Namespace('courses', description='Course operations', authorizations=authorizations)

instructor_model = api.model('Instructor', {
    'instructor_id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String
})

course_model = api.model('Course', {
    'course_id': fields.String,
    'title': fields.String,
    'instructor': fields.Nested(instructor_model)
})

course_content_model = api.model('CourseContent', {
    'content_id': fields.Integer,
    'lecture_title': fields.String,
    'lecture_url': fields.String,
    'transcript_url': fields.String
})

week_model = api.model('Week', {
    'week_number': fields.Integer,
    'contents': fields.List(fields.Nested(course_content_model))
})

course_contents_list = api.model('CourseContentsList', {
    'course_id': fields.String,
    'course_title': fields.String,
    'weeks': fields.List(fields.Nested(week_model))
})

@api.route('/')
class CourseList(Resource):

    @api.marshal_list_with(course_model)
    @api.doc(security="jsonWebToken")
    @jwt_required()
    def get(self):
        """List all courses the student is enrolled in"""
        user_id = get_jwt_identity()
        return CourseService.get_enrolled_courses(user_id)


@api.route('/<string:id>')
@api.param('id', 'The course identifier')
class Course(Resource):

    @api.marshal_with(course_model)
    @api.doc(security="jsonWebToken")
    @jwt_required()
    def get(self, id):
        """Fetch a course given its identifier"""
        course = CourseService.get_course_by_id(id)
        if course:
            return course
        api.abort(404, "Course {} doesn't exist".format(id))


@api.route('/<string:id>/contents')
@api.param('id', 'The course identifier')
class CourseContents(Resource):
    @api.marshal_with(course_contents_list)
    @api.doc(security="jsonWebToken")
    @jwt_required()
    def get(self, id):
        """Fetch all contents of a specific course"""
        user_id = get_jwt_identity()
        
        course_contents = CourseService.get_course_contents(id)
        if course_contents:
            return course_contents
        api.abort(404, f"Course {id} doesn't exist or has no content")