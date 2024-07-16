from flask_restx import Namespace, Resource, fields
from app.services import NoteService
from flask_jwt_extended import jwt_required, get_jwt_identity

authorizations = {
    "jsonWebToken" : {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

api = Namespace('notes', description='Note operations', authorizations=authorizations)

note_input_model = api.model('Note Input', {
    # 'student_id': fields.Integer(required=True), # student_id isn't required because we can get it from the jwt token
    'note_content': fields.String(required=True)
})

note_output_model = api.model('Note Output', {
    'note_id': fields.Integer,
    'student_id': fields.Integer,
    'note_content': fields.String,
    'created_at': fields.DateTime,
    'modified_at': fields.DateTime
})


@api.route('/')
class Notes(Resource):
    # this will mandate the jwt token for all the methods in this class
    method_decorators = [jwt_required()]

    @api.expect(note_input_model)
    @api.marshal_with(note_output_model, code=201)
    @api.doc(security="jsonWebToken")
    def post(self):
        """Create a new note"""
        user_id = get_jwt_identity()
        note = NoteService.create_note(user_id, api.payload['note_content'])
        return note, 201

    @api.marshal_list_with(note_output_model)
    @api.doc(security="jsonWebToken")
    def get(self):
        """Get all notes"""
        user_id = get_jwt_identity()
        print(user_id)
        notes = NoteService.get_notes_by_student_id(user_id)
        return notes, 200