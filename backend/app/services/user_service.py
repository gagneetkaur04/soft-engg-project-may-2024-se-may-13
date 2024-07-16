from app.models import Student
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

        # TODO: add checks for duplicate emails and other validations, return appropriate error messages in those cases
        # TODO: enroll these students in the courses by default

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