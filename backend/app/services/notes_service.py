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
    
    @staticmethod
    def get_note_by_id(note_id):
        return Note.query.get(note_id)
    
    @staticmethod
    def update_note(note_id, note_content):
        note = Note.query.get(note_id)
        note.note_content = note_content
        db.session.commit()
        return note
    
    @staticmethod
    def delete_note(note_id):
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        return None # after deletion, there is no note to return