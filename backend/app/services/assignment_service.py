from app.models import Assignment, AssignmentQuestion, Grade
from app import db

class AssignmentService:
    @staticmethod
    def assignment_exists(assignment_id):
        return Assignment.query.get(assignment_id) is not None
    
    @staticmethod
    def get_assignments_by_course_and_week(course_id, week_number):
        assignments = Assignment.query.filter_by(course_id=course_id, week_number=week_number).all()
        result = []
        for assignment in assignments:
            questions = AssignmentQuestion.query.filter_by(assignment_id=assignment.assignment_id).all()
            assignment_data = {
                'assignment_id': assignment.assignment_id,
                'questions': [{
                    'question_id': q.question_id,
                    'question_text': q.question_text,
                    'options': {
                        'a': q.option_a,
                        'b': q.option_b,
                        'c': q.option_c,
                        'd': q.option_d
                    }
                } for q in questions]
            }
            result.append(assignment_data)
        return result
    
    @staticmethod
    def get_all_assignments_by_course(course_id):
        assignments = Assignment.query.filter_by(course_id=course_id).all()
        result = []

        # find the number of weeks in the course, 
        # it will be the maximum week number of all assignments
        # can find using SQLAlchemy order_by

        max_week = Assignment.query.filter_by(course_id=course_id).order_by(Assignment.week_number.desc()).first().week_number
        # print(max_week)

       # now we can use the above function get_assignments_by_course_and_week 
       # to get assignments for each week by looping through the weeks
       # combine them together to construct the response

        for week_number in range(1, max_week + 1):
            assignments = AssignmentService.get_assignments_by_course_and_week(course_id, week_number)
            week_wise_assignments = {
                'week_number': week_number,
                'assignments': assignments
            }
            result.append(week_wise_assignments)

        return result

    @staticmethod
    def submit_assignment(student_id, assignment_id, answers):
        questions = AssignmentQuestion.query.filter_by(assignment_id=assignment_id).all()
        correct_count = 0
        for question in questions:
            if str(question.question_id) in answers and answers[str(question.question_id)] == question.correct_option:
                correct_count += 1
        
        score = (correct_count / len(questions)) * 100
        grade = Grade(student_id=student_id, assignment_id=assignment_id, score=round(score, 2))
        db.session.add(grade)
        db.session.commit()
        return grade
    
    @staticmethod
    def get_all_grades_by_course(student_id, course_id):
        return db.session.query(Grade).join(Assignment).filter(Grade.student_id==student_id, Assignment.course_id==course_id).all()

    @staticmethod
    def get_grade_by_assignment(student_id, assignment_id):
        return Grade.query.filter_by(student_id=student_id, assignment_id=assignment_id).first()
