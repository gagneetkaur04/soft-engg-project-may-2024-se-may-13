import json
from app.models import CourseContent

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
