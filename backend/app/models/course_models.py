from app import db

class Instructor(db.Model):
    __tablename__ = 'instructors'
    instructor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    courses = db.relationship('Course', backref='instructor', lazy=True)


class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.instructor_id'), nullable=False)
    course_contents = db.relationship('CourseContent', backref='course', lazy=True)
    assignments = db.relationship('Assignment', backref='course', lazy=True)


class CourseContent(db.Model):
    __tablename__ = 'course_content'
    content_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String, db.ForeignKey('courses.course_id'), nullable=False)
    week_number = db.Column(db.Integer, nullable=False)
    lecture_url = db.Column(db.String(255), nullable=False)
    lecture_title = db.Column(db.String(200), nullable=False)
    transcript_url = db.Column(db.String(255), nullable=True)


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), primary_key=True)
    course_id = db.Column(db.String, db.ForeignKey('courses.course_id'), primary_key=True)
