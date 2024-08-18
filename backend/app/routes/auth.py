from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import UserService

api = Namespace('auth', description='Authentication operations')

user_registration_model = api.model('Student Registration', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
})

user_login_model = api.model('Student Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

user_model = api.model('Student', {
    'student_id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String
})

@api.route('/register')
class Register(Resource):
    @api.expect(user_registration_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Register a new user"""
        user = UserService.create_user(**api.payload)
        if not user:
            api.abort(400, 'User with this email already exists')
        else:
            return user, 201

@api.route('/login')
class Login(Resource):
    @api.expect(user_login_model)
    def post(self):
        """Login and receive JWT token"""
        user = UserService.get_user_by_email(api.payload['email'])
        if user and UserService.check_password(user, api.payload['password']):
            access_token = create_access_token(identity=user.student_id)
            return {'access_token': access_token}, 200
        api.abort(401, 'Invalid credentials')