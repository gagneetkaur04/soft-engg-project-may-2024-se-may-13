from app import db
from datetime import datetime

class Note(db.Model):
    __tablename__ = 'notes'
    note_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    note_content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    modified_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())


class ChatHistory(db.Model):
    __tablename__ = 'chat_history'
    conversation_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    sender = db.Column(db.String, nullable=False)