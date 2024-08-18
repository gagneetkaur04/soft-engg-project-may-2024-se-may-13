from app import db

class Assignment(db.Model):
    __tablename__ = 'assignments'
    assignment_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String, db.ForeignKey('courses.course_id'), nullable=False)
    week_number = db.Column(db.Integer, nullable=False)
    questions = db.relationship('AssignmentQuestion', backref='assignment', lazy=True)

class AssignmentQuestion(db.Model):
    __tablename__ = 'assignment_questions'
    question_id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.assignment_id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)

class SubmissionAnswer(db.Model):
    __tablename__ = 'submission_answers'
    submission_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('assignment_questions.question_id'), nullable=False)
    chosen_answer = db.Column(db.String(1), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)

class Grade(db.Model):
    __tablename__ = 'grades'
    grade_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.assignment_id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)