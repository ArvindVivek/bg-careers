import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(photo):
    response = openai.Completion.create(
        engine='davinci',
        prompt=f"Summarize the content in this design UI/UX photo: {photo}",
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop=None
    )
    summary = response.choices[0].text.strip()
    return summary

def generate_resume_overview(resume):
    response = openai.Completion.create(
        engine='davinci',
        prompt=f"Generate an overview of the content in this resume with highlighted skills/experience in design: {resume}",
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop=None
    )
    overview = response.choices[0].text.strip()
    return overview