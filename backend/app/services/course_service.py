import os
import google.generativeai as genai
from app.models import Course, Student, CourseContent
from app import db
from dotenv import load_dotenv

class CourseService:
    system_instruction =  """
    You are a bot in a Learning Management System. You job is to generate the detailed course 
    highlights of a given course. You will be given the course title and the lecture titles
    for that course in a week-by-week format. Using this information, you need to generate the
    course highlights in a bullet-point format. Make sure to include the main topics covered in
    each week and the key takeaways from the course. The course highlights should be no longer
    than 500-600 words.
    """

    @staticmethod
    def initialize_gemini():
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash',
                                    system_instruction=CourseService.system_instruction)
        return model
    
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
    
    @staticmethod
    def generate_course_highlights(course_id):
        course_contents = CourseService.get_course_contents(course_id)
        if not course_contents:
            return None
        
        model = CourseService.initialize_gemini()
        prompt = f"""Generate the course highlights for the following course: '{course_contents['course_title']}'. 
        The course contains the following weeks and their contents: {course_contents['weeks']}."""

        response = model.generate_content(prompt)
        return {"highlights" : response.text.strip()}