from app.models import Note
from app import db

class NoteService:
    @staticmethod
    def create_note(student_id, note_content):
        note = Note(student_id=student_id, note_content=note_content)
        db.session.add(note)
        db.session.commit()
        return note

    @staticmethod
    def get_notes_by_student_id(student_id):
        return Note.query.filter_by(student_id=student_id).all()
    