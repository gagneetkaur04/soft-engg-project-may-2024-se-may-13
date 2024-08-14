import json
from app.models import CourseContent, Instructor, Course
from .assignment_data import insert_default_assignments_mlt, insert_default_assignments_stats
from .prog_assignment_data import insert_default_programming_assignments

from app import db

def insert_course_contents_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    course_id = data['course_id']
    week_wise = data['week_wise']

    for week in week_wise:
        week_number = int(week['title'].split(' ')[1])
        for video in week['videos']:
            lecture_url = f"https://www.youtube.com/watch?v={video['yt_vid']}"
            lecture_title = video['title']
            transcript_url = video.get('transcript_vtt_url')

            course_content = CourseContent(
                course_id=course_id,
                week_number=week_number,
                lecture_url=lecture_url,
                lecture_title=lecture_title,
                transcript_url=transcript_url
            )

            db.session.add(course_content)
    
    db.session.commit()

def insert_default_instructors():
    prof_sudarshan = Instructor(first_name='Sudarshan', last_name='Iyengar', email='sudarshan@iitrpr.ac.in')
    prof_usha = Instructor(first_name='Usha', last_name='Mohan', email='ushamohan@iitm.ac.in')
    prof_arun = Instructor(first_name='Arun', last_name='Rajkumar', email='arunr@cse.iitm.ac.in')

    db.session.add_all([prof_sudarshan, prof_usha, prof_arun])
    db.session.commit()

def get_instructor_by_email(email):
    return Instructor.query.filter_by(email=email).first()

def insert_default_courses():
    prof_sudarshan = get_instructor_by_email('sudarshan@iitrpr.ac.in')
    prof_usha = get_instructor_by_email('ushamohan@iitm.ac.in')
    prof_arun = get_instructor_by_email('arunr@cse.iitm.ac.in')

    intro_python = Course(course_id='CS1002', title='Programming in Python', instructor_id=prof_sudarshan.instructor_id)
    stats1 = Course(course_id='MA1002', title='Statistics for Data Science I', instructor_id=prof_usha.instructor_id)
    mlt = Course(course_id='CS2007', title='Machine Learning Techniques', instructor_id=prof_arun.instructor_id)

    db.session.add_all([intro_python, stats1, mlt])
    db.session.commit()

def initialize_db_and_data():
    db.create_all()
    insert_default_instructors()
    insert_default_courses()
    insert_default_assignments_mlt()
    insert_default_assignments_stats()
    insert_default_programming_assignments()
    insert_course_contents_from_json('app/utils/data/cs1002.json')
    insert_course_contents_from_json('app/utils/data/ma1002.json')
    insert_course_contents_from_json('app/utils/data/cs2007.json')
    print('Database initialized with default data')