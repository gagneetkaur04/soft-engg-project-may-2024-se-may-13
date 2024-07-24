from app import db

class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_pw = db.Column(db.String(255), nullable=False)
    notes = db.relationship('Note', backref='student', lazy=True)
    conversations = db.relationship('Conversation', backref='student', lazy=True)
    courses = db.relationship('Course', secondary='enrollments', backref='students')
    grades = db.relationship('Grade', backref='student', lazy=True)
    submission_answers = db.relationship('SubmissionAnswer', backref='student', lazy=True)
