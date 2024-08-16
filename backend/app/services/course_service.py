from app.models import Course, Student, CourseContent
from app import db

class CourseService:
    @staticmethod
    def get_enrolled_courses(student_id):
        student = Student.query.get(student_id)
        return student.courses

    @staticmethod
    def get_course_by_id(course_id):
        return Course.query.get(course_id)

    @staticmethod
    def get_course_contents(course_id):
        course = Course.query.get(course_id)
        if not course:
            return None
        
        contents = CourseContent.query.filter_by(course_id=course_id).order_by(CourseContent.week_number).all()
        
        # Group contents by week
        content_by_week = {}
        for content in contents:
            if content.week_number not in content_by_week:
                content_by_week[content.week_number] = []
            content_by_week[content.week_number].append({
                'content_id': content.content_id,
                'lecture_title': content.lecture_title,
                'lecture_url': content.lecture_url,
                'transcript_url': content.transcript_url
            })
        
        # Format the result
        result = {
            'course_id': course.course_id,
            'course_title': course.title,
            'weeks': [
                {
                    'week_number': week,
                    'contents': week_contents
                }
                for week, week_contents in content_by_week.items()
            ]
        }
        return result
    
    @staticmethod
    def get_course_content_by_id(course_id, content_id):
        content = CourseContent.query.get(content_id)
        
        # Make sure the content belongs to that specific course
        if content and content.course_id == course_id:
            return content
        return None