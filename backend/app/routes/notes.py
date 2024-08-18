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
        """Create a new note in the current user's account"""
        user_id = get_jwt_identity()
        note = NoteService.create_note(user_id, api.payload['note_content'])
        return note, 201

    @api.marshal_list_with(note_output_model)
    @api.doc(security="jsonWebToken")
    def get(self):
        """Get all notes for the current user"""
        user_id = get_jwt_identity()
        print(user_id)
        notes = NoteService.get_notes_by_student_id(user_id)
        return notes, 200
    
@api.route('/<int:note_id>')
@api.param('note_id', 'The note identifier')
class Note(Resource):

    method_decorators = [jwt_required()]
    
    @api.marshal_with(note_output_model)
    @api.doc(security="jsonWebToken")
    def get(self, note_id):
        """Fetch a note given its ID"""
        note = NoteService.get_note_by_id(note_id)
        student_id = get_jwt_identity()

        if not note:
            api.abort(404, f'Note with ID: {note_id} not found')
        if note.student_id != student_id:
            api.abort(403, 'Unauthorized to access this note')
        return note, 200
    
    @api.doc(security="jsonWebToken")
    @api.expect(note_input_model)
    @api.marshal_with(note_output_model)
    def put(self, note_id):
        """Update a note given its ID"""
        note = NoteService.get_note_by_id(note_id)
        student_id = get_jwt_identity()

        if not note:
            api.abort(404, f'Note with ID: {note_id} not found')
        if note.student_id != student_id:
            api.abort(403, 'Unauthorized to update this note')
        note = NoteService.update_note(note_id, api.payload['note_content'])
        return note, 200
    
    @api.doc(security="jsonWebToken")
    def delete(self, note_id):
        """Delete a note given its ID"""
        note = NoteService.get_note_by_id(note_id)
        student_id = get_jwt_identity()

        if not note:
            api.abort(404, f'Note with ID: {note_id} not found')
        if note.student_id != student_id:
            api.abort(403, 'Unauthorized to delete this note')
        NoteService.delete_note(note_id)
        return {"message": "Note deleted successfully"}, 200