from app import db

class ProgrammingAssignment(db.Model):
    __tablename__ = 'programming_assignments'
    prog_assignment_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String, db.ForeignKey('courses.course_id'), nullable=False)
    title = db.Column(db.String(200), nullable=False) # title of the problem
    description = db.Column(db.Text, nullable=False) # description of the problem statement

class ProgrammingSubmission(db.Model):
    __tablename__ = 'programming_submissions'
    prog_submission_id = db.Column(db.Integer, primary_key=True)
    prog_assignment_id = db.Column(db.Integer, db.ForeignKey('programming_assignments.prog_assignment_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    code = db.Column(db.Text, nullable=False)
    score = db.Column(db.Float)

class TestCase(db.Model):
    __tablename__ = 'test_cases'
    test_case_id = db.Column(db.Integer, primary_key=True)
    prog_assignment_id = db.Column(db.Integer, db.ForeignKey('programming_assignments.prog_assignment_id'), nullable=False)
    input_data = db.Column(db.Text, nullable=False)
    expected_output = db.Column(db.Text, nullable=False)
