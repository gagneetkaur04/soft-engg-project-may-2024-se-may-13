from app.models import Assignment, AssignmentQuestion, SubmissionAnswer, Grade
from app import db

class AssignmentService:
    @staticmethod
    def assignment_exists(assignment_id):
        return Assignment.query.get(assignment_id) is not None
    
    @staticmethod
    def get_assignments_by_course_and_week(course_id, week_number):
        return Assignment.query.filter_by(course_id=course_id, week_number=week_number).all()
    
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
        assignment = Assignment.query.get(assignment_id)
        total_questions = len(assignment.questions)
        correct_answers = 0

        # remember answers is a dict of question_id, answer pairs
        # like {"1": "a", "2": "b", ...}
        for question_id, chosen_answer in answers.items():
            question = AssignmentQuestion.query.get(question_id)
            is_correct = (chosen_answer == question.correct_option)
            if is_correct:
                correct_answers += 1

            submission = SubmissionAnswer(
                student_id=student_id,
                question_id=question_id,
                chosen_answer=chosen_answer,
                is_correct=is_correct
            )
            db.session.add(submission)

        score = (correct_answers / total_questions) * 100
        grade = Grade(student_id=student_id, assignment_id=assignment_id, score=score)
        db.session.add(grade)
        db.session.commit()

        return grade
    
    @staticmethod
    def get_student_submission(student_id, assignment_id):
        assignment = Assignment.query.get(assignment_id)

        submission = SubmissionAnswer.query.join(AssignmentQuestion).filter(
            SubmissionAnswer.student_id == student_id,
            AssignmentQuestion.assignment_id == assignment_id
        ).all()

        return submission

    @staticmethod
    def get_all_grades_by_course(student_id, course_id):
        return db.session.query(Grade).join(Assignment).filter(Grade.student_id==student_id, Assignment.course_id==course_id).all()

    @staticmethod
    def get_grade_by_assignment(student_id, assignment_id):
        return Grade.query.filter_by(student_id=student_id, assignment_id=assignment_id).first()
