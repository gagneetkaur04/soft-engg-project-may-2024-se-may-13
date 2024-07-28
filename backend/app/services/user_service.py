from app.models import Student, Course
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    @staticmethod
    def create_user(first_name, last_name, email, password):

        # Check if user with this email already exists & disallow registration in that case
        if UserService.get_user_by_email(email):
            return None

        hashed_pw = generate_password_hash(password)
        student = Student(first_name=first_name, last_name=last_name, email=email, hashed_pw=hashed_pw)
        
        db.session.add(student)

        # enroll the newly registered student in default courses
        python = Course.query.get('CS1002')
        stats1 = Course.query.get('MA1002')
        mlt = Course.query.get('CS2007')
        default_courses = [python, stats1, mlt]
        student.courses.extend(default_courses)

        db.session.commit()
        return student

    @staticmethod
    def get_user_by_id(student_id):
        return Student.query.filter_by(student_id=student_id).first()
    
    @staticmethod
    def get_user_by_email(email):
        return Student.query.filter_by(email=email).first()

    @staticmethod
    def check_password(student, password):
        return check_password_hash(student.hashed_pw, password)