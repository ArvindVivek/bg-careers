from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def generate_summary(photos):
    content_arr = [
        {
            "type": "text",
            "text": "Respond with no formatting. I am applying to design, UI/UX and product roles with these designs. I would like a summary of my work to include in my portfolio. Here are some of my designs: ",
        },
    ]

    for photo in photos:
        content_arr.append({
            "type": "image_url",
            "image_url": {
                "url": photo,
            },
        })

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": content_arr,
            }
        ],
        max_tokens=100,
    )
    summary = response.choices[0].message.content

    return summary

def generate_resume_overview(resume):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful design/UI/UX/product hiring assistant. Respond with no formatting."},
            {"role": "user", "content": f"I am applying to design, UI/UX and product roles with this resume, give me the types of jobs specific for me based on my resume: {resume}"}
        ],
        max_tokens=50,
    )

    overview = response.choices[0].message.content
    return overview