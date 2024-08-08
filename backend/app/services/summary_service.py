from app.models import CourseContent
import google.generativeai as genai
import os, requests
from dotenv import load_dotenv

class SummaryService:

    system_instruction =  """
    You are lecture summarizer. You will be given a lecture transcript and you need 
    to generate a summary for it. Make sure to generate a concise summary that captures 
    the main points of the lecture in bullet points. The summary should be no longer than 
    250-300 words.
    """

    @staticmethod
    def initialize_gemini():
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash',
                                    system_instruction=SummaryService.system_instruction)
        return model

    @staticmethod
    def fetch_lecture_transcript(content_id):
        lecture = CourseContent.query.get(content_id)
        if lecture and lecture.transcript_url:
            # make a get request to fetch the transcript from the url
            response = requests.get(lecture.transcript_url)
            if response.status_code == 200:
                return response.text
        return None
    
    @staticmethod
    def generate_summary(content_id):
        transcript = SummaryService.fetch_lecture_transcript(content_id)
        if transcript:
            model = SummaryService.initialize_gemini()
            prompt = f"""Generate a summary for the following lecture transcript: '{transcript}'."""
            response = model.generate_content(prompt)
            return {"summary" : response.text.strip()}
        return None