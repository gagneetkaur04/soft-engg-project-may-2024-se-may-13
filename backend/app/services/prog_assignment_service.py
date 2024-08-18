from app import db
from app.models import ProgrammingAssignment, ProgrammingSubmission, TestCase
from app.utils import execute_code

class ProgrammingAssignmentService:

    @staticmethod
    def get_all_assignments():
        return ProgrammingAssignment.query.all()
    
    @staticmethod
    def get_assignment(assignment_id):
        return ProgrammingAssignment.query.get(assignment_id)

    @staticmethod
    def get_submission_by_student(assignment_id, student_id):
        return ProgrammingSubmission.query.filter_by(prog_assignment_id=assignment_id, student_id=student_id).first()

    @staticmethod
    def submit_assignment(assignment_id, student_id, code):

        # Run test cases and calculate score
        test_cases = TestCase.query.filter_by(prog_assignment_id=assignment_id).all()
        total_cases = len(test_cases)
        passed_cases = 0

        for test_case in test_cases:
            # Execute user's code with the test case input
            result = execute_code(code, test_case.input_data)
            if "error" in result:
                # Handle error in user's code
                return {"error": result["error"]}
            
            if result["output"].strip() == test_case.expected_output.strip():
                passed_cases += 1

        score = (passed_cases / total_cases) * 100 if total_cases > 0 else 0

        # Save the submission
        submission = ProgrammingSubmission(
            prog_assignment_id=assignment_id,
            student_id=student_id,
            code=code
        )
        db.session.add(submission)
        submission.score = score
        db.session.commit()

        return submission

    @staticmethod
    def get_all_submissions_by_student(student_id):
        return ProgrammingSubmission.query.filter_by(student_id=student_id).all()